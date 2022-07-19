
#Creation Date:  (December 1, 2006)

#Author: John Creson
import maya.cmds as cmds
import maya, os, sys, fnmatch
from pathlib2 import Path
import re
_aw_python_scripts_menu_name  = "aw_user_tools_menu"
_aw_python_scripts_menu_label = "AW User Tools"
if os.environ.has_key("MAYA_USER_TOOLS_DIR"):
	_aw_user_tools_main_folder    = Path(os.path.expandvars(os.environ["MAYA_USER_TOOLS_DIR"]))
else:
	_aw_user_tools_main_folder = ""

def findFile(path):
	#Find the file named path in the sys.path.
	#Returns the full path name if found, None if not found
	for dirname in sys.path:
		possible = os.path.join(dirname, path)
		if os.path.isfile(possible):
			# print dirname
			return dirname
	# print ("None")
	return None

def gen_pythonScripts(mainDir, pMenu, depth=0):
	# this looks in the folder where this script is run from and generates the
	# cascading menues and Python script buttons
	mainDir = Path(mainDir)
	ignors  = ["__init__.py", "userSetup.py", "pythonScripts.py",".idea",".gitignore",".git"]
	files   = [f for f in mainDir.glob("*.py") if not f.parts[-1] in ignors]
	try:
		folders = [folder for folder in mainDir.iterdir(True) if not folder.baseName.startswith(".")]
	except:
		folders = [folder for folder in mainDir.iterfolders() if not folder.baseName.startswith(".")]
	folders = sorted(folders)
	
	gMainProgressBar = get_main_progress_bar()


	for current_file in files:
		isinstance(current_file, Path)
		if(cmds.progressBar (gMainProgressBar, query=True, isCancelled=True)):
			break
		if(cmds.progressBar(gMainProgressBar, q=True, pr=True)  == 100):
			cmds.progressBar (gMainProgressBar, e=True, pr=1)
		
		data = current_file.read_text()
		mch = re.search("def " + current_file.baseName + ".*\(.*\)", data)
		if mch != None:
			if mch.group().replace("def ", "").split("(")[0] == current_file.baseName:
				label    =  " ".join(current_file.baseName.split("_"))
				baseName = str(current_file.baseName)
				cmds.progressBar (gMainProgressBar, edit=True, step=1)
				cmds.progressBar (gMainProgressBar, e=True, status=("Adding: "+baseName) )
				pyMenuItem = cmds.menuItem ( parent=pMenu, label=label, command='Maya_UserTools.importAndRun ("%(baseName)s")' % vars() )
	
	for current_folder in folders:
		isinstance(current_folder, Path)
		if(cmds.progressBar (gMainProgressBar, query=True, isCancelled=True)):
			break
		files   = [f for f in mainDir.glob("*.py") if not f.parts[-1] in ignors]
		check = False
		if current_folder.parent.baseName == "Maya_User_Tools":
			check = True
		else:
			for current_file in files:
				data = current_file.read_text()
				mch = re.search("def " + current_file.baseName + ".*\(.*\)", data)
				if mch != None:
					if mch.group().replace("def ", "").split("(")[0] == current_file.baseName:
						check = True
						break
		if check and depth == 0:
			menuName = "_".join(current_folder.baseName.split())
			menuName = ("empt_" + menuName + "_menu")
			label    =  " ".join(current_folder.baseName.split("_"))
			menu     = cmds.menuItem(menuName, subMenu=True, aob=1, tearOff=True, parent=pMenu, label=label)
			#This adds the folder into the PythonPath
			if not str(current_folder) in sys.path:
				sys.path.append(str(current_folder))

			#start new can scan
			gen_pythonScripts (current_folder, menuName, depth+1)
		else:
			if not str(current_folder) in sys.path:
				sys.path.append(str(current_folder))
			gen_pythonScripts (current_folder, pMenu, depth+1)
def importAndRun(scrpt):
	# create the Python command that is invoked by the menu item
	# This could be changed to scrpt.main if that is normal
	# The reload command should have a way of being turned off and on from the UI
	exec 'import ' + scrpt
	if not scrpt in ["Align_Objects"]:
		exec  'reload (' + scrpt + ')'
	if scrpt == "Maya_UserTools":
		exec scrpt + '.pythonScripts()'
	else:
		exec scrpt + '.' + scrpt + '()'

def menu_exist(menu_name):
	return cmds.menu(menu_name, exists=True)

def delete_menu(menu_name):
	if menu_exist(menu_name):
		cmds.deleteUI(menu_name)

def create_menu(menu_name, label, parent, tearOff=True, aob=True):
	Menu = cmds.menu (menu_name, parent=parent, tearOff=tearOff, aob=aob, label=label)
	return Menu

def get_main_window():
	gMainWindow = maya.mel.eval('$temp1=$gMainWindow')
	return gMainWindow

def get_main_progress_bar():
	gMainProgressBar = maya.mel.eval('$temp=$gMainProgressBar')
	return gMainProgressBar

def pythonScripts():
	global _aw_python_scripts_menu_name, _aw_python_scripts_menu_label, _aw_user_tools_main_folder
	delete_menu(_aw_python_scripts_menu_name)
	gMainWindow = get_main_window()
	gMainProgressBar = get_main_progress_bar()
	if not str(_aw_user_tools_main_folder) in sys.path:
		sys.path.append(str(_aw_user_tools_main_folder))
	mainDir = _aw_user_tools_main_folder
	timer = maya.mel.eval('timerX')
	try:
		cmds.waitCursor (state=True)
		cmds.progressBar(
			gMainProgressBar,
			edit=True,
			beginProgress=True,
			isInterruptable=True,
			status="Creating pythonScripts...",
			maxValue=100)
	
		pMenu = create_menu(_aw_python_scripts_menu_name, _aw_python_scripts_menu_label, parent=gMainWindow, tearOff=True, aob=True)
		pyMenuItem = cmds.menuItem ( parent=pMenu, label="Rebuild Menu", command='Maya_UserTools.importAndRun ("Maya_UserTools")' )
		if len(str(mainDir)):
			gen_pythonScripts(mainDir, pMenu)
	except:
		cmds.warning("User Tools Failed To Load")
	cmds.waitCursor (state=False)

	endTime = maya.mel.eval('timerX -st %(timer)s' % vars())

	cmds.progressBar (gMainProgressBar, edit=True,endProgress=True,)

	# print ("pythonScripts has now been updated in: " + str(endTime) + " seconds...!")
