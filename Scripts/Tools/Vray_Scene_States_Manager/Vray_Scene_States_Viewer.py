try:
	_maya_check = True
	import Scripts.Global_Constants.Nodes
	import Scripts.NodeCls.M_Nodes
	import Scripts.UIFns.Find_UI
	import maya.cmds as cmds
	from maya.app.general.mayaMixin import MayaQWidgetBaseMixin,MayaQWidgetDockableMixin
	try:
		cmds.loadPlugin("vrayformaya",qt=True)
	except:
		pass
	if not len(cmds.fileInfo( 'AW_Vray_States_Viewer_Version', query=True )):
		# version = cmds.confirmDialog( title='Viewer Version', message='The Viewer Version For This File Has Not Been Set\nPlease Select The Version You Would Like To Use\n\nWarning!! Version 2 is Still In Beta', button=['Version 1','Version 2'], defaultButton='Version 1', cancelButton='Version 1', dismissString='Version 1' )[-1]
		cmds.fileInfo( 'AW_Vray_States_Viewer_Version', "3" )
except:
	_maya_check = False
import os
import string
import yaml
import QT
import QT.DataModels.Qt_Roles_And_Enums
import Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets

if int(cmds.about(version=True)) >= 2017:
	import Compiled_UIs.Vray_Scene_State_Viewer
	Compiled_Vray_Scene_State_Viewer = Compiled_UIs.Vray_Scene_State_Viewer
else:
	import Compiled_UIs.pyside_V1.Vray_Scene_State_Viewer
	Compiled_Vray_Scene_State_Viewer = Compiled_UIs.pyside_V1.Vray_Scene_State_Viewer

import Scripts.General_Maya_Util
Custom_Widgets = Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets
Vray_Scene_State_Viewer_Item_Model  =  Custom_Widgets.Vray_Scene_State_Viewer_Item_Model
Qt_Roles_And_Enums   =  QT.DataModels.Qt_Roles_And_Enums
File_Dialog_Options  =  QT.DataModels.Qt_Roles_And_Enums.File_Dialog_Options
Qt     = QT.Qt
QtCore = QT.QtCore
QtGui  = QT.QtGui
uic    = QT.uic

QT.ui_Loader.registerCustomWidget(Custom_Widgets.Asset_Tree_View)
QT.ui_Loader.registerCustomWidget(Custom_Widgets.Asset_Grid)

ui_file = os.path.realpath(os.path.dirname(__file__)+"\Vray_Scene_State_Viewer.ui")
update_warning_file = os.path.realpath(os.path.dirname(__file__)+"\UI\Warning_Message.ui")
#uiform, uibase = uic.loadUiType(ui_file)

#class Enum_List_Delegate(QT.QItemDelegate):
	#def get_item_from_index(self, index):
		#isinstance(index, QtCore.QModelIndex)
		#m = index.model()
		#if isinstance(m, QT.QSortFilterProxyModel):
			#pm = m
			#m  = m.sourceModel()
			#index = pm.mapToSource(index)
		#item = m.itemFromIndex(index)
		#return item
	#def createEditor(self, parent, option, index):
		#isinstance(index, QtCore.QModelIndex)
		#item = self.get_item_from_index(index)
		#if isinstance(item, Custom_Widgets.Enum_Plug_Item):
			#if len(item.node_listEnumNames):
				#editor = QT.QComboBox(parent)
				#editor.addItems(item.node_listEnumNames)
				#return editor
		#editor = super(Enum_List_Delegate, self).createEditor(parent, option, index)
		#return editor

	#def setEditorData(self, editor, index):
		#if isinstance(editor, QT.QComboBox):
			#item = self.get_item_from_index(index)
			#editor.setCurrentIndex(item._data.value)
		#else:
			#super(Enum_List_Delegate, self).setEditorData(editor, index)

	#def setModelData(self, editor, model, index):
		#if isinstance(editor, QT.QComboBox):
			#item = self.get_item_from_index(index)
			#item.setData(editor.currentText())
		#else:
			#super(Enum_List_Delegate, self).setModelData(editor, model, index)

	#def updateEditorGeometry(self, editor, option, index):
		#editor.setGeometry(option.rect)

