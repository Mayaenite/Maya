import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.api.OpenMaya as newOM
import math, sys
import helpers
from itertools import count

MFn = OpenMaya.MFn

"""
cmds.file(new=True,f=True)
cmds.unloadPlugin("AW_Scene_State_Manager",f=True)
cmds.loadPlugin("C:/Users/dloveridge/SkyDrive/SYSENV_V2/Maya/plug-ins/AW_Scene_State_Manager/AW_Scene_State_Manager.py")


# Create A Scene State Manager
StateManager         = cmds.awSceneState()

# Add Scene States
default_state        = cmds.awSceneState(edit=True,sceneStateManager=StateManager,addState=True)
bob_state            = cmds.awSceneState(edit=True, sceneStateManager=StateManager,addState=True,name="Bob")
john_state           = cmds.awSceneState(edit=True, sceneStateManager=StateManager,addState=True,name="John")
multi_state_creation = cmds.awSceneState(edit=True,sceneStateManager=StateManager,addState=True,state=["Car","Truck","Van"])

# Remove Scene States
cmds.awSceneState(edit=True,sceneStateManager=StateManager,removeState=True,state=[default_state])
cmds.awSceneState(edit=True,sceneStateManager=StateManager,removeState=True,state=multi_state_creation)

# Add Vray ObjectProperties aka(Part Sets)
default_part        = cmds.awSceneState(edit=True,sceneStateManager=StateManager,addPart=True)
multi_part_creation = cmds.awSceneState(edit=True,sceneStateManager=StateManager,addPart=True,part=["Car_Part","Truck_Parts","Van_Parts"])

# Assine Vray ObjectProperties aka(Part Sets) To The Diffent State Types Of A bob_state To Move Them Around
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, beauty=True,    state=bob_state, part=[default_part])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, invisible=True, state=bob_state, part=[default_part])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, matte=True,     state=bob_state, part=[default_part])

# Assine Vray ObjectProperties aka(Part Sets) To The Diffent State Types Of A john_state To Move Them Around
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, beauty=True,    state=john_state, part=[default_part])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, invisible=True, state=john_state, part=[default_part])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, matte=True,     state=john_state, part=[default_part])

cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, beauty=True, state=bob_state, part=multi_part_creation)

cmds.awSceneState(edit=True, sceneStateManager=StateManager, assinePart=True, beauty=True, state=john_state, part=multi_part_creation)

StateManager         = cmds.awSceneState()
bob_state            = cmds.awSceneState(edit=True, sceneStateManager=StateManager,addState=True,name="Bob")
default_part        = cmds.awSceneState(edit=True,sceneStateManager=StateManager,addPart=True)
default_part2        = cmds.awSceneState(edit=True,sceneStateManager=StateManager,addPart=True)
trans,shap = cmds.polyCube(w=1,h=1,d=1,sx=1,sy=1,sz=1,ax=[0,1,0],cuv=4,ch=1)
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assineNodes=True, part=default_part, node=["pCube1","pCube2","pCube3"])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assineNodes=True, part=default_part2, node=["pCube1","pCube2","pCube3"])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assineNodes=True, part=default_part, node=["pCube1"])
cmds.awSceneState(edit=True, sceneStateManager=StateManager, assineNodes=True, part=default_part2, node=["pCube1"])
"""

########################################################################
class Counter(object):
	#----------------------------------------------------------------------
	def __init__(self,start=1):
		self.num = count(start)
	#----------------------------------------------------------------------
	def __call__(self):
		return next(self.num)

plugin_id_counter = Counter(0x00001)

class NMSG(object):
	ConnectionMade    = OpenMaya.MNodeMessage.kConnectionMade
	ConnectionBroken  = OpenMaya.MNodeMessage.kConnectionBroken
	Att_Eval          = OpenMaya.MNodeMessage.kAttributeEval
	Att_Set           = OpenMaya.MNodeMessage.kAttributeSet
	Att_Locked        = OpenMaya.MNodeMessage.kAttributeLocked
	Att_Unlocked      = OpenMaya.MNodeMessage.kAttributeUnlocked
	Att_Added         = OpenMaya.MNodeMessage.kAttributeAdded
	Att_Removed       = OpenMaya.MNodeMessage.kAttributeRemoved
	Att_Renamed       = OpenMaya.MNodeMessage.kAttributeRenamed
	Att_Keyable       = OpenMaya.MNodeMessage.kAttributeKeyable
	Att_Unkeyable     = OpenMaya.MNodeMessage.kAttributeUnkeyable
	Array_Added       = OpenMaya.MNodeMessage.kAttributeArrayAdded
	Array_Removed     = OpenMaya.MNodeMessage.kAttributeArrayRemoved
	IncomingDirection = OpenMaya.MNodeMessage.kIncomingDirection
	OtherPlugSet      = OpenMaya.MNodeMessage.kOtherPlugSet


	Key_ChangeInvalid = OpenMaya.MNodeMessage.kKeyChangeInvalid
	Make_Keyable      = OpenMaya.MNodeMessage.kMakeKeyable
	Make_Unkeyable    = OpenMaya.MNodeMessage.kMakeUnkeyable

G_dependFn  = OpenMaya.MFnDependencyNode()
G_fnSet     = OpenMaya.MFnSet()

#----------------------------------------------------------------------
def Attribute_Changed_Callback(msg,plg,otherplg,data):
	isinstance(data, OpenMaya.MObject)
	isinstance(plg, OpenMaya.MPlug)
	isinstance(otherplg, OpenMaya.MPlug)

	name      , partialName       = plg.name(), plg.partialName()
	other_name, other_partialName = otherplg.name(), otherplg.partialName()
	message   = ""
	change_type = ""
	extra = ""
	
	if msg & NMSG.ConnectionBroken or msg & NMSG.ConnectionMade or msg & NMSG.OtherPlugSet:

		G_dependFn.setObject(otherplg.node())

		other_node_name = G_dependFn.name()
		
		message = "Change Type :%s: <'%s'> %s <'%s'>"

		if msg & NMSG.ConnectionBroken:
			change_type = "Connection Broken"
			extra = "Disconnected from"
			message = message % (change_type, name, extra, other_name)
		elif msg & NMSG.ConnectionMade:
			extra = "Connected To"
			change_type = "Connection Made"
			message = message % (change_type, name, extra, other_name)

		elif msg & NMSG.OtherPlugSet:
			change_type = "OtherPlugSet"
			message = message % (change_type, name, extra, other_name)

	elif msg & NMSG.Att_Added or msg & NMSG.Att_Removed or msg & NMSG.Att_Eval or msg & NMSG.Att_Set or msg & NMSG.Att_Locked or msg & NMSG.Att_Unlocked or msg & NMSG.Att_Unkeyable or msg & NMSG.Att_Keyable or msg & NMSG.Att_Renamed or msg & NMSG.Att_Added or msg & NMSG.Array_Added or msg & NMSG.Array_Removed or msg & NMSG.Make_Keyable or msg & NMSG.Make_Unkeyable:

		G_dependFn.setObject(plg.node())

		node_name = G_dependFn.name()

		message = "Change Type :%s:\n\tAttribute :%s:"

		if msg & NMSG.Att_Added or msg & NMSG.Att_Removed or msg & NMSG.Att_Eval or msg & NMSG.Att_Set or msg & NMSG.Att_Locked or msg & NMSG.Att_Unlocked or msg & NMSG.Att_Unkeyable or msg & NMSG.Att_Keyable or msg & NMSG.Att_Renamed:

			if msg & NMSG.Att_Added:
				change_type = "Added"

			elif msg & NMSG.Att_Removed:
				change_type = "Removed"

			elif msg & NMSG.Att_Eval:
				change_type = "Eval"

			elif msg & NMSG.Att_Set:
				change_type = "Set"

			elif msg & NMSG.Att_Locked:
				change_type = "Locked"

			elif msg & NMSG.Att_Unlocked:
				change_type = "UnLocked"

			elif msg & NMSG.Att_keyable:
				change_type = "Keyable"

			elif msg & NMSG.Att_Unkeyable:
				change_type = "Unkeyable"

			message = message % (change_type, name)

		elif msg & NMSG.Array_Added or msg & NMSG.Array_Removed:

			if msg & NMSG.Array_Added:
				change_type = "Array Added"

			elif msg & NMSG.Array_Removed:
				change_type = "Array Removed"

			message = message % (change_type, name)

		elif msg & NMSG.Make_Keyable or msg & NMSG.Make_Unkeyable:
			if msg & NMSG.Make_Keyable:
				change_type = "Keyable"

			elif msg & NMSG.Make_Unkeyable:
				change_type = "Unkeyable"

			message = message % (change_type, name)

	if not message == "" and not change_type == "":
		print(message)
#----------------------------------------------------------------------
def is_Old_API(obj):
	""""""
	return obj.__class__.__module__ == 'maya.OpenMaya'

