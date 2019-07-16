import pymel.core as pm
import maya.cmds as cmds
import json
import itertools
from functools import partial


#----------------------------------------------------------------------
def flatten(x):
	result = []
	for el in x:
		if hasattr(el, "__iter__") and not isinstance(el, basestring):
			result.extend(flatten(el))
		else:
			result.append(el)
	return result

#----------------------------------------------------------------------
def get_unique_attribute_values(attribute_name):
	""""""
	atts = cmds.ls("*."+attribute_name)
	res = set()
	for att in atts:
		val = cmds.getAttr(att)
		if not val == None and len(val):
			for v in val.split(","):
				res.add(v)
	return list(res)

#----------------------------------------------------------------------
def get_Objects_With_Existing_Attribute(attribute_name):
	""""""
	res = []
	atts = cmds.ls("*."+attribute_name,long=True)
	for att in atts:
		node = att.split(".")[0]
		res.append(node)
	return res

#----------------------------------------------------------------------
def get_Objects_With_Attribute_Matching_Value(attr,value,nodes=[]):
	res = []
	if not len(nodes):
		atts = cmds.ls("*."+attr,long=True)
	else:
		atts = [node+"."+attr for node in cmds.ls(nodes,long=True)]
	for att in atts:
		try:
			val = cmds.getAttr(att)
			vals = val.split(",")
			for val in vals:
				if len(val):
					if str(value) == str(val):
						node = att.split(".")[0]
						res.append(node)
						break
		except ValueError:
			continue
	return res

class Honda_Tags(object):
	COMPONENTS          = "COMPONENT_SELECTION"
	VVP                 = "VVP_CATEGORY"
	CODE                = "CODE"
	TRIM                = "BodyStyleTrim"
	ANIM                = "ANIM_CATEGORY"
	SEAT_POSITION       = "SEAT_POSITION"
	SEAT_MOVEMENT       = "SEAT_MOVEMENT"
	WHEEL_ROTATION      = "WHEEL_ROTATION"

######################################################################## UTILTY LAMBDA FUNCTIONS
uuids_to_names                                    = lambda idlist:cmds.ls(idlist)
names_to_uuids                                    = lambda names:cmds.ls(names,uuid=True)
get_Node_Name                                     = lambda node:cmds.ls(cmds.ls(node))[0].split("|")[-1]
get_Node_Path                                     = lambda node:cmds.ls(node,l=True)[0]
get_Node_UUid                                     = lambda node:cmds.ls(node, uuid=True)[0]
get_Parent                                        = lambda node:none_To_List(cmds.listRelatives(node, parent=True, fullPath=True))
none_To_List                                      = lambda val:val if val is not None else []
get_All_Geometry_Descendents                      = lambda node:cmds.ls(cmds.listRelatives(node, allDescendents=True, path=True),geometry=True,l=True)
get_Parent                                        = lambda node:none_To_List(cmds.listRelatives(node, parent=True, fullPath=True))
#get_Honda_Component_Selection_Values              = partial(get_unique_attribute_values,Honda_Tags.COMPONENTS)
#get_Honda_Trim_Values                             = partial(get_unique_attribute_values,Honda_Tags.TRIM)
#get_Honda_Vic_Category_Values                     = partial(get_unique_attribute_values,Honda_Tags.VVP)
#get_Honda_Code_Values                             = partial(get_unique_attribute_values,Honda_Tags.CODE)
#get_Honda_Anim_Category_Values                    = partial(get_unique_attribute_values,Honda_Tags.ANIM)
#get_Honda_Seat_Position_Values                    = partial(get_unique_attribute_values,Honda_Tags.SEAT_POSITION)
#get_Honda_Seat_Movement_Values                    = partial(get_unique_attribute_values,Honda_Tags.SEAT_MOVEMENT)
#get_Honda_Wheel_Rotation_Values                   = partial(get_unique_attribute_values,Honda_Tags.WHEEL_ROTATION)


