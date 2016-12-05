try:
	_maya_check = True
	import Scripts.Global_Constants.Nodes
	import Scripts.NodeCls.M_Nodes
	import Scripts.UIFns.Find_UI
	import maya.cmds as cmds
	if not len(cmds.fileInfo( 'AW_Vray_States_Viewer_Version', query=True )):
		# version = cmds.confirmDialog( title='Viewer Version', message='The Viewer Version For This File Has Not Been Set\nPlease Select The Version You Would Like To Use\n\nWarning!! Version 2 is Still In Beta', button=['Version 1','Version 2'], defaultButton='Version 1', cancelButton='Version 1', dismissString='Version 1' )[-1]
		cmds.fileInfo( 'AW_Vray_States_Viewer_Version', "1" )
except:
	_maya_check = False
import os
import string
import yaml
import QT
import QT.DataModels.Qt_Roles_And_Enums
import Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets
import Compiled_UIs.Vray_Scene_State_Viewer
import Scripts.General_Maya_Util
Custom_Widgets = Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets
Vray_Scene_State_Viewer_Item_Model  =  Custom_Widgets.Vray_Scene_State_Viewer_Item_Model
Qt_Roles_And_Enums   =  QT.DataModels.Qt_Roles_And_Enums
File_Dialog_Options  =  QT.DataModels.Qt_Roles_And_Enums.File_Dialog_Options
Qt     = QT.Qt
QtCore = QT.QtCore
QtGui  = QT.QtGui
uic    = QT.uic


ui_file = os.path.realpath(os.path.dirname(__file__)+"\Vray_Scene_State_Viewer.ui")
uiform, uibase = uic.loadUiType(ui_file)

class Enum_List_Delegate(QtGui.QItemDelegate):
	def get_item_from_index(self, index):
		isinstance(index, QtCore.QModelIndex)
		m = index.model()
		if isinstance(m, QtGui.QSortFilterProxyModel):
			pm = m
			m  = m.sourceModel()
			index = pm.mapToSource(index)
		item = m.itemFromIndex(index)
		return item
	def createEditor(self, parent, option, index):
		isinstance(index, QtCore.QModelIndex)
		item = self.get_item_from_index(index)
		if isinstance(item, Custom_Widgets.Enum_Plug_Item):
			if len(item.node_listEnumNames):
				editor = QtGui.QComboBox(parent)
				editor.addItems(item.node_listEnumNames)
				return editor
		editor = super(Enum_List_Delegate, self).createEditor(parent, option, index)
		return editor

	def setEditorData(self, editor, index):
		if isinstance(editor, QtGui.QComboBox):
			item = self.get_item_from_index(index)
			editor.setCurrentIndex(item._data.value)
		else:
			super(Enum_List_Delegate, self).setEditorData(editor, index)

	def setModelData(self, editor, model, index):
		if isinstance(editor, QtGui.QComboBox):
			item = self.get_item_from_index(index)
			item.setData(editor.currentText())
		else:
			super(Enum_List_Delegate, self).setModelData(editor, model, index)

	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)

