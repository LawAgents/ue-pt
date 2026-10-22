"""Throttled client for the Publications Office of the EU: public SPARQL endpoint and Cellar REST (no key).

Rules (EU-LAW.xml eu.rule.fetch, same as the Portuguese pipeline): one global throttle (>= MIN_INTERVAL seconds
between two request STARTS; several requests may be in flight), the project User-Agent on every request, an immediate
stop after 3 consecutive errors or on HTTP 429/503. A 404 on a document is a normal answer ("no such expression"),
not an error.
"""
import http.client
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

from common import USER_AGENT

SPARQL_URL = "https://publications.europa.eu/webapi/rdf/sparql"
CELEX_URL = "https://publications.europa.eu/resource/celex/"
MIN_INTERVAL = 0.55  # 2 request starts per second at most
MAX_CONSECUTIVE_ERRORS = 3
SLOW_DOWN = (429, 503)
CDM = "http://publications.europa.eu/ontology/cdm#"
POR = "http://publications.europa.eu/resource/authority/language/POR"


class FetchAborted(Exception):
    """Too many errors or the server asked to slow down: stop everything, publish nothing."""


class ServiceChanged(FetchAborted):
    """The services answered in a shape we do not know."""


def urllib_transport(url, data, headers, timeout=None):
    """Default transport: returns (status, body). Redirects are followed (Cellar redirects once). OSError on failure."""
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout or (300 if "/sparql" in url else 120)) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() or b""
    except urllib.error.URLError as e:
        raise OSError(str(e.reason)) from e
    except http.client.HTTPException as e:
        raise OSError(f"{type(e).__name__}: {e}") from e


class Cellar:
    def __init__(self, transport=urllib_transport, clock=time.monotonic, sleep=time.sleep,
                 min_interval=MIN_INTERVAL, user_agent=USER_AGENT, log=None):
        self._transport, self._clock, self._sleep = transport, clock, sleep
        self.min_interval, self.user_agent = min_interval, user_agent
        self._log = log or (lambda msg: print(msg, file=sys.stderr))
        # A new client waits one interval before its first request, so two runs started back to back keep the rate.
        self._next_start = clock() + min_interval
        self._lock = threading.Lock()
        self.aborted = False
        self.errors_in_row = 0
        self.requests = 0

    def _request(self, url, headers=None, ok_statuses=(), pass_statuses=()):
        """One throttled GET with error accounting. Returns the body, or None when the status is in ok_statuses;
        a status in pass_statuses (HTTP 300) is a normal answer whose body is returned."""
        h = {"User-Agent": self.user_agent}
        h.update(headers or {})
        with self._lock:
            if self.aborted:
                raise FetchAborted("aborted by another request")
            now = self._clock()
            start = max(now, self._next_start)
            self._next_start = start + self.min_interval
            self.requests += 1
        if start > now:
            self._sleep(start - now)
        try:
            status, body = self._transport(url, None, h)
            err = None if status == 200 or status in pass_statuses else f"HTTP {status}"
        except OSError as e:
            status, body, err = None, b"", f"network error: {e}"
        with self._lock:
            if err is None:
                self.errors_in_row = 0
                return body
            if status in ok_statuses:
                self.errors_in_row = 0   # the server answered normally: there is just no such document
                return None
            self.errors_in_row += 1
            errors_in_row = self.errors_in_row
        self._log(f"request failed ({err}) for {url[:160]}")
        if status in SLOW_DOWN:
            self.aborted = True
            raise FetchAborted(f"{err} for {url[:120]}: the server asked to slow down")
        if errors_in_row >= MAX_CONSECUTIVE_ERRORS:
            self.aborted = True
            raise FetchAborted(f"{errors_in_row} consecutive errors, last: {err} for {url[:120]}")
        return self._request(url, headers, ok_statuses, pass_statuses)

    # ---- SPARQL -------------------------------------------------------------------------------------

    def sparql(self, query):
        """Bindings of a SELECT query as a list of {var: value}."""
        url = SPARQL_URL + "?" + urllib.parse.urlencode({"query": query})
        body = self._request(url, {"Accept": "application/sparql-results+json"})
        try:
            rows = json.loads(body)["results"]["bindings"]
            return [{k: v["value"] for k, v in r.items()} for r in rows]
        except (ValueError, KeyError, TypeError) as e:
            raise ServiceChanged("SPARQL answer has an unknown shape") from e

    def sparql_paged(self, template, key="celex", page=10000):
        """Run `template` (with @last@ and @limit@ placeholders) page by page, by key: FILTER(STR(?key) > last)
        ORDER BY ?key. OFFSET above 10,000 fails on this server and GROUP BY/MAX returns partial results."""
        out, last = [], ""
        while True:
            rows = self.sparql(template.replace("@last@", last.replace("'", "")).replace("@limit@", str(page)))
            out += rows
            if len(rows) < page:
                return out
            last = rows[-1][key]

    # ---- documents ----------------------------------------------------------------------------------

    def xhtml(self, celex):
        """Portuguese XHTML text of a CELEX document, or None when there is none (404)."""
        return self.xhtml_with_notes(celex)[0]

    def xhtml_with_notes(self, celex):
        """(text or None, notes). When the manifestation has several items, Cellar answers HTTP 300 with a list of them:
        the text items (html/xhtml) are fetched in stream order and joined into one document; other media types
        (images, pdf, zip) are skipped and named in the notes."""
        headers = {"Accept": "application/xhtml+xml", "Accept-Language": "por"}
        body = self._request(CELEX_URL + celex, headers, ok_statuses=(404, 406), pass_statuses=(300,))
        if body is None:
            return None, []
        text = self._decode(body, celex)
        if not text.lstrip().startswith("<html><head><title>300 Multiple-Choice"):
            return text, []
        items = parse_items(text)
        notes, parts = [], []
        for order, href, name in items:
            if not name.lower().endswith((".html", ".htm", ".xhtml")):
                notes.append(f"item {order} ({name}) skipped: not a text item")
                continue
            part = self._request(href.replace("http://", "https://", 1), headers, ok_statuses=(404,))
            if part is None:
                notes.append(f"item {order} ({name}) skipped: HTTP 404")
                continue
            parts.append(self._decode(part, celex))
        if not parts:
            return None, notes + ["300 answer without a text item"]
        return merge_xhtml(parts), notes

    @staticmethod
    def _decode(body, celex):
        try:
            return body.decode("utf-8")
        except UnicodeDecodeError as e:
            raise ServiceChanged(f"{celex}: the answer is not UTF-8") from e


def parse_items(text):
    """[(order, url, stream name)] of the items listed in a Cellar 300 answer, in stream order."""
    out = []
    for chunk in text.split('<li title="item">')[1:]:
        href = re.search(r'href="([^"]+)"', chunk)
        name = re.search(r'title="stream_name">([^<]*)<', chunk)
        order = re.search(r'title="stream_order"[^>]*>(\d+)<', chunk)
        if href and name:
            out.append((int(order.group(1)) if order else len(out) + 1, href.group(1), name.group(1)))
    return sorted(out)


def merge_xhtml(parts):
    """One document from several: the first one whole, the body content of the others added before its </body>."""
    if len(parts) == 1:
        return parts[0]
    extra = []
    for p in parts[1:]:
        m = re.search(r"<body[^>]*>(.*)</body>", p, re.S | re.I)
        extra.append(m.group(1) if m else p)
    first = parts[0]
    i = first.lower().rfind("</body>")
    joined = chr(10).join(extra)
    return first[:i] + joined + chr(10) + first[i:] if i >= 0 else first + joined
