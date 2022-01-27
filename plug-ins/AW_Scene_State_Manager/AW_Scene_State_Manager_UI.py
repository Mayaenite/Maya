from maya import cmds, mel, utils, OpenMayaUI
import maya.OpenMaya     as OM_V1
import maya.api.OpenMaya as OM_V2

from functools import partial
from itertools import count
import sys
import os
import types
import logging
import collections
import math
import uuid
import QT
import importlib

Qt        = QT.Qt
QtCore    = QT.QtCore
QtGui     = QT.QtGui
QtSlot    = QT.QtSlot
QtSignal  = QT.QtSignal
uic       = QT.uic
import AW_Scene_State_Manager_UI_rc
import QT.DataModels.Qt_Roles_And_Enums
import QT.My_Py_Side.QtGui.QWidget
import QT.My_Py_Side.QtGui.QStandardItem
import QT.My_Py_Side.QtGui.QStandardItemModel
import QT.My_Py_Side.QtGui.QTreeView
import QT.My_Py_Side.QtGui.QListView
import QT.My_Py_Side.QtGui.QTableView
import QT.My_Py_Side.QtCore.QMimeData

QWidget            = QT.My_Py_Side.QtGui.QWidget.QWidget
QStandardItem      = QT.My_Py_Side.QtGui.QStandardItem.QStandardItem
QStandardItemModel = QT.My_Py_Side.QtGui.QStandardItemModel.QStandardItemModel
QTreeView          = QT.My_Py_Side.QtGui.QTreeView.QTreeView
QListView          = QT.My_Py_Side.QtGui.QListView.QListView
QTableView         = QT.My_Py_Side.QtGui.QTableView.QTableView
QMimeData          = QT.My_Py_Side.QtCore.QMimeData.QMimeData
Drag_And_Drop_MimeData          = QT.My_Py_Side.QtCore.QMimeData.Drag_And_Drop_MimeData
Qt_Roles_And_Enums = QT.DataModels.Qt_Roles_And_Enums
IDRLS              = Qt_Roles_And_Enums.Standered_Item_Data_Roles


import Scripts.NodeCls.M_Nodes
import Scripts.OpenMaya_Util_API
import Scripts.General_Maya_Util
import Scripts.Global_Constants.Nodes
import Scripts.UIFns.Find_UI
import Scripts.UICls
import Scripts.Utility_And_Helpers
import Scripts.callbacks

importlib.reload(Scripts.NodeCls.M_Nodes)
importlib.reload(Scripts.Global_Constants.Nodes)

callbacks             = Scripts.callbacks
MCallbackIdWrapper    = callbacks.MCallbackIdWrapper
UIs                   = Scripts.UICls
Find_UI               = Scripts.UIFns.Find_UI
wrapInstance          = QT.wraperfn
M_Nodes               = Scripts.NodeCls.M_Nodes
Display_Layers        = Scripts.Global_Constants.Nodes.Display_Layers
Render_Layers         = Scripts.Global_Constants.Nodes.Render_Layers
Shading_Engines       = Scripts.Global_Constants.Nodes.Shading_Engines
Global_Variables      = Scripts.General_Maya_Util.Mel_Global_Variables()
Option_Variables      = Scripts.General_Maya_Util.OptionVariables()
MayaUndoChunk         = Scripts.OpenMaya_Util_API.MayaUndoChunk
MayaSkipUndoChunk     = Scripts.OpenMaya_Util_API.MayaSkipUndoChunk
HashableMObjectHandle = Scripts.Utility_And_Helpers.HashableMObjectHandle

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin, MayaQWidgetDockableMixin

def make_logger():
	logger = logging.getLogger('AW Scene States Editor')
	#logger.setLevel(logging.WARNING)
	logger.setLevel(logging.DEBUG)
	if len(logger.handlers) == 0:
		formatter = logging.Formatter('[%(name)s] %(levelname)s: %(message)s')
		ch = logging.StreamHandler()
		ch.setFormatter(formatter)
		logger.addHandler(ch)
		logger.propagate=0   # do not propagate to the standard Maya logger or it will double-represent it in the logs
	return logger

