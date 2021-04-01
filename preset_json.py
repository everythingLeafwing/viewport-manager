import json
import bpy


def loadPreset(location):
    with open(location) as json_file:
        print(json.load(json_file))
        data = json.load(json_file)

        with data["lighting"] as lighting:
            if lighting["type"] == "studio":
                bpy.context.space_data.shading.light = 'STUDIO'
                bpy.context.space_data.shading.studio_light = lighting["lighting file"]

                with lighting["world space lighting"] as world_space_lighting:
                    bpy.context.space_data.shading.use_world_space_lighting = world_space_lighting
                    if world_space_lighting:
                        bpy.context.space_data.shading.studiolight_rotate_z = world_space_lighting["rotation"]

        bpy.context.space_data.shading.color_type = data["color"]
        bpy.context.space_data.shading.background_type = data["background"]
        bpy.context.space_data.shading.show_backface_culling = data["backface culling"]

        bpy.context.space_data.shading.show_xray =  data["x-ray"]["enabled"]
        if data["x-ray"]["enabled"]:
            bpy.context.space_data.shading.xray_alpha = data["x-ray"]["alpha"]