########################################################################
# uiform, QtGui.QMainWindow
class Vray_Scene_States_Viewer_MainWindow(uiform, QtGui.QMainWindow):
#class Vray_Scene_States_Viewer_MainWindow(Compiled_UIs.Vray_Scene_State_Viewer.Ui_Vray_Scene_States_Viewer,QtGui.QMainWindow):
	#----------------------------------------------------------------------
	ACTIVE_RENDER_LAYER_CHANGED = QT.QtSignal()
	NEW_RENDER_LAYER_CREATED = QT.QtSignal()
	def __init__(self, parent=None):
		if parent == None and _maya_check:
			parent = Scripts.UIFns.Find_UI.getMayaWindow()
		isinstance(self, Compiled_UIs.Vray_Scene_State_Viewer.Ui_Vray_Scene_States_Viewer)
		super(Vray_Scene_States_Viewer_MainWindow,self).__init__(parent)
		self.setupUi(self)
		#self.Asset_Grid_groupBox.hide()
		self.entity_tree_view.hide()
		if self.Version_Check() == 2:
			self.Update_Button.hide()
		self.model                = Vray_Scene_State_Viewer_Item_Model(self)
		self.asset_filtered_model = Custom_Widgets.Master_Asset_Item_Filter_ProxyModel(parent=self)
		self.asset_filtered_model.setSourceModel(self.model)
		self.Update_Button.clicked.connect(self.Run_Update)
		self.rebuild_Render_layer_states_button.clicked.connect(self.Rebuild_Render_Layer_States)
		# cmds.scriptJob(e=["renderLayerChange", self.update_on_render_layer_Added], killWithScene=True)
		self._Render_Layer_Changed_Script_Job_ID = cmds.scriptJob(e=["renderLayerManagerChange", self.emit_render_layer_changed], killWithScene=True)
		
	def Version_Check(self):
		return Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets.Viewer_Version_check()
	#----------------------------------------------------------------------
	def run_Item_View_Assinments(self):
		self.entity_tree_view.setModel(self.asset_filtered_model)
		delegate = Enum_List_Delegate()
		self.entity_tree_view.setItemDelegate(delegate)
		self.Asset_Grid_widget.build_Master_Assets_Grid(self.model.File_References)
	#----------------------------------------------------------------------
	def show(self):
		super(Vray_Scene_States_Viewer_MainWindow, self).show()
		self.run_Item_View_Assinments()
		
	def emit_render_layer_changed(self):
		self.ACTIVE_RENDER_LAYER_CHANGED.emit()
		if self.Version_Check() == 2:
			try:
				active_layer = Scripts.NodeCls.M_Nodes.RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
				if cmds.objExists("Vray_Scene_States_Global_Render_Group"):
					master_node = Scripts.NodeCls.M_Nodes.MNODE("Vray_Scene_States_Global_Render_Group")
					active_layer.addMembers([master_node])
				else:
					master_node = None
			except:
				master_node = None
	
	def update_on_render_layer_Added(self):
		for file_ref in self.model.File_References.Children:
			for asset in file_ref.Children:
				isinstance(asset, Custom_Widgets.Asset_Item)
				for layer in [layer for layer in Scripts.Global_Constants.Nodes.Render_Layers() if not ":" in layer.name]:
					asset.enum_render_states_plug.enable_Render_Layer_Overide(layer=layer)
	
	def Rebuild_Render_Layer_States(self):
		active_layer = Scripts.NodeCls.M_Nodes.RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
		layers = [layer for layer in Scripts.Global_Constants.Nodes.Render_Layers() if not ":" in layer.name]
		if self.Version_Check() == 1:
			for layer in  layers:
				layer.makeCurrent()
				self.emit_render_layer_changed()
				# cmds.refresh(force=True)
				for file_ref in self.model.File_References.Children:
					for asset in file_ref.Children:
						isinstance(asset, Custom_Widgets.Asset_Item)
						asset.clear_Children_From_Render_Layer()
						# cmds.refresh(force=True)
		for layer in layers:
			isinstance(layer, Scripts.NodeCls.M_Nodes.RenderLayer)
			layer.makeCurrent()
			self.emit_render_layer_changed()
			# cmds.refresh(force=True)
			for item in self.Asset_Grid_widget.items:
				isinstance(item, Custom_Widgets.Asset_Frame)
				current = item.asset_states.currentIndex()
				item.asset_states.setCurrentIndex(0)
				item.asset_states.update_asset_attribute()
				# cmds.refresh(force=True)
				item.asset_states.setCurrentIndex(current)
				item.asset_states.update_asset_attribute()
				# cmds.refresh(force=True)
		active_layer.makeCurrent()
	#----------------------------------------------------------------------
	def showEvent(self, event):
		super(Vray_Scene_States_Viewer_MainWindow, self).showEvent(event)
	#----------------------------------------------------------------------
	def hideEvent(self, event):
		super(Vray_Scene_States_Viewer_MainWindow, self).hideEvent(event)

	#----------------------------------------------------------------------
	def Run_Update(self):
		""""""
		check = cmds.confirmDialog( title='Viewer Version', message='If You Update To Version 2.\nAll Your Render Layers Will Be Cleared\nAnd Group Node Called\nVray_Scene_States_Global_Render_Group Will Be Added\nParent All Top Level Reference Node Under It\nAnd The Display Layers Will Take Care Of The Rest\n\n WARNING!!! BEFORE YOU UPDATE!!!\nANY FILES THAT ARE REFS.\nTHAT THE SCENE STATE MANAGER WAS USED ON\nNEED TO HAVE HAD THE Sync Display Layers RUN FOR THE NEW VERSION TO WORK\n\nDo you Want To Continue', button=['yes','no'], defaultButton='no', cancelButton='no', dismissString='no' )
		if check == "yes":
			cmds.fileInfo( 'AW_Vray_States_Viewer_Version', "2" )
			self.model.run_update(full=True)
			self.Rebuild_Render_Layer_States()
			self.Update_Button.hide()
States_Viewer = None
isinstance(States_Viewer, Compiled_UIs.Vray_Scene_State_Viewer.Ui_Vray_Scene_States_Viewer)

def make_ui():
	global States_Viewer
	if States_Viewer == None:
		States_Viewer = Vray_Scene_States_Viewer_MainWindow()
		States_Viewer.show()
		cmds.scriptJob(runOnce=True, event= ["deleteAll",remove_Viewer])
	elif Scripts.General_Maya_Util.getModifier() == 'Ctrl+Alt+Shift':
		cmds.scriptJob(kill=States_Viewer._Render_Layer_Changed_Script_Job_ID)
		remove_Viewer()
		States_Viewer = Vray_Scene_States_Viewer_MainWindow()
		States_Viewer.show()
	else:
		States_Viewer.show()
	return States_Viewer

def remove_Viewer():
	global States_Viewer
	States_Viewer.hide()
	States_Viewer.setParent(None)
	States_Viewer = None
	
