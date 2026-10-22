#!/usr/bin/env python3
"""Write config/pt-ids.txt: the ids of the Portuguese repo (LawAgents/pt), used to link directives to the Portuguese acts
that transpose them (EU-LAW.xml eu.rule.transposition). Reads the index shards of the Portuguese repo, read-only.

  python scripts/gen_pt_ids.py --from-dir PATH_TO_CHECKOUT [--out config/pt-ids.txt]
  python scripts/gen_pt_ids.py --from-url https://raw.githubusercontent.com/LawAgents/pt/main/ [--out ...]

The first form reads indice-*.md in a checkout; the second fetches indice.md and the shards it lists (GitHub only,
so CI can refresh the list without a clone). One id per line, sorted.
"""
import argparse
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import USER_AGENT, atomic_write  # noqa: E402

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "config" / "pt-ids.txt"
SKIP = {"indice.md", "indice-temas.md"}


def ids_from_shard(text):
    """First cell of every table row that looks like an id (lowercase letters, digits and hyphens)."""
    out = set()
    for ln in text.splitlines():
        if ln.startswith("| "):
            first = ln.split("|")[1].strip()
            if re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)+", first):
                out.add(first)
    return out


def from_dir(path):
    ids = set()
    for p in sorted(Path(path).glob("indice-*.md")):
        if p.name not in SKIP:
            ids |= ids_from_shard(p.read_text(encoding="utf-8"))
    return ids


def from_url(base):
    base = base.rstrip("/") + "/"

    def get(name):
        req = urllib.request.Request(base + name, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8")

    names = re.findall(r"\| (indice-[a-z0-9-]+\.md) \|", get("indice.md"))
    ids = set()
    for n in names:
        if n not in SKIP:
            ids |= ids_from_shard(get(n))
    return ids


def main(argv=None):
    ap = argparse.ArgumentParser(description="Write config/pt-ids.txt from the index of the Portuguese repo.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--from-dir", help="checkout of LawAgents/pt (reads indice-*.md)")
    src.add_argument("--from-url", help="raw base URL of LawAgents/pt (fetches indice.md and its shards)")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args(argv)
    ids = from_dir(a.from_dir) if a.from_dir else from_url(a.from_url)
    if not ids:
        print("no ids found: refusing to write an empty list", file=sys.stderr)
        return 1
    atomic_write(a.out, "\n".join(sorted(ids)) + "\n")
    print(f"{len(ids)} ids written to {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
