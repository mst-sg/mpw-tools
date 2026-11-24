"""Export the published 2027 MPW milestones without changing their date precision."""
import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASENAME = "2027-mpw-schedules"
COLUMNS = (
    "route", "foundry", "node_nm", "milestone", "date", "date_granularity",
    "status", "source_publisher", "source_url", "source_verified_on",
)
LABELS = {
    "shuttle_window": "Planning window",
    "tapeout": "Tapeout",
    "gds_submission": "GDS submission deadline",
    "tape_in": "Tape-in",
}


def render(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    lines = [
        "# Selected 2027 mature-node MPW shuttle milestones",
        "",
        "MST publishes month-level HHGrace planning windows. Europractice and X-FAB "
        "publish dated milestones for specific runs. The dates below are public planning "
        "references. Ask the provider about your process options, eligibility and allocation.",
        "",
        "| Route | Foundry | Node | Milestone | Published date | Status | Source | Source checked |",
        "| --- | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        source = f"[{row['source_publisher']}]({row['source_url']})"
        cells = (row["route"], row["foundry"], f"{row['node_nm']} nm", LABELS[row["milestone"]],
                 row["date"], row["status"], source, row["source_verified_on"])
        lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |")
    lines.extend([
        "",
        "[CSV](2027-mpw-schedules.csv) · [JSON](2027-mpw-schedules.json) · "
        "[MSTchip planning guide](https://mstchip.com/mpw/guides/2027-mature-node-mpw-schedule)",
    ])
    return {"csv": stream.getvalue(), "md": "\n".join(lines) + "\n"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report stale exports without writing.")
    args = parser.parse_args()
    rows = json.loads((ROOT / f"{BASENAME}.json").read_text(encoding="utf-8"))["schedules"]
    for extension, contents in render(rows).items():
        path = ROOT / f"{BASENAME}.{extension}"
        expected = contents.encode("utf-8")
        if args.check:
            if not path.is_file() or path.read_bytes() != expected:
                parser.exit(1, f"{path.name} needs regeneration\n")
        else:
            path.write_bytes(expected)


if __name__ == "__main__":
    main()
