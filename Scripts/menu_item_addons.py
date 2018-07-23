import pymel.core as pm
import maya.cmds as cmds
import maya.mel
import maya.utils as utils


MAYA_VERSION           = int(cmds.about(version=True))

def Add_Custom_Menu_Items():
	if MAYA_VERSION != 2015:
		maya.mel.eval('buildSelectMenu("MayaWindow|mainSelectMenu");')
		Select_All_By_Type_MenuItem = "MayaWindow|mainSelectMenu|selAllHierItem"
	else:
		maya.mel.eval('buildEditMenu("MayaWindow|mainEditMenu");')
		Select_All_By_Type_MenuItem = "MayaWindow|mainEditMenu|selAllHierItem"
		
	maya.mel.eval('ModObjectsMenu MayaWindow|mainModifyMenu;')
	
	Modify_Menu =  "MayaWindow|mainModifyMenu"
	
	aw_HOT_PIVOT_ACTION = cmds.menuItem( annotation="Reset The Selected Trasform Matrix", command='aw_HOT_PIVOT_ACTION;', image="menuIconModify.png", label="HOT PIVOT ACTION", version="2015", parent=Modify_Menu, sourceType="mel")
	SelLocatorItem      = cmds.menuItem( annotation="Select All Locator Transforms", command='cmds.select(cmds.listRelatives(cmds.ls(typ="locator"),parent=True,typ="transform",fullPath=True))', image="locator.png", label="Locators", version="2015", parent=Select_All_By_Type_MenuItem, sourceType="python")

#----------------------------------------------------------------------
def find_UI_By_Name(name):
	""""""
	long=True
	for key in ["controlLayouts","controls","editors","panels","windows","menus","menuItems","radioMenuItemCollections"]:
		kwargs = {key:True,"long":True}
		for ui_item in cmds.lsUI(**kwargs):
			if ui_item.endswith(name):
				return pm.ui.PyUI(ui_item)
	return None

#----------------------------------------------------------------------
def create_AW_Display_Layer_Tab_Menu():
	""""""
	DisplayLayerTab = find_UI_By_Name("DisplayLayerTab")
	if DisplayLayerTab is not None:
		AW_DisplayLayerTab_Menu = pm.menu("AW_DisplayLayerTab_Menu", tearOff=False,label="AW", parent=DisplayLayerTab)
		# Create
		create_sub_menu         = pm.menuItem("AW_DisplayLayerTab_Create_Sub_Menu", tearOff=True, label="Create", subMenu=True, parent=AW_DisplayLayerTab_Menu)
		pm.menuItem("aw_display_layers_from_selected_transform_groups",annotation="Create A Display Layer For Every Selected Transform Group With The Name Matching That Group", command="aw_generate_display_layers_from_selected_transform_groups", label="Selection To Layers",sourceType="mel")
		# Display
		display_sub_menu        = pm.menuItem("AW_DisplayLayerTab_Create_Sub_Menu", tearOff=True, label="Display", subMenu=True, parent=AW_DisplayLayerTab_Menu)
		pm.menuItem("aw_highlight_display_layers_used_in_active_selection",annotation="Highlights The Display Layers That Are Currently Used In the Active Selection", command="aw_highlight_display_layers_used_in_active_selection", label="Highlight From Selection",sourceType="mel")
		
utils.executeDeferred(__name__+".create_AW_Display_Layer_Tab_Menu()")
utils.executeDeferred(__name__+".Add_Custom_Menu_Items()")