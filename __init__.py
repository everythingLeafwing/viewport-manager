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

### presets: (write any added ones here too)
#
## solid
#
# default
# flat
# random color
# maya
# outline
#
## render viewports
# material previewer

class default(bpy.types.Operator):
        bl_label = "default"
        bl_idname = "vpm.default_preset"
        
        def execute(self, context):
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
            
            return {'FINISHED'}

class random(bpy.types.Operator):
        bl_label = "random"
        bl_idname = "vpm.random_preset"
        
        def execute(self, context):
            data.currentViewport = "random"
            
            # lighting
            bpy.context.space_data.shading.light = 'STUDIO'
            bpy.context.space_data.shading.studio_light = 'Default'
            bpy.context.space_data.shading.use_world_space_lighting = False
            
            # color and background
            bpy.context.space_data.shading.color_type = 'RANDOM'
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
            
            return {'FINISHED'}



solidViewPresets = [
    default,
    random
]

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

class solidPresets(bpy.types.Panel):
    bl_idname = "vm_basic_viewport_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = "vm_viewport_presets"
    bl_context = "vm_viewport_presets"
    bl_label = "solid viewports"
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        for op in solidViewPresets:
            layout.operator(op.bl_idname)
            
        
        

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

subPanels = {
    VPM_PRESETS, render_exr
}
presetTypes = {
    solidPresets, renderPresets
}

def register():
    bpy.utils.register_class(ViewportManager)
    bpy.utils.register_class(VPM_Properties)
    
    for cls in solidViewPresets:
        bpy.utils.register_class(cls)
    
    for cls in subPanels:
        bpy.utils.register_class(cls)
    for cls in presetTypes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.VPM_props = bpy.props.PointerProperty(type= VPM_Properties)


def unregister():
    bpy.utils.unregister_class(ViewportManager)
    bpy.utils.unregister_class(VPM_Properties)
    
    for cls in subPanels:
        bpy.utils.unregister_class(cls)
    for cls in presetTypes:
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.VPM_props

if __name__ == "__main__":
    register()
