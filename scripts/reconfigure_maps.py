"""
Looks at all the mapnik xml files in ../xml
Creates ../tilestache/tilestache.cfg (backing up the old copy)
Create ../html/layers_fixture.js (backing up the old copy)
"""
from glob import glob
from os import path, rename
from templates import *

cdir = path.abspath(path.join(path.dirname(__file__), "..", "xml"))
tscfg = path.abspath(path.join(path.dirname(__file__),
                     "..", "tilestache", "tilestache.cfg"))
jsfixt = path.abspath(path.join(path.dirname(__file__),
                      "..", "html", "layers_fixture.js"))

ids = []
tilelayers = []
fixturelayers = []

# Looks at all the mapnik xml files in ../xml
idx = 0
for xml in glob(path.join(cdir, '*.xml')):
    idx += 1
    ids.append(idx)
    layername = path.splitext(path.basename(xml))[0]
    tilelayers.append(tilelayer_template % (layername, xml))
    fixturelayers.append(fixturelayer_template % (layername, layername, idx))

# Creates ../tilestache/tilestache.cfg (backing up the old copy)
cfg = cfg_template % ','.join(tilelayers)
if path.exists(tscfg):
    bu = tscfg + ".backup"
    rename(tscfg, bu)

with open(tscfg, 'w') as fh:
    fh.write(cfg)

# Create ../html/layers_fixture.js (backing up the old copy)
fixture = fixture_template % (','.join(fixturelayers),
                              ','.join(str(x) for x in ids))
if path.exists(jsfixt):
    bu = jsfixt + ".backup"
    rename(jsfixt, bu)

with open(jsfixt, 'w') as fh:
    fh.write(fixture)