logger = make_logger()

#----------------------------------------------------------------------
def create_Resource_Icon(rc):
	pixmap  = QT.QtGui.QPixmap(rc)
	icon = QT.QtGui.QIcon(pixmap)
	return icon

_beauty_parts_icon        = create_Resource_Icon(":/items/beauty_parts")
_vray_objectprops_icon    = create_Resource_Icon(":/items/object_props")
_invisible_parts_item     = create_Resource_Icon(":/items/invisible_parts")
_matte_parts_icon         = create_Resource_Icon(":/items/matte_parts")
_part_sets_icon           = create_Resource_Icon(":/items/part_sets")
_scene_state_icon         = create_Resource_Icon(":/items/scene_state")
_scene_state_list_icon    = create_Resource_Icon(":/items/scene_state_list")
_scene_state_manager_icon = create_Resource_Icon(":/items/state_manager")
_transform_icon           = create_Resource_Icon(":/maya_types/transform")

objectType_to_icon =  dict(AW_Scene_State_Manager=_scene_state_manager_icon,
                           AW_Scene_State_List=_scene_state_list_icon,
                           AW_Scene_State=_scene_state_icon,
                           AW_Matte_Parts=_matte_parts_icon,
                           AW_Invisible_Parts=_invisible_parts_item,
                           AW_Beauty_Parts=_beauty_parts_icon,
                           AW_Part_Sets=_part_sets_icon,
                           VRayObjectProperties=_vray_objectprops_icon,
                           transform=_transform_icon)
########################################################################
class NMSG(object):
	ConnectionMade    = OM_V1.MNodeMessage.kConnectionMade
	ConnectionBroken  = OM_V1.MNodeMessage.kConnectionBroken
	Att_Eval          = OM_V1.MNodeMessage.kAttributeEval
	Att_Set           = OM_V1.MNodeMessage.kAttributeSet
	Att_Locked        = OM_V1.MNodeMessage.kAttributeLocked
	Att_Unlocked      = OM_V1.MNodeMessage.kAttributeUnlocked
	Att_Added         = OM_V1.MNodeMessage.kAttributeAdded
	Att_Removed       = OM_V1.MNodeMessage.kAttributeRemoved
	Att_Renamed       = OM_V1.MNodeMessage.kAttributeRenamed
	Att_Keyable       = OM_V1.MNodeMessage.kAttributeKeyable
	Att_Unkeyable     = OM_V1.MNodeMessage.kAttributeUnkeyable
	Array_Added       = OM_V1.MNodeMessage.kAttributeArrayAdded
	Array_Removed     = OM_V1.MNodeMessage.kAttributeArrayRemoved
	IncomingDirection = OM_V1.MNodeMessage.kIncomingDirection
	OtherPlugSet      = OM_V1.MNodeMessage.kOtherPlugSet


	Key_ChangeInvalid = OM_V1.MNodeMessage.kKeyChangeInvalid
	Make_Keyable      = OM_V1.MNodeMessage.kMakeKeyable
	Make_Unkeyable    = OM_V1.MNodeMessage.kMakeUnkeyable
########################################################################
class Maya_Item(QStandardItem):
	def __init__(self, node):
		super(Maya_Item, self).__init__(node.nice_name)
		self.node = node
		isinstance(self.node, M_Nodes.MNODE)
		
	#----------------------------------------------------------------------
	def data(self, role=IDRLS.DISPLAY):
		""""""
		if role == IDRLS.DECORATION:
			if self.node.objectType in objectType_to_icon:
				return objectType_to_icon[self.node.objectType]
		if role == IDRLS.FOREGROUND:
			if self.node.isFromReferencedFile:
				return QtGui.QColor("red")
		return QtGui.QStandardItem.data(self, role)
	def setData(self, value, role):
		if role == IDRLS.EDIT:
			self.node.name = value
		else:
			super(Maya_Item, self).setData(value , role)
	def select_node(self):
		cmds.select(self.node.name,noExpand=True)

########################################################################
class Maya_Transform_Item(Maya_Item):
	pass

