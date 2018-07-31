import pymel.core as pm
import  os

def create_display_Layer_editor():
	import Scripts.Tools.Display_Layer_Editor.Layer_Editor
	try:
		wig = Scripts.Tools.Display_Layer_Editor.Layer_Editor.Initialize_Layer_Editor()
		return wig
	except:
		pass
	
AW_Display_Layer_Editor = pm.evalDeferred(create_display_Layer_editor,lowestPriority=True)