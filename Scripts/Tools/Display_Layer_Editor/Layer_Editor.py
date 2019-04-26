
import maya.api.OpenMaya as OM
import pymel.core as pm
from pymel.core import nodetypes
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from maya.app.general import mayaMixin

import PYQT
from PYQT import BASE_CLASS_DEFINITIONS
from PYQT.MAYA_CLASS_DEFINITIONS import Maya_API_Callback_Builders,DATA_MODELS,DATA_TYPES,DATA_VIEWS
from PYQT.MAYA_CLASS_DEFINITIONS.Item_Data_Roles import Maya_Item_Data_Roles

import os
import sys
import logging
import logging.handlers
import Scripts.General_Maya_Util
import Scripts.OpenMaya_Util_API
import Scripts.menu_item_addons
from functools import wraps
from PYQT.RESOURCES.Maya_Innerface_Icons import *

ui_Loader                = PYQT.GUI_Loader
General_Util             = Scripts.General_Maya_Util
Util_API                 = Scripts.OpenMaya_Util_API
MayaQWidgetBaseMixin     = mayaMixin.MayaQWidgetBaseMixin
MayaQWidgetDockableMixin = mayaMixin.MayaQWidgetDockableMixin
S_Msg_A_Flags            = Maya_API_Callback_Builders.Scene_Message_After_Flags
S_Msg_B_Flags            = Maya_API_Callback_Builders.Scene_Message_Before_Flags
S_Msg_Flags              = Maya_API_Callback_Builders.Scene_Message_Flags
Node_Msg_Flags           = Maya_API_Callback_Builders.Node_Message_Flages

from pymel.internal.factories import virtualClasses

#----------------------------------------------------------------------
def name_Depend_Node(node_name):
	""""""
	sel_list = OM.MSelectionList()
	sel_list.add(node_name)
	Mobject = sel_list.getDependNode(0)	
	isinstance(Mobject,OM.MObject)
	return Mobject
#----------------------------------------------------------------------
def name_Depend_Function(node_name):
	""""""
	mobject = name_Depend_Node(node_name)
	res  = OM.MFnDependencyNode(mobject)
	return res
########################################################################
class Callbacks_Collection_Modual(object):
	""""""
	#----------------------------------------------------------------------
	@staticmethod
	def Initialize_Callbacks_Modual():
		""""""
		if not Callbacks_Collection_Modual.Is_Initialized():
			modual = dict()
			modual["SCENE_CALLBACK_IDS"] = []
			modual["PER_NODE_CALLBACK_IDS"] = {}
			modual["NODE_TO_TREE_ITEMS"] = {}
			sys.modules["DML_DISPLAY_LAYER_EDITOR_CALLBACK_IDS"] = modual
	#----------------------------------------------------------------------
	@staticmethod
	def Re_Initialize_Callbacks_Modual():
		""""""
		if not Callbacks_Collection_Modual.Is_Initialized():
			del sys.modules["DML_DISPLAY_LAYER_EDITOR_CALLBACK_IDS"]

		modual = dict()
		modual["SCENE_CALLBACK_IDS"] = []
		modual["PER_NODE_CALLBACK_IDS"] = {}
		modual["NODE_TO_TREE_ITEMS"] = {}
		sys.modules["DML_DISPLAY_LAYER_EDITOR_CALLBACK_IDS"] = modual
	#----------------------------------------------------------------------
	@staticmethod
	def get_Tree_Item_Node_Name(self,tree_item):
		""""""
		return tree_item.data()
	#----------------------------------------------------------------------
	@staticmethod
	def Is_Initialized():
		""""""
		return sys.modules.has_key("DML_DISPLAY_LAYER_EDITOR_CALLBACK_IDS")
	#----------------------------------------------------------------------
	@staticmethod
	def get_Callbacks_Modual():
		""""""
		Callbacks_Collection_Modual.Initialize_Callbacks_Modual()
		res = sys.modules["DML_DISPLAY_LAYER_EDITOR_CALLBACK_IDS"]
		isinstance(res,dict)
		return res
	#----------------------------------------------------------------------
	@staticmethod
	def get_Node_To_Tree_Items_Modual():
		""""""
		res = Callbacks_Collection_Modual.get_Callbacks_Modual()
		res = res["NODE_TO_TREE_ITEMS"]
		isinstance(res,dict)
		return res
	#----------------------------------------------------------------------
	@staticmethod
	def get_Scene_Callback_Ids_Modual():
		""""""
		modual = Callbacks_Collection_Modual.get_Callbacks_Modual()
		res = modual["SCENE_CALLBACK_IDS"]
		isinstance(res,list)
		return res
	#----------------------------------------------------------------------
	@staticmethod
	def get_Per_Node_Callback_Ids_Modual():
		""""""
		modual = Callbacks_Collection_Modual.get_Callbacks_Modual()
		res = modual["PER_NODE_CALLBACK_IDS"]
		isinstance(res,dict)
		return res	
	#----------------------------------------------------------------------
	@staticmethod
	def get_Tree_Items_For_Node(node_name):
		""""""
		Mobject = name_Depend_Node(node_name)
		handel = OM.MObjectHandle(Mobject)
		modual = Callbacks_Collection_Modual.get_Node_To_Tree_Items_Modual()
		if modual.has_key(handel.hashCode()):
			return modual[handel.hashCode()]
		return []
	#----------------------------------------------------------------------
	@staticmethod
	def add_Tree_Item_To_Node(tree_item,node_name=None):
		""""""
		if node_name == None:
			node_name = Callbacks_Collection_Modual.get_Tree_Item_Node_Name(tree_item)
		Mobject = name_Depend_Node(node_name)
		handel = OM.MObjectHandle(Mobject)
		modual = Callbacks_Collection_Modual.get_Node_To_Tree_Items_Modual()
		if not modual.has_key(handel.hashCode()):
			modual[handel.hashCode()]=[]
		modual[handel.hashCode()].append(tree_item)
		return handel
	#----------------------------------------------------------------------
	@staticmethod
	def remove_Node_From_Node_To_Tree_Items_Modual(node_name):
		""""""
		Mobject = name_Depend_Node(node_name)
		handel = OM.MObjectHandle(Mobject)
		modual = Callbacks_Collection_Modual.get_Node_To_Tree_Items_Modual()
		if modual.has_key(handel.hashCode()):
			del modual[handel.hashCode()]
	#----------------------------------------------------------------------
	@staticmethod
	def add_Per_Node_Callbacks(tree_item,node_name=None):
		""""""
		if node_name == None:
			node_name = Callbacks_Collection_Modual.get_Tree_Item_Node_Name(tree_item)
		Mobject = name_Depend_Node(node_name)
		modual = Callbacks_Collection_Modual.get_Per_Node_Callback_Ids_Modual()
		handel = OM.MObjectHandle(Mobject)
		cbs    = tree_item.add_Callbacks()
		modual[handel.hashCode()] = cbs
		return handel
	#----------------------------------------------------------------------
	@staticmethod
	def remove_Per_Node_Callbacks(node_name):
		""""""
		Mobject = name_Depend_Node(node_name)
		handel  = OM.MObjectHandle(Mobject)
		modual = Callbacks_Collection_Modual.get_Per_Node_Callback_Ids_Modual()
		if modual.has_key(handel.hashCode()):
			del modual[handel.hashCode()]
	#----------------------------------------------------------------------
	@staticmethod
	def add_Scene_Callback_Ids(ids):
		""""""
		res = Callbacks_Collection_Modual.get_Scene_Callback_Ids_Modual()
		res.extend(ids)
	#----------------------------------------------------------------------
	@staticmethod
	def clear_Scene_Callback_Ids():
		""""""
		modual = Callbacks_Collection_Modual.get_Callbacks_Modual()
		del modual["SCENE_CALLBACK_IDS"]
		modual["SCENE_CALLBACK_IDS"] = []
	#----------------------------------------------------------------------
	@staticmethod
	def clear_Per_Node_Callbacks():
		""""""
		modual = Callbacks_Collection_Modual.get_Callbacks_Modual()
		del modual["PER_NODE_CALLBACK_IDS"]
		modual["PER_NODE_CALLBACK_IDS"] = {}
	#----------------------------------------------------------------------
	@staticmethod
	def clear_Node_To_Tree_Items():
		""""""
		modual = Callbacks_Collection_Modual.get_Callbacks_Modual()
		del modual["NODE_TO_TREE_ITEMS"]
		modual["NODE_TO_TREE_ITEMS"] = {}

