import pymel.core as pm

def create_display_Layer_editor():
	try:
		wig = Scripts.Tools.Display_Layer_Editor.Layer_Editor.Initialize_Layer_Editor()
		return wig
	except Exception as e:
		print e
	
try:
	import Scripts.Tools.Display_Layer_Editor.Layer_Editor
	AW_Display_Layer_Editor = pm.evalDeferred(create_display_Layer_editor,lowestPriority=True)
except Exception as e:
	print e