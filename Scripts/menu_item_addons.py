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
	maya.mel.eval('buildViewMenu("MayaWindow|mainWindowMenu");')
	
	Modify_Menu      =  "MayaWindow|mainModifyMenu"
	main_Window_Menu =  "MayaWindow|mainWindowMenu"
	
	aw_HOT_PIVOT_ACTION  = cmds.menuItem( annotation="Reset The Selected Trasform Matrix", command='aw_HOT_PIVOT_ACTION;', image="menuIconModify.png", label="HOT PIVOT ACTION", version="2018", parent=Modify_Menu, sourceType="mel")
	SelLocatorItem       = cmds.menuItem( annotation="Select All Locator Transforms", command='cmds.select(cmds.listRelatives(cmds.ls(typ="locator"),parent=True,typ="transform",fullPath=True))', image="locator.png", label="Locators", version="2018", parent=Select_All_By_Type_MenuItem, sourceType="python")
	#open_asset_views_gui = cmds.menuItem( annotation="Asset Views UI", command='try:\n\tDML_Tools.Maya.Maya_Tools.Asset_Views.build_GUI()\nexcept:\n\timport DML_Tools.Maya.Maya_Tools.Asset_Views\n\tDML_Tools.Maya.Maya_Tools.Asset_Views.build_GUI()', label="DML Asset Views", version="2018", parent=main_Window_Menu, sourceType="python")
	
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
		try:
			rlay = pm.rowLayout(numberOfColumns=3, parent=DisplayLayerTab.getChildren()[0])
			pm.button("AW_DisplayLayerTab_force_update_item", command='import pymel.core as pm\npm.mel.eval("updateLayerEditor")',annotation="Force Update",statusBarMessage="Force Update", label="FU", parent=rlay)
			pm.button("AW_highlight_display_layers_used_in_active_selection", command='import pymel.core as pm\npm.mel.eval("aw_highlight_display_layers_used_in_active_selection")',annotation="Highlight From Selection",statusBarMessage="Highlights The Display Layers That Are Currently Used In the Active Selection", label="HFS", parent=rlay)
			pm.button("aw_show_layer_by_expression_name", command='import pymel.core as pm\npm.mel.eval("aw_show_layer_by_expression_name")',annotation="Make Visibility Only\nDisplay Layers With Matching Critera",statusBarMessage="Make Visibility Only Display Layers With Matching Critera", label="SML", parent=rlay)
			
		except:
			pass
		AW_DisplayLayerTab_Menu = pm.menu("AW_DisplayLayerTab_Menu", tearOff=False,label="AW", parent=DisplayLayerTab)
		# Create
		create_sub_menu         = pm.menuItem("AW_DisplayLayerTab_Create_Sub_Menu", tearOff=True, label="Create", subMenu=True, parent=AW_DisplayLayerTab_Menu)
		pm.menuItem("aw_display_layers_from_selected_transform_groups",annotation="Create A Display Layer For Every Selected Transform Group With The Name Matching That Group", command="aw_generate_display_layers_from_selected_transform_groups", label="Selection To Layers",sourceType="mel")
		# Display
		#display_sub_menu        = pm.menuItem("AW_DisplayLayerTab_Create_Sub_Menu", tearOff=True, label="Display", subMenu=True, parent=AW_DisplayLayerTab_Menu)
		#pm.menuItem("aw_highlight_display_layers_used_in_active_selection",annotation="Highlights The Display Layers That Are Currently Used In the Active Selection", command="aw_highlight_display_layers_used_in_active_selection", label="Highlight From Selection",sourceType="mel")
		
utils.executeDeferred(__name__+".create_AW_Display_Layer_Tab_Menu()")
utils.executeDeferred(__name__+".Add_Custom_Menu_Items()")