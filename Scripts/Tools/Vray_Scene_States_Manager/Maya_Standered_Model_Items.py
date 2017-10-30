#speak = QtCore.Signal((int,), (str,))
import os
import yaml
import Yaml_Config_Data

import QT
import QT.DataModels.Qt_Roles_And_Enums
import QT.DataModels.QStandardItemModel
import QT.DataModels.QSortFilterProxyModel
import QT.DataModels.QStandardItem
import QT.DataModels.MimeData

Qt       = QT.Qt
QtSlot   = QT.QtSlot
QtSignal = QT.QtSignal
QtCore   = QT.QtCore
QtGui    = QT.QtGui
uic      = QT.uic

QStandardItemModel    = QT.DataModels.QStandardItemModel.QStandardItemModel
try:
	_maya_check = True
	import Scripts.NodeCls.M_Nodes
	import maya.cmds as cmds
	M_Nodes              = Scripts.NodeCls.M_Nodes
	Container            = M_Nodes.Container
	Script_Node          = M_Nodes.Script_Node
	SelectionSet         = M_Nodes.SelectionSet
	VRayObjectProperties = M_Nodes.VRayObjectProperties

except:
	_maya_check = False

########################################################################
class Data_Roles(QT.DataModels.Qt_Roles_And_Enums.Standered_Item_Data_Roles):
	ITEM           = QT.userRole_counter()
	DATA_OBJECT    = QT.userRole_counter()

#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Utility Functions
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
########################################################################
class Named_Data_Object(object):
	""""""
	def __init__(self,name,**kwargs):
		self.name = name
	def __str__(self):
		return str(self.name)

	def __repr__(self):
		return str(self.name)

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
		if role == Data_Roles.ITEM:
			return self
		return super(_Base_Item, self).data(role)
	
	#----------------------------------------------------------------------
	@property
	def asset_item_count(self):
		""""""
		res = len([item for item in self.Model.findItems(text="*",flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchWildcard,column=0) if item.type() == Asset_Item.ITEM_TYPE])
		return res
	#----------------------------------------------------------------------
	@property
	def render_state_count(self):
		""""""
		res = len([item for item in self.Model.findItems(text="*",flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchWildcard,column=0) if item.type() == Render_State_Item.ITEM_TYPE])
		return res
	#----------------------------------------------------------------------
	@property
	def part_sets_count(self):
		""""""
		res = len([item for item in self.Model.findItems(text="*",flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchWildcard,column=0) if item.type() == Part_Set_Item.ITEM_TYPE])
		return res	
	#----------------------------------------------------------------------
	def find_Part_Sets_By_Name(self, name):
		""""""
		res = [item for item in self.model().findItems(text=name,flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchExactly,column=0) if item.type() == Part_Set_Item.ITEM_TYPE]
		return res
	#----------------------------------------------------------------------
	def find_Render_States_By_Name(self, name):
		""""""
		res = [item for item in self.model().findItems(text=name,flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchExactly,column=0) if item.type() == Render_State_Item.ITEM_TYPE]
		return res
	#----------------------------------------------------------------------
	def find_Render_States_By_asset_assembly_ref(self, ref_id,ref_type):
		""""""
		res = [item for item in self.model().findItems(text="*",flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchWildcard,column=0) if item.type() == Render_State_Item.ITEM_TYPE]
		res = [item for item in res if item.asset_assembly_ref_id == ref_id and item.asset_assembly_ref_type == ref_type]
		return res
	#----------------------------------------------------------------------
	def find_Part_Set_Refs_By_Name(self, name):
		""""""
		res = [item for item in self.model().findItems(text=name,flags=Qt.MatchFlag.MatchRecursive|Qt.MatchFlag.MatchExactly,column=0) if item.type() == Part_Set_Reference_Item.ITEM_TYPE]
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
				name = M_Nodes.VRayObjectProperties(name)
		super(Vray_Object_Properties_Item, self).__init__(name, **kwargs)
		if _maya_check:
			if isinstance(self._data, M_Nodes.VRayObjectProperties):
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
				self.node_plug_reflectionAmount       = self._data._reflectionAmount_plug
				self.node_plug_refractionAmount       = self._data._refractionAmount_plug
	

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
			item = Asset_Item(asset)
			self.appendRow(item)

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
			self.setChild(0, 0, self.Unassined)
			self.setChild(1, 0, self.Matte)
			self.setChild(2, 0, self.Invisible)
			self.setChild(3, 0, self.Beauty)
		else:
			self.from_Yaml(render_state, part_sets)
	#----------------------------------------------------------------------
	def to_Yaml(self, parts):
		""""""
		name         = self.data()
		Unassined    = self.Unassined.to_Yaml(parts)
		Matte        = self.Matte.to_Yaml(parts)
		Invisible    = self.Invisible.to_Yaml(parts)
		Beauty       = self.Beauty.to_Yaml(parts)
		render_state = Yaml_Config_Data.Render_State(name=name, Unassined=Unassined, Matte=Matte, Invisible=Invisible, Beauty=Beauty)
		
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
		
		self.setChild(0, 0, self.Unassined)
		self.setChild(1, 0, self.Matte)
		self.setChild(2, 0, self.Invisible)
		self.setChild(3, 0, self.Beauty)
		
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
class Beauty_Overides_Item(Reference_Container_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Beauty_Overides_Item,self).__init__("Beauty",**kwargs)
	#----------------------------------------------------------------------
	def to_Yaml(self,parts):
		""""""
		container = Yaml_Config_Data.Beauty_Overides()
		return super(Beauty_Overides_Item, self).to_Yaml(container, parts)
	
