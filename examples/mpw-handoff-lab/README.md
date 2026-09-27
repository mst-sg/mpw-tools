# MPW handoff teaching lab

MST-created synthetic geometry and exercises. MIT licensed. Not a PDK, electrical design or foundry submission. No DRC/LVS has been run; JSON files are fictional report-metadata summaries.

## Run without extra dependencies
Unzip this package. In its directory run `python3 verify.py` (or `python verify.py` on Windows). Expect checksum PASS, consistent metadata for reports-consistent.json, and two DRC mismatches for reports-stale.json (hash and revision).

## Inspect the GDS independently
`python3 -m venv .venv`

Activate that environment, install `pip install -r requirements.txt`, then run `python inspect.py`.

Both layouts: top MST_DEMO_TOP; 2 cells; DBU 0.001 micrometers; layers 1/0, 2/0, 99/0. A bounding box 100×60 micrometers; B 120×60. See expected-layouts.json. `generate.py` recreates the fixtures with timestamps disabled; do not regenerate a delivered package without updating its hashes and evidence.

## Browser exercise
https://mst-sg.com/tools/mpw-gds/

https://mst-sg.com/tools/report-revision-check/

Read handbook.html. Select layout-b.gds and compare each metadata file. A passing consistency check does not validate the source reports, approved decks, electrical correctness or foundry acceptance.

## Files
Two layouts, expected geometry JSON, consistent/stale metadata, schema template, handoff/test-plan CSV templates, Python generators/checkers, expected results, handbook and checksums. No customer material or restricted process files.
