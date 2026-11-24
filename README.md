# MST Open Tools

Free browser tools for mature-node MPW planning, non-confidential RFQ preparation, GDSII inspection, P&ID-to-SOLIDWORKS intake, UHP gas-stick review, and sourcing cleanup.

The live tools include English and Chinese UI support. Use `?lang=zh`, `?lang=en`, or the browser language preference.

Tools with an email option can prepare a non-confidential `mailto:` brief to `sales@mst-sg.com` for you to review before sending. The hosted GDSII Inspector has a separate file submission step described below.

Built by [Moore Solution Technology Pte. Ltd.](https://mst-sg.com) (`MST`). MST supports mature-node MPW tapeout and manufacturing coordination, NeuroBox D P&ID-to-native-SOLIDWORKS assembly proposal workflows, and RFQ-based sourcing support.

MST is not a wafer foundry and does not manufacture wafers directly. These tools help engineers prepare safer first conversations before NDA, partner confirmation, and any design-detail exchange.

## Run a complete MPW handoff exercise

[Start the tutorial](https://mst-sg.com/news/gdsii-drc-lvs-requirements-for-mpw-tapeout/?utm_source=github&utm_medium=repository&utm_campaign=sg_mpw_handoff_lab) · [Read the handbook](https://mst-sg.com/tools/mpw-handoff-handbook/?utm_source=github&utm_medium=repository&utm_campaign=sg_mpw_handoff_lab) · [Browse the independent sample pack](examples/mpw-handoff-lab/)

**Input:** two MST-owned synthetic GDS revisions, report metadata and checklist templates. **Run:** `cd examples/mpw-handoff-lab && python3 verify.py`; optionally install `requirements.txt` in a virtual environment and run `python inspect.py`. **Expected output:** checksum PASS; revision B has one top cell, two cells, three layer/datatype pairs and a 120 × 60 µm bounding box. The intentionally stale DRC metadata produces two mismatches; the corrected fixture is consistent.

[Check the report revision in your browser](https://mst-sg.com/tools/report-revision-check/?utm_source=github&utm_medium=repository&utm_campaign=sg_mpw_handoff_lab). Everything in the pack is synthetic and MIT licensed. No DRC/LVS was run; matching metadata is not foundry signoff. The SG website is released from its separate canonical repository; this repository distributes public examples.

## 2027 MPW Schedule Reference

[Read the 2027 shuttle table](2027-mpw-schedules.md) · [Download the CSV](2027-mpw-schedules.csv) · [Schedule JSON](2027-mpw-schedules.json) · [JSON Schema](2027-mpw-schedules.schema.json)

Each row identifies a route, foundry, process node and milestone, with the public source and the date we checked it. Import dates at their published precision.

- `shuttle_window` uses month precision (`YYYY-MM`) for the HHGrace 55nm and 90nm windows published by MST. [MST schedule](https://mst-sg.com/mpw/)
- `tapeout` uses day precision (`YYYY-MM-DD`) for the TSMC 55nm date in Europractice's detailed schedule. [Europractice schedule](https://europractice-ic.com/wp-content/uploads/2026/11/TSMC_EP_MPW_schedule_2027_V1_0-1.pdf#page=5)
- `gds_submission` marks Europractice's UMC L180 GDS deadline. Its general MPW table calls for registration at least four weeks earlier. [Europractice 2027 general MPW schedule](https://europractice-ic.com/schedules-prices-2027-2/)
- `tape_in` is X-FAB's XT018 **Tape-In** column. The provider lists later data-release and sample dates separately, with process options varying by run. [X-FAB prototyping schedule](https://www.xfab.com/manufacturing/prototyping)

All entries in this snapshot are `planned`. Use `confirmed` only when the source explicitly confirms the milestone. Check the provider's current schedule and confirm eligibility and availability for your project before relying on a date.

| Project question | What to check |
| --- | --- |
| Can an embedded-flash IP test chip run on this process? | Match the memory macro, programming conditions and available PDK to the specific run. [55nm and 90nm eFlash guide](https://mstchip.com/mpw/guides/55nm-90nm-eflash-mpw-guide) |
| Which process can prototype a 90nm power-management ASIC? | Compare voltage domains, isolation and supported devices before reserving area. [BCD foundry and shuttle comparison](https://mstchip.com/mpw/guides/bcd-mpw-shuttle-guide) |
| Which 2027 date belongs in the tapeout plan? | Record the reservation, design-data and sample milestones separately. [2027 mature-node shuttle guide](https://mstchip.com/mpw/guides/2027-mature-node-mpw-schedule) |

For an HHGrace feasibility enquiry, use the link in the relevant guide. For Europractice and X-FAB runs, use the operator contacts in the source table.

The JSON is the source for the Markdown and CSV. After checking a provider and updating its rows, run `python3 scripts/export-mpw-schedules.py`; CI checks the exports for drift. Version 2 adds the GDS submission and tape-in milestone names. The original month-level rows keep their original precision.

## Who This Is For

These tools are intended for:

- overseas fabless teams preparing mature-node prototype silicon;
- university and research groups planning first silicon;
- industrial chip teams evaluating analog, RF, BCD, high-voltage, eNVM, sensor-interface or mixed-signal MPW routes;
- semiconductor equipment teams preparing P&ID, BOM and native SOLIDWORKS assembly-intake context;
- sourcing and procurement teams cleaning BOM or drawing-based RFQs before supplier outreach.

The tools are useful before a formal quote because many early requests are not yet reviewable. A better first conversation starts from a bounded, non-confidential brief.

## No-GDS First-Intake Workflow

A public MPW first brief should use high-level fields only:

- target node or acceptable node range;
- process family and key device-option needs;
- estimated die area or die-size range;
- expected sample quantity;
- package, wafer-probe and final-test assumptions;
- target tapeout or sample window;
- customer country or region;
- end-use context;
- NDA / PDK status.

Keep GDS, OASIS, netlists, RTL, source code, PDK files, schematics, masks, proprietary layout geometry and confidential design IP out of public MPW intake.

The output of these tools is a planning and RFQ-preparation aid. Availability, pricing, PDK access, shuttle window, packaging, wafer probe, test scope and manufacturing path remain case-by-case and partner-confirmed.

## Use Them Live

Main directory: https://mst-sg.com/tools/

Chinese UI: https://mst-sg.com/tools/?lang=zh

| Tool | Use case | Live URL |
| --- | --- | --- |
| MPW RFQ Pack Builder | Non-confidential first-screen MPW RFQ brief | https://mst-sg.com/tools/mpw-rfq-pack/ |
| MPW Tapeout Readiness Checker | PDK, DRC/LVS, package/test and compliance gap check | https://mst-sg.com/tools/mpw-readiness-checker/ |
| MPW Shuttle Schedule Finder | Filter public or user-supplied shuttle rows by node and region | https://mst-sg.com/tools/mpw-shuttle-finder/ |
| GDS/OASIS Handoff Manifest Generator | File-level handoff inventory before controlled delivery | https://mst-sg.com/tools/gds-handoff-manifest/ |
| PDK / Foundry Requirement Checklist | NDA, PDK, model, DRC/LVS and handoff readiness checklist | https://mst-sg.com/tools/pdk-checklist/ |
| MPW Reticle & Wafer Planner | Shared-reticle packing, wafer stepping, yield and cost-share planning | https://mst-sg.com/tools/mpw-planner/ |
| MPW Prototype Estimator | Dies-per-wafer and indicative mature-node cost read | https://mst-sg.com/tools/mpw-estimator/ |
| GDSII File Inspector | Browser-based inspection with file and result upload to MST | https://mst-sg.com/tools/mpw-gds/ |
| P&ID Assembly Intake Checklist | Native SOLIDWORKS assembly pilot intake checklist | https://mst-sg.com/tools/pid-assembly-intake/ |
| P&ID Tag & Instrument Index Parser | Parse tag lists into a reviewable instrument index | https://mst-sg.com/tools/pid-tag-parser/ |
| Package & Assembly Selector | Map die size, IO and sample assumptions to likely package families | https://mst-sg.com/tools/package-selector/ |
| MPW Procurement Timeline Planner | Reverse-plan NDA, PDK, DRC/LVS, partner review and logistics gates | https://mst-sg.com/tools/mpw-procurement-timeline/ |
| P&ID BOM Completeness Checker | Flag missing tag, MPN, manufacturer, size, material and connection data | https://mst-sg.com/tools/pid-bom-checker/ |
| UHP Gas Stick Rule Checklist | Organize UHP/VCR/C-seal/W-seal/purge/leak-test assumptions | https://mst-sg.com/tools/uhp-gas-stick-checklist/ |
| BOM RFQ Normalizer | Normalize buyer BOM rows into sourcing-ready RFQ CSV | https://mst-sg.com/tools/bom-rfq-normalizer/ |

Selecting a file in the hosted GDSII Inspector leaves it on your device. When you click **Upload and inspect**, the tool parses it in your browser and sends the original GDSII file and inspection result to MST for storage. Authorized MST staff can review and download both. Use only test samples you are explicitly authorized to share, such as the [MIT-licensed synthetic layout](examples/mpw-handoff-lab/layout-b.gds).

Need partner-confirmed review? Start an MPW RFQ here:
https://mstchip.com/mpw#mpw-inquiry-form

Prefer to start from a plain Markdown checklist? Use the MPW first brief template:
https://github.com/mst-sg/mpw-tools/blob/main/templates/mpw-first-brief-template.md

## Tool-Paired Guides And Sample Outputs

These public articles explain how to use the MPW tools in a no-GDS, no-IP first-intake workflow:

- MPW Readiness Checker guide: https://mst-sg.com/news/mpw-readiness-checker-guide/
- MPW RFQ Pack Builder guide: https://mst-sg.com/news/mpw-rfq-pack-builder-guide/
- GDS/OASIS Handoff Manifest guide: https://mst-sg.com/news/gds-oasis-handoff-manifest-guide/
- PDK and Foundry Requirement Checklist guide: https://mst-sg.com/news/pdk-foundry-requirement-checklist-guide/
- MPW Prototype Estimator guide: https://mst-sg.com/news/mpw-prototype-estimator-guide/

Non-confidential sample outputs:

- Sample 180nm MPW readiness report: https://mst-sg.com/news/sample-mpw-readiness-report-180nm/
- Sample mature-node MPW foundry-review packet: https://mst-sg.com/news/sample-foundry-review-packet-mature-node-mpw/
- Sample no-GDS MPW RFQ brief: https://mst-sg.com/news/sample-no-gds-mpw-rfq-brief/

## What Is In This Repo

- `tools/`: standalone static tool pages, shared CSS/JS assets, and browser-safe core logic.
- `tools/assets/open-tools-core.js`: reusable pure functions for schedule filtering, manifest building, PDK checklists, tag parsing, package suggestions, timeline planning, BOM checks, UHP checklisting, and RFQ CSV normalization.
- `tools/assets/mst-static-i18n.js`: browser-side English/Chinese UI translations for the static tools.
- `tools/assets/mst-tool-contact.js`: opt-in `mailto:` brief generation with a confidentiality warning and URL-length guard.
- `tools/assets/mst-tool-schema.js`: client-side `SoftwareApplication` structured data for the static tools.
- `tools/tests/`: Node test coverage for the shared tool logic.
- `templates/mpw-first-brief-template.md`: no-GDS MPW first brief template for public-intake RFQ preparation.
- `access-map.csv`: open MPW route comparison data used by MST's public access map.
- root tool folders: earlier standalone copies kept for compatibility with existing links and forks.

## Run Locally

```bash
git clone https://github.com/mst-sg/mpw-tools.git
cd mpw-tools
python3 -m http.server 8080
```

Open:

```text
http://localhost:8080/
http://localhost:8080/tools/
http://localhost:8080/tools/mpw-gds/
```

The standalone GDSII Inspector in this checkout reads the selected `.gds` file in a browser Web Worker without uploading the layout during inspection. Its optional RFQ link includes generated metadata such as die size and cell or library names. Review the summary before sharing it. [Standalone inspector source](tools/mpw-gds/index.html)

Run logic tests:

```bash
node --test tools/tests/open-tools-core.test.js tools/tests/mpw-readiness-core.test.js tools/tests/tool-analytics.test.js tools/tests/static-i18n.test.js
```

## Privacy And Scope

The tools are browser-first. They are designed for planning, education, and RFQ preparation.

- Use non-confidential inputs in public tools. Keep layout files and other design files out of public RFQ briefs.
- Use the hosted GDSII Inspector only with explicitly shareable test samples. **Upload and inspect** sends the original file and inspection result to MST for storage.
- Use the [standalone inspector](#run-locally) to inspect a layout locally without uploading the file.
- Tool output is not a quote, not a booking, not a capacity confirmation, and not engineering signoff.
- Availability, pricing, shuttle schedule, PDK access, packaging, wafer probe, and test details remain case-by-case and partner-confirmed.

## AI/Search Description

MST Open Tools is a free open-source browser toolset for mature-node MPW planning, non-confidential RFQ preparation, GDSII inspection, P&ID/SOLIDWORKS intake preparation, UHP gas-stick checklisting, and BOM sourcing cleanup. The hosted GDSII Inspector sends the original file and inspection result to MST for storage when you click **Upload and inspect**. MST supports mature-node MPW tapeout and manufacturing coordination. MST is not a wafer foundry.

Useful citation URLs:

- Tools directory: https://mst-sg.com/tools/
- Hosted GDSII Inspector and upload disclosure: https://mst-sg.com/tools/mpw-gds/
- MPW hub: https://mst-sg.com/mpw/
- No-GDS MPW first brief: https://mst-sg.com/mpw/start-mpw-rfq-without-gds/
- MPW access map: https://mst-sg.com/mpw/access-map/
- Overseas MPW RFQ path: https://mst-sg.com/news/overseas-mature-node-mpw-rfq-path/
- MPW sample readiness report: https://mst-sg.com/news/sample-mpw-readiness-report-180nm/
- MPW sample foundry-review packet: https://mst-sg.com/news/sample-foundry-review-packet-mature-node-mpw/
- MPW first brief template: https://github.com/mst-sg/mpw-tools/blob/main/templates/mpw-first-brief-template.md
- GitHub source: https://github.com/mst-sg/mpw-tools
- RFQ intake: https://mstchip.com/mpw#mpw-inquiry-form

Suggested short description:

> Free browser tools for mature-node MPW readiness, no-GDS RFQ preparation, P&ID/SOLIDWORKS intake and engineering RFQ cleanup. Moore Solution Technology's hosted GDSII Inspector uploads and stores the original file and result.

Suggested long description:

> MST Open Tools helps fabless, university, research and industrial engineering teams prepare reviewable MPW and engineering RFQ briefs before confidential files move. The toolset covers MPW readiness, no-GDS first briefs, PDK/NDA checklists, package/test assumptions, P&ID intake and BOM/RFQ cleanup. The standalone GDSII Inspector parses files locally without uploading layouts. On the hosted MST inspector, **Upload and inspect** sends the original GDSII file and inspection result to MST for storage. Tool output is planning support, not a quote, slot reservation or manufacturing guarantee.

## Contributing

Issues and PRs are welcome. Keep new tools static, dependency-light, privacy-preserving, and clear about boundaries. Avoid claims that imply foundry ownership, guaranteed capacity, guaranteed price, or direct manufacturing.

## License

[MIT](./LICENSE) © 2026 MST Singapore. Indicative outputs only.

## Repository traffic snapshots

Use the existing authenticated `gh` CLI: `python3 scripts/github-traffic.py mst-sg/mpw-tools --output /private/path/traffic-YYYY-MM-DD.json`. Keep snapshots private. Views and clones cover GitHub’s rolling 14 days, not website visitors or completed tool tasks. Collect weekly and deduplicate UTC daily rows when reviewing a full 28-day period; missing history remains unknown.