#get_Honda_Component_Selection_Nodes               = partial(get_Objects_With_Existing_Attribute,Honda_Tags.COMPONENTS)
#get_Honda_Trim_Nodes                              = partial(get_Objects_With_Existing_Attribute,Honda_Tags.TRIM)
#get_Honda_Vic_Category_Nodes                      = partial(get_Objects_With_Existing_Attribute,Honda_Tags.VVP)
#get_Honda_Code_Nodes                              = partial(get_Objects_With_Existing_Attribute,Honda_Tags.CODE)
#get_Honda_Anim_Category_Nodes                     = partial(get_Objects_With_Existing_Attribute,Honda_Tags.ANIM)
#get_Honda_Seat_Position_Nodes                     = partial(get_Objects_With_Existing_Attribute,Honda_Tags.SEAT_POSITION)
#get_Honda_Seat_Movement_Nodes                     = partial(get_Objects_With_Existing_Attribute,Honda_Tags.SEAT_MOVEMENT)
#get_Honda_Wheel_Rotation_Nodes                    = partial(get_Objects_With_Existing_Attribute,Honda_Tags.WHEEL_ROTATION)


#get_Honda_Nodes_For_Component_Selection           = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.COMPONENTS,val,nodes)
#get_Honda_Nodes_For_Trim                          = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.TRIM,val,nodes)
#get_Honda_Nodes_For_Vic_Category                  = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.VVP,val,nodes)
#get_Honda_Nodes_For_Code                          = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.CODE,val,nodes)
#get_Honda_Nodes_For_Anim_Category                 = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.ANIM,val,nodes)
#get_Honda_Nodes_For_Seat_Position                 = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.SEAT_POSITION,val,nodes)
#get_Honda_Nodes_For_Seat_Movement                 = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.SEAT_MOVEMENT,val,nodes)
#get_Honda_Nodes_For_Wheel_Rotation                = lambda val,nodes=[]:get_Objects_With_Attribute_Matching_Value(Honda_Tags.WHEEL_ROTATION,val,nodes)

#----------------------------------------------------------------------
def clear_AW_honda_Rebuild_Data():
	""""""
	for att in cmds.ls("*.hondaRebuildData"):
		cmds.deleteAttr(att)
#----------------------------------------------------------------------
def find_AW_honda_Rebuild_Data():
	""""""
	for att in cmds.ls("*.hondaRebuildData",long=True):
		return att.split(".")[0]
#----------------------------------------------------------------------
def has_AW_honda_Rebuild_Data(node):
	return cmds.attributeQuery( "hondaRebuildData",node=node, exists=True )
#----------------------------------------------------------------------
def add_AW_honda_Rebuild_Data(node):
	if not has_AW_honda_Rebuild_Data(node):
		cmds.addAttr(node, longName="hondaRebuildData",dt="string",shortName="hrbd",hidden=True)
#----------------------------------------------------------------------
def set_AW_honda_Rebuild_Data(node,val):
	if not has_AW_honda_Rebuild_Data(node):
		add_AW_honda_Rebuild_Data(node)
	cmds.setAttr(node+".hondaRebuildData", val, typ="string")
#----------------------------------------------------------------------
def get_AW_honda_Rebuild_Data(node):
	if has_AW_honda_Rebuild_Data(node):
		return cmds.getAttr(node+".hondaRebuildData")
	else:
		raise LookupError("{} does not have a honda Rebuild Data".format(node))

#----------------------------------------------------------------------
def has_AW_honda_ID(node):
	return cmds.attributeQuery( "hondaAssetId",node=node, exists=True )
#----------------------------------------------------------------------
def get_AW_honda_ID(node):
	if has_AW_honda_ID(node):
		return cmds.getAttr(node+".hondaAssetId")
	else:
		raise LookupError("{} does not have a honda Asset Id".format(node))
#----------------------------------------------------------------------
def add_AW_honda_ID(node):
	if not has_AW_honda_ID(node):
		cmds.addAttr(node, longName="hondaAssetId",attributeType="long",shortName="haid",hidden=True)
#----------------------------------------------------------------------
def set_AW_honda_ID(node,val):
	if not has_AW_honda_ID(node):
		add_AW_honda_ID(node)
	cmds.setAttr(node+".hondaAssetId", val)
#----------------------------------------------------------------------
def clear_AW_honda_ID():
	""""""
	for att in cmds.ls("*.hondaAssetId"):
		cmds.deleteAttr(att)
#----------------------------------------------------------------------
def nodes_To_Honda_IDs(nodes):
	return [get_AW_honda_ID(node) for node in cmds.ls(nodes)]

#----------------------------------------------------------------------
def honda_IDs_To_Nodes(ids,idDict):
	return cmds.ls([idDict[idnum] for idnum in ids],long=True)
