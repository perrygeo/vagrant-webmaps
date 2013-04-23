
cfg_template = """{
  "cache": {
    "name": "Redis",
    "host": "localhost",
    "port": 6379,
    "db": 0
  },
  "layers": {
    "osm": {
      "provider": {
        "name": "proxy",
        "url": "http://tile.openstreetmap.org/{Z}/{X}/{Y}.png"
      }
    },%s
  }
}
"""

tilelayer_template = """
    "%s": {
      "provider": {
        "name": "mapnik",
        "mapfile": "%s"
      },
      "metatile": {
        "rows": 4,
        "columns": 4,
        "buffer": 64
      },
      "preview": {
        "lat": 0.0,
        "lon": 0.0,
        "zoom": 2,
        "ext": "png"
      }
    }"""

fixturelayer_template = """{
            "name": "%s", "url": ["/tiles/%s/${z}/${x}/${y}.png"],
            "opacity": 1.0, "lookups": {"field": null, "details": []}, "graphic": null, 
            "default_on": true, "data_source": "", "subLayers": [],
            "utfurl": null, "description": null, "arcgis_layers": null, "legend": null, "legend_title": null, 
            "attributes": {"attributes": [], "compress_attributes": false, "event": "click", "title": null}, 
            "fill_opacity": null, "learn_link": null, "type": "XYZ", "id": %d, "color": null, 
            "legend_subtitle": null
        }"""

fixture_template = """app.fixture = {
    "layers": [
        %s
    ],
    "themes": [
        {
            "layers": [%s],
            "description": null, "display_name": "Layers", "id": 1, "learn_link": ""
        }
   ]
}
"""
