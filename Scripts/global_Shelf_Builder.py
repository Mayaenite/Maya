import maya.mel
from maya import cmds
import pymel.core as pm
import os

MAYA_VERSION           = int(cmds.about(version=True))

"MayaWindow|mainSelectMenu|selAllHierItem"
def get_Top_Level_Shelf():
	res = pm.melGlobals['gShelfTopLevel']
	return res

def get_Shelf_Form():
	res = pm.melGlobals['gShelfForm']
	return res

def getShelfStyle(shelfTab=""):
	if shelfTab == "":
		return cmds.optionVar(q='shelfItemStyle')
	else:
		kids=cmds.tabLayout(shelfTab,q=1,ca=1)
		if len(kids)>0:
			shelfTab = shelfTab + "|" + kids[0]
			return cmds.shelfLayout(shelfTab,q=1,style=1)
		else:
			return cmds.optionVar(q='shelfItemStyle')

def shelfStyle(shelfLayout, style="nochange",size="nochange"):
	width=0
	height=0
	h=0
	curSize=0
	boxWidth=0
	temp=0
	curStyle=''
	
	if style == "nochange":
		style=cmds.optionVar(q='shelfItemStyle')
	if size == "nochange":
		size=cmds.optionVar(q='shelfItemSize')	
	if not size in ["Large", "Medium", "Small"]:
		if size == "small":
			size="Small"
		elif size == "medium":
			size="Medium"	
		elif size == "large":
			size="Large"
		else:
			size="Small"
	if style == "textOnly":
		width=120
		height=20
		h=26
		boxWidth=500
	elif style == "iconAndTextHorizontal":
		if size == "Small":
			width=150
			height=34
			h=40
			boxWidth=504		
		elif size == "Medium":
			width=128
			height=48
			h=54
			boxWidth=505
		elif size == "Large":
			width=144
			height=64
			h=70
			boxWidth=506
	elif style == "iconAndTextVertical":
		if size == "Small":
			width=122
			height=54
			h=60
			boxWidth=507
		elif size == "Medium":
			width=80
			height=68
			h=74
			boxWidth=508
		elif size == "Large":
			width=80
			height=84
			h=90
			boxWidth=509
	elif style == "iconOnly":
		if size == "Small":
			width=34
			height=34
			h=40
			boxWidth=501
		elif size == "Medium":
			width=48
			height=48
			h=54
			boxWidth=502
		elif size == "Large":
			width=64
			height=64
			h=70
			boxWidth=503
	else:
		style="iconOnly"
		if size == "Small":
			width=34
			height=34
			h=40
			boxWidth=501
		elif size == "Medium":
			width=48
			height=48
			h=54
			boxWidth=502		
		elif size == "Large":
			width=64
			height=64
			h=70
			boxWidth=503
	cmds.shelfLayout(shelfLayout,cwh=(width, height),h=h,e=1,st=style)

def remove_optional_variables(shelfName):
	nShelves =cmds.optionVar(q='numShelves')
	shelf_num = 0
	shelf_found = False
	while shelf_num <= nShelves:
		if not shelf_found:
			if shelfName == cmds.optionVar(q='shelfName%i' % shelf_num):
				shelfLoad_key = "shelfLoad" + str(shelf_num)
				shelfName_key = "shelfName" + str(shelf_num)
				shelfFile_key = "shelfFile" + str(shelf_num)
				cmds.optionVar(remove=shelfLoad_key)
				cmds.optionVar(remove=shelfName_key)
				cmds.optionVar(remove=shelfFile_key)
				shelf_found = True
		if shelf_found:
			old_shelfLoad_key = "shelfLoad" + str(shelf_num)
			old_shelfName_key = "shelfName" + str(shelf_num)
			old_shelfFile_key = "shelfFile" + str(shelf_num)
			new_shelfLoad_key = "shelfLoad" + str(shelf_num+1)
			new_shelfName_key = "shelfName" + str(shelf_num+1)
			new_shelfFile_key = "shelfFile" + str(shelf_num+1)
			cmds.optionVar(iv=[old_shelfLoad_key, cmds.optionVar(q=new_shelfLoad_key)])
			cmds.optionVar(sv=[old_shelfName_key, cmds.optionVar(q=new_shelfName_key)])
			cmds.optionVar(sv=[old_shelfFile_key, cmds.optionVar(q=new_shelfFile_key)])
		
		shelf_num += 1
	shelfLoad_key = "shelfLoad" + str(nShelves)
	shelfName_key = "shelfName" + str(nShelves)
	shelfFile_key = "shelfFile" + str(nShelves)
	cmds.optionVar(remove=shelfLoad_key)
	cmds.optionVar(remove=shelfName_key)
	cmds.optionVar(remove=shelfFile_key)
	cmds.optionVar(iv=["numShelves",nShelves-1])

