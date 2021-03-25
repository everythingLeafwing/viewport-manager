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
    "category": "Add Mesh",
}


class VP_DP_DEFAULT(bpy.types.Operator):
    bl_label = "default"
    bl_idname = "view.default_display"
    
    def execute(self, context):
        
        bpy.context.space_data.shading.type = 'SOLID'
        
        bpy.context.space_data.shading.color_type = 'OBJECT'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = True
        
        bpy.context.space_data.shading.cavity_type = 'WORLD'
        bpy.context.space_data.shading.cavity_ridge_factor = 2.5
        bpy.context.space_data.shading.cavity_valley_factor = 1
        
        bpy.context.space_data.shading.curvature_ridge_factor = 0.5
        bpy.context.space_data.shading.curvature_valley_factor = 0
        
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
        bpy.context.space_data.shading.cavity_ridge_factor = 2.5
        bpy.context.space_data.shading.cavity_valley_factor = 1
        
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

class ViewportPresets(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Viewport Presets"
    bl_idname = "VIEWPORT_PRESETS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Viewport presets"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        
        row.label(text= "select a viewport preset to switch to")
        
        row = layout.row()
        row.operator("view.default_display")
        row = layout.row()
        row.operator("view.flat")
        row = layout.row()
        row.operator("view.random_color_display")
        row = layout.row()
        row.operator("view.material_previewer_display")
        row = layout.row()
        row.operator("view.maya_display")
        row = layout.row()
        row.operator("view.outline_display")


def register():
    bpy.utils.register_class(VP_DP_DEFAULT)
    bpy.utils.register_class(VP_DP_FLAT)
    bpy.utils.register_class(VP_DP_RANDOMCOLOR)
    bpy.utils.register_class(VP_DP_MATERIALPREVIEWER)
    bpy.utils.register_class(VP_DP_MAYA)
    bpy.utils.register_class(VP_DP_OUTLINE)
    bpy.utils.register_class(ViewportPresets)


def unregister():
    bpy.utils.unregister_class(VP_DP_DEFAULT)
    bpy.utils.unregister_class(VP_DP_FLAT)
    bpy.utils.unregister_class(VP_DP_RANDOMCOLOR)
    bpy.utils.unregister_class(VP_DP_MATERIALPREVIEWER)
    bpy.utils.unregister_class(VP_DP_MAYA)
    bpy.utils.unregister_class(VP_DP_OUTLINE)
    bpy.utils.unregister_class(ViewportPresets)

if __name__ == "__main__":
    register()