Callbacks_Collection_Modual.Initialize_Callbacks_Modual()

#----------------------------------------------------------------------
def make_logger(name, level=logging.DEBUG):
	def get_log_file(name):
		name = name.replace(" ", "_")
		try:
			folder = os.path.join(os.environ["LOCALAPPDATA"], "ArmstrongWhite", "Maya", "Tools", "Display_Layer_Editor", "Logging", name)
		except KeyError:
			try:
				folder = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "ArmstrongWhite", "Maya", "Tools", "Selection_Set_Editor", "Logging", name)
			except KeyError:
				folder = os.path.join(os.environ["TEMP"], "ArmstrongWhite", "Maya", "Tools", "Selection_Set_Editor", "Logging", name)

		if not os.path.exists(folder):
			os.makedirs(folder)
		filename = os.path.join(folder, "Log.txt")
		return filename
	logger = logging.getLogger(name)
	logger.propagate=0   # do not propagate to the standard Maya logger or it will double-represent it in the logs
	logger.setLevel(level)

	if len(logger.handlers) == 0:
		logfile          = get_log_file(name)
		stream_formatter = logging.Formatter('[%(name)s %(levelname)s] %(message)s')
		file_formatter   = logging.Formatter('%(levelname)s %(funcName)s #%(lineno)d:%(message)s')

		stream_handler   = logging.StreamHandler()
		file_handler     = logging.handlers.RotatingFileHandler( logfile, mode='a', maxBytes=102400, backupCount=10, encoding=None, delay=0)

		stream_handler.setFormatter(stream_formatter)
		stream_handler.setLevel(level)
		logger.addHandler(stream_handler)

		file_handler.setFormatter(file_formatter)
		file_handler.setLevel(level)
		logger.addHandler(file_handler)
	return logger
#----------------------------------------------------------------------
def createColorIcon(color):
	pixmap = PYQT.QPixmap(16, 16)
	painter = PYQT.QPainter(pixmap)
	painter.setPen(PYQT.Qt.NoPen)
	painter.fillRect(PYQT.QRect(0, 0, 16, 16), color)
	painter.end()	
	return PYQT.QIcon(pixmap)
#----------------------------------------------------------------------
def remap_Index_To_Source(func):
	'''
	This decorator is used to manage the unlocking of self for all calls that
	require change access rights to the 'network' node itself.
	'''
	@wraps(func)
	def wrapper(*args, **kws):
		view = args[0]  # args[0] is self
		index = args[1]  # args[0] is a QModelIndex
		if isinstance(view, PYQT.QAbstractItemView):
			view_model = self.model()
			if isinstance(view_model, PYQT.QSortFilterProxyModel):
				index = view_model.mapToSource(index)
		return func(self, index)
	return wrapper
#----------------------------------------------------------------------
def remap_Index_From_Source(func):
	'''
	This decorator is used to manage the unlocking of self for all calls that
	require change access rights to the 'network' node itself.
	'''
	@wraps(func)
	def wrapper(*args, **kws):
		view = args[0]  # args[0] is self
		index = args[1]  # args[0] is a QModelIndex
		if isinstance(view, PYQT.QAbstractItemView):
			view_model = self.model()
			if isinstance(view_model, PYQT.QSortFilterProxyModel):
				index = view_model.mapFromSource(index)
		return func(self, index)
	return wrapper

########################################################################
class DML_DisplayLayerManager_Virtual_Class(pm.nt.DisplayLayerManager):
	""" this is an example of how to create your own subdivisions of existing nodes. """
	#----------------------------------------------------------------------
	@classmethod
	def _isVirtual( cls, obj, name ):
		"""PyMEL code should not be used inside the callback, only API and maya.cmds. """
		return True
	#----------------------------------------------------------------------
	@classmethod	
	def _createVirtual(cls, **kwargs ):
		return "layerManager"
	#----------------------------------------------------------------------
	@classmethod
	def _postCreateVirtual(cls, newNode, **kwargs ):
		""" """
	#----------------------------------------------------------------------
	def iter_Layers(self,ignoreDefault=True):
		for elem in self.displayLayerId.connections(type="displayLayer"):
			if elem.nodeName()=="defaultLayer" and ignoreDefault:
				continue
			yield elem

########################################################################
class DML_Display_Layer_Virtual_Class(nodetypes.DisplayLayer):
	""" this is an example of how to create your own subdivisions of existing nodes. """
	_ClassRegistrationID = 'AAS_Asset_Assembly_ObjectSet_Base'
	## WING IDE CODE COMPLEASHION ##
	if False:
		message       = pm.Attribute()
		dagSetMembers = pm.Attribute()
		dnSetMembers  = pm.Attribute()
		self          = nodetypes.DisplayLayer()
	#----------------------------------------------------------------------
	@classmethod
	def _isVirtual( cls, obj, name ):
		"""PyMEL code should not be used inside the callback, only API and maya.cmds. """
		fn = pm.api.MFnDependencyNode(obj)
		try:
			if not fn.hasAttribute("aasVirtualClassRegistrationName"):
				return True
		except:
			pass
		return False
	#----------------------------------------------------------------------
	@classmethod	
	def _createVirtual(cls, **kwargs ):
		name = kwargs.get("name",kwargs.get("n"))
		if not pm.objExists(name):
			name = str(pm.createDisplayLayer(**kwargs))
		return name
	#----------------------------------------------------------------------
	@classmethod
	def _postCreateVirtual(cls, newNode, **kwargs ):
		""" """
		# add the identifying attribute. the attribute name will be set on subclasses of this class
		newNode = pm.PyNode(newNode)
		isinstance(newNode,cls)
		newNode._postCreateReal(**kwargs)
	#----------------------------------------------------------------------
	def _postCreateReal(self,**kwargs):
		""""""
		pass
	#----------------------------------------------------------------------
	def add_Members(self,*args):
		""""""
		args = pm.ls(args,dagObjects=True)
		items = [self]
		items.extend(args)
		pm.editDisplayLayerMembers(*items,noRecurse=True)
	#----------------------------------------------------------------------
	def add_Members_From_Active_Selection(self):
		self.add_Members(pm.ls(sl=True))
	#----------------------------------------------------------------------
	def remove_Members(self,*args):
		""""""
		input_items = pm.ls(args)
		current_members = self.get_Members()
		items = [item for item in input_items if item in current_members] 
		items = ["defaultLayer"] + items
		pm.editDisplayLayerMembers(*items)
	#----------------------------------------------------------------------
	def remove_Members_In_Active_Selection(self):
		self.remove_Members(pm.ls(sl=True))
	#----------------------------------------------------------------------
	def get_Members(self):
		""""""
		items = pm.editDisplayLayerMembers( self, fullNames=True, query=True )
		if items is not None:
			res = pm.ls(items)
			return res
		else:
			return []
	#----------------------------------------------------------------------
	def get_Member_Count(self):
		if not self.exists():
			return 0
		items = pm.editDisplayLayerMembers( self, fullNames=True, query=True )
		if items is None:
			return 0
		else:
			return len(items)
	#----------------------------------------------------------------------
	def select_Members(self,**kwargs):
		""""""
		pm.select(self.get_Members(),**kwargs)
	#----------------------------------------------------------------------
	def select_set(self):
		self.select(noExpand=True)

	members     = property(get_Members)

virtualClasses.register(DML_DisplayLayerManager_Virtual_Class,False)
virtualClasses.register(DML_Display_Layer_Virtual_Class,False)

########################################################################
class _Global_Options(object):
	display_show_name_spaces                              = General_Util.OptionVar("aw_display_layer_editor_tools_namespaces", True)
	make_first_tab                                        = General_Util.OptionVar("aw_display_layer_editor_tools_make_first_tab", True)
	layers_tab_position                                   = General_Util.OptionVar("aw_display_layer_editor_tools_layers_tab_position", 0)
	selection_set_outliner_option_Filter_Syntax           = General_Util.OptionVar("aw_display_layer_editor_outlineer_filter_syntax", 1)
	selection_set_outliner_option_Filter_Case_Sensitivity = General_Util.OptionVar("aw_display_layer_editor_outlineer_filter_case_sensitivity", False)
	selection_set_outliner_option_Filter_Scan_Type        = General_Util.OptionVar("aw_display_layer_editor_outlineer_filter_scan_type", 0)
	display_layer_editor_selection_style                  = General_Util.OptionVar("aw_display_layer_editor_selection_style", 0)
