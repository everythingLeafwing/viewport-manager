# I'm not dealing with separate files in an add-on
# every file is seperated like this
#---------------------------------- filename ---------------------------------
# NEVER IMPORT MODULES TWICE


# MODULES FOR ENTIRE ADDON GO HERE
# --------------------------------- modules ----------------------------------------
import bpy


# ------------------------------- add-on data ---------------------------------------

bl_info = {
    "name": "Viewport Presets",
    "author": "EverythingLeafwing",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Viewport Manager",
    "description": "helps you manage the viewport",
    "warning": "",
    "doc_url": "",
    "category": "View",
}


# --------------------------------- global data ------------------------------------


class data:
    currentViewport = "[none]"



# -------------------------------- exr render stuff ----------------------------------

class VPM_OP_EXR_RENDER_SETTINGS(bpy.types.Operator):
    bl_idname = "vpm.exr_render_settings"
    bl_label = "setup exr rendering"
    
    def execute(self, context):
        bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR'
        
        return {'FINISHED'}


# -------------------------------- presets ----------------------------------

# FORGET THE JSON
# DO IT LIKE THIS

class default(bpy.types.operator):
        data_name = "default"
        
        def execute():
            data.currentViewport = "default"
            
            # lighting
            bpy.context.space_data.shading.light = 'STUDIO'
            bpy.context.space_data.shading.studio_light = 'Default'
            bpy.context.space_data.shading.use_world_space_lighting = False
            
            # color and background
            bpy.context.space_data.shading.color_type = 'MATERIAL'
            bpy.context.space_data.shading.background_type = 'THEME'
            
            # options
            bpy.context.space_data.shading.show_backface_culling = False
            bpy.context.space_data.shading.show_xray = False
            bpy.context.space_data.shading.show_shadows = False

            # cavity
            bpy.context.space_data.shading.show_cavity = True
            bpy.context.space_data.shading.cavity_type = 'WORLD'
            bpy.context.space_data.shading.cavity_ridge_factor = 2.5
            
            bpy.context.space_data.shading.use_dof = False
            bpy.context.space_data.shading.show_object_outline = False
            bpy.context.space_data.shading.show_specular_highlight = True



basic = [
    default
]

# ---------------------------------- preset operators ----------------------------------

class VPM_DP_DEFAULT(bpy.types.Operator):
    bl_label = "default"
    bl_idname = "view.default_display"
    
    def execute(self, context):
        data.currentViewport = "default"
        
        # do absolutely nothing
        # someone has to fix this
        
        return {'FINISHED'}

class VPM_DP_FLAT(bpy.types.Operator):
    bl_label = "flat"
    bl_idname = "view.flat"
    
    def execute(self, context):
        data.currentViewport = "flat"
        
        bpy.context.space_data.shading.type = 'SOLID'
        
        bpy.context.space_data.shading.color_type = 'OBJECT'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = False
        
        bpy.context.space_data.shading.show_object_outline = False
        return {'FINISHED'}

class VPM_DP_RANDOMCOLOR(bpy.types.Operator):
    bl_label = "random color"
    bl_idname = "view.random_color_display"
    
    def execute(self, context):
        data.currentViewport = "random color"

        bpy.context.space_data.shading.type = 'SOLID'

        bpy.context.space_data.shading.color_type = 'RANDOM'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = True
        
        bpy.context.space_data.shading.cavity_type = 'WORLD'
        
        bpy.context.space_data.shading.cavity_ridge_factor = context.scene.VPM_props.Ridge
        bpy.context.space_data.shading.cavity_valley_factor = context.scene.VPM_props.Valley
        
        bpy.context.space_data.shading.curvature_ridge_factor = 0.5
        bpy.context.space_data.shading.curvature_valley_factor = 0
        
        bpy.context.space_data.shading.show_object_outline = False
        return {'FINISHED'}


class VPM_DP_MATERIALPREVIEWER(bpy.types.Operator):
    bl_label = "material previewer"
    bl_idname = "view.material_previewer_display"
    
    def execute(self, context):
        data.currentViewport = "material previewer"
        
        bpy.context.space_data.shading.type = 'MATERIAL'
        
        bpy.context.space_data.shading.studiolight_intensity = 1
        bpy.context.space_data.shading.studiolight_background_alpha = 1
        bpy.context.space_data.shading.studiolight_background_blur = 0
        
        return {'FINISHED'}

class VPM_DP_MAYA(bpy.types.Operator):
    bl_label = "maya"
    bl_idname = "view.maya_display"
    
    def execute(self, context):
        data.currentViewport = "maya"

        bpy.context.space_data.shading.type = 'SOLID'

        bpy.context.space_data.shading.color_type = 'SINGLE'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = False
        
        bpy.context.space_data.shading.color_type = 'SINGLE'
        bpy.context.space_data.shading.single_color = (0.595251, 0.75432, 0.8)
        
        bpy.context.space_data.shading.show_object_outline = False
        
        return {'FINISHED'}

