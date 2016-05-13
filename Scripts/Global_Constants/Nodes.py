try:
	import Scripts.NodeCls.M_Nodes
	M_Nodes = Scripts.NodeCls.M_Nodes
	__import_check = False
except:
	__import_check = True
	M_Nodes = None
from maya import cmds

def import_Check():
	global __import_check, M_Nodes
	if __import_check:
		import Scripts.NodeCls.M_Nodes
		M_Nodes = Scripts.NodeCls.M_Nodes
		__import_check = False
#----------------------------------------------------------------------
#----------------------------------------------------------------------
def assemblies():
	"""A List Of Root Level Tranform MNODES"""
	import_Check()
	return M_Nodes.strings_to_MNODES(cmds.ls(assemblies=True))
#----------------------------------------------------------------------
def Render_Layers(includeDefault=False, includeRefs=False):
	"""A List Of All RenderLayer"""
	import_Check()
	res = [M_Nodes.RenderLayer(layer) for layer in cmds.ls(type="renderLayer")]
	if not includeDefault:
		res = [layer for layer in res if not layer.name == 'defaultRenderLayer']
	if not includeRefs:
		res = [layer for layer in res if not ":" in layer.name]
	return res
#----------------------------------------------------------------------
def Display_Layers():
	"""A List Of All DisplayLayer"""
	import_Check()
	return [M_Nodes.DisplayLayer(item) for item in cmds.ls(type="displayLayer") if not 'defaultLayer' in item]

#----------------------------------------------------------------------
def Shading_Engines():
	import_Check()
	"""A List Of All DisplayLayer"""
	return [M_Nodes.Shading_Engine(item) for item in cmds.ls(type="shadingEngine") if not "initial" in item]