def set_optional_Varables(shelfName):
	nShelves =cmds.optionVar(q='numShelves')
	nShelves+=1
	shelfLoad_key  = "shelfLoad" + str(nShelves)
	shelfName_key  = "shelfName" + str(nShelves)
	shelfFile_key  = "shelfFile" + str(nShelves)
	shelfFile_name = "shelf_"    + shelfName
	cmds.optionVar(iv=['numShelves', nShelves])
	cmds.optionVar(iv=[shelfLoad_key, 0])
	cmds.optionVar(sv=[shelfName_key, shelfName])
	cmds.optionVar(sv=[shelfFile_key, shelfFile_name])

def addNewShelfTab(newName):
	#
	#  Description:
	#		This method adds the shelf layout to the tab layout. Due to the
	#		ornary nature of the shelf/grid it causes mutch geometry negotiations.
	#		As a workaround a separator widget is used as a place holder while the
	#		tab layout is unmanaged.  This causes a blink but this is far preferable
	#		to the resizing that takes place otherwise.
	#
	gShelfTopLevel = get_Top_Level_Shelf()
	gShelfForm     = get_Shelf_Form()
	style          = getShelfStyle(gShelfTopLevel)
	shelfName      = ''
	newShelfName   = ''
	shelfHeight    = cmds.tabLayout(gShelfTopLevel,q=1,h=1)
	
	cmds.tabLayout(gShelfTopLevel,edit=1, visible=False)
	
	cmds.setParent(gShelfForm)
	cmds.separator('spacingSeparator',h=shelfHeight,style="single")
	
	cmds.formLayout(gShelfForm,edit=1,
	                af=[('spacingSeparator', 'top', 0),
	                    ('spacingSeparator', 'left', 0),
	                    ('spacingSeparator', 'bottom', 0),
	                    ('spacingSeparator', 'right', 0)])
	
	cmds.tabLayout(gShelfTopLevel, edit=1, manage=False)
	
	cmds.setParent(gShelfTopLevel)
	
	if newName == "":
		newShelfName=cmds.shelfLayout()
	else:
		newShelfName=cmds.shelfLayout(newName)
		
	# Match the style of the other tabs
	shelfStyle(newShelfName, style, "Small")
	
	cmds.tabLayout(gShelfTopLevel, edit=1, visible=True,manage=True)
	
	shelfName=cmds.tabLayout(gShelfTopLevel,q=1,ca=1)[-1]
	
	if not pm.mel.exists('shelfLabel_melToUI'):
		pm.mel.source("shelfLabel.mel")
	
	shelf_label = pm.mel.shelfLabel_melToUI(shelfName)
	pm.shelfTabLayout(gShelfTopLevel,
	                  edit=1,
	                  tabLabel=(shelfName, shelf_label)
	                  )
	#
	# If the user has created a new shelf with the same name as the 
	# default shelves like Animation, Curves, Surfaces, Polygons ..., 
	# edit the tab label to set the localized name in the UI
	#
	pm.deleteUI('spacingSeparator')
	#  Do that preference thang.
	#
	set_optional_Varables(shelfName)
	## Save shelf file to shelves directory
	##
	#shelfDir=cmds.about(preferences=True)+"/prefs/shelves/"
	## Make sure we are using the shelves directory.
	#pm.saveShelf(newShelfName,(shelfDir + "shelf_" + shelfName))
	return shelfName