########################################################################
class AW_Scene_State_Manager_Item(Maya_Item):
	pass
########################################################################
class AW_Scene_State_List_Item(Maya_Item):
	pass
########################################################################
class AW_Scene_State_Item(Maya_Item):
	
	def setData(self, value, role):
		if role == IDRLS.EDIT:
			with MayaUndoChunk():
				self.node.name = value
				for child in self.Children:
					if isinstance(child, AW_Beauty_Parts_Item):
						child.node.name = value + "_Beauty"
					elif isinstance(child, AW_Matte_Parts_Item):
						child.node.name = value + "_Matte"
					elif isinstance(child, AW_Invisible_Parts_Item):
						child.node.name = value + "_Invisible"
		else:
			super(Maya_Item, self).setData(value , role)
########################################################################
class AW_Matte_Parts_Item(Maya_Item):
	#----------------------------------------------------------------------
	def data(self, role=IDRLS.DISPLAY):
		""""""
		if role == IDRLS.DISPLAY:
			return "Matte"
		return super(AW_Matte_Parts_Item, self).data(role)
########################################################################
class AW_Invisible_Parts_Item(Maya_Item):
	#----------------------------------------------------------------------
	def data(self, role=IDRLS.DISPLAY):
		""""""
		if role == IDRLS.DISPLAY:
			return "Invisible"
		return super(AW_Invisible_Parts_Item, self).data(role)
########################################################################
class AW_Beauty_Parts_Item(Maya_Item):
	#----------------------------------------------------------------------
	def data(self, role=IDRLS.DISPLAY):
		""""""
		if role == IDRLS.DISPLAY:
			return "Beauty"
		return super(AW_Beauty_Parts_Item, self).data(role)
########################################################################
class AW_Part_Sets_Item(Maya_Item):
	pass
########################################################################
class Vray_ObjectProperties_Item(Maya_Item):
	pass

Class_to_objectType =  dict(AW_Scene_State_Manager=AW_Scene_State_Manager_Item,
                            AW_Scene_State_List=AW_Scene_State_List_Item,
                            AW_Scene_State=AW_Scene_State_Item,
                            AW_Matte_Parts=AW_Matte_Parts_Item,
                            AW_Invisible_Parts=AW_Invisible_Parts_Item,
                            AW_Beauty_Parts=AW_Beauty_Parts_Item,
                            AW_Part_Sets=AW_Part_Sets_Item,
                            VRayObjectProperties=Vray_ObjectProperties_Item,
                            transform=Maya_Transform_Item)

#----------------------------------------------------------------------
def add_State_Function(item):
	return partial(cmds.awSceneState, (), **{"edit":True, "addState":True})


#----------------------------------------------------------------------
def add_Part_Function(item):
	manager_item = item
	return partial(cmds.awSceneState, (), **{"edit":True, "addPart":True})


#----------------------------------------------------------------------
def remove_State_Function(item):
	if not isinstance(item, AW_Scene_State_Item) or item.node.isFromReferencedFile:
		return False
	else:
		return partial(cmds.awSceneState, (), **{"edit":True, "removeState":True, "state": item.text()})

#----------------------------------------------------------------------
def assine_Selected_To_Part_Set_Function(item):
	if isinstance(item, Vray_ObjectProperties_Item):
		if not item.node.isFromReferencedFile:
			items = cmds.ls(sl=True,type="transform",long=True)
			if len(items):
				return partial(cmds.awSceneState, (), **{"edit":True, "assineNodes":True, "part":item.text(), "node": items})
	return False
#----------------------------------------------------------------------
def make_item(node, parent=None):
	isinstance(node, M_Nodes.MNODE)
	if str(node.objectType) in Class_to_objectType:
		res = Class_to_objectType[str(node.objectType)](node)
	else:
		res = Maya_Item(node)
	if isinstance(parent, (Maya_Item, QtGui.QStandardItem, QStandardItem)):
		parent.appendRow([res])
	return res

########################################################################
class Scene_State_MimeData(Drag_And_Drop_MimeData):
	def __init__(self, indexes, **kwargs):
		super(Scene_State_MimeData, self).__init__(indexes, **kwargs)

