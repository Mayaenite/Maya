#speak = QtCore.Signal((int,), (str,))
import os
import yaml
import Yaml_Config_Data
import uuid

import QT
import QT.DataModels.Qt_Roles_And_Enums
import QT.DataModels.QTreeView
import QT.DataModels.QListView
import QT.DataModels.QStandardItemModel
import QT.DataModels.QSortFilterProxyModel
import QT.DataModels.QStandardItem
import QT.DataModels.QTableView
import QT.DataModels.MimeData
import QT.DataModels.QComboBox

Qt       = QT.Qt
QtSlot   = QT.QtSlot
QtSignal = QT.QtSignal
QtProperty = QT.QtProperty
QtCore   = QT.QtCore
QtGui    = QT.QtGui
uic      = QT.uic

QStandardItemModel    = QT.DataModels.QStandardItemModel.QStandardItemModel
QSortFilterProxyModel = QT.DataModels.QSortFilterProxyModel.QSortFilterProxyModel
QTreeView             = QT.DataModels.QTreeView.QTreeView
QListView             = QT.DataModels.QListView.QListView
QTableView            = QT.DataModels.QTableView.QTableView
QComboBox             = QT.DataModels.QComboBox.QComboBox

try:
	_maya_check = True
	import Scripts.NodeCls.M_Nodes
	import Scripts.UICls.Controls
	import Scripts.UICls.Windows	
	import Scripts.UICls.Layouts
	import Scripts.UICls.Panels
	import Scripts.Global_Constants.Nodes
	import maya.cmds as cmds
	M_Nodes              = Scripts.NodeCls.M_Nodes
	Render_Layer         = M_Nodes.RenderLayer
	Container            = M_Nodes.Container
	Script_Node          = M_Nodes.Script_Node
	SelectionSet         = M_Nodes.SelectionSet
	VRayObjectProperties = M_Nodes.VRayObjectProperties
	M_Layouts            = Scripts.UICls.Layouts
	M_Controls           = Scripts.UICls.Controls
	M_Panels             = Scripts.UICls.Panels
	M_Windows            = Scripts.UICls.Windows
	get_Current_Render_Layer = lambda :cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True )
	

except:
	_maya_check = False

#----------------------------------------------------------------------
def Viewer_Version_check():
	""""""
	version = cmds.fileInfo('AW_Vray_States_Viewer_Version', query=True )
	if len(version):
		version = int(version[0])
	else:
		version = 2
	return version

_Vray_Scene_States_Viewer_Version = Viewer_Version_check()

########################################################################
class Data_Roles(QT.DataModels.Qt_Roles_And_Enums.Standered_Item_Data_Roles):
	ITEM           = QT.userRole_counter()
	ITEM_DATA      = QT.userRole_counter()
	DATA_OBJECT    = QT.userRole_counter()

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Utility Functions
#---------------------------------------------------------------------------------------------------
def AutoQObject(*class_def, **kwargs):
	class Object(QtCore.QObject):
		def __init__(self, **kwargs):
			QtCore.QObject.__init__(self)
			for key, val in class_def:
				self.__dict__['_'+key] = kwargs.get(key, val())

		def __repr__(self):
			values = ('%s=%r' % (key, self.__dict__['_'+key]) \
					  for key, value in class_def)
			return '<%s (%s)>' % (kwargs.get('name', 'QObject'), ', '.join(values))

		for key, value in class_def:
			nfy = locals()['_nfy_'+key] = QtSignal((value))

			def _get(key):
				def f(self):
					return self.__dict__['_'+key]
				return f

			def _set(key):
				def f(self, value):
					self.__dict__['_'+key] = value
					try:
						att = getattr(self,'_nfy_'+key)
						att.emit(value)
					except:
						pass
				return f

	return Object
#----------------------------------------------------------------------
def is_Base_Item_Instance(item):
	""""""
	return isinstance(item,_Base_Item)
#----------------------------------------------------------------------
def name_or_none(item):
	""""""
	if is_Base_Item_Instance(item):
		return item.data()
	else:
		return "None"
	
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Persistent Data Types
_Data_Object = AutoQObject( ['name', str], name='Data_Object')
########################################################################
class Named_Data_Object(object):
	""""""
	def __init__(self,name,**kwargs):
		self.name = name
	def __str__(self):
		return str(self.name)

	def __repr__(self):
		return str(self.name)
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Undo Commands
########################################################################
class Active_Asset_Change_Command(QT.QUndoCommand):
	def __init__(self, view, current, previous, parent=None):
		isinstance(view, Asset_Tree_View)
		isinstance(previous, _Base_Item)
		isinstance(current, Assets_Item)
		
		if not isinstance(previous, _Base_Item):
			previous_name = "None"
		else:
			previous_name = previous.data()
		
		super(Active_Asset_Change_Command, self).__init__("Select %s Deselect %s" % (current.data(), previous_name))
		self.view        = view
		self.current     = current
		self.current_row = current.row()
		self.previous    = previous
		self.resort_data = self.Restore_Data(view, previous)
		
	class Restore_Data(object):
		def __init__(self, asset_view, previous_asset_item):
			isinstance(asset_view,Asset_Tree_View)
			isinstance(previous_asset_item,Asset_Item)
			self.asset_view          = asset_view
			self.render_states_view  = asset_view.render_states_view
			self.part_sets_view      = asset_view.part_sets_view
			self.previous_asset_item = previous_asset_item
			self.current_render_item = self.render_states_view.current_item()
			
		def restore(self):
			if is_Base_Item_Instance(self.previous_asset_item):
				self.asset_view.set_Current_Item(self.previous_asset_item)
				if is_Base_Item_Instance(self.current_render_item):
					self.render_states_view.set_Current_Item(self.current_render_item)
				else:
					self.render_states_view.clearSelection()
			else:
				self.asset_view.clearSelection()
				self.render_states_view.clearSelection()
				
	def undo(self):
		self.resort_data.restore()

	def redo(self):
		if not self.view.current_item().row() == self.current_row:
			self.view.set_Current_Item(self.current)
			
########################################################################
class Selection_Change_Command(QT.QUndoCommand):
	def __init__(self, view, current, previous, parent=None):
		previous_name = name_or_none(previous)
		current_name  = name_or_none(current)
		super(Selection_Change_Command, self).__init__("Select %s Deselect %s" % (current_name, previous_name))
		self.view        = view
		self.current     = current
		self.previous    = previous
		isinstance(self.view, Filtered_Proxy_List_View)
		isinstance(self.previous, _Base_Item)
		isinstance(self.current, _Base_Item)

	def undo(self):
		if is_Base_Item_Instance(self.previous):
			self.view.set_Current_Item(self.previous)
		else:
			self.view.clearSelection()
	def redo(self):
		if self.view.current_item().row() != self.current.row():
			self.view.set_Current_Item(self.current)
			
########################################################################
class Rename_Item_Command(QT.QUndoCommand):
	def __init__(self, item, newName, parent=None):
		super(Rename_Item_Command, self).__init__("Reparent Items")
		self.newName     = newName
		self.oldName     = oldName

	def undo(self):
		for item in self.items:
			item.assine_to_old_parent()

	def redo(self):
		for item in self.items:
			item.assine_to_new_parent()


########################################################################
class Reparent_Items_Command(QT.QUndoCommand):
	def __init__(self, newParent, items, parent=None):
		super(Reparent_Items_Command, self).__init__("Reparent Items")
		self.items         =  [self.Item_Data(item, newParent) for item in items]
		self.newParent     =  newParent

	class Item_Data(object):
		def __init__(self, item, newParent):
			self.item       =  item
			self.old_Parent =  item.parent()
			self.new_Parent =  newParent
			isinstance(self.item, _Base_Item)
			isinstance(self.new_Parent, _Base_Item)
			isinstance(self.old_Parent, _Base_Item)

		def assine_to_new_parent(self):
			self.old_row    =  self.item.row()
			self.old_Parent.removeRow(self.old_row)
			self.new_Parent.appendRow(self.item)

		def assine_to_old_parent(self):
			row = self.item.row()

			self.new_Parent.removeRow(row)
			self.old_Parent.insertRow(self.old_row, self.item)



	def undo(self):
		for item in reversed(self.items):
			item.assine_to_old_parent()

	def redo(self):
		for item in self.items:
			item.assine_to_new_parent()


########################################################################
class Move_Part_Set_Items_Command(QT.QUndoCommand):
	def __init__(self, newParent, items, parent=None):
		super(Move_Part_Set_Items_Command, self).__init__("Move Part Set Items")
		self.items         =  [self.Item_Data(item, newParent) for item in items]
		self.newParent     =  newParent

	class Item_Data(object):
		def __init__(self, item, newParent):
			self.ref_item       =  item
			isinstance(self.ref_item, Part_Set_Reference_Item)
			
			self.item = self.ref_item._data
			self.input_newPartent = newParent
			self.input_oldParent  = self.ref_item.parent().parent().parent().parent()
			isinstance(self.item, Part_Set_Item)
			isinstance(self.input_newPartent, Assets_Item)
			
			old_parent = self.item.parent().parent()
			while old_parent.Parent.type() != Assets_Item.ITEM_TYPE:
				old_parent = old_parent.Parent
			
			self.old_Parent =  old_parent
			
			while newParent.Parent.type() != Assets_Item.ITEM_TYPE:
				newParent = newParent.Parent
			self.new_Parent =  newParent
			
			isinstance(self.new_Parent, Asset_Item)
			isinstance(self.old_Parent, Asset_Item)

		def assine_to_new_parent(self):
			if not self.new_Parent.data() == self.old_Parent.data():
				self.old_row    =  self.item.row()
				child = self.old_Parent.Part_Sets.takeChild(self.old_row)
				self.new_Parent.Part_Sets.appendRow(child)
				self.old_Parent.Part_Sets.removeRow(self.old_row)
				
			for ref in [ref for ref in self.old_Parent.find_child_items(self.item.data()) if ref.type() == Part_Set_Reference_Item.ITEM_TYPE]:
				isinstance(ref, Part_Set_Reference_Item)
				ref.parent().removeRow(ref.row())
				
			asset_item = self.input_newPartent
			while asset_item.type() != Assets_Item.ITEM_TYPE:
				for render_state in asset_item.Render_States.Children:
					isinstance(render_state, Render_State_Item)
					render_state.Unassined.appendRow(Part_Set_Reference_Item(self.item))
				asset_item = asset_item.Parent
				
			if _maya_check:
				self.new_Parent._data.addNode([self.item.node])
				
		def assine_to_old_parent(self):
			if not self.new_Parent.data() == self.old_Parent.data():
				old_row    =  self.item.row()
				child = self.new_Parent.Part_Sets.takeChild(old_row)
				self.old_Parent.Part_Sets.insertRow(self.old_row, child)
				self.new_Parent.Part_Sets.removeRow(old_row)
				
			for ref in [ref for ref in self.new_Parent.find_child_items(self.item.data()) if ref.type() == Part_Set_Reference_Item.ITEM_TYPE]:
				isinstance(ref, Part_Set_Reference_Item)
				ref.parent().removeRow(ref.row())
				
			asset_item = self.input_oldParent
			while asset_item.type() != Assets_Item.ITEM_TYPE:
				for render_state in asset_item.Render_States.Children:
					isinstance(render_state, Render_State_Item)
					render_state.Unassined.appendRow(Part_Set_Reference_Item(self.item))
				asset_item = asset_item.Parent
				
			if _maya_check:
				self.old_Parent._data.addNode([self.item.node])


	def undo(self):
		for item in reversed(self.items):
			item.assine_to_old_parent()

	def redo(self):
		for item in self.items:
			item.assine_to_new_parent()


########################################################################
class Add_Asset_Command(QT.QUndoCommand):
	def __init__(self, asset, name=None, parent=None):
		super(Add_Asset_Command, self).__init__("Add Asset")
		isinstance(asset, Asset_Item)
		self.asset = asset
		if name == None:
			num = self.asset.asset_item_count + 1
			name = "AW_Asset_%s" % str(num).zfill(4)
		self.data_obj  =  Named_Data_Object(name)
	#----------------------------------------------------------------------
	def update_current_render_states(self, new_part):
		""""""
		self.new_part_set_refs = []
		for render_state in self.model.Render_States.rowChildren():
			ref = Part_Set_Reference_Item(new_part)
			self.new_part_set_refs.append( ref )
			render_state.Unassined.appendRow( ref )

	def undo(self):
		if _maya_check:
			self.Asset._data.removeContainer()
			
		self.add_state_cmd.undo()
		row = self.Asset.row()
		self.Asset.Parent.removeRow(row)
	def redo(self):
		self.Asset = Asset_Item(asset=self.data_obj)
		self.asset.appendRow(self.Asset)
		if _maya_check:
			if self.asset.type() == Asset_Item.ITEM_TYPE:
				self.asset.node_addNode([self.Asset.node], includeNetwork=False, includeHierarchyBelow=False)
		self.add_state_cmd = Add_Render_State_Command(self.Asset, name="Empty")
		self.add_state_cmd.redo()
		
########################################################################
class Add_Part_Set_Command(QT.QUndoCommand):
	def __init__(self, single, asset, name=None, parent=None):
		super(Add_Part_Set_Command, self).__init__("Add Part Set")
		isinstance(asset,Asset_Item)
		self.single        = single
		self.asset         = asset
		self.part_sets     = asset.Part_Sets
		self.render_states = asset.Render_States
		if name == None:
			num = self.asset.part_sets_count + 1
			name = "Part_Set_%s" % str(num).zfill(4)
		self.name = name

	def undo(self):
		for ref in self.new_part_set_refs:
			ref.Parent.removeRow(ref.row())
			if _maya_check:
				self.PartSet._data.delete()
			row = self.PartSet.row()
			self.part_sets.removeRow(row)
			
	def redo(self):
		self.new_part_set_refs = []
		data                   = Named_Data_Object(self.name)
		self.PartSet           = Part_Set_Item(data)
		top_asset = self.asset
		while top_asset.Parent.type() != Assets_Item.ITEM_TYPE:
				top_asset = top_asset.Parent
		top_asset.Part_Sets.appendRow([self.PartSet])
		if _maya_check:
			self.asset.node_addNode([self.PartSet.node])

		for render_state in top_asset.Render_States.rowChildren():
			ref = Part_Set_Reference_Item(self.PartSet)
			self.new_part_set_refs.append( ref )
			render_state.Unassined.appendRow( ref )
			
		asset_scan = self.asset
		while asset_scan.Parent.type() != Assets_Item.ITEM_TYPE:
			for render_state in asset_scan.Render_States.rowChildren():
				ref = Part_Set_Reference_Item(self.PartSet)
				self.new_part_set_refs.append( ref )
				render_state.Unassined.appendRow( ref )
			asset_scan = asset_scan.parent()
		self.single.emit(self.PartSet)
		
########################################################################
class Remove_Part_Set_Command(QT.QUndoCommand):
	def __init__(self, view, parts, parent=None):
		super(Remove_Part_Set_Command, self).__init__("Add Part Set")
		asset = view.asset_tree_view.current_item()
		isinstance(asset, Asset_Item)
		isinstance(view,Asset_Tree_View)
		
		self.view      = view
		self.asset     = asset
		self.part_sets = asset.Part_Sets
		self.parts     = parts
		self.restore_data = []
		
	class Ref_State_Restore_Data(object):
		#----------------------------------------------------------------------
		def __init__(self, part_ref):
			isinstance(part_ref, Part_Set_Reference_Item)
			self.row           = part_ref.row()
			state_overide      = part_ref.get_Overide_assinment()
			self.state_overide_row = state_overide.row()
			self.state_overide_parent_row = state_overide.Parent.row()
			self.part_name     = part_ref.data()
			
		def restore(self, part):
			ref  = Part_Set_Reference_Item(part)
			try:
				state_overide = part.Parent.Parent.Render_States.child(self.state_overide_parent_row).child(self.state_overide_row)
				state_overide.insertRow(self.row, ref)
			except:
				pass
			return ref
	class Part_Set_Restore_Data(object):
		#----------------------------------------------------------------------
		def __init__(self, part_sets, part):
			""""""
			isinstance(part, Part_Set_Item)
			isinstance(part_sets, Part_Sets_Item)
			self.part_sets      = part_sets
			self.name           = part.data()
			self.row            = part_sets.row()
			self.ref_assinments = []
			if _maya_check:
				self.node_members   = part.node_members
				self.node_member_names =  part.node_memberNames
			
			for ref in  part.find_Part_Set_Refs_By_Name(self.name):
				storage = Remove_Part_Set_Command.Ref_State_Restore_Data(ref)
				self.ref_assinments.append(storage)
				
		def restore(self):
			if not _maya_check:
				data_object = Named_Data_Object(self.name)
			else:
				data_object = self.name
			part = Part_Set_Item(data_object)
			self.part_sets.insertRow(self.row, part)
			for ref in self.ref_assinments:
				ref.restore(part)
			
			if _maya_check:
				part.node_addElement(self.node_member_names)
			return part
			

	def undo(self):
		self.parts = []
		for item in  self.restore_data:
			part = item.restore()
			self.parts.append(part)
			if _maya_check:
				self.asset.node_addNode([part.node])				
			
	def generate_restore_data(self):
		restore_data = []
		for part in  self.parts:
			storage = self.Part_Set_Restore_Data(self.part_sets, part)
			restore_data.append(storage)
		return restore_data
	
	def redo(self):
		self.restore_data = self.generate_restore_data()
		for part in  self.parts:
			for ref in  self.asset.Render_States.find_child_items(part.data()):
				ref.get_Overide_assinment().removeRow(ref.row())
			if _maya_check:
				try:
					cmds.lockNode(part._data, lock=False)
					part._data.delete()
					row = part.row()
					self.part_sets.removeRow(row)
				except:
					cmds.warning("was Unable to Remove part Set")

########################################################################
class Add_Render_State_Command(QT.QUndoCommand):
	def __init__(self, asset, name=None, parent=None):
		super(Add_Render_State_Command, self).__init__("Add Remder State")
		isinstance(asset, Asset_Item)
		self.asset         = asset
		self.render_states = asset.Render_States
		self.part_sets     = asset.Part_Sets
		if name == None:
			num = self.asset.render_state_count + 1
			name = "render_state_%s" %  str(num).zfill(4)
		self.name=name

	def undo(self):
		self.render_states.removeRow(self.Render_State.row())

	def redo(self):
		self.Render_State = Render_State_Item(self.name)
		self.render_states.appendRow(self.Render_State)
		collected = []
		for child_ref in self.render_states.parent().Part_Sets.Children:
			if not child_ref.data() in collected:
				collected.append(child_ref.data())
				ref = Part_Set_Reference_Item(child_ref)
				self.Render_State.Unassined.appendRow( ref )

########################################################################
class Duplacate_Render_State_Command(QT.QUndoCommand):
	def __init__(self, render_state, parent=None):
		super(Duplacate_Render_State_Command, self).__init__("Add Remder State")
		isinstance(render_state, Render_State_Item)
		self.orig_render_state  = render_state

	def undo(self):
		self.cloned_render_state.parent().removeRow(self.cloned_render_state.row())
		
	def redo(self):
		self.cloned_render_state = Render_State_Item(self.orig_render_state.data()+"_Copy")
		self.orig_render_state.parent().appendRow(self.cloned_render_state)
		for clone_overide, orig_overide in zip(self.cloned_render_state.Children, self.orig_render_state.Children):
			for part in orig_overide.Children:
				ref = Part_Set_Reference_Item(part._data)
				clone_overide.appendRow(ref)

			
