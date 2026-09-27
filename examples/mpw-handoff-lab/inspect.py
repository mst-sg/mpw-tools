#!/usr/bin/env python3
"""Verify both synthetic GDS files against independently recorded expected values."""
import json,hashlib
from pathlib import Path
import klayout.db as kdb
root=Path(__file__).resolve().parent
expected=json.loads((root/'expected-layouts.json').read_text())
for rev,e in expected.items():
    path=root/f'layout-{rev}.gds';layout=kdb.Layout();layout.read(str(path))
    assert hashlib.sha256(path.read_bytes()).hexdigest()==e['sha256'],'Hash differs'
    assert [c.name for c in layout.top_cells()]==e['top_cells'],'Top cell differs'
    assert layout.cells()==e['cells'],'Cell count differs'
    assert abs(layout.dbu-e['dbu_micrometers'])<1e-12,'DBU differs'
    assert sorted([[i.layer,i.datatype] for i in layout.layer_infos()])==e['layers'],'Layer list differs'
    box=layout.top_cell().dbbox()
    assert [box.left,box.bottom,box.right,box.top]==e['bbox_micrometers'],'Bounding box differs'
    print(f'layout-{rev}.gds: PASS; top=MST_DEMO_TOP, cells=2, DBU=0.001 um, bbox={e["bbox_micrometers"]} um')
print('Geometry metadata checked. No DRC, LVS or electrical validation was performed.')