########################################################################
# uiform, QT.QMainWindow
class Vray_Scene_States_Viewer_MainWindow(MayaQWidgetDockableMixin, QT.QMainWindow):
#class Vray_Scene_States_Viewer_MainWindow(Compiled_UIs.Vray_Scene_State_Viewer.Ui_Vray_Scene_States_Viewer,QT.QMainWindow):
	#----------------------------------------------------------------------
	ACTIVE_RENDER_LAYER_CHANGED = QT.QtSignal()
	NEW_RENDER_LAYER_CREATED = QT.QtSignal()
	def __init__(self, parent=None):
		isinstance(self, Compiled_Vray_Scene_State_Viewer.Ui_Vray_Scene_States_Viewer)
		super(Vray_Scene_States_Viewer_MainWindow,self).__init__(parent)
		self._use_Beta = False
		if False:
			isinstance(self.model,Vray_Scene_State_Viewer_Item_Model)
			isinstance(self.multi_state_assignment_button,QT.QPushButton)
	def _init(self):
		#self.Asset_Grid_groupBox.hide()
		if not len(cmds.fileInfo( 'AW_Vray_States_Viewer_Version', query=True )):
			cmds.fileInfo( 'AW_Vray_States_Viewer_Version', str(Custom_Widgets._Vray_Scene_States_Viewer_Current_Version) )
			#self.rebuild_Render_layer_states_button.hide()

		self.entity_tree_view.hide()
		if self.Version_Check() >= Custom_Widgets._Vray_Scene_States_Viewer_Current_Version:
			self.Update_Button.hide()
		else:
			self.Update_Button.setText("Transfer To New System")
			self.rebuild_Render_layer_states_button.setEnabled(False)
			self.Update_Button.show()
		self.model                = Vray_Scene_State_Viewer_Item_Model(self)
		self.asset_filtered_model = Custom_Widgets.Master_Asset_Item_Filter_ProxyModel(parent=self)
		self.asset_filtered_model.setSourceModel(self.model)
		# Custom_Widgets.Master_Asset_Item_Filter_ProxyModel
		self.Update_Button.clicked.connect(self.Run_Update)
		self.rebuild_Render_layer_states_button.clicked.connect(self.Rebuild_Render_Layer_States)
		self.multi_state_assignment_button.clicked.connect(self.on_multi_state_assignment_button_pushed)
		self._Render_Layer_Added_Script_Job_ID = cmds.scriptJob(e=["renderLayerChange", self.update_on_render_layer_Added], killWithScene=True)
		self._Post_Scene_Read_Script_Job_ID = cmds.scriptJob(e=["PostSceneRead", self.update_on_render_layer_Added], killWithScene=True)
		self._Render_Layer_Changed_Script_Job_ID = cmds.scriptJob(e=["renderLayerManagerChange", self.emit_render_layer_changed], killWithScene=True)
		self.actionSet_State_By_Name.triggered.connect(self.Assine_Overide_State_To_Render_Layer_With_Matching_Name_Combo_Box)
		self.run_Item_View_Assinments()
	#----------------------------------------------------------------------
	def get_Data_Model_Item_Render_Layers(self):
		""""""
		return self.model.Render_Layers
	#----------------------------------------------------------------------
	def get_Data_Model_Item_File_References(self,lookup=None):
		""""""
		if lookup == None:
			return self.model.File_References.Children
		elif isinstance(lookup,int):
			res = self.model.File_References.child(lookup)
		elif isinstance(lookup,basestring):
			res = self.model.File_References.find_child_items(lookup,recurive=False)
			if len(res):
				res = res[0]
			else:
				res = self.model.File_References.find_Child_By_UUID(lookup)
				if len(res):
					res = res[0]
				else:
					res = None
		isinstance(res,Custom_Widgets.File_Reference_Item)
		return res
	#----------------------------------------------------------------------
	def get_Data_Model_Item_Asset(self,file_ref_lookup=None,asset_lookup=None):
		""""""
		if file_ref_lookup == None:
			file_refs = self.get_Data_Model_Item_File_References()
			res = []
			for ref in file_refs:
				res.extend(ref.Children)
			return res
		else:
			if not isinstance(file_ref_lookup,Custom_Widgets.File_Reference_Item):
				file_ref_lookup = self.get_Data_Model_Item_File_References(lookup=file_ref_lookup)
				if not isinstance(file_ref_lookup,Custom_Widgets.File_Reference_Item):
					return None
			
			if asset_lookup == None:
				return file_ref_lookup.Children
			elif isinstance(asset_lookup,int):
				return file_ref_lookup.child(asset_lookup)	
	def Version_Check(self):
		return Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets.Viewer_Version_check()
	#----------------------------------------------------------------------
	def run_Item_View_Assinments(self):
		self.entity_tree_view.setModel(self.asset_filtered_model)
		# delegate = Enum_List_Delegate()
		# self.entity_tree_view.setItemDelegate(delegate)
		self.Asset_Grid_widget.build_Master_Assets_Grid(self.model.File_References)
	#----------------------------------------------------------------------
	def show(self):
		super(Vray_Scene_States_Viewer_MainWindow, self).show()
	#----------------------------------------------------------------------
	def get_asset_states_comboxs(self):
		res = []
		for item in self.Asset_Grid_widget.items:
			res.append(item.asset_states)
		return res
	#----------------------------------------------------------------------
	@QT.QtSlot()
	def Assine_Overide_State_To_Render_Layer_With_Matching_Name_Combo_Box(self):
		def run_List_View():
			state_comboxs = self.get_asset_states_comboxs()

			for rl in cmds.ls(typ="renderLayer"):
				if not "defaultRenderLayer" in rl:
					cmds.editRenderLayerGlobals( currentRenderLayer=rl)

					for cb in state_comboxs:
						index=cb.rootIndex()
						m    = index.model()
						item = m.itemFromIndex(index)

						for child in item.Children[2:]:
							if rl.startswith(child.data()):
								cb.setCurrentIndex(child.index())
								cb.update_asset_attribute()
								break
		def run_Combo_Box():
			state_comboxs = self.get_asset_states_comboxs()

			for rl in cmds.ls(typ="renderLayer"):
				if not "defaultRenderLayer" in rl:
					cmds.editRenderLayerGlobals( currentRenderLayer=rl)

					for cb in state_comboxs:
						index=cb.rootModelIndex()
						m    = index.model()
						item = m.itemFromIndex(index)

						for child in item.Children[2:]:
							if rl.startswith(child.data()):
								row_num = cb.findText(child.data(),QT.Qt.MatchFlag.MatchExactly)
								cb.setCurrentIndex(0)
								cb.setCurrentIndex(row_num)
								break
	#----------------------------------------------------------------------		
	def emit_render_layer_changed(self):
		self.ACTIVE_RENDER_LAYER_CHANGED.emit()
		if self.Version_Check() >= 2:
			try:
				active_layer = Scripts.NodeCls.M_Nodes.RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
				if cmds.objExists("Vray_Scene_States_Global_Render_Group"):
					master_node = Scripts.NodeCls.M_Nodes.MNODE("Vray_Scene_States_Global_Render_Group")
					active_layer.addMembers([master_node])
				else:
					master_node = None
			except:
				master_node = None
	#----------------------------------------------------------------------
	def update_on_render_layer_Added(self):
		for file_ref in self.model.File_References.Children:
			for asset in file_ref.Children:
				#isinstance(asset, Custom_Widgets.Asset_Item)
				for layer in [layer for layer in Scripts.Global_Constants.Nodes.Render_Layers() if not ":" in layer.name]:
					if not layer.name in [item.data() for item in self.model.Render_Layers.Children]:
						self.model.Render_Layers.appendRow(Custom_Widgets.Maya_Render_Layer_Item(layer))
					if asset._data.attributeExists("renderStates"):
						asset.enum_render_states_plug.enable_Render_Layer_Overide(layer=layer)
					asset.assigned_State_plug.enable_Render_Layer_Overide(layer=layer)
	#----------------------------------------------------------------------
	def Rebuild_Render_Layer_States(self):
		active_layer = Scripts.NodeCls.M_Nodes.RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
		layers = [layer for layer in Scripts.Global_Constants.Nodes.Render_Layers() if not ":" in layer.name]
		if len(layers):
			cmds.progressWindow(title="Rebuilding Layers",progress=0, maxValue = len(layers), status="", isInterruptable=True)
			try:
				warnings = {}
				cmds.refresh(suspend=True)
				if self.Version_Check() == 1:
					for layer in  layers:
						layer.makeCurrent()
						self.emit_render_layer_changed()
						for file_ref in self.model.File_References.Children:
							for asset in file_ref.Children:
								isinstance(asset, Custom_Widgets.Asset_Item)
								asset.clear_Children_From_Render_Layer()
				for layer in layers:
					isinstance(layer, Scripts.NodeCls.M_Nodes.RenderLayer)
					layer.makeCurrent()
					self.emit_render_layer_changed()
					for item in self.Asset_Grid_widget.items:
						isinstance(item, Custom_Widgets.Asset_States_GroupBox)
						scan_result = item.asset_states._asset.Render_States.find_Child_By_UUID(item.asset_states._asset.assigned_State_plug.value)
						if len(scan_result):
							current = item.asset_states.currentIndex()
							if not current.data() == 'Default_Empty':
								item.asset_states.CurrentIndex.parent().child(0,0).data()
							item.asset_states.update_asset_attribute()
							item.asset_states.setCurrentIndex(current)
							item.asset_states.update_asset_attribute()
						else:
							if not item.title() in warnings.keys():
								warnings[item.title()]=[]
							warnings[item.title()].append(str(layer))
					cmds.progressWindow( edit=True, step=1)

				if not len(warnings):
					cmds.confirmDialog( title='Rebuild', message="Rebuild Finished Without Errors")
				else:
					message = ""
					for asset_name,layers in warnings.iteritems():
						message = "The Layers For Reference {}.\nCould Not Be Rebuilt Because Assigned State Does Not Exist\n".format(asset_name)
						message += ",".join(layers)+"\n\n"
					cmds.confirmDialog( title='Rebuild Warnings', message=message)
			except Exception as e:
				cmds.confirmDialog( title='Rebuild Error', message="Rebuild Faild With Error "+ str(e))
			finally:
				cmds.refresh( suspend=False)
				cmds.progressWindow(endProgress=1)
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
		if self.Version_Check() == 1:
			message = "Your Verion Is {}\n".format(self.Version_Check())
			message += "The Current Version is {}\n".format(Custom_Widgets._Vray_Scene_States_Viewer_Current_Version)
			message += 'If You Update To Version 2.\n'
			message += 'All Your Render Layers Will Be Cleared\n'
			message += 'And Group Node Called\n'
			message += 'Vray_Scene_States_Global_Render_Group Will Be Added\n'
			message += 'Parent All Top Level Reference Node Under It\n'
			message += 'And The Display Layers Will Take Care Of The Rest\n\n'
			message += 'WARNING!!! BEFORE YOU UPDATE!!!\n'
			message += 'ANY FILES THAT ARE REFS.\n'
			message += 'THAT THE SCENE STATE MANAGER WAS USED ON\n'
			message += 'NEED TO HAVE HAD THE Sync Display Layers RUN FOR THE NEW VERSION TO WORK\n\n'
			message += 'Do you Want To Continue'
			check = cmds.confirmDialog( title='Out Of Date Version', message=message, button=['yes','no'], defaultButton='no', cancelButton='no', dismissString='no' )
			if check == "yes":
				cmds.fileInfo( 'AW_Vray_States_Viewer_Version', "2" )
				self.model.run_update(full=True)
				# self.Update_Button.hide()
		if self.Version_Check() >= 2 :
			# message = "Your Verion Is {}\n".format(self.Version_Check())
			# message += "The Current Version is {}\n\n".format(Custom_Widgets._Vray_Scene_States_Viewer_Current_Version)
			# message += 'Do To Your Horribly Incompetent Coder.\n\n'
			# message += 'A Bug Was Found That Produces An Inconsistent Display\n'
			# message += 'Of What State Was Last Assigned To A Render Layer.\n\n'
			# message += 'These Inconsistencies Produced Incorrect Rebuilds\n'
			# message += 'By Applying A Different State Than Originally Assigned.\n\n'
			# message += 'The Bug Is Instantiated When A State In The Manager Is Removed\n'
			# message += 'And The Indexing Order Of State Assinment Becomes Offset.\n\n'
			# message += 'This Update Will Force A Render Layer Rebuild\n'
			# message += 'Witch Will Implement The New Lookup Mechanism And Remove The Old One.\n\n'
			# message += 'It Is Impossible To Compinsate For The Index Offset\n'
			# message += 'Do To Not Knowing How Many States May Have Been Deleted.\n\n'
			# message += 'Because The Forced Rebuild Has To Relay On The Old Lookup Mechanism\n'
			# message += 'You Should Make Sure Each Render Layer Has Its Correct State Assigned.\n'
			# check = cmds.confirmDialog( title='Viewer Version', message=message, button=['yes','no'], defaultButton='no', cancelButton='no', dismissString='no')
			States_Viewer = QT.ui_Loader.load(update_warning_file)
			res = States_Viewer.exec_()
			if res:
				self.Rebuild_Render_Layer_States()
				cmds.fileInfo( 'AW_Vray_States_Viewer_Version', "3" )
				# Custom_Widgets._Vray_Scene_States_Viewer_Version = 3
				self.rebuild_Render_layer_states_button.setEnabled(True)
				self.Update_Button.hide()
	#----------------------------------------------------------------------
	def on_multi_state_assignment_button_pushed(self):
		""""""
		cmds.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
		wig = QT.ui_Loader.load(Custom_Widgets.Render_Layer_States_File)
		isinstance(wig,Custom_Widgets.Render_Layer_State_Assignment)
		wig._runsetup(self.model)
		wig.exec_()
		

