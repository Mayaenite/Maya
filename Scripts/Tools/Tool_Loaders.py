display_Layer_Editor_Window, display_Layer_Editor_Doc = None, None
import  os
os.sys.path.append(os.path.dirname(__file__))

def create_display_Layer_editor():
	global display_Layer_Editor_Window, display_Layer_Editor_Doc
	import Scripts.Tools.Display_Layer_Editor
	try:
		display_Layer_Editor_Window.display_layer_tree.remove_Maya_Scene_CallBacks()
		display_Layer_Editor_Window.display_layer_tree.cleanup()
	except:
		pass
	reload(Scripts.Tools.Display_Layer_Editor)
	display_Layer_Editor_Window, display_Layer_Editor_Doc = Scripts.Tools.Display_Layer_Editor.make_Editor(True)