########################################################################
class AW_Scene_States_Item_Model(QStandardItemModel):
	MODEL_REPOPULATED =  QtSignal()
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		""""""
		super(AW_Scene_States_Item_Model, self).__init__(parent=parent)
		self._registered_Maya_Callbacks         = []
		self._registered_PerNode_Maya_Callbacks = {}
		self._DependFn                          = OM_V1.MFnDependencyNode()
		self._DagFn                             = OM_V1.MFnDagNode()
	#----------------------------------------------------------------------
	def populateModel(self):
		# Create the headers
		self.cleanup()
		self.clear()
		columnHeaders = ['Name']
		for col,colName in enumerate(columnHeaders):
			self.setHeaderData(col, Qt.Horizontal, colName, Qt.EditRole)
		# Recurse through child widgets
		self.scan_dag_path_recursivley(start=True)
		self.MODEL_REPOPULATED.emit()
	#----------------------------------------------------------------------
	def scan_dag_path_recursivley(self,parentItem=None,node=None,start=False):
		if start:
			parentItem          = self.invisibleRootItem()
			scene_state_Manager = cmds.awSceneState()
			self._Manager_Node  = M_Nodes.SelectionSet(str(scene_state_Manager))
			self._Manager_Item  = make_item(self._Manager_Node, parentItem)
			for node in self._Manager_Node.children:
				self.scan_dag_path_recursivley(self._Manager_Item,node)
			isinstance(self._Manager_Item, AW_Scene_State_Manager_Item)
		else:
			elem = make_item(node, parentItem)
			self.addPerNodeMayaCallbacks(elem)
			if node.objectType == "VRayObjectProperties":
				for member in node.members:
					member_elem = make_item(member, elem)
					self.addPerNodeMayaCallbacks(member_elem)
			elif not isinstance(elem, Maya_Transform_Item):
				for node in node.children:
					self.scan_dag_path_recursivley(elem,node)
	#----------------------------------------------------------------------
	def cleanup(self):
		'''Cleanup environment by removing the Maya callbacks, etc.'''
		# MCallbackWrapper items automatically clean themselves up on deletion
		self._registered_PerNode_Maya_Callbacks = {}
		
	#----------------------------------------------------------------------
	def addPerNodeMayaCallbacks(self, item):
		'''
		Add the Maya per-node callbacks for the specified item
		and register them with the widget (so they can be cleaned up).

		:Parameters:
		    nodeObj (MObject)
		'''
		# Get an MObjectHandle for the MObject
		isinstance(item, Maya_Item)
		nodeObj = item.node.obj.object()
		nodeObjHandle = HashableMObjectHandle(nodeObj)

		# Trivial rejection
		#if self._registered_PerNode_Maya_Callbacks.has_key(nodeObjHandle):
			#print ": Maya per-node callback already has a key in the dict. Expected it to be empty. Overwriting."

		# Get a reference to the list for that node in the dict
		# init it to a list if it is a new reference
		perNodeCallbacks = self._registered_PerNode_Maya_Callbacks.setdefault(nodeObjHandle, [])

		# = Membership changed
		cb = callbacks.create_Attribute_Changed_Callback(item.node.name, self.Attribute_Changed_Callback, item)
		perNodeCallbacks.append(cb)

		# = Name changed callback
		cb = callbacks.create_Name_Changed_Callback(item.node.name, self.CB_AW_Scene_State_Manager_Name_Changed, item)
		perNodeCallbacks.append(cb)
	#----------------------------------------------------------------------	
	def removePerNodeMayaCallbacks(self, nodeObjs):
		'''Remove per-node Maya callbacks.
			:Parameters:
				nodeObjs=List of MObject dependency nodes on which to remove the Maya per-node callbacks
		'''
		# Remove existing per-set callbacks
		nodeObjHandles = [HashableMObjectHandle(nodeObj) for nodeObj in nodeObjs]
		# Determine MObjectHandles for the nodeObjs as that is used for the keys
		for nodeObjHandle in nodeObjHandles:
			if nodeObjHandle in self._registered_PerNode_Maya_Callbacks:
				try:
					callback_list = self._registered_PerNode_Maya_Callbacks[nodeObjHandle]
				except KeyError:
					pass
				del self._registered_PerNode_Maya_Callbacks[nodeObjHandle]		
	# ===================
	# Global Callbacks
	# ===================
	#----------------------------------------------------------------------
	def remove_Maya_Scene_CallBacks(self):
		while len(self._registered_Maya_Callbacks):
			cb = self._registered_Maya_Callbacks.pop()
			del cb
	#----------------------------------------------------------------------
	def add_Maya_Scene_Callbacks(self):
		""""""
		self._registered_Maya_Callbacks = []
		cb = callbacks.create_NodeAdded_Callback("AW_Scene_State_Manager" , self.CB_AW_Scene_State_Manager_Added, None)
		self._registered_Maya_Callbacks.append(cb)
		cb = callbacks.create_NodeRemoved_Callback("AW_Scene_State_Manager" , self.CB_AW_Scene_State_Manager_Removed, None)
		self._registered_Maya_Callbacks.append(cb)
		cb = callbacks.create_Scene_Message_Callback(OM_V1.MSceneMessage.kBeforeNew, self.CB_Before_Scene_Change, 'kBeforeNew')
		self._registered_Maya_Callbacks.append(cb)
		cb = Scripts.callbacks.create_Scene_Message_Callback(OM_V1.MSceneMessage.kBeforeOpen, self.CB_Before_Scene_Change, 'kBeforeOpen') 
		self._registered_Maya_Callbacks.append(cb)
		cb = Scripts.callbacks.create_Scene_Message_Callback(OM_V1.MSceneMessage.kAfterNew, self.CB_After_Scene_Changed, 'kBeforeNew') 
		self._registered_Maya_Callbacks.append(cb)
		cb = Scripts.callbacks.create_Scene_Message_Callback(OM_V1.MSceneMessage.kAfterOpen, self.CB_After_Scene_Changed, 'kBeforeOpen') 
		self._registered_Maya_Callbacks.append(cb)
	#----------------------------------------------------------------------
	def CB_Before_Scene_Change(self, clientData):
		self.cleanup()
	#----------------------------------------------------------------------
	def CB_After_Scene_Changed(self, clientData):
		self.remove_Maya_Scene_CallBacks()
		self.populateModel()
		self.add_Maya_Scene_Callbacks()
	#----------------------------------------------------------------------
	def CB_AW_Scene_State_Manager_Added(self, nodeObj, clientData):
		""""""
		self._DependFn.setObject(nodeObj)
		items = self.findItems(self._DependFn.name(), Qt.MatchFixedString|Qt.MatchCaseSensitive|Qt.MatchRecursive, 0)
		if not len(items):
			node = M_Nodes.SelectionSet(self._DependFn.name())
			item = make_item(node, self.invisibleRootItem())
			self.addPerNodeMayaCallbacks(item)
	#----------------------------------------------------------------------
	def CB_AW_Scene_State_Manager_Removed(self, nodeObj, clientData):
		""""""
		self._DependFn.setObject(nodeObj)
		items = self.findItems(self._DependFn.name(), Qt.MatchFixedString|Qt.MatchCaseSensitive|Qt.MatchRecursive, 0)
		if len(items):
			item = items[0]
			root = self.invisibleRootItem()
			root.removeRow(item.row())
	#----------------------------------------------------------------------
	def CB_AW_Scene_State_Manager_Name_Changed(self, nodeObj, prevName, clientData):
		self._DependFn.setObject(nodeObj)
		clientData.setText(self._DependFn.name())
	#----------------------------------------------------------------------
	def Attribute_Changed_Callback(self, msg, plg, otherplg, clientData):
		isinstance(clientData, Maya_Item)
		isinstance(plg, OM_V1.MPlug)
		isinstance(otherplg, OM_V1.MPlug)
		
		if msg & NMSG.ConnectionBroken or msg & NMSG.ConnectionMade or msg & NMSG.OtherPlugSet:
			plg_fn      = OM_V1.MFnAttribute((plg.attribute()))
			otherPlg_fn = OM_V1.MFnAttribute((otherplg.attribute()))
			if msg & NMSG.ConnectionBroken:
				if otherPlg_fn.name() == 'message' and  plg_fn.name() == 'dnSetMembers':
					self._DependFn.setObject(otherplg.node())
					for item in clientData.rowChildren():
						if item.text() == self._DependFn.name():
							clientData.removeRow(item.row())
				elif otherPlg_fn.name() == 'instObjGroups' and  plg_fn.name() == 'dagSetMembers':
					self._DagFn.setObject(otherplg.node())
					node = M_Nodes.MNODE(self._DagFn.name())
					for item in clientData.rowChildren():
						if item.text() == node.nice_name:
							clientData.removeRow(item.row())
							
			elif msg & NMSG.ConnectionMade:
				if otherPlg_fn.name() == 'message' and  plg_fn.name() == 'dnSetMembers':
					self._DependFn.setObject(otherplg.node())
					node = M_Nodes.SelectionSet(self._DependFn.name())
					self.scan_dag_path_recursivley(clientData, node)
					#item = make_item(node, clientData)
					#self.addPerNodeMayaCallbacks(item)
				elif otherPlg_fn.name() == 'instObjGroups' and  plg_fn.name() == 'dagSetMembers':
					self._DagFn.setObject(otherplg.node())
					node = M_Nodes.MNODE(self._DagFn.name())
					self.scan_dag_path_recursivley(clientData, node)
					#item = make_item(node, clientData)
	#----------------------------------------------------------------------
	def mimeData(self, indexes):
		super_data = super(AW_Scene_States_Item_Model,self).mimeData(indexes)
		res = Scene_State_MimeData(indexes, model=self, super_data=super_data)
		return res
	#----------------------------------------------------------------------
	def dropMimeData(self, data, action, row, column, parent):
		if isinstance(data, Scene_State_MimeData):
			parentItem = self.itemFromIndex(parent)
			if isinstance(parentItem, (AW_Beauty_Parts_Item, AW_Invisible_Parts_Item, AW_Matte_Parts_Item)):
				if not parentItem.node.isFromReferencedFile:
					state_name = parentItem.parent().text()
					item_names = [item.text() for  item in  data.items if isinstance(item, Vray_ObjectProperties_Item)]
					
					if len(item_names):
						if isinstance(parentItem, AW_Beauty_Parts_Item):
							cmds.awSceneState(edit=True, assinePart=True, beauty=True,    state=state_name, part=item_names)
						elif isinstance(parentItem, AW_Matte_Parts_Item):
							cmds.awSceneState(edit=True, assinePart=True, matte=True,     state=state_name, part=item_names)
						elif isinstance(parentItem, AW_Invisible_Parts_Item):
							cmds.awSceneState(edit=True, assinePart=True, invisible=True, state=state_name, part=item_names)
					return False
				return False
			elif isinstance(parentItem, Vray_ObjectProperties_Item):
				item_names = [item.text() for  item in  data.items if isinstance(item, Maya_Transform_Item)]
				
				if len(item_names):
					cmds.awSceneState(edit=True, assineNodes=True, part=parentItem.text(), node=item_names)
				return False
			else:
				part_set_items = []
				for item in  data.items:
					if isinstance(item, Vray_ObjectProperties_Item):
						parentItem = item.parent()
						if isinstance(parentItem, (AW_Beauty_Parts_Item, AW_Invisible_Parts_Item, AW_Matte_Parts_Item)):
							part_set_items.append(item)
				if len(part_set_items):
					with MayaUndoChunk():
						for item in part_set_items:
							state_item = item.parent().parent()
							cmds.awSceneState(edit=True, unAssinePart=True, state=state_item.text(), part=item.text())
				return False
						
		return False