########################################################################
class ActiveSelectionRestore(object):
	''''''
	#----------------------------------------------------------------------
	def __enter__(self):
		self.active_Selection = Util_API.get_Active_Selection_List(OldApi=False)
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		cmds.select(self.active_Selection.getSelectionStrings())
########################################################################
class Maya_QWidget(mayaMixin.MayaQWidgetBaseMixin, PYQT.QWidget):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Maya_QWidget, self).__init__(parent=parent)

########################################################################
class Maya_PushButton(PYQT.QPushButton):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Maya_PushButton, self).__init__(parent=parent)

########################################################################
class Maya_LineEdit(PYQT.QLineEdit):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Maya_LineEdit, self).__init__(parent=parent)
########################################################################
class OptionVariable_Bool_Action(PYQT.QAction):
	def __init__(self, name, var_name, var_val=True, parent=None):
		super(OptionVariable_Bool_Action, self).__init__(name, parent)
		if isinstance(var_name, General_Util.OptionVar):
			self._variable = var_name
		else:
			self._variable = General_Util.OptionVar(var_name, var_val)
		self.setCheckable(True)
		self.setChecked(PYQT.Qt.Checked if self.variable_value else PYQT.Qt.Unchecked)
		self.changed.connect(self.update_variable)
	#----------------------------------------------------------------------
	@PYQT.QtSlot()
	def update_variable(self):
		""""""
		self.variable_value =  self.isChecked()
	#----------------------------------------------------------------------
	@property
	def variable_value(self):
		""""""
		return self._variable.value
	#----------------------------------------------------------------------
	@variable_value.setter
	def variable_value(self, val):
		""""""
		self._variable.value = val
########################################################################
class Make_First_Tab_OptionVariable_Action(OptionVariable_Bool_Action):
	def __init__(self, parent=None):
		super(Make_First_Tab_OptionVariable_Action, self).__init__("Make First Tab", _Global_Options.make_first_tab, var_val=True, parent=parent)
		self.changed.connect(self.on_Changed_Set_Tab_Position)
	#----------------------------------------------------------------------
	@PYQT.QtSlot()
	def on_Changed_Set_Tab_Position(self):
		""""""
		tab_layout = Scripts.menu_item_addons.find_UI_By_Name("DisplayLayerTab").getParent()
		tabs       = tab_layout.getTabLabelIndex()
		
		aw_display_position  = tabs.index('AW Diplay')+1
		last_tab_position = len(tabs)
		
		if self.isChecked() and not aw_display_position == 1:
			tab_layout.moveTab([aw_display_position,1])
			maya_display_position = tab_layout.getTabLabelIndex().index('Display')+1
			tab_layout.moveTab([maya_display_position, last_tab_position])
			tab_layout.setSelectTab("aw_display_layer_editor_tab")
			
		elif not self.isChecked() and aw_display_position == 1:
			tab_layout.moveTab([aw_display_position,last_tab_position])
			maya_display_position = tab_layout.getTabLabelIndex().index('Display')+1
			tab_layout.moveTab([maya_display_position, 1])
			tab_layout.setSelectTab("aw_display_layer_editor_tab")
########################################################################
class Display_Option_Tool_Button(PYQT.QToolButton):
	def _run_setup(self):
		self.setText("Display Options")
		self.option_make_first_tab   = Make_First_Tab_OptionVariable_Action()
		self.addActions([self.option_make_first_tab])
		
########################################################################
class OptionVariable_ComboBox(PYQT.QComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None, var_name=None, var_val=0):
		super(OptionVariable_ComboBox, self).__init__(parent)
		if isinstance(var_name, General_Util.OptionVar):
			self._variable = var_name
		else:
			self._variable = General_Util.OptionVar(var_name, var_val)
	#----------------------------------------------------------------------
	def _inishalize(self):
		""""""
		self.setCurrentIndex(self._variable.value)
		self.currentIndexChanged.connect(self.update_variable)
	#----------------------------------------------------------------------
	@PYQT.QtSlot(int)
	def update_variable(self, index):
		""""""
		self._variable.value =  index
		
########################################################################
class OptionVariable_Layers_Tab_Position_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None, var_name=None, var_val=0):
		super(OptionVariable_Layers_Tab_Position_ComboBox, self).__init__(parent,_Global_Options.layers_tab_position,0)
	#----------------------------------------------------------------------
	def _inishalize(self):
		""""""
		super(OptionVariable_Layers_Tab_Position_ComboBox, self)._inishalize()
		self.currentIndexChanged.connect(self.on_Current_Index_Changed_Set_Tab_Position)
		self.on_Current_Index_Changed_Set_Tab_Position(self._variable.value)
	#----------------------------------------------------------------------
	@PYQT.QtSlot(str)
	def on_Current_Index_Changed_Set_Tab_Position(self,val):
		""""""
		if isinstance(val,int):
			val =["north", "east","west"][val] 
		tab_layout = Scripts.menu_item_addons.find_UI_By_Name("DisplayLayerTab").getParent()
		tab_layout.setTabPosition(val)
		
########################################################################
class OptionVariable_CheckBox(PYQT.QCheckBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None, var_name=None, var_val=0):
		super(OptionVariable_CheckBox, self).__init__(parent)
		if isinstance(var_name, General_Util.OptionVar):
			self._variable = var_name
		else:
			self._variable = General_Util.OptionVar(var_name, var_val)
	#----------------------------------------------------------------------
	def _inishalize(self):
		""""""
		self.setChecked(self._variable.value)
		self.stateChanged.connect(self.update_variable)
	#----------------------------------------------------------------------
	@PYQT.QtSlot(int)
	def update_variable(self, val):
		""""""
		self._variable.value =  val


########################################################################
class AW_Display_Layer_Editor_Filter_Style_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(AW_Display_Layer_Editor_Filter_Style_ComboBox, self).__init__(parent=parent, var_name=_Global_Options.selection_set_outliner_option_Filter_Syntax, var_val=0)
		self.addItem("Starts With")
		self.addItem("Ends With")
		self.addItem("Contains")
		self._inishalize()
	#----------------------------------------------------------------------
	def get_PatternSyntax(self):
		""""""
		return PYQT.QRegExp.PatternSyntax(self.itemData(self.currentIndex()))

########################################################################
class AW_Display_Layer_Editor_Item_Selection_Style_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(AW_Display_Layer_Editor_Item_Selection_Style_ComboBox, self).__init__(parent=parent, var_name=_Global_Options.display_layer_editor_selection_style, var_val=0)
		self.addItem("Extended",userData=PYQT.QAbstractItemView.SelectionMode.ExtendedSelection.name)
		self.addItem("Multi",userData=PYQT.QAbstractItemView.SelectionMode.MultiSelection.name)
		self.addItem("Contiguous",userData=PYQT.QAbstractItemView.SelectionMode.ContiguousSelection.name)
		self.addItem("Single Selection",userData=PYQT.QAbstractItemView.SelectionMode.SingleSelection.name)
		self._inishalize()
	#----------------------------------------------------------------------
	def get_Selection_Style(self):
		""""""
		return PYQT.QAbstractItemView.SelectionMode.ContiguousSelection.values[self.itemData(self.currentIndex())]
########################################################################
class AW_Display_Layer_Editor_Filter_Case_Sensitivity_CheckBox(OptionVariable_CheckBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(AW_Display_Layer_Editor_Filter_Case_Sensitivity_CheckBox, self).__init__(parent=parent, var_name=_Global_Options.selection_set_outliner_option_Filter_Case_Sensitivity, var_val=0)
		self._inishalize()

	#----------------------------------------------------------------------
	def get_CaseSensitivity(self):
		""""""
		return [PYQT.Qt.CaseSensitivity.CaseInsensitive, PYQT.Qt.CaseSensitivity.CaseSensitive][self.isChecked()]
########################################################################
class Filter_Scan_Options_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Filter_Scan_Options_ComboBox, self).__init__(parent=parent, var_name=_Global_Options.selection_set_outliner_option_Filter_Scan_Type, var_val=0)
		self.addItem("Simple")
		self.addItem("Complex")
		self._inishalize()

########################################################################
class Tool_Button(PYQT.QToolButton):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		"""Constructor"""
		super(Tool_Button, self).__init__(parent=parent)

