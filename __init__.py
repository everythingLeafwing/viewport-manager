import bpy

bl_info = {
    "name": "Viewport Presets",
    "author": "EverythingLeafwing",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Viewport Presets",
    "description": "Adds viewport presets",
    "warning": "",
    "doc_url": "",
    "category": "View",
}


# basic viewport
class VP_DP_DEFAULT(bpy.types.Operator):
    bl_label = "default"
    bl_idname = "view.default_display"
    
    def execute(self, context):
        
        bpy.context.space_data.shading.type = 'SOLID'
        
        bpy.context.space_data.shading.color_type = 'OBJECT'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = True
        
        bpy.context.space_data.shading.cavity_type = 'WORLD'
        
        bpy.context.space_data.shading.cavity_ridge_factor = context.scene.vp_props.Ridge
        bpy.context.space_data.shading.cavity_valley_factor = context.scene.vp_props.Valley
        
        bpy.context.space_data.shading.show_object_outline = False
        return {'FINISHED'}

class VP_DP_FLAT(bpy.types.Operator):
    bl_label = "flat"
    bl_idname = "view.flat"
    
    def execute(self, context):
        
        bpy.context.space_data.shading.type = 'SOLID'
        
        bpy.context.space_data.shading.color_type = 'OBJECT'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = False
        
        bpy.context.space_data.shading.show_object_outline = False
        return {'FINISHED'}

class VP_DP_RANDOMCOLOR(bpy.types.Operator):
    bl_label = "random color"
    bl_idname = "view.random_color_display"
    
    def execute(self, context):

        bpy.context.space_data.shading.type = 'SOLID'

        bpy.context.space_data.shading.color_type = 'RANDOM'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = True
        
        bpy.context.space_data.shading.cavity_type = 'WORLD'
        
        bpy.context.space_data.shading.cavity_ridge_factor = context.scene.vp_props.Ridge
        bpy.context.space_data.shading.cavity_valley_factor = context.scene.vp_props.Valley
        
        bpy.context.space_data.shading.curvature_ridge_factor = 0.5
        bpy.context.space_data.shading.curvature_valley_factor = 0
        
        bpy.context.space_data.shading.show_object_outline = False
        return {'FINISHED'}


class VP_DP_MATERIALPREVIEWER(bpy.types.Operator):
    bl_label = "material previewer"
    bl_idname = "view.material_previewer_display"
    
    def execute(self, context):
        
        bpy.context.space_data.shading.type = 'MATERIAL'
        
        bpy.context.space_data.shading.studiolight_intensity = 1
        bpy.context.space_data.shading.studiolight_background_alpha = 1
        bpy.context.space_data.shading.studiolight_background_blur = 0
        
        return {'FINISHED'}

class VP_DP_MAYA(bpy.types.Operator):
    bl_label = "maya"
    bl_idname = "view.maya_display"
    
    def execute(self, context):

        bpy.context.space_data.shading.type = 'SOLID'

        bpy.context.space_data.shading.color_type = 'SINGLE'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = False
        
        bpy.context.space_data.shading.color_type = 'SINGLE'
        bpy.context.space_data.shading.single_color = (0.595251, 0.75432, 0.8)
        
        bpy.context.space_data.shading.show_object_outline = False
        
        return {'FINISHED'}

class VP_DP_OUTLINE(bpy.types.Operator):
    bl_label = "outline"
    bl_idname = "view.outline_display"
    
    def execute(self, context):

        bpy.context.space_data.shading.type = 'SOLID'

        bpy.context.space_data.shading.color_type = 'TEXTURE'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = False
        
        bpy.context.space_data.shading.color_type = 'SINGLE'
        bpy.context.space_data.shading.single_color = (0, 0, 0)
        
        bpy.context.space_data.shading.show_object_outline = True
        bpy.context.space_data.shading.object_outline_color = (1, 1, 1)
        
        return {'FINISHED'}


class VP_Properties(bpy.types.PropertyGroup):
    Valley = bpy.props.FloatProperty(name= "Valley", default= 1, min=0, max=2.5)
    Ridge = bpy.props.FloatProperty(name= "Ridge", default= 2.5, min=0, max=2.5)

class ViewportPresets(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Viewport Presets"
    bl_idname = "VIEWPORT_PRESETS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Viewport presets"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        
        row.label(text= "select a viewport preset to switch to")
        
        box = layout.box()
        box.label(text= "settings:")
        box.prop(scene.vp_props, "Ridge")
        box.prop(scene.vp_props, "Valley")
        
        box = layout.box()
        box.label(text= "basic viewports:")
        box.operator("view.default_display")
        box.operator("view.flat")
        box.operator("view.random_color_display")
        box.operator("view.maya_display")
        box.operator("view.outline_display")
        box = layout.box()
        box.label(text= "render viewports:")
        box.operator("view.material_previewer_display")

classes = {
    VP_DP_DEFAULT, VP_DP_FLAT, VP_DP_RANDOMCOLOR, VP_DP_MAYA, VP_DP_OUTLINE,
    VP_DP_MATERIALPREVIEWER,
    VP_Properties,
    ViewportPresets
}

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.vp_props = bpy.props.PointerProperty(type= VP_Properties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.vp_props

if __name__ == "__main__":
    register()