########################################################################
class List_View(QListView):
	def __init__(self, *args, **kwargs):
		super(List_View, self).__init__(*args, **kwargs)
########################################################################
class AW_Part_Sets_List_View(List_View):
	def __init__(self, *args, **kwargs):
		super(AW_Part_Sets_List_View, self).__init__(*args, **kwargs)
########################################################################		
class AW_Scene_States_List_View(List_View):
	def __init__(self, *args, **kwargs):
		super(AW_Scene_States_List_View, self).__init__(*args, **kwargs)

	@QtSlot()
	#----------------------------------------------------------------------
	def remove_Selected_Scene_States(self):
		""""""
		states = []
		m = self.model()
		for index in self.selectedIndexes():
			item = m.itemFromIndex(index)
			if not item.node.isFromReferencedFile:
				states.append(item.text())
		if len(states):
			cmds.awSceneState(edit=True, removeState=True, state=states)
			
########################################################################
class Tree_View(QTreeView):
	def __init__(self, *args, **kwargs):
		super(Tree_View, self).__init__(*args, **kwargs)
	#----------------------------------------------------------------------
	def contextMenuActions(self, menu, item):
		action_select = QtGui.QAction(menu)
		action_select.setText("select")
		action_select.triggered.connect(partial(cmds.select, item.text(), **{"noExpand":True}))
		menu.addAction(action_select)
		add_state_fn = add_State_Function(item)
		
		action_add_state = QtGui.QAction(menu)
		action_add_state.setText("Add Scene State")
		action_add_state.triggered.connect(add_state_fn)
		menu.addAction(action_add_state)
		
		remove_state_fn = remove_State_Function(item)
		if remove_state_fn:
			action_remove_state = QtGui.QAction(menu)
			action_remove_state.setText("Remove Scene State")
			action_remove_state.triggered.connect(remove_state_fn)
			menu.addAction(action_remove_state)
			
		add_part_fn = add_Part_Function(item)
		action_add_part = QtGui.QAction(menu)
		action_add_part.setText("Add Part Set")
		action_add_part.triggered.connect(add_part_fn)
		menu.addAction(action_add_part)
		
		assine_selected_to_part_set_fn = assine_Selected_To_Part_Set_Function(item)
		if assine_selected_to_part_set_fn:
			action_assine_selected_to_part = QtGui.QAction(menu)
			action_assine_selected_to_part.setText("Assine Selected Transforms")
			action_assine_selected_to_part.triggered.connect(assine_selected_to_part_set_fn)
			menu.addAction(action_assine_selected_to_part)		
		
	def contextMenuEvent(self, event):
		win = self.window()
		index = self.indexAt(event.pos())
		item  = self.model().itemFromIndex(index)
		if index.isValid():
			menu = QtGui.QMenu(self)
			self.contextMenuActions(menu,item)
			menu.exec_(event.globalPos())