########################################################################
class WidgetDelegate(PYQT.QStyledItemDelegate):
	"""A delegate for drawing a arbitrary QWidget"""
	#----------------------------------------------------------------------
	def __init__(self, item_data, parent=None):
		""""""
		super(WidgetDelegate, self).__init__(parent)
		self.item_data = item_data
		isinstance(self.item_data, Item_Data)
	#----------------------------------------------------------------------
	def paint(self, painter, option, index):
		""""""
		PYQT.QStyledItemDelegate.paint(self, painter, option, index)
	#----------------------------------------------------------------------
	def editorEvent(self, event, model, option, index):
		""""""
		return super(WidgetDelegate, self).editorEvent(event, model, option, index)
	#----------------------------------------------------------------------
	def helpEvent(self, event, view, option, index):
		""""""
		super(WidgetDelegate, self).helpEvent(event, view, option, index)
	#----------------------------------------------------------------------
	def sizeHint(self, option, index):
		""""""
		return PYQT.QStyledItemDelegate.sizeHint(self, option, index)
	#----------------------------------------------------------------------
	def commitData(self, editor):
		""""""
		super(WidgetDelegate, self).commitData(editor)
	#----------------------------------------------------------------------
	def createEditor(self, parent, option, index):
		""" Creates and returns the custom object we'll use to edit."""
		editor = self.item_data.create_editor(parent)
		if editor is None:
			return PYQT.QStyledItemDelegate.createEditor(self, parent, option, index)
		else:
			return editor
	#----------------------------------------------------------------------
	def closeEditor(self, editor, endedithint=PYQT.QAbstractItemDelegate.NoHint):
		""""""
		super(WidgetDelegate, self).closeEditor(editor, endedithint)
	#----------------------------------------------------------------------
	def setEditorData(self, editor, index):
		""" Sets the data to be displayed and edited by our custom editor. """
		PYQT.QStyledItemDelegate.setEditorData(self, editor, index)
	#----------------------------------------------------------------------
	def setModelData(self, editor, model, index):
		""" Get the data from our custom editor and stuffs it into the model."""
		PYQT.QStyledItemDelegate.setModelData(self, editor, model, index) 
########################################################################
class Display_Layer_Container_Tree_Item(BASE_CLASS_DEFINITIONS.DATA_TYPES.Model_Items.Base_Model_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,model=None, parent_item=None):
		"""Constructor"""
		item = BASE_CLASS_DEFINITIONS.DATA_TYPES.Item_Data_Storage.Internal_Item_Data(tree_item=self, selectable=False, enabled=True, editable=False, dragable=False, dropable=False, display_name="Display Layer Container")
		super(Display_Layer_Container_Tree_Item,self).__init__(model=model, parent_item=parent_item, items=[item])
		self._node_added_callback_id = None
		self._node_removed_callback_id = None
	#----------------------------------------------------------------------
	def cleanup(self,*args):
		'''Cleanup environment by removing the Maya callbacks, etc.'''
		# Scan Through All The Childern
		for child in self.all_childern:
			if hasattr(child,"remove_Callbacks"):
				# Remove All The Maya Callbacks Befor We Clear The Root
				child.remove_Callbacks()

		# This Function Removes All The child Tree Items
		# and removes That PerNode Callbacks
		self.clear_Children()
	#----------------------------------------------------------------------
	def repopulate(self,*args):
		'''Clear and populate the table with data retrieved from the Maya scene. Add Maya callbacks for changes to trigger UI updates.'''
		# Clear items in QTreeWidget
		#self.logger.debug("Creating AW Master Selection Set Grouping Node")
		for layer in pm.ls(type="displayLayer"):
			if not "defaultLayer" in layer.nodeName():
				self.add_Display_Layer(layer)
		self.model.layoutChanged.emit()
	#----------------------------------------------------------------------
	def CB_On_Node_Added(self,mobject,clientData):
		""""""
		fn = OM.MFnDependencyNode(mobject)
		self.add_Display_Layer(fn.name())
	#----------------------------------------------------------------------
	def CB_On_Node_Removed(self,mobject,clientData):
		""""""
		fn = OM.MFnDependencyNode(mobject)
		self.remove_Display_Layer(fn.name())
	#----------------------------------------------------------------------
	def add_Callbacks(self):
		""""""
		self._node_added_callback_id = Maya_API_Callback_Builders.create_NodeAdded_Callback("displayLayer",self.CB_On_Node_Added)
		self._node_removed_callback_id = Maya_API_Callback_Builders.create_NodeRemoved_Callback("displayLayer",self.CB_On_Node_Removed)
	#----------------------------------------------------------------------
	def add_Display_Layer(self,layer):
		""""""
		layer = pm.PyNode(layer)
		if not "defaultLayer" in layer.nodeName():
			if not layer in self.get_Display_Layers():
				layer_tree_item = Display_Layer_Tree_Item(layer, model=self.model, parent_item=None)
				self.appendChild(layer_tree_item)
				return layer_tree_item
	#----------------------------------------------------------------------
	def get_Display_Layers(self):
		""""""
		res = []
		for item in self.childItems:
			res.append(item.get_internal_Data())
		return res
	#----------------------------------------------------------------------
	def remove_Display_Layer(self,layer):
		""""""
		layer = pm.PyNode(layer)
		for item in self.childItems:
			if item.get_internal_Data() == layer:
				self.removeChild(item)

########################################################################
class Display_Layer_Tree_Item_Data(DATA_TYPES.Node_Item_Data.Base_Maya_Node_Data):
	""""""
	_vis_off_color   = PYQT.QBrush(PYQT.Constants.Colors.RED)
	_vis_empty_color = PYQT.QBrush(PYQT.Constants.Colors.CYAN)
	_vis_insel_color = PYQT.QBrush(PYQT.Constants.Colors.GREEN)
	#----------------------------------------------------------------------
	def __init__(self, node,**kwargs):
		#if not len(node.drawInfo.connections()):
			#kwargs["foreground_color"]=PYQT.Constants.Colors.CYAN
		kwargs["checkable"]=True
		if node.visibility.get():
			kwargs["foreground_color"]=PYQT.Constants.Colors.WHITE
		else:
			kwargs["foreground_color"]=PYQT.Constants.Colors.RED
		super(Display_Layer_Tree_Item_Data,self).__init__(node,**kwargs)
		## WING IDE CODE COMPLEASHION ##
		if False:
			isinstance(self.internal_data,DML_Display_Layer_Virtual_Class)
	#----------------------------------------------------------------------
	def _fn_get_checked_value(self):
		""""""
		try:
			if self.internal_data.visibility.get():
				return PYQT.Qt.CheckState.Checked
			else:
				return PYQT.Qt.CheckState.Unchecked
		except:
			return None
	#----------------------------------------------------------------------
	def _fn_set_checked_value(self,value):
		""""""
		try:
			if value:
				self.internal_data.visibility.set(True)
			else:
				self.internal_data.visibility.set(False)
		except:
			pass
		super(Display_Layer_Tree_Item_Data,self)._fn_set_checked_value(value)
	#----------------------------------------------------------------------
	def _selection_contains_members(self):
		""""""
		sel = set(pm.ls(sl=True))
		mem = set(self.internal_data.get_Members())
		return len(sel.intersection(mem))
	##----------------------------------------------------------------------
	#def data(self, role=Maya_Item_Data_Roles.DISPLAY):
		#if role == Maya_Item_Data_Roles.FOREGROUND:
			#if not self.internal_data.get_Member_Count():
				#return self._vis_empty_color
			#if not self.internal_data.visibility.get():
				#return self._vis_off_color
		#return super(Display_Layer_Tree_Item_Data, self).data(role)