########################################################################
class Remove_Render_State_Command(QT.QUndoCommand):
	def __init__(self, view, states, parent=None):
		super(Remove_Render_State_Command, self).__init__("Remove Render State")
		asset                   = view.asset_tree_view.current_item()
		isinstance(view, Asset_Tree_View)
		isinstance(asset, Asset_Item)
		self.view               = view
		self.asset              = asset
		self.part_sets_item     = asset.Part_Sets
		self.part_sets_view     = view.part_sets_view
		self.render_states_item = asset.Render_States
		self.render_states_view = view.render_states_view
		self.states             = states
		self.restore_data = []
		
	class State_Restore_Data(object):
		#----------------------------------------------------------------------
		def __init__(self, view, item, asset):
			isinstance(view, Asset_Tree_View)
			isinstance(item, Render_State_Item)
			isinstance(asset, Asset_Item)
			
			self.row                = item.row()
			self.name               = item._data.name
			
			self.Unassined          = [ref._data for ref in item.Unassined.Children]
			self.Invisible          = [ref._data for ref in item.Invisible.Children]
			self.Beauty             = [ref._data for ref in item.Beauty.Children]
			self.Matte              = [ref._data for ref in item.Matte.Children]
			
			self.part_sets_item     = asset.Part_Sets
			self.part_sets_view     = view.part_sets_view
			
			self.render_states_item = asset.Render_States
			self.render_states_view = view.render_states_view

			
		def restore(self):
			render_state = Render_State_Item(self.name)
			self.render_states_item.insertRow(self.row, render_state)
			[render_state.Unassined.appendRow( Part_Set_Reference_Item( part ) ) for part in self.Unassined]
			[render_state.Invisible.appendRow( Part_Set_Reference_Item( part ) ) for part in self.Invisible]
			[render_state.Beauty.appendRow( Part_Set_Reference_Item( part ) ) for part in self.Beauty]
			[render_state.Matte.appendRow( Part_Set_Reference_Item( part ) ) for part in self.Matte]
			return render_state
	
	
	def undo(self):
		self.states = []
		for item in  self.restore_data:
			isinstance(item, self.State_Restore_Data)
			render_state = item.restore()
			self.states.append(render_state)
		if len(self.states):
			self.render_states_view.set_Current_Item(render_state)
		

	def redo(self):
		self.restore_data = []
		for state in self.states:
			isinstance(state, Render_State_Item)
			storage = self.State_Restore_Data(self.view, state, self.asset)
			self.restore_data.append(storage)
			
		for state in  self.states:
			row = state.row()
			[state.Unassined.removeRow(ref.row()) for ref in state.Unassined.Children]
			[state.Beauty.removeRow(ref.row()) for ref in state.Beauty.Children]
			[state.Invisible.removeRow(ref.row()) for ref in state.Invisible.Children]
			[state.Matte.removeRow(ref.row()) for ref in state.Matte.Children]
			self.render_states_item.removeRow(row)
		if len(self.render_states_item.Children):
			self.render_states_view.set_Current_Item(self.render_states_item.Children[0])
	
########################################################################
class Render_States_Restore_Data(object):
	########################################################################
	class Render_State_Restore_Data(object):
		#----------------------------------------------------------------------
		def __init__(self, item):
			isinstance(item, Render_State_Item)
			self.row                = item.row()
			self.name               = item.data()
			self.parent_row         = item.parent().row()
			
			self.Unassined_names = [ref.data() for ref in item.Unassined.Children]
			self.Invisible_names = [ref.data() for ref in item.Invisible.Children]
			self.Beauty_names    = [ref.data() for ref in item.Beauty.Children]
			self.Matte_names     = [ref.data() for ref in item.Matte.Children]
		
		def restore_Item(self,asset):
			isinstance(asset,Asset_Item)
			render_state  = Render_State_Item(self.name)
			#render_state.Unassined.setRowCount(len(self.Unassined_names))
			#render_state.Matte.setRowCount(len(self.Matte_names))
			#render_state.Invisible.setRowCount(len(self.Invisible_names))
			#render_state.Beauty.setRowCount(len(self.Beauty_names))
			
			asset.Render_States.setChild(self.row, render_state)
			return render_state
		
	#----------------------------------------------------------------------
	def __init__(self, asset):
		isinstance(asset, Asset_Item)
		self.rowCount     =  asset.Render_States.RowCount
		self.restore_data =  []
		for item in asset.Render_States.rowChildren():
			storage = self.Render_State_Restore_Data(item)
			self.restore_data.append(storage)
			
	def restore(self, asset):
		isinstance(asset, Asset_Item)
		asset.Render_States.setRowCount(self.rowCount)
		for item in self.restore_data:
			isinstance(item,Render_States_Restore_Data.Render_State_Restore_Data)
			item.restore_Item(asset)

########################################################################
class Part_Set_Ref_Restore_Data(object):
	#----------------------------------------------------------------------
	def __init__(self, asset, ref):
		""""""
		isinstance(asset, Asset_Item)
		isinstance(ref, Part_Set_Reference_Item)
		self.asset             = asset
		self.row               = ref.row()
		self.name              = ref.data()
		self.render_state_name = ref.parent().parent().data()
		self.overide_state_name= ref.get_Overide_assinment().data()
			
	def restore(self,asset):
		isinstance(asset,Asset_Item)
		self.asset    = asset
		part_set      = asset.Part_Sets.find_child_items(self.name, recurive=False)[0]
		render_state  = asset.Render_States.find_child_items(self.render_state_name, recurive=False)[0]
		overide_state = render_state.find_child_items(self.overide_state_name, recurive=False)[0]
		ref           = Part_Set_Reference_Item(part_set)
		overide_state.setChild(self.row, ref)

########################################################################
class Part_Set_Restore_Data(object):
	#----------------------------------------------------------------------
	def __init__(self, part):
		""""""
		isinstance(part, Part_Set_Item)
		self.name    = part.data()
		self.row     = part.row()
		self.parent_row = part.parent().row()
		if _maya_check:
			self.node_names = part.node_memberNames
			part.node_delete()
		
	def restore(self, asset, part_sets):
		isinstance(part_sets,Part_Sets_Item)
		isinstance(asset,Asset_Item)
		
		part = Part_Set_Item(self.name)
		part_sets.setChild(self.row, part)
		if _maya_check:
			part.node_include_items(self.node_names)
			asset.node_addNode([part.node], includeNetwork=False, includeHierarchyBelow=False)
			asset.node_addNode(self.node_names)
########################################################################
class Part_Sets_Restore_Data(object):
	#----------------------------------------------------------------------
	def __init__(self, asset):
		""""""
		isinstance(asset, Asset_Item)
		self.asset          = asset
		self.rowCout        = asset.Part_Sets.rowCount()
		self.restore_data   = []
		for item in asset.Part_Sets.rowChildren():
			storage = Part_Set_Restore_Data(item)
			self.restore_data.append(storage)
			
	def restore(self,asset):
		isinstance(asset,Asset_Item)
		asset.Part_Sets.setRowCount(self.rowCout)
		for item in self.restore_data:
			item.restore(asset, asset.Part_Sets)
			
########################################################################
class Asset_Restore_Data(object):
	#----------------------------------------------------------------------
	def __init__(self, view, asset):
		isinstance(view, Asset_Tree_View)
		isinstance(asset, Asset_Item)
		if _maya_check:
			self.node_names = [node.name for node in asset.node_nodeList]
			
		self.view               = view
		self.part_sets_view     = view.part_sets_view
		self.render_states_view = view.render_states_view
		self.name               = asset.data()
		self.row                = asset.row()
		self.rowCount           = asset.rowCount()
		self.render_states_data = Render_States_Restore_Data(asset)
		self.part_sets_data     = Part_Sets_Restore_Data(asset)
		self.restore_data       = []
		self.part_refs_data     = []
		
		for ref in asset.Render_States.find_child_item_types(Part_Set_Reference_Item.ITEM_TYPE):
			storage = Part_Set_Ref_Restore_Data(asset, ref)
			self.part_refs_data.append(storage)
			
		if self.rowCount > 2:
			for item in [child for child in asset.rowChildren() if isinstance(child, Asset_Item)]:
				storage = Asset_Restore_Data(view, item)
				self.restore_data.append(storage)
		# if _maya_check:
			# asset.node_removeContainer()
				
	
	def restore(self, parent_asset):
		isinstance(parent_asset, Asset_Item)
		asset = Asset_Item(self.name)
		parent_asset.insertRow(self.row, asset)
		if _maya_check:
			if parent_asset.ITEM_TYPE == Asset_Item.ITEM_TYPE:
				parent_asset.node_addNode([asset.node])
		
		self.part_sets_data.restore(asset)
		self.render_states_data.restore(asset)
		
		for item in self.restore_data:
			item.restore(asset)
		for ref in  self.part_refs_data:
			ref.restore(asset)
		return asset
	
########################################################################
class Remove_Asset_Command(QT.QUndoCommand):
	def __init__(self, view, asset=""):
		super(Remove_Asset_Command, self).__init__("Remove Assets")
		if not isinstance(asset, str):
			asset = view.current_item()
		isinstance(view, Asset_Tree_View)
		isinstance(asset, Asset_Item)
		self.asset              = asset
		self.parent_asset       = asset.parent()
		self.view               = view
		self.part_sets_view     = view.part_sets_view
		self.render_states_view = view.render_states_view
		self.row                = asset.row()
		self.rowCount           = asset.rowCount()
		self.parentRow          = asset.parent().row()
		
	
	def undo(self):
		self.asset = self.asset_restore_data.restore(self.parent_asset)
	
	def redo(self):
		self.asset_restore_data = Asset_Restore_Data(self.view,self.asset)
		if not self.asset.Parent.ITEM_TYPE == self.view.root_Item().ITEM_TYPE:
			self.view.set_Current_Item(self.asset.Parent)
		elif self.asset.row() != 0:
			self.view.set_Current_Item(self.asset.Parent.rowChildren()[0])
		
		self.asset.Render_States.clear_Children()
		self.asset.Part_Sets.clear_Children()	
		self.asset.parent().removeRow(self.row)
			
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Input Widgets
##======================================================================
########################################################################
class Asset_States_ComboBox(QComboBox):
	def __init__(self, asset, parent=None):
		isinstance(asset, Asset_Item)
		super(Asset_States_ComboBox, self).__init__(parent=parent)
		self.setModel(asset.Model)
		self.setRootModelIndex(asset.Render_States.index())
		self.setEditable(True)
		self._asset = asset
		self._maya_forced = False
		self.setCurrentIndex(0)
		self.currentIndexChanged.connect(self.update_asset_attribute)
		items =  [child.data() for child in asset.Render_States.Children]
		self._c = QT.QCompleter(items, self)
		self._c.setCaseSensitivity(Qt.CaseInsensitive)
		self.setCompleter(self._c)

	def update_asset_attribute(self):
		current_render_layer = cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True )
		current_index        = self.currentIndex()
		current_plug_index   = self._asset.enum_render_states_plug.value
		if not current_render_layer == "defaultRenderLayer":
			self._asset.enum_render_states_plug.value = self.currentIndex()
			if not self._maya_forced or not current_index == current_plug_index:
				self._asset.set_Render_States_Plug_Overide()
				actived_state = self._asset.Render_States.child(self.currentIndex())
				isinstance(actived_state, Render_State_Item)
				actived_state.apply_Vray_Overide_States()
			else:
				self._maya_forced = False
		else:
			self.setCurrentIndex(0)
			self._asset.enum_render_states_plug.value = 0
			for layer in Scripts.Global_Constants.Nodes.Display_Layers():
				layer.visibility.value = 1
	def update_On_Render_Layer_Change(self):
		self._maya_forced = True
		if not cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) == "defaultRenderLayer":
			self.setCurrentIndex(self._asset.enum_render_states_plug.value)
		else:
			self.setCurrentIndex(0)
	
##======================================================================
########################################################################
class Asset_States_ListView(QListView):
	def __init__(self, asset, parent=None):
		isinstance(asset, Asset_Item)
		super(Asset_States_ListView, self).__init__(parent=parent)
		self.setModel(asset.Model)
		self.setRootIndex(asset.Render_States.index())
		self._asset = asset
		self._maya_forced = False
		self.doubleClicked.connect(self.update_asset_attribute)
		self.setEditTriggers(self.NoEditTriggers)

	def update_asset_attribute(self):
		current_render_layer = get_Current_Render_Layer()
		current_index        = self.currentIndex()
		current_plug_index   = self._asset.enum_render_states_plug.value
		if not current_render_layer == "defaultRenderLayer":
			self._asset.enum_render_states_plug.value = current_index.row()
			if not self._maya_forced or not current_index.row() == current_plug_index:
				self._asset.set_Render_States_Plug_Overide()
				actived_state = self._asset.Render_States.child(current_index.row())
				isinstance(actived_state, Render_State_Item)
				actived_state.apply_Vray_Overide_States()
			else:
				self._maya_forced = False
		else:
			self.setCurrentIndex(self._asset.Render_States.child(0).index())
			self._asset.enum_render_states_plug.value = 0
			for layer in Scripts.Global_Constants.Nodes.Display_Layers():
				layer.visibility.value = 1
	def update_On_Render_Layer_Change(self):
		self._maya_forced = True
		if not get_Current_Render_Layer() == "defaultRenderLayer":
			self.setCurrentIndex(self._asset.Render_States.child(self._asset.enum_render_states_plug.value).index())
		else:
			self.model().itemFromIndex(self.rootIndex()).child(0).index()
			self.setCurrentIndex(self.model().itemFromIndex(self.rootIndex()).child(0).index())
			
########################################################################
class Asset_States_GroupBox(QT.QGroupBox):
	def __init__(self, asset, parent=None):
		isinstance(asset, Asset_Item)
		super(Asset_States_GroupBox, self).__init__(parent=parent)
		self.verticalLayout = QT.QVBoxLayout(self)
		self.asset_states   = Asset_States_ListView(asset, self)
		
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setTitle(asset.Parent.data())
		self.verticalLayout.addWidget(self.asset_states)
		
########################################################################
class Asset_Frame(QT.QFrame):
	def __init__(self, asset, parent=None):
		isinstance(asset, Asset_Item)
		super(Asset_Frame, self).__init__(parent=parent)
		self.setFrameShape(QT.QFrame.Box)
		self.setFrameShadow(QT.QFrame.Plain)
		
		self.verticalLayout = QT.QVBoxLayout(self)
		self.asset_name     = QT.QLabel(self)
		self.asset_states   = Asset_States_ComboBox(asset, self)
		
		self.asset_name.setAlignment(QtCore.Qt.AlignCenter)
		self.asset_name.setText(asset.Parent.data())
		
		self.verticalLayout.addWidget(self.asset_name)
		self.verticalLayout.addWidget(self.asset_states)
		
########################################################################
class Asset_Grid(QT.QWidget):
	def __init__(self, parent=None):
		super(Asset_Grid, self).__init__(parent=parent)
		
		self.gridLayout  = QT.QGridLayout(self)
		self.items = []
		self.asset_row = 0
		self.asset_column = 0
		
	def add_asset_item(self, asset):
		if self.window()._use_Beta:
			frame = Asset_States_GroupBox(asset, self)
		else:
			frame = Asset_Frame(asset, self)
		
		self.window().ACTIVE_RENDER_LAYER_CHANGED.connect(frame.asset_states.update_On_Render_Layer_Change)
		self.gridLayout.addWidget(frame, self.asset_row, self.asset_column, 1, 1)
		self.items.append(frame)
		self.asset_column += 1
		if self.asset_column == 3:
			self.asset_column = 0
			self.asset_row += 1

	@QtSlot(QT.QStandardItem)
	def build_Master_Assets_Grid(self, root_item):
		if isinstance(root_item, QT.QStandardItem):
			if len(self.items):
				for item in  self.items:
					self.gridLayout.removeWidget(item)
					del item
					self.items =  []
					self.asset_row = 0
					self.asset_column = 0
			if root_item.rowCount():
				for i in range(root_item.rowCount()):
					file_ref_item = root_item.child(i)
					isinstance(file_ref_item, File_Reference_Item)
					for asset in file_ref_item.Children:
						isinstance(asset, Assets_Item)
						if len(asset.Render_States.Children):
							self.add_asset_item(asset)
		
	@QtSlot(QT.QStandardItem)
	def rebuild_grid(self, file_refence_item):
		if isinstance(file_refence_item, File_Reference_Item):
			if len(self.items):
				for item in  self.items:
					self.gridLayout.removeWidget(item)
					del item
					self.items =  []
					self.asset_row = 0
					self.asset_column = 0
			childern = file_refence_item.find_child_item_types(Asset_Item.ITEM_TYPE)
			if len(childern):
				for asset in childern:
					isinstance(asset, Asset_Item)
					if len(asset.Render_States.Children):
						self.add_asset_item(asset)

########################################################################
class ComboBox(QComboBox):
	def __init__(self,*args,**kwargs):
		super(ComboBox,self).__init__(*args,**kwargs)
		self._last_active_index = 0
		self.currentIndexChanged.connect(self.add_CurrentIndex_Changed_Undo)
	
	@QtSlot()
	def add_CurrentIndex_Changed_Undo(self):
		undo_stack = self.window().undo_stack
		if self._last_active_index != self.currentIndex():
			cmd = Active_Asset_Change_Command(self, self._last_active_index,self.currentIndex())
			self.window().undo_stack.push(cmd)
			self._last_active_index = self.currentIndex()
########################################################################
class GroupBox(QT.QGroupBox):
	def __init__(self,*args,**kwargs):
		super(GroupBox,self).__init__(*args,**kwargs)
		
########################################################################
class Active_Refence_ComboBox(QComboBox):
	CURRENT_REFERENCE_CHANGED =  QtSignal(QT.QStandardItem)
	def __init__(self,*args,**kwargs):
		super(Active_Refence_ComboBox,self).__init__(*args,**kwargs)
		self.currentIndexChanged.connect(self.current_reference_changed)
		
	
	@QtSlot(int)
	def current_reference_changed(self, index):
		item = self.model().item(index, 0)
		if not item is None:
			self.CURRENT_REFERENCE_CHANGED.emit(item)
	
########################################################################
class Asset_Line_Edit(QT.QLineEdit):
	def __init__(self,*args,**kwargs):
		super(Asset_Line_Edit,self).__init__(*args,**kwargs)
		
########################################################################
class Yaml_Output_Display(QT.QTextEdit):
	def __init__(self,*args,**kwargs):
		super(Yaml_Output_Display,self).__init__(*args,**kwargs)
		
########################################################################
class Active_Asset_ComboBox(ComboBox):
	def __init__(self,*args,**kwargs):
		super(Active_Asset_ComboBox,self).__init__(*args,**kwargs)
		self.editTextChanged.connect(self.editing_Finished)
		
	def editing_Finished(self):
		line = self.lineEdit()
		text = line.text()
		print text
		
	def setItemText(self,index, value):
		super(Active_Asset_ComboBox,self).setItemText(index, value)
		
	def showPopup(self):
		res = super(Active_Asset_ComboBox,self).showPopup()
		return res
	
	def hidePopup(self):
		return super(Active_Asset_ComboBox,self).hidePopup()
########################################################################
class ToolButton(QT.QToolButton):
	""""""
	def __init__(self,*args,**kwargs):
		super(ToolButton,self).__init__(*args,**kwargs)
		self.setMenu(QT.QMenu("Display Apperence"))
		self.make_menu()
		self.triggered.connect(self.set_display)
		
	def set_display(self, action):
		editor = self.window().Model_Editor
		isinstance(editor, Maya_Modle_Editor)
		editor.editor_set_displayAppearance(action.text())
			
	def make_menu(self):
		for val in  ["wireframe", "points", "boundingBox", "smoothShaded", "flatShaded"]:
			action = QT.QAction(self)
			action.setText(val)
			self.menu().addAction(action)
		
