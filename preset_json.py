import json
import bpy


def loadPreset(location):
    with open(location) as json_file:
        data = json.load(json_file)["presets"]
        
        with lighting as data["lighting"]:
            if lighting["type"] == "studio":
                bpy.context.space_data.shading.light = 'STUDIO'
                if lighting["lighting file"] == "basic"