########################################################################
class Display_Layer_Tree_Item(DATA_TYPES.Model_Items.Base_Maya_Node_Item):
	_Item_Type = PYQT.userType_generator()
	#logger = make_logger("Diplay Layer Tree Item", logging.INFO)
	#----------------------------------------------------------------------
	def __init__(self, layer, model=None, parent_item=None):
		self._check_in_progress = False
		layer = DML_Display_Layer_Virtual_Class(layer)
		items = [Display_Layer_Tree_Item_Data(layer),DATA_TYPES.Node_Item_Data.Base_Maya_Plug_Data(layer.visibility)]
		super(Display_Layer_Tree_Item, self).__init__(model, parent_item, items)
		Callbacks_Collection_Modual.add_Per_Node_Callbacks(self,layer.nodeName())
		Callbacks_Collection_Modual.add_Tree_Item_To_Node(self,layer.nodeName())
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = super(Display_Layer_Tree_Item,self).get_internal_Data(column=column)
		## WING IDE CODE COMPLEASHION ##
		if False:
			isinstance(res, Display_Layer_Tree_Item_Data)
		return res
	#----------------------------------------------------------------------
	def add_Callbacks(self):
		'''
		Add the Maya per-node callbacks for the specified item
		and register them with the widget (so they can be cleaned up).
		'''
		res = []
		internal_data = self.get_internal_Data()
		# Member Assinments Changed Callback
		res.append(Maya_API_Callback_Builders.create_Attribute_Changed_Callback(internal_data.name(), self._on_Attribute_Changed, None))
		#res.append(Maya_API_Callback_Builders.create_Node_Pre_Removal_Callback(internal_data.nodeName(), self.CB_On_Node_Removed))
		return res
	#----------------------------------------------------------------------
	def CB_On_Node_Removed(self,mobject,clientData):
		""""""
		self.remove_Callbacks()
		self.parentItem.removeChild(self)
	#----------------------------------------------------------------------
	def remove_Callbacks(self):
		""""""
		internal_data = self.get_internal_Data()
		Callbacks_Collection_Modual.remove_Per_Node_Callbacks(internal_data.nodeName())
		Callbacks_Collection_Modual.remove_Node_From_Node_To_Tree_Items_Modual(internal_data.nodeName())
	#----------------------------------------------------------------------
	def apply_color_change(self):
		if not len(self.get_internal_Data().drawInfo.connections()):
			self._column_items.set_foreground_color(PYQT.Constants.Colors.CYAN)
		elif self.get_internal_Data().visibility.get():
			self._column_items.set_foreground_color(PYQT.Constants.Colors.WHITE)
		else:
			self._column_items.set_foreground_color(PYQT.Constants.Colors.RED)
		self._check_in_progress = False
		self._column_items.items[0]._update_Changed_Data(Maya_Item_Data_Roles.FOREGROUND)
	#----------------------------------------------------------------------
	def _on_Attribute_Changed(self, msg, plug , other, client):

		isinstance(plug ,OM.MPlug)
		isinstance(other,OM.MPlug)
		if Maya_API_Callback_Builders.Node_Message_Flages.Was_Attribute_Set(msg):
			#for check in ["visibility","hideOnPlayback","texturing","shading","levelOfDetail","displayType"]:
			if "visibility" in plug.name():
				#if not len(self.get_internal_Data().drawInfo.connections()):
					#self._column_items.set_foreground_color(PYQT.Constants.Colors.CYAN)
				if plug.asBool():
					self._column_items.set_foreground_color(PYQT.Constants.Colors.WHITE)
				else:
					self._column_items.set_foreground_color(PYQT.Constants.Colors.RED)
				self._column_items.items[0]._update_Changed_Data(Maya_Item_Data_Roles.FOREGROUND)

		#if Maya_API_Callback_Builders.Node_Message_Flages.Was_Connection_Broken(msg):
			#if "drawInfo" in plug.name():
				#if not self._check_in_progress:
					#pm.evalDeferred(self.apply_color_change,lowestPriority=True)
					#self._check_in_progress = True
		#if Maya_API_Callback_Builders.Node_Message_Flages.Was_Connection_Made(msg):
			#if "drawInfo" in plug.name():
				#if not self._check_in_progress:
					#pm.evalDeferred(self.apply_color_change,lowestPriority=True)
					#self._check_in_progress = True
	#----------------------------------------------------------------------
	def repopulate(self):
		'''Clear and populate the table with data retrieved from the Maya scene.
		Add Maya callbacks for creaseSet changes to trigger UI updates.
		'''
		## Remove existing per-set callbacks
		## MCallbackWrapper objects auto-remove themselves.
		## See also self.removePerNodeMayaCallbacks()
		#self.logger.debug("repopulating Display Layer %r" % self.data())
		## Clear items in QTreeWidget
		pass