########################################################################
class Camera_List_ToolButton(QT.QToolButton):
	""""""
	def __init__(self,*args,**kwargs):
		super(Camera_List_ToolButton,self).__init__(*args,**kwargs)
		self.setMenu(QT.QMenu("Set Active Camera", self))
		if _maya_check:
			self.make_menu()
			self.triggered.connect(self.set_cam)
			
	def mousePressEvent(self, event):
		self.make_menu()
		super(Camera_List_ToolButton,self).mousePressEvent(event)
		
	def set_cam(self, action):
		cam, name = action.data()
		if cmds.objExists(name):
			editor = self.window().Model_Editor.editor_set_camera(name)
		else:
			self.menu().removeAction(action)
			action.setParent(None)
			
	def make_menu(self):
		menu   = self.menu()
		children = self.findChildren(QT.QAction)
		if isinstance(children, list):
			for child in children:
				data = child.data()
				if isinstance(data, list):
					cam, name = data[0], data[1]
					if not cmds.objExists(name):
						self.menu().removeAction(child)
						child.setParent(None)
		
		for cam in Scripts.NodeCls.M_Nodes.strings_to_MNODES(cmds.ls(type="camera")):
			cam_parent = cam.get_parent()
			action_name = "action_" + cam_parent.nice_name
			if not self.findChild(QT.QAction, action_name):
				action = QT.QAction(self)
				action.setObjectName(action_name)
				action.setData([cam, cam.nice_name])
				action.setText(cam_parent.nice_name)
				menu.addAction(action)
		
    
	

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Maya Widgets
########################################################################
class Maya_Modle_Editor(QT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Maya_Modle_Editor, self).__init__(*args, **kwargs)
		self.m_editor =  None
	#----------------------------------------------------------------------
	@QtSlot(QT.QMainWindow)
	def _run_setup(self, main_window):
		""""""
		isinstance(main_window, QT.QMainWindow)
		self.main_window            = main_window
		self.beauty_overide_view    = main_window.beauty_overide_view
		self.matte_overide_view     = main_window.matte_overide_view
		self.invisible_overide_view = main_window.invisible_overide_view
		self.part_sets_view         = main_window.part_sets_view
		self.render_states_view     = main_window.render_states_view
		self.asset_tree_view        = main_window.asset_tree_view
		self.entity_tree_view       = main_window.entity_tree_view
		layout = self.layout()
		
		if _maya_check:
			if self.window()._Enable_Model_Editor:
				window        = M_Windows.Window()
				panelayout    = Scripts.UICls.Layouts.PaneLayout()
				self.m_editor = M_Panels.ModelEditor("MyModelEditor")
				self.m_editor._widget.setParent(self)
				layout.addWidget(self.m_editor._widget)
				
				cmds.showWindow( window )
				cmds.deleteUI(window,window=True)
				
				self.Main_Conn               = M_Nodes.SelectionConnection(self.m_editor.name+"_Main_Connection"       , parent=self.m_editor)
				self.Highlight_Sel_Conn      = M_Nodes.SelectionConnection(self.m_editor.name+"_Highlight_Connection"  , parent=self.m_editor)
				self.Selection_Sel_Conn      = M_Nodes.SelectionConnection(self.m_editor.name+"_Selection_Connection"  , parent=self.m_editor)
				cmds.isolateSelect(self.m_editor,state=1)
				self.Main_Conn.connect_to_editor_MainList(self.m_editor)
				#self.Selection_Sel_Conn.connect_to_editor_Selection(self.maya_model_editor)
				#self.Highlight_Sel_Conn.connect_to_editor_Highlight(self.maya_model_editor)
	
	#----------------------------------------------------------------------
	def destroy(self):
		super(Maya_Modle_Editor, self).destroy()
	#----------------------------------------------------------------------
	@QtSlot(list)
	def add_Objects_To_Main_Connection(self, objs):
		self.Main_Conn.add_objects(objs)
		self.do_Auto_Frame()
	#----------------------------------------------------------------------
	@QtSlot(list)
	def remove_Objects_From_Main_Connection(self, objs):
		self.Main_Conn.remove_objects(objs)
	#----------------------------------------------------------------------
	@QtSlot(bool)
	def editor_ActiveOnly(self, value):
		self.m_editor.activeOnly = value
	#----------------------------------------------------------------------
	@QtSlot(str)
	def editor_displayAppearance(self, value):
		if value in  ["wireframe", "points", "boundingBox", "smoothShaded", "flatShaded"]:
			self.m_editor.displayAppearance = value
		
	@QtSlot()
	#----------------------------------------------------------------------
	def Viewfit_Frame_All(self):
		""""""
		cmds.viewFit(self.m_editor.camera, panel=self.m_editor, all=True, animate=1)
	@QtSlot()
	#----------------------------------------------------------------------
	def Viewfit_Frame_Selected(self):
		""""""
		cmds.viewFit(self.m_editor.camera, animate=1)
		
	@QtSlot()
	#----------------------------------------------------------------------
	def do_Auto_Frame(self):
		""""""
		if self.auto_frame_value:
			self.Viewfit_Frame_All()
		
	#----------------------------------------------------------------------
	def get_Auto_Frame_Value(self):
		return self.property("Auto_Frame_Value")
	@QtSlot(bool)
	#----------------------------------------------------------------------
	def set_Auto_Frame_Value(self, value):
		self.setProperty("Auto_Frame_Value", value)
	auto_frame_value = property(get_Auto_Frame_Value, set_Auto_Frame_Value)
	#----------------------------------------------------------------------
	def showEvent(self, event):
		super(Maya_Modle_Editor, self).showEvent(event)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_mainListConnection(self):
		""""""
		return self.m_editor.get_mainListConnection()
	
	def editor_set_mainListConnection(self, value):
		""""""
		self.m_editor.set_mainListConnection(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_forceMainConnection(self):
		""""""
		return self.m_editor.get_forceMainConnection()
	
	def editor_set_forceMainConnection(self, value):
		""""""
		self.m_editor.set_forceMainConnection(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_selectionConnection(self):
		""""""
		return self.m_editor.get_selectionConnection()
	
	def editor_set_selectionConnection(self, value):
		""""""
		self.m_editor.set_selectionConnection(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_highlightConnection(self):
		""""""
		return self.m_editor.get_highlightConnection()
	
	def editor_set_highlightConnection(self, value):
		""""""
		self.m_editor.set_highlightConnection(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_filter(self):
		""""""
		return self.m_editor.get_filter()
	
	def editor_set_filter(self, value):
		""""""
		self.m_editor.set_filter(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def lockMainConnection(self,value):
		""""""
		self.m_editor.lockMainConnection(value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.m_editor.stateString()
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.m_editor.set_unlockMainConnection(value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.m_editor.set_updateMainConnection(value)
	#----------------------------------------------------------------------
	def editor_get_docTag(self):
		""""""
		return self.m_editor.get_docTag()
	
	def editor_set_docTag(self, value):
		""""""
		self.m_editor.set_docTag(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_camera(self):
		""""""
		return self.m_editor.get_camera()
	
	def editor_set_camera(self, value):
		""""""
		self.m_editor.set_camera(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_cameraName(self,value):
		""""""
		self.m_editor.set_cameraName(value)
	#----------------------------------------------------------------------
	def editor_get_displayLights(self):
		""""""
		return self.m_editor.get_displayLights()
	
	def editor_set_displayLights(self, value):
		""""""
		self.m_editor.set_displayLights(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_bufferMode(self):
		""""""
		return self.m_editor.get_bufferMode()
	
	def editor_set_bufferMode(self, value):
		""""""
		self.m_editor.set_bufferMode(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_activeOnly(self):
		""""""
		return self.m_editor.get_activeOnly()
	
	def editor_set_activeOnly(self, value):
		""""""
		self.m_editor.set_activeOnly(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_interactive(self):
		""""""
		return self.m_editor.get_interactive()
	#----------------------------------------------------------------------
	def editor_set_interactive(self, value):
		""""""
		self.m_editor.set_interactive(value)
	#----------------------------------------------------------------------
	def editor_get_default(self):
		""""""
		return self.m_editor.get_default()
	
	def editor_set_default(self, value):
		""""""
		self.m_editor.set_default(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_ignorePanZoom(self):
		""""""
		return self.m_editor.get_ignorePanZoom()
	@QtSlot(bool)
	def editor_set_ignorePanZoom(self, value):
		""""""
		self.m_editor.set_ignorePanZoom(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_twoSidedLighting(self):
		""""""
		return self.m_editor.get_twoSidedLighting()
	@QtSlot(bool)
	def editor_set_twoSidedLighting(self, value):
		""""""
		self.m_editor.set_twoSidedLighting(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_displayAppearance(self):
		""""""
		return self.m_editor.get_displayAppearance()
	@QtSlot(str)
	def editor_set_displayAppearance(self, value):
		""""""
		if value in  ["wireframe", "points", "boundingBox", "smoothShaded", "flatShaded"]:
			self.m_editor.displayAppearance = value
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_wireframeOnShaded(self):
		""""""
		return self.m_editor.get_wireframeOnShaded()
	@QtSlot(bool)
	def editor_set_wireframeOnShaded(self, value):
		""""""
		self.m_editor.set_wireframeOnShaded(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_headsUpDisplay(self):
		""""""
		return self.m_editor.get_headsUpDisplay()
	@QtSlot(bool)
	def editor_set_headsUpDisplay(self, value):
		""""""
		self.m_editor.set_headsUpDisplay(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_selectionHiliteDisplay(self):
		""""""
		return self.m_editor.get_selectionHiliteDisplay()
	@QtSlot(bool)
	def editor_set_selectionHiliteDisplay(self, value):
		""""""
		self.m_editor.set_selectionHiliteDisplay(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_useDefaultMaterial(self):
		""""""
		return self.m_editor.get_useDefaultMaterial()
	@QtSlot(bool)
	def editor_set_useDefaultMaterial(self, value):
		""""""
		self.m_editor.set_useDefaultMaterial(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_useColorIndex(self):
		""""""
		return self.m_editor.get_useColorIndex()
	
	def editor_set_useColorIndex(self, value):
		""""""
		self.m_editor.set_useColorIndex(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_userNode(self):
		""""""
		return self.m_editor.get_userNode()
	
	def editor_set_userNode(self, value):
		""""""
		self.m_editor.set_userNode(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_wireframeBackingStore(self):
		""""""
		return self.m_editor.get_wireframeBackingStore()
	@QtSlot(bool)
	def editor_set_wireframeBackingStore(self, value):
		""""""
		self.m_editor.set_wireframeBackingStore(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_useRGBImagePlane(self):
		""""""
		return self.m_editor.get_useRGBImagePlane()
	
	def editor_set_useRGBImagePlane(self, value):
		""""""
		self.m_editor.set_useRGBImagePlane(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_imagePlane(self):
		""""""
		return self.m_editor.get_imagePlane()
	@QtSlot(bool)
	def editor_set_imagePlane(self, value):
		""""""
		self.m_editor.set_imagePlane(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_updateColorMode(self,value):
		""""""
		self.m_editor.updateColorMode(value)
	#----------------------------------------------------------------------
	@property
	def editor_colorMap(self):
		""""""
		return self.m_editor.colorMap()
	#----------------------------------------------------------------------
	def editor_get_backfaceCulling(self):
		""""""
		return self.m_editor.get_backfaceCulling()
	@QtSlot(bool)
	def editor_set_backfaceCulling(self, value):
		""""""
		self.m_editor.set_backfaceCulling(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_xray(self):
		""""""
		return self.m_editor.get_xray()
	@QtSlot(bool)
	def editor_set_xray(self, value):
		""""""
		self.m_editor.set_xray(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_jointXray(self):
		""""""
		return self.m_editor.get_jointXray()
	@QtSlot(bool)
	def editor_set_jointXray(self, value):
		""""""
		self.m_editor.set_jointXray(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_activeComponentsXray(self):
		""""""
		return self.m_editor.get_activeComponentsXray()
	@QtSlot(bool)
	def editor_set_activeComponentsXray(self, value):
		""""""
		self.m_editor.set_activeComponentsXray(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_maxConstantTransparency(self):
		""""""
		return self.m_editor.get_maxConstantTransparency()
	
	def editor_set_maxConstantTransparency(self, value):
		""""""
		self.m_editor.set_maxConstantTransparency()
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_displayTextures(self):
		""""""
		return self.m_editor.get_displayTextures()
	@QtSlot(bool)
	def editor_set_displayTextures(self, value):
		""""""
		self.m_editor.set_displayTextures(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_smoothWireframe(self):
		""""""
		return self.m_editor.get_smoothWireframe()
	@QtSlot(bool)
	def editor_set_smoothWireframe(self, value):
		""""""
		self.m_editor.set_smoothWireframe(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_lineWidth(self):
		""""""
		return self.m_editor.get_lineWidth()
	@QtSlot(float)
	def editor_set_lineWidth(self, value):
		""""""
		self.m_editor.set_lineWidth(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_textureMaxSize(self):
		""""""
		return self.m_editor.get_textureMaxSize()
	@QtSlot(int)
	def editor_set_textureMaxSize(self, value):
		""""""
		if value % 2 == 0:
			self.m_editor.set_textureMaxSize(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	@property
	def editor_textureMemoryUsed(self):
		""""""
		return self.m_editor.get_(textureMemoryUsed=True)
	#----------------------------------------------------------------------
	def editor_get_textureAnisotropic(self):
		""""""
		return self.m_editor.get_textureAnisotropic()
	@QtSlot(bool)
	def editor_set_textureAnisotropic(self, value):
		""""""
		self.m_editor.set_textureAnisotropic(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_textureSampling(self):
		""""""
		return self.m_editor.get_textureSampling()
	@QtSlot(int)
	@QtSlot(str)
	def editor_set_textureSampling(self, value):
		"""point sample = 1 : bilinear interpolation = 2"""
		if value in ["point", "bilinear interpolation"]:
			value = ["point", "bilinear interpolation"].index(value)
		if value in [0, 1]:
			self.m_editor.set_textureSampling(value+1)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_textureDisplay(self):
		""""""
		return self.m_editor.get_textureDisplay()
	@QtSlot(str)
	def editor_set_textureDisplay(self, value):
		""""""
		if value in  [ "modulate","decal"]:
			self.m_editor.set_textureDisplay(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_textureHilight(self):
		""""""
		return self.m_editor.get_textureHilight()
	@QtSlot(bool)
	def editor_set_textureHilight(self, value):
		""""""
		self.m_editor.set_textureHilight(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogging(self):
		""""""
		return self.m_editor.get_fogging()
	@QtSlot(bool)
	def editor_set_fogging(self, value):
		""""""
		self.m_editor.set_fogging(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogSource(self):
		""""""
		return self.m_editor.get_fogSource()
	@QtSlot(str)
	def editor_set_fogSource(self, value):
		""""""
		if value in p["fragment", "coordinate"]:
			self.m_editor.set_fogSource(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogMode(self):
		""""""
		return self.m_editor.get_fogMode()
	@QtSlot(str)
	def editor_set_fogMode(self, value):
		""""""
		if value in p["linear", "exponent", "exponent2"]:
			self.m_editor.set_fogMode(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogDensity(self):
		""""""
		return self.m_editor.get_fogDensity()
	@QtSlot(float)
	def editor_set_fogDensity(self, value):
		""""""
		self.m_editor.set_fogDensity(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogEnd(self):
		""""""
		return self.m_editor.get_fogEnd()
	@QtSlot(float)
	def editor_set_fogEnd(self, value):
		""""""
		self.m_editor.set_fogEnd(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogStart(self):
		""""""
		return self.m_editor.get_fogStart()
	@QtSlot(float)
	def editor_set_fogStart(self, value):
		""""""
		self.m_editor.set_fogStart(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fogColor(self):
		""""""
		return self.m_editor.get_fogColor()
	@QtSlot(list)
	def editor_set_fogColor(self, value):
		""""""
		self.m_editor.set_fogColor(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_shadows(self):
		""""""
		return self.m_editor.get_shadows()
	@QtSlot(bool)
	def editor_set_shadows(self, value):
		""""""
		self.m_editor.set_shadows(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_rendererName(self):
		""""""
		return self.m_editor.get_rendererName()
	
	def editor_set_rendererName(self, value):
		""""""
		self.m_editor.set_rendererName(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	@property
	def editor_rendererDeviceName(self):
		""""""
		return self.m_editor.rendererDeviceName()
	#----------------------------------------------------------------------
	@property
	def editor_rendererList(self):
		""""""
		return self.m_editor.rendererList()
	#----------------------------------------------------------------------
	@property
	def editor_rendererListUI(self):
		""""""
		return self.m_editor.rendererListUI()
	#----------------------------------------------------------------------
	def editor_get_rendererOverrideName(self):
		""""""
		return self.m_editor.get_rendererOverrideName()
	#----------------------------------------------------------------------
	def editor_set_rendererOverrideName(self, value):
		""""""
		self.m_editor.set_rendererOverrideName(value)
	#----------------------------------------------------------------------
	rendererOverrideName = property(editor_get_rendererOverrideName, editor_set_rendererOverrideName)
	#----------------------------------------------------------------------
	@property
	def editor_rendererOverrideList(self):
		""""""
		return self.m_editor.rendererOverrideList()
	#----------------------------------------------------------------------
	@property
	def editor_rendererOverrideListUI(self):
		""""""
		return self.m_editor.rendererOverrideListUI()
	#----------------------------------------------------------------------
	def editor_get_colorResolution(self):
		""""""
		return self.m_editor.get_colorResolution()
	#----------------------------------------------------------------------
	def editor_set_colorResolution(self, value):
		""""""
		self.m_editor.set_colorResolution(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_bumpResolution(self):
		""""""
		return self.m_editor.get_bumpResolution()
	
	def editor_set_bumpResolution(self, value):
		""""""
		self.m_editor.set_bumpResolution(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_transparencyAlgorithm(self):
		""""""
		return self.m_editor.get_transparencyAlgorithm()
	
	@QtSlot(str)
	def editor_set_transparencyAlgorithm(self, value):
		""""""
		if value in  ["frontAndBackCull", "perPolygonSort"]:
			self.m_editor.set_transparencyAlgorithm(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_transpInShadows(self):
		""""""
		return self.m_editor.get_transpInShadows()
	
	def editor_set_transpInShadows(self, value):
		""""""
		self.m_editor.set_transpInShadows(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_cullingOverride(self):
		""""""
		return self.m_editor.get_cullingOverride()
	
	def editor_set_cullingOverride(self, value):
		""""""
		self.m_editor.set_cullingOverride(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_lowQualityLighting(self):
		""""""
		return self.m_editor.get_lowQualityLighting()
	@QtSlot(bool)
	def editor_set_lowQualityLighting(self, value):
		""""""
		self.m_editor.set_lowQualityLighting(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_occlusionCulling(self):
		""""""
		return self.m_editor.get_occlusionCulling()
	@QtSlot(bool)
	def editor_set_occlusionCulling(self, value):
		""""""
		self.m_editor.set_occlusionCulling(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_useBaseRenderer(self):
		""""""
		return self.m_editor.get_useBaseRenderer()
	
	def editor_set_useBaseRenderer(self, value):
		""""""
		self.m_editor.set_useBaseRenderer(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_nurbsCurves(self):
		""""""
		return self.m_editor.get_nurbsCurves()
	@QtSlot(bool)
	def editor_set_nurbsCurves(self, value):
		""""""
		self.m_editor.set_nurbsCurves(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_nurbsSurfaces(self):
		""""""
		return self.m_editor.get_nurbsSurfaces()
	@QtSlot(bool)
	def editor_set_nurbsSurfaces(self, value):
		""""""
		self.m_editor.set_nurbsSurfaces(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_polymeshes(self):
		""""""
		return self.m_editor.get_polymeshes()
	@QtSlot(bool)
	def editor_set_polymeshes(self, value):
		""""""
		self.m_editor.set_polymeshes(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_subdivSurfaces(self):
		""""""
		return self.m_editor.get_subdivSurfaces()
	@QtSlot(bool)
	def editor_set_subdivSurfaces(self, value):
		""""""
		self.m_editor.set_subdivSurfaces(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_planes(self):
		""""""
		return self.m_editor.get_planes()
	@QtSlot(bool)
	def editor_set_planes(self, value):
		""""""
		self.m_editor.set_planes(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_lights(self):
		""""""
		return self.m_editor.get_lights()
	@QtSlot(bool)
	def editor_set_lights(self, value):
		""""""
		self.m_editor.set_lights(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_cameras(self):
		""""""
		return self.m_editor.get_cameras()
	@QtSlot(bool)
	def editor_set_cameras(self, value):
		""""""
		self.m_editor.set_cameras(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_controlVertices(self):
		""""""
		return self.m_editor.get_controlVertices()
	@QtSlot(bool)
	def editor_set_controlVertices(self, value):
		""""""
		self.m_editor.set_controlVertices(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_grid(self):
		""""""
		return self.m_editor.get_grid()
	@QtSlot(bool)
	def editor_set_grid(self, value):
		""""""
		self.m_editor.set_grid(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_hulls(self):
		""""""
		return self.m_editor.get_hulls()
	@QtSlot(bool)
	def editor_set_hulls(self, value):
		""""""
		self.m_editor.set_hulls(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_joints(self):
		""""""
		return self.m_editor.get_joints()
	@QtSlot(bool)
	def editor_set_joints(self, value):
		""""""
		self.m_editor.set_joints(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_ikHandles(self):
		""""""
		return self.m_editor.get_ikHandles()
	@QtSlot(bool)
	def editor_set_ikHandles(self, value):
		""""""
		self.m_editor.set_ikHandles(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_deformers(self):
		""""""
		return self.m_editor.get_deformers()
	@QtSlot(bool)
	def editor_set_deformers(self, value):
		""""""
		self.m_editor.set_deformers(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_dynamics(self):
		""""""
		return self.m_editor.get_dynamics()
	@QtSlot(bool)
	def editor_set_dynamics(self, value):
		""""""
		self.m_editor.set_dynamics(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_fluids(self):
		""""""
		return self.m_editor.get_fluids()
	@QtSlot(bool)
	def editor_set_fluids(self, value):
		""""""
		self.m_editor.set_fluids(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_hairSystems(self):
		""""""
		return self.m_editor.get_hairSystems()
	@QtSlot(bool)
	def editor_set_hairSystems(self, value):
		""""""
		self.m_editor.set_hairSystems(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_follicles(self):
		""""""
		return self.m_editor.get_follicles()
	@QtSlot(bool)
	def editor_set_follicles(self, value):
		""""""
		self.m_editor.set_follicles(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_nCloths(self):
		""""""
		return self.m_editor.get_nCloths()
	@QtSlot(bool)
	def editor_set_nCloths(self, value):
		""""""
		self.m_editor.set_nCloths(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_nParticles(self):
		""""""
		return self.m_editor.get_nParticles()
	@QtSlot(bool)
	def editor_set_nParticles(self, value):
		""""""
		self.m_editor.set_nParticles(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_nRigids(self):
		""""""
		return self.m_editor.get_nRigids()
	@QtSlot(bool)
	def editor_set_nRigids(self, value):
		""""""
		self.m_editor.set_nRigids(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_dynamicConstraints(self):
		""""""
		return self.m_editor.get_dynamicConstraints()
	@QtSlot(bool)
	def editor_set_dynamicConstraints(self, value):
		""""""
		self.m_editor.set_dynamicConstraints(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_locators(self):
		""""""
		return self.m_editor.get_locators()
	@QtSlot(bool)
	def editor_set_locators(self, value):
		""""""
		self.m_editor.set_locators(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_manipulators(self):
		""""""
		return self.m_editor.get_manipulators()
	@QtSlot(bool)
	def editor_set_manipulators(self, value):
		""""""
		self.m_editor.set_manipulators(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_dimensions(self):
		""""""
		return self.m_editor.get_dimensions()
	@QtSlot(bool)
	def editor_set_dimensions(self, value):
		""""""
		self.m_editor.set_dimensions(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_handles(self):
		""""""
		return self.m_editor.get_handles()
	@QtSlot(bool)
	def editor_set_handles(self, value):
		""""""
		self.m_editor.set_handles(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_pivots(self):
		""""""
		return self.m_editor.get_pivots()
	@QtSlot(bool)
	def editor_set_pivots(self, value):
		""""""
		self.m_editor.set_pivots(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_textures(self):
		""""""
		return self.m_editor.get_textures()
	@QtSlot(bool)
	def editor_set_textures(self, value):
		""""""
		self.m_editor.set_textures(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_strokes(self):
		""""""
		return self.m_editor.get_strokes()
	@QtSlot(bool)
	def editor_set_strokes(self, value):
		""""""
		self.m_editor.set_strokes(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_pluginObjects(self,value):
		""""""
		self.m_editor.set_(pluginObjects=value)
	#----------------------------------------------------------------------
	@property
	def editor_queryPluginObjects(self):
		""""""
		return self.m_editor.queryPluginObjects()
	#----------------------------------------------------------------------
	def editor_get_allObjects(self):
		""""""
		return self.m_editor.get_allObjects()
	@QtSlot(bool)
	def editor_set_allObjects(self, value):
		""""""
		self.m_editor.set_allObjects(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_useInteractiveMode(self):
		""""""
		return self.m_editor.get_useInteractiveMode()
	@QtSlot(bool)
	def editor_set_useInteractiveMode(self, value):
		""""""
		self.m_editor.set_useInteractiveMode(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_activeView(self):
		""""""
		return self.m_editor.get_activeView()
	@QtSlot(bool)
	def editor_set_activeView(self, value):
		""""""
		self.m_editor.set_activeView(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_sortTransparent(self):
		""""""
		return self.m_editor.get_sortTransparent()
	@QtSlot(bool)
	def editor_set_sortTransparent(self, value):
		""""""
		self.m_editor.set_sortTransparent(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_viewSelected(self):
		""""""
		return self.m_editor.get_viewSelected()
	@QtSlot(bool)
	def editor_set_viewSelected(self, value):
		""""""
		self.m_editor.set_viewSelected(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_setSelected(self,value):
		""""""
		self.m_editor.setSelected(value)
	@QtSlot(bool)
	def editor_addSelected(self,value):
		""""""
		self.m_editor.addSelected(value)
	@QtSlot(bool)
	def editor_removeSelected(self,value):
		""""""
		self.m_editor.removeSelected(value)
	@QtSlot(str)
	def editor_addObjects(self,value):
		""""""
		self.m_editor.addObjects(value)
	#----------------------------------------------------------------------
	@property
	def editor_viewObjects(self):
		""""""
		return self.m_editor.viewObjects()
	@QtSlot(bool)
	def editor_noUndo(self,value):
		""""""
		self.m_editor.noUndo(value)
	#----------------------------------------------------------------------
	@property
	def editor_cameraSetup(self):
		""""""
		return self.m_editor.get_cameraSetup()
	#----------------------------------------------------------------------
	def editor_get_editorChanged(self):
		""""""
		return self.m_editor.get_cameraSetup()
	#----------------------------------------------------------------------
	def editor_set_editorChanged(self, value):
		""""""
		self.m_editor.set_editorChanged(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def editor_get_objectFilter(self):
		""""""
		return self.m_editor.get_objectFilter()
	#----------------------------------------------------------------------
	def editor_set_objectFilter(self, value):
		""""""
		self.m_editor.set_objectFilter(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	@property
	def editor_objectFilterUI(self):
		""""""
		return self.m_editor.objectFilterUI()
	#----------------------------------------------------------------------
	@property
	def editor_objectFilterList(self):
		""""""
		return self.m_editor.objectFilterList()
	#----------------------------------------------------------------------
	@property
	def editor_objectFilterListUI(self):
		""""""
		return self.m_editor.objectFilterListUI()
	#----------------------------------------------------------------------
	def editor_get_objectFilterShowInHUD(self):
		""""""
		return self.m_editor.get_objectFilterShowInHUD()
	#----------------------------------------------------------------------
	def editor_set_objectFilterShowInHUD(self, value):
		""""""
		self.m_editor.set_objectFilterShowInHUD(value)
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	@property
	def editor_isFiltered(self):
		""""""
		return self.m_editor.isFiltered()
	#----------------------------------------------------------------------
	@property
	def editor_filteredObjectList(self):
		""""""
		return self.m_editor.filteredObjectList()
	#----------------------------------------------------------------------
	@property
	def editor_viewType(self):
		""""""
		return self.m_editor.viewType()

	filter                  = property(editor_get_filter, editor_set_filter)
	mainListConnection      = property(editor_get_mainListConnection, editor_set_mainListConnection)
	forceMainConnection     = property(editor_get_forceMainConnection, editor_set_forceMainConnection)
	selectionConnection     = property(editor_get_selectionConnection, editor_set_selectionConnection)
	highlightConnection     = property(editor_get_highlightConnection, editor_set_highlightConnection)
	docTag                  = property(editor_get_docTag, editor_set_docTag)
	camera                  = property(editor_get_camera, editor_set_camera)
	displayLights           = property(editor_get_displayLights, editor_set_displayLights)
	bufferMode              = property(editor_get_bufferMode, editor_set_bufferMode)
	activeOnly              = property(editor_get_activeOnly, editor_set_activeOnly)
	interactive             = property(editor_get_interactive, editor_set_interactive)
	default                 = property(editor_get_default, editor_set_default)
	ignorePanZoom           = property(editor_get_ignorePanZoom, editor_set_ignorePanZoom)
	twoSidedLighting        = property(editor_get_twoSidedLighting, editor_set_twoSidedLighting)
	displayAppearance       = property(editor_get_displayAppearance, editor_set_displayAppearance)
	wireframeOnShaded       = property(editor_get_wireframeOnShaded, editor_set_wireframeOnShaded)
	headsUpDisplay          = property(editor_get_headsUpDisplay, editor_set_headsUpDisplay)
	selectionHiliteDisplay  = property(editor_get_selectionHiliteDisplay, editor_set_selectionHiliteDisplay)
	useDefaultMaterial      = property(editor_get_useDefaultMaterial, editor_set_useDefaultMaterial)
	useColorIndex           = property(editor_get_useColorIndex, editor_set_useColorIndex)
	userNode                = property(editor_get_userNode, editor_set_userNode)
	wireframeBackingStore   = property(editor_get_wireframeBackingStore, editor_set_wireframeBackingStore)
	useRGBImagePlane        = property(editor_get_useRGBImagePlane, editor_set_useRGBImagePlane)
	imagePlane              = property(editor_get_imagePlane, editor_set_imagePlane)
	backfaceCulling         = property(editor_get_backfaceCulling, editor_set_backfaceCulling)
	xray                    = property(editor_get_xray, editor_set_xray)
	jointXray               = property(editor_get_jointXray, editor_set_jointXray)
	activeComponentsXray    = property(editor_get_activeComponentsXray, editor_set_activeComponentsXray)
	maxConstantTransparency = property(editor_get_maxConstantTransparency, editor_set_maxConstantTransparency)
	displayTextures         = property(editor_get_displayTextures, editor_set_displayTextures)
	smoothWireframe         = property(editor_get_smoothWireframe, editor_set_smoothWireframe)
	lineWidth               = property(editor_get_lineWidth, editor_set_lineWidth)
	textureMaxSize          = property(editor_get_textureMaxSize, editor_set_textureMaxSize)
	textureAnisotropic      = property(editor_get_textureAnisotropic, editor_set_textureAnisotropic)
	textureSampling         = property(editor_get_textureSampling, editor_set_textureSampling)
	textureDisplay          = property(editor_get_textureDisplay, editor_set_textureDisplay)
	textureHilight          = property(editor_get_textureHilight, editor_set_textureHilight)
	fogging                 = property(editor_get_fogging, editor_set_fogging)
	fogSource               = property(editor_get_fogSource, editor_set_fogSource)
	fogMode                 = property(editor_get_fogMode, editor_set_fogMode)
	fogDensity              = property(editor_get_fogDensity, editor_set_fogDensity)
	fogEnd                  = property(editor_get_fogEnd, editor_set_fogEnd)
	fogStart                = property(editor_get_fogStart, editor_set_fogStart)
	fogColor                = property(editor_get_fogColor, editor_set_fogColor)
	shadows                 = property(editor_get_shadows, editor_set_shadows)
	rendererName            = property(editor_get_rendererName, editor_set_rendererName)
	colorResolution         = property(editor_get_colorResolution, editor_set_colorResolution)
	bumpResolution          = property(editor_get_bumpResolution, editor_set_bumpResolution)
	transparencyAlgorithm   = property(editor_get_transparencyAlgorithm, editor_set_transparencyAlgorithm)
	transpInShadows         = property(editor_get_transpInShadows, editor_set_transpInShadows)
	cullingOverride         = property(editor_get_cullingOverride, editor_set_cullingOverride)
	lowQualityLighting      = property(editor_get_lowQualityLighting, editor_set_lowQualityLighting)
	occlusionCulling        = property(editor_get_occlusionCulling, editor_set_occlusionCulling)
	useBaseRenderer         = property(editor_get_useBaseRenderer, editor_set_useBaseRenderer)
	nurbsCurves             = property(editor_get_nurbsCurves, editor_set_nurbsCurves)
	nurbsSurfaces           = property(editor_get_nurbsSurfaces, editor_set_nurbsSurfaces)
	polymeshes              = property(editor_get_polymeshes, editor_set_polymeshes)
	subdivSurfaces          = property(editor_get_subdivSurfaces, editor_set_subdivSurfaces)
	planes                  = property(editor_get_planes, editor_set_planes)
	lights                  = property(editor_get_lights, editor_set_lights)
	cameras                 = property(editor_get_cameras, editor_set_cameras)
	controlVertices         = property(editor_get_controlVertices, editor_set_controlVertices)
	grid                    = property(editor_get_grid, editor_set_grid)
	hulls                   = property(editor_get_hulls, editor_set_hulls)
	joints                  = property(editor_get_joints, editor_set_joints)
	ikHandles               = property(editor_get_ikHandles, editor_set_ikHandles)
	deformers               = property(editor_get_deformers, editor_set_deformers)
	dynamics                = property(editor_get_dynamics, editor_set_dynamics)
	fluids                  = property(editor_get_fluids, editor_set_fluids)
	hairSystems             = property(editor_get_hairSystems, editor_set_hairSystems)
	follicles               = property(editor_get_follicles, editor_set_follicles)
	nCloths                 = property(editor_get_nCloths, editor_set_nCloths)
	nParticles              = property(editor_get_nParticles, editor_set_nParticles)
	nRigids                 = property(editor_get_nRigids, editor_set_nRigids)
	dynamicConstraints      = property(editor_get_dynamicConstraints, editor_set_dynamicConstraints)
	locators                = property(editor_get_locators, editor_set_locators)
	manipulators            = property(editor_get_manipulators, editor_set_manipulators)
	dimensions              = property(editor_get_dimensions, editor_set_dimensions)
	handles                 = property(editor_get_handles, editor_set_handles)
	pivots                  = property(editor_get_pivots, editor_set_pivots)
	textures                = property(editor_get_textures, editor_set_textures)
	strokes                 = property(editor_get_strokes, editor_set_strokes)
	allObjects              = property(editor_get_allObjects, editor_set_allObjects)
	useInteractiveMode      = property(editor_get_useInteractiveMode, editor_set_useInteractiveMode)
	activeView              = property(editor_get_activeView, editor_set_activeView)
	sortTransparent         = property(editor_get_sortTransparent, editor_set_sortTransparent)
	viewSelected            = property(editor_get_viewSelected, editor_set_viewSelected)
	editorChanged           = property(editor_get_editorChanged, editor_set_editorChanged)
	objectFilter            = property(editor_get_objectFilter, editor_set_objectFilter)
	objectFilterShowInHUD   = property(editor_get_objectFilterShowInHUD, editor_set_objectFilterShowInHUD)
##======================================================================
# Model Views
##======================================================================
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Table Model Views
########################################################################
class Standered_Table_View(QTableView):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Standered_Table_View, self).__init__(*args, **kwargs)
	#----------------------------------------------------------------------
	@QtSlot(QT.QMainWindow)
	def _run_setup(self, main_window):
		""""""
		isinstance(main_window, QT.QMainWindow)
		self.main_window            = main_window
		self.beauty_overide_view    = main_window.beauty_overide_view
		self.matte_overide_view     = main_window.matte_overide_view
		self.invisible_overide_view = main_window.invisible_overide_view
		self.part_sets_view         = main_window.part_sets_view
		self.render_states_view     = main_window.render_states_view
		self.asset_tree_view        = main_window.asset_tree_view
		self.entity_tree_view       = main_window.entity_tree_view
		
		isinstance(self.beauty_overide_view, Beauty_Overide_View)
		isinstance(self.matte_overide_view, Matte_Overide_View)
		isinstance(self.invisible_overide_view, Invisible_Overide_View)
		isinstance(self.part_sets_view, Part_Sets_List_View)
		isinstance(self.render_states_view, Render_States_List_View)
		isinstance(self.asset_tree_view, Asset_Tree_View)
		isinstance(self.entity_tree_view, Entity_Tree_View)
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ List Model Views
########################################################################
class Standered_List_View(QListView):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Standered_List_View, self).__init__(*args, **kwargs)
		
	#----------------------------------------------------------------------
	@QtSlot(QT.QMainWindow)
	def _run_setup(self, main_window):
		""""""
		isinstance(main_window, QT.QMainWindow)
		self.main_window            = main_window
		self.beauty_overide_view    = main_window.beauty_overide_view
		self.matte_overide_view     = main_window.matte_overide_view
		self.invisible_overide_view = main_window.invisible_overide_view
		self.part_sets_view         = main_window.part_sets_view
		self.render_states_view     = main_window.render_states_view
		self.asset_tree_view        = main_window.asset_tree_view
		self.entity_tree_view       = main_window.entity_tree_view
		# self.model_editor_widget    = main_window.Model_Editor
		
		isinstance(self.beauty_overide_view, Beauty_Overide_View)
		isinstance(self.matte_overide_view, Matte_Overide_View)
		isinstance(self.invisible_overide_view, Invisible_Overide_View)
		isinstance(self.part_sets_view, Part_Sets_List_View)
		isinstance(self.render_states_view, Render_States_List_View)
		isinstance(self.asset_tree_view, Asset_Tree_View)
		isinstance(self.entity_tree_view, Entity_Tree_View)
		# isinstance(self.model_editor_widget, Maya_Modle_Editor)
	#----------------------------------------------------------------------
	def selected_Items(self):
		res = []
		for index in self.selectedIndexes():
			item = self.item_From_Index(index)
			res.append(item)
		return res
	
	#----------------------------------------------------------------------
	def item_From_Index(self, index):
		item = index.model().itemFromIndex(index)
		isinstance(index, _Base_Item)
		return item
	
	def dragEnterEvent(self,event):
		super(Standered_List_View,self).dragEnterEvent(event)
	def model(self):
		res = super(Standered_List_View, self).model()
		isinstance(res, Vray_Scene_State_Manager_Item_Model)
		return res

########################################################################
class Filtered_Proxy_List_View(Standered_List_View):
	""""""
	ACTIVE_PROXY_INDEX_CHANGED = QtSignal(QtCore.QModelIndex)
	ACTIVE_INDEX_CHANGED       = QtSignal(QtCore.QModelIndex)
	ACTIVE_ITEM_CHANGED        = QtSignal(QT.QStandardItem)
	SELECTED_ITEMS_CHANGED     = QtSignal(list)
	ITEM_MEMBERES_SELECTED   = QtSignal(list)
	ITEM_MEMBERES_DESELECTED = QtSignal(list)
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Filtered_Proxy_List_View, self).__init__(*args, **kwargs)
	#----------------------------------------------------------------------
	def model(self):
		res = super(Filtered_Proxy_List_View, self).model()
		isinstance(res, Sorted_Item_Filter_ProxyModel)
		return res
	#----------------------------------------------------------------------
	def source_Model(self):
		res = self.model().sourceModel()
		isinstance(res, Vray_Scene_State_Manager_Item_Model)
		return res
	#----------------------------------------------------------------------
	def to_Source_Index(self, index):
		index = self.Model.mapToSource(index)
		isinstance(index, QtCore.QModelIndex)
		return index
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def set_Current_Item(self, item):
		index = self.Model.mapFromSource(item.index())
		self.setCurrentIndex(index)
	#----------------------------------------------------------------------
	def current_Source_Index(self):
		index = self.Model.mapToSource(self.CurrentIndex)
		isinstance(index, QtCore.QModelIndex)
		return index
	#----------------------------------------------------------------------
	def selected_Source_Index(self):
		res = []
		for index in self.selectedIndexes():
			index = self.Model.mapToSource(index)
			res.append(index)
		return res
	#----------------------------------------------------------------------
	def selected_Items(self):
		res = []
		for index in self.selectedIndexes():
			item = self.item_From_Index(index)
			res.append(item)
		return res
	#----------------------------------------------------------------------
	def selected_Real_Items(self):
		res = []
		for item in self.selected_Items():
			res.append(item._data)
		return res
	#----------------------------------------------------------------------
	def current_item(self):
		item  = self.Source_Model.itemFromIndex(self.current_Source_Index())
		isinstance(item, _Base_Item)
		return item
	#----------------------------------------------------------------------
	def item_From_Index(self, index):
		if index.model() == self.model():
			index = self.to_Source_Index(index)
		item = self.Source_Model.itemFromIndex(index)
		isinstance(index, _Base_Item)
		return item
	
	#----------------------------------------------------------------------
	def items_From_Index_List(self, indexs):
		res = []
		for index in indexs:
			item = self.item_From_Index(index)
			res.append(item)
		return res
	
	#----------------------------------------------------------------------
	def destination_Index(self, index):
		""""""
		return self.Model.mapFromSource(index)
	#----------------------------------------------------------------------
	def item_To_Destination_Index(self, item):
		""""""
		return self.Model.mapFromSource(item.index())
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def set_Root_Item(self, item):
		""""""
		index = self.item_To_Destination_Index(item)
		self.setRootIndex(index)
	#----------------------------------------------------------------------
	def root_Item(self):
		""""""
		return self.item_From_Index(self.rootIndex())
	#----------------------------------------------------------------------
	def setRootIndex(self,index):
		if index.isValid():
			if not index.model() == self.model():
				index = self.model().mapFromSource(index)
			super(Filtered_Proxy_List_View,self).setRootIndex(index)
	#----------------------------------------------------------------------
	def currentChanged(self, current, previous):
		res = super(Filtered_Proxy_List_View, self).currentChanged(current, previous)
		self.Update_On_Active_Index_Changed(current)
		return res
	
	#----------------------------------------------------------------------
	def Node_Members_From_Selection(self, selection):
		items       = self.items_From_Index_List(selection.indexes())
		memberNames = []
		for item in items:
			if item.type() == Part_Set_Reference_Item.ITEM_TYPE:
				isinstance(item, Part_Set_Reference_Item)
				
				memberNames.extend(item._data.node_memberNames)
		return memberNames
			
	#----------------------------------------------------------------------
	def selectionChanged(self, selected, deselected):
		super(Filtered_Proxy_List_View, self).selectionChanged(selected, deselected)
		items = self.items_From_Index_List(selected.indexes())
		self.SELECTED_ITEMS_CHANGED.emit(items)
		
		if deselected.count():
			members = self.Node_Members_From_Selection(deselected)
			self.ITEM_MEMBERES_DESELECTED.emit(members)
		if selected.count():
			members = self.Node_Members_From_Selection(selected)
			self.ITEM_MEMBERES_SELECTED.emit(members)
	
	#----------------------------------------------------------------------
	@QT.QtSlot(QtCore.QModelIndex)
	def Update_On_Active_Index_Changed(self, index):
		if index.isValid():
			proxy_index = index
			index       = self.to_Source_Index(proxy_index)
			item        = self.item_From_Index(proxy_index)
			self.ACTIVE_PROXY_INDEX_CHANGED.emit(proxy_index)
			self.ACTIVE_INDEX_CHANGED.emit(index)
			self.ACTIVE_ITEM_CHANGED.emit(item)
	Source_Model = property(source_Model)
########################################################################
class Render_States_List_View(Filtered_Proxy_List_View):
	""""""
	Selected_Render_State_Changed = QtSignal(QtCore.QModelIndex)
	ACTIVE_INDEX_CHANGED          = QtSignal(QtCore.QModelIndex)
	ACTIVE_ITEM_CHANGED           = QtSignal(QT.QStandardItem)
	
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Render_States_List_View, self).__init__(*args, **kwargs)
		
	#----------------------------------------------------------------------
	def currentChanged(self, current, previous):
		if not self.part_sets_view.SelectionModel == None:
			self.part_sets_view.SelectionModel.clearSelection()
		if not self.beauty_overide_view.SelectionModel == None:
			self.beauty_overide_view.SelectionModel.clearSelection()
		if not self.matte_overide_view.SelectionModel == None:
			self.matte_overide_view.SelectionModel.clearSelection()
		if not self.invisible_overide_view.SelectionModel == None:
			self.invisible_overide_view.SelectionModel.clearSelection()
		if self.main_window._Enable_Model_Editor:
			self.model_editor_widget.Main_Conn.clear()
		res = super(Render_States_List_View, self).currentChanged(current, previous)
	
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def Update_On_Active_Item_Changed(self, item):
		if item.Type == Asset_Item.ITEM_TYPE:
			isinstance(item, Asset_Item)
			self.set_Root_Item(item.Render_States)
			if item.Render_States.RowCount:
				self.set_Current_Item(item.Render_States.child(0))
	#----------------------------------------------------------------------
	def contextMenuEvent(self, event):
		win = self.window()
		menu = QT.QMenu(self)		
		index = self.indexAt(event.pos())
		item  = self.item_From_Index(index)
		if index.isValid():
			item.contextMenuActions(menu)
		else:
			menu.addAction(win.actionAdd_Render_State)
			menu.addAction(win.actionRemove_Selected_States)
		menu.exec_(event.globalPos())
		
	#def dragMoveEvent(self, event):
		#md =  event.mimeData()
		#self.matte_overide_view.setAcceptDrops(True)
		#self.part_sets_view.setAcceptDrops(True)
		#self.beauty_overide_view.setAcceptDrops(True)
		#self.invisible_overide_view.setAcceptDrops(True)
		#self.asset_tree_view.setAcceptDrops(True)
		#self.render_states_view.setAcceptDrops(True)
		#if isinstance(md, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			#if isinstance(md.drag_source, (Part_Sets_List_View, Beauty_Overide_View, Matte_Overide_View, Invisible_Overides_Item, Asset_Tree_View)):
				#self.setAcceptDrops(False)
			#else:
				#self.setAcceptDrops(True)
		#return super(Render_States_List_View, self).dragMoveEvent(event)
########################################################################
class Part_Sets_List_View(Filtered_Proxy_List_View):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Part_Sets_List_View, self).__init__(*args, **kwargs)
		
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def Update_On_Active_Item_Changed(self, item):
		if item.Type == Render_State_Item.ITEM_TYPE:
			isinstance(item, Render_State_Item)
			self.set_Root_Item(item.Unassined)
	
	def print_item(self):
		index = self.indexAt(self._context_pos).data()
		print index.data()
	#----------------------------------------------------------------------
	def contextMenuEvent(self, event):
		win = self.window()
		index = self.indexAt(event.pos())
		item  = self.item_From_Index(index)
		menu = QT.QMenu(self)
		menu.addAction(win.actionAdd_Part_Set)
		menu.addAction(win.actionDelete_Parts)
		if index.isValid():
			if _maya_check:
				item.contextMenuActions(menu)
		menu.exec_(event.globalPos())
		
	#def dragMoveEvent(self, event):
		#md =  event.mimeData()
		#self.matte_overide_view.setAcceptDrops(True)
		#self.part_sets_view.setAcceptDrops(True)
		#self.beauty_overide_view.setAcceptDrops(True)
		#self.invisible_overide_view.setAcceptDrops(True)
		#self.asset_tree_view.setAcceptDrops(True)
		#self.render_states_view.setAcceptDrops(True)
		#if isinstance(md, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			#if not isinstance(md.drag_source, (Beauty_Overide_View, Matte_Overide_View, Invisible_Overide_View)):
				#self.setAcceptDrops(False)
			#else:
				#self.setAcceptDrops(True)
		#return super(Part_Sets_List_View, self).dragMoveEvent(event)
########################################################################
class Beauty_Overide_View(Filtered_Proxy_List_View):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Beauty_Overide_View, self).__init__(*args, **kwargs)
		
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def Update_On_Active_Item_Changed(self, item):
		if item.Type == Render_State_Item.ITEM_TYPE:
			isinstance(item, Render_State_Item)
			self.set_Root_Item(item.Beauty)
			
	#def dragMoveEvent(self, event):
		#self.matte_overide_view.setAcceptDrops(True)
		#self.part_sets_view.setAcceptDrops(True)
		#self.beauty_overide_view.setAcceptDrops(True)
		#self.invisible_overide_view.setAcceptDrops(True)
		#self.asset_tree_view.setAcceptDrops(True)
		#self.render_states_view.setAcceptDrops(True)
		#md =  event.mimeData()
		#if isinstance(md, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			#if not isinstance(md.drag_source, (Part_Sets_List_View, Matte_Overide_View, Invisible_Overide_View)):
				#self.setAcceptDrops(False)
			#else:
				#self.setAcceptDrops(True)
		#return super(Beauty_Overide_View, self).dragMoveEvent(event)
	
########################################################################
class Invisible_Overide_View(Filtered_Proxy_List_View):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Invisible_Overide_View, self).__init__(*args, **kwargs)
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def Update_On_Active_Item_Changed(self, item):
		if item.Type == Render_State_Item.ITEM_TYPE:
			isinstance(item, Render_State_Item)
			self.set_Root_Item(item.Invisible)
	#----------------------------------------------------------------------
	#def dragMoveEvent(self, event):
		#md =  event.mimeData()
		#self.matte_overide_view.setAcceptDrops(True)
		#self.part_sets_view.setAcceptDrops(True)
		#self.beauty_overide_view.setAcceptDrops(True)
		#self.invisible_overide_view.setAcceptDrops(True)
		#self.asset_tree_view.setAcceptDrops(True)
		#self.render_states_view.setAcceptDrops(True)
		#if isinstance(md, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			#if not isinstance(md.drag_source, (Part_Sets_List_View, Matte_Overide_View, Beauty_Overide_View)):
				#self.setAcceptDrops(False)
			#else:
				#self.setAcceptDrops(True)
		#return super(Invisible_Overide_View, self).dragMoveEvent(event)
########################################################################
class Matte_Overide_View(Filtered_Proxy_List_View):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Matte_Overide_View, self).__init__(*args, **kwargs)
	#----------------------------------------------------------------------
	@QT.QtSlot(QT.QStandardItem)
	def Update_On_Active_Item_Changed(self, item):
		if item.Type == Render_State_Item.ITEM_TYPE:
			isinstance(item, Render_State_Item)
			self.set_Root_Item(item.Matte)
	#----------------------------------------------------------------------
	#def dragMoveEvent(self, event):
		#md =  event.mimeData()
		#self.matte_overide_view.setAcceptDrops(True)
		#self.part_sets_view.setAcceptDrops(True)
		#self.beauty_overide_view.setAcceptDrops(True)
		#self.invisible_overide_view.setAcceptDrops(True)
		#self.asset_tree_view.setAcceptDrops(True)
		#self.render_states_view.setAcceptDrops(True)
		#if isinstance(md, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			#if not isinstance(md.drag_source, (Part_Sets_List_View, Invisible_Overide_View, Beauty_Overide_View)):
				#self.setAcceptDrops(False)
			#else:
				#self.setAcceptDrops(True)
		#return super(Matte_Overide_View, self).dragMoveEvent(event)
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Tree Model Views
########################################################################
class Standered_Tree_View(QTreeView):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Standered_Tree_View, self).__init__(*args, **kwargs)

	#----------------------------------------------------------------------
	@QtSlot(QT.QMainWindow)
	def _run_setup(self, main_window):
		""""""
		isinstance(main_window, QT.QMainWindow)
		self.main_window            = main_window
		self.beauty_overide_view    = main_window.beauty_overide_view
		self.matte_overide_view     = main_window.matte_overide_view
		self.invisible_overide_view = main_window.invisible_overide_view
		self.part_sets_view         = main_window.part_sets_view
		self.render_states_view     = main_window.render_states_view
		self.asset_tree_view        = main_window.asset_tree_view
		self.entity_tree_view       = main_window.entity_tree_view
		
		isinstance(self.beauty_overide_view, Beauty_Overide_View)
		isinstance(self.matte_overide_view, Matte_Overide_View)
		isinstance(self.invisible_overide_view, Invisible_Overide_View)
		isinstance(self.part_sets_view, Part_Sets_List_View)
		isinstance(self.render_states_view, Render_States_List_View)
		isinstance(self.asset_tree_view, Asset_Tree_View)
		isinstance(self.entity_tree_view, Entity_Tree_View)

########################################################################
class Filtered_Proxy_Tree_View(Standered_Tree_View):
	""""""
	ACTIVE_PROXY_INDEX_CHANGED = QtSignal(QtCore.QModelIndex)
	ACTIVE_INDEX_CHANGED       = QtSignal(QtCore.QModelIndex)
	ACTIVE_ITEM_CHANGED        = QtSignal(QT.QStandardItem)
	#----------------------------------------------------------------------
	def model(self):
		res = super(Filtered_Proxy_Tree_View, self).model()
		isinstance(res, QT.QSortFilterProxyModel)
		return res
	#----------------------------------------------------------------------
	def source_Model(self):
		res = self.model().sourceModel()
		isinstance(res, Vray_Scene_State_Manager_Item_Model)
		return res
	#----------------------------------------------------------------------
	Source_Model = property(source_Model)
	#----------------------------------------------------------------------
	def to_Source_Index(self, index):
		index = self.Model.mapToSource(index)
		isinstance(index, QtCore.QModelIndex)
		return index
	#----------------------------------------------------------------------
	def to_destination_Index(self, index):
		""""""
		return self.Model.mapFromSource(index)

	#----------------------------------------------------------------------
	def current_Source_Index(self):
		index = self.Model.mapToSource(self.CurrentIndex)
		isinstance(index, QtCore.QModelIndex)
		return index
	#----------------------------------------------------------------------
	Current_Source_Index = property(current_Source_Index)
	#----------------------------------------------------------------------
	def selected_Source_Index(self):
		res = []
		for index in self.selectedIndexes():
			index = self.Model.mapToSource(index)
			res.append(index)
		return res
	#----------------------------------------------------------------------
	def selected_Items(self):
		res = []
		for index in self.selectedIndexes():
			item = self.item_From_Index(index)
			res.append(item)
		return res
	#----------------------------------------------------------------------
	@QtSlot(QT.QStandardItem)
	def set_Current_Item(self, item):
		index = self.Model.mapFromSource(item.index())
		self.setCurrentIndex(index)
	#----------------------------------------------------------------------
	def current_item(self):
		item  = self.Source_Model.itemFromIndex(self.Current_Source_Index)
		isinstance(item, _Base_Item)
		return item
	#----------------------------------------------------------------------
	def item_To_Destination_Index(self, item):
		""""""
		return self.Model.mapFromSource(item.index())
	#----------------------------------------------------------------------
	@QtSlot(QT.QStandardItem)
	def set_Root_Item(self, item):
		""""""
		index = self.item_To_Destination_Index(item)
		self.setRootIndex(index)
	#----------------------------------------------------------------------
	def root_Item(self):
		""""""
		return self.item_From_Index(self.rootIndex())
	#----------------------------------------------------------------------
	Current_Item = property(current_item)
	#----------------------------------------------------------------------
	def item_From_Index(self, index):
		if index.model() == self.model():
			index = self.to_Source_Index(index)
		item = self.Source_Model.itemFromIndex(index)
		isinstance(index, _Base_Item)
		return item
	#----------------------------------------------------------------------
	def currentChanged(self, current, previous):
		self.Update_On_Active_Index_Changed(current)
		return super(Filtered_Proxy_Tree_View, self).currentChanged(current, previous)
	#----------------------------------------------------------------------
	@QT.QtSlot(QtCore.QModelIndex)
	def Update_On_Active_Index_Changed(self, index):
		if index.isValid():
			proxy_index = index
			index       = self.to_Source_Index(proxy_index)
			item        = self.item_From_Index(proxy_index)
			self.ACTIVE_PROXY_INDEX_CHANGED.emit(proxy_index)
			self.ACTIVE_INDEX_CHANGED.emit(index)
			self.ACTIVE_ITEM_CHANGED.emit(item)

########################################################################
class Entity_Tree_View(Standered_Tree_View):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Entity_Tree_View, self).__init__(*args, **kwargs)
########################################################################
class Asset_Tree_View(Filtered_Proxy_Tree_View):
	""""""
	ACTIVE_PROXY_INDEX_CHANGED = QtSignal(QtCore.QModelIndex)
	ACTIVE_INDEX_CHANGED       = QtSignal(QtCore.QModelIndex)
	ACTIVE_ITEM_CHANGED        = QtSignal(QT.QStandardItem)
	#----------------------------------------------------------------------
	def __init__(self, *args, **kwargs):
		"""Constructor"""
		super(Asset_Tree_View, self).__init__(*args, **kwargs)
	#----------------------------------------------------------------------
	@QtSlot()	
	def add_New_Part_Set(self, name=None):
		""""""
		current_asset = self.current_item()
		isinstance(current_asset,Asset_Item)
		cmd = Add_Part_Set_Command(self.window().PART_SET_CREATED, current_asset, name=name)
		self.window().undo_stack.push(cmd)
		
	#----------------------------------------------------------------------
	@QtSlot()	
	def add_New_Render_State(self, name=None):
		""""""
		current_asset = self.current_item()
		cmd = Add_Render_State_Command(current_asset, name=name)
		self.window().undo_stack.push(cmd)
		
	#----------------------------------------------------------------------
	@QtSlot()	
	def add_New_Asset(self, name=None, subAsset=False):
		""""""
		if subAsset:
			current_asset = self.current_item()
		else:
			current_asset = self.Source_Model.Assets
			
		if subAsset and not isinstance(current_asset,Asset_Item):
			current_asset = self.Source_Model.Assets
		cmd = Add_Asset_Command(current_asset, name=name)
		self.window().undo_stack.push(cmd)
	#----------------------------------------------------------------------
	@QtSlot()
	def delete_Selected_Assets(self):
		items = self.selected_Items()
		if len(items):
			cmd = Remove_Asset_Command(self, asset=items[0])
			self.window().undo_stack.push(cmd)
	#----------------------------------------------------------------------
	@QtSlot()
	def delete_Selected_Part_Sets(self):
		asset  = self.current_item()
		parent = asset.Part_Sets
		items  = self.part_sets_view.selected_Real_Items()
		if len(items):
			cmd = Remove_Part_Set_Command(self, items)
			self.window().undo_stack.push(cmd)
			
	#----------------------------------------------------------------------
	@QtSlot()
	def delete_Empty_Part_Sets(self):
		asset  = self.current_item()
		parent = asset.Part_Sets
		empty_items = []
		for child in parent.Children:
			if not len(child.node_memberNames):
				empty_items.append(child)
		if len(empty_items):
			cmd = Remove_Part_Set_Command(self, empty_items)
			self.window().undo_stack.push(cmd)
	
	#----------------------------------------------------------------------
	@QtSlot()
	def delete_Selected_Render_States(self):
		items = self.render_states_view.selected_Items()
		if len(items):
			cmd = Remove_Render_State_Command(self, items)
			self.window().undo_stack.push(cmd)
			
	#----------------------------------------------------------------------
	@QT.QtSlot(QtCore.QModelIndex, QtCore.QModelIndex)
	def Update_On_Selection_Changed(self, current, previous):
		win = self.window()
		if isinstance(win, QT.QDockWidget):
			win = win.parentWidget()
		
		current_item  = self.item_From_Index(current)
		previous_item = self.item_From_Index(previous)
		if not isinstance(previous_item, _Base_Item):
			previous_name = "None"
		else:
			previous_name = previous_item.data()
		if not win.undo_stack.undoText() == "Select %s Deselect %s" % (current_item.data(), previous_name):
			cmd = Active_Asset_Change_Command(self, current_item, previous_item)
			win.undo_stack.push(cmd)
	#----------------------------------------------------------------------
	def currentChanged(self, current, previous):
		#self.Update_On_Selection_Changed(current, previous)
		#self.Update_On_Active_Index_Changed(current)
		super(Asset_Tree_View, self).currentChanged(current, previous)
	
	#----------------------------------------------------------------------
	def model(self):
		res = super(Asset_Tree_View, self).model()
		isinstance(res, Asset_Item_Filter_ProxyModel)
		return res

	def dragMoveEvent(self, event):
		md =  event.mimeData()
		self.matte_overide_view.setAcceptDrops(True)
		self.part_sets_view.setAcceptDrops(True)
		self.beauty_overide_view.setAcceptDrops(True)
		self.invisible_overide_view.setAcceptDrops(True)
		self.asset_tree_view.setAcceptDrops(True)
		self.render_states_view.setAcceptDrops(True)
		if isinstance(md, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			if not isinstance(md.drag_source, (Part_Sets_List_View)):
				event.setAccepted(False)
				
		self.setAcceptDrops(event.isAccepted())
		return super(Asset_Tree_View, self).dragMoveEvent(event)

	def contextMenuEvent(self, event):
		win = self.window()
		index = self.indexAt(event.pos())
		item  = self.item_From_Index(index)
		if index.isValid():
			if isinstance(item.model(), Vray_Scene_State_Manager_Item_Model):
				menu = QT.QMenu(self)
				if _maya_check:
					item.contextMenuActions(menu)
				menu.exec_(event.globalPos())		
##======================================================================
# Standered Data Model Items
##======================================================================
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Base Item Types
########################################################################
class _Base_Item(QT.DataModels.QStandardItem.QStandardItem):
	ITEM_TYPE       = QT.user_type_counter()
	Item_Data_Roles =  Data_Roles
	def __init__(self,*args,**kwargs):
		super(_Base_Item,self).__init__(*args,**kwargs)
	
	def resort_partent(self):
		self.parent().sortChildren()
		
	def data(self, role=Data_Roles.DISPLAY):
		if role == Data_Roles.ITEM_DATA:
			return self
		if role == QtCore.Qt.UserRole:
			return self
		return super(_Base_Item, self).data(role)
	
	#----------------------------------------------------------------------
	@property
	def asset_item_count(self):
		""""""
		res = len([item for item in self.Model.findItems(text="*",flags=Qt.MatchRecursive|Qt.MatchWildcard,column=0) if item.type() == Asset_Item.ITEM_TYPE])
		return res
	#----------------------------------------------------------------------
	@property
	def render_state_count(self):
		""""""
		res = len([item for item in self.Model.findItems(text="*",flags=Qt.MatchRecursive|Qt.MatchWildcard,column=0) if item.type() == Render_State_Item.ITEM_TYPE])
		return res
	#----------------------------------------------------------------------
	@property
	def part_sets_count(self):
		""""""
		res = len([item for item in self.Model.findItems(text="*",flags=Qt.MatchRecursive|Qt.MatchWildcard,column=0) if item.type() == Part_Set_Item.ITEM_TYPE])
		return res	
	#----------------------------------------------------------------------
	def find_Part_Sets_By_Name(self, name):
		""""""
		res = [item for item in self.model().findItems(text=name,flags=Qt.MatchRecursive|Qt.MatchExactly,column=0) if item.type() == Part_Set_Item.ITEM_TYPE]
		return res
	#----------------------------------------------------------------------
	def find_Render_States_By_Name(self, name):
		""""""
		res = [item for item in self.model().findItems(text=name,flags=Qt.MatchRecursive|Qt.MatchExactly,column=0) if item.type() == Render_State_Item.ITEM_TYPE]
		return res
	#----------------------------------------------------------------------
	def find_Part_Set_Refs_By_Name(self, name):
		""""""
		res = [item for item in self.model().findItems(text=name,flags=Qt.MatchRecursive|Qt.MatchExactly,column=0) if item.type() == Part_Set_Reference_Item.ITEM_TYPE]
		return res
########################################################################
class _Data_Item(_Base_Item):
	"""Base Class For Holding Non Qt Based Data"""
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self, data=None, **kwargs):
		super(_Data_Item,self).__init__(**kwargs)
		self._data = data

	def data(self, role=Data_Roles.DISPLAY):
		if role in self.Item_Data_Roles.DP_ED:
			return str(self._data)

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self._data
		
		if role == self.Item_Data_Roles.ITEM:
			return self

		return super(_Data_Item, self).data(role)

	def setData(self, value, role=Data_Roles.EDIT):
		if role in self.Item_Data_Roles.DP_ED:
			self._data =  value
		else:
			return super(_Data_Item, self).data(role)
########################################################################
class _Named_Data_Item(_Data_Item):
	ITEM_TYPE       = QT.user_type_counter()
	def __init__(self,name,**kwargs):
		data = Named_Data_Object(name)
		super(_Named_Data_Item,self).__init__(data,**kwargs)
		isinstance(self._data, Named_Data_Object)
		self.references = []
		
	def data(self, role=Data_Roles.DISPLAY):
		
		if role in self.Item_Data_Roles.DP_ED:
			return self._data.name

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self._data
		
		return super(_Named_Data_Item, self).data(role)

	def setData(self, value, role=Data_Roles.EDIT):
		if role in self.Item_Data_Roles.DP_ED:
			if isinstance(value, (unicode, str)):
				self._data.name = value
			else:
				self._data = value
		else:
			return super(_Named_Data_Item, self).data(role)
		
########################################################################
class _Reference_Item(_Base_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,item,**kwargs):
		super(_Reference_Item,self).__init__(**kwargs)
		self._data = item
		if hasattr(item,"references"):
			item.references.append(self)
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		return self._data.data(role)
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.EDIT):
		self._data.setData(value, role)

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ External Data Item Types
########################################################################
class MPlug_Item(_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self, node, **kwargs):
		""""""
		super(MPlug_Item,self).__init__(node, **kwargs)
		if _maya_check:
			self.node = node
			isinstance(self._data, M_Nodes.MPLUG)
			isinstance(self.node, M_Nodes.MPLUG)
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED:
			if _maya_check:
				return self._data.value

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self.node
		if role == self.Item_Data_Roles.ITEM:
			return self		

		return super(MPlug_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED and _maya_check:
			self._data.value = value
		else:
			return super(MPlug_Item, self).setData(value, role)	
	#----------------------------------------------------------------------
	def get_Node(self):
		""""""
		return self._data
	#----------------------------------------------------------------------
	def set_Node(self, node):
		""""""
		if isinstance(node, M_Nodes.MPLUG):
			self._data = node
		elif isinstance(node, str) and cmds.objExists(node):
			self._data = M_Nodes.MPLUG(node)
		else:
			raise ValueError("node input must be and instance of MNODE or a name of and existing Node")
	#----------------------------------------------------------------------
	node = property(get_Node, set_Node)
	
	#----------------------------------------------------------------------
	def node_get_Input_Plugs(self):
		""""""
		return self.node.get_Input_Plugs()
	#----------------------------------------------------------------------
	def node_get_Output_Plugs(self):
		""""""
		return self.node.get_Output_Plugs()
	#----------------------------------------------------------------------
	def node_get_Input_Nodes(self):
		""""""
		return self.node.get_Input_Nodes()
	#----------------------------------------------------------------------
	def node_get_Output_Nodes(self):
		""""""
		return self.node.get_Output_Nodes()
	#----------------------------------------------------------------------
	def node_Disconnect_All_Inputs(self):
		""""""
		self.node.Disconnect_All_Inputs()
	#----------------------------------------------------------------------
	def node_simple_Disconnect(self,plug):
		self.node.simple_Disconnect(plug)

	#----------------------------------------------------------------------
	def node_Simple_Connect(self,plg):
		""""""
		self.node.Simple_Connect(plug)
	#----------------------------------------------------------------------
	@property
	def node_lock(self):
		self.node.lock
	#----------------------------------------------------------------------
	@property
	def node_unlock(self):
		self.node.unlock
	#----------------------------------------------------------------------
	@property
	def node_name(self):
		return self.node.name
	#----------------------------------------------------------------------
	@property
	def node_partialName(self):
		self.node.partialName
	#----------------------------------------------------------------------
	@property
	def node_keyable(self):
		"""Return the keyable status of the attribute """
		return self.node.keyable
	#----------------------------------------------------------------------
	def node_make_keyable(self,val):
		"""Return the keyable status of the attribute """
		return self.node.make_keyable(val)
	#----------------------------------------------------------------------
	@property
	def node_exists(self):
		"""Return true if the attribute exists"""
		return self.node.exists
	#----------------------------------------------------------------------
	def node_enable_Render_Layer_Overide(self,layer=None):
		"""Return true if the attribute exists"""
		return self.node.enable_Render_Layer_Overide(layer=layer)
	#----------------------------------------------------------------------
	def node_disable_Render_Layer_Overide(self,layer=None):
		return self.node.disable_Render_Layer_Overide(layer=layer)
	#----------------------------------------------------------------------
	@property
	def node_connectable(self):
		"""Return the connectable status of the attribute"""
		return self.node.connectable
	#----------------------------------------------------------------------
	@property
	def node_message(self):
		"""Return true if the attribute is a message attribute"""
		return self.node.message
	#----------------------------------------------------------------------
	@property
	def node_enum(self):
		"""Return true if the attribute is a enum attribute"""
		return self.node.enum
	#----------------------------------------------------------------------
	@property
	def node_hidden(self):
		"""Return the hidden status of the attribute"""
		return self.node.hidden
	#----------------------------------------------------------------------
	@property
	def node_indexMatters(self):
		"""Return the indexMatters status of the attribute"""
		return self.node.indexMatters
	#----------------------------------------------------------------------
	@property
	def node_readable(self):
		"""Return the readable status of the attribute"""
		return self.node.readable
	#----------------------------------------------------------------------
	@property
	def node_storable(self):
		"""Return true if the attribute is storable"""
		return self.node.storable
	#----------------------------------------------------------------------
	@property
	def node_writable(self):
		"""Return true if the attribute is a message attribute"""
		return self.node.writable
	#----------------------------------------------------------------------
	@property
	def node_multi(self):
		"""Return true if the attribute is a multi-attribute"""
		return self.node.multi
	#----------------------------------------------------------------------
	@property
	def node_minimum(self):
		return self.node.minimum
	#----------------------------------------------------------------------
	@property
	def node_maximum(self):
		return self.node.maximum
	#----------------------------------------------------------------------
	@property
	def node_range(self):
		return self.node.range
	#----------------------------------------------------------------------
	@property
	def node_usedAsColor(self):
		return self.node.usedAsColor
	#----------------------------------------------------------------------
	@property
	def node_softRange(self):
		"""Return true if the attribute is a message attribute"""
		return self.node.softRange
	#----------------------------------------------------------------------
	@property
	def node_softMin(self):
		return self.node.softMin
	#----------------------------------------------------------------------
	@property
	def node_softMax(self):
		return self.node.softMax
	#----------------------------------------------------------------------
	@property
	def node_numberOfChildren(self):
		return self.node.numberOfChildren
	#----------------------------------------------------------------------
	@property
	def node_listSiblings(self):
		return self.node.listSiblings
	#----------------------------------------------------------------------
	@property
	def node_listChildren(self):
		return self.node.listChildren
	#----------------------------------------------------------------------
	@property
	def node_listParent(self):
		return self.node.listParent
	#----------------------------------------------------------------------
	@property
	def node_listEnum(self):
		return self.node.listEnum
	#----------------------------------------------------------------------
	@property
	def node_listEnumNames(self):
		return self.node.listEnumNames
	#----------------------------------------------------------------------
	@property
	def node_listDefault(self):
		return self.node.listDefault
	#----------------------------------------------------------------------
	@property
	def node_minExists(self):
		return self.node.minExists
	#----------------------------------------------------------------------
	@property
	def node_maxExists(self):
		return self.node.maxExists
	#----------------------------------------------------------------------
	@property
	def node_rangeExists(self):
		return self.node.rangeExists
	#----------------------------------------------------------------------
	@property
	def node_softMinExists(self):
		return self.node.softMinExists
	#----------------------------------------------------------------------
	@property
	def node_softMaxExists(self):
		return self.node.softMaxExists
	#----------------------------------------------------------------------
	@property
	def node_softRangeExists(self):
		return self.node.softRangeExists
	#----------------------------------------------------------------------
	@property
	def node_longName(self):
		return self.node.longName
	#----------------------------------------------------------------------
	@property
	def node_niceName(self):
		return self.node.niceName
	#----------------------------------------------------------------------
	@property
	def node_shortName(self):
		return self.node.shortName
	#----------------------------------------------------------------------
	@property
	def node_type(self):
		return self.node.type

########################################################################
class Enum_Plug_Item(MPlug_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self, node, **kwargs):
		""""""
		super(Enum_Plug_Item,self).__init__(node, **kwargs)
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED:
			if _maya_check:
				if role == self.Item_Data_Roles.EDIT:
					return self._data.listEnumNames
				else:
					if not self._data.listEnumNames:
						return self._data.value
					return self._data.listEnumNames[self._data.value]
		return super(Enum_Plug_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED and _maya_check:
			try:
				index = self._data.listEnumNames.index(value)
				self._data.value = index
			except ValueError:
				pass
		else:
			return super(Enum_Plug_Item, self).setData(value, role)	

########################################################################
class MNode_Item(_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self, node, **kwargs):
		""""""
		super(MNode_Item,self).__init__(node, **kwargs)
		if _maya_check:
			self.node = node
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED:
			if _maya_check:
				return self.node_name

		if role == self.Item_Data_Roles.DATA_OBJECT:
			return self.node

		return super(MNode_Item, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED and _maya_check:
			self.node_name = value
		else:
			return super(MNode_Item, self).setData(value, role)	
	#----------------------------------------------------------------------
	def get_Node(self):
		""""""
		return self._data
	#----------------------------------------------------------------------
	def set_Node(self, node):
		""""""
		if isinstance(node, M_Nodes.MNODE):
			self._data = node
		elif isinstance(node, str) and cmds.objExists(node):
			self._data = M_Nodes.MNODE(node)
		else:
			raise ValueError("node input must be and instance of MNODE or a name of and existing Node")
	#----------------------------------------------------------------------
	node = property(get_Node, set_Node)
	#----------------------------------------------------------------------
	def get_Node_Name(self):
		""""""
		return self._data.nice_name_wo_ns
	#----------------------------------------------------------------------
	def set_Node_Name(self, name):
		""""""
		self._data.name =  name
	#----------------------------------------------------------------------
	node_name = property(get_Node_Name, set_Node_Name)
	#----------------------------------------------------------------------
	@property
	def node_type(self):
		""""""
		return self._data.objectType
	#----------------------------------------------------------------------
	@property
	def node_transform_type(self):
		""""""
		return self._data.transfromType
	#----------------------------------------------------------------------
	@property
	def node_assined_display_layer(self):
		""""""
		return self._data.assinedDisplayLayer
	#----------------------------------------------------------------------
	@property
	def node_transform_descendents(self):
		""""""
		return self._data.all_transform_Descendents
	#----------------------------------------------------------------------
	@property
	def node_child_count(self):
		""""""
		return self._data.numberOfChildern
	#----------------------------------------------------------------------
	@property
	def node_Descendents(self):
		""""""
		return self._data.allDescendents
	#----------------------------------------------------------------------
	@property
	def node_child_transforms(self):
		""""""
		return self._data.child_transforms
	#----------------------------------------------------------------------
	@property
	def node_has_child_transforms(self):
		""""""
		return self._data.has_child_transforms
	#----------------------------------------------------------------------
	@property
	def node_children(self):
		""""""
		return self._data.children
	#----------------------------------------------------------------------
	@property
	def node_parents(self):
		""""""
		return self._data.allParents
	#----------------------------------------------------------------------
	@property
	def node_exists(self):
		""""""
		return self._data.objectExists

	#----------------------------------------------------------------------
	def node_delete(self):
		""""""
		return self._data.delete()
########################################################################
class Maya_Asset_Item(MNode_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.Container(name,
				                         dagContainer=True,
				                         force=False, addNode=False,
				                         current=False,
				                         includeShaders=False,
				                         publishConnections=False,
				                         nodeNamePrefix=False,
				                         includeHierarchyAbove=False,
				                         includeHierarchyBelow=False)
				
		super(Maya_Asset_Item, self).__init__(name, **kwargs)
		if _maya_check:
			if isinstance(self._data, M_Nodes.Container):
				self.node_plug_rmbCommand      = self._data.rmbCommand
				self.node_plug_templateName    = self._data.templateName
				self.node_plug_templateVersion = self._data.templateVersion
				self.node_plug_templatePath    = self._data.templatePath
				self.node_plug_iconName        = self._data.iconName
				self.node_plug_viewMode        = self._data.viewMode
				self.node_plug_creator         = self._data.creator
				self.node_plug_creationDate    = self._data.creationDate
				self.node_plug_rootTransform   = self._data.rootTransform

	#----------------------------------------------------------------------
	def node_bindAttr(self,nodeAttr,unboundName):
		"""
		Bind a contained attribute to an unbound published name on the interface of the container
		returns a list of bound published names.
		The first string specifies the node and attribute name to be bound in "node.attr" format.
		The second string specifies the name of the unbound published name.
		In query mode, returns a string array of the published names and their corresponding attributes.
		The flag can also be used in query mode in conjunction with the
		-publishName, -publishAsParent, and -publishAsChild flags.
		"""
		return self._data.bindAttr(nodeAttr, unboundName)
	#----------------------------------------------------------------------
	def node_unbindAttr(self,nodeAttr,unboundName):
		"""Unbind a published attribute from its published name on the interface of the container,
		leaving an unbound published name on the interface of the container
		returns a list of unbound published names.
		The first string specifies the node and attribute name to be unbound in "node.attr" format,
		and the second string specifies the name of the bound published name.
		In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
		"""
		return self._data.unbindAttr(nodeAttr, unboundName)
	#----------------------------------------------------------------------
	def node_unpublishName(self,name):
		"""Unpublish an unbound name from the interface of the container."""
		return self._data.unpublishName(name)
	#----------------------------------------------------------------------
	def node_unbindAndUnpublish(self,name):
		""""""
		return self._data.unbindAndUnpublish(name)
	#----------------------------------------------------------------------
	def node_publishName(self,name,bindTo=""):
		"""
		Publish a name to the interface of the container
		
		if bindTo is set with the format "node.attr"
		  Publish the given name and bind the attribute to the given name
		  
		returns the actual name published to the interface.
		"""
		return self._data.publishName(name, bindTo=bindTo)
	#----------------------------------------------------------------------
	def node_publishAsParent(self,node,name):
		"""Publish contained node to the interface of the container to indicate it can be a parent to external nodes.
		The second string is the name of the published node.
		In query mode, 
		  returns a string of array of the published names and the corresponding nodes.
		  
		If -publishName flag is used in query mode,
		  only returns the published names;
		  
		if -bindAttr flag is used in query mode,
		  only returns the name of the published nodes."""
		return self._data.publishAsParent(node, name)
	#----------------------------------------------------------------------
	def node_unpublishParent(self,name):
		""""""
		return self._data.unpublishParent(name)
	#----------------------------------------------------------------------
	def node_unpublishChild(self,name):
		""""""
		return self._data.unpublishChild(name)
	#----------------------------------------------------------------------
	def node_publishAsChild(self,node,name):
		"""Publish contained node to the interface of the container to indicate it can be a child of external nodes.
		The second string is the name of the published node.
		In query mode,
		  returns a string of the published names and the corresponding nodes.
		
		If -publishName flag is used in query mode,
		  only returns the published names;
		
		if -bindAttr flag is used in query mode,
		  only returns the name of the published nodes."""
		
		return self._data.publishAsChild(node, name)
	
	#----------------------------------------------------------------------
	def node_publishedNames(self,bound=False,unBound=False,parents=False,children=False,NodeAttr=""):
		"""returns the published names for the container.
		If the bound flag is True,
		  returns only the names that are bound;
		  
		if the unBound flag is True,
		  returns only the names that are not bound;
		  
		if the parents flags is True,
		  returns only names of published parents.
		  
		if the children flags is True,
		  returns only names of published children.
		  
		if the NodeAttr is specified with an attribute argument in the "node.attr" format,
		  returns the published name for that attribute, if any.
		"""
		return self._data.publishedNames(bound=bound, unBound=unBound, parents=parents, children=children, NodeAttr=NodeAttr)
	
	#----------------------------------------------------------------------
	def node_addNode(self, nodes, includeNetwork=False, includeHierarchyBelow=False):
		""""""
		return self._data.addNode(nodes, includeNetwork=includeNetwork, includeHierarchyBelow=includeHierarchyBelow)
	#----------------------------------------------------------------------
	@QtSlot()
	def node_addSelectedNodes(self, includeNetwork=False, includeHierarchyBelow=False):
		""""""
		return self._data.addSelectedNodes(includeNetwork=includeNetwork, includeHierarchyBelow=includeHierarchyBelow)
	#----------------------------------------------------------------------
	def node_removeNode(self,*nodes):
		"""Specifies the list of nodes to remove from container."""
		return self._data.removeNode(*nodes)
	#----------------------------------------------------------------------
	@property
	def node_nodeList(self):
		"""Specifies the list of nodes to remove from container."""
		return self._data.nodeList
	#----------------------------------------------------------------------
	def node_makeCurent(self):
		""""""
		return self._data.makeCurent()
		
	#----------------------------------------------------------------------
	@property
	def node_parentContainer(self):
		""""""
		return self._data.parentContainer
		
	#----------------------------------------------------------------------
	def node_asset(self,*nodes):
		""""""
		return self._data.asset(*nodes)
	
	#----------------------------------------------------------------------
	def node_removeContainer(self):
		""""""
		return self._data.removeContainer()
	
	#----------------------------------------------------------------------
	@QtSlot()
	def node_select_Container_Contents(self):
		self._data.select_Container_Contents
	#----------------------------------------------------------------------
	@QtSlot()
	def node_select_Transform_Descendents(self):
		self._data.select_Transform_Descendents
	#----------------------------------------------------------------------
	@QtSlot()
	def node_select_All_Descendents(self):
		self._data.select_All_Descendents
	#----------------------------------------------------------------------
	@QtSlot()
	def node_select_All_Parents(self):
		self._data.select_All_Parents
########################################################################
class Maya_Render_Layer_Item(MNode_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.RenderLayer(name)
		super(Maya_Render_Layer_Item, self).__init__(name, **kwargs)
		if _maya_check:
			isinstance(self._data, M_Nodes.RenderLayer)


########################################################################
class Maya_Display_Layer_Item(MNode_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.RenderLayer(name)
		super(Maya_Display_Layer_Item, self).__init__(name, **kwargs)
		if _maya_check:
			isinstance(self._data, M_Nodes.DisplayLayer)

########################################################################
class Maya_Selection_Set_Item(MNode_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.SelectionSet(name, empty=True, copy=None, text="", renderable=False)
		super(Maya_Selection_Set_Item, self).__init__(name, **kwargs)
		if _maya_check:
			isinstance(self._data, M_Nodes.SelectionSet)
	#----------------------------------------------------------------------
	def node_select_set(self):
		self._data.select_set()
	#----------------------------------------------------------------------
	def node_select_members(self):
		self._data.select_members()
	#----------------------------------------------------------------------
	def node_remove_items(self,*items):
		self._data.remove(*items)
	#----------------------------------------------------------------------
	def node_remove_selected(self):
		self._data.remove_selected()
	#----------------------------------------------------------------------
	def node_include_items(self,*items):
		self._data.include(*items)
	#----------------------------------------------------------------------
	def node_include_special(self,*items):
		self._data.include_special(*items)
	#----------------------------------------------------------------------
	def node_addElement(self,*items):
		self._data.addElement(*items)
	#----------------------------------------------------------------------
	def node_intersecting_members(self,selectionSet):
		return self._data.intersecting_members(selectionSet)
	#----------------------------------------------------------------------
	def node_isSubSet(self,item):
		return self._data.isSubSet(item)
	#----------------------------------------------------------------------
	def node_hasSubSet(self,item):
		return self._data.hasSubSet(item)
	#----------------------------------------------------------------------
	@property
	def node_size(self):
		return self._data.size
	#----------------------------------------------------------------------
	@property
	def node_memberNames(self):
		return self._data.memberNames
	#----------------------------------------------------------------------
	@property
	def node_members(self):
		return self._data.members
	#----------------------------------------------------------------------
	@property
	def node_parents(self):
		return self._data.parents
	#----------------------------------------------------------------------
	@property
	def node_children(self):
		return self._data.children

########################################################################
class Vray_Object_Properties_Item(Maya_Selection_Set_Item):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		"""Constructor"""
		if _maya_check:
			if not isinstance(name, M_Nodes.MNODE):
				name = M_Nodes.VRayRenderState(name)
		super(Vray_Object_Properties_Item, self).__init__(name, **kwargs)
		if _maya_check:
			if isinstance(self._data, M_Nodes.VRayRenderState):
				self.node_plug_giVisibility           = self._data._giVisibility_plug
				self.node_plug_primaryVisibility      = self._data._primaryVisibility_plug
				self.node_plug_reflectionVisibility   = self._data._reflectionVisibility_plug
				self.node_plug_refractionVisibility   = self._data._refractionVisibility_plug
				self.node_plug_shadowVisibility       = self._data._shadowVisibility_plug
				self.node_plug_matteSurface           = self._data._matteSurface_plug
				self.node_plug_generateRenderElements = self._data._generateRenderElements_plug
				self.node_plug_shadows                = self._data._shadows_plug
				self.node_plug_affectAlpha            = self._data._affectAlpha_plug
				self.node_plug_generateGI             = self._data._generateGI_plug
				self.node_plug_receiveGI              = self._data._receiveGI_plug
				self.node_plug_generateCaustics       = self._data._generateCaustics_plug
				self.node_plug_receiveCaustics        = self._data._receiveCaustics_plug
				self.node_plug_ignore                 = self._data._ignore_plug
				self.node_plug_overrideMBSamples      = self._data._overrideMBSamples_plug
				self.node_plug_objectIDEnabled        = self._data._objectIDEnabled_plug
				self.node_plug_alphaContribution      = self._data._alphaContribution_plug
	


	def Add_Members_To_Render_Layer(self,layer=None):
		self._data.Add_Members_To_Render_Layer(layer)

	def Remove_Members_To_Render_Layer(self,layer=None):
		self._data.Remove_Members_From_Render_Layer(layer)

	def apply_Matte_Layer_Override(self,layer=None):
		self._data.apply_Matte_Layer_Override(layer)

	def apply_Invisible_Layer_Override(self,layer=None):
		self._data.apply_Invisible_Layer_Override(layer)

	def apply_Beauty_Layer_Override(self,layer=None):
		self._data.apply_Beauty_Layer_Override(layer)

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Top Level Item Types
########################################################################
class Assets_Item(_Named_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self,**kwargs):
		if kwargs.has_key("yaml"):
			assets = kwargs.pop("yaml")
			from_yaml = True
		else:
			from_yaml = False
		super(Assets_Item,self).__init__("Assets", **kwargs)
		if from_yaml:
			self.from_Yaml(assets)
	#----------------------------------------------------------------------
	def to_Yaml(self):
		""""""
		items = []
		for item in self.rowChildren():
			isinstance(item, Asset_Item)
			asset = item.to_Yaml()
			items.append(asset)
		assets = Yaml_Config_Data.Assets(items=items, parent=None)
		
		for item in items:
			item.parent = assets
		return assets
	#----------------------------------------------------------------------
	def from_Yaml(self, assets):
		""""""
		items = []
		isinstance(assets, Yaml_Config_Data.Assets)
		for asset in assets.items:
			isinstance(asset,Yaml_Config_Data.Asset)
			item = Asset_Item(asset, asset_parent=self)
			#self.appendRow(item)
			#plug = Enum_Plug_Item(item.enum_render_states_plug)
			#self.setChild(item.row(), plug, column=1)
########################################################################
class File_Reference_Item(_Named_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self, Config_Data,**kwargs):
		isinstance(Config_Data, Yaml_Config_Data.Config_Data)
		super(File_Reference_Item, self).__init__(Config_Data.name_space, **kwargs)
		self.setColumnCount(2)
		self._config_data = Config_Data
		for asset in Config_Data.Assets.items:
			asset_item = Asset_Item(asset, asset_parent=self)
			asset_item.setColumnCount(2)
			#self.appendRow(asset_item)
			plug = Enum_Plug_Item(asset_item.enum_render_states_plug)
			self.setChild(asset_item.row(), plug, column=1)

########################################################################
class Part_Sets_Item(_Named_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self,**kwargs):
		if kwargs.has_key("yaml"):
			assets = kwargs.pop("yaml")
			from_yaml = True
		else:
			from_yaml = False
		super(Part_Sets_Item,self).__init__("Part_Sets",**kwargs)
		if from_yaml:
			self.from_Yaml(assets)
		
	#----------------------------------------------------------------------
	def to_Yaml(self):
		""""""
		part_sets = Yaml_Config_Data.Part_Sets()
		for part in self.rowChildren():
			isinstance(part,Part_Set_Item)
			item = part.to_Yaml()
			item.parent = part_sets
			part_sets.parts.append( item )
		return part_sets
	#----------------------------------------------------------------------
	def from_Yaml(self, part_sets):
		""""""
		items = []
		isinstance(part_sets, Yaml_Config_Data.Part_Sets)
		for part in part_sets.parts:
			isinstance(part,Yaml_Config_Data.Part_Set)
			item = Part_Set_Item(part)
			items.append(item)
		self.appendRows(items)

########################################################################
class Render_States_Item(_Named_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self,**kwargs):
		if kwargs.has_key("yaml") and  kwargs.has_key("part_sets"):
			render_states = kwargs.pop("yaml")
			part_sets     = kwargs.pop("part_sets")
			asset_parent  = kwargs.pop("asset_parent")
			from_yaml = True
		else:
			from_yaml = False
		super(Render_States_Item,self).__init__("Render States", **kwargs)
		if from_yaml:
			self.from_Yaml(render_states, part_sets)
			
	#----------------------------------------------------------------------
	def to_Yaml(self, parts):
		""""""
		render_states =  Yaml_Config_Data.Render_States()
		for child in  self.rowChildren():
			isinstance(child, Render_State_Item)
			state = child.to_Yaml(parts)
			state.parent = render_states
			render_states.states.append(state)
		return render_states
	#----------------------------------------------------------------------
	def from_Yaml(self, render_states, part_sets):
		""""""
		isinstance(render_states, Yaml_Config_Data.Render_States)
		isinstance(part_sets, Part_Sets_Item)
		for render_state in render_states.states:
			isinstance(render_state,Yaml_Config_Data.Render_State)
			item = Render_State_Item(None, yaml=render_state, part_sets=part_sets)
			self.appendRow(item)
########################################################################
class Render_Layers_Item(_Named_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self,**kwargs):
		super(Render_Layers_Item,self).__init__("Render Layers", **kwargs)
		for layer in Scripts.Global_Constants.Nodes.Render_Layers(includeDefault=True):
			self.appendRow(Maya_Render_Layer_Item(layer))

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Item Collection Types
########################################################################
class Render_State_Item(_Named_Data_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,name,**kwargs):
		if kwargs.has_key("yaml") and kwargs.has_key("part_sets"):
			render_state = kwargs.pop("yaml")
			part_sets    = kwargs.pop("part_sets")
			super(Render_State_Item,self).__init__(render_state.name,**kwargs)
			from_yaml = True
		else:
			super(Render_State_Item,self).__init__(name,**kwargs)
			from_yaml = False
			
		self.RowCount = 4
		if not from_yaml:
			self.Matte               = Matte_Overides_Item()
			self.Invisible           = Invisible_Overides_Item()
			self.Beauty              = Beauty_Overides_Item()
			self.Unassined           = Unassined_Overides_Item()
			self.favorit             = 0
			self.setChild(0, 0, self.Unassined)
			self.setChild(1, 0, self.Matte)
			self.setChild(2, 0, self.Invisible)
			self.setChild(3, 0, self.Beauty)
			self.uid = str(uuid.uuid4())
			self._asset_assembly_ref = None
		else:
			self.from_Yaml(render_state, part_sets)
	#----------------------------------------------------------------------
	def contextMenuActions(self, menu):
		action_Set_Fav = QT.QAction(menu)
		if self.favorit:
			action_Set_Fav.setText("Remove From Favorits")
			action_Set_Fav.triggered.connect(self.remove_From_Favorit)
		else:
			action_Set_Fav.setText("Add To Favorits")
			action_Set_Fav.triggered.connect(self.add_To_Favorit)
		menu.addAction(action_Set_Fav)
	#----------------------------------------------------------------------
	def add_To_Favorit(self):
		""""""
		self.favorit = 1
	#----------------------------------------------------------------------
	def remove_From_Favorit(self):
		""""""
		self.favorit = 0
	#----------------------------------------------------------------------
	def to_Yaml(self, parts):
		""""""
		name         = self.data()
		Unassined    = self.Unassined.to_Yaml(parts)
		Matte        = self.Matte.to_Yaml(parts)
		Invisible    = self.Invisible.to_Yaml(parts)
		Beauty       = self.Beauty.to_Yaml(parts)
		render_state = Yaml_Config_Data.Render_State(name=name, Unassined=Unassined, Matte=Matte, Invisible=Invisible, Beauty=Beauty, favorit=self.favorit,uid=self.uid)
		
		Unassined.parent = render_state
		Matte.parent     = render_state
		Invisible.parent = render_state
		Beauty.parent    = render_state
		return render_state
	#----------------------------------------------------------------------
	def from_Yaml(self, render_state, part_sets):
		""""""
		isinstance(render_state, Yaml_Config_Data.Render_State)
		isinstance(part_sets, Part_Sets_Item)
		self.Matte               = Matte_Overides_Item(yaml=render_state.Matte, part_sets=part_sets)
		self.Invisible           = Invisible_Overides_Item(yaml=render_state.Invisible, part_sets=part_sets)
		self.Beauty              = Beauty_Overides_Item(yaml=render_state.Beauty, part_sets=part_sets)
		self.Unassined           = Unassined_Overides_Item(yaml=render_state.Unassined, part_sets=part_sets)
		
		if not hasattr(render_state, "favorit"):
			self.favorit             = 0
		else:
			self.favorit             = render_state.favorit
			
		if not hasattr(render_state, "uid"):
			self.uid                 = str(uuid.uuid4())
		else:
			self.uid                 = render_state.uid
		
		if not hasattr(render_state, "_asset_assembly_ref"):
			self._asset_assembly_ref = None
		else:
			self._asset_assembly_ref = render_state._asset_assembly_ref			
		self.setChild(0, 0, self.Unassined)
		self.setChild(1, 0, self.Matte)
		self.setChild(2, 0, self.Invisible)
		self.setChild(3, 0, self.Beauty)
	
	#----------------------------------------------------------------------
	def apply_Vray_Overide_States(self):
		if not cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) == "defaultRenderLayer":
			# self.parent().parent().clear_Children_From_Render_Layer()
			for child in  self.Children:
				child.apply_Vray_Overide_States()
				
			
	#----------------------------------------------------------------------
	def get_all_but_unassied_parts(self):
		items = []
		items.extend([item for item in self.Beauty.Children])
		items.extend([item for item in self.Matte.Children])
		items.extend([item for item in self.Invisible.Children])
		return items
	
	#----------------------------------------------------------------------
	def get_all_but_unassied_node_members(self):
		nodes = []
		items = [item._data.node for item in self.get_all_but_unassied_parts()]
		for item in items:
			nodes.extend(item.members)
		return nodes
	
	@property
	def Beauty_Parts(self):
		return self.Beauty.Children
	@property
	def Matte_Parts(self):
		return self.Matte.Children
	@property
	def Invisible_Parts(self):
		return self.Invisible.Children
	@property
	def Unassined_Parts(self):
		return self.Unassined.Children
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		
		if role == self.Item_Data_Roles.FOREGROUND and self.favorit:
			return QT.QColor(Qt.green)
		return super(Render_State_Item, self).data(role)
	
########################################################################
class Reference_Container_Item(_Named_Data_Item):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		if kwargs.has_key("yaml") and kwargs.has_key("part_sets"):
			from_yaml = True
			container = kwargs.pop("yaml")
			part_sets = kwargs.pop("part_sets")
		else:
			from_yaml = False
			
		super(Reference_Container_Item,self).__init__(name,**kwargs)
		if from_yaml:
			self.from_Yaml(container, part_sets)
			
	#----------------------------------------------------------------------
	def to_Yaml(self, container, parts):
		""""""
		isinstance(container, Yaml_Config_Data.Overides_Container)
		isinstance(parts,list)
		for item in self.rowChildren():
			isinstance(item, Part_Set_Reference_Item)
			if item.type() != 0:
				part = item.to_Yaml(parts)
				if not part == None:
					container.links.append(part)
		return container
	#----------------------------------------------------------------------
	def from_Yaml(self, container, part_sets):
		""""""
		isinstance(container, Yaml_Config_Data.Overides_Container)
		isinstance(part_sets, Part_Sets_Item)
		refs = []
		for link in container.links:
			isinstance(link, Yaml_Config_Data.Part_Set)
			for part_set in part_sets.Children:
				isinstance(part_set, Part_Set_Item)
				if part_set.data() == link.name:
					refs.append(Part_Set_Reference_Item(part_set))
					break
		self.appendRows(refs)

########################################################################
class Overides_Item(Reference_Container_Item):
	""""""
	#----------------------------------------------------------------------
	def to_Yaml(self,parts):
		""""""
		if self.ITEM_TYPE == Beauty_Overides_Item.ITEM_TYPE:
			container = Yaml_Config_Data.Beauty_Overides()
		elif self.ITEM_TYPE == Matte_Overides_Item.ITEM_TYPE:
			container = Yaml_Config_Data.Matte_Overides()
		elif self.ITEM_TYPE == Invisible_Overides_Item.ITEM_TYPE:
			container = Yaml_Config_Data.Invisible_Overides()
		elif self.ITEM_TYPE == Unassined_Overides_Item.ITEM_TYPE:
			container = Yaml_Config_Data.Unassined_Overides()
		else:
			cmds.error("ITEM TYPE Could Not Be Found")
			raise LookupError("ITEM TYPE Could Not Be Found")
		return super(Overides_Item, self).to_Yaml(container, parts)
	#----------------------------------------------------------------------
	def apply_Vray_Overide_States(self):
		if not cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) == "defaultRenderLayer":
			
			for ref in self.Children:
				if Viewer_Version_check() == 1:
					if self.ITEM_TYPE in [Beauty_Overides_Item.ITEM_TYPE, Matte_Overides_Item.ITEM_TYPE, Invisible_Overides_Item.ITEM_TYPE]:
						ref._data.Add_Members_To_Render_Layer()
					else:
						ref._data._data.Remove_Members_From_Render_Layer()
							
				if self.ITEM_TYPE == Beauty_Overides_Item.ITEM_TYPE:
					ref._data.apply_Beauty_Layer_Override()
				elif self.ITEM_TYPE == Matte_Overides_Item.ITEM_TYPE:
					ref._data.apply_Matte_Layer_Override()
				elif self.ITEM_TYPE == Invisible_Overides_Item.ITEM_TYPE:
					ref._data.apply_Invisible_Layer_Override()
				elif self.ITEM_TYPE == Unassined_Overides_Item.ITEM_TYPE:
					ref._data._data.set_Default_Override_Values()
				
				if Viewer_Version_check() == 2:
					if not ref._data.node_assined_display_layer == "defaultLayer":
						dl = M_Nodes.DisplayLayer(ref._data.node_assined_display_layer)
						dl.visibility.enable_Render_Layer_Overide()
						if self.ITEM_TYPE in [Beauty_Overides_Item.ITEM_TYPE, Matte_Overides_Item.ITEM_TYPE, Invisible_Overides_Item.ITEM_TYPE]:
							dl.visibility.value = 1
						else:
							dl.visibility.value = 0
	
########################################################################
class Beauty_Overides_Item(Overides_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Beauty_Overides_Item,self).__init__("Beauty",**kwargs)
	
########################################################################
class Matte_Overides_Item(Overides_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Matte_Overides_Item,self).__init__("Matte",**kwargs)

########################################################################
class Invisible_Overides_Item(Overides_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Invisible_Overides_Item,self).__init__("Invisible",**kwargs)

########################################################################
class Unassined_Overides_Item(Overides_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Unassined_Overides_Item,self).__init__("Unassined",**kwargs)
	
########################################################################
class Master_Assets_Item(Reference_Container_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Master_Assets_Item,self).__init__("Master Assets",**kwargs)

########################################################################
class Part_Set_Item(Vray_Object_Properties_Item):
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self,part,**kwargs):
		if part.__class__.__name__ == Yaml_Config_Data.Part_Set.__name__:
			isinstance(part, Yaml_Config_Data.Part_Set)
			if hasattr(part, "uid"):
				self.uid = part.uid
			else:
				self.uid = str(uuid.uuid4())
				
			if not hasattr(part, "_asset_assembly_ref"):
				self._asset_assembly_ref = None
			else:
				self._asset_assembly_ref = part._asset_assembly_ref
				
			if hasattr(part, "maya_node"):
				if part.maya_node != None:
					super(Part_Set_Item,self).__init__(part.maya_node,**kwargs)
				else:
					super(Part_Set_Item,self).__init__(part.name,**kwargs)
			else:
				super(Part_Set_Item,self).__init__(part.name,**kwargs)
				
		elif isinstance(part, Named_Data_Object):
			super(Part_Set_Item,self).__init__(part.name,**kwargs)
			self.uid = str(uuid.uuid4())
			self._asset_assembly_ref = None
		else:
			super(Part_Set_Item,self).__init__(part,**kwargs)
			self.uid = str(uuid.uuid4())
			self._asset_assembly_ref = None
		
		try:
			self._data.lockNode()
		except:
			print "Was Unable to lock %s " % self._data.name
		
	#----------------------------------------------------------------------
	def setData(self, value, role=Data_Roles.DISPLAY):
		""""""
		if role in self.Item_Data_Roles.DP_ED and _maya_check:
			if not value.endswith("_set"):
				part_set_value = value + "_set"
				display_layer_value =  value
			else:
				part_set_value = value
				display_layer_value =  value.replace("_set", "")
				
			link_dl = self.node_Get_Linked_Display_Layer()
			if link_dl is not None:
				link_dl.name =  display_layer_value
			self._data.unlockNode()
			self.node_name = part_set_value
			self._data.lockNode()
		else:
			return super(Part_Set_Item, self).setData(value, role)
	#----------------------------------------------------------------------
	def to_Yaml(self):
		""""""
		res = Yaml_Config_Data.Part_Set(name=self.data(), uid=self.uid, asset_assembly_ref=self._asset_assembly_ref)
		return res
	#----------------------------------------------------------------------
	def node_Get_Linked_Display_Layer(self):
		""""""
		link = self._data.Make_Plug("displayLayerLink")
		return link.value
		
########################################################################
class Asset_Item(Maya_Asset_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,asset,**kwargs):
		if kwargs.has_key("asset_parent"):
			parent = kwargs.pop("asset_parent")
		else:
			parent = None
		if isinstance(asset, Yaml_Config_Data.Asset):
			from_yaml = True
			if hasattr(asset, "maya_node"):
				super(Asset_Item,self).__init__(asset.maya_node,**kwargs)
			else:
				super(Asset_Item,self).__init__(asset.name,**kwargs)
				
		elif isinstance(asset, Named_Data_Object):
			from_yaml = False
			super(Asset_Item,self).__init__(asset.name,**kwargs)
		else:
			from_yaml = False
			super(Asset_Item,self).__init__(asset,**kwargs)
		
		if parent:
			parent.appendRow(self)
			
		if not from_yaml:
			self.Part_Sets      = Part_Sets_Item()
			self.Render_States  = Render_States_Item()
			self.appendRow(self.Part_Sets)
			self.appendRow(self.Render_States)
		else:
			self.from_Yaml(asset)
		if _maya_check:
			if not self._data.attributeExists("renderStates"):
				self.enum_render_states_plug = self._data.Add_Enum_Attribute("renderStates", ["Test"], remake=False)
			else:
				self.enum_render_states_plug = self._data.Make_Enum_Plug("renderStates")
				
	#----------------------------------------------------------------------
	def contextMenuActions(self, menu):
		action_selected_Set = QT.QAction(menu)
		action_selected_Set.setText("Add Selected To Container")
		action_selected_Set.triggered.connect(self.node_addSelectedNodes)
		menu.addAction(action_selected_Set)
		
		action_selected_members = QT.QAction(menu)
		action_selected_members.setText("Select All Descendents")
		action_selected_members.triggered.connect(self.node_select_All_Descendents)
		menu.addAction(action_selected_members)
		
		action_include_selected = QT.QAction(menu)
		action_include_selected.setText("Select Transform Descendents")
		action_include_selected.triggered.connect(self.node_select_Transform_Descendents)
		menu.addAction(action_include_selected)
		
		action_remove_selected = QT.QAction(menu)
		action_remove_selected.setText("Select Container Contents")
		action_remove_selected.triggered.connect(self.node_select_Container_Contents)
		menu.addAction(action_remove_selected)
				
	#----------------------------------------------------------------------
	def from_Yaml(self, asset):
		""""""
		top_levle_asset = self
		while not top_levle_asset.Parent.type() in [Assets_Item.ITEM_TYPE, File_Reference_Item.ITEM_TYPE]:
			top_levle_asset = top_levle_asset.Parent
		isinstance(asset, Yaml_Config_Data.Asset)
		self.Part_Sets      = Part_Sets_Item(yaml=asset.Part_Sets)
		self.insertRow(0, self.Part_Sets)
		
		self.Render_States  = Render_States_Item(yaml=asset.Render_States, part_sets=top_levle_asset.Part_Sets, asset_parent=self)
		self.insertRow(1, self.Render_States)
		
		for child_asset in  asset.Child_Assets:
			item = Asset_Item(child_asset, asset_parent=self)
			#self.appendRow(item)
			item.setColumnCount(2)
			plug = Enum_Plug_Item(item.enum_render_states_plug)
			self.setChild(item.row(), plug, column=1)
	#----------------------------------------------------------------------
	def to_Yaml(self):
		""""""
		part_sets     = self.Part_Sets.to_Yaml()
		top_asset = self
		if not top_asset.Parent.type() == Assets_Item.ITEM_TYPE:
			while top_asset.Parent.type() != Assets_Item.ITEM_TYPE:
				top_asset = top_asset.Parent
			top_parts = top_asset._master_part_sets
		else:
			self._master_part_sets = part_sets
			top_parts = part_sets
		
		render_states = self.Render_States.to_Yaml(top_parts.parts)
		assets        = [item.to_Yaml() for item in  self.Children if isinstance(item, Asset_Item)]
		res           = Yaml_Config_Data.Asset(name=self.data(), render_states=render_states, part_sets=part_sets, child_assets=assets)
		part_sets.parent = res
		render_states.parent = res
		return res
	#----------------------------------------------------------------------
	def Update_Enum_Render_States(self):
		if _maya_check:
			values = [child.data() for child in self.Render_States.Children]
			if len(values):
				self.enum_render_states_plug.set_Enums(values)
	#----------------------------------------------------------------------
	def set_Render_States_Plug_Overide(self, layer=None):
		if layer == None:
			layer = cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True )
		if layer != "defaultRenderLayer":
			self.enum_render_states_plug.enable_Render_Layer_Overide(layer)

	#----------------------------------------------------------------------
	def clear_Children_From_Render_Layer(self, layer=None):
		self._data.remove_All_Descendents_From_Render_Layer(layer)
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Item Reference Item Types
########################################################################
class Part_Set_Reference_Item(_Reference_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,item,**kwargs):
		super(Part_Set_Reference_Item,self).__init__(item,**kwargs)
		isinstance(self._data, Part_Set_Item)
	#----------------------------------------------------------------------
	def contextMenuActions(self, menu):
		action_selected_Set = QT.QAction(menu)
		action_selected_Set.setText("select Maya Node")
		action_selected_Set.triggered.connect(self._data.node_select_set)
		menu.addAction(action_selected_Set)
		
		action_selected_members = QT.QAction(menu)
		action_selected_members.setText("Select Maya Members")
		action_selected_members.triggered.connect(self._data.node_select_members)
		menu.addAction(action_selected_members)
		
		action_include_selected = QT.QAction(menu)
		action_include_selected.setText("Include Selected")
		action_include_selected.triggered.connect(self._data._data.include_Selected)
		menu.addAction(action_include_selected)
		
		action_remove_selected = QT.QAction(menu)
		action_remove_selected.setText("Remove Selected")
		action_remove_selected.triggered.connect(self._data._data.remove_selected)
		menu.addAction(action_remove_selected)
		
	#----------------------------------------------------------------------
	def get_Overide_assinment(self):
		""""""
		res = self.parent()
		isinstance(res, Reference_Container_Item)
		return res
	#----------------------------------------------------------------------
	def to_Yaml(self, parts):
		""""""
		for part in parts:
			isinstance(part,Yaml_Config_Data.Part_Set)
			if part.name == self.data():
				return part
		return None
########################################################################
class Master_Asset_Reference_Item(_Reference_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,item,**kwargs):
		super(Master_Asset_Reference_Item,self).__init__(item,**kwargs)
		isinstance(self._data, Asset_Item)
	#----------------------------------------------------------------------
	def data(self, role=Data_Roles.DISPLAY):
		if role == Data_Roles.DISPLAY:
			return self._data.parent().data()
		return self._data.data(role)

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Data Models 
########################################################################
class Vray_Scene_State_Manager_Item_Model(QStandardItemModel):
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		super(Vray_Scene_State_Manager_Item_Model,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def mimeData(self, indexes):
		super_data = super(Vray_Scene_State_Manager_Item_Model,self).mimeData(indexes)
		res = QT.DataModels.MimeData.Drag_And_Drop_MimeData(indexes, model=self, super_data=super_data)
		return res

	#----------------------------------------------------------------------
	def dropMimeData(self, data, action, row, column, parent):
		if isinstance(data, QT.DataModels.MimeData.Drag_And_Drop_MimeData):
			parentItem = self.itemFromIndex(parent)
			if not parent == None:
				if isinstance(data.drop_destination, (Beauty_Overide_View, Matte_Overide_View, Invisible_Overide_View, Part_Sets_List_View)):
					if isinstance(data.drag_source, (Beauty_Overide_View, Matte_Overide_View, Invisible_Overide_View, Part_Sets_List_View)):
						if parentItem.type() == Part_Set_Reference_Item.ITEM_TYPE:
							parentItem = parentItem.get_Overide_assinment()
						vscrollbar = data.drag_source.verticalScrollBar()
						sliderPos  = vscrollbar.value()
						cmd = Reparent_Items_Command(parentItem, data.items)
						data.drag_source.SelectionModel.clearSelection()
						undo_stack = self.parentWidget().window().undo_stack
						undo_stack.push(cmd)
						vscrollbar.setValue(sliderPos-len(data.items))
						data.drag_source.Model.sort()
						return True
				elif isinstance(data.drop_destination, Asset_Tree_View):
					if isinstance(data.drag_source, (Beauty_Overide_View, Matte_Overide_View, Invisible_Overide_View, Part_Sets_List_View)):
						if parentItem.type() == Asset_Item.ITEM_TYPE:
							isinstance(parentItem, Asset_Item)
							cmd = Move_Part_Set_Items_Command(parentItem, data.items)
							undo_stack = self.parentWidget().window().undo_stack
							undo_stack.push(cmd)
							return True
				elif isinstance(data.drop_destination, Render_States_List_View):
					if isinstance(data.drag_source, Render_States_List_View):
						if parentItem.type() == Render_State_Item.ITEM_TYPE:
							parentItem = parentItem.parent()
						cmd = Duplacate_Render_State_Command(data.items[0])
						undo_stack = self.parentWidget().window().undo_stack
						undo_stack.push(cmd)
						return True
			return False
		else:
			return False #res = super(Vray_Scene_State_Manager_Item_Model,self).dropMimeData(data, action, row, column, parent)
		return res

	#----------------------------------------------------------------------
	def run_Vray_States_Setup(self):
		parentItem           = self.invisibleRootItem()
		self.Assets          = Assets_Item()
		parentItem.appendRow(self.Assets)
		
	#----------------------------------------------------------------------	
	def to_Yaml_Object(self):
		""""""
		assets = self.Assets.to_Yaml()
		output = Yaml_Config_Data.Config_Data(assets=assets)
		assets.parent = output
		return output
	
	#----------------------------------------------------------------------
	def to_Yaml(self, file_path=None):
		""""""
		return yaml.dump(self.to_Yaml_Object())

	#----------------------------------------------------------------------
	def from_Yaml(self, file_path=None):
		""""""
		if _maya_check:
			data = Yaml_Config_Data.load_config_Script()
		else:
			data = Yaml_Config_Data.load_config_data_from_file(file_path)
			
		while self.Assets.RowCount:
			self.Assets.removeRow(0)
			
		self.Assets.from_Yaml()
		
	def scan_for_Master_Render_States(self):
		render_states_list = self.Assets.find_child_item_types(Render_States_Item.ITEM_TYPE)
		for render_states in  render_states_list:
			isinstance(render_states, Render_States_Item)
			scan = render_states.find_child_items("Default_Empty", recurive=False)
			if not len(scan):
				Render_State = Render_State_Item("Default_Empty")
				render_states.insertRow(0, Render_State)
				collected = []
				for child_ref in render_states.parent().find_child_item_types(Part_Set_Reference_Item.ITEM_TYPE):
					if not child_ref._data.data() in collected:
						collected.append(child_ref._data.data())
						ref = Part_Set_Reference_Item(child_ref._data)
						Render_State.Unassined.appendRow( ref )
				scan_item = render_states.find_child_items("Default_Empty", recurive=False)[0]
			else:
				scan_item = scan[0]
			isinstance(scan_item, Render_State_Item)
			if scan_item.Row != 0:
				row = scan_item.Row
				child = render_states.takeChild(row)
				render_states.removeRow(row)
				render_states.insertRow(0, child)
		
			
	#----------------------------------------------------------------------
	def from_Yaml_Object(self, data):
		""""""
		if data != None:
			self.setRowCount(0)
			self.Assets = Assets_Item(yaml=data.Assets)
			self.appendRow(self.Assets)
		self.scan_for_Master_Render_States()
	#----------------------------------------------------------------------
	def make_yaml_Data(self):
		return self.to_Yaml()
	
	#----------------------------------------------------------------------
	def load_temp_yaml_Data(self):
		data = Yaml_Config_Data.load_config_data("C:\yaml_temp\Temp.yaml")
		self.from_Yaml_Object(data)
		
	#----------------------------------------------------------------------
	def save_temp_yaml_Data(self):
		data = self.to_Yaml_Object()
		Yaml_Config_Data.save_config_data_to_file(data, "C:\yaml_temp\Temp.yaml")
########################################################################
class Vray_Scene_State_Viewer_Item_Model(QStandardItemModel):
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		super(Vray_Scene_State_Viewer_Item_Model,self).__init__(*args,**kwargs)
		self.setColumnCount(2)
		if _maya_check:
			self.run_setup()
	#----------------------------------------------------------------------	
	def run_setup(self):
		self.yaml_data_refs = Yaml_Config_Data.find_yaml_config_script_Refs()
		parentItem  = self.invisibleRootItem()
		self.File_References = _Named_Data_Item("File References")
		self.Render_Layers   = Render_Layers_Item()
		self.Master_Assets   = Master_Assets_Item()
		parentItem.appendRows([self.File_References, self.Render_Layers, self.Master_Assets])
		ref_items = []
		top_level_items = [item[1:] for item in cmds.ls( assemblies=True,objectsOnly=True,long=True)]
		for data in  self.yaml_data_refs:
			isinstance(data, Yaml_Config_Data.Config_Data)
			file_ref_item = File_Reference_Item(data)
			self.File_References.appendRow(file_ref_item)
			for asset in  file_ref_item.Children:
				isinstance(asset, Asset_Item)
				ref = Master_Asset_Reference_Item(asset)
				ref.setColumnCount(2)
				self.Master_Assets.appendRow(ref)
				plug = Enum_Plug_Item(asset.enum_render_states_plug)
				self.Master_Assets.setChild(ref.row(), plug, column=1)
				ref_items.extend([item for item in cmds.referenceQuery(ref._data._data.name,nodes=True,dagPath=True) if item in top_level_items])
		if Viewer_Version_check() == 2:
			self.run_update()
	#----------------------------------------------------------------------
	def run_update(self, full=False):
		""""""
		
		if full:
			for rl in Scripts.Global_Constants.Nodes.Render_Layers():
				cmds.editRenderLayerMembers(str(rl),cmds.editRenderLayerMembers(str(rl), query=True, fullNames=True) ,remove=True)
		if not cmds.objExists("Vray_Scene_States_Global_Render_Group"):
			master_node = M_Nodes.MNODE(cmds.group(name="Vray_Scene_States_Global_Render_Group", empty=True))
		else:
			master_node = M_Nodes.MNODE("Vray_Scene_States_Global_Render_Group")
		for rl in Scripts.Global_Constants.Nodes.Render_Layers():
			rl.addMembers([master_node])
			
	#----------------------------------------------------------------------
	def mimeData(self, indexes):
		super_data = super(Vray_Scene_State_Viewer_Item_Model,self).mimeData(indexes)
		res = QT.DataModels.MimeData.Drag_And_Drop_MimeData(indexes, model=self, super_data=super_data)
		return res
########################################################################
class Base_ProxyModel(QSortFilterProxyModel):
	def __init__(self,parent=None):
		super(Base_ProxyModel,self).__init__(parent)
	#----------------------------------------------------------------------
	def sourceModel(self):
		""""""
		res = super(Base_ProxyModel,self).sourceModel()
		isinstance(res,Vray_Scene_State_Manager_Item_Model)
		return res
########################################################################
class Asset_Item_Filter_ProxyModel(Base_ProxyModel):
	def __init__(self,parent=None):
		super(Asset_Item_Filter_ProxyModel,self).__init__(parent)
	#----------------------------------------------------------------------
	def filterAcceptsRow(self, sourceRow, sourceParent):
		if not sourceParent.isValid():
			return True
		parentItem = self.sourceModel().itemFromIndex(sourceParent)
		if parentItem.Type in [Assets_Item.ITEM_TYPE, File_Reference_Item.ITEM_TYPE]:
			return True
		if parentItem.child(sourceRow).Type == Asset_Item.ITEM_TYPE:
			return True		
		return False
	
########################################################################
class Master_Asset_Item_Filter_ProxyModel(Base_ProxyModel):
	def __init__(self,parent=None):
		super(Master_Asset_Item_Filter_ProxyModel,self).__init__(parent)
	#----------------------------------------------------------------------
	def filterAcceptsRow(self, sourceRow, sourceParent):
		if not sourceParent.isValid():
			return True
		parentItem = self.sourceModel().itemFromIndex(sourceParent)
		if parentItem.Type in [_Named_Data_Item.ITEM_TYPE, Assets_Item.ITEM_TYPE, File_Reference_Item.ITEM_TYPE]:
			return True
		if parentItem.Type in [File_Reference_Item.ITEM_TYPE]:
			if parentItem.child(sourceRow).Type == Asset_Item.ITEM_TYPE:
				return True
		return True
	
########################################################################
class Sorted_Item_Filter_ProxyModel(Base_ProxyModel):
	def __init__(self,parent=None):
		super(Sorted_Item_Filter_ProxyModel,self).__init__(parent)
		
	#----------------------------------------------------------------------
	def filterAcceptsRow(self, sourceRow, sourceParent):
		if not sourceParent.isValid():
			return True
		parentItem = self.sourceModel().itemFromIndex(sourceParent)
		if parentItem.child(sourceRow) is None:
			return False
		if parentItem.child(sourceRow).Type == Render_State_Item.ITEM_TYPE:
			if parentItem.child(sourceRow).data() == "Default_Empty":
				return False
		if parentItem.data() == "Render States":
			if self.sourceModel().parentWidget().Favorits_Only_checkBox.isChecked():
				if not parentItem.child(sourceRow).favorit:
					return False
			
			exp = self.filterRegExp()
			if exp.pattern() != "":
				if exp.exactMatch(parentItem.child(sourceRow).data()):
					return True
				else:
					return False
		return True
