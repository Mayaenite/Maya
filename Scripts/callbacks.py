import sys, os
import maya.cmds as cmds
import OpenMaya_Util_API
import Maya_Callback_Builders

_G_Active_Render_Layer_Before_Save =  ""
#----------------------------------------------------------------------
def Set_To_Master_Layer_BeFore_Scene_Save(clientData):
	global _G_Active_Render_Layer_Before_Save
	if not cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True) == "defaultRenderLayer":
		_G_Active_Render_Layer_Before_Save =  cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True)
		cmds.editRenderLayerGlobals( currentRenderLayer='defaultRenderLayer' )
#----------------------------------------------------------------------
def Reactive_Render_Layer_After_Scene_Save(clientData):
	global _G_Active_Render_Layer_Before_Save
	if not _G_Active_Render_Layer_Before_Save == "":
		cmds.editRenderLayerGlobals( currentRenderLayer=_G_Active_Render_Layer_Before_Save)
		_G_Active_Render_Layer_Before_Save = ""
#----------------------------------------------------------------------
def Add_Part_Set_Message_On_Vray_ObjectProperty_Creation(nodeObj, clientData):
	fn = OpenMaya_Util_API.oldOM.MFnDependencyNode(nodeObj)
	if fn.typeName() == "VRayObjectProperties":
		if not fn.hasAttribute("partSetMessage"):
			OpenMaya_Util_API.Attribute_Tools.Add_Message(fn.name(), attr="partSetMessage")

def Add_Custom_Menu_Items_Vray_Plugin_Load(plugin):
	if plugin == "vrayformaya":
		if cmds.menu("vrayMenuCreateItem",query=True,exists=True):
			# cmds.menuItem( divider=True,parent="vrayMenuCreateItem")
			cmds.menuItem("AWvrayAttributesMakeMenu",label="AW Add Vray Attribute",parent="vrayMenuCreateItem",subMenu=True, version="2015")
			cmds.menuItem("vrayMenuCreatematerialIdAttributesItem",command='[cmds.vray("addAttributesFromGroup",item, "vray_material_id",1) for item in cmds.ls(sl=True,long=True) if cmds.objectType(item).startswith("VRay") and "Mtl" in cmds.objectType(item)]',parent="AWvrayAttributesMakeMenu",label="Add Material IDs", annotation="Add A Vray Material ID Attribute For All The Selected Vray Materials")
			cmds.menuItem("vrayMenuRemovematerialIdAttributesItem",command='[cmds.vray("addAttributesFromGroup",item, "vray_material_id",0) for item in cmds.ls(sl=True,long=True) if cmds.objectType(item).startswith("VRay") and "Mtl" in cmds.objectType(item)]',parent="AWvrayAttributesMakeMenu",label="Remove Material IDs", annotation="Remove Vray Material ID Attribute For All The Selected Vray Materials")
			cmds.menuItem("vrayMenuCreateobjectIdAttributesItem",command='[cmds.vray("addAttributesFromGroup",obj,"vray_objectID",1) for obj in cmds.ls(sl=True,long=True,type="transform")]',parent="AWvrayAttributesMakeMenu",label="Add Object IDs", annotation="Add A Vray Object ID Attribute To All The Selected Transform Nodes")
			cmds.menuItem("vrayMenuCreateRoundedEdgesAttributesItem",command='[cmds.vray("addAttributesFromGroup",mesh,"vray_roundedges",1) for mesh in cmds.ls(sl=True,dagObjects=True,shapes=True,long=True,flatten=True,type="mesh")]',parent="AWvrayAttributesMakeMenu",label="Add Rounded Edges", annotation="Add A Vray Rounded Edges Attribute To All The Selected Mesh Nodes")
			cmds.menuItem("vrayMenuCreateSubdivisionAttributesItem",command='[cmds.vray("addAttributesFromGroup",mesh,"vray_subdivision",1) for mesh in cmds.ls(sl=True,dagObjects=True,shapes=True,long=True,flatten=True,type="mesh")]',parent="AWvrayAttributesMakeMenu",label="Add Subdivision", annotation="Add A Vray Subdivision Attribute To All The Selected Mesh Nodes")
			cmds.menuItem("vrayMenuRemoveSubdivisionAttributesItem",command='[cmds.vray("addAttributesFromGroup",mesh,"vray_subdivision",0) for mesh in cmds.ls(sl=True,dagObjects=True,shapes=True,long=True,flatten=True,type="mesh")]',parent="AWvrayAttributesMakeMenu",label="Remove Subdivision", annotation="Add A Vray Subdivision Attribute To All The Selected Mesh Nodes")
			cmds.menuItem("vrayMenuCreatefileGammaAttributesItem",command='[cmds.vray("addAttributesFromGroup",item,"vray_file_gamma",1) for item in cmds.ls(sl=True,typ="file")]',parent="AWvrayAttributesMakeMenu",label="Add File Gamma", annotation="Add A Vray File Gamma Attribute To All The Selected Texture File Nodes")
			cmds.menuItem("vrayMenuCreateSkipExportAttributesItem",command='[cmds.vray("addAttributesFromGroup",obj,"vray_skip_export",1) for obj in cmds.ls(sl=True,long=True,type="transform")]',parent="AWvrayAttributesMakeMenu",label="Add Skip Export", annotation="Add A Vray Skip Export Attribute To All The Selected Transform Nodes")

########################################################################
class Hypergraph_Node_PopupMenu_CallbackFunction_Data(object):
	def __init__(self,node):
		self.node = node
	def __call__(self,*args):
		cmds.hyperShade(objects=self.node)
		sel = cmds.ls(selection=True,visible=True)
		if len(sel):
			cmds.select(sel)
		else:
			cmds.select(clear=True)

#----------------------------------------------------------------------
def Hypergraph_Node_PopupMenu_CallbackFunction(arg1):
	cmds.menuItem(radialPosition="SE", subMenu=True, label="AW")
	cmds.menuItem(radialPosition="N", label="Select Visible Objects With Material", command = Hypergraph_Node_PopupMenu_CallbackFunction_Data(arg1))
	cmds.menuItem(radialPosition="S", label="Vray Mtl Swapper", command = Maya_UserTools.importAndRun("Vray_Mtl_Swapper"))
	cmds.setParent( '..', menu=True )

#cmds.callbacks(addCallback=Hypergraph_Node_PopupMenu_CallbackFunction, hook='addItemsToHypergraphNodePopupMenu', owner='Drew_Loveridge')
#cmds.callbacks(addCallback=Display_Layer_Changed_Callback_Function, hook='Display_Layer_Changed', owner='Drew_Loveridge')
cmds.loadPlugin( addCallback=Add_Custom_Menu_Items_Vray_Plugin_Load )
callbackId1 = Maya_Callback_Builders.create_Scene_Message_Callback(Maya_Callback_Builders.Scene_Message_Before_Flags.Save, Set_To_Master_Layer_BeFore_Scene_Save, None)
callbackId2 = Maya_Callback_Builders.create_Scene_Message_Callback(Maya_Callback_Builders.Scene_Message_After_Flags.Save, Reactive_Render_Layer_After_Scene_Save, None)