def removeShelfTab(shelfName):
	if cmds.shelfLayout(shelfName,exists=True):
		childArray = cmds.shelfLayout(shelfName,query=True,childArray=True)
		if isinstance(childArray,list):
			for bnt in cmds.shelfLayout(shelfName,query=True,childArray=True):
				cmds.deleteUI(bnt,control=True)
		cmds.deleteUI(shelfName,layout=True)
		remove_optional_variables(shelfName)
		
		shelfDir=cmds.about(preferences=True)+"/prefs/shelves/"
		shelf_file = os.path.join(shelfDir, str("shelf_" + shelfName + ".mel") )
		if os.path.exists(shelf_file):
			os.remove(shelf_file)

def Build_DataPrep_Tools(shelfName):
	active_shelf = shelfName
	removeShelfTab(active_shelf)
	addNewShelfTab(active_shelf)
	# polyAutoProjection
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "poly Auto Projections"
		    ,label      = "polyAutoProjection"
		    ,image      = "polyLayoutUV.png"
		    ,image1     = "polyLayoutUV.png"
		    ,style      = "iconOnly"
		    ,command    = "aw_Box_Map_Selected_RTC" 
		    ,sourceType = "mel")
	# polyNormal
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "Reverses The Normals On All The Currently Selected PolyTransforms"
		    ,label      = "polyNormal"
		    ,image      = "polyNormal.png"
		    ,image1     = "polyNormal.png"
		    ,style      = "iconOnly"
		    ,command    = "{\n    int $history_check = `constructionHistory -q -tgl`;\n    \n    string $selList[] = `ls -transforms -sl`;\n    \n    string $item;\n    \n    constructionHistory -tgl off;\n    \n    for($item in $selList){\n        select -r $item;\n        string $itemShapes[] = `pickWalk -d down`;\n        \n        if(`objectType -isType \"mesh\" $itemShapes[0]`){\n            select -r $item;\n            polyNormal -constructionHistory off -normalMode 04;\n        };\n    };\n    \n    select -r $selList;\n    \n    if($history_check == 1){\n        constructionHistory -tgl on;\n    };\n}" 
		    ,sourceType = "mel" )
	# ZB2MA
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "Transfer UV Cords From Zbrush To Maya" 
		    ,label      = "ZBrush To Maya"
		    ,image      = "ZBrush.png"
		    ,image1     = "ZBrush.png"
		    ,style      = "iconOnly"
		    ,command    = "Maya_UserTools.importAndRun ('Zbrush_To_Maya')"
		    ,sourceType = "python" )
	# Display_Layers_To_Selection_Sets
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "Display Layers To Selection Sets"
		    ,label      = "Display_Layers_To_Selection_Sets"
		    ,image      = "layerEditor.png"
		    ,image1     = "layerEditor.png"
		    ,style      = "iconOnly"
		    ,command    = "import Scripts.LayerFns.Layers_To_Sets\nScripts.LayerFns.Layers_To_Sets.Display_Layers_To_Selection_Sets()" 
		    ,sourceType = "python" )
	# Find_Innersecting_Display_Layers
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "Find All Innersecting Display layers"
		    ,label      = "Find_Innersecting_Display_Layers"
		    ,image      = "intersectCurves.png"
		    ,image1     = "intersectCurves.png"
		    ,style      = "iconOnly"
		    ,command    = "import Scripts.LayerFns.Layers_To_Sets\nScripts.LayerFns.Layers_To_Sets.Display_Layers_To_Selection_Sets()\nDisplay_Layers_To_Selection_Sets = Scripts.NodeCls.M_Nodes.SelectionSet(\"Display_Layers_To_Selection_Sets\")\nDisplay_Layers_To_Selection_Sets.Find_All_Sub_Set_Innersecting_Sets()" 
		    ,sourceType = "python" )
	# Assine_Tranforms_To_Closet_Group_Display_Layer
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "Assine Tranforms With Child Shape Nodes To The Closet Parent Group Display Layer"
		    ,label      = "Assine_Tranforms_To_Closet_Group_Display_Layer"
		    ,image      = "pythonFamily.png"
		    ,image1     = "pythonFamily.png"
		    ,style      = "iconOnly"
		    ,sourceType = "python"
		    ,menuItem   = (("Tranforms To Closet Group DL" , "import Scripts.LayerFns.Display_layer_Reasinment\nScripts.LayerFns.Display_layer_Reasinment.Assine_Tranforms_To_Closet_Group_Display_Layer()"), ("Group Tranforms To Default Display Layer", "import Scripts.LayerFns.Display_layer_Reasinment\nScripts.LayerFns.Display_layer_Reasinment.Assine_Group_Tranforms_To_Default_Display_Layer()"))
		    ,menuItemPython = (0, 1))
	# Alembic_Asset_Extraction
	cmds.shelfButton(parent=active_shelf
		    ,annotation = "Alembic_Asset_Extraction"
		    ,label      = "Alembic_Asset_Extraction"
		    ,image      = "alembic_asset_extractor.png"
		    ,image1     = "alembic_asset_extractor.png"
		    ,style      = "iconOnly"
	        ,menuItem   = (("Export" , "import Scripts.Tools.Asset_Extraction\nScripts.Tools.Asset_Extraction.Alembic_Asset_Extraction.Alembic_Asset_Writer()"), ("Import", "import Scripts.Tools.Asset_Extraction\nScripts.Tools.Asset_Extraction.Alembic_Asset_Extraction.Alembic_Asset_reader()")), 
		    # ,command    = "import Scripts.Tools.Asset_Extraction\nScripts.Tools.Asset_Extraction.Alembic_Asset_Extraction.Asset_Extractor()"
	        menuItemPython = (0, 1),
		    sourceType = "python" )
	# Alembic Asset Extraction V2
	cmds.shelfButton(parent=active_shelf
	        ,annotation = "Alembic Asset Extraction V2"
	        ,label      = "Alembic Asset Extraction V2"
	        ,image      = "ATB.jpg"
	        ,image1     = "ATB.jpg"
	        ,style      = "iconOnly"
	        ,command    = "import Scripts.Tools.Asset_Extraction.Alembic_Asset_Extraction_V2_GUI\nreload(Scripts.Tools.Asset_Extraction.Alembic_Asset_Extraction_V2_GUI)\nScripts.Tools.Asset_Extraction.Alembic_Asset_Extraction_V2_GUI.load_Gui()"
	        ,sourceType = "python" )
	# Visibility_Connect_Maker
	cmds.shelfButton(parent=active_shelf
	        ,annotation = "Connect The Visibility Of The Currently Selected Nodes To The Last Node Selected"
	        ,label      = "Visibility_Connect_Maker"
	        ,image      = "pythonFamily.png"
	        ,image1     = "pythonFamily.png"
	        ,imageOverlayLabel = "VC" 
	        ,style      = "iconOnly"
	        ,command    = "import pymel.core as pm\n\nselection = pm.ls(selection = True)\nmemberSet = selection[:-1]\ncontroller = selection[-1]\n\nfor item in memberSet:\n    print item, pm.nodeType(item)\n    if pm.nodeType(item) == 'transform':\n       pm.connectAttr( controller.visibility, item.visibility )"
	        ,sourceType = "python" )
	# SeperatePolyByShader
	cmds.shelfButton(parent=active_shelf
	        ,annotation = "Seperate Selected Polys By There Face Shading Assinments"
	        ,label      = "Seperate Poly By Shader"
	        ,image      = "polySeparate.png"
	        ,image1     = "polySeparate.png"
	        ,style      = "iconOnly"
	        ,command    = "SeperatePolyByShader"
	        ,sourceType = "mel" )
	# SeperatePolyByShader
	cmds.shelfButton(parent=active_shelf
	        ,annotation = "Does Some Cool Stuff"
	        ,label      = "Planar Proj Unforld"
	        ,image      = "easybutton.jpg"
	        ,image1     = "easybutton.jpg"
	        ,style      = "iconOnly"
	        ,command    = "Planar_Proj_Unforld_RTC"
	        ,sourceType = "mel" )
	# AW Poly Unite
	cmds.shelfButton(parent=active_shelf
	        ,annotation = "Runs Poly Unite On The Selected Objects\nIf The Objects Selected Belong To Different Display Layers Or Different Parents\n A Window Will Pop Up For You To Set The New Object To\n Other wise The Resault Will Be Reparented And Reassined To Its\nOrignal Parent And Layer"
	        ,label      = "AW Poly Unite"
	        ,image      = "polyUnite.png"
	        ,image1     = "polyUnite.png"
	        ,style      = "iconOnly"
	        ,command    = "aw_Poly_Unite_RTC"
	        ,sourceType = "mel" )	