########################################################################		
class AW_Part_Sets_Tree_View(QListView):
	def __init__(self, *args, **kwargs):
		super(AW_Part_Sets_List_View, self).__init__(*args, **kwargs)
########################################################################		
class AW_Scene_States_Tree_View(QTreeView):
	def __init__(self, *args, **kwargs):
		super(AW_Scene_States_Tree_View, self).__init__(*args, **kwargs)
		model = AW_Scene_States_Item_Model(parent=self)
		self.setModel(model)
	#----------------------------------------------------------------------
	def contextMenuActions(self, menu, item):
		action_select = QtGui.QAction(menu)
		action_select.setText("select")
		action_select.triggered.connect(partial(cmds.select, item.text(), **{"noExpand":True}))
		menu.addAction(action_select)
		add_state_fn = add_State_Function(item)
		
		action_add_state = QtGui.QAction(menu)
		action_add_state.setText("Add Scene State")
		action_add_state.triggered.connect(add_state_fn)
		menu.addAction(action_add_state)
		
		remove_state_fn = remove_State_Function(item)
		if remove_state_fn:
			action_remove_state = QtGui.QAction(menu)
			action_remove_state.setText("Remove Scene State")
			action_remove_state.triggered.connect(remove_state_fn)
			menu.addAction(action_remove_state)
			
		add_part_fn = add_Part_Function(item)
		action_add_part = QtGui.QAction(menu)
		action_add_part.setText("Add Part Set")
		action_add_part.triggered.connect(add_part_fn)
		menu.addAction(action_add_part)
		
		assine_selected_to_part_set_fn = assine_Selected_To_Part_Set_Function(item)
		if assine_selected_to_part_set_fn:
			action_assine_selected_to_part = QtGui.QAction(menu)
			action_assine_selected_to_part.setText("Assine Selected Transforms")
			action_assine_selected_to_part.triggered.connect(assine_selected_to_part_set_fn)
			menu.addAction(action_assine_selected_to_part)		
		
	def contextMenuEvent(self, event):
		win = self.window()
		index = self.indexAt(event.pos())
		item  = self.model().itemFromIndex(index)
		if index.isValid():
			menu = QtGui.QMenu(self)
			self.contextMenuActions(menu,item)
			menu.exec_(event.globalPos())