#----------------------------------------------------------------------
def add_Honda_ID_Attribute_To_All_Objects():
	res = dict()
	for num,node in enumerate(cmds.ls(dagObjects=True, materials=True,long=True)):
		add_AW_honda_ID(node)
		set_AW_honda_ID(node,num)
		uuid = get_Node_UUid(node)
		res[num] = uuid
	return res
#----------------------------------------------------------------------
def build_Honda_Node_dicts():
	res = dict()
	for att in cmds.ls("*.hondaAssetId"):
		node = att.split(".")[0]
		val  = cmds.getAttr(att)
		uuid = get_Node_UUid(node)
		res[val]=uuid
	return res

#----------------------------------------------------------------------
def replace_Honda_Trim_Slashes_With_Underscores():
	""""""
	for att in cmds.ls("*."+Honda_Tags.TRIM):
		val = cmds.getAttr(att)
		val = val.replace("/","_")
		cmds.setAttr(att,val,typ="string")


########################################################################
class Base_Class(object):
	""""""
	HONDA_ID_To_Uuid_Dict = dict()
	
########################################################################
class Honda_Metadata_Nodes_And_Values(Base_Class):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,data):
		""""""
		if isinstance(data,str):
			self.attrTag     = data
			self.values      = get_unique_attribute_values(self.attrTag)
			self.nodes       = get_Objects_With_Existing_Attribute(self.attrTag)
			self.collections = self._build_collections()
		elif isinstance(data,dict):
			self.attrTag = data["attrTag"]
			self.values = data["values"]
			self.nodes = data["nodes"]
			if len(self.nodes):
				if isinstance(self.nodes[0],int):
					self.nodes = honda_IDs_To_Nodes(self.nodes, self.HONDA_ID_To_Uuid_Dict)
			self.collections = self._load_collections(data["collections"])
	#----------------------------------------------------------------------
	def _build_collections(self):
		res = []
		for value in self.values:
			nodes = get_Objects_With_Attribute_Matching_Value(self.attrTag,value,self.nodes)
			res.append(Honda_Metadata_Tag_Collection([value,nodes]))
		return res
	#----------------------------------------------------------------------
	def _load_collections(self,data):
		res = []
		for collection in data: 
			res.append(Honda_Metadata_Tag_Collection(collection))
		return res
	#----------------------------------------------------------------------
	def to_dict(self):
		ids = nodes_To_Honda_IDs(self.nodes)
		collections = [item.to_dict() for item in self.collections]
		return dict(attrTag=self.attrTag,values=self.values,nodes=ids,collections=collections)

########################################################################
class Honda_Metadata_Tag_Collection(Base_Class):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,data):
		if isinstance(data,list):
			self.tag    = data[0]
			self.nodes  = data[1]
		elif isinstance(data,dict):
			self.tag    = data["tag"]
			self.nodes  = data["nodes"]
			
		if len(self.nodes):
			if isinstance(self.nodes[0],int):
				self.nodes = honda_IDs_To_Nodes(self.nodes, self.HONDA_ID_To_Uuid_Dict)
			
	#----------------------------------------------------------------------
	def to_dict(self):
		ids = nodes_To_Honda_IDs(self.nodes)
		return dict(tag=self.tag,nodes=ids)


########################################################################
class Honda_Display_Layer_Node(object):
	""""""

	def __init__(self,node):
		"""Constructor"""
		self.node = node
	#----------------------------------------------------------------------
	@property
	def name(self):
		"""Constructor"""
		return self.node.split("|")[-1]
	#----------------------------------------------------------------------
	@property
	def display_layer_name(self):
		""""""
		return "DL_" + self.name
	#----------------------------------------------------------------------
	@property
	def part_set_name(self):
		""""""
		return self.display_layer_name + "_set"
	#----------------------------------------------------------------------
	def create_Display_Layer(self):
		""""""
		if not cmds.objExists(self.display_layer_name):
			cmds.createDisplayLayer( self.get_Geo_Transforms_From_Nodes(), name=self.display_layer_name)
	#----------------------------------------------------------------------
	def display_Layer_Has_Part_Set(self):
		""""""
		return cmds.objExists(self.part_set_name)
	#----------------------------------------------------------------------
	def get_Geo_Transforms_From_Nodes(self):
		""""""
		geo = get_All_Geometry_Descendents(self.node)
		trasnforms = get_Parent(geo)
		return trasnforms
	#----------------------------------------------------------------------
	def __repr__(self):
		""""""
		return self.node
	#----------------------------------------------------------------------
	def __str__(self):
		""""""
		return self.node
