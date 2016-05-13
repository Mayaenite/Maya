import os
USE_WING_DEBUG = int(os.environ.get("USE_WING_DEBUG", 0))
# if USE_WING_DEBUG:
	# try:
		# import wingdbstub
	# except:
		# pass
#----------------------------------------------------------------------
def _path_fixer(path):
	"""File Path Standerizer"""
	path = os.path.expandvars(path)
	return path.replace("\\", "/")

#----------------------------------------------------------------------
def get_and_set_environ_key_path(key, default, add_to_path=False, fource_default=False, fource_check=None):
	""""""
	res = _path_fixer(os.environ.get(key, default))
	if fource_default and callable(fource_check):
		if fource_check(res):
			res = _path_fixer(default)
	elif fource_default:
		res = _path_fixer(default)

	if add_to_path:
		if os.path.exists(res) and not res in os.sys.path:
			os.sys.path.append(res)
	os.environ[key] = res
	return res

MAYA_GUI = False
NO_USER_TOOLS = os.environ.get("NO_USER_TOOLS", "0")
os.environ["MAYA_GUI"] = "0"

#----------------------------------------------------------------------
AW_BASE                = get_and_set_environ_key_path("AW_BASE", os.path.realpath(os.path.dirname(__file__)+"/.."), add_to_path=True, fource_default=False)
#----------------------------------------------------------------------
AW_SITE_PACKAGES       = get_and_set_environ_key_path("AW_SITE_PACKAGES", "//Blue/app_config/python/AW_site_packages", add_to_path=True)
#----------------------------------------------------------------------
AW_MAYA_SCRIPT_PATH    = get_and_set_environ_key_path("MAYA_SCRIPT_PATH", os.path.join(AW_BASE, "Maya", "Mel"), add_to_path=False, fource_default=False)
#----------------------------------------------------------------------
AW_XBM_LANG_PATH       = get_and_set_environ_key_path("XBMLANGPATH", os.path.join(AW_BASE, "Maya", "icons"), add_to_path=False, fource_default=False)
#----------------------------------------------------------------------
if NO_USER_TOOLS == '0':
	AW_MAYA_USER_TOOLS_DIR = get_and_set_environ_key_path("MAYA_USER_TOOLS_DIR","//Blue/app_config/Git_Live_Code/User_Tools/Maya_User_Tools", add_to_path=True)
	
try:
	import maya.cmds as cmds
	import maya.utils as utils
	import maya.mel
	MAYA_VERSION           = int(cmds.about(version=True))
	MAYA_BATCH             = cmds.about(b=True)
	MAYA_GUI              = False if MAYA_BATCH else True 
	os.environ["MAYA_GUI"] = "1" if MAYA_GUI else "0"
	os.environ["QT_PACKAGE"] = "PySide" if MAYA_VERSION >= 2013 else "PyQt4"
except:
	pass

if MAYA_GUI:
	cmds.setStartupMessage(os.path.join(AW_BASE, "Maya", "icons", "MayaStartupImage.png"))
	if MAYA_VERSION == 2015:
		#----------------------------------------------------------------------
		temp_paths = os.environ.get("MAYA_SCRIPT_PATH", "") + ";" + _path_fixer(os.path.join(AW_BASE, "Maya", "Mel", "2015"))
		AW_MAYA_SCRIPT_PATH    = os.environ["MAYA_SCRIPT_PATH"] = temp_paths
		#----------------------------------------------------------------------
		MEL_MAYA_BONUS_TOOLS = os.path.join(AW_BASE, "Maya", "Mel", "2015", "MayaBonusTools", "Contents", "scripts-2015")
		MEL_MAYA_BONUS_TOOLS += ";" + os.path.join(AW_BASE, "Maya", "Mel", "2015", "MayaBonusTools", "Contents", "scripts")
		os.environ["MAYA_SCRIPT_PATH"] = os.environ["MAYA_SCRIPT_PATH"] + ";" + MEL_MAYA_BONUS_TOOLS
		
		BONUS_TOOLS_ICONS    = get_and_set_environ_key_path("BONUS_TOOLS_ICONS", os.path.join(AW_BASE, "Maya", "Mel", "2015", "MayaBonusTools", "Contents", "icons"), add_to_path=False, fource_default=True)
		os.environ["XBMLANGPATH"] = os.environ["XBMLANGPATH"] + ";" + BONUS_TOOLS_ICONS
		#----------------------------------------------------------------------
		_MAYA_BONUS_TOOLS = [os.path.join(AW_BASE, "Maya", "Mel", "2015", "MayaBonusTools", "Contents", "python-2015")]
		_MAYA_BONUS_TOOLS.append(os.path.join(AW_BASE, "Maya", "Mel", "2015", "MayaBonusTools", "Contents", "python"))
		for p in _MAYA_BONUS_TOOLS: 
			if os.path.exists(p) and not p in os.sys.path:
				os.sys.path.append(p)
		if NO_USER_TOOLS == '0':
			utils.executeDeferred ('maya.mel.eval("bonusToolsMenu")')
	if NO_USER_TOOLS == '0':
		utils.executeDeferred ('import Scripts.global_Shelf_Builder')
		utils.executeDeferred ('import Maya_UserTools; Maya_UserTools.pythonScripts()')
		utils.executeDeferred ('import Scripts.callbacks')
		utils.executeDeferred ('import Scripts.Maya_Runtime_Commands')
	# utils.executeDeferred ('import Scripts.Tools.Selection_Set_Manager.Selection_Set_Editor_Loader; G_Selection_Set_Editor = Scripts.Tools.Selection_Set_Manager.Selection_Set_Editor_Loader.Load_Editor()')
