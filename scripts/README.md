# Pipeline scripts (ue-pt)

Python 3.12+, standard library only. Every script has `--help`. Tests: `python -m unittest discover -s scripts/tests`.
Contract: `spec/EU-LAW.xml` of the Portuguese repo (decisions, schema, rules). Same CLI and exit codes as the Portuguese pipeline.

| Script | What it does |
|---|---|
| `run_update.py --mode initial\|weekly --raw DIR --repo DIR [--budget-seconds N] [--workers N]` | fetch, convert, validate, index and size check in a staging dir (`DIR/stage`), then replaces the repo files. `--config DIR` (default `REPO/config`), `--max-part-kb`. |
| `fetch.py --mode ... --raw DIR [--budget-seconds N] [--workers 8] [--repo DIR]` | lists by SPARQL, downloads the Portuguese XHTML into the raw cache. With `--repo`: weekly mode skips acts the repo already holds, and acts that left force get an end-of-validity date. |
| `convert.py --raw DIR --out DIR [--repo DIR] [--config DIR] [--max-part-kb 70]` | XHTML to markdown (ids, front matter, parts, transposition section). Acts without a raw record are copied from `--repo`. |
| `validate.py --root DIR [--raw DIR] [--config DIR] [--json OUT]` | blocking errors and warnings as JSON; exit 1 on any blocking error. |
| `build_index.py --root DIR --config DIR` | `nomes-comuns.md`, `indice.md`, `indice-regulamentos*.md`, `indice-diretivas*.md` (at most 40 KB each), `revogados.md`. |
| `check_size.py --repo DIR [--tree DIR]` | prints git objects and tracked tree size; exit 1 above 1 GiB. |
| `gen_pt_ids.py --from-dir CHECKOUT \| --from-url RAW_BASE [--out config/pt-ids.txt]` | writes the list of Portuguese ids (from the `indice-*.md` of LawAgents/pt) used to link directives to their Portuguese transposition acts. |

## `run_update.py` exit codes

- `0` ready to commit. Prints `CHANGED=true|false` (also appended to `$GITHUB_OUTPUT` when set).
- `2` time budget reached while fetching. The repo is untouched; run the same command again and it resumes.
- `1` failure. The repo is untouched, the error list is in `RAW/errors.json` (`{mode, stage, errors, warnings}`), a summary goes to stderr.
  Stages: `fetch`, `validate` (conversion errors too), `index`, `size`, `internal`.

Any blocking error fails the whole update. Acts without Portuguese text are not errors: they are listed in `RAW/excluded.json`.

## Fetching

- Source: `publications.europa.eu` only (SPARQL and Cellar). Lists: in-force `REG` and `DIR` (title, ELI), consolidated versions that have
  a Portuguese xhtml, originals that have one, Portuguese national implementing measures (about 10 requests in all, paged by key).
- Selection per act: the latest consolidated version dated up to today, else the original, else excluded. A document that answers 404
  falls back to the next consolidated version, then to the original.
- At most 2 request starts per second in total (also with 8 workers), `User-Agent: LawAgents-ue/0.1 (+https://github.com/LawAgents/ue-pt)`,
  stop at once after 3 consecutive errors or on HTTP 429/503. A 404 on a document is not an error.
- `initial`: every selected act without an up-to-date record in the raw cache. `weekly` (with `--repo`): the same, but an act the repo
  already holds with the same document is not downloaded again, so a week costs the list requests plus the new or re-consolidated acts.
  The raw cache is a convenience: without it, unchanged acts are copied from the repo.

## Config (`config/`)

- `nomes-comuns.txt`: `id | nome comum | sigla1, sigla2`, 30 to 50 entries, written by hand (only a test fixture ships). A missing file,
  a missing id or a wrong number of entries fails the update.
- `pt-ids.txt`: ids of the Portuguese repo, from `gen_pt_ids.py`. A transposition line gets `id: ...` only when the id is in this list.

## Layout written to the repo

`regulamentos/AAAA/regulamento-ue-AAAA-N.md` and `diretivas/AAAA/diretiva-ue-AAAA-N.md`. An act above 70 KB, or with repeated article
numbers, is split: `{type}/AAAA/{id}/{id}.md` (overview with the parts table and `## Estrutura`) plus `{id}-{part}.md`. A single article
above the cap stays whole (reported as warning `large_file`). Only these folders and the root index files are ever written or deleted.
