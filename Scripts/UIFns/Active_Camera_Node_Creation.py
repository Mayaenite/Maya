import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds
import Scripts.OpenMaya_Util_API
import Scripts.General_Maya_Util

Util_General = Scripts.General_Maya_Util
Util_API     = Scripts.OpenMaya_Util_API

get_Panel_With_Focus    = lambda :pm.getPanel(withFocus=True)
get_Panel_Under_Pointer = lambda :pm.getPanel(underPointer=True)

#----------------------------------------------------------------------
def nodeTypeNiceName(nodeType):
	""""""
	lookupId = "n_" + nodeType + ".niceName"	
	if cmds.displayString(lookupId,exists=True):
		labelName = mel.eval('uiRes ' + lookupId)
	else:
		labelName = mel.eval('interToUI ' + nodeType)
	return labelName
#----------------------------------------------------------------------
def get_Light_Types():
	""""""
	light_types = cmds.listNodeTypes("light")
	return light_types
#----------------------------------------------------------------------
def get_Type_Nice_Names(types):
	""""""
	res = [nodeTypeNiceName(t) for t in types]
	return res
#----------------------------------------------------------------------
def get_Light_Named_command_Functions():
	""""""
	res = []
	types      = get_Light_Types()
	nice_names = get_Type_Nice_Names(types)
	functions  = []
	command_names = []
	for t, n in zip(types, nice_names):
		fn = "import %s\n" % __name__
		fn += '%s.create_Light_From_Modle_Editor_View("%s")' % (__name__, t)
		cmd_name = "aw_create_" + t + "_at_active_view"
		functions.append(fn)
		command_names.append(cmd_name)
	for t,n,c,f in zip(types, nice_names, command_names, functions):
		res.append([t, n, c, f])
	return res

_run_time_commands = get_Light_Named_command_Functions()

#----------------------------------------------------------------------
def get_VRay_Light_Types():
	""""""
	light_types = cmds.listNodeTypes("light")
	res = [l for l in light_types if l.startswith("VRay")]
	return res
#----------------------------------------------------------------------
def get_Maya_Light_Types():
	""""""
	light_types = cmds.listNodeTypes("light")
	res = [l for l in light_types if not l.startswith("VRay")]
	return res
#----------------------------------------------------------------------
def match_point_and_orient(master,slave):
	"""Matches The Slave Translate and Rotate To The Master Using Constrants Then Delete's The Constraints"""
	# Create A Point Constraint To Match The Translate
	p_Constraint = cmds.pointConstraint(str(master),str(slave),offset=[0,0,0],weight=1)
	# Create A Orientate Constraint To Match The Rotate
	o_Constraint = cmds.orientConstraint(str(master),str(slave),offset=[0,0,0],weight=1)
	# Remove The Constraints
	cmds.delete(p_Constraint,o_Constraint)
#----------------------------------------------------------------------
def get_persp_cam():
	""""""
	persp = pm.PyNode("persp")
	return persp
#----------------------------------------------------------------------
def is_Model_Editor(pan):
	""""""
	if pan is None:
		return False
	return pan.type() == "modelEditor"
#----------------------------------------------------------------------
def get_Model_Panel():
	"""Get The Camara Used In The input Editor Panel"""
	currentPanel = get_Panel_Under_Pointer()
	if not is_Model_Editor(currentPanel):
		currentPanel = get_Panel_With_Focus()
	if not is_Model_Editor(currentPanel):
		raise LookupError("No Model Panel Was Found Under The Pointer Or With Focus")
	return pm.ui.ModelPanel(currentPanel.name())
#----------------------------------------------------------------------
def get_panel_cam(panel_name=None):
	"""Get The Camara Used In The input Editor Panel"""
	if panel_name is None:
		currentPanel = get_Model_Panel()
	else:
		currentPanel = pm.ui.Panel(panel_name)
		if not is_Model_Editor(currentPanel):
			raise TypeError("The Input Panel Name Was Not A Model Panel")

	m_panel  = pm.ui.ModelPanel(currentPanel.name())
	cam      = pm.PyNode(m_panel.getCamera())

	if cam.type() == 'camera':
		cam = cam.getParent()

	return cam
#----------------------------------------------------------------------
def create_light(lightType="spotLight"):
	trans = pm.shadingNode(lightType,asLight=True)
	shape = trans.getChildren()[0]
	return trans,shape
#----------------------------------------------------------------------
def tear_Off_Copy(panel_name):
	res = mel.eval('tearOffCopyItemCmd  "modelPanel" "%s";' % (panel_name))
	res = pm.ui.ModelPanel(res)
	return res
#----------------------------------------------------------------------
def look_Through_Object(obj,panel_name,nearClip=1.0, farClip=10000.0):
	pm.lookThru(panel_name,obj,nearClip=nearClip, farClip=farClip)
#----------------------------------------------------------------------
def view_Look_At(cam):
	pm.viewLookAt(cam)
#----------------------------------------------------------------------
def create_light_from_cam(cam,lightType="spotLight"):
	""""""
	cam = pm.PyNode(str(cam))
	ltr,lsh = create_light(lightType)
	# lsh.locatorScale.set(5)
	# lsh.locatorScale.showInChannelBox(True)
	match_point_and_orient(cam, ltr)
	try:
		lsh.centerOfIllumination.set(cam.centerOfInterest.get())
	except:
		pass
	return ltr
#----------------------------------------------------------------------
def create_Light_From_Modle_Editor_View(lightType="spotLight"):
	""""""
	Use_Look_At_Selection =  Util_General.OptionVar("AW_Model_Editor_View_Object_Creation_Use_Look_At_Selection", val=0)
	Use_Look_Through =  Util_General.OptionVar("AW_Model_Editor_View_Object_Creation_Use_Look_Through", val=1)
	
	active_Selection = cmds.ls(long=True,sl=True)
	model_panel = get_Model_Panel()
	cam         = get_panel_cam(model_panel)
	light       = create_light_from_cam(cam,lightType)
	
	cmds.select(active_Selection)
	
	if Use_Look_Through.value:
		look_Through_Object(light,model_panel.name())
	if Use_Look_At_Selection.value:
		pm.viewLookAt(cam)

def make_Run_Time_Commands():
	global _run_time_commands
	for item_list in _run_time_commands:
		t, n, c, f =  item_list
		if not cmds.runTimeCommand(c, exists=True):
			cmds.runTimeCommand(c, annotation="Create A " + n + " At The Active View In The Modle Editor", command=f, category="User", commandLanguage="python", default=True)

def make_Model_Editor_Menu_Items(parent_menu, editor=None):
	global _run_time_commands
	cmds.setParent(parent_menu, m=True)
	if not cmds.menu(parent_menu, q=True, ni=True):
		cmds.menuItem(label="Create Light", subMenu=True, tearOff=True)
		for item_list in _run_time_commands:
			t, n, c, f =  item_list
			cmds.menuItem(label=n, command=f, sourceType="python")