########################################################################
class Honda_Metadata_Trim_Nodes_And_Values(Honda_Metadata_Nodes_And_Values):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,data):
		""""""
		super(Honda_Metadata_Trim_Nodes_And_Values, self).__init__(data)
		self.nodes       = [Honda_Display_Layer_Node(node) for node in self.nodes]
	#----------------------------------------------------------------------
	def _build_collections(self):
		res = []
		for value in self.values:
			nodes = get_Objects_With_Attribute_Matching_Value(self.attrTag,value,self.nodes)
			res.append(Honda_Metadata_Trim_Collection([value,nodes]))
		return res
	#----------------------------------------------------------------------
	def _load_collections(self,data):
		res = []
		for collection in data: 
			res.append(Honda_Metadata_Trim_Collection(collection))
		return res
	
	#----------------------------------------------------------------------
	def create_Display_Layers(self):
		""""""
		for node in self.nodes:
			node.create_Display_Layer()

	
########################################################################
class Honda_Metadata_Trim_Collection(Honda_Metadata_Tag_Collection):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,data):
		super(Honda_Metadata_Trim_Collection, self).__init__(data)
		self.nodes = [Honda_Display_Layer_Node(node) for node in self.nodes] 
	#----------------------------------------------------------------------
	@property
	def eim_name(self):
		""""""
		return self.tag
	#----------------------------------------------------------------------
	def get_Assigned_Display_Layers(self):
		return [item.display_layer_name for item in self.nodes]
########################################################################
class Honda_Metadata(Base_Class):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		"""Constructor"""
		self.component      = Honda_Metadata_Nodes_And_Values(kwargs.get("component",Honda_Tags.COMPONENTS))
		self.trims          = Honda_Metadata_Trim_Nodes_And_Values(kwargs.get("trims",Honda_Tags.TRIM))
		self.vvp            = Honda_Metadata_Nodes_And_Values(kwargs.get("vvp",Honda_Tags.VVP))
		self.codes          = Honda_Metadata_Nodes_And_Values(kwargs.get("codes",Honda_Tags.CODE))
		self.anim           = Honda_Metadata_Nodes_And_Values(kwargs.get("anim",Honda_Tags.ANIM))
		self.seat_position  = Honda_Metadata_Nodes_And_Values(kwargs.get("seat_position",Honda_Tags.SEAT_POSITION))
		self.seat_movement  = Honda_Metadata_Nodes_And_Values(kwargs.get("seat_movement",Honda_Tags.SEAT_MOVEMENT))
		self.wheel_rotation = Honda_Metadata_Nodes_And_Values(kwargs.get("wheel_rotation",Honda_Tags.WHEEL_ROTATION))
	#----------------------------------------------------------------------
	def to_dict(self):
		res = dict()
		res["component"]=self.component.to_dict()
		res["trims"]=self.trims.to_dict()
		res["vvp"]=self.vvp.to_dict()
		res["codes"]=self.codes.to_dict()
		res["anim"]=self.anim.to_dict()
		res["seat_position"]=self.seat_position.to_dict()
		res["seat_movement"]=self.seat_movement.to_dict()
		res["wheel_rotation"]=self.wheel_rotation.to_dict()
		return res
	#----------------------------------------------------------------------
	def to_json(self):
		""""""
		obj = self.to_dict()
		return json.dumps(obj)
		
#----------------------------------------------------------------------
def Store_Honda_MetaData(node):
	""""""
	clear_AW_honda_Rebuild_Data()
	replace_Honda_Trim_Slashes_With_Underscores()
	Base_Class.HONDA_ID_To_Uuid_Dict = add_Honda_ID_Attribute_To_All_Objects()
	honda_metadata = Honda_Metadata()
	json_data = honda_metadata.to_json()
	add_AW_honda_Rebuild_Data(node)
	set_AW_honda_Rebuild_Data(node, json_data)
	
#----------------------------------------------------------------------
def build_Honda_MetaData():
	""""""
	node = find_AW_honda_Rebuild_Data()
	json_string = get_AW_honda_Rebuild_Data(node)
	json_data = json.loads(json_string)
	Base_Class.HONDA_ID_To_Uuid_Dict = build_Honda_Node_dicts()
	honda_metadata = Honda_Metadata(**json_data)
	return honda_metadata 
	