########################################################################
class AW_Display_Layer_Editor_List_View(DATA_VIEWS.List_Views.DATA_VIEWS.List_Views.Filtered_Proxy_List_View):
	UPDATE_SELECTION = PYQT.QtSignal()
	ACTIVE_SELECTION_CHANGED = PYQT.QtSignal(*(PYQT.QModelIndex, ))
	SELECTION_CHANGED        = PYQT.QtSignal(PYQT.QItemSelection, PYQT.QItemSelection)
	CURRENT_CHANGED          = PYQT.QtSignal(PYQT.QModelIndex, PYQT.QModelIndex)
	def __init__(self, parent=None):
		super(AW_Display_Layer_Editor_List_View, self).__init__(parent)
	#----------------------------------------------------------------------
	def dragEnterEvent(self,event):
		"""
		dragEnterEvent(event)
			event=PYQT.QDragEnterEvent

		This event handler is called when a drag is in progress and the mouse enters this widget
		The event is passed in the event parameter.
		If the event is ignored, the widget wont receive any drag move events .
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(AW_Display_Layer_Editor_List_View,self).dragEnterEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragLeaveEvent(self,event):
		"""
		dragLeaveEvent(event)
			event=PYQT.QDragLeaveEvent

		This event handler is called when a drag is in progress and the mouse leaves this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(AW_Display_Layer_Editor_List_View,self).dragLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragMoveEvent(self,event):
		"""
		dragMoveEvent(event)
			event=PYQT.QDragMoveEvent

		This event handler is called if a drag is in progress, and when any of the following conditions occur: the cursor enters this widget, the cursor moves within this widget, or a modifier key is pressed on the keyboard while this widget has the focus
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(AW_Display_Layer_Editor_List_View,self).dragMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		"""
		dropEvent(event)
			event=PYQT.QDropEvent

		This event handler is called when the drag is dropped on this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(AW_Display_Layer_Editor_List_View,self).dropEvent(event)
		return res
	#----------------------------------------------------------------------
	def enterEvent(self,event):
		""""""
		super(AW_Display_Layer_Editor_List_View,self).enterEvent(event)
	#----------------------------------------------------------------------
	def selectionChanged(self,selected,deselected):
		"""
		selectionChanged(selected,deselected)
			selected=PYQT.QItemSelection
			deselected=PYQT.QItemSelection

		This slot is called when the selection is changed
		The previous selection (which may be empty), is specified by deselected , and the new selection by selected.
		"""
		isinstance(selected, PYQT.QItemSelection)
		isinstance(deselected, PYQT.QItemSelection)
		PYQT.QListView.selectionChanged(self, selected, deselected)
		self.UPDATE_SELECTION.emit()
		self.SELECTION_CHANGED.emit(selected, deselected)
		if selected.count() >= 1:
			first_index = selected.indexes()[0]
			self.ACTIVE_SELECTION_CHANGED.emit(first_index)
	#----------------------------------------------------------------------
	def currentChanged(self,current,previous):
		"""
		currentChanged(current,previous)
			current=PYQT.QModelIndex
			previous=PYQT.QModelIndex

		This slot is called when a new item becomes the current item
		The previous current item is specified by the previous index, and the new item by the current index.
		If you want to know about changes to items see the PySide.PYQT.QAbstractItemView.dataChanged() signal.
		"""
		PYQT.QListView.currentChanged(self, current,previous)
		self.CURRENT_CHANGED.emit(current,previous)
	#----------------------------------------------------------------------
	def mouseDoubleClickEvent(self,event):
		"""
		mouseDoubleClickEvent(event)
			event=PYQT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse double click events for the widget.
		The default implementation generates a normal mouse press event.
		"""
		if event.button() == PYQT.Qt.MouseButton.MidButton:
			active = self.SelectedIndexes
			if len(active):
				item = active[0]
				internal = item.data(Maya_Item_Data_Roles.INTERNAL_DATA)
				layer = internal.get_internal_Data()
				if layer.visibility.get():
					layer.visibility.set(False)
				else:
					layer.visibility.set(True)
				event.setAccepted(False)
				return False
		res = super(AW_Display_Layer_Editor_List_View,self).mouseDoubleClickEvent(event)
	#----------------------------------------------------------------------
	def mouseMoveEvent(self,event):
		"""
		mouseMoveEvent(event)
			event=PYQT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse move events for the widget.
		If mouse tracking is switched off, mouse move events only occur if a mouse button is pressed while the mouse is being moved
		If mouse tracking is switched on, mouse move events occur even if no mouse button is pressed.
		QMouseEvent.pos() reports the position of the mouse cursor, relative to this widget
		For press and release events, the position is usually the same as the position of the last mouse move event, but it might be different if the users hand shakes
		This is a feature of the underlying window system, not Qt.
		If you want to show a tooltip immediately, while the mouse is moving (e.g., to get the mouse coordinates with QMouseEvent.pos() and show them as a tooltip), you must first enable mouse tracking as described above
		Then, to ensure that the tooltip is updated immediately, you must call QToolTip.showText() instead of PySide.PYQT.QWidget.setToolTip() in your implementation of PySide.PYQT.QWidget.mouseMoveEvent() .
		"""
		res = super(AW_Display_Layer_Editor_List_View,self).mouseMoveEvent(event)
	#----------------------------------------------------------------------
	def mousePressEvent(self,event):
		"""
		mousePressEvent(event)
			event=PYQT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse press events for the widget.
		If you create new widgets in the PySide.PYQT.QWidget.mousePressEvent() the PySide.PYQT.QWidget.mouseReleaseEvent() may not end up where you expect, depending on the underlying window system (or X11 window manager), the widgets location and maybe more.
		The default implementation implements the closing of popup widgets when you click outside the window
		For other widget types it does nothing.
		"""
		if event.button() == PYQT.Qt.MouseButton.MidButton:
			index = self.indexAt(event.pos())
			if index.isValid():
				internal_data = index.data(Maya_Item_Data_Roles.INTERNAL_DATA)
				layer         = internal_data.get_internal_Data()
				print "Middle Mouse Pressed on {}".format(layer.nodeName())
				if event.modifiers() == PYQT.Qt.Modifier.CTRL:
					layer.select_Members()
				elif event.modifiers() == PYQT.Qt.Modifier.CTRL | PYQT.Qt.Modifier.SHIFT:
					for other in internal_data.parent.childItems:
						other_layer = other.get_internal_Data()
						if not other_layer == layer:
							other_layer.visibility.set(False)
						else:
							other_layer.visibility.set(True)
				else:
					if internal_data.data(column=1):
						internal_data.setData(False, column=1,role=Maya_Item_Data_Roles.EDIT)
					else:
						internal_data.setData(True, column=1,role=Maya_Item_Data_Roles.EDIT)
					internal_data.column_items.items[1]._update_Changed_Data(Maya_Item_Data_Roles.FOREGROUND)
		else:
			res = super(AW_Display_Layer_Editor_List_View,self).mousePressEvent(event)
	#----------------------------------------------------------------------
	def mouseReleaseEvent(self,event):
		"""
		mouseReleaseEvent(event)
			event=PYQT.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse release events for the widget.
		"""
		res = super(AW_Display_Layer_Editor_List_View,self).mouseReleaseEvent(event)
	#----------------------------------------------------------------------
	def get_index(self, index):
		""""""
		if isinstance(self.model(), PYQT.QSortFilterProxyModel):
			index = self.model().mapFromSource(index)
		return index
	#----------------------------------------------------------------------
	def modify_Selection_Of_Index(self, item, command):
		""""""
		if hasattr(item,"index"):
			index = self.get_index(item.index)
		elif issubclass(item.__class__, PYQT.QModelIndex):
			index = self.get_index(item)
		else:
			raise ValueError("input Must Be a Tree_Item Or QModelIndex")

		rec = self.visualRect(index)
		self.setSelection(rec, command)
	#----------------------------------------------------------------------
	def replace_Selection(self, items=[]):
		""""""
		self.clearSelection()
		for item in items:
			self.modify_Selection_Of_Index(item, PYQT.QItemSelectionModel.SelectionFlag.Select)
		if len(items):
			self.scrollTo(self.get_index(item.index))
	#----------------------------------------------------------------------
	def _Create_Context_Menus(self,index):
		""""""
		editor = self.parentWidget().parentWidget().parentWidget()
		internal_data = index.data(Maya_Item_Data_Roles.INTERNAL_DATA)
		context_menu   = PYQT.QMenu(self)
		layer         = internal_data.get_internal_Data()
		# Options_Menu         = self.selection_set_view_set_item_context_menu.addMenu("Options")
		# Display_Options_Menu = Options_Menu.addMenu("Display")
		#selection_Menu       = self._context_menu.addMenu("Selecting")
		#Assinments_Menu      = self._context_menu.addMenu("Assinments")
		#Viewport_Menu        = self._context_menu.addMenu("Viewport")

		## Color ConText Menus
		action = PYQT.QAction("select Members",context_menu)
		action.triggered.connect(layer.select_Members)
		context_menu.addAction(action)

		action = PYQT.QAction("Remove Selected",context_menu)
		action.triggered.connect(layer.remove_Members_In_Active_Selection)
		context_menu.addAction(action)

		action = PYQT.QAction("Add Selected",context_menu)
		action.triggered.connect(layer.add_Members_From_Active_Selection)
		context_menu.addAction(action)

		context_menu.addSeparator()

		select_main_menu      = context_menu.addMenu("Select")

		action = PYQT.QAction("select Hilighted Members",context_menu)
		action.triggered.connect(editor.on_Select_Layer_Members_Button_clicked)
		select_main_menu.addAction(action)

		edit_menu             = context_menu.addMenu("Edit")

		return context_menu
		#placement_menu.addAction(self._main_window.action_Move_Highlighted_Down)

		#node_locking_menu.addAction(self._main_window.action_Lock_Highlighted_Sets)
		#node_locking_menu.addAction(self._main_window.action_Unlock_Highlighted_Sets)

		#selection_Menu.addAction(self._main_window.action_Select_Highlighted_Sets)
		#selection_Menu.addAction(self._main_window.action_Select_Highlighted_Child_Sets)
		#selection_Menu.addAction(self._main_window.action_Select_Highlighted_Set_Members)
		#selection_Menu.addAction(self._main_window.action_Select_Highlighted_Set_Member_Recursively)

		#Assinments_Menu.addAction(self._main_window.action_Add_Selection_To_Highlighted_Sets)
		#Assinments_Menu.addAction(self._main_window.action_Remove_Selection_From_Highlighted_Sets)
		#Assinments_Menu.addSeparator()
		#Assinments_Menu.addAction(self._main_window.action_Add_Highlighted_Nodes_To_Highlighted_Set)
		#Assinments_Menu.addAction(self._main_window.action_Remove_Highlighted_From_Parent_Sets)

		#Viewport_Menu.addAction(self._main_window.action_Frame_Highlighted_Set_Members)
		#Viewport_Menu.addAction(self._main_window.action_Frame_Highlighted)
		#Viewport_Menu.addAction(self._main_window.action_Reveal_Highlighted_Outliner_Panel)
	#----------------------------------------------------------------------
	def contextMenuEvent(self, event):
		mods     = event.modifiers()
		key_mods = PYQT.Qt.KeyboardModifier
		index = self.indexAt(event.pos())
		if index.isValid():
			if mods == key_mods.NoModifier:
				context_menu = self._Create_Context_Menus(index)
				context_menu.exec_(event.globalPos())
########################################################################
class TreeModel(DATA_MODELS.Node_Tree_Model.TreeModel):
	def __init__(self, parent=None, root_item=None, headers=[]):
		super(TreeModel, self).__init__(parent=parent, root_item=root_item, headers=headers)

########################################################################
class Display_Layer_Manager_Model(TreeModel):
	''''''
	# ==============
	# OVERRIDDEN FUNCTIONS
	# ==============
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		'''		'''
		#self.logger = make_logger("Display Layer Manager Model", logging.INFO)
		super(Display_Layer_Manager_Model, self).__init__(parent=parent, root_item=None, headers=["Name","visibility","playback","texturing","shading","levelOfDetail","displayType","overrideRGBColors","color","overrideColorRGB","enabled"])
		self.layer_container = Display_Layer_Container_Tree_Item(model=self, parent_item=self.rootItem)