QT.ui_Loader.registerCustomWidget(Vray_Scene_States_Viewer_MainWindow)

States_Viewer = None

isinstance(States_Viewer, Compiled_Vray_Scene_State_Viewer.Ui_Vray_Scene_States_Viewer)

def make_ui(useBeta=False):
	global States_Viewer
	if States_Viewer == None:
		States_Viewer = QT.ui_Loader.load(ui_file)#Vray_Scene_States_Viewer_MainWindow()
		States_Viewer._use_Beta = useBeta
		States_Viewer._init()
		States_Viewer.move(200,100)
		States_Viewer.show()
		cmds.scriptJob(runOnce=True, event= ["deleteAll",remove_Viewer])
	elif Scripts.General_Maya_Util.getModifier() == 'Ctrl+Alt+Shift':
		try:
			cmds.scriptJob(kill=States_Viewer._Render_Layer_Changed_Script_Job_ID)
			cmds.scriptJob(kill=States_Viewer._Render_Layer_Added_Script_Job_ID)
			cmds.scriptJob(kill=States_Viewer._Post_Scene_Read_Script_Job_ID)
		except:
			pass
		remove_Viewer()
		States_Viewer = QT.ui_Loader.load(ui_file)
		States_Viewer._use_Beta = useBeta
		States_Viewer._init()
		States_Viewer.move(200,100)
		States_Viewer.show()
	else:
		States_Viewer.show()
	return States_Viewer

def remove_Viewer():
	global States_Viewer
	if States_Viewer is not None:
		States_Viewer.hide()
		States_Viewer.setParent(None)
		States_Viewer = None

