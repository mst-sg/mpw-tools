#!/usr/bin/env python3
"""Offline teaching-package checksum and report-binding exercise; standard library only."""
import hashlib,json,sys
from pathlib import Path
root=Path(__file__).resolve().parent
for line in (root/'SHA256SUMS').read_text().splitlines():
    digest,name=line.split('  ',1)
    if Path(name).name!=name:raise SystemExit('Unsafe manifest name')
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'Checksum failed: '+name
print('Package checksums: PASS')
actual=hashlib.sha256((root/'layout-b.gds').read_bytes()).hexdigest()
for filename,count in [('reports-consistent.json',0),('reports-stale.json',2)]:
    data=json.loads((root/filename).read_text());problems=[]
    for r in data['reports']:
        for k,v in [('layout_sha256',actual),('layout_revision','B'),('top_cell','MST_DEMO_TOP'),('pdk_revision','TEACHING-NO-PDK-v1')]:
            if r[k]!=v:problems.append(r['kind']+': '+k+' mismatch')
    assert len(problems)==count,(filename,problems)
    print(filename+': '+('metadata consistent' if not problems else '; '.join(problems)))
print('Exercise: PASS. This is not signoff and does not run DRC or LVS.')
