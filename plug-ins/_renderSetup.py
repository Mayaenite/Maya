import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
import maya.mel as mel

import sys


# Using the Maya Python API 2.0.
def maya_useNewAPI():
    pass


renderSetupVersion = '1.0'


# List of all available initializers
import my_app.renderSetup.model.initialize as modelInitializer
modules = [ modelInitializer ]

# UI components  -  batch mode (i.e. Maya IO) does not need them
if not cmds.about(batch=True):
    # Add all available UI related initializers
    import my_app.renderSetup.views.initialize as viewsInitializer
    modules += [ viewsInitializer ]


def initializePlugin(mobject):
    """ Initialize all the needed nodes """
    mplugin = OpenMaya.MFnPlugin(mobject, "Autodesk", renderSetupVersion, "Any")

    mel.eval("loadRenderLayerFilters()")
    
    for module in modules:
        module.initialize(mplugin)

def uninitializePlugin(mobject):
    """ Uninitialize all the nodes """
    mplugin = OpenMaya.MFnPlugin(mobject, "Autodesk", renderSetupVersion, "Any")

    mel.eval("unloadRenderLayerFilters()")
    
    for module in modules:
        module.uninitialize(mplugin)