def Build_Artist_Tools(shelfName):
	active_shelf = shelfName
	removeShelfTab(active_shelf)
	addNewShelfTab(active_shelf)
	# Maya Mat Replace
	cmds.shelfButton(parent=active_shelf
		,annotation="Maya Mat Replace" 
		,label="maya_mat_replace_v05" 
		,imageOverlayLabel="MMR" 
		,image="materialEditor.png" 
		,image1="materialEditor.png" 
		,style="iconOnly" 
		,command="import dmf_scripts.maya_mat_replace_v05\nreload(dmf_scripts.maya_mat_replace_v05)\ndmf_scripts.maya_mat_replace_v05.main()" 
		,sourceType="python")
	# Asset Assembly System
	cmds.shelfButton(parent=active_shelf
	         ,annotation="Asset Assembly System" 
	         ,image="Assembly_Model.png" 
	         ,image1="Assembly_Model.png" 
	         ,style="iconOnly" 
	         ,command="if not os.path.join(System_Paths.AW_COMMON_UTILITIES,'Other') in os.sys.path:\n\tos.sys.path.append(os.path.join(System_Paths.AW_COMMON_UTILITIES,'Other'))\nimport AW_Asset_Assembly_System.Simple_Main_Window\n_G_Asset_Assembly_System_UI = AW_Asset_Assembly_System.Simple_Main_Window.load_main_window()"
	         ,sourceType="python")
	# Vray Scene States Manager
	cmds.shelfButton(parent=active_shelf
            ,annotation="Vray Scene States Manager" 
            ,image="vray_scene_states_manager.png" 
            ,image1="vray_scene_states_manager.png" 
            ,style="iconOnly" 
            ,command="import Scripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Manager\nScripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Manager.make_ui()"
            ,sourceType="python")
	# Vray Scene States Viewer
	# cmds.shelfButton(parent=active_shelf
            # ,annotation="Vray Scene States Viewer\nHOLD DOWN\nCTRL + ALT + SHIFT\nTO FORCE THE VIEWER TO REBUILD ITSELF AND REPARSE THE YAML DATA\nYou Can Also Do This To Switch Between The Different Versions" 
            # ,image="vray_scene_states_viewer.png" 
            # ,image1="vray_scene_states_viewer.png" 
            # ,style="iconOnly" 
            # ,command="import Scripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Viewer\nScripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Viewer.make_ui()"
            # ,sourceType="python")
	# Vray Scene States Viewer Beta
	cmds.shelfButton(parent=active_shelf
	         ,annotation="Vray Scene States Viewer Beta Lists\nTo Use Double Click On Any Of The States In The List\nTo Assign That State To The Current Render Layer\nHOLD DOWN\nCTRL + ALT + SHIFT\nTO FORCE THE VIEWER TO REBUILD ITSELF AND REPARSE THE YAML DATA"
	         ,image="vray_scene_states_viewer_beta.png" 
	         ,image1="vray_scene_states_viewer_beta.png" 
	         ,style="iconOnly" 
	         ,command="import Scripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Viewer\nScripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Viewer.make_ui(True)"
	         ,sourceType="python")
	# Deadline_Submiter
	cmds.shelfButton(parent=active_shelf
            ,annotation="Deadline Submiter"
            ,label     = "Submit To Deadline"
            ,imageOverlayLabel="" 
            ,image  = "Submit_To_Deadline.png"
            ,image1 = "Submit_To_Deadline.png"
            ,style="iconOnly" 
            ,command="SubmitJobToDeadline"
            ,sourceType="mel")		
	# AW Camera Snap
	cmds.shelfButton(parent=active_shelf
        ,annotation="takes a list of selected cameras in your scene as an input\n and creates a new camera with an animation path that moves through the position of each of the original"
        ,label     = "Camera Snap"
        ,image      = "CameraSnap.png"
        ,image1     = "CameraSnap.png" 
        ,imageOverlayLabel="csnp" 
        ,command="print(\"Camera Snap Tool\");\nsource \"CameraSnap.mel\";\nCameraSnap(1);\n" 
        ,sourceType="mel")
	# AW Camera Snap
	cmds.shelfButton(parent=active_shelf
        ,annotation="Selection Set Helper Tool"
        ,label     = "SSM"
        ,image      = "Selection_Set_Manager.png"
        ,image1     = "Selection_Set_Manager.png"
	    , version   = 2015
        ,imageOverlayLabel="ssm"
        ,command="import Scripts.Tools.Selection_Set_Manager.Selection_Set_Editor_Loader\nG_Selection_Set_Editor = Scripts.Tools.Selection_Set_Manager.Selection_Set_Editor_Loader.Load_Editor()" 
        ,sourceType="python")