# Identical_Node_Editor
# ==============
########################################################################

head, tail = os.path.split(__file__)
tail = tail.split(".")[0] + ".ui"
os.path.join(head, tail)
_ui_file_Path = os.path.join(head, tail)
form, base = uic.loadUiType(_ui_file_Path)

class AW_Scene_States_Editor_Widget(MayaQWidgetDockableMixin, form, QtGui.QWidget):
	def __init__(self, parent=None):
		super(AW_Scene_States_Editor_Widget, self).__init__(parent=parent)
		self.setupUi(self)
		win = self.window()
		isinstance(self.Scene_States_listView, AW_Scene_States_List_View)
		isinstance(self.Part_Sets_listView, AW_Part_Sets_List_View)
		isinstance(self.Part_Sets_List_Group_Box, QtGui.QGroupBox)
		isinstance(self.Scene_States_List_Group_Box, QtGui.QGroupBox)
		isinstance(self.Scene_States_Manager_Tool_Box, QtGui.QGroupBox)
		isinstance(self.Scene_State_Manager_States_Tree, AW_Scene_States_Tree_View)
		
		self.model = AW_Scene_States_Item_Model(parent=self)
		self.model.MODEL_REPOPULATED.connect(self.assine_Model_Data)
		#self.setAttribute(Qt.WA_DeleteOnClose, True)
		
	#----------------------------------------------------------------------
	def assine_Model_Data(self):
		""""""
		self.Scene_State_Manager_States_Tree.setModel(self.model)
		self.Part_Sets_listView.setModel(self.model)
		self.Scene_States_listView.setModel(self.model)
		self.Part_Sets_listView.setRootIndex(self.model._Manager_Item.child(1).index())
		self.Scene_States_listView.setRootIndex(self.model._Manager_Item.child(0).index())
		
	@QtSlot()
	#----------------------------------------------------------------------
	def add_New_Scene_State(self):
		""""""
		cmds.awSceneState(edit=True, addState=True)
	@QtSlot()
	#----------------------------------------------------------------------
	def add_New_Part_Set(self):
		""""""
		cmds.awSceneState(edit=True, addPart=True)
		
	@QtSlot()
	#----------------------------------------------------------------------
	def remove_Render_States(self):
		""""""
		cmds.awSceneState(edit=True, addPart=True)	
	@QtSlot()
	#----------------------------------------------------------------------
	def _Initialize(self):
		""""""
		self.model.populateModel()
		self.model.remove_Maya_Scene_CallBacks()
		self.model.cleanup()
		self.model.populateModel()
		self.model.add_Maya_Scene_Callbacks()
		self.assine_Model_Data()
	#----------------------------------------------------------------------
	def closeEvent(self, event):
		QtGui.QWidget.closeEvent(self, event)
	#----------------------------------------------------------------------	
	def showEvent(self, *args):
		'''Show the widget, add the callbacks, and repopulate the data.'''
		super(AW_Scene_States_Editor_Widget, self).showEvent(*args)
	#----------------------------------------------------------------------
	def hideEvent(self,event):
		'''When widget is hidden, remove the Maya callbacks and clean up.'''
		# NOTE: Not using super() as hideEvent could be called after it seems that self is deleted with __del__ and super does not work then
		QtGui.QWidget.hideEvent(self, event)