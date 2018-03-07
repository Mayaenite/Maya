import pymel.core as pm
import maya.cmds as cmds
import maya.utils as utils
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
		create_sub_menu         = pm.menuItem("AW_DisplayLayerTab_Create_Sub_Menu", tearOff=True, label="Create", subMenu=True, parent=AW_DisplayLayerTab_Menu)
		pm.menuItem("aw_display_layers_from_selected_transform_groups",annotation="Create A Display Layer For Every Selected Transform Group With The Name Matching That Group", command="aw_generate_display_layers_from_selected_transform_groups", label="Selection To Layers",sourceType="mel")
		
utils.executeDeferred (__name__+".create_AW_Display_Layer_Tab_Menu()")