########################################################################
class Display_Layer_Manager_Proxy_Model(DATA_MODELS.Node_Proxy_Models.BASE_SORT_FILTER_PROXY_MODEL):
	""""""
	startswith,endswith,contains = range(3)
	def __init__(self, parent=None):
		super(Display_Layer_Manager_Proxy_Model, self).__init__(parent=parent)
		self._filter_type =  self.startswith
		self._line_input_widget = None
	#----------------------------------------------------------------------
	def assign_Line_Input(self,widget):
		""""""
		isinstance(widget,PYQT.QLineEdit)
		self._line_input_widget = widget
		widget.textEdited.connect(self.setFilterFixedString)
	#----------------------------------------------------------------------
	def filterAcceptsRow(self,source_row, source_parent):
		""""""
		if not source_parent.isValid():
			return True
		if self.FilterRegExp.isEmpty():
			return True

		child_value = source_parent.child(source_row,0).data()
		pattern     = self.FilterRegExp.pattern()
		if self.filterCaseSensitivity() == PYQT.Qt.CaseSensitivity.CaseInsensitive:
			child_value = child_value.lower()
			pattern = pattern.lower()

		if self._filter_type == self.startswith:
			return child_value.startswith(pattern)
		elif self._filter_type == self.endswith:
			return child_value.endswith(pattern)
		else:
			return pattern in child_value

	#----------------------------------------------------------------------
	@PYQT.Slot(int)
	def set_Filter_Type(self,val):
		""""""
		self._filter_type = val
		self.sort()

