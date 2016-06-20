import os
import maya.cmds  as cmds
import maya.utils as utils
import maya.mel   as mel
import Scripts
from Environment_Access import System_Paths, System_Settings, utilities

if System_Settings.USE_WING_DEBUG:
	try:
		import wingdbstub
	except:
		pass
	
MAYA_VERSION           = int(cmds.about(version=True))
MAYA_BATCH             = cmds.about(b=True)
MAYA_GUI               = False if MAYA_BATCH else True 
os.environ["MAYA_GUI"] = "1" if MAYA_GUI else "0"
os.environ["QT_PACKAGE"] = "PySide" if MAYA_VERSION >= 2013 else "PyQt4"

if MAYA_GUI:
	utilities.add_To_System_Path(System_Paths._CODE_AW_SITE_PACKAGES)
	if MAYA_VERSION == 2015:
		cmds.setStartupMessage(os.path.join(System_Paths._CODE_MAYA_XBM_PATH , "MayaStartupImage.png"))
		#----------------------------------------------------------------------
		utilities.add_To_Multi_Path_Environment_Key("MAYA_SCRIPT_PATH", [System_Paths._CODE_MAYA_SCRIPT_PATH, System_Paths._CODE_MAYA_SCRIPT_PATH_2015, System_Paths._CODE_MAYA_BONUS_TOOLS_MEL, System_Paths._CODE_MAYA_BONUS_TOOLS_MEL_2015])
		#----------------------------------------------------------------------
		utilities.add_To_Multi_Path_Environment_Key("XBMLANGPATH", [System_Paths._CODE_MAYA_BONUS_TOOLS_ICONS, System_Paths._CODE_MAYA_XBM_PATH])
		#----------------------------------------------------------------------
		utilities.add_To_System_Path(System_Paths._CODE_MAYA_BONUS_TOOLS_PYTHON)
		utilities.add_To_System_Path(System_Paths._CODE_MAYA_BONUS_TOOLS_PYTHON_2014)
		utilities.add_To_System_Path(System_Paths._CODE_MAYA_BONUS_TOOLS_PYTHON_2015)
		if not System_Settings.NO_USER_TOOLS:
			utilities.add_To_System_Path(System_Paths.MAYA_USER_TOOLS_DIR)
			utils.executeDeferred ('mel.eval("bonusToolsMenu")')
	if not System_Settings.NO_USER_TOOLS:
		utils.executeDeferred ('import Scripts.global_Shelf_Builder')
		utils.executeDeferred ('import Maya_UserTools; Maya_UserTools.pythonScripts()')
		utils.executeDeferred ('import Scripts.callbacks')
		utils.executeDeferred ('import Scripts.Maya_Runtime_Commands')
	# utils.executeDeferred ('import Scripts.Tools.Selection_Set_Manager.Selection_Set_Editor_Loader; G_Selection_Set_Editor = Scripts.Tools.Selection_Set_Manager.Selection_Set_Editor_Loader.Load_Editor()')