#def Add_Custom_Menu_Items():
	#if MAYA_VERSION == 2017 or MAYA_VERSION == 2016:
		#maya.mel.eval('buildSelectMenu("MayaWindow|mainSelectMenu");')
		#Select_All_By_Type_MenuItem = "MayaWindow|mainSelectMenu|selAllHierItem"
	#else:
		#maya.mel.eval('buildEditMenu("MayaWindow|mainEditMenu");')
		#Select_All_By_Type_MenuItem = "MayaWindow|mainEditMenu|selAllHierItem"
		
	#maya.mel.eval('ModObjectsMenu MayaWindow|mainModifyMenu;')
	
	#Modify_Menu =  "MayaWindow|mainModifyMenu"
	
	#aw_HOT_PIVOT_ACTION = cmds.menuItem( annotation="Reset The Selected Trasform Matrix", command='aw_HOT_PIVOT_ACTION;', image="menuIconModify.png", label="HOT PIVOT ACTION", version="2015", parent=Modify_Menu, sourceType="mel")
	#SelLocatorItem      = cmds.menuItem( annotation="Select All Locator Transforms", command='cmds.select(cmds.listRelatives(cmds.ls(typ="locator"),parent=True,typ="transform",fullPath=True))', image="locator.png", label="Locators", version="2015", parent=Select_All_By_Type_MenuItem, sourceType="python")
	
removeShelfTab("Old_AW_DP_Tools")
removeShelfTab("Old_AW_CG_Tools")
# removeShelfTab("Deadline")
Build_DataPrep_Tools("AW_DP_Tools")
Build_Artist_Tools("AW_CG_Tools")
#Add_Custom_Menu_Items()