#----------------------------------------------------------------------
def _isValidMObjectHandle(obj):
	if isinstance(obj, OpenMaya.MObjectHandle) :
		return obj.isValid() and obj.isAlive()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMObject(obj):
	if isinstance(obj, OpenMaya.MObject) :
		return not obj.isNull()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMPlug(obj):
	if isinstance(obj, OpenMaya.MPlug) :
		return not obj.isNull()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagPath(obj):
	if isinstance(obj, OpenMaya.MDagPath) :
		# when the underlying MObject is no longer valid, dag.isValid() will still return true,
		# but obj.fullPathName() will be an empty string
		return obj.isValid() and obj.fullPathName()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMNode(obj):
	if _isValidMObject(obj) :
		return obj.hasFn(MFn.kDependencyNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagNode(obj):
	if _isValidMObject(obj) :
		return obj.hasFn(MFn.kDagNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValidMNodeOrPlug(obj):
	return _isValidMPlug(obj) or _isValidMNode (obj)
#----------------------------------------------------------------------
def to_New_MObject(nodeName, force_Depend=False):
	""" Get the API MObject given the name of an existing node """
	if not isinstance(nodeName, str):
		raise ValueError("nodeName must be a string Repersenting the name of an MObject")
	else:
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = newOM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( nodeName )
		try :
			# ASSINE THE FIRST SELECTED ITEM
			obj = sel.getDependNode(0)
		except :
			raise LookupError("Could Not get DependNode That Matched %s" % nodeName)
		
		if force_Depend:
			return obj
		
		if obj.hasFn(MFn.kDagNode):
			# ASSINE THE FIRST SELECTED ITEM
			obj = sel.getDagPath(0)
		return obj
#----------------------------------------------------------------------
def to_Old_MObject(nodeName, force_Depend=False):
	""" Get the API MObject given the name of an existing node """
	if not isinstance(nodeName, str):
		raise ValueError("nodeName must be a string Repersenting the name of an MObject")
	else:
		# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
		obj = OpenMaya.MObject()
		
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = OpenMaya.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( nodeName )
		try :
			# ASSINE THE FIRST SELECTED ITEM
			sel.getDependNode( 0, obj )
		except :
			raise LookupError("Could Not get DependNode That Matched %s" % nodeName)
		
		if force_Depend:
			return obj
		
		if obj.hasFn(MFn.kDagNode):
			
			obj = OpenMaya.MDagPath()
			# ASSINE THE FIRST SELECTED ITEM
			sel.getDagPath( 0, obj )
		return obj
#----------------------------------------------------------------------
def to_New_MPlug(obj, plug_name):
	plg = None
	
	if isinstance(obj, str):
		obj = to_New_MObject(obj)
	else:
		obj = Convert_MObject(obj, force_new=True)
	if isinstance(plug_name, str):
		if obj.hasFn(MFn.kDagNode):
			obj = obj.node()
		fn = newOM.MFnDependencyNode(obj)
		# Check If The Attribute Exists On The MObject
		if not fn.hasAttribute(plug_name):
			raise ValueError("The MObject %s has not attribute %s" % (fn.name(), plug_name))
	
		# Get The Attribute MObject
		plg = fn.attribute(plug_name)
	else:
		plg = plug_name
		
	# Get The MPlug From The obj MObject and plg_obj MObject
	plg    = newOM.MPlug(obj, plg)
	
	return plg
#----------------------------------------------------------------------
def to_Old_MPlug(obj, plug_name):
	plg = None
	
	if isinstance(obj, str):
		obj = to_Old_MObject(obj)
	else:
		obj = Convert_MObject(obj, force_old=True)
	if isinstance(plug_name, str):
		if obj.hasFn(MFn.kDagNode):
			obj = obj.node()
		fn = OpenMaya.MFnDependencyNode(obj)
		# Check If The Attribute Exists On The MObject
		if not fn.hasAttribute(plug_name):
			raise ValueError("The MObject %s has not attribute %s" % (fn.name(), plug_name))
	
		# Get The Attribute MObject
		plg = fn.attribute(plug_name)
	else:
		plg = plug_name
		
	# Get The MPlug From The obj MObject and plg_obj MObject
	plg    = OpenMaya.MPlug(obj, plg)
	
	return plg
#----------------------------------------------------------------------
def Convert_MObject(obj, force_old=False, force_new=False):
	if is_Old_API(obj):
		if force_old:
			return obj
		if obj.hasFn(MFn.kDagNode):
			fn = OpenMaya.MFnDagNode(obj)
			res = to_New_MObject(fn.fullPathName())
		else:
			fn = OpenMaya.MFnDependencyNode(obj)
			res = to_New_MObject(fn.name())
	else:
		if force_new:
			return obj		
		if obj.hasFn(MFn.kDagNode):
			fn = newOM.MFnDagNode(obj)
			res = to_Old_MObject(fn.fullPathName())
		else:
			fn = newOM.MFnDependencyNode(obj)
			res = to_Old_MObject(fn.name())
	return res
#----------------------------------------------------------------------
def Convert_MPlug(plug, force_old=False, force_new=False):
	node = plug.node()
	isinstance(plug, OpenMaya.MPlug)
	index = None
	if is_Old_API(plug):
		if plug.isElement():
			index = plug.logicalIndex()
		if force_old:
			return plug
		if node.hasFn(MFn.kDagNode):
			fn = OpenMaya.MFnDagNode(node)
			res = to_New_MPlug(fn.fullPathName(), plug.partialName())
		else:
			fn = OpenMaya.MFnDependencyNode(node)
			res = to_New_MPlug(fn.name(), plug.partialName())
	else:
		if plug.isElement:
			index = plug.logicalIndex()		
		if force_new:
			return plug
		if node.hasFn(MFn.kDagNode):
			fn = newOM.MFnDagNode(node)
			res = to_Old_MPlug(fn.fullPathName(), plug.partialName())
		else:
			fn = newOM.MFnDependencyNode(node)
			res = to_Old_MPlug(fn.name(), plug.partialName())
	if index is not None:
		res = res.elementByLogicalIndex(index)
	return res
#----------------------------------------------------------------------
def get_Connected_Plugs(plug_name, obj=None, asDst=True, asSrc=False):
	if isinstance(plug_name, str):
		if isinstance(obj,str):
			obj = to_Old_MObject(obj)
		if isinstance(obj, OpenMaya.MObject):
			# Get The MPlug From The obj MObject and plg_obj MObject
			plg = to_Old_MPlug(obj, plug_name)
		else:
			raise ValueError("if Plug name input is a string then the obj input must be set to a valid MObject")
	else:
		plg = plug_name
	
	if not isinstance(plg, OpenMaya.MPlug):
		raise ValueError("plug_name input must be and attribute name or a MPlug")
	else:
		newplg = Convert_MPlug(plg, force_new=True)
	# Get The Plugs Connected To The Input Attribute
	plg_array = OpenMaya.MPlugArray()
	plg.connectedTo(plg_array, asDst, asSrc)
	# The Return List Of Plugs
	res = []
	for index in range(plg_array.length()):
		res.append(plg_array[index])
	return res
#----------------------------------------------------------------------
def get_Connected_Nodes(plug_name, obj=None, asDst=True, asSrc=False):
	
	plugs   = get_Connected_Plugs(plug_name, obj, asDst, asSrc)
	# The Return List Of Nodes The Plugs Belong To
	res = []
	for plug in plugs:
		Convert_MPlug(plug, force_old=True)
		node = plug.node()
		res.append(node)
	return res
#----------------------------------------------------------------------
def get_Plug_Elements(plug):
	new_plug = Convert_MPlug(plug, force_new=True)
	res = []
	indices = plug.getExistingArrayAttributeIndices()
	for i in indices:
		item = plug.elementByLogicalIndex(i)
		item = Convert_MPlug(item, force_old=True)
		res.append(item)
	return res
#----------------------------------------------------------------------
def get_Assined_VrayObjectProperties_Plug(obj):
	""""""
	fn = newOM.MFnDependencyNode()
	obj = Convert_MObject(obj, force_new=True)
	instObjGroups = to_New_MPlug(obj,"instObjGroups")
	Indices = instObjGroups.getExistingArrayAttributeIndices()
	for index in Indices:
		elem = instObjGroups.elementByLogicalIndex(index)
		if elem.isSource:
			connections = elem.connectedTo(False,True)
			for plg in connections:
				node = plg.node()
				if node.hasFn(MFn.kDependencyNode):
					fn.setObject(node)
					if fn.typeName == 'VRayObjectProperties':
						source_plug = Convert_MPlug(elem, force_old=True)
						dest_plug   = Convert_MPlug(plg, force_old=True)
						return [source_plug, dest_plug]
	return []
#----------------------------------------------------------------------
def get_Next_instObjGroups_Plug_Index(obj):
	obj = Convert_MObject(obj, force_new=True)
	instObjGroups = to_New_MPlug(obj, "instObjGroups")
	next_index = 0
	if instObjGroups.numElements():
		next_index =  max(instObjGroups.getExistingArrayAttributeIndices()) + 1
	return next_index

# Custom Helper Classes
########################################################################
class ObjectProperties(object):
	def __init__(self, obj):
		isinstance(obj, OpenMaya.MObject)
		self._obj                   = obj
		self.fnSet                  = OpenMaya.MFnSet(obj)
		self.message                = to_Old_MPlug(obj,"message")
		self.dnSetMembers           = to_Old_MPlug(obj,"dnSetMembers")
		self.dagSetMembers          = to_Old_MPlug(obj,"dagSetMembers")
		self.giVisibility           = to_Old_MPlug(obj,'giVisibility')
		self.primaryVisibility      = to_Old_MPlug(obj,'primaryVisibility')
		self.reflectionVisibility   = to_Old_MPlug(obj,'reflectionVisibility')
		self.refractionVisibility   = to_Old_MPlug(obj,'refractionVisibility')
		self.shadowVisibility       = to_Old_MPlug(obj,'shadowVisibility')
		self.matteSurface           = to_Old_MPlug(obj,'matteSurface')
		self.generateRenderElements = to_Old_MPlug(obj,'generateRenderElements')
		self.shadows                = to_Old_MPlug(obj,'shadows')
		self.affectAlpha            = to_Old_MPlug(obj,'affectAlpha')
		self.generateGI             = to_Old_MPlug(obj,'generateGI')
		self.receiveGI              = to_Old_MPlug(obj,'receiveGI')
		self.generateCaustics       = to_Old_MPlug(obj,'generateCaustics')
		self.receiveCaustics        = to_Old_MPlug(obj,'receiveCaustics')
		self.ignore                 = to_Old_MPlug(obj,'ignore')
		self.overrideMBSamples      = to_Old_MPlug(obj,'overrideMBSamples')
		self.objectIDEnabled        = to_Old_MPlug(obj,'objectIDEnabled')
		self.alphaContribution      = to_Old_MPlug(obj,'alphaContribution')
		
	#----------------------------------------------------------------------
	def get_Members(self):
		""""""
		sel = OpenMaya.MSelectionList()
		self.fnSet.getMembers(sel, False)
		return sel
	#----------------------------------------------------------------------
	def get_Next_DagMember_Plug_Index(self):
		dagSetMembers = Convert_MPlug(self.dagSetMembers, force_new=True)
		next_index = 0
		if dagSetMembers.numElements():
			next_index =  max(dagSetMembers.getExistingArrayAttributeIndices()) + 1
		return next_index
	#----------------------------------------------------------------------
	def add_Members(self, dgModer, objs):
		isinstance(dgModer, OpenMaya.MDGModifier)
		# Check if the objs is not a lists and if not make it part of one
		if isinstance(objs, (OpenMaya.MObject, newOM.MObject, OpenMaya.MDagPath, newOM.MDagPath)):
			objs = [objs]
		# Create A Temp Fn To Access Node Data
		fn = OpenMaya.MFnDagNode()
		# iterate Through Each Node
		for obj in objs:
			# Check If the Node Is Part Of the Dag Graph
			if obj.hasFn(MFn.kDagNode):
				# Make Sure That The MObject Is And Old Api Type
				obj = Convert_MObject(obj, force_old=True)
				# Check If This Object is allready A member of this set
				if not self.fnSet.isMember(obj):
					# Check If The Node Currently Assined To A Different VrayObjectProperty
					connection_check = get_Assined_VrayObjectProperties_Plug(obj)
					if len(connection_check):
						# Seperate The Connect Check into the source Node Plug and The Distination VrayObjectProperty Plug
						source_plug, dest_plug = connection_check
						try:
							# Disconnect The Node From Its Currently Assined VrayObjectProperty
							dgModer.disconnect(source_plug, dest_plug)
							dgModer.doIt()
						except RuntimeError:
							OpenMaya.MGlobal.displayError("Could not Disconnect '%s' from '%s'" % (source_plug.name(), dest_plug.name()) )
					else:
						# Get The Plug That Connects To the VrayObjectProperty dagmembers plug
						instObjGroups = to_Old_MPlug(obj, "instObjGroups")
						source_plug = instObjGroups.elementByLogicalIndex(0)
					
					try:
						# Get The Next elem index to be connect
						next_index = self.get_Next_DagMember_Plug_Index()
						# Get the plug Element 
						dest_plug = self.dagSetMembers.elementByLogicalIndex(next_index)
						dgModer.connect(source_plug, dest_plug)
						dgModer.doIt()
					except RuntimeError:
						OpenMaya.MGlobal.displayError("Could not Connect '%s' from '%s'" % (source_plug.name(), dest_plug.name()) )


# Node definitions
_Node_definition_Class_List = []
########################################################################
class AW_Base_Sets(OpenMayaMPx.MPxObjectSet):
	kNodeName = "AW_Base_Sets"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	
	#----------------------------------------------------------------------
	@property
	def dag_SetMembers_Plug(self):
		G_dependFn.setObject(self.thisMObject())
		plg = OpenMaya.MPlug(self.thisMObject(), G_dependFn.attribute("dagSetMembers"))
		return plg
	
	#----------------------------------------------------------------------
	@property
	def api2_dag_SetMembers_Plug(self):
		plg = Convert_MPlug(self.dag_SetMembers_Plug)
		return plg
	#----------------------------------------------------------------------
	@property
	def depend_SetMembers_Plug(self):
		G_dependFn.setObject(self.thisMObject())
		plg = OpenMaya.MPlug(self.thisMObject(), G_dependFn.attribute("dnSetMembers"))
		return plg
	#----------------------------------------------------------------------
	@property
	def api2_depend_SetMembers_Plug(self):
		plg = Convert_MPlug(self.depend_SetMembers_Plug)
		return plg
	#----------------------------------------------------------------------
	@property
	def Plug_message(self):
		G_dependFn.setObject(self.thisMObject())
		plg = OpenMaya.MPlug(self.thisMObject(), G_dependFn.attribute("message"))
		return plg
	#----------------------------------------------------------------------
	@property
	def api2_Plug_message(self):
		plg = Convert_MPlug(self.Plug_message)
		return plg
	#----------------------------------------------------------------------
	@property
	def Plug_usedByNodes(self):
		return OpenMaya.MPlug(self.thisMObject(), self.usedByNodes)
	
	def dag_Children(self):
		res = []
		indices = OpenMaya.MIntArray()
		elements = get_Plug_Elements(self.dag_SetMembers_Plug)
		for elem in elements:
			isinstance(elem, OpenMaya.MPlug)
			items = get_Connected_Nodes(elem, obj=None, asDst=True, asSrc=False)
			if len(items):
				item = items[0].node()
				res.append(item)
		return res
	#----------------------------------------------------------------------
	def depend_Children(self):
		res = []
		indices  = list(self.api2_depend_SetMembers_Plug.getExistingArrayAttributeIndices())
		for i in indices:
			elem = self.api2_depend_SetMembers_Plug.elementByLogicalIndex(i)
			isinstance(elem, OpenMaya.MPlug)
			items = elem.connectedTo(True, False)
			if len(items):
				plg  = items[0]
				item = Convert_MObject(plg.node())
				res.append(item)
		return res
	#----------------------------------------------------------------------
	def members(self):
		""""""
		selset = OpenMaya.MSelectionList()
		self._fnset.getMembers(selset, False)
		return selset
	#----------------------------------------------------------------------
	def connect_To_Next_dnSetmembers(self, dgModer, message):
		""""""

		isinstance(dgModer, OpenMaya.MDGModifier)
		next_index = 0
		plug = Convert_MPlug(self.depend_SetMembers_Plug)
		indices = plug.getExistingArrayAttributeIndices()
		if len(indices):
			next_index =  max(indices) + 1
		dgModer.connect(message, self.depend_SetMembers_Plug.elementByLogicalIndex(next_index))
		dgModer.doIt()
	
	# initializer
	#----------------------------------------------------------------------
	@classmethod
	def nodeInitializer(cls):
		pass
	# creator
	#----------------------------------------------------------------------
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
_Node_definition_Class_List.append(AW_Base_Sets)

########################################################################
class AW_Part_Sets(AW_Base_Sets):
	kNodeName = "AW_Part_Sets"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	
	@classmethod
	def scan_tracking_Data(cls, obj):
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				return cls.kTrackingDictionary[key]["obj"]
		return None
	#----------------------------------------------------------------------
	def __init__(self):
		AW_Base_Sets.__init__(self)
		AW_Part_Sets.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	#----------------------------------------------------------------------
	def canBeDeleted(self, isSrcNode):
		plg = OpenMaya.MPlug(self.thisMObject(), self.usedByNodes)
		if helpers.get_connected_plug_objects(plg, False, True).length():
			return False
		return True
	# override
	#----------------------------------------------------------------------
	def postConstructor(self):
		"""
		 When instances of this node are created internally, the
		 MObject associated with the instance is not created until
		 after the constructor of this class is called. This means
		 that no member functions can be called in
		 the constructor.  The postConstructor solves this
		 problem. Maya will call this function after the internal
		 object has been created.  As a general rule do all of your
		 initialization in the postConstructor.
		"""
		_hash = OpenMaya.MObjectHandle(self.thisMObject()).hashCode()
		att_changed_id = OpenMaya.MNodeMessage.addAttributeChangedCallback(self.thisMObject(), Attribute_Changed_Callback, None)
		self.__class__.kTrackingDictionary[_hash] = dict(obj=self, ids=[att_changed_id])
		self._fnset = helpers.toMFnSet(self.thisMObject())

	#----------------------------------------------------------------------
	def __del__(self):
		_hash = OpenMayaMPx.asHashable(self)
		data = self.__class__.kTrackingDictionary.get(_hash, False)
		if data:
			for ID in data["ids"]:
				OpenMaya.MSceneMessage.removeCallback(ID)
			del self.__class__.kTrackingDictionary[_hash]
	#----------------------------------------------------------------------
	def setDependentsDirty(self, plugBeingDirtied, affectedPlugs):
		isinstance(plugBeingDirtied, OpenMaya.MPlug)
		isinstance(affectedPlugs, OpenMaya.MPlugArray)
		return True
	# override
	#----------------------------------------------------------------------
	def compute(self, plug, dataBlock):
		"""
		 Since there are no output attributes this is not necessary but
		 if we wanted to compute an output mesh for rendering it would
		 be done here base on the inputs.
		"""
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def legalConnection(self, plug, otherPlug, asSrc, isLegal):
		"""
			plug     :attribute on this node
			otherPlug:attribute on other node
			asSrc    :is this plug a source of the connection
			isLegal	 :set this to true if the connection is legal, false otherwise
		"""
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		G_dependFn.setObject(otherPlug.node())
		if not asSrc and not G_dependFn.typeName() == "VRayObjectProperties":
			isLegal = False
		else:
			return OpenMaya.kUnknownParameter

	#----------------------------------------------------------------------
	def connectionMade(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionBroken(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	
	#----------------------------------------------------------------------	
	def get_Part_Set_By_Name(self, name):
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeName() == "VRayObjectProperties":
				if fnDepend.name() == name:
					res = child
					break
		isinstance(res, OpenMaya.MObject)
		return res
	
	#----------------------------------------------------------------------	
	def Names_To_Part_Sets(self, names):
		fnDepend = OpenMaya.MFnDependencyNode()
		res = []
		children = self.depend_Children()
		for name in names:
			for child in children:
				fnDepend.setObject(child)
				if fnDepend.typeName() == "VRayObjectProperties" and fnDepend.name() == name:
					res.append(child)
					children.remove(child)
					break
		return res
	
	# initializer
	@classmethod
	def nodeInitializer(cls):
		pass

	# creator
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
_Node_definition_Class_List.append(AW_Part_Sets)

########################################################################
class AW_Parts_Container(AW_Base_Sets):
	kNodeName = "AW_Parts_Container"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	@classmethod
	def scan_tracking_Data(cls, obj):
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				return cls.kTrackingDictionary[key]["obj"]
		return None
	#----------------------------------------------------------------------
	def canBeDeleted(self, isSrcNode):
		return False
	#----------------------------------------------------------------------
	def legalConnection(self, plug, otherPlug, asSrc, isLegal):
		"""
			plug     :attribute on this node
			otherPlug:attribute on other node
			asSrc    :is this plug a source of the connection
			isLegal	 :set this to true if the connection is legal, false otherwise
		"""
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		G_dependFn.setObject(otherPlug.node())
		if not asSrc and not G_dependFn.typeName() == "VRayObjectProperties":
			isLegal = False
		else:
			return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def legalDisconnection(self, plug, otherPlug, asSrc, isLegal):
		"""
			plug     :attribute on this node
			otherPlug:attribute on other node
			asSrc    :is this plug a source of the connection
			isLegal	 :set this to true if the connection is legal, false otherwise
		"""
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		G_dependFn.setObject(otherPlug.node())
		if asSrc and G_dependFn.typeName() != AW_Scene_State.kNodeName:
			isLegal = False
		else:
			return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionMade(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionBroken(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def __del__(self):
		_hash = OpenMayaMPx.asHashable(self)
		data = self.__class__.kTrackingDictionary.get(_hash, False)
		if data:
			for ID in data["ids"]:
				OpenMaya.MSceneMessage.removeCallback(ID)
			del self.__class__.kTrackingDictionary[_hash]
	#----------------------------------------------------------------------
	def postConstructor(self):
		"""
		 When instances of this node are created internally, the
		 MObject associated with the instance is not created until
		 after the constructor of this class is called. This means
		 that no member functions can be called in
		 the constructor.  The postConstructor solves this
		 problem. Maya will call this function after the internal
		 object has been created.  As a general rule do all of your
		 initialization in the postConstructor.
		"""
		_hash = OpenMayaMPx.asHashable(self)
		att_changed_id = OpenMaya.MNodeMessage.addAttributeChangedCallback(self.thisMObject(), Attribute_Changed_Callback, None)
		self.__class__.kTrackingDictionary[_hash] = dict(obj=self, ids=[att_changed_id])
		self._fnset = helpers.toMFnSet(self.thisMObject())
	#----------------------------------------------------------------------
	@classmethod
	def nodeInitializer(cls):
		pass
	#----------------------------------------------------------------------
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
	#----------------------------------------------------------------------
	def has_Part_Set(self, part):
		isinstance(part, OpenMaya.MObject)
		return self._fnset.isMember(part)
	#----------------------------------------------------------------------
	def get_Parent_Scene_State(self):
		""""""
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		items = OpenMaya.MPlugArray()
		self.Plug_message.connectedTo(items, False, True)
		if items.length():
			for i in range(items.length()):
				item = items[i]
				node = item.node()
				fnDepend.setObject(node)
				if fnDepend.typeId().id() == AW_Scene_State.kNodeId.id():
					res = AW_Scene_State.scan_tracking_Data(node)
		return res
	#----------------------------------------------------------------------
	def Assine_Part_set(self, moder, parts):
		isinstance(moder, OpenMaya.MDGModifier)
		fndepend  = OpenMaya.MFnDependencyNode()
		fndepend2 = OpenMaya.MFnDependencyNode()
		fnset     = OpenMaya.MFnSet()
		for part in  parts:
			scene_state = self.get_Parent_Scene_State()
			if not self._fnset.isMember(part):
				fndepend.setObject(part)
				if fndepend.typeName() == "VRayObjectProperties":
					message_plg = to_Old_MPlug(part, "message")
					plugs = get_Connected_Plugs(message_plg, obj=None, asDst=False, asSrc=True)
					for plug in  plugs:
						node = plug.node()
						fndepend2.setObject(node)
						if fndepend2.typeId().id() in [AW_Beauty_Parts.kNodeId.id(), AW_Matte_Parts.kNodeId.id(), AW_Invisible_Parts.kNodeId.id()]:
							if scene_state._fnset.isMember(node):
								moder.disconnect(message_plg, plug)
								moder.doIt()
					self.connect_To_Next_dnSetmembers(moder, message_plg)
					
	#----------------------------------------------------------------------
	def UnAssine_Part_set(self, moder, parts):
		isinstance(moder, OpenMaya.MDGModifier)
		fndepend    = OpenMaya.MFnDependencyNode()
		fndepend2   = OpenMaya.MFnDependencyNode()
		fnset       = OpenMaya.MFnSet()
		scene_state = self.get_Parent_Scene_State()
		for part in  parts:
			if self._fnset.isMember(part):
				fndepend.setObject(part)
				if fndepend.typeName() == "VRayObjectProperties":
					message_plg = to_Old_MPlug(part, "message")
					plugs = get_Connected_Plugs(message_plg, obj=None, asDst=False, asSrc=True)
					for plug in  plugs:
						node = plug.node()
						fndepend2.setObject(node)
						if fndepend2.typeId().id() in [AW_Beauty_Parts.kNodeId.id(), AW_Matte_Parts.kNodeId.id(), AW_Invisible_Parts.kNodeId.id()]:
							if scene_state._fnset.isMember(node):
								moder.disconnect(message_plg, plug)
								moder.doIt()
_Node_definition_Class_List.append(AW_Parts_Container)

########################################################################
class AW_Beauty_Parts(AW_Parts_Container):
	kNodeName = "AW_Beauty_Parts"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	def __init__(self):
		AW_Parts_Container.__init__(self)
		AW_Beauty_Parts.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	@classmethod
	def scan_tracking_Data(cls, obj):
		res = None
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				res = cls.kTrackingDictionary[key]["obj"]
				break
		isinstance(res, AW_Beauty_Parts)
		return res
	#----------------------------------------------------------------------
	@classmethod
	def nodeInitializer(cls):
		pass
	#----------------------------------------------------------------------
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
_Node_definition_Class_List.append(AW_Beauty_Parts)

########################################################################
class AW_Invisible_Parts(AW_Parts_Container):
	kNodeName = "AW_Invisible_Parts"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	def __init__(self):
		AW_Parts_Container.__init__(self)
		AW_Invisible_Parts.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	@classmethod
	def scan_tracking_Data(cls, obj):
		res = None
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				res = cls.kTrackingDictionary[key]["obj"]
				break
		isinstance(res, AW_Invisible_Parts)
		return res
	#----------------------------------------------------------------------
	@classmethod
	def nodeInitializer(cls):
		pass
	#----------------------------------------------------------------------
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
_Node_definition_Class_List.append(AW_Invisible_Parts)

########################################################################
class AW_Matte_Parts(AW_Parts_Container):
	kNodeName = "AW_Matte_Parts"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	def __init__(self):
		AW_Parts_Container.__init__(self)
		AW_Matte_Parts.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	@classmethod
	def scan_tracking_Data(cls, obj):
		res = None
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				res = cls.kTrackingDictionary[key]["obj"]
				break
		isinstance(res, AW_Matte_Parts)
		return res
	#----------------------------------------------------------------------
	@classmethod
	def nodeInitializer(cls):
		pass
	#----------------------------------------------------------------------
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
_Node_definition_Class_List.append(AW_Matte_Parts)

########################################################################
class AW_Scene_State(AW_Base_Sets):
	kNodeName = "AW_Scene_State"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	
	@classmethod
	def scan_tracking_Data(cls, obj):
		res = None
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				res = cls.kTrackingDictionary[key]["obj"]
				break
		isinstance(res, AW_Scene_State)
		return res
	#----------------------------------------------------------------------
	def __init__(self):
		AW_Base_Sets.__init__(self)
		AW_Scene_State.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	#----------------------------------------------------------------------
	def canBeDeleted(self, isSrcNode):
		plg = OpenMaya.MPlug(self.thisMObject(), self.usedByNodes)
		if helpers.get_connected_plug_objects(plg, False, True).length():
			return False
		return False
	# override
	#----------------------------------------------------------------------
	def postConstructor(self):
		"""
		 When instances of this node are created internally, the
		 MObject associated with the instance is not created until
		 after the constructor of this class is called. This means
		 that no member functions can be called in
		 the constructor.  The postConstructor solves this
		 problem. Maya will call this function after the internal
		 object has been created.  As a general rule do all of your
		 initialization in the postConstructor.
		"""
		_hash = OpenMayaMPx.asHashable(self)
		att_changed_id = OpenMaya.MNodeMessage.addAttributeChangedCallback(self.thisMObject(), Attribute_Changed_Callback, None)
		AW_Scene_State.kTrackingDictionary[_hash] = dict(obj=self, ids=[att_changed_id])
		self._fnset = helpers.toMFnSet(self.thisMObject())

	#----------------------------------------------------------------------
	def __del__(self):
		_hash = OpenMayaMPx.asHashable(self)
		data = self.__class__.kTrackingDictionary.get(_hash, False)
		if data:
			for ID in data["ids"]:
				OpenMaya.MSceneMessage.removeCallback(ID)
			del self.__class__.kTrackingDictionary[_hash]
	#----------------------------------------------------------------------
	def legalConnection(self, plug, otherPlug, asSrc, isLegal):
		"""
			plug     :attribute on this node
			otherPlug:attribute on other node
			asSrc    :is this plug a source of the connection
			isLegal	 :set this to true if the connection is legal, false otherwise
		"""
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		G_dependFn.setObject(otherPlug.node())
		if not asSrc and not G_dependFn.typeName() in [AW_Beauty_Parts.kNodeName, AW_Invisible_Parts.kNodeName, AW_Matte_Parts.kNodeName]:
			isLegal = False
		else:
			return OpenMaya.kUnknownParameter
	##----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def setDependentsDirty(self, plugBeingDirtied, affectedPlugs):
		isinstance(plugBeingDirtied, OpenMaya.MPlug)
		isinstance(affectedPlugs, OpenMaya.MPlugArray)
		return True
	# override
	#----------------------------------------------------------------------
	def compute(self, plug, dataBlock):
		"""
		 Since there are no output attributes this is not necessary but
		 if we wanted to compute an output mesh for rendering it would
		 be done here base on the inputs.
		"""
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionMade(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionBroken(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter

	# initializer
	@classmethod
	def nodeInitializer(cls):
		pass

	# creator
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
	#----------------------------------------------------------------------
	def get_Parent_States_List(self):
		""""""
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		items = OpenMaya.MPlugArray()
		self.Plug_message.connectedTo(items, False, True)
		if items.length():
			for i in range(items.length()):
				item = items[i]
				node = item.node()
				fnDepend.setObject(node)
				if fnDepend.typeId().id() == AW_Scene_State_List.kNodeId.id():
					res = AW_Scene_State_List.scan_tracking_Data(node)
		return res
	
	#----------------------------------------------------------------------
	def get_Beauty(self):
		""""""
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeId().id() == AW_Beauty_Parts.kNodeId.id():
				res = AW_Beauty_Parts.scan_tracking_Data(child)
				break
		isinstance(res, AW_Beauty_Parts)
		return res
	
	#----------------------------------------------------------------------
	def get_Invisible(self):
		""""""
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeId().id() == AW_Invisible_Parts.kNodeId.id():
				res = AW_Invisible_Parts.scan_tracking_Data(child)
				break
		isinstance(res, AW_Invisible_Parts)
		return res
	
	#----------------------------------------------------------------------
	def get_Matte(self):
		""""""
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeId().id() == AW_Matte_Parts.kNodeId.id():
				res = AW_Matte_Parts.scan_tracking_Data(child)
				break
		isinstance(res, AW_Matte_Parts)
		return res
	
	#----------------------------------------------------------------------
	def get_State_Type(self, kValue):
		""""""
		res = None
		if kValue == kBeauty:
			res = self.get_Beauty()
		elif kValue == kMatte:
			res = self.get_Matte()
		elif kValue == kInvisible:
			res = self.get_Invisible()
		isinstance(res, AW_Parts_Container)
		return res
_Node_definition_Class_List.append(AW_Scene_State)

########################################################################
class AW_Scene_State_List(AW_Base_Sets):
	kNodeName = "AW_Scene_State_List"
	kNodeId   = OpenMaya.MTypeId(plugin_id_counter())
	kTrackingDictionary         = {}
	att_changed_id = 0
	@classmethod
	def scan_tracking_Data(cls, obj):
		res = None
		if hasattr(obj, "name"):
			name = obj.name()
		else:
			dependFn  = OpenMaya.MFnDependencyNode(obj)
			name = dependFn.name()
			
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				res = cls.kTrackingDictionary[key]["obj"]
				break
		isinstance(res, AW_Scene_State_List)
		return res
	#----------------------------------------------------------------------
	def __init__(self):
		AW_Base_Sets.__init__(self)
		AW_Scene_State_List.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	#----------------------------------------------------------------------
	def canBeDeleted(self, isSrcNode):
		plg = OpenMaya.MPlug(self.thisMObject(), self.usedByNodes)
		if helpers.get_connected_plug_objects(plg, True, True).length():
			return False
		if not isSrcNode:
			return False
		return False
	# override
	#----------------------------------------------------------------------
	def postConstructor(self):
		"""
		 When instances of this node are created internally, the
		 MObject associated with the instance is not created until
		 after the constructor of this class is called. This means
		 that no member functions can be called in
		 the constructor.  The postConstructor solves this
		 problem. Maya will call this function after the internal
		 object has been created.  As a general rule do all of your
		 initialization in the postConstructor.
		"""
		_hash = OpenMayaMPx.asHashable(self)
		att_changed_id = OpenMaya.MNodeMessage.addAttributeChangedCallback(self.thisMObject(), Attribute_Changed_Callback, None)
		self.__class__.kTrackingDictionary[_hash] = dict(obj=self, ids=[att_changed_id])
		self._fnset = helpers.toMFnSet(self.thisMObject())

	#----------------------------------------------------------------------
	def __del__(self):
		_hash = OpenMayaMPx.asHashable(self)
		data = self.__class__.kTrackingDictionary.get(_hash, False)
		if data:
			for ID in data["ids"]:
				OpenMaya.MSceneMessage.removeCallback(ID)
			del self.__class__.kTrackingDictionary[_hash]
	#----------------------------------------------------------------------
	def legalConnection(self, plug, otherPlug, asSrc, isLegal):
		"""
			plug     :attribute on this node
			otherPlug:attribute on other node
			asSrc    :is this plug a source of the connection
			isLegal	 :set this to true if the connection is legal, false otherwise
		"""
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		G_dependFn.setObject(otherPlug.node())
		if not asSrc and not G_dependFn.typeName() == AW_Scene_State.kNodeName:
			isLegal = False
		else:
			return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------	
	def get_Scene_State_By_Name(self, name):
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeId().id() == AW_Scene_State.kNodeId.id():
				if fnDepend.name() == name:
					item = AW_Scene_State.scan_tracking_Data(child)
					if not item == None:
						res = item
						break
		isinstance(res, AW_Scene_State)
		return res
	
	def setDependentsDirty(self, plugBeingDirtied, affectedPlugs):
		isinstance(plugBeingDirtied, OpenMaya.MPlug)
		isinstance(affectedPlugs, OpenMaya.MPlugArray)
		return True
	# override
	#----------------------------------------------------------------------
	def compute(self, plug, dataBlock):
		"""
		 Since there are no output attributes this is not necessary but
		 if we wanted to compute an output mesh for rendering it would
		 be done here base on the inputs.
		"""
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionMade(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionBroken(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter

	# initializer
	@classmethod
	def nodeInitializer(cls):
		pass

	# creator
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
	
	#----------------------------------------------------------------------
	def get_Parent_Manager(self):
		""""""
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		items = OpenMaya.MPlugArray()
		self.Plug_message.connectedTo(items, False, True)
		if items.length():
			for i in range(items.length()):
				item = items[i]
				node = item.node()
				fnDepend.setObject(node)
				if fnDepend.typeId().id() == AW_Scene_State_Manager.kNodeId.id():
					res = AW_Scene_State_Manager.scan_tracking_Data(node)
		return res
_Node_definition_Class_List.append(AW_Scene_State_List)

########################################################################
class AW_Scene_State_Manager(AW_Base_Sets):
	kNodeName           = "AW_Scene_State_Manager"
	kNodeId             = OpenMaya.MTypeId(plugin_id_counter())
	_active_instance    = None
	kTrackingDictionary = {}
	att_changed_id      = 0
	
	@classmethod
	def scan_tracking_Data(cls, obj):
		dependFn  = OpenMaya.MFnDependencyNode(obj)
		name = dependFn.name()
		res = None
		for key in list(cls.kTrackingDictionary.keys()):
			if cls.kTrackingDictionary[key]["obj"].name() == name:
				res = cls.kTrackingDictionary[key]["obj"]
				break
		isinstance(res, AW_Scene_State_Manager)
		return res
	
	##----------------------------------------------------------------------
	def __init__(self):
		OpenMayaMPx.MPxObjectSet.__init__(self)
		AW_Base_Sets.__init__(self)
		AW_Scene_State_Manager._active_instance = self
		AW_Scene_State_Manager.kTrackingDictionary[OpenMayaMPx.asHashable(self)] = dict(obj=self, ids=[])
	#----------------------------------------------------------------------	
	def get_Part_Sets(self):
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeId().id() == AW_Part_Sets.kNodeId.id():
				item = AW_Part_Sets.scan_tracking_Data(child)
				if not item == None:
					res = item
					break
		isinstance(res, AW_Part_Sets)
		return res
	#----------------------------------------------------------------------	
	def get_States_List(self):
		fnDepend = OpenMaya.MFnDependencyNode()
		res = None
		for child in self.depend_Children():
			fnDepend.setObject(child)
			if fnDepend.typeId().id() == AW_Scene_State_List.kNodeId.id():
				item = AW_Scene_State_List.scan_tracking_Data(child)
				if not item == None:
					res = item
					break
		isinstance(res, AW_Scene_State_List)
		return res
	# override
	#----------------------------------------------------------------------
	def postConstructor(self):
		"""
		 When instances of this node are created internally, the
		 MObject associated with the instance is not created until
		 after the constructor of this class is called. This means
		 that no member functions can be called in
		 the constructor.  The postConstructor solves this
		 problem. Maya will call this function after the internal
		 object has been created.  As a general rule do all of your
		 initialization in the postConstructor.
		"""
		att_changed_id = OpenMaya.MNodeMessage.addAttributeChangedCallback(self.thisMObject(), Attribute_Changed_Callback, None)
		AW_Scene_State_Manager.kTrackingDictionary[OpenMayaMPx.asHashable(self)]["ids"] = [att_changed_id]
		self._fnset = helpers.toMFnSet(self.thisMObject())
	#----------------------------------------------------------------------
	def __del__(self):
		_hash = OpenMayaMPx.asHashable(self)
		data = self.__class__.kTrackingDictionary.get(_hash, False)
		AW_Scene_State_Manager._active_instance = None
		if data:
			for ID in data["ids"]:
				OpenMaya.MSceneMessage.removeCallback(ID)
			del self.__class__.kTrackingDictionary[_hash]
	#----------------------------------------------------------------------
	def legalConnection(self, plug, otherPlug, asSrc, isLegal):
		"""
			plug     :attribute on this node
			otherPlug:attribute on other node
			asSrc    :is this plug a source of the connection
			isLegal	 :set this to true if the connection is legal, false otherwise
		"""
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		G_dependFn.setObject(otherPlug.node())
		if not asSrc and not G_dependFn.typeName() in [AW_Scene_State_List.kNodeName, AW_Part_Sets.kNodeName]:
			isLegal = False
		else:
			return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def setDependentsDirty(self, plugBeingDirtied, affectedPlugs):
		isinstance(plugBeingDirtied, OpenMaya.MPlug)
		isinstance(affectedPlugs, OpenMaya.MPlugArray)
		return True
	#----------------------------------------------------------------------
	def compute(self, plug, dataBlock):
		"""
		 Since there are no output attributes this is not necessary but
		 if we wanted to compute an output mesh for rendering it would
		 be done here base on the inputs.
		"""
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionMade(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	def connectionBroken(self, plug, otherPlug, asSrc):
		isinstance(plug, OpenMaya.MPlug)
		isinstance(otherPlug, OpenMaya.MPlug)
		return OpenMaya.kUnknownParameter
	#----------------------------------------------------------------------
	@classmethod
	def nodeInitializer(cls):
		pass
	#----------------------------------------------------------------------
	@classmethod
	def nodeCreator(cls):
		return OpenMayaMPx.asMPxPtr(cls())
_Node_definition_Class_List.append(AW_Scene_State_Manager)


kCmdName                = "awSceneState"
kManager_Flag           = "-ssm"
kManager_LongFlag       = "-sceneStateManager"
kName_Flag              = "-n"
kName_LongFlag          = "-name"
kPartSet_Flag           = "-p"
kPartSet_LongFlag       = "-part"
kState_Flag             = "-s"
kState_LongFlag         = "-state"
kNode_Flag              = "-nod"
kNode_LongFlag          = "-node"
kAddState_Flag          = "-ads"
kAddState_LongFlag      = "-addState"
kRemoveState_Flag       = "-rms"
kRemoveState_LongFlag   = "-removeState"
kAddPartSet_Flag        = "-adp"
kAddPartSet_LongFlag    = "-addPart"
kRemovePartSet_Flag     = "-rmp"
kRemovePartSet_LongFlag = "-removePart"
kAssinPart_Flag         = "-anp"
kAssinPart_LongFlag     = "-assinePart"
kUnAssinePart_Flag      = "-uap"
kUnAssinePart_LongFlag  = "-unAssinePart"
kMatte_Flag             = "-m"
kMatte_LongFlag         = "-matte"
kBeauty_Flag            = "-b"
kBeauty_LongFlag        = "-beauty"
kInvisible_Flag         = "-i"
kInvisible_LongFlag     = "-invisible"

kAssinNodes_Flag        = "-ann"
kAssinNodes_LongFlag    = "-assineNodes"
kUnAssineNodes_Flag     = "-uan"
kUnAssineNodes_LongFlag = "-unAssineNodes"


#----------------------------------------------------------------------
def extract_String_Args_For_Flag(Flag, argData):
	""""""
	arglist = OpenMaya.MArgList()
	index = 0
	while True:
		try:
			argData.getFlagArgumentList(Flag, index, arglist)
			index += 1
		except:
			break
	res = [arglist.asString(index) for index in range(arglist.length())]
	return res
#----------------------------------------------------------------------
def extract_args(args):
	""""""
	arglist = OpenMaya.MArgList(args)
	res = [arglist.asString(index) for index in range(arglist.length())]
	return res
#----------------------------------------------------------------------
def Find_AW_Scene_State_Manager():
	fn = OpenMaya.MFnDependencyNode()
	depend_iter = OpenMaya.MItDependencyNodes(MFn.kPluginObjectSet)
	while not depend_iter.isDone():
		dpnode = depend_iter.thisNode()
		fn.setObject(dpnode)
		if fn.typeId().id() == AW_Scene_State_Manager.kNodeId.id():
			item = AW_Scene_State_Manager.scan_tracking_Data(dpnode)
			return item
		next(depend_iter)
	return False
#----------------------------------------------------------------------
def Find_Scene_State_Manager_From_Input_String(name):
	dpnIter = OpenMaya.MItDependencyNodes(MFn.kPluginObjectSet)
	res = None
	while not dpnIter.isDone():
		item = dpnIter.thisNode()
		fn = OpenMaya.MFnDependencyNode(item)
		if fn.typeId().id() == AW_Scene_State_Manager.kNodeId.id():
			if fn.name() == name:
				res = AW_Scene_State_Manager.scan_tracking_Data(item)
				break
		next(dpnIter)
	isinstance(res, AW_Scene_State_Manager)
	return res
#----------------------------------------------------------------------
def Find_Scene_State_Manager_From_Active_Selection():
	res = None
	activeSelection = OpenMaya.MSelectionList()
	OpenMaya.MGlobal.getActiveSelectionList(activeSelection)
	sel_iter = OpenMaya.MItSelectionList(activeSelection)
	sel_iter.setFilter(MFn.kPluginObjectSet)
	while not sel_iter.isDone():
		dpnode=OpenMaya.MObject()
		sel_iter.getDependNode(dpnode)
		fn = OpenMaya.MFnDependencyNode(dpnode)
		if fn.typeId().id() == AW_Scene_State_Manager.kNodeId.id():
			res = AW_Scene_State_Manager.scan_tracking_Data(dpnode)
			break
		next(sel_iter)
	isinstance(res, AW_Scene_State_Manager)
	return res
#----------------------------------------------------------------------
def Find_Scene_States_From_Active_Selection():
	res = None
	activeSelection = OpenMaya.MSelectionList()
	OpenMaya.MGlobal.getActiveSelectionList(activeSelection)
	sel_iter = OpenMaya.MItSelectionList(activeSelection)
	sel_iter.setFilter(MFn.kPluginObjectSet)
	res = []
	fn = OpenMaya.MFnDependencyNode()
	while not sel_iter.isDone():
		dpnode=OpenMaya.MObject()
		sel_iter.getDependNode(dpnode)
		fn.setObject(dpnode)
		if fn.typeId().id() == AW_Scene_State.kNodeId.id():
			found = AW_Scene_State.scan_tracking_Data(dpnode)
			if found is not None:
				res.append(found)
		next(sel_iter)
	return res
#----------------------------------------------------------------------
def Find_Scene_State_From_Input_String(name):
	dpnIter = OpenMaya.MItDependencyNodes(MFn.kPluginObjectSet)
	res = None
	fn = OpenMaya.MFnDependencyNode()
	while not dpnIter.isDone():
		item = dpnIter.thisNode()
		fn.setObject(item)
		if fn.typeId().id() == AW_Scene_State.kNodeId.id():
			if fn.name() == name:
				res = AW_Scene_State.scan_tracking_Data(item)
				break
		next(dpnIter)
	isinstance(res, AW_Scene_State)
	return res
#----------------------------------------------------------------------
def Find_Scene_States_From_Active_Selection():
	res = None
	activeSelection = OpenMaya.MSelectionList()
	OpenMaya.MGlobal.getActiveSelectionList(activeSelection)
	sel_iter = OpenMaya.MItSelectionList(activeSelection)
	sel_iter.setFilter(MFn.kPluginObjectSet)
	res = []
	fn = OpenMaya.MFnDependencyNode()
	while not sel_iter.isDone():
		dpnode=OpenMaya.MObject()
		sel_iter.getDependNode(dpnode)
		fn.setObject(dpnode)
		if fn.typeName() == 'VRayObjectProperties':
			found = ObjectProperties(dpnode)
			res.append(found)
		next(sel_iter)
	return res
#----------------------------------------------------------------------
def Find_Part_Set_From_Input_String(name):
	dpnIter = OpenMaya.MItDependencyNodes(MFn.kPluginObjectSet)
	res = None
	fn = OpenMaya.MFnDependencyNode()
	while not dpnIter.isDone():
		item = dpnIter.thisNode()
		fn.setObject(item)
		if fn.typeName() == 'VRayObjectProperties':
			if fn.name() == name:
				res = ObjectProperties(item)
				break
		next(dpnIter)
	isinstance(res, ObjectProperties)
	return res
#----------------------------------------------------------------------
def Find_All_Part_Sets():
	res = []
	fn = OpenMaya.MFnDependencyNode()
	depend_iter = OpenMaya.MItDependencyNodes(MFn.kPluginObjectSet)
	while not depend_iter.isDone():
		dpnode = depend_iter.thisNode()
		fn.setObject(dpnode)
		if fn.typeId().id() == AW_Part_Sets.kNodeId.id():
			item = AW_Part_Sets.scan_tracking_Data(dpnode)
			if item is not None:
				res.append(item)
		next(depend_iter)
	return res
#----------------------------------------------------------------------
def Find_Part_Sets_From_Input_String(name):
	dpnIter = OpenMaya.MItDependencyNodes(MFn.kPluginObjectSet)
	res = None
	fn = OpenMaya.MFnDependencyNode()
	while not dpnIter.isDone():
		item = dpnIter.thisNode()
		fn.setObject(item)
		if fn.typeId().id() == AW_Part_Sets.kNodeId.id():
			if fn.name() == name:
				res = AW_Part_Sets.scan_tracking_Data(item)
				break
		next(dpnIter)
	isinstance(res, AW_Part_Sets)
	return res
#----------------------------------------------------------------------
def Find_Part_Sets_From_Active_Selection():
	res = None
	activeSelection = OpenMaya.MSelectionList()
	OpenMaya.MGlobal.getActiveSelectionList(activeSelection)
	sel_iter = OpenMaya.MItSelectionList(activeSelection)
	sel_iter.setFilter(MFn.kPluginObjectSet)
	res = []
	fn = OpenMaya.MFnDependencyNode()
	while not sel_iter.isDone():
		dpnode=OpenMaya.MObject()
		sel_iter.getDependNode(dpnode)
		fn.setObject(dpnode)
		if fn.typeId().id() == AW_Part_Sets.kNodeId.id():
			found = AW_Part_Sets.scan_tracking_Data(dpnode)
			if not found == None:
				res.append(found)
		next(sel_iter)
	return res

kBeauty, kMatte, kInvisible =  list(range(3))

class AW_Scene_State_Command(OpenMayaMPx.MPxCommand):
	#----------------------------------------------------------------------
	def __init__(self):
		OpenMayaMPx.MPxCommand.__init__(self)
		self._DGmod    = OpenMaya.MDGModifier()
		self._fnSet    = OpenMaya.MFnSet()
		self._fnDepend = OpenMaya.MFnDependencyNode()
	#----------------------------------------------------------------------
	def remove_scene_states(self, states_list, names):
		""""""
		# Create A Temp Function set to Access The MObject
		fnDepend = OpenMaya.MFnDependencyNode()
		# Iterate Through Each Scene State Name
		for name in  names:
			# Find The Scene State Instance That Matches The Current name
			scene_state  = states_list.get_Scene_State_By_Name(name)
			# Make Sure A Scene State Was Found
			if scene_state is not None:
				# get a list of all the children conneted To the depend set Members Attribute
				depend_Children = scene_state.depend_Children()
				# Iterate Through Each Child Connect To The Depend Set Members Attribute
				for child in depend_Children:
					# Assine The Temp Function Set To The Current Child
					fnDepend.setObject(child)
					# Create A MPlug For the message Attribute Of The Current Child
					plgA = to_Old_MPlug(child, "message")
					# Get A List Of The Connect Plug That This Childs message plug is the source of
					child_connects = get_Connected_Plugs(plgA, asDst=True, asSrc=False)
					# Iterate Through Each Connected Plug
					for plgB in child_connects:
						## get The Node Of Plug B
						#B_node = plgB.node()
						# Dissconnect Child Message Plug From What Ever It is Connected To
						self._DGmod.disconnect(plgA, plbB)
						self._DGmod.doIt()
						# Now Delete The Child
					self._DGmod.deleteNode(child)
					self._DGmod.doIt()
				
				#### Get A List Of The Connected Plugs scene_state message plug is the source of
				#child_connects = get_Connected_Plugs(scene_state.Plug_message, asDst=True, asSrc=False)
				#### Iterate Through Each Connected Plug
				#for plgB in child_connects:
					### Dissconnect PlgB from The scene state message plug
					#self._DGmod.disconnect(scene_state.Plug_message, plbB)
					#self._DGmod.doIt()
					### Now Delete The Scene State
				item =  to_Old_MObject(scene_state.name())
				self._DGmod.deleteNode(item)
				self._DGmod.doIt()
	#----------------------------------------------------------------------
	def create_scene_state(self, states_list, names=[]):
		""""""
		# Create An Empty List To Hold The Return Value
		res = []
		# Check If The input Names is Empty
		if not len(names):
			# Create A Default Scene State
			names.append(None)
		# Iterate Through Each name
		for name in names:
			# Create A New Scene State
			scene_state_obj = self._DGmod.createNode(AW_Scene_State.kNodeId)
			self._DGmod.doIt()
			# Get The Scene State Python Class Instance
			scene_state  = AW_Scene_State.scan_tracking_Data(scene_state_obj)
			# Add The scene state to the return value
			res.append(scene_state)
			# Check if The name value is set
			if not name == None:
				# If So Set The Name Of The Scene State To the input Name
				self._DGmod.renameNode(scene_state.thisMObject(), name)
			else:
				self._DGmod.renameNode(scene_state.thisMObject(), "AW_Render_State")
				
			self._DGmod.doIt()
			# Connect The Scene State To The Scene States List As A Child Of The depend set Members
			states_list.connect_To_Next_dnSetmembers(self._DGmod, scene_state.Plug_message)
			self._DGmod.doIt()
			
			# Create A Beauty State 
			beauty       = AW_Beauty_Parts.scan_tracking_Data(self._DGmod.createNode(AW_Beauty_Parts.kNodeId))
			# Create A Invisible State 
			invisible    = AW_Invisible_Parts.scan_tracking_Data(self._DGmod.createNode(AW_Invisible_Parts.kNodeId))
			# Create A Matte State 
			matte        = AW_Matte_Parts.scan_tracking_Data(self._DGmod.createNode(AW_Matte_Parts.kNodeId))
			self._DGmod.doIt()
			# Connect The State To The Newly Created Scene State
			[scene_state.connect_To_Next_dnSetmembers(self._DGmod, item.Plug_message) for item in [beauty, invisible, matte]]
		
		return res
	#----------------------------------------------------------------------
	def create_VRayObjectProperties(self, names=[]):
		""""""
		# Create An Empty List For The Return Value
		res = []
		# Get All The Part Sets In The Scene
		partsets = Find_All_Part_Sets()
		# Check If The Input Names Is empty
		if not len(names):
			# If so Add A Default Name
			names.append("AW_Vray_Part_Set")
		# Iterate Through Each name
		for name in names:
			# Create a VRayObjectProperty
			objectProperty  = self._DGmod.createNode("VRayObjectProperties")
			self._DGmod.doIt()
			# Set The Newly Created Objects Name
			self._DGmod.renameNode(objectProperty, name)
			self._DGmod.doIt()
			# Add The New Object To The Return Value
			res.append(objectProperty)
			# Get A MPlug For The message Attribute Of The New Object
			message_plg = to_Old_MPlug(objectProperty, "message")
			# Iterate Through Each PartSet
			for partset in partsets:
				# Connect The New Object To The dependincy Set Member Attribute
				partset.connect_To_Next_dnSetmembers(self._DGmod, message_plg)
		
		return res
	#----------------------------------------------------------------------
	def remove_Vray_ObjectProperties(self, part_sets, name):
		""""""
		## Create A Default Scene State
		isinstance(part_sets, AW_Part_Sets)
		# Build A Temp Function To Access The MObjects
		fnDepend = OpenMaya.MFnDependencyNode()
		
		part_set  = part_sets.get_Part_Set_By_Name(name)
		if part_set is not None:
			plgA = to_Old_MPlug(part_set, "message")
			for plgB in get_Connected_Plugs(plgA, asDst=True, asSrc=False):
				self._DGmod.disconnect(plgA, plbB)
				self._DGmod.doIt()
			
			self._DGmod.deleteNode(child)
			self._DGmod.doIt()
	#----------------------------------------------------------------------
	def create_New_State_Manager(self, name=None):
		""""""
		fnDN           = OpenMaya.MFnDependencyNode()
		# Create The Scene States Manager Node
		state_Manager_object = self._DGmod.createNode(AW_Scene_State_Manager.kNodeId)
		self._DGmod.doIt()
		# Get The Python Class Instances
		state_Manager_Node      = AW_Scene_State_Manager.scan_tracking_Data(state_Manager_object)
		
		# Set The Scene States Manager Name
		if name is not None:
			self._DGmod.renameNode(state_Manager_object, name)
		else:
			self._DGmod.renameNode(state_Manager_object, "AW_Scene_States_Manager")
		self._DGmod.doIt()
		
			
		# Create The Scene States Container
		states_list_object = self._DGmod.createNode(AW_Scene_State_List.kNodeId)
		self._DGmod.doIt()
		# Get The Python Class Instance
		states_list        = AW_Scene_State_List.scan_tracking_Data(states_list_object)
		
		# Set The Scene States List Name
		self._DGmod.renameNode(states_list_object, "AW_Scene_States_List")
		self._DGmod.doIt()
		
		# Create The Part Sets Container
		part_sets_object   = self._DGmod.createNode(AW_Part_Sets.kNodeId)
		self._DGmod.doIt()
		# Get The Python Class Instance
		part_sets          = AW_Part_Sets.scan_tracking_Data(part_sets_object)
		
		# Set The Part Sets List Name
		self._DGmod.renameNode(part_sets_object, "AW_Part_Sets_List")
		self._DGmod.doIt()
		
		for item in [states_list, part_sets]:
			state_Manager_Node.connect_To_Next_dnSetmembers(self._DGmod, item.Plug_message)
		
		scene_state   = self.create_scene_state(states_list, [])
		
		return state_Manager_Node
	#----------------------------------------------------------------------
	def isUndoable(self):
		return True
	#----------------------------------------------------------------------
	def find_manager(self):
		"""Finds A Scene State Manager Eather from the user input or by the active selection list"""
		# Set The Default Value
		manager_name = None
		# Check if The Flat Has Been set
		if self.argData.isFlagSet(kManager_Flag):
			# Get The Name Of The Manager From The input
			manager_name = self.argData.flagArgumentString(kManager_Flag, 0)
			# Find The Class instance That Matches The input name
			manager = Find_Scene_State_Manager_From_Input_String(manager_name)
		# Get The Name Of The Manager From The Active Selection List
		else:
			# Find The Class instance From The Active Selection List
			manager = Find_Scene_State_Manager_From_Active_Selection()
		isinstance(manager, AW_Scene_State_Manager)
		return manager
	#----------------------------------------------------------------------
	def get_Assinment_Type(self):
		for v, flag in zip([kBeauty, kMatte, kInvisible], [kBeauty_Flag,kMatte_Flag,kInvisible_Flag]):
			if self.argData.isFlagSet(flag):
				return v
	#----------------------------------------------------------------------
	def doIt(self, args):
		"""Starting Point Of Mel Command"""
		# Collect The Input Key Words From The User
		self.argData = OpenMaya.MArgDatabase(self.syntax(), args)
		# Get The Input args as a list of strings
		self.argList = extract_args(args)
		# Check If the Edit Flat is set
		if self.argData.isEdit():
			# if so enter edit mode
			self.doIt_Edit_Mode()
		# Check If the Query Flat is set
		elif self.argData.isQuery():
			# if so enter query mode
			self.doIt_Query_Mode()
		# else enter create mode
		else:
			self.doIt_Create_Mode()
	#----------------------------------------------------------------------
	def doIt_Edit_Mode(self):
		"""All Operatrions that invalve changing the structure of a state manager"""
		if self.argData.isFlagSet(kName_Flag):
			name = self.argData.flagArgumentString(kName_Flag, 0)
		else:
			name = None
		# Check if The Assine Parts Flag is set
		# When This Flag is Set To True Then
		# The Speified Part Sets Will Be Asseined
		# To A Spacife State On A Spicfied Scene State
		if self.argData.isFlagSet(kAssinPart_Flag):
			# Get The Scene State Manager That We Will Be Editing
			manager = Find_AW_Scene_State_Manager()
			# Check To Make Sure That A Scene State Manager Was Found
			# If Raise And Error
			if manager == None:
				message = "Could Not Find The 'AW_Scene_State_Manager'"
				OpenMaya.MGlobal.displayError(message)
				raise ValueError(message)
			else:
				# Check If Any State Types Have Been Specified
				# if not Raise and Error
				if not any([self.argData.isFlagSet(kBeauty_Flag), self.argData.isFlagSet(kMatte_Flag), self.argData.isFlagSet(kInvisible_Flag)]):
					message = "When Assining Part Sets To States you must set the type of assinment flag -%s/-%s,-%s/-%s,-%s/-%s" % (kBeauty_Flag,kBeauty_LongFlag, kMatte_Flag, kMatte_LongFlag, kInvisible_Flag, kInvisible_LongFlag)
					OpenMaya.MGlobal.displayError(message)
					raise KeyError(message)
				else:
					# Check To make Sure That A Scene State Has Been Specifed
					# If not raise and error
					if not self.argData.isFlagSet(kState_Flag):
						message = "When Assining Part Sets To A State you must set the -%s/-%s flag for the State That The PartSets Are to be assined to" % (kState_Flag,kState_LongFlag)
						OpenMaya.MGlobal.displayError(message)
						raise KeyError(message)
					else:
						# Check To Make Sure That Parts Have Been Specifed
						# If Not Raise an Error
						if not self.argData.isFlagSet(kPartSet_Flag):
							message = "When Assining Part Sets To A State you must set the -%s/-%s flag for the parts to assined" % (kPartSet_Flag,kPartSet_LongFlag)
							OpenMaya.MGlobal.displayError(message)
							raise KeyError(message)
						# Collect The Itme and Preform The New Assinmets
						else:
							# Get The New State Thate Will Be Used For Part Assinment
							self.assinment_type = self.get_Assinment_Type()
							# Get the name of The scene State To Be Used
							state_name = self.argData.flagArgumentString(kState_Flag, 0)
							# Get The List Of Part Set Names To Be Assied To The State
							part_set_names   = extract_String_Args_For_Flag(kPartSet_Flag, self.argData)
							# Get The Child States List Form The Manager Specifed By the User
							states_list      = manager.get_States_List()
							# Get The Child Part Sets List Form The Manager Specifed By the User
							part_sets_list   = manager.get_Part_Sets()
							# From The Name Find The Scene State Class Instance
							scene_state      = states_list.get_Scene_State_By_Name(state_name)
							# Using The Scene State Get The Part Set Contaner state type
							assinement_state = scene_state.get_State_Type(self.assinment_type)
							# Convert The List Of Part Set Names To There Vray ObjectPropties 
							part_sets        = part_sets_list.Names_To_Part_Sets(part_set_names)
							# Using The Assinment State Preform The New Assinmets
							assinement_state.Assine_Part_set(self._DGmod, part_sets)
		# Check if The UnAssine Parts Flag is set
		# When This Flag is Set To True Then
		# The Speified Part Sets Will Be UnAsseined
		# From A Spacife State
		elif self.argData.isFlagSet(kUnAssinePart_Flag):
			# Get The Scene State Manager That We Will Be Editing
			manager = Find_AW_Scene_State_Manager()
			# Check To Make Sure That A Scene State Manager Was Found
			# If Raise And Error
			if manager == None:
				message = "Could Not Find The 'AW_Scene_State_Manager'"
				OpenMaya.MGlobal.displayError(message)
				raise ValueError(message)
			else:
				# Check To make Sure That A Scene State Has Been Specifed
				# If not raise and error
				if not self.argData.isFlagSet(kState_Flag):
					message = "When UnAssining Part Sets From A State you must set the -%s/-%s flag for the State That The PartSets Are to be Unassined From" % (kState_Flag,kState_LongFlag)
					OpenMaya.MGlobal.displayError(message)
					raise KeyError(message)
				else:
					# Check To Make Sure That Parts Have Been Specifed
					# If Not Raise an Error
					if not self.argData.isFlagSet(kPartSet_Flag):
						message = "When UnAssining Part Sets From A State you must set the -%s/-%s flag for the parts to Unassined" % (kPartSet_Flag,kPartSet_LongFlag)
						OpenMaya.MGlobal.displayError(message)
						raise KeyError(message)
					# Collect The Itme and Preform The New Assinmets
					else:
						# Get the name of The scene State To Be Used
						state_name = self.argData.flagArgumentString(kState_Flag, 0)
						# Get The List Of Part Set Names To Be Assied To The State
						part_set_names   = extract_String_Args_For_Flag(kPartSet_Flag, self.argData)
						# Get The Child States List Form The Manager Specifed By the User
						states_list      = manager.get_States_List()
						# Get The Child Part Sets List Form The Manager Specifed By the User
						part_sets_list   = manager.get_Part_Sets()
						# From The Name Find The Scene State Class Instance
						scene_state      = states_list.get_Scene_State_By_Name(state_name)
						# Convert The List Of Part Set Names To There Vray ObjectPropties 
						part_sets        = part_sets_list.Names_To_Part_Sets(part_set_names)
						
						for assinement_state in [scene_state.get_Beauty(), scene_state.get_Matte(), scene_state.get_Invisible()]:
							# Using The Assinment State Preform The unAssinmets
							assinement_state.UnAssine_Part_set(self._DGmod, part_sets)
		# Check if The Assin Nodes Flag is set
		# When This Flag is Set To True Then
		# The Speified Nodes Will Be Removed From There Current Part Set and
		# Asseined To The Spacife One
		elif self.argData.isFlagSet(kAssinNodes_Flag):
			# Check To Make Sure That A Part Set Has Been Specifed
			# If Not Raise an Error
			if not self.argData.isFlagSet(kPartSet_Flag):
				message = "When Assining Nodes To A Part Set you must set the -%s/-%s flag for the part that the nodes will be assined to" % (kPartSet_Flag,kPartSet_LongFlag)
				OpenMaya.MGlobal.displayError(message)
				raise KeyError(message)
			else:
				# Check To Make Sure That Nodes Has Been Specifed
				# If Not Raise an Error
				if not self.argData.isFlagSet(kNode_Flag):
					message = "When Assining Nodes To A Part Set you must set the -%s/-%s flag for the Nodes that will be assined Part" % (kNode_Flag,kNode_LongFlag)
					OpenMaya.MGlobal.displayError(message)
					raise KeyError(message)
				else:
					# Get The Part Set Name 
					part_name = self.argData.flagArgumentString(kPartSet_Flag, 0)
					# Convert Name To A Maya.MObject
					part_obj   = to_Old_MObject(part_name)
					# Create A Custom Vray ObjectProperty Wrapper Instances
					part       = ObjectProperties(part_obj)
					# Get All The Input Nodes To Assine
					node_names = extract_String_Args_For_Flag(kNode_Flag, self.argData)
					# iterate through each node
					for node_name in node_names:
						# Convert it to an MObject
						node = to_Old_MObject(node_name)
						# Apply New Assinments
						part.add_Members(self._DGmod, node)
		# Check if The Add Part Set Flag is set
		# When This Flag is Set To True Then
		# The User As Spified To Create A New Part Set 
		# And Add It To The Spacifed Scene State Manager
		elif self.argData.isFlagSet(kAddPartSet_Flag):
			# Create and Empty list That will Bold The command Return value
			res = []
			# Set The Default Value Of The Parts To Be Created
			parts = []
			# Check if Part Set Flag Has Been Set
			if self.argData.isFlagSet(kPartSet_Flag):
				# If So Get All The Names Of The Part Sets To Be Created
				parts = extract_String_Args_For_Flag(kPartSet_Flag, self.argData)
			# Other Wise Check If The Name Flag Was Set 
			elif name != None:
				# If So Set The Part Names To A Single Item list containg The Name
				parts = [name]
			# Create The New Part Sets AKA (VRayObjectProperties)
			objects = self.create_VRayObjectProperties(parts)
			# Iterate Through Each Created Object
			for obj in objects:
				# Set The Global Depend Function Set To The Object To Ascces The Object Name
				G_dependFn.setObject(obj)
				# Add The New To The Command Return Value
				res.append(G_dependFn.name())
			# Set The Result of this command to the list of names of VRayObjectProperties created
			OpenMayaMPx.MPxCommand.setResult(res)
		# Check if The Remove State Flag is set
		# When This Flag is Set To True Then
		# The Spified Scene State Will Be Deleted
		# From The Spacifed Scene State Manager
		elif self.argData.isFlagSet(kRemoveState_Flag):
			# Get The Scene State Manager That We Will Be Editing
			manager = Find_AW_Scene_State_Manager()
			# Check To Make Sure That A Scene State Manager Was Found
			# If Raise And Error
			if manager == None:
				message = "Could Not Find The 'AW_Scene_State_Manager'"
				OpenMaya.MGlobal.displayError(message)
				raise ValueError(message)
			else:
				# Check If States Have Been Specified
				if not self.argData.isFlagSet(kState_Flag):
					message = "When Removing A Scene Statea you must set the -%s/-%s Flag to a to a list of scene state names" % (kState_Flag,kState_LongFlag)
					OpenMaya.MGlobal.displayError(message)
					raise ValueError(message)
				else:
					# Get The list of scene state names
					states = extract_String_Args_For_Flag(kState_Flag, self.argData)
					states_list = manager.get_States_List()
					# Remove The Scene States
					self.remove_scene_states(states_list, states)
		# Check if The Add State Flag is set
		# When This Flag is Set To True Then
		# Scene State Will Be Created
		# For The Spacifed Scene State Manager
		elif self.argData.isFlagSet(kAddState_Flag):
			# Get The Scene State Manager That We Will Be Editing
			manager = Find_AW_Scene_State_Manager()
			# Check To Make Sure That A Scene State Manager Was Found
			# If Raise And Error
			if manager == None:
				message = "Could Not Find The 'AW_Scene_State_Manager'"
				OpenMaya.MGlobal.displayError(message)
				raise ValueError(message)
			else:
				# Set The Default Value
				states = []
				# Check If The State Names Have Been Specifed
				if self.argData.isFlagSet(kState_Flag):
					# Get The State Names From The Flag
					states = extract_String_Args_For_Flag(kState_Flag, self.argData)
				# Or Check If The Name Has Been Specifed
				elif self.argData.isFlagSet(kName_Flag):
					# Get The State Names From The Flag
					states = extract_String_Args_For_Flag(kName_Flag, self.argData)
				states_list =  manager.get_States_List()
				# Create The New Scene States
				scene_state_nodes = self.create_scene_state(states_list, states)
				# Generate A List Of scene states names for command return
				res = [item.name() for item in scene_state_nodes]
				# Set The Command Return Value	
				OpenMayaMPx.MPxCommand.setResult(res)
	#----------------------------------------------------------------------
	def doIt_Query_Mode(self):
		""""""
	#----------------------------------------------------------------------
	def doIt_Create_Mode(self):
		""""""
		state_Manager = Find_AW_Scene_State_Manager()
		if not isinstance(state_Manager, AW_Scene_State_Manager):
			state_Manager = self.create_New_State_Manager(None)
		OpenMayaMPx.MPxCommand.setResult(state_Manager.name())
	#----------------------------------------------------------------------
	def undoIt(self):
		self._DGmod.undoIt()
	#----------------------------------------------------------------------
	def redoIt(self):
		self._DGmod.doIt()
#----------------------------------------------------------------------
def cmdCreator():
	return OpenMayaMPx.asMPxPtr(AW_Scene_State_Command())
#----------------------------------------------------------------------
def cmdSyntaxCreator():
	syntax = OpenMaya.MSyntax()
	syntax.enableEdit(True)
	syntax.enableQuery(True)
	syntax.setObjectType(OpenMaya.MSyntax.kSelectionList)
	syntax.useSelectionAsDefault(True)
	syntax.addFlag(kName_Flag     , kName_LongFlag, OpenMaya.MSyntax.kString)
	
	syntax.addFlag(kAssinPart_Flag, kAssinPart_LongFlag)
	syntax.addFlag(kBeauty_Flag   , kBeauty_LongFlag)
	syntax.addFlag(kInvisible_Flag, kInvisible_LongFlag)
	syntax.addFlag(kMatte_Flag    , kMatte_LongFlag)
	syntax.addFlag(kUnAssinePart_Flag , kUnAssinePart_LongFlag)
	
	syntax.addFlag(kAddState_Flag     , kAddState_LongFlag)
	syntax.addFlag(kRemoveState_Flag  , kRemoveState_LongFlag)
	syntax.addFlag(kAddPartSet_Flag   , kAddPartSet_LongFlag)
	syntax.addFlag(kRemovePartSet_Flag, kRemovePartSet_LongFlag)
	
	syntax.addFlag(kPartSet_Flag      , kPartSet_LongFlag, OpenMaya.MSyntax.kString)
	syntax.addFlag(kState_Flag        , kState_LongFlag, OpenMaya.MSyntax.kString)
	syntax.addFlag(kManager_Flag      , kManager_LongFlag, OpenMaya.MSyntax.kString)
	syntax.addFlag(kNode_Flag         , kNode_LongFlag, OpenMaya.MSyntax.kString)
	syntax.addFlag(kAssinNodes_Flag   , kAssinNodes_LongFlag)
	syntax.addFlag(kUnAssineNodes_Flag, kUnAssineNodes_LongFlag)
	
	syntax.makeFlagMultiUse(kPartSet_Flag)
	syntax.makeFlagMultiUse(kState_Flag)
	syntax.makeFlagMultiUse(kNode_Flag)
	return syntax

fileOpenCB = 0
fileNewCB = 0
#----------------------------------------------------------------------
def clearTrackingDictionaries(unused):
	AW_Scene_State_Manager._active_instance = None
	for node in _Node_definition_Class_List:
		node.kTrackingDictionary = {}
		
menus = []
# initialize the script plug-in
#----------------------------------------------------------------------
def initializePlugin(mobject):
	global  fileNewCB, fileOpenCB, menus
	fileOpenCB = OpenMaya.MSceneMessage.addCallback( OpenMaya.MSceneMessage.kBeforeOpen,clearTrackingDictionaries)
	fileNewCB  = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kBeforeNew,clearTrackingDictionaries)
	
	mplugin = OpenMayaMPx.MFnPlugin(mobject, "Autodesk", "1.0", "Any")
	try:
		mplugin.registerCommand(kCmdName, cmdCreator, cmdSyntaxCreator)
	except:
		sys.stderr.write("Failed to register command: %s" % kCmdName)
		raise
	for node in _Node_definition_Class_List:
		try:
			mplugin.registerNode(node.kNodeName, node.kNodeId, node.nodeCreator, node.nodeInitializer, OpenMayaMPx.MPxNode.kObjectSet)
		except:
			sys.stderr.write("Failed to register node: %s" % node.kNodeName)
			raise
	menus = mplugin.addMenuItem("Create Scene State Manager", 'mainCreateMenu', "awSceneState", "")
	menus.extend(mplugin.addMenuItem("Add Scene State", 'mainCreateMenu', "awSceneState -ast", ""))
# uninitialize the script plug-in
#----------------------------------------------------------------------
def uninitializePlugin(mobject):
	global  fileNewCB, fileOpenCB, menus
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand(kCmdName)
	except:
		sys.stderr.write("Failed to deregister command: %s" % kCmdName)
		raise
	for node in _Node_definition_Class_List:
		try:
			mplugin.deregisterNode(node.kNodeId)
		except:
			sys.stderr.write("Failed to deregister node: %s" % node.kNodeName)
			raise

	if fileOpenCB != 0:
		OpenMaya.MSceneMessage.removeCallback(fileOpenCB)
		fileOpenCB = 0

	if fileNewCB != 0:
		OpenMaya.MSceneMessage.removeCallback(fileNewCB)
		fileNewCB = 0
	mplugin.removeMenuItem(menus)