########################################################################
class Matte_Overides_Item(Reference_Container_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Matte_Overides_Item,self).__init__("Matte",**kwargs)

	#----------------------------------------------------------------------
	def to_Yaml(self,parts):
		""""""
		container = Yaml_Config_Data.Matte_Overides()
		return super(Matte_Overides_Item, self).to_Yaml(container, parts)
########################################################################
class Invisible_Overides_Item(Reference_Container_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Invisible_Overides_Item,self).__init__("Invisible",**kwargs)

	#----------------------------------------------------------------------
	def to_Yaml(self,parts):
		""""""
		container = Yaml_Config_Data.Invisible_Overides()
		return super(Invisible_Overides_Item, self).to_Yaml(container, parts)
########################################################################
class Unassined_Overides_Item(Reference_Container_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Unassined_Overides_Item,self).__init__("Unassined",**kwargs)
		
	#----------------------------------------------------------------------
	def to_Yaml(self,parts):
		""""""
		container = Yaml_Config_Data.Unassined_Overides()
		return super(Unassined_Overides_Item, self).to_Yaml(container, parts)
########################################################################
class Part_Set_Item(Vray_Object_Properties_Item):
	ITEM_TYPE  = QT.user_type_counter()
	def __init__(self,part,**kwargs):
		if part.__class__.__name__ == Yaml_Config_Data.Part_Set.__name__:
			name = part.name
		elif isinstance(part, Named_Data_Object):
			name = part.name
		else:
			name = part
		super(Part_Set_Item,self).__init__(name,**kwargs)
			
	#----------------------------------------------------------------------
	def to_Yaml(self):
		""""""
		res = Yaml_Config_Data.Part_Set(self.data())
		return res
########################################################################
class Asset_Item(Maya_Asset_Item):
	ITEM_TYPE  = QT.user_type_counter()
	#----------------------------------------------------------------------
	def __init__(self,asset,**kwargs):
		if isinstance(asset, Yaml_Config_Data.yaml.YAMLObject):
			from_yaml = True
			super(Asset_Item,self).__init__(asset.name,**kwargs)
		elif isinstance(asset, Named_Data_Object):
			from_yaml = False
			super(Asset_Item,self).__init__(asset.name,**kwargs)
		else:
			from_yaml = False
			super(Asset_Item,self).__init__(asset,**kwargs)
		
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
	def from_Yaml(self, asset):
		""""""
		isinstance(asset, Yaml_Config_Data.Asset)
		self.Part_Sets      = Part_Sets_Item(yaml=asset.Part_Sets)
		self.appendRow(self.Part_Sets)
		
		self.Render_States  = Render_States_Item(yaml=asset.Render_States, part_sets=self.Part_Sets)
		self.appendRow(self.Render_States)
		
		for child_asset in  asset.Child_Assets:
			item = Asset_Item(child_asset)
			self.appendRow(item)
	
	#----------------------------------------------------------------------
	def to_Yaml(self):
		""""""
		part_sets     = self.Part_Sets.to_Yaml()
		render_states = self.Render_States.to_Yaml(part_sets.parts)
		assets        = [item.to_Yaml() for item in  self.Children if isinstance(item, Asset_Item)]
		res           = Yaml_Config_Data.Asset(name=self.data(), render_states=render_states, part_sets=part_sets, child_assets=assets)
		part_sets.parent = res
		render_states.parent = res
		return res
	def Update_Enum_Render_States(self):
		if _maya_check:
			values = [child.data() for child in self.Render_States.Children]
			self.enum_render_states_plug.set_Enums(values)
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
		action_selected_Set = QtGui.QAction(menu)
		action_selected_Set.setText("select Maya Node")
		action_selected_Set.triggered.connect(self._data.node_select_set)
		menu.addAction(action_selected_Set)
		
		action_selected_members = QtGui.QAction(menu)
		action_selected_members.setText("Select Maya Members")
		action_selected_members.triggered.connect(self._data.node_select_members)
		menu.addAction(action_selected_members)
		
		action_include_selected = QtGui.QAction(menu)
		action_include_selected.setText("Include Selected")
		action_include_selected.triggered.connect(self._data._data.include_Selected)
		menu.addAction(action_include_selected)
		
		action_remove_selected = QtGui.QAction(menu)
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
class Standard_Item_Model(QStandardItemModel):
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		super(Standard_Item_Model,self).__init__(*args,**kwargs)
		
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
		
		
	#----------------------------------------------------------------------
	def from_Yaml_Object(self, data):
		""""""
		if data != None:
			self.setRowCount(0)
			self.Assets = Assets_Item(yaml=data.Assets)
			self.appendRow(self.Assets)
	
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
						
					
								