########################################################################
class _CODE_COMPLEATION_HELPER(PYQT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		''''''
		super(_CODE_COMPLEATION_HELPER,self).__init__(parent=parent)
		if False:
			self.AWDisplay_Layer_Editor           = AW_Display_Layer_Editor()
			self.Layer_Editor_Main_Tool_Bar       = PYQT.QFrame()
			self.toolButton                       = Display_Option_Tool_Button()
			self.label_2                          = PYQT.QLabel()
			self.Filter_Options_Frame             = PYQT.QFrame()
			self.Filter_Options_label             = PYQT.QLabel()
			self.Filter_Style_comboBox            = AW_Display_Layer_Editor_Filter_Style_ComboBox()
			self.Filter_Case_checkBox             = AW_Display_Layer_Editor_Filter_Case_Sensitivity_CheckBox()
			self.Filter_Options_Text              = Maya_LineEdit()
			self.Layer_Controls_Frame             = PYQT.QFrame()
			self.Layer_Visibility_Toggle_Button   = Maya_PushButton()
			self.Layer_Visibility_On_Button       = Maya_PushButton()
			self.Layer_Visibility_Off_Button      = Maya_PushButton()
			self.Layer_Visibility_All_Off_Button  = Maya_PushButton()
			self.Layer_Visibility_All_On_Button   = Maya_PushButton()
			self.Display_Types                    = PYQT.QStackedWidget()
			self.List_View_Page                   = PYQT.QWidget()
			self.listView                         = AW_Display_Layer_Editor_List_View()
			self.Table_View_Page                  = PYQT.QWidget()
			self.tableView                        = PYQT.QTableView()
			self.Tree_View_Page                   = PYQT.QWidget()
			self.treeView                         = PYQT.QTreeView()
			self.Hilight_Selection_Tools_Button   = PYQT.QToolButton()
			self.Layer_Editing_Frame              = PYQT.QFrame()
			self.Select_Layer_Members_Button      = Maya_PushButton()
			self.Add_Layers_Members_Button        = Maya_PushButton()
			self.Remove_Layer_Members_Button      = Maya_PushButton()
			self.Create_New_Empty_Layer_Button    = Maya_PushButton()
			self.Create_New_Selected_Layer_Button = Maya_PushButton()
			self.Delete_Layer_Button              = Maya_PushButton()
			self.label                            = PYQT.QLabel()
			self.View_Selection_Mode_comboBox     = AW_Display_Layer_Editor_Item_Selection_Style_ComboBox()
			self.verticalLayout_4                 = PYQT.QVBoxLayout()
			self.horizontalLayout                 = PYQT.QHBoxLayout()
			self.verticalLayout_3                 = PYQT.QVBoxLayout()
			self.Filter_Options_Layout            = PYQT.QHBoxLayout()
			self.gridLayout                       = PYQT.QGridLayout()
			self.verticalLayout_2                 = PYQT.QVBoxLayout()
			self.verticalLayout                   = PYQT.QVBoxLayout()
			self.verticalLayout_5                 = PYQT.QVBoxLayout()
			self.verticalLayout_7                 = PYQT.QVBoxLayout()
			self.horizontalLayout_5               = PYQT.QHBoxLayout()
			self.horizontalLayout_2               = PYQT.QHBoxLayout()
			self.layers_Tab_Position_comboBox     = OptionVariable_Layers_Tab_Position_ComboBox()

########################################################################
class AW_Display_Layer_Editor(mayaMixin.MayaQWidgetBaseMixin,_CODE_COMPLEATION_HELPER):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(AW_Display_Layer_Editor, self).__init__(parent=parent)
		self._data_model = Display_Layer_Manager_Model(parent=self)	
		self._data_proxy_model = Display_Layer_Manager_Proxy_Model(parent=self)
		self._data_proxy_model.setSourceModel(self._data_model)
		self._data_proxy_model.setDynamicSortFilter(True)
		self._display_layer_tab = None
		if False:
			isinstance(self._display_layer_tab,pm.uitypes.TabLayout)
	#----------------------------------------------------------------------
	def _run_setup(self):
		""""""
		self._display_layer_tab = Scripts.menu_item_addons.find_UI_By_Name("DisplayLayerTab").getParent()
		self._data_proxy_model.assign_Line_Input(self.Filter_Options_Text)
		self._data_model.layer_container.repopulate()
		self._data_proxy_model.setSourceModel(self._data_model)
		self.listView.setModel(self._data_proxy_model)
		self.listView.setRootIndex(self._data_proxy_model.source_Index_From_Item(self._data_model.layer_container))
		self.listView.UPDATE_SELECTION.connect(self._Disable_Add_Button_On_Multi_Selection)
		self.on_Filter_Style_comboBox_currentIndexChanged()
		self.on_Filter_Case_checkBox_stateChanged()
		
		action = PYQT.QAction("Hilight From Active",self.Hilight_Selection_Tools_Button)
		action.setToolTip("Hilight The Display Layers Invalved With The Acive Selection")
		action.setStatusTip("Hilight The Display Layers Invalved With The Acive Selection")
		action.triggered.connect(self.Hilight_Tool_Action_Hilight_From_Active_Selection)
		self.Hilight_Selection_Tools_Button.addAction(action)
		
		action = PYQT.QAction("Hilight From Active And Parents",self.Hilight_Selection_Tools_Button)
		action.setToolTip("Hilight The Display Layers Invalved With The Acive Selection And All Of There Parents")
		action.setStatusTip("Hilight The Display Layers Invalved With The Acive Selection And All Of There Parents")
		action.triggered.connect(self.Hilight_Tool_Action_Hilight_From_Active_Selection_And_Parents)
		self.Hilight_Selection_Tools_Button.addAction(action)
		
		action = PYQT.QAction("Hilight Empty Layers",self.Hilight_Selection_Tools_Button)
		action.setToolTip("Hilight The Display Layers That Have Nothing In Them ")
		action.setStatusTip("Hilight The Display Layers That Have Nothing In Them")
		action.triggered.connect(self.Hilight_Tool_Action_Hilight_Empty_Display_Layers)
		self.Hilight_Selection_Tools_Button.addAction(action)
		self.toolButton._run_setup()
		self.layers_Tab_Position_comboBox._inishalize()
	#----------------------------------------------------------------------
	def _Disable_Add_Button_On_Multi_Selection(self):
		""""""
		if len(self.listView.SelectedIndexes) > 1:
			self.Add_Layers_Members_Button.setEnabled(False)
		else:
			self.Add_Layers_Members_Button.setEnabled(True)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def Hilight_Tool_Action_Hilight_From_Active_Selection_And_Parents(self):
		""""""
		items = []
		layers = pm.listConnections(pm.ls(sl=True),type="displayLayer")
		layers += pm.listConnections(pm.listRelatives(pm.ls(sl=True),allParents=True),type="displayLayer")
		layers = list(set(layers))
		for item in layers:
			tree_item = self._data_model.layer_container.find_child(item.nodeName())
			if tree_item is not None:
				items.append(tree_item)
		if len(items):
			self.listView.replace_Selection(items)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def Hilight_Tool_Action_Hilight_From_Active_Selection(self):
		""""""
		items = []
		for item in pm.listConnections(pm.ls(sl=True),type="displayLayer"):
			tree_item = self._data_model.layer_container.find_child(item.nodeName())
			if tree_item is not None:
				items.append(tree_item)
		if len(items):
			self.listView.replace_Selection(items)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def Hilight_Tool_Action_Hilight_Empty_Display_Layers(self):
		""""""
		items = []
		for child in self._data_model.layer_container.childItems:
			isinstance(child,Display_Layer_Tree_Item)
			if not child.get_internal_Data().get_Member_Count():
				items.append(child)
		if len(items):
			self.listView.replace_Selection(items)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Create_New_Empty_Layer_Button_clicked(self):
		""""""
		#pm.mel.eval("layerEditorCreateLayer 1;")
		pm.createDisplayLayer(name="layer1",empty=True,noRecurse=True,makeCurrent=False)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Create_New_Selected_Layer_Button_clicked(self):
		""""""
		#pm.mel.eval("layerEditorCreateLayer 2;")
		pm.createDisplayLayer(name="layer1",noRecurse=True,makeCurrent=False)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Delete_Layer_Button_clicked(self):
		""""""
		items = []
		for item in self.listView.selected_Items():
			items.append(item.get_internal_Data())
		pm.delete(items)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Select_Layer_Members_Button_clicked(self):
		""""""
		items = []
		for item in self.listView.selected_Items():
			items.extend(item.get_internal_Data().members)
		if len(items):
			pm.select(items)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Add_Layers_Members_Button_clicked(self):
		""""""
		items = self.listView.selected_Items()
		if len(items):
			items[0].get_internal_Data().add_Members(pm.ls(sl=True))
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Remove_Layer_Members_Button_clicked(self):
		""""""
		selection = pm.ls(sl=True)
		for item in self.listView.selected_Items():
			item.get_internal_Data().remove_Members(selection)		
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Layer_Visibility_On_Button_clicked(self):
		""""""
		items = []
		for item in self.listView.selected_Items():
			items.append(item.get_internal_Data())
		if len(items):
			with ActiveSelectionRestore():
				pm.select(items)
				args = [".visibility"]
				args.extend([1]*len(items))
				cmds.setAttr(*args)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Layer_Visibility_Off_Button_clicked(self):
		""""""
		items = []
		for item in self.listView.selected_Items():
			items.append(item.get_internal_Data())
		if len(items):
			with ActiveSelectionRestore():
				pm.select(items)
				args = [".visibility"]
				args.extend([0]*len(items))
				cmds.setAttr(*args)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Layer_Visibility_Toggle_Button_clicked(self):
		""""""
		for item in self.listView.selected_Items():
			if item.get_internal_Data().visibility.get():
				item.get_internal_Data().visibility.set(False)
			else:
				item.get_internal_Data().visibility.set(True)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Layer_Visibility_All_Off_Button_clicked(self):
		""""""
		items = [item for item in cmds.ls(type="displayLayer") if not "defaultLayer" in item]
		if len(items):
			with ActiveSelectionRestore():
				cmds.select(items)
				args = [".visibility"]
				args.extend([0]*len(items))
				cmds.setAttr(*args)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Layer_Visibility_All_On_Button_clicked(self):
		""""""
		items = [item for item in cmds.ls(type="displayLayer") if not "defaultLayer" in item]
		if len(items):
			with ActiveSelectionRestore():
				cmds.select(items)
				args = [".visibility"]
				args.extend([1]*len(items))
				cmds.setAttr(*args)
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_View_Selection_Mode_comboBox_currentIndexChanged(self):
		self.listView.setSelectionMode(self.View_Selection_Mode_comboBox.get_Selection_Style())
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Filter_Style_comboBox_currentIndexChanged(self):		
		self._data_proxy_model.set_Filter_Type(self.Filter_Style_comboBox.currentIndex())
		self._data_proxy_model.setFilterFixedString(self._data_proxy_model.FilterRegExp.pattern())
	#----------------------------------------------------------------------
	@PYQT.Slot()
	def on_Filter_Case_checkBox_stateChanged(self):
		""""""
		self._data_proxy_model.setFilterCaseSensitivity(self.Filter_Case_checkBox.get_CaseSensitivity())

#______________________________________________________________________________________________
ui_Loader.registerCustomWidget(Display_Option_Tool_Button)
ui_Loader.registerCustomWidget(OptionVariable_Layers_Tab_Position_ComboBox)
ui_Loader.registerCustomWidget(AW_Display_Layer_Editor_Filter_Case_Sensitivity_CheckBox)
ui_Loader.registerCustomWidget(AW_Display_Layer_Editor_Filter_Style_ComboBox)
ui_Loader.registerCustomWidget(Filter_Scan_Options_ComboBox)
ui_Loader.registerCustomWidget(AW_Display_Layer_Editor_List_View)
ui_Loader.registerCustomWidget(AW_Display_Layer_Editor)
ui_Loader.registerCustomWidget(Maya_QWidget)
ui_Loader.registerCustomWidget(Maya_PushButton)
ui_Loader.registerCustomWidget(Maya_LineEdit)
ui_Loader.registerCustomWidget(AW_Display_Layer_Editor_Item_Selection_Style_ComboBox)


#----------------------------------------------------------------------
def _Perform_Before_Scene_New_And_Open_Clean_Up(wig):
	""""""
	isinstance(wig,AW_Display_Layer_Editor)
	Callbacks_Collection_Modual.clear_Per_Node_Callbacks()
	Callbacks_Collection_Modual.clear_Node_To_Tree_Items()
	wig._data_model.layer_container.cleanup()
#----------------------------------------------------------------------
def CB_Before_Scene_New_Open(wig):
	""""""
	_Perform_Before_Scene_New_And_Open_Clean_Up(wig)
#----------------------------------------------------------------------
def CB_After_Scene_Open_And_New(wig):
	""""""
	pass

#----------------------------------------------------------------------
def _Add_Scene_CallBacks(wig):
	""""""
	ids = []
	## Before Scene Open And New  
	ids.append( Maya_API_Callback_Builders.create_Scene_Before_New_Message_Callback(CB_Before_Scene_New_Open,wig) )
	ids.append( Maya_API_Callback_Builders.create_Scene_Before_Open_Message_Callback(CB_Before_Scene_New_Open,wig) )

	## After Scene Open And New
	#ids.append( Maya_API_Callback_Builders.create_Scene_After_Open_Message_Callback(CB_After_Scene_Open_And_New,wig) )
	#ids.append( Maya_API_Callback_Builders.create_Scene_After_New_Message_Callback(CB_After_Scene_Open_And_New,wig) )
	wig._data_model.layer_container.add_Callbacks()
	Callbacks_Collection_Modual.add_Scene_Callback_Ids(ids)
#----------------------------------------------------------------------
def remove_Layer_Editor():
	""""""
	if pm.menuBarLayout("aw_display_layer_editor_tab",q=True,exists=True):
		pm.deleteUI("aw_display_layer_editor_tab")
#----------------------------------------------------------------------
def add_Layer_Editor():
	""""""
	if not pm.menuBarLayout("aw_display_layer_editor_tab",q=True,exists=True):
		file_path = os.path.join(os.path.dirname(__file__),"UI","AW_Display_Layer_Editor.ui")
		wig = ui_Loader.load_file(file_path)
		PYQT.QMetaObject.connectSlotsByName(wig)
		wig._run_setup()
		if False:
			isinstance(wig,AW_Display_Layer_Editor)
		
		Display_Layer_Tab                     = Scripts.menu_item_addons.find_UI_By_Name("DisplayLayerTab").getParent()
		aw_display_layer_editor_tab           = pm.menuBarLayout("aw_display_layer_editor_tab",parent=Display_Layer_Tab)
		Qt_aw_display_layer_editor_tab        = aw_display_layer_editor_tab.asQtObject()
		Qt_aw_display_layer_editor_tab_layout = Qt_aw_display_layer_editor_tab.layout()
		Qt_aw_display_layer_editor_tab_layout.addWidget(wig)
		Display_Layer_Tab.setTabLabel(["aw_display_layer_editor_tab","AW Diplay"])
		wig.toolButton.option_make_first_tab.on_Changed_Set_Tab_Position()
		if wig.toolButton.option_make_first_tab.isChecked():
			Display_Layer_Tab.setSelectTab("aw_display_layer_editor_tab")
		_Add_Scene_CallBacks(wig)
		return wig
	else:
		return find_Layer_Editor()
#----------------------------------------------------------------------
def find_Layer_Editor():
	""""""
	main_win = pm.uitypes.PyUI("MayaWindow")
	main_win_QT = main_win.asQtObject()
	found_children = main_win_QT.findChildren(PYQT.QWidget,"AWDisplay_Layer_Editor")
	if len(found_children):
		for found_child in found_children:
			if found_child.objectName() == "AWDisplay_Layer_Editor":
				return found_child

def Initialize_Layer_Editor():
	return add_Layer_Editor()