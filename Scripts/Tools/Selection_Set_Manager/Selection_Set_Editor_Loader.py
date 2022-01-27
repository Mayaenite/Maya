
import QT
import Scripts.UICls.mayaMixin
import maya.app.general.mayaMixin
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken import wrapInstance
from . import AW_Selection_Set_Editor
import importlib

def Load_Editor(force_Reload=True):
	expaded_items =  []
	if force_Reload:
		mayaMainWindowPtr = omui.MQtUtil.mainWindow()
		rootWidget        = wrapInstance(long(mayaMainWindowPtr), QT.QtGui.QWidget)
		found_children    = rootWidget.findChildren(Scripts.UICls.mayaMixin.MayaQWidgetDockableMixin)
		if len(found_children):
			for found_child in found_children:
				if found_child.objectName() == "Selection_Set_Editor":
					editor        =  found_child
					try:
						expaded_items = editor.Selection_Set_Outliner_Tree_View.get_expanded_items()
					except:
						pass
					editor.cleanup()
					native_Parent = editor.nativeParentWidget()
					native_Parent.hide()
					native_Parent.setParent(None)
					del native_Parent
					importlib.reload(AW_Selection_Set_Editor)
	editor = AW_Selection_Set_Editor.UI_LOADER()
	if len(expaded_items):
		editor.Selection_Set_Outliner_Tree_View.set_expand_item_by_name(expaded_items)
	return editor
 