class VPM_DP_OUTLINE(bpy.types.Operator):
    bl_label = "outline"
    bl_idname = "view.outline_display"
    
    def execute(self, context):
        scene = context.scene
        data.currentViewport = "outline"

        bpy.context.space_data.shading.type = 'SOLID'

        bpy.context.space_data.shading.color_type = 'TEXTURE'
        bpy.context.space_data.shading.background_type = 'THEME'
        
        bpy.context.space_data.shading.show_cavity = False
        
        bpy.context.space_data.shading.color_type = 'SINGLE'
        
        bpy.context.space_data.shading.show_object_outline = True
        bpy.context.space_data.shading.show_specular_highlight = scene.VPM_props.OutlineLightObjects
            
        bpy.context.space_data.shading.show_specular_highlight = scene.VPM_props.OutlineLightObjects
        bpy.context.space_data.shading.single_color = scene.VPM_props.OutlineObjectColor
        bpy.context.space_data.shading.object_outline_color = scene.VPM_props.OutlineColor
        
        return {'FINISHED'}







# the addons needed properties
class VPM_Properties(bpy.types.PropertyGroup):
    Valley = bpy.props.FloatProperty(name= "Valley", default= 1, min=0, max=2.5)
    Ridge = bpy.props.FloatProperty(name= "Ridge", default= 2.5, min=0, max=2.5)
    
    OutlineObjectColor = bpy.props.FloatVectorProperty(name= "Object Color", default= [0, 0, 0], subtype="COLOR")
    OutlineColor = bpy.props.FloatVectorProperty(name= "Outline Color", default= [1, 1, 1], subtype="COLOR")
    OutlineLightObjects = bpy.props.BoolProperty(name= "specular shading", default= False)








class ViewportManager(bpy.types.Panel):
    bl_label = "Viewport Manager"
    bl_idname = "viewport_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Viewport Manager"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        row.label(text= "viewport")

class VPM_PRESETS(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Presets"
    bl_parent_id = "viewport_manager"
    bl_idname = "vm_viewport_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "viewport_manager"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        
        box = layout.box()
        box.label(text= "settings:")
        
        if data.currentViewport == "random color" or data.currentViewport == "default":
            box.prop(scene.VPM_props, "Ridge")
            box.prop(scene.VPM_props, "Valley")
        
            bpy.context.space_data.shading.cavity_ridge_factor = context.scene.VPM_props.Ridge
            bpy.context.space_data.shading.cavity_valley_factor = context.scene.VPM_props.Valley
        
        if data.currentViewport == "outline":
            box.prop(scene.VPM_props, "OutlineObjectColor")
            box.prop(scene.VPM_props, "OutlineColor")
            box.prop(scene.VPM_props, "OutlineLightObjects")
            
            bpy.context.space_data.shading.show_specular_highlight = scene.VPM_props.OutlineLightObjects
            bpy.context.space_data.shading.single_color = scene.VPM_props.OutlineObjectColor
            bpy.context.space_data.shading.object_outline_color = scene.VPM_props.OutlineColor
        
        layout.label(text= "current display: " + str(data.currentViewport))

class basicPresets(bpy.types.Panel):
    bl_idname = "vm_basic_viewport_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = "vm_viewport_presets"
    bl_context = "vm_viewport_presets"
    bl_label = "basic viewports"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        layout.row().operator("view.default_display")
        layout.row().operator("view.flat")
        layout.row().operator("view.random_color_display")
        layout.row().operator("view.maya_display")
        layout.row().operator("view.outline_display")

class renderPresets(bpy.types.Panel):
    bl_idname = "vm_render_viewport_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = "vm_viewport_presets"
    bl_context = "vm_viewport_presets"
    bl_label = "render viewports"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        layout.row().operator("view.material_previewer_display")


class render_exr(bpy.types.Panel):
    bl_label = "render MatCap"
    bl_parent_id = "viewport_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "viewport_manager"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        row.operator("vpm.exr_render_settings")
        row = layout.row()
        row.operator("render.render")

operators = {
    VPM_DP_DEFAULT, VPM_DP_FLAT, VPM_DP_RANDOMCOLOR, VPM_DP_MAYA, VPM_DP_OUTLINE,
    VPM_DP_MATERIALPREVIEWER, VPM_OP_EXR_RENDER_SETTINGS
}
subPanels = {
    VPM_PRESETS, render_exr
}
presetTypes = {
    basicPresets, renderPresets
}

def register():
    bpy.utils.register_class(ViewportManager)
    bpy.utils.register_class(VPM_Properties)
    
    for cls in operators:
        bpy.utils.register_class(cls)
    for cls in subPanels:
        bpy.utils.register_class(cls)
    for cls in presetTypes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.VPM_props = bpy.props.PointerProperty(type= VPM_Properties)


def unregister():
    bpy.utils.unregister_class(ViewportManager)
    bpy.utils.unregister_class(VPM_Properties)
    
    for cls in operators:
        bpy.utils.unregister_class(cls)
    for cls in subPanels:
        bpy.utils.unregister_class(cls)
    for cls in presetTypes:
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.VPM_props

if __name__ == "__main__":
    register()
