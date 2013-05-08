#!/usr/bin/env python
import os
from glob import glob

print "Caching some tiles..."
sz = 4
nz = 6

zooms = [str(x) for x in range(sz,sz+nz+1)]

extent = '41.8 -125.1 49.2 -116.3'

layers = []
wildcard = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','xml', '*.xml'))
print wildcard
for xml in glob(wildcard):
    layername = os.path.splitext(os.path.basename(xml))[0]
    layers.append(layername)

tilecfg = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','tilestache','tilestache.cfg'))
for zoom in zooms:
    for layer in layers:
        print "#--------------------------------------#"
        cmd = "tilestache-seed.py -c %s -l %s -e %s -b %s %s" % (tilecfg, layer, 'png', extent, zoom)
        print cmd
        print "#--------------------------------------#"
        os.popen(cmd)
