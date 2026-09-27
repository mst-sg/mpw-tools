#!/usr/bin/env python3
"""Regenerate MST's own synthetic geometry. Requires klayout==0.30.12.
Not an electrical design, PDK, DRC deck, LVS deck or submission package.
"""
import hashlib,json
from pathlib import Path
import klayout.db as kdb
ROOT=Path(__file__).resolve().parent
for revision,width in [('a',100000),('b',120000)]:
    layout=kdb.Layout();layout.dbu=0.001
    top=layout.create_cell('MST_DEMO_TOP');tile=layout.create_cell('UNIT_TILE')
    top.shapes(layout.layer(99,0)).insert(kdb.Box(0,0,width,60000))
    tile.shapes(layout.layer(1,0)).insert(kdb.Box(0,0,10000,5000))
    tile.shapes(layout.layer(2,0)).insert(kdb.Box(2000,1000,8000,4000))
    for x in [10000,30000]:top.insert(kdb.CellInstArray(tile.cell_index(),kdb.Trans(x,10000)))
    options=kdb.SaveLayoutOptions();options.format='GDS2';options.gds2_write_timestamps=False
    layout.write(str(ROOT/f'layout-{revision}.gds'),options)
hashes={rev:hashlib.sha256((ROOT/f'layout-{rev}.gds').read_bytes()).hexdigest() for rev in ['a','b']}
def report(kind,rev):return {'kind':kind,'layout_sha256':hashes[rev.lower()],'top_cell':'MST_DEMO_TOP','layout_revision':rev,'pdk_revision':'TEACHING-NO-PDK-v1','deck_revision':'TEACHING-NO-SIGNOFF-v1','result':'pass'}
for name,revs in [('reports-consistent.json',['B','B']),('reports-stale.json',['A','B'])]:
    (ROOT/name).write_text(json.dumps({'schema':1,'notice':'Teaching metadata only; no DRC or LVS has run. These files are not verification reports.','reports':[report(kind,rev) for kind,rev in zip(['DRC','LVS'],revs)]},indent=2)+'\n')
(ROOT/'expected-layouts.json').write_text(json.dumps({rev:{'sha256':hashes[rev],'top_cells':['MST_DEMO_TOP'],'cells':2,'dbu_micrometers':0.001,'layers':[[1,0],[2,0],[99,0]],'bbox_micrometers':[0,0,width,60],'stored_boundaries':3,'stored_references':2} for rev,width in [('a',100),('b',120)]},indent=2)+'\n')
print('Generated two synthetic GDS layouts and two teaching metadata sets.')
