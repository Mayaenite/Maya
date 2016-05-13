import os
import string
import yaml
import QT
import QT.DataModels.Qt_Roles_And_Enums
import Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets
import Compiled_UIs.Vray_Scene_State_Manager
try:
	_maya_check = True
	import Scripts.UIFns.Find_UI
	import Scripts.Global_Constants.Nodes
	import Scripts.NodeCls.M_Nodes
	import maya.cmds as cmds
except ImportError as  e:
	print e
	_maya_check = False
	
Custom_Widgets = Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets
Vray_Scene_State_Manager_Item_Model  =  Custom_Widgets.Vray_Scene_State_Manager_Item_Model
Qt_Roles_And_Enums   =  QT.DataModels.Qt_Roles_And_Enums
File_Dialog_Options  =  QT.DataModels.Qt_Roles_And_Enums.File_Dialog_Options
Qt        = QT.Qt
QtCore    = QT.QtCore
QtGui     = QT.QtGui
QtSlot    = QT.QtSlot
QtSignal  = QT.QtSignal
uic       = QT.uic




ui_file = os.path.realpath(os.path.dirname(__file__)+"\Vray_Scene_State_Manager.ui")
uiform, uibase = uic.loadUiType(ui_file)

isinstance(uiform, Compiled_UIs.Vray_Scene_State_Manager.Ui_Vray_Scene_State_Manager)

class Render_State_Layer(object):
	
	def __init__(self, render_state):
		self.render_state = render_state
		isinstance(self.render_state, Custom_Widgets.Render_State_Item)
		self.Beauty_state    = self.render_state.Beauty
		self.Matte_state     = self.render_state.Matte
		self.Invisible_state = self.render_state.Invisible
		self.Build_Shaders()
		self.Build_Layer()
		
	def Build_Shaders(self):
		self.Beauty_Pass    = Scripts.NodeCls.M_Nodes.ShadingNode("Beauty_Pass")
		self.Matte_Pass     = Scripts.NodeCls.M_Nodes.ShadingNode("Matte_Pass")
		self.Invisible_Pass = Scripts.NodeCls.M_Nodes.ShadingNode("Invisible_Pass")
		
		self.Beauty_Pass.plug_access.outColor.setValue([1,1,1])
		self.Matte_Pass.plug_access.outColor.setValue([0,0,0])
		self.Invisible_Pass.plug_access.outColor.setValue([1.0, 0.0, 1.0])
		
		self.Beauty_Pass_SG    = Scripts.NodeCls.M_Nodes.Shading_Engine("Beauty_Pass_SG")
		self.Matte_Pass_SG     = Scripts.NodeCls.M_Nodes.Shading_Engine("Matte_Pass_SG")
		self.Invisible_Pass_SG = Scripts.NodeCls.M_Nodes.Shading_Engine("Invisible_Pass_SG")
		
		self.Beauty_Pass_SG.Assine_To_Material(self.Beauty_Pass)
		self.Matte_Pass_SG.Assine_To_Material(self.Matte_Pass)
		self.Invisible_Pass_SG.Assine_To_Material(self.Invisible_Pass)
		

	def Build_Layer(self):
		self.Render_Layer = Scripts.NodeCls.M_Nodes.RenderLayer(self.render_state.data())
		if len(self.Render_Layer.members):
			self.Render_Layer.removeMembers(self.Render_Layer.members)
		nodes = []
		for item in self.render_state.get_all_but_unassied_parts():
			isinstance(item, Custom_Widgets.Part_Set_Reference_Item)
			nodes.append(item._data.node)
		self.Render_Layer.addMembers(nodes)
		self.Render_Layer.makeCurrent()
		cmds.refresh(f=True)
		for item in self.Beauty_state.Children:
			self.Beauty_Pass_SG.addElement(item._data.node.members)
			cmds.refresh(f=True)
		for item in self.Matte_state.Children:
			self.Matte_Pass_SG.addElement(item._data.node.members)
			cmds.refresh(f=True)
		for item in self.Invisible_state.Children:
			self.Invisible_Pass_SG.addElement(item._data.node.members)
			cmds.refresh(f=True)
			
########################################################################
# uiform, QtGui.QMainWindow
#class Vray_Scene_States_Manager_MainWindow(uiform, QtGui.QMainWindow):
class Vray_Scene_States_Manager_MainWindow(Compiled_UIs.Vray_Scene_State_Manager.Ui_Vray_Scene_State_Manager,QtGui.QMainWindow):
	ACTIVATE_RUN_SETUP     = QT.QtSignal(QtGui.QMainWindow)
	PART_SET_DELEATED      = QT.QtSignal((int,),(str,))
	PART_SET_CREATED       = QT.QtSignal((Custom_Widgets.Part_Set_Item,), (QtGui.QStandardItem,),(QtCore.QModelIndex,))
	RENDER_STATE_DELEATED  = QT.QtSignal((int,),(str,))
	RENDER_STATE_CREATED   = QT.QtSignal((Custom_Widgets.Render_State_Item,), (QtGui.QStandardItem,),(QtCore.QModelIndex,))
	ASSET_DELEATED         = QT.QtSignal((int,),(str,))
	ASSET_CREATED          = QT.QtSignal((Custom_Widgets.Asset_Item,), (QtGui.QStandardItem,),(QtCore.QModelIndex,))
	_Enable_Model_Editor   = False
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		if parent == None and _maya_check:
			parent = Scripts.UIFns.Find_UI.getMayaWindow()
		isinstance(self, Compiled_UIs.Vray_Scene_State_Manager.Ui_Vray_Scene_State_Manager)
		super(Vray_Scene_States_Manager_MainWindow,self).__init__(parent)
		self.setupUi(self)
		self.ACTIVATE_RUN_SETUP.emit(self)
		self.verticalGroupBox.hide()
		self.entity_tree_view.hide()
		self.undo_stack =  QtGui.QUndoStack()
		
		if self._Enable_Model_Editor:
			self.part_sets_view.ITEM_MEMBERES_SELECTED.connect(self.add_Objects_To_Model_Editor)
			self.part_sets_view.ITEM_MEMBERES_DESELECTED.connect(self.remove_Objects_From_Model_Editor)
			
			self.beauty_overide_view.ITEM_MEMBERES_SELECTED.connect(self.add_Objects_To_Model_Editor)
			self.beauty_overide_view.ITEM_MEMBERES_DESELECTED.connect(self.remove_Objects_From_Model_Editor)
			
			self.matte_overide_view.ITEM_MEMBERES_SELECTED.connect(self.add_Objects_To_Model_Editor)
			self.matte_overide_view.ITEM_MEMBERES_DESELECTED.connect(self.remove_Objects_From_Model_Editor)
			
			self.invisible_overide_view.ITEM_MEMBERES_SELECTED.connect(self.add_Objects_To_Model_Editor)
			self.invisible_overide_view.ITEM_MEMBERES_DESELECTED.connect(self.remove_Objects_From_Model_Editor)
		
		self.model =  Vray_Scene_State_Manager_Item_Model(self)
		
		self.asset_item_filter_proxy_model = Custom_Widgets.Asset_Item_Filter_ProxyModel(self)
		self.asset_item_filter_proxy_model.setSourceModel(self.model)
		
		
		self.sorted_proxy_model = Custom_Widgets.Sorted_Item_Filter_ProxyModel(self)
		self.sorted_proxy_model.setSourceModel(self.model)
		self.run_Item_View_Assinments()
		self.render_layer_helper_button.clicked.connect(self.Construct_Render_Layer_From_Render_State)
		self.isolateSelect_Button.toggled.connect(self.isolate_Select_Render_State)
		self.render_states_view.clicked.connect(self.update_isolate_Select_Render_State)
		if _maya_check:
			self.Script_Data = Custom_Widgets.Yaml_Config_Data.find_yaml_config_scripts()
			cmds.scriptJob(killWithScene=True, event=['SceneSaved',self.Save])
			
	#----------------------------------------------------------------------
	@QT.QtSlot(list)
	def remove_Objects_From_Model_Editor(self, objs):
		self.Model_Editor.remove_Objects_From_Main_Connection(objs)
	#----------------------------------------------------------------------
	@QT.QtSlot(list)
	def add_Objects_To_Model_Editor(self, objs):
		self.Model_Editor.add_Objects_To_Main_Connection(objs)
		
	#----------------------------------------------------------------------
	def run_Item_View_Assinments(self):
		self.sorted_proxy_model = Custom_Widgets.Sorted_Item_Filter_ProxyModel(self)
		self.sorted_proxy_model.setSourceModel(self.model)
		self.model.run_Vray_States_Setup()
		self.entity_tree_view.setModel(self.model)
		self.asset_tree_view.setModel(self.asset_item_filter_proxy_model)
		self.render_states_view.setModel(self.sorted_proxy_model)
		self.part_sets_view.setModel(self.sorted_proxy_model)
		self.invisible_overide_view.setModel(self.sorted_proxy_model)
		self.beauty_overide_view.setModel(self.sorted_proxy_model)
		self.matte_overide_view.setModel(self.sorted_proxy_model)
		self.asset_tree_view.set_Root_Item(self.model.Assets)
	###----------------------------------------------------------------------
	##def contextMenuEvent(self, event):
		##menu = QtGui.QMenu(self)
		##menu.addAction(self.actionAdd_Part_Set)
		##menu.addAction(self.actionAdd_Render_State)
		##menu.exec_(event.globalPos())
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def undo_it(self):
		self.undo_stack.undo()

	#----------------------------------------------------------------------
	@QT.QtSlot()
	def redo_it(self):
		self.undo_stack.redo()

	#----------------------------------------------------------------------
	@QT.QtSlot()
	def reset_Item_View(self):
		asset        = self.model.Assets.child(0)
		render_state = asset.Render_States.child(0)
		self.asset_tree_view.set_Root_Item(self.model.Assets)
		self.asset_tree_view.set_Current_Item(asset)
		
	#----------------------------------------------------------------------
	@QT.QtSlot()
	@QT.QtSlot(str)
	def add_Part_Set(self, name=None):
		self.asset_tree_view.add_New_Part_Set(name=name)
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Remove_Selected_Part_Sets(self):
		self.asset_tree_view.delete_Selected_Part_Sets()
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Remove_Selected_Render_States(self):
		self.asset_tree_view.delete_Selected_Render_States()

	#----------------------------------------------------------------------
	@QT.QtSlot()
	@QT.QtSlot(str)
	def add_Asset(self, name=None,subAsset=False):
		self.asset_tree_view.add_New_Asset(name=name, subAsset=subAsset)
		item = self.model.Assets.Children[-1]
		self.asset_tree_view.set_Current_Item(item)
		isinstance(item, Custom_Widgets.Asset_Item)
		return item
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Remove_Selected_Assets(self):
		self.asset_tree_view.delete_Selected_Assets()


	#----------------------------------------------------------------------
	@QT.QtSlot()
	@QT.QtSlot(str)
	def add_Child_Asset(self, name=None):
		self.asset_tree_view.add_New_Asset(name=name, subAsset=True)
	#----------------------------------------------------------------------
	@QT.QtSlot()
	@QT.QtSlot(str)
	def add_Render_State(self, name=None):
		self.asset_tree_view.add_New_Render_State(name=name)
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def open_File(self):
		""""""
		if _maya_check:
			self.Load_Temp_yaml()
			#self.model.from_Yaml()
			#self.Update_On_Render_State_Selection_Changed(self.model.Render_States.child(0).index())
			#self.undo_stack.clear()
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def save_File_As(self):
		""""""
		if _maya_check:
			value = self.model.to_Yaml()
	#----------------------------------------------------------------------
	def show(self):
		super(Vray_Scene_States_Manager_MainWindow, self).show()
		if self._Enable_Model_Editor:
			self.Model_Editor.m_editor.widget.show()
	
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Save(self):
		self.model.scan_for_Master_Render_States()
		for asset in self.model.Assets.find_child_item_types(Custom_Widgets.Asset_Item.ITEM_TYPE):
			isinstance(asset, Custom_Widgets.Asset_Item)
			asset.Update_Enum_Render_States()
		data = self.model.to_Yaml_Object()
		self.Script_Data.save_Config_Data(data)
		
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Load(self):
		if _maya_check:
			data = self.Script_Data.load_Config_Data()
			if data != None:
				self.model.from_Yaml_Object(data)
				self.reset_Item_View()
				self.undo_stack.clear()
				self.sorted_proxy_model.sort()
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Construct_From_Display_Layers(self):
		if _maya_check:
			
			layers = Scripts.Global_Constants.Nodes.Display_Layers()
			if self.model.Assets.RowCount:
				asset = self.asset_tree_view.current_item()
			else:
				asset = self.add_Asset(name="Display_Layers_Asset", subAsset=False)
			
			for layer in layers:
				isinstance(layer, Scripts.NodeCls.M_Nodes.DisplayLayer)
				name = layer.name + "_set"
				if not asset.child_item_exists(name):
					self.asset_tree_view.add_New_Part_Set(name=name)
					part = self.model.Assets.find_Part_Sets_By_Name(name)[0]
					part._data.unlockNode()
					asset.node_addNode([part.node])
					part.node_include_items(layer.members)
					part._data.lockNode()
	@QT.QtSlot()
	def sync_Display_Layers(self):
		for dl in Scripts.Global_Constants.Nodes.Display_Layers():
			isinstance(dl, Scripts.NodeCls.M_Nodes.DisplayLayer)
			ps_link = dl.Add_Simple_Attribute("partSetLink", 'message', shortName="pslnk", hidden=False, writable=True, readable=True, storable=True, keyable=False)
			if cmds.objExists(dl.nice_name+"_set"):
				vrop = Scripts.NodeCls.M_Nodes.VRayObjectProperties(dl.nice_name+"_set")
				vrop.unlockNode()
				dl_link = vrop.Add_Simple_Attribute("displayLayerLink", 'message', shortName="dllnk", hidden=False, writable=True, readable=True, storable=True, keyable=False)
				ps_link.Simple_Connect(dl_link)
				if len(dl.members):
					vrop.addElement(dl.members)
				vrop.lockNode()
	#----------------------------------------------------------------------
	def Construct_Render_Layer_From_Render_State(self):
		item = self.render_states_view.current_item()
		Render_State_Layer(item)
		
	@QT.QtSlot()
	#----------------------------------------------------------------------
	def Apply_Current_State_To_Diaplay_Layers(self):
		item = self.render_states_view.current_item()
		isinstance(item, Custom_Widgets.Render_State_Item)
		for part in item.Beauty_Parts:
			cmds.setAttr(part._data.node.assinedDisplayLayer+".visibility",1)
		for part in item.Invisible_Parts:
			cmds.setAttr(part._data.node.assinedDisplayLayer+".visibility",1)
		for part in item.Matte_Parts:
			cmds.setAttr(part._data.node.assinedDisplayLayer+".visibility",1)
		for part in item.Unassined_Parts:
			cmds.setAttr(part._data.node.assinedDisplayLayer+".visibility",0)
	@QT.QtSlot()
	#----------------------------------------------------------------------
	def Show_All_Diaplay_Layers(self):
		for layer in Scripts.Global_Constants.Nodes.Display_Layers():
			isinstance(layer, Scripts.NodeCls.M_Nodes.DisplayLayer)
			layer.visibility.value = 1
	#----------------------------------------------------------------------	
	@QT.QtSlot(bool)
	def isolate_Select_Render_State(self, state):
		model_pan = cmds.getPanel(withLabel="Persp View")
		try:
			if state:
				current_selection = cmds.ls(sl=True)
				render_state = self.render_states_view.current_item()
				if render_state is None:
					cmds.headsUpMessage("Can not isolateing Please Select A Render State")
				else:
					members = render_state.get_all_but_unassied_node_members()
					cmds.isolateSelect( model_pan, state=False )
					cmds.select(clear=True)
					if len(members):
						cmds.select(members)
						cmds.isolateSelect( model_pan, state=state )
						cmds.isolateSelect( model_pan, addSelected=True )
					else:
						cmds.isolateSelect( model_pan, state=True )
						
					if len(current_selection):
						cmds.select(current_selection)
					else:
						cmds.select(clear=True)
			else:
				cmds.isolateSelect( model_pan, state=state )
		except:
			cmds.headsUpMessage("had a problem isolateing Could Not Panel withLabel Persp View")
		
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def update_isolate_Select_Render_State(self):
		if self.isolateSelect_Button.isChecked():
			self.isolate_Select_Render_State(True)

States_Manager = None
isinstance(States_Manager, Compiled_UIs.Vray_Scene_State_Manager.Ui_Vray_Scene_State_Manager)
_remove_manager_job_id = -1
def make_ui():
	global States_Manager, _remove_manager_job_id
	if States_Manager == None:
		States_Manager = Vray_Scene_States_Manager_MainWindow()
		States_Manager.show()
		States_Manager.Load()
		_remove_manager_job_id = cmds.scriptJob(runOnce=True, event= ["deleteAll",remove_manager])
	else:
		States_Manager.show()
	return States_Manager

def remove_manager():
	global States_Manager
	States_Manager.hide()
	check = States_Manager._Enable_Model_Editor
	States_Manager = None	
	#States_Manager.setParent(None)
	#del States_Manager
	if check:
		cmds.deleteUI("MyModelEditor", editor = True)
