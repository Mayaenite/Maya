#!/usr/bin/env python
import maya.api.OpenMaya as newOM
import maya.OpenMaya as oldOM
import maya.cmds as cmds
from functools import wraps
import Class_Comands
import sys
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def __simplafy_Source_Analises(item):
	new_item = item
	return new_item
########################################################################
class Error(Exception):
	"""Base class for exceptions in this module."""
	pass
########################################################################
class NothingSelectedError(Error):
	"""Exception raised When A Selection is Required But Nothing Is Selected."""
	#----------------------------------------------------------------------
	def __init__(self):
		self.message = "There Was Nothing Selected Please Select Somthing And Try Again"
########################################################################
class MObjectCreationError(Error):
	"""Exception raised When The Input Giving Could Not Be Converted To A Valid MObject."""
	#----------------------------------------------------------------------
	def __init__(self, inVal):
		self.message = "The Input Value Giving %r Could Not Be Converted To A Valid MObject" % inVal
########################################################################
class MDagPathCreationError(Error):
	"""Exception raised When The Input Giving Could Not Be Converted To A Valid MDagPath Object."""
	#----------------------------------------------------------------------
	def __init__(self, inVal):
		self.message = "The Input Value Giving %r Could Not Be Converted To A Valid MDagPath" % inVal
########################################################################
class MPlugCreationError(Error):
	"""Exception raised When The Input Giving Could Not Be Converted To A Valid MDagPath Object."""
	#----------------------------------------------------------------------
	def __init__(self, inVal):
		self.message = "The Input Value Giving %r Could Not Be Converted To A Valid MPlug" % inVal

#----------------------------------------------------------------------
def next_active_id():
	""""""
	with file(os.path.join(os.path.dirname(__file__), "Active_id.txt"), "r") as f:
		line = int(f.readline())
	with file(os.path.join(os.path.dirname(__file__), "Active_id.txt"), "w") as f:
		f.write(str(line+1))
	return line
#---------------------------------------------------------------------------------
def find_Node_By_IDkey(key):
	node = [att.split(".")[0] for att in cmds.ls("*.object_id_key") if cmds.getAttr(att) == key]
	if len(node):
		return node[0]
	else:
		return None
# Context Managers and Decorators ---
#---------------------------------------------------------------------------------
########################################################################
class ScriptJobIdWrapper(object):
	'''Wrapper class to handle cleaning up of MCallbackIds from registered MMessage
	'''
	def __init__(self, callbackId):
		self.callbackId = callbackId

	def __del__(self):
		try:
			cmds.scriptJob(kill=self.callbackId)
		except:
			pass

	def __repr__(self):
		return 'ScriptJobIdWrapper(%r)'%self.callbackId
########################################################################
class HashableMObjectHandle(oldOM.MObjectHandle):
	'''
	Hashable MObjectHandle referring to an MObject that can be used as a key in a dict.
		:See MObjectHandle documentation for more information.
	'''
	#----------------------------------------------------------------------
	def __hash__(self):
		'''
		Use the proper unique hash value unique to the MObject
		that the MObjectHandle points to
		so this class can be used as a key in a dict.
		:Return:
			MObjectHandle.hasCode()
			unique memory address for the MObject that is hashable
		'''
		return self.hashCode()
	#----------------------------------------------------------------------
	def new_api_object(self):
		""""""
		return Convert_MObject(self.object(),force_new=True)
		
# ==============
# UNDO BLOCKS
#   Classes to be used with the 'with' command to denote specific blocks
#   that should handle undo in a certain way
# ==============

########################################################################
class MayaUndoChunk(object):
	'''
	Safe way to manage group undo chunks using the 'with' command.
	It will close the chunk automatically on exit from the block
	:Example:
		cmds.polyCube()
		with MayaUndoChunk():
			cmds.polyCube()
			cmds.polyCube()
		cmds.undo()
	'''
	#----------------------------------------------------------------------
	def __enter__(self):
		cmds.undoInfo(openChunk=True)
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		cmds.undoInfo(closeChunk=True)
########################################################################	
class MayaSkipUndoChunk(object):
	'''
	Safe way to using the 'with' command
	to create a block of commands that are not added to the undo queue.
	It will close the chunk automatically on exit from the block and
	restore the existing undo state.

	:Example:
	    cmds.polyCube()
	    with MayaSkipUndoChunk():
	        cmds.polyCube()
	        cmds.polyCube()
	    cmds.polyCube()
	'''
	#----------------------------------------------------------------------
	def __enter__(self):
		self.undoState = cmds.undoInfo(q=True, state=True)
		if self.undoState == True:
			cmds.undoInfo(stateWithoutFlush=False)
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		if self.undoState == True:
			cmds.undoInfo(stateWithoutFlush=True)
#----------------------------------------------------------------------
def nodeLockManager(func):
	'''
	Simple decorator to manage metaNodes which are locked. Why lock??
	Currently just the metaRig and therefore any subclasses of that are locked.
	The reason is that the Maya 'network' node I use has issues when certain
	connections are deleted, the node itself can get deleted and cleanup, removing
	the entire network! Try it, make a metaNode and key an attr on it, then run
	cutKeys...the node will be deleted.

	This decorator is used to manage the unlocking of self for all calls that
	require change access rights to the 'network' node itself.
	'''
	@wraps(func)
	def wrapper(*args, **kws):
		res = None
		err = None
		plg = None
		plglocked = False
		locked=False
		try:
			mNode=args[0]  # args[0] is self
			if isinstance(mNode, MPLUG):
				plg   = mNode
				mNode = mNode.node
				plglocked = plg.locked
			locked = cmds.lockNode(mNode.name,q=True,lock=True)[0]
			if locked:
				cmds.lockNode(mNode.name,lock=False)
			if plglocked:
				cmds.setAttr(plg,lock=False)
			res=func(*args, **kws)
		except StandardError, error:
			err=error
		finally:
			if isinstance(plg, MPLUG):
				if plglocked and not func.func_name == "unlock":
					cmds.setAttr(plg,lock=True)
			if locked and cmds.objExists(mNode.name):
				cmds.lockNode(mNode.name, lock=True)
			if err:
				traceback = sys.exc_info()[2]  # get the full traceback
				raise StandardError(StandardError(err), traceback)
			return res
	return wrapper
# MOBJECT Utilty Functions ---
#----------------------------------------------------------------------
def ChildShape(Transform):
	"""returns the fisrt child shape or None if there is no shape connteced to this transform"""
	childern = cmds.listRelatives(Transform,children=True,shapes=True,fullPath=True)
	if childern:
		#CHECKS TO SEE IF CHILD SHAPES ARE PRESENT
		#RETURNES ONLY THE FIRST CHILD
		return childern[0]
	else:
		#RETURN NONE IF THERE IS NO SHAPE CONNTECED TO THIS TRANSFORM
		return childern;
#----------------------------------------------------------------------
def ShapeType(Transform):
	shape = ChildShape(Transform)
	if shape:
		#GET THE NODE TYPE OF THE GIVEN SHAPE
		return cmds.objectType(shape)
	else:
		#IF THERE WAS NO SHAPE FOUND FOR DAG TRAVERSING PURPUSES WE WILL RETURN THE WORD GROUP
		return "group"
#----------------------------------------------------------------------
def Seperate_Attribute_Element_Name(attName):
	""""""
	index = None
	if "[" in attName.split(".")[-1]:
		items = attName.split(".")[-1].split("[", 1)
		attName, index = items[0], int(items[1].replace("]", "").strip())
	return attName, index
#----------------------------------------------------------------------
def is_Old_API(obj):
	""""""
	return obj.__class__.__module__ == 'maya.OpenMaya'
#----------------------------------------------------------------------
def _isValidMObjectHandle(obj):
	if isinstance(obj, (oldOM.MObjectHandle, newOM.MObjectHandle)) :
		return obj.isValid() and obj.isAlive()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMObject(obj):
	if isinstance(obj, (oldOM.MObject, newOM.MObject)):
		return not obj.isNull()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMPlug(obj):
	if isinstance(obj, (oldOM.MPlug, newOM.MPlug)):
		if isinstance(obj, oldOM.MPlug):
			return not obj.isNull()
		else:
			return not obj.isNull
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagPath(obj):
	if isinstance(obj, (oldOM.MDagPath, newOM.MDagPath)):
		# when the underlying MObject is no longer valid, dag.isValid() will still return true,
		# but obj.fullPathName() will be an empty string
		return obj.isValid() and obj.fullPathName()
	else :
		return False
#----------------------------------------------------------------------
def _isValidMNode(obj):
	if _isValidMObject(obj) :
		return obj.hasFn(oldOM.MFn.kDependencyNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagNode(obj):
	if _isValidMObject(obj) :
		return obj.hasFn(oldOM.MFn.kDagNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValidMNodeOrPlug(obj):
	return _isValidMPlug(obj) or _isValidMNode (obj)
#----------------------------------------------------------------------
def get_Active_Selection_List(OldApi=True):
	"""Gets All The Objects Currently Selected In Maya"""
	# User The Old Api
	if OldApi:
		# Create A Storage Container For The Active Selection
		selectionList = oldOM.MSelectionList()
		# Fill The Container With The Active Selection
		oldOM.MGlobal.getActiveSelectionList(selectionList)
		# Return The Selection List
		return selectionList
	# Else Use The New Api
	else:
		# Get The Active Selection
		selectionList = newOM.MGlobal.getActiveSelectionList()
		# Return The Selection List
		return selectionList
#----------------------------------------------------------------------
def get_Active_Selection_List_Names(OldApi=True):
	"""Gets All The Objects Currently Selected In Maya"""
	selectionList = get_Active_Selection_List(OldApi)
	if OldApi:
		names = []
		selectionList.getSelectionStrings(names)
		return names
	else:
		names = selectionList.getSelectionStrings()
		return names
#----------------------------------------------------------------------
def to_New_MObject(nodeName):
	""" Get the API MObject given the name of an existing node """
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	obj = None
	if _isValidMObject(nodeName):
		obj = nodeName
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	elif isinstance(nodeName, (str, unicode)):
		sel = newOM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( nodeName )
		# ASSINE THE ADDED ITEM
		obj = sel.getDependNode(0)
	# CHECK IF THE INPUT CANTAINS A FUNCTION TO RETRIVE AN MOBJECT
	elif hasattr(nodeName, "object"):
		# RETRIVE THE MOBJECT
		obj = nodeName.object()
	#ONE LAST CHECK TO MAKE SURE A VALID MOBJECT WAS AQUARIED
	if not _isValidMObject(obj):
		raise MObjectCreationError(nodeName)
	return obj
#----------------------------------------------------------------------
def to_Old_MObject(nodeName):
	""" Get the API MObject given the name of an existing node """
	obj = None
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	if _isValidMObject(nodeName):
		obj = nodeName
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	elif isinstance(nodeName, (str, unicode)):
		# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
		obj = oldOM.MObject()
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = oldOM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( nodeName )
		# ASSINE THE ADDED ITEM
		sel.getDependNode( 0, obj )
	# CHECK IF THE INPUT CANTAINS A FUNCTION TO RETRIVE AN MOBJECT
	elif hasattr(nodeName, "object"):
		# RETRIVE THE MOBJECT
		obj = nodeName.object()
	#ONE LAST CHECK TO MAKE SURE A VALID MOBJECT WAS AQUARIED
	if not _isValidMObject(obj):
		raise MObjectCreationError(nodeName)
	return obj
#----------------------------------------------------------------------
def toMObject(nodeName, OldApi=True):
	""" Get the API MObject given the name of an existing node """
	if OldApi:
		obj = to_Old_MObject(nodeName)
	else:
		obj = to_New_MObject(nodeName)
	isinstance(obj, oldOM.MObject)
	return obj
#----------------------------------------------------------------------
def to_New_MPlug(plugName):
	""" Get the API MObject given the name of an existing node """
	plug = None
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	if _isValidMPlug(plugName):
		plug = plugName
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	elif isinstance(plugName, (str, unicode)):
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = newOM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( plugName )
		# ASSINE THE ADDED ITEM
		plug = sel.getPlug(0)
	#ONE LAST CHECK TO MAKE SURE A VALID MOBJECT WAS AQUARIED
	if not _isValidMPlug(plug):
		raise MPlugCreationError(plugName)
	return plug
#----------------------------------------------------------------------
def to_Old_MPlug(plugName):
	""" Get the API MObject given the name of an existing node """
	plug = None
	#CHECK IF THE INPUT IS ALREADY A MOBJECT
	if _isValidMPlug(plugName):
		plug = plugName
	# CHECK THE INPUT TO SEE IF IT IS THE OBJECT NAME
	elif isinstance(plugName, (str, unicode)):
		# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
		plug = oldOM.MPlug()
		# MAKE A SELECTIONLIST STORAGE CONTAINER
		sel = oldOM.MSelectionList()
		# ADD IT TO STORAGE CONTAINER
		sel.add( plugName )
		# ASSINE THE ADDED ITEM
		sel.getPlug( 0, plug )
	#ONE LAST CHECK TO MAKE SURE A VALID MOBJECT WAS AQUARIED
	if not _isValidMPlug(plug):
		raise MPlugCreationError(plugName)
	return plug
#----------------------------------------------------------------------
def toMPlug(plugName, OldApi=True):
	""" Get the API MObject given the name of an existing node """
	if OldApi:
		plug = to_Old_MPlug(plugName)
	else:
		plug = to_New_MPlug(plugName)
	isinstance(plug, oldOM.MPlug)
	return plug
#----------------------------------------------------------------------
def make_MObjectHandle(obj):
	""" Get the API MObjectHandle"""
	obj = Convert_MObject(obj, force_old=True)
	handle = HashableMObjectHandle(obj)
	return handle
#----------------------------------------------------------------------
def to_New_MDagPath(nodeName):
	""" Get the API MObject given the name of an existing node """
	obj = toMObject(nodeName, OldApi=False)
	if not _isValidMDagNode(obj):
		raise ValueError("The input Node %s Is Not A Valid MDagPath Object" % nodeName)
	dagpath =  newOM.MDagPath.getAPathTo(obj)
	isinstance(dagpath, newOM.MDagPath)
	return dagpath
#----------------------------------------------------------------------
def to_Old_MDagPath(nodeName):
	""" Get the API MObject given the name of an existing node """
	obj = toMObject(nodeName, OldApi=True)
	if not _isValidMDagNode(obj):
		raise ValueError("The input Node %s Is Not A Valid MDagPath Object" % nodeName)
	dagpath = oldOM.MDagPath.getAPathTo(obj)
	isinstance(dagpath, oldOM.MDagPath)
	return dagpath
#----------------------------------------------------------------------
def toMDagPath(nodeName, OldApi=True):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if OldApi:
		dagPath = to_Old_MDagPath(nodeName)
	else:
		dagPath = to_New_MDagPath(nodeName)
	return dagPath
#----------------------------------------------------------------------
def get_Function_Set(nodeName, OldApi=True):
	"""Get The Maya Function Set That Is Appropriate For The Givin MObject"""
	if OldApi:
		fnTypes = oldOM.MFn
		mod     = oldOM
	else:
		fnTypes = newOM.MFn
		mod     = newOM
		
	obj = toMObject(nodeName, OldApi)
	
	if obj.hasFn(fnTypes.kTransform):
		return mod.MFnTransform(obj)
	elif obj.hasFn(fnTypes.kMesh):
		return mod.MFnMesh(obj)
	elif obj.hasFn(fnTypes.kDagNode):
		return mod.MFnDagNode(obj)
	# elif obj.hasFn(fnTypes.kAttribute):
		# if obj.hasFn(fnTypes.kNumericAttribute):
			# return mod.MFnNumericAttribute(obj)
		# elif obj.hasFn(fnTypes.kCompoundAttribute):
			# return mod.MFnCompoundAttribute(obj)
		# elif obj.hasFn(fnTypes.kTypedAttribute):
			# return mod.MFnTypedAttribute(obj)
		# elif obj.hasFn(fnTypes.kMessageAttribute):
			# return mod.MFnMessageAttribute(obj)
		# elif obj.hasFn(fnTypes.kMatrixAttribute):
			# return mod.MFnMatrixAttribute(obj)
		# elif obj.hasFn(fnTypes.kGenericAttribute):
			# return mod.MFnGenericAttribute(obj)
		# elif obj.hasFn(fnTypes.kEnumAttribute):
			# return mod.MFnEnumAttribute(obj)
		# else:
			# return mod.MFnAttribute(obj)
	elif obj.hasFn(fnTypes.kDependencyNode):
		return mod.MFnDependencyNode(obj)
#----------------------------------------------------------------------
def nameToNode( nodeName=None ,asobj=False, aspath=False, asplug=False, OldApi=True):
	"""function that returns a node object given a name"""
	res = None
	if nodeName is None:
		# IF NOT GET THE CURRENTLY ACTIVE SELECTIONLIST
		names  = get_Active_Selection_List_Names(OldApi)
		if not len(names):
			oldOM.MGlobal.displayError("Nothing Currently Selected And No Input was Given")
			raise NothingSelectedError()
		nodeName = names[0]
		
	if asobj:
		res = toMObject(nodeName, OldApi)
	elif aspath:
		res = toMDagPath(nodeName, OldApi)
	elif asplug:
		res = toMPlug(nodeName, OldApi)
	else:
		res = get_Function_Set(nodeName, OldApi)
	resFn = __simplafy_Source_Analises(res)
	return resFn
#----------------------------------------------------------------------
def nameToPlug( node, attrName=None, OldApi=True):
	"""function that finds a plug given a node object and plug name"""
	# CHECK IF THE INPUT NODE IS NOT AND NODE OBJECT BUT THE NAME OF AN OBJECT
	plug = None
	if isinstance(node, (str, unicode)):
		if node.count("."):
			plug = toMPlug(node, OldApi=OldApi)
		else:
			if isinstance(attrName, (str, unicode)):
				node_fn = nameToNode(node, OldApi=OldApi)
				node_name = ".".join([node_fn.name(), attrName])
				plug = toMPlug(node_name, OldApi=OldApi)
			else:
				raise ValueError("node input was not an attribute and the attrName input was left blank")
			
	elif _isValidMPlug(node):
		plug = node
	elif _isValidMObject(node):
		node_fn = nameToNode(node, OldApi)
		plug = toMPlug(node_fn.name())
	else:
		raise MPlugCreationError(node)
	return plug
#----------------------------------------------------------------------
def Convert_MObject(obj, force_old=False, force_new=False):
	if is_Old_API(obj):
		if force_old:
			return obj
		if obj.hasFn(oldOM.MFn.kDagNode):
			fn = oldOM.MFnDagNode(obj)
			res = to_New_MObject(fn.fullPathName())
		else:
			fn = oldOM.MFnDependencyNode(obj)
			res = to_New_MObject(fn.name())
	else:
		if force_new:
			return obj		
		if obj.hasFn(newOM.MFn.kDagNode):
			fn = newOM.MFnDagNode(obj)
			res = to_Old_MObject(fn.fullPathName())
		else:
			fn = newOM.MFnDependencyNode(obj)
			res = to_Old_MObject(fn.name())
	return res
#----------------------------------------------------------------------
def Convert_MPlug(plug, force_old=False, force_new=False):
	node = plug.node()
	isinstance(plug, oldOM.MPlug)
	index = None
	if is_Old_API(plug):
		if plug.isElement():
			index = plug.logicalIndex()
		if force_old:
			return plug
		if node.hasFn(oldOM.MFn.kDagNode):
			fn = oldOM.MFnDagNode(node)
			res = to_New_MPlug(fn.fullPathName(), plug.name().split(".")[-1])
		else:
			fn = oldOM.MFnDependencyNode(node)
			res = to_New_MPlug(fn.name(), plug.name().split(".", 1)[1])
	else:
		if plug.isElement:
			index = plug.logicalIndex()		
		if force_new:
			return plug
		if node.hasFn(newOM.MFn.kDagNode):
			fn = newOM.MFnDagNode(node)
			res = to_Old_MPlug(fn.fullPathName(), plug.name().split(".", 1)[1])
		else:
			fn = newOM.MFnDependencyNode(node)
			res = to_Old_MPlug(fn.name(), plug.name().split(".", 1)[1])
	return res
#----------------------------------------------------------------------
def flatten(x):
	result = []
	for el in x:
		if hasattr(el, "__iter__") and not isinstance(el, basestring):
			result.extend(flatten(el))
		else:
			result.append(el)
	return result

########################################################################
class Named_Object(object):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself"""
	#----------------------------------------------------------------------
	def __init__(self,name):
		self._name = name
	#----------------------------------------------------------------------
	def __str__(self):
		return unicode(self.name)
	#----------------------------------------------------------------------
	def __repr__(self):
		return unicode(self.name)
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.name)
	#----------------------------------------------------------------------
	def __eq__(self, other):
		return unicode(self.name) == unicode(other)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return unicode(self.name) != unicode(other)
	#----------------------------------------------------------------------
	def get_name(self):
		return unicode(self._name)
	#----------------------------------------------------------------------
	name          = property(get_name)
########################################################################
class NameSpace(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name=None, current=False):
		if name is None:
			if current:
				name = cmds.namespaceInfo(currentNamespace=True,absoluteName=True)
			else:
				name = oldOM.MNamespace.rootNamespace()
		elif not cmds.namespace(exists=name):
			raise LookupError("The Input Namespace %r Does Not Exist" % name)
		super(NameSpace, self).__init__(name)
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for child in self.children:
			yield child
	#----------------------------------------------------------------------
	def __getitem__(self, val):
		""""""
		return self.children.__getitem__(val)
	#----------------------------------------------------------------------
	def __contains__(self, val):
		""""""
		val = str(val)
		for child in self:
			if val in [str(child.short_name), str(child.name)]:
				return True
		return False
	#----------------------------------------------------------------------
	def __enter__(self):
		self._reset_name = NameSpace(current=True)
		self.Make_Current()
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		self._reset_name.Make_Current()
	#----------------------------------------------------------------------
	def Make_Current(self):
		""""""
		cmds.namespace(setNamespace=self)
	#----------------------------------------------------------------------
	@property
	def parent(self):
		""""""
		return cmds.namespaceInfo(self.name,parent=True, absoluteName=True)
	#----------------------------------------------------------------------
	@property
	def children(self):
		""""""
		filter_out = [":UI", ":shared"]
		names = cmds.namespaceInfo(self.name,listOnlyNamespaces=True,absoluteName=True)
		if names is None:
			return []
		names = [name for name in names if not name in filter_out]
		return [NameSpace(name) for name in names]
	#----------------------------------------------------------------------
	@property
	def short_name(self):
		""""""
		return cmds.namespaceInfo(self.name,shortName=True)
	#----------------------------------------------------------------------
	def getObjects(self, types=None):
		""""""
		kwargs = dict(long=True)
		if types is not None:
			kwargs["type"]=types
		return strings_to_Maya_Nodes(cmds.ls(cmds.namespaceInfo(self.name, listOnlyDependencyNodes=True, dagPath=True), **kwargs))
	#----------------------------------------------------------------------
	def Add_Child(self, name):
		""""""
		if not name in [child.short_name for child in self.children]:
			new_namespace = cmds.namespace(parent=self.name,addNamespace=name,absoluteName=True)
		else:
			for child in self.children:
				if child.short_name == name:
					return child
		return NameSpace(new_namespace)
	#----------------------------------------------------------------------
	def Merge_Childern(self):
		""""""
		for child in self:
			self._merge_Childern_recursively(child)
	#----------------------------------------------------------------------
	def _merge_Childern_recursively(self, child):
		""""""
		pass
	#----------------------------------------------------------------------
	def setParent(self, parent):
		if not str(parent) == str(self.parent):
			if not isinstance(parent, NameSpace):
				parent = NameSpace(parent)
			new_namespace = parent.Add_Child(self.short_name)
			cmds.namespace(moveNamespace=[self.name,new_namespace], force=True)
			cmds.namespace(removeNamespace=self.name)
			self._name = new_namespace.name
	#----------------------------------------------------------------------
	def get_name(self):
		return unicode(self._name)
	#----------------------------------------------------------------------
	def set_name(self, name):
		name = cmds.namespace(validateName=name)
		if not isinstance(name, (str, unicode, Named_Object)):
			raise ValueError("The name attriute can only be set to a str or unicode value")
		cmds.namespace(parent=self.parent,rename=[self.name,name])
		self._name = unicode(str(name))
	#----------------------------------------------------------------------
	name          = property(get_name, set_name)
########################################################################
class MDT(object):
	Int32Array     ='Int32Array'
	doubleArray    ='doubleArray'
	lattice        ='lattice'
	matrix         ='matrix'
	mesh           ='mesh'
	nurbsCurve     ='nurbsCurve'
	nurbsSurface   ='nurbsSurface'
	pointArray     ='pointArray'
	string         ='string'
	stringArray    ='stringArray'
	vectorArray    ='vectorArray'
	#----------------------------------------------------------------------
	@classmethod
	def items(cls):
		return [cls.Int32Array, cls.doubleArray, cls.lattice, cls.matrix, cls.mesh, cls.nurbsCurve, cls.nurbsSurface, cls.pointArray, cls.string, cls.stringArray, cls.vectorArray]
########################################################################
class MAT(object):
	bool           ='bool'
	byte           ='byte'
	char           ='char'
	compound       ='compound'
	double         ='double'
	double2        ='double2'
	double3        ='double3'
	doubleAngle    ='doubleAngle'
	doubleLinear   ='doubleLinear'
	enum           ='enum'
	float          ='float'
	float2         ='float2'
	float3         ='float3'
	fltMatrix      ='fltMatrix'
	long           ='long'
	long2          ='long2'
	long3          ='long3'
	message        ='message'
	reflectance    ='reflectance'
	short          ='short'
	short2         ='short2'
	short3         ='short3'
	spectrum       ='spectrum'
	time           ='time'
	#----------------------------------------------------------------------
	@classmethod
	def items(cls):
		return [cls.bool, cls.byte, cls.char, cls.compound, cls.double, cls.double2, cls.double3, cls.doubleAngle, cls.doubleLinear, cls.enum, cls.float, cls.float2, cls.float3, cls.fltMatrix, cls.long, cls.long2, cls.long3, cls.message, cls.reflectance, cls.short, cls.short2, cls.short3, cls.spectrum, cls.time]
	#----------------------------------------------------------------------
	@classmethod
	def triples(cls):
		return [cls.double3, cls.float3, cls.short3, cls.long3]
	#----------------------------------------------------------------------
	@classmethod
	def double(cls):
		return [cls.double2, cls.float2, cls.short2, cls.long2]
	#----------------------------------------------------------------------
	@classmethod
	def complex(cls):
		return [cls.double2, cls.double3,cls.float2, cls.float3,cls.long2, cls.long3,cls.short2, cls.short3]
	#----------------------------------------------------------------------
	@classmethod
	def numerical(cls):
		return [cls.bool, cls.byte, cls.char, cls.double, cls.doubleAngle, cls.doubleLinear, cls.float, cls.long, cls.reflectance, cls.short, cls.spectrum, cls.time]
########################################################################
class MTypes(object):
	DTS = ['Int32Array', 'doubleArray', 'lattice', 'matrix', 'mesh', 'nurbsCurve', 'nurbsSurface', 'pointArray', 'string', 'stringArray', 'vectorArray']
	ATS = ['bool', 'byte', 'char', 'TdataCompound','compound', 'double', 'double2', 'double3', 'doubleAngle', 'doubleLinear', 'enum', 'float', 'float2', 'float3', 'fltMatrix', 'long', 'long2', 'long3', 'message', 'reflectance', 'short', 'short2', 'short3', 'spectrum', 'time']
	NTS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	STS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	CTS = ['double2', 'double3','float2', 'float3','long2', 'long3','short2', 'short3']
########################################################################
class Attribute_Tools(object):
	#----------------------------------------------------------------------
	@classmethod
	def build_kwargs(cls, create=None           , query=None           , edit=None    , multiuse=None,
		             attributeType=None    , usedAsColor=None     , storable=None, 
		             cachedInternally=None , exists=None          , category=None,
		             dataType=None         , defaultValue=None    , enumName=None,
		             hasMaxValue=None      , hasMinValue=None     , hasSoftMaxValue=None,
		             writable=None         , hasSoftMinValue=None , hidden=None,
		             indexMatters=None     , internalSet=None     , keyable=None,
		             usedAsFilename=None   , shortName=None       , longName=None,
		             maxValue=None         , minValue=None        , multi=None,
		             niceName=None         , numberOfChildren=None, parent=None,
		             readable=None         , softMaxValue=None    , softMinValue=None, fromPlugin=None):
		locs = locals()
		res = dict()
		keys = ["create","query","edit","multiuse","attributeType","cachedInternally","category","dataType","defaultValue","enumName","exists","fromPlugin","hasMaxValue","hasMinValue","hasSoftMaxValue","hasSoftMinValue","hidden","indexMatters","internalSet","keyable","longName","maxValue","minValue","multi","niceName","numberOfChildren","parent","readable","shortName","softMaxValue","softMinValue","storable","usedAsColor","usedAsFilename","writable"]
		[res.__setitem__(key, locs.__getitem__(key)) for key in keys if not locs.get(key) == None ]
		return res
	#----------------------------------------------------------------------
	@classmethod
	def make_plug_path(cls, node=None, attr=None):
		if node == None:
			node = cmds.ls(sl=True)
		if isinstance(node, Maya_Node):
			node = node.name
		if attr == None:
			if "." in node:
				attr = ".".join(node.split(".")[1:])
				node = node.split(".")[0]
			else:
				raise ValueError("input was not a valid Plug")
		full_plug_path = ".".join([str(node), str(attr)])
		return full_plug_path, node, attr
	#----------------------------------------------------------------------
	@classmethod
	def make_MPLUG(cls, node, attr):
		plug = MPLUG(node, attr)
		#try:
		#except:
			#raise StandardError('Could Not Be Converted To An MPLUG From Inputs "%s","%s" ' % (node, attr))
		return plug
	#----------------------------------------------------------------------
	@classmethod
	def get_Simple_Value(cls, node, attr=None):
		plug, node, attr = cls.make_plug_path(node, attr)
		plug_type = cmds.getAttr(plug, type=True)
		if plug_type in MTypes.STS or plug_type == "string":
			return cmds.getAttr(plug)
		elif plug_type in MTypes.CTS:
			return list(cmds.getAttr(plug)[0])
		return cmds.getAttr(plug)
	#----------------------------------------------------------------------
	@classmethod
	def get_Simple_Multi_Index_Value(cls, node, attr=None):
		plug, node, attr = cls.make_plug_path(node, attr)
		plug_type = cmds.getAttr(plug, type=True)
		if plug_type in MTypes.STS or plug_type == "string":
			return cmds.getAttr(plug)
		elif plug_type in MTypes.CTS:
			return list(cmds.getAttr(plug)[0])
		return cmds.getAttr(plug)
	#----------------------------------------------------------------------
	@classmethod
	def set_Simple_Value(cls, node, value, attr=None):
		plug, node, attr = cls.make_plug_path(node, attr)
		plug_type = cmds.getAttr(plug, type=True)
		if plug_type in MTypes.STS or plug_type == "string" or plug_type == "enum":
			if plug_type == "string":
				cmds.setAttr(plug,value,type=plug_type)
			else:
				cmds.setAttr(plug,value)
		elif plug_type in MTypes.CTS and plug_type.endswith("2"):
			cmds.setAttr(plug,value[0],value[1],type=plug_type)
		elif plug_type in MTypes.CTS and plug_type.endswith("3"):
			cmds.setAttr(plug,value[0],value[1],value[2],type=plug_type)
		else:
			cmds.setAttr(plug,value)
	#----------------------------------------------------------------------
	@classmethod
	def attribute_Exists(cls, node,attr=None):
		plug, node, attr = cls.make_plug_path(node, attr)
		return cmds.attributeQuery(attr,node=node, exists=True )
	#----------------------------------------------------------------------
	@classmethod
	def delete_Attribute(cls, node,attr=None):
		plug, node, attr = cls.make_plug_path(node, attr)
		if cls.attribute_Exists(node,attr):
			cmds.deleteAttr( node, attribute=attr )
	#----------------------------------------------------------------------
	@classmethod
	def add_Attr(cls, at, node, attr=None, multi=None, longName=None, shortName=None,niceName=None, indexMatters=None, numberOfChildren=None, parent=None, defaultValue=None, storable=None, keyable=None, readable=None, hidden=None, writable=None, maxValue=None, minValue=None, softMaxValue=None, softMinValue=None):
		""""""
		cls.build_kwargs(attributeType=at, storable=storable, defaultValue=defaultValue, writable=writable,hidden=hidden, indexMatters=indexMatters,keyable=keyable, shortName=shortName, longName=longName, maxValue=maxValue, minValue=minValue, multi=multi, niceName=niceName, numberOfChildren=numberOfChildren, parent=parent, readable=readable, softMaxValue=softMaxValue, softMinValue=softMinValue)
		plug, node, attr = cls.make_plug_path(node, attr)
		if not cls.attribute_Exists(node, attr):
			cmds.addAttr(node,longName=attr,attributeType=at, multi=multi, )
		return cls.make_MPLUG(node, attr)
	#----------------------------------------------------------------------
	@classmethod
	def add_Simple_Attr(cls, at, node, attr=None, multi=False, indexMatters=True, parent=False):
		""""""
		plug, node, attr = cls.make_plug_path(node=node, attr=attr)
		
		kwargs = dict(longName=attr, attributeType=at)
		
		if parent:
			kwargs["parent"] = parent
		if multi:
			kwargs["multi"] = multi
			kwargs["indexMatters"] = indexMatters
			
		if not cls.attribute_Exists(node, attr):
			cmds.addAttr(node,**kwargs)
		return cls.make_MPLUG(node, attr)
	#----------------------------------------------------------------------
	@classmethod
	def add_2_Item_Attr(cls, at, node, attr=None, multi=False, parent=False):
		plug, node, attr = cls.make_plug_path(node, attr)
		if not cls.attribute_Exists(node, attr):
			if parent:
				cmds.addAttr(node,longName=attr,at=str(at+'2'), multi=multi, parent=parent)
			else:
				cmds.addAttr(node,longName=attr,at=str(at+'2'), multi=multi)
			cmds.addAttr(node,longName=(attr + "X"),parent=attr,attributeType=at)
			cmds.addAttr(node,longName=(attr + "Y"),parent=attr,attributeType=at)
		return cls.make_MPLUG(node, attr)
	#----------------------------------------------------------------------
	@classmethod
	def add_3_Item_Attr(cls, at, node, attr=None, multi=False, parent=False):
		plug, node, attr = cls.make_plug_path(node, attr)
		if not cls.attribute_Exists(node, attr):
			if parent:
				cmds.addAttr(node,longName=attr,attributeType=at+'3', multi=multi, parent=parent)
			else:
				cmds.addAttr(node,longName=attr,attributeType=at+'3', multi=multi)
			cmds.addAttr(node,longName=(attr + "X"),parent=attr,attributeType=at)
			cmds.addAttr(node,longName=(attr + "Y"),parent=attr,attributeType=at)
			cmds.addAttr(node,longName=(attr + "Z"),parent=attr,attributeType=at)
		return cls.make_MPLUG(node, attr)
	#----------------------------------------------------------------------
	@classmethod
	def add_Simple_Data(cls, dt, node, attr=None, multi=False, parent=False):
		""""""
		plug, node, attr = cls.make_plug_path(node, attr)
		if not cls.attribute_Exists(node, attr):
			if parent:
				cmds.addAttr(node,longName=attr,dt=dt, multi=multi, parent=parent)
			else:
				cmds.addAttr(node,longName=attr,dt=dt, multi=multi)
		return cls.make_MPLUG(node, attr)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Char(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('char', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Multi_Char(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('char', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Byte(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('byte', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Byte_M(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('byte', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Bool(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('bool', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Bool_M(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('bool', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Short(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('short', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Short_M(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('short', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Short2(cls, node, attr=None, parent=False):
		return cls.add_2_Item_Attr('short', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Short2_M(cls, node, attr=None, parent=False):
		return cls.add_2_Item_Attr('short', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Short3(cls, node, attr=None, parent=False):
		return cls.add_3_Item_Attr("short", node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Long(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('long', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Long_M(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('long', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Long2(cls, node, attr=None, parent=False):
		return cls.add_2_Item_Attr('long', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Long2_M(cls, node, attr=None, parent=False):
		return cls.add_2_Item_Attr('long', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Long3(cls, node, attr=None, parent=False):
		return cls.add_3_Item_Attr('long', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Long3_M(cls, node, attr=None, parent=False):
		return cls.add_3_Item_Attr('long', node, attr=attr, multi=True, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Float(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr("float", node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Float2(cls, node, attr=None, parent=False):
		return cls.add_2_Item_Attr("float", node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Float3(cls, node, attr=None, parent=None):
		return cls.add_3_Item_Attr("float", node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Double_Angle(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr("doubleAngle", node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Double_Linear(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr("doubleLinear", node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Message(cls, node, attr=None, parent=False):
		return cls.add_Simple_Attr('message', node, attr=attr, multi=False, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Message_M(cls, node, attr=None, indexMatters=True, parent=False):
		return cls.add_Simple_Attr('message', node, attr=attr, multi=True, indexMatters=indexMatters, parent=parent)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Enum(cls, node, attr=None, enumName="Green:Blue:", parent=False):
		plug, node, attr = cls.make_plug_path(node, attr)
		if not cls.attribute_Exists(node, attr):
			if parent:
				cmds.addAttr( node, shortName=attr, longName=attr, at="enum",enumName=enumName, parent=parent)
			else:
				cmds.addAttr( node, shortName=attr, longName=attr, at="enum",enumName=enumName)
		return Enum_MPLUG(cls.make_MPLUG(node, attr))
	#----------------------------------------------------------------------
	@classmethod
	def Add_String(cls, node, attr=None, parent=False):
		return cls.add_Simple_Data("string", node, attr=attr, multi=False)
	#----------------------------------------------------------------------
	@classmethod
	def Add_String_M(cls, node, attr=None):
		return cls.add_Simple_Data("string", node, attr=attr, multi=True)
	#----------------------------------------------------------------------
	@classmethod
	def Add_String_Array(cls, node, attr=None):
		return cls.add_Simple_Data("stringArray", node, attr=attr, multi=False)
	#----------------------------------------------------------------------
	@classmethod
	def Add_String_Array_M(cls, node, attr=None):
		return cls.add_Simple_Data("stringArray", node, attr=attr, multi=True)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Float_Matrix(cls, node, attr=None):
		return cls.add_Simple_Data("fltMatrix", node, attr=attr, multi=False)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Float_Matrix_M(cls, node, attr=None):
		return cls.add_Simple_Data("fltMatrix", node, attr=attr, multi=True)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Int32_Array(cls, node, attr=None):
		return cls.add_Simple_Data("Int32Array", node, attr=attr, multi=False)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Int32_Array_M(cls, node, attr=None):
		return cls.add_Simple_Data("Int32Array", node, attr=attr, multi=True)	
	#----------------------------------------------------------------------
	@classmethod
	def Add_Double_Array(cls, node, attr=None):
		return cls.add_Simple_Data("doubleArray", node, attr=attr, multi=False)
	#----------------------------------------------------------------------
	@classmethod
	def Add_Double_Array_M(cls, node, attr=None):
		return cls.add_Simple_Data("doubleArray", node, attr=attr, multi=True)
	#----------------------------------------------------------------------
	@classmethod
	def Set_String_M_Item(cls, node, attr, Value, Index):
		cmds.setAttr((node + "." + attr + "[" + str(Index) + "]"),Value,type=("string"))
	#----------------------------------------------------------------------
	@classmethod
	def Set_Float_Matrix(cls, node, attr, M):
		plug   = node + "." + attr
		values = flatten(M)
		cmds.setAttr((plug),values,type=("matrix"))
	#----------------------------------------------------------------------
	@classmethod
	def Set_Float_Matrix_M(cls, node, attr, M, Index):
		plug   = node + "." + attr + "[" + str(Index) + "]"
		values = flatten(M)
		cmds.setAttr((plug),values,type=("matrix"))
	#----------------------------------------------------------------------
	@classmethod
	def Set_Int32_Array(cls, node, attr, IntValues):
		plug = node + "." + attr
		cmds.setAttr(plug,IntValues,type="Int32Array")
	#----------------------------------------------------------------------
	@classmethod
	def Set_Int32_Array_M(cls, node, attr, IntValues, Index):
		plug = node + "." + attr + "[" + str(Index) + "]"
		cmds.setAttr(plug,IntValues,type="Int32Array")
	#----------------------------------------------------------------------
	@classmethod
	def Set_Double_Array(cls, node, attr, FltValues):
		plug = node + "." + attr
		cmds.setAttr(plug,FltValues,type="doubleArray")
	#----------------------------------------------------------------------
	@classmethod
	def Set_Double_Array_M(cls, node, attr, FltValues, Index):
		plug = node + "." + attr + "[" + str(Index) + "]"
		cmds.setAttr(plug,FltValues,type="doubleArray")
	#----------------------------------------------------------------------
	@classmethod
	def Set_String_Array(cls, node, attr, StrValues):
		plug = node + "." + attr
		cmds.setAttr(plug,StrValues,type="stringArray")
	#----------------------------------------------------------------------
	@classmethod
	def Set_String_Array_M(cls, node, attr, StrValues, Index):
		plug = node + "." + attr + "[" + str(Index) + "]"
		cmds.setAttr(plug,StrValues,type="stringArray")
	
	#Adds a compond attribute
	@classmethod
	#----------------------------------------------------------------------
	def Add_Compound_Attribute(cls, node, attrName, child_attribs):
		if not cls.attribute_Exists( node, attrName):
			child_count = len(child_attribs)
			cmds.addAttr(node, shortName=attrName, longName=attrName, numberOfChildren=child_count, attributeType='compound' )
			for typ, name in child_attribs:
				if typ == "bool":
					cls.Add_Bool(node, attr=name, parent=attrName)
				elif typ == "byte":
					cls.Add_Byte(node, attr=name, parent=attrName)
				elif typ == "char":
					cls.Add_Char(node, attr=name, parent=attrName)
				elif typ == "enum":
					cls.Add_Enum(node, attr=name, enumName="Green:Blue:", parent=attrName)
				elif typ.startswith("long"):
					if typ.endswith("2"):
						cls.Add_Long2(node, attr=name, parent=attrName)
					elif typ.endswith("3"):
						cls.Add_Long3(node, attr=name, parent=attrName)
					else:
						cls.Add_Long(node, attr=name, parent=attrName)
				elif typ.startswith("short"):
					if typ.endswith("2"):
						cls.Add_Short2(node, attr=name, parent=attrName)
					elif typ.endswith("3"):
						cls.Add_Short3(node, attr=name, parent=attrName)
					else:
						cls.Add_Short(node, attr=name, parent=attrName)
				elif typ.startswith("float"):
					if typ.endswith("2"):
						cls.Add_Float2(node, attr=name, parent=attrName)
					elif typ.endswith("3"):
						cls.Add_Float3(node, attr=name, parent=attrName)
					else:
						cls.Add_Float(node, attr=name, parent=attrName)
				elif typ == "string":
					cls.Add_String(node, attr=name, parent=attrName)
				elif typ == "stringArray":
					cls.Add_String_Array(node, attr=name, parent=attrName)
			cls.make_plug_path(node=node, attr=attrName)
			return MPLUG(node, attrName)

########################################################################
class _API_MPlug(newOM.MPlug):
	""""""
	Att_Fn = newOM.MFnAttribute()
	#----------------------------------------------------------------------
	def numChildren(self):
		""""""
		return 0 if not self.isCompound else super(MPlug, self).numChildren()
	#----------------------------------------------------------------------
	num_Children = property(numChildren)
	#----------------------------------------------------------------------
	def child_Plugs(self):
		""""""
		return [] if not self.isCompound else [MPlug(self.child(index)) for index in range(self.num_Children)]
	#----------------------------------------------------------------------
	def child_Attributes(self):
		""""""
		return [] if not self.isCompound else [self.child(index).attribute() for index in range(self.num_Children)]
	#----------------------------------------------------------------------
	def childNames(self):
		""""""
		return [] if not self.isCompound else [self.Att_Fn.setObject(att).name for att in self.child_Attributes()]
	#----------------------------------------------------------------------
	def parent(self):
		""""""
		parent = MPlug(super(MPlug, self).parent())
		return parent
	#----------------------------------------------------------------------
	def connectedTo(self, src, dest):
		return [MPlug(plg) for plg in super(MPlug, self).connectedTo(src, dest)]
	#----------------------------------------------------------------------
	def child(self, arg):
		""""""
		if not self.isCompound:
			raise TypeError("Plug %r is not a compound Attribute" % self.name())

		arg_type = type(arg)

		if not arg_type in [int, str, unicode]:
			raise TypeError("input must be one of types [int,str,unicode] and a %s type was found" % arg_type.__name__)

		if arg_type is int:
			if arg >= self.num_Children:
				raise IndexError("The Input value %i Exceeds The Total Number Of Childern Of The Attribute %r" % (arg, self.name()))
			else:
				index = arg

		elif type(arg) in [str, unicode]:
			names = self.childNames()
			if not arg in names:
				raise LookupError("The Attribute %s Has No Child With The Input %r " % (self.name, arg))
			else:
				try:
					index = names.index(arg)
				except ValueError:
					raise LookupError("The Attribute %s Has No Child With The Input %r " % (self.name, arg))
		child = MPlug(super(MPlug, self).child(index))
		return child
	#----------------------------------------------------------------------
	def siblings(self):
		""""""
		try:
			parent = self.parent()
			return [] if not parent.isCompound else parent.child_Plugs()
		except:
			return []
	#----------------------------------------------------------------------
	def elementByLogicalIndex(self, index):
		""""""
		res = super(MPlug, self).elementByLogicalIndex(index)
		res = MPlug(res)
		return res
	#----------------------------------------------------------------------
	def iter_Elements(self):
		""""""
		for index in range(self.numElements()):
			elem = self.elementByLogicalIndex(index)
			yield elem

########################################################################
class MPLUG(object):
	"""
	This Class Is A Base Class That Holds The A Memeory Pointer to a Nodes Attribute
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	def __init__(self,node,att=None):
		if isinstance(node, MPLUG):
			self.old_obj  = node.old_obj
			self.new_obj  = node.new_obj
			self.api_obj  = node.api_obj
			self.node     = node.node
			self._Att_Fn  = node._Att_Fn
		else:
			self._Att_Fn = newOM.MFnAttribute()
			if isinstance(node, (oldOM.MPlug, newOM.MPlug)):
				self.new_obj  = nameToPlug(node.name(), att, OldApi=False)
				self.old_obj  = nameToPlug(node.name(), att, OldApi=True)
				self.api_obj  = _API_MPlug(self.new_obj)
				self.node     = Maya_Node(node.name().split(".")[0])
			elif isinstance(node, (str, unicode)):
				if node.count('.'):
					att  =  node.split(".", 1)[1]
					node =  node.split(".", 1)[0]
				self.new_obj  = nameToPlug(node, att, OldApi=False)
				self.old_obj  = nameToPlug(node, att, OldApi=True)
				self.api_obj  = _API_MPlug(self.new_obj)
				self.node     = Maya_Node(node)
			elif isinstance(node, Maya_Node):
				self.node = node
				self.new_obj  = nameToPlug(node.name, att, OldApi=False)
				self.old_obj  = nameToPlug(node.name, att, OldApi=True)
				self.api_obj  = _API_MPlug(self.new_obj)
			self._Att_Fn.setObject(self.api_obj.attribute())
	#----------------------------------------------------------------------
	def __str__(self):
		return str(self.node.name + '.' + self.longName)
	#----------------------------------------------------------------------
	def __repr__(self):
		return str(self.node.name + '.' + self.longName)
	#----------------------------------------------------------------------
	def getElementByIndex(self, index):
		try:
			res = self.old_obj.elementByLogicalIndex(index)
			res = MPLUG(res)
		except:
			res = None
		return res	
	#----------------------------------------------------------------------
	def getValue(self):
		if self.type in MAT.numerical() or self.type == MDT.string:
			return cmds.getAttr(self.name)
		elif self.type in MAT.complex():
			return list(cmds.getAttr(self.name)[0])
		elif self.type == "message":
			nodes = self.input_Nodes
			if len(nodes):
				return nodes[0]
			else:
				return None
		elif self.type is None:
			res = []
			if self.has_source_connections:
				plugs = self.input_Plugs
				for plg in plugs:
					val = plg.value
					if val is not None:
						if isinstance(val, (list, tuple)):
							res.extend(val)
						else:
							res.append(val)
				return res
		return cmds.getAttr(self.name)
	#----------------------------------------------------------------------
	@nodeLockManager
	def setValue(self, value):
		if self.type in MTypes.NTS or self.type == "string" or self.type == "enum":
			if self.type == "string":
				cmds.setAttr(self,value,type=self.type)
			else:
				cmds.setAttr(self,value)
		elif self.type in MTypes.CTS:
			if self.type.endswith("2"):
				cmds.setAttr(self,value[0],value[1],type=self.type)
			elif self.type.endswith("3"):
				cmds.setAttr(self,value[0],value[1],value[2],type=self.type)
		else:
			cmds.setAttr(self.name,value,type=self.type)
	#----------------------------------------------------------------------
	def get_input_Plug_Names(self):
		""""""
		res = []
		source = cmds.listConnections( self ,source=True,destination=False, plugs=True,skipConversionNodes=True)
		if source:
			res = source
		return res		
	#----------------------------------------------------------------------
	def get_output_Plug_Names(self):
		""""""
		res = []
		source = cmds.listConnections( self ,source=False,destination=True,plugs=True,skipConversionNodes=True)
		if source:
			res = source
		return res		
	#----------------------------------------------------------------------
	def get_input_Node_Names(self):
		""""""
		res = cmds.listConnections( self ,source=True,plugs=False,skipConversionNodes=True)
		return res
	#----------------------------------------------------------------------
	def get_output_Node_Names(self):
		""""""
		res = cmds.listConnections( self ,source=False,destination=True,plugs=False,skipConversionNodes=True)
		return res
	#----------------------------------------------------------------------
	@property
	def input_Plugs(self):
		""""""
		res = []
		source = self.get_input_Plug_Names()
		if source:
			for s in source:
				plg = MPLUG(s)
				res.append(plg)
		return res	
	#----------------------------------------------------------------------
	@property
	def output_Plugs(self):
		""""""
		res = []
		source = self.get_output_Plug_Names()
		if source:
			for s in source:
				plg = MPLUG(s)
				res.append(plg)
		return res		
	#----------------------------------------------------------------------
	@property
	def input_Nodes(self):
		""""""
		res = []
		sources = self.get_input_Node_Names()
		if sources:
			res = strings_to_Maya_Nodes(sources)
		return res
	#----------------------------------------------------------------------
	@property
	def output_Nodes(self):
		""""""
		res = []
		destinations =  self.get_output_Node_Names()
		if destinations:
			res = strings_to_Maya_Nodes(destinations)
		return res
	#----------------------------------------------------------------------
	@nodeLockManager
	def Disconnect_All_Inputs(self):
		""""""
		if self.isArray:
			for plg in self.iter_element_plugs():
				for input_plg in plg.input_Plugs:
					cmds.disconnectAttr(input_plg,plg)
		else:
			for plg in self.input_Plugs:
				cmds.disconnectAttr(plg,self)
	@nodeLockManager
	def Disconnect_All_Output(self):
		""""""
		if self.isArray:
			for plg in self.iter_element_plugs():
				for input_plg in plg.output_Plugs:
					cmds.disconnectAttr(plg, input_plg)
		else:
			for plg in self.output_Plugs:
				cmds.disconnectAttr(plg,self)
	#----------------------------------------------------------------------
	@nodeLockManager
	def Simple_Disconnect(self,plug):
		cmds.disconnectAttr(self, plug)
	#----------------------------------------------------------------------
	@nodeLockManager
	def Simple_Connect(self,plg):
		""""""
		if not cmds.isConnected(self,plg):
			cmds.connectAttr(self,plg,force=True)
	#----------------------------------------------------------------------
	@nodeLockManager
	def lock(self):
		cmds.setAttr(self,lock=True)
	#----------------------------------------------------------------------
	@nodeLockManager
	def unlock(self):
		cmds.setAttr(self,lock=False)
	#----------------------------------------------------------------------
	@property
	def locked(self):
		""""""
		return cmds.getAttr( self,lock=True )
	#----------------------------------------------------------------------
	@property
	def size(self):
		""""""
		return cmds.getAttr(self.name,size=True)
	#----------------------------------------------------------------------
	@property
	def keyable(self):
		"""Return the keyable status of the attribute """
		# return cmds.attributeQuery( self.plugName,node=self.node , keyable=True )
		return self.api_obj.isKeyable
	#----------------------------------------------------------------------
	@nodeLockManager
	def make_keyable(self,val):
		"""Return the keyable status of the attribute """
		return cmds.setAttr(self,k=val)
	#----------------------------------------------------------------------
	@property
	def exists(self):
		"""Return true if the attribute exists"""
		return cmds.attributeQuery( self.plugName,node=self.node, exists=True )
	#----------------------------------------------------------------------
	@nodeLockManager
	def enable_Render_Layer_Overide(self,layer=None):
		"""Return true if the attribute exists"""
		if layer:
			cmds.editRenderLayerAdjustment( self.name, layer=layer )
		else:
			cmds.editRenderLayerAdjustment( self.name)
	#----------------------------------------------------------------------
	@nodeLockManager
	def disable_Render_Layer_Overide(self,layer=None):
		if layer:
			try:
				cmds.editRenderLayerAdjustment( self.name, remove=True, layer=layer )
			except RuntimeError:
				pass
		else:
			try:
				cmds.editRenderLayerAdjustment( self.name, remove=True)
			except RuntimeError:
				pass
	#----------------------------------------------------------------------
	@property
	def connectable(self):
		"""Return the connectable status of the attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  connectable=True )
	#----------------------------------------------------------------------
	@property
	def message(self):
		"""Return true if the attribute is a message attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  message=True )
	#----------------------------------------------------------------------
	@property
	def enum(self):
		"""Return true if the attribute is a enum attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  enum=True )
	#----------------------------------------------------------------------
	@property
	def hidden(self):
		"""Return the hidden status of the attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  hidden=True )
	#----------------------------------------------------------------------
	@property
	def indexMatters(self):
		"""Return the indexMatters status of the attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  indexMatters=True )
	#----------------------------------------------------------------------
	@property
	def readable(self):
		"""Return the readable status of the attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  readable=True )
	#----------------------------------------------------------------------
	@property
	def storable(self):
		"""Return true if the attribute is storable"""
		return cmds.attributeQuery( self.plugName,node=self.node,  storable=True )
	#----------------------------------------------------------------------
	@property
	def writable(self):
		"""Return true if the attribute is a message attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  writable=True )
	#----------------------------------------------------------------------
	@property
	def multi(self):
		"""Return true if the attribute is a multi-attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  multi=True )
	#----------------------------------------------------------------------
	@property
	def isArray(self):
		""""""
		return self.old_obj.isArray()
	#----------------------------------------------------------------------
	@property
	def isElement(self):
		""""""
		return self.old_obj.isElement()
	#----------------------------------------------------------------------
	@property
	def isDynamic(self):
		""""""
		return self.old_obj.isDynamic()
	#----------------------------------------------------------------------
	@property
	def isSource(self):
		""""""
		return self.old_obj.isSource()
	#----------------------------------------------------------------------
	@property
	def isDestination(self):
		""""""
		return self.old_obj.isDestination()
	#----------------------------------------------------------------------
	@property
	def isProcedural(self):
		""""""
		return self.old_obj.isProcedural()
	#----------------------------------------------------------------------
	@property
	def isConnected(self):
		""""""
		return self.old_obj.isConnected()
	#----------------------------------------------------------------------
	@property
	def isChild(self):
		""""""
		return self.old_obj.isChild()
	#----------------------------------------------------------------------
	@property
	def isChannelBox(self):
		""""""
		return self.old_obj.isChannelBox()
	#----------------------------------------------------------------------
	@property
	def isCompound(self):
		""""""
		return self.old_obj.isCompound()
	#----------------------------------------------------------------------
	@property
	def isNetworked(self):
		""""""
		return self.old_obj.isNetworked()
	#----------------------------------------------------------------------
	@property
	def isIgnoredWhenRendering(self):
		""""""
		return self.old_obj.isIgnoredWhenRendering()
	#----------------------------------------------------------------------
	@property
	def isFromReferencedFile(self):
		""""""
		return self.old_obj.isFromReferencedFile()
	#----------------------------------------------------------------------
	@property
	def usesMultiBuilder(self):
		"""Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data"""
		return cmds.attributeQuery( self.plugName,node=self.node,  usesMultiBuilder=True )
	#----------------------------------------------------------------------
	@property
	def minimum(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  minimum=True )
	#----------------------------------------------------------------------
	@property
	def has_source_connections(self):
		return cmds.listConnections( self ,source=True, destination=False, plugs=True, skipConversionNodes=True) != None
	#----------------------------------------------------------------------
	@property
	def has_destination_connections(self):
		return cmds.listConnections( self ,source=False, destination=True, plugs=True, skipConversionNodes=True) != None
	#----------------------------------------------------------------------
	@property
	def maximum(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  maximum=True )
	#----------------------------------------------------------------------
	@property
	def range(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  range=True )
	#----------------------------------------------------------------------
	@property
	def usedAsColor(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  usedAsColor=True )
	#----------------------------------------------------------------------
	@property
	def softRange(self):
		"""Return true if the attribute is a message attribute"""
		return cmds.attributeQuery( self.plugName,node=self.node,  softRange=True )
	#----------------------------------------------------------------------
	@property
	def softMin(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  softMin=True )
	#----------------------------------------------------------------------
	@property
	def softMax(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  softMax=True )
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  numberOfChildren=True )
	#----------------------------------------------------------------------
	@property
	def listSiblings(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  listSiblings=True )
	#----------------------------------------------------------------------
	@property
	def listChildren(self):
		return strings_to_MPLUGS([self.name + "." + child for child in self.childNames])
	@property
	def childNames(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  listChildren=True )

	#----------------------------------------------------------------------
	def get_child_plug(self, arg):
		if type(arg)==int:
			if arg >= self.numberOfChildren:
				raise IndexError("The Input value %i Excedes The Total Number Of Childern Of The Attribute %r" % (arg, self.name))
			else:
				return MPLUG(self.new_obj.child(arg))
			
		elif type(arg) == str or type(arg) == unicode:
			if not arg in self.childNames:
				raise LookupError("The Attribute %s Has No Child With The Input %r " % (self.name, arg))
			else:
				return MPLUG(self.name + "." + arg)
		else:
			raise TypeError("input must be a int or str and a %r was found" % type(arg))
	#----------------------------------------------------------------------
	@property
	def listParent(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  listParent=True )
	#----------------------------------------------------------------------
	@property
	def listEnum(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  listEnum=True )
	#----------------------------------------------------------------------
	@property
	def listDefault(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  listDefault=True )
	#----------------------------------------------------------------------
	@property
	def minExists(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  minExists=True )
	#----------------------------------------------------------------------
	@property
	def maxExists(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  maxExists=True )
	#----------------------------------------------------------------------
	@property
	def rangeExists(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  rangeExists=True )
	#----------------------------------------------------------------------
	@property
	def softMinExists(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  softMinExists=True )
	#----------------------------------------------------------------------
	@property
	def softMaxExists(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  softMaxExists=True )
	#----------------------------------------------------------------------
	@property
	def softRangeExists(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  softRangeExists=True )
	#----------------------------------------------------------------------
	@property
	def niceName(self):
		return cmds.attributeQuery( self.plugName,node=self.node,  niceName=True )
	#----------------------------------------------------------------------
	@property
	def longName(self):
		res = cmds.attributeQuery( self.plugName,node=self.node,  longName=True )
		if self.isElement:
			res += "[%i]" % self.logicalIndex
		return res
	#----------------------------------------------------------------------
	@property
	def shortName(self):
		res = cmds.attributeQuery( self.plugName,node=self.node,  shortName=True )
		if self.isElement:
			res += "[%i]" % self.logicalIndex
		return res
	#----------------------------------------------------------------------
	@property
	def name(self):
		return self.new_obj.name()
	#----------------------------------------------------------------------
	@property
	def plugName(self):
		res = self.new_obj.name()
		res = res.split(".")[-1]
		if self.isElement:
			res = res.split('[')[0]
		return res
	#----------------------------------------------------------------------
	@property
	def partialName(self):
		return self.new_obj.partialName()
	#----------------------------------------------------------------------
	@property
	def array(self):
		if self.isElement:
			return MPLUG(self.new_obj.array())
		return None
	#----------------------------------------------------------------------
	@property
	def numElements(self):
		if self.multi:
			return self.old_obj.numElements()
		else:
			return -1
	#----------------------------------------------------------------------
	@property
	def numConnectedElements(self):
		if self.multi:
			return self.new_obj.numConnectedElements()
		else:
			return 0
	#----------------------------------------------------------------------
	@property
	def getSetAttrCmds(self):
		data = []
		self.old_obj.getSetAttrCmds(data)
		return data
	#----------------------------------------------------------------------
	@property
	def listEnumNames(self):
		if self.listEnum == None:
			return []
		return self.listEnum[0].split(":")
	#----------------------------------------------------------------------
	@property
	def elementParent(self):
		if self.isElement:
			res = MPLUG(self.name.split("[")[0])
		else:
			res = self
		return res
	#----------------------------------------------------------------------
	@property
	def type(self):
		return cmds.getAttr(self.name,typ=True )
	#----------------------------------------------------------------------
	@property
	def logicalIndex(self):
		if self.isElement:
			return self.old_obj.logicalIndex()
		else:
			return None
	#----------------------------------------------------------------------
	@property
	def multiIndices(self):
		return cmds.getAttr(self, multiIndices=True)
	#----------------------------------------------------------------------
	@property
	def multiElements(self):
		""""""
		elems     = cmds.listAttr(self,multi=True)
		node_name = self.node.name
		plugs     = [".".join([node_name,elem]) for elem in elems]
		return strings_to_MPLUGS(plugs)
	@property
	#----------------------------------------------------------------------	
	def element_plugs(self):
		plugs = cmds.listConnections( self.name ,plugs=True,skipConversionNodes=True)
		res = strings_to_MPLUGS(plugs)
		return res
	@property
	#----------------------------------------------------------------------	
	def element_nodes(self):
		plugs = cmds.listConnections( self.name ,skipConversionNodes=True)
		res = strings_to_Maya_Nodes(plugs)
		return res
	#----------------------------------------------------------------------
	def clean_Element_Indexing(self):
		if self.isElement:
			plug = self.array
		else:
			plug = self
		if plug.multi:
			if range(plug.numConnectedElements) != plug.multiIndices:
				
				if plug.has_source_connections:
					connection_plgs = plug.input_Plugs
					plug.Disconnect_All_Inputs()
					
					for index, plg in enumerate(connection_plgs):
						cmds.connectAttr(plg.name, plug.name+"[%i]" % index,force=True)
						
				elif plug.has_destination_connections:
					connection_plgs = plug.output_Plugs
					plug.Disconnect_All_Output()
					
					for index, plg in enumerate(connection_plgs):
						try:
							cmds.connectAttr(plug.name+"[%i]" % index, plg.name,force=True)
						except:
							pass
				
				for plg in plug.multiElements:
					if not plg.isConnected:
						cmds.removeMultiInstance(plg.name,b=True)
	#----------------------------------------------------------------------	
	def iter_element_plugs(self):
		for index in self.multiIndices:
			plg = self.getElementByIndex(index)
			yield plg
	#----------------------------------------------------------------------	
	def get_Array_Element_Plugs(self):
		res = []
		for index in self.multiIndices:
			plg = self.getElementByIndex(index)
			res.append(plg)
		return res
	#----------------------------------------------------------------------
	def is_Connected_To_Source(self, plg):
		""""""
		return plg.new_obj in self.new_obj.connectedTo(0,1)
	#----------------------------------------------------------------------
	def is_Connected_To_Dest(self, plg):
		""""""
		return plg.new_obj in self.new_obj.connectedTo(1,0)
	#----------------------------------------------------------------------
	value = property(getValue,setValue)
########################################################################
class Enum_MPLUG(MPLUG):
	"""
	This Class Is A Base Class That Holds The A Memeory Pointer to a Nodes Attribute
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	@nodeLockManager
	def set_Enums(self,enumNames):
		cmds.addAttr(self.name, edit=True,  enumName=":".join(enumNames)+":")
########################################################################
class Attribute_Plug_Access(object):
	#----------------------------------------------------------------------
	def __init__(self,mnode):
		""""""
		#cmds.listAttr(mnode)#multi=False,scalar=False,hasData=True,connectable=True,string=(name+"*")
		for item in sorted(list(set([".".join([mnode.name,att.split(".")[0]]) for att in cmds.listAttr(mnode)]))):
			if not hasattr(self,item):
				try:
					plg = MPLUG(str(item))
					setattr(self, item.split(".")[-1], plg)
				except:
					pass
		self._obj = mnode

	# #----------------------------------------------------------------------
	# def __getattribute__(self,name):
		# if not name == "_obj":
			# att_list = sorted(list(set([".".join([mnode.name,att.split(".")[0]]) for att in cmds.listAttr(mnode)])))
			# if not att_list == None:
				# if name in att_list:
					# return MPLUG(self._obj._MFns.findPlug(name,True))
		# return object.__getattribute__(self,name)
########################################################################
class Singleton(object):
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance
########################################################################
class Maya_Node(object):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#_node_collection = Node_Types_Container()
	#----------------------------------------------------------------------
	def __new__(cls,*args,**kwargs):
		if len(args) and not kwargs.has_key("name"):
			nodeName = args[0]
		else:
			nodeName = kwargs.get("nodeName",kwargs.get("name",None))
		if isinstance(nodeName,Maya_Node):
			return nodeName
		obj = object.__new__(cls)
		return obj
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		if len(args):
			nodeName = args[0]
		else:
			nodeName = kwargs.get("nodeName",kwargs.get("name",None))

		self.assign_To_Node(nodeName)
	#----------------------------------------------------------------------
	def get_Mobj(self):
		""""""
		return object.__getattribute__(self, "_MObject")
	#----------------------------------------------------------------------
	def get_ObjectHandle(self):
		""""""
		return object.__getattribute__(self, "_MObjectHandle")
	#----------------------------------------------------------------------
	def assign_To_Node(self, nodeName):
		if nodeName:
			try:
				fns    = nameToNode(nodeName)
				obj    = fns.object()
				handle = make_MObjectHandle(obj)
				self._MObject       = obj
				self._MFns          = fns
				self._MObjectHandle = handle
				self.select_commsnds = Class_Comands.Select_Command_Content(self)
			except StandardError, error:
				raise StandardError(error)
	#----------------------------------------------------------------------
	def __str__(self):
		return self.name
	#----------------------------------------------------------------------
	def __repr__(self):
		return self.name
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.name)
	#----------------------------------------------------------------------
	def isValidMObject(self):
		'''
		validate the MObject, without this Maya will crash if the pointer is no longer valid
		TODO: thinking of storing the dagPath when we fill in the mNode to start with and
		if this test fails, ie the scene has been reloaded, then use the dagPath to refind
		and refil the mNode property back in.... maybe??
		'''
		if self._MObjectHandle is None:
			log.info('_MObjectHandle not yet setup')
			return False
		return _isValidMObjectHandle(self._MObjectHandle)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return unicode(self.name) != unicode(other)
	#----------------------------------------------------------------------
	def __get_name(self):
		if hasattr(self._MFns,"fullPathName"):
			return self._MFns.fullPathName()
		else:
			return self._MFns.name()
	#----------------------------------------------------------------------
	@nodeLockManager
	def __set_name(self,value):
		cmds.rename(self.name,unicode(value))
	#----------------------------------------------------------------------
	@property
	def nice_name(self):
		return self.name.split("|")[-1]
	#----------------------------------------------------------------------
	@property
	def nice_name_wo_ns(self):
		return self.nice_name.split(":")[-1]
	#----------------------------------------------------------------------
	@property
	def namespace(self):
		return ':' + ":".join(self.name.split(":")[:-1])
	#----------------------------------------------------------------------
	@property
	def short_name(self):
		if hasattr(self._MFns,"partialPathName"):
			return self._MFns.partialPathName()
		return self.name
	#----------------------------------------------------------------------
	def Make_Plug(self,att):
		plug = MPLUG(self.name, att)
		if plug.enum:
			plug = Enum_MPLUG(plug)
		return plug
	#----------------------------------------------------------------------
	def Make_Enum_Plug(self,att):
		plug = Enum_MPLUG(self.name, att)
		return plug
	@property
	#----------------------------------------------------------------------
	def has_parent(self):
		""""""
		return False if cmds.listRelatives(self.name, parent=True, path=True) is None else True
	#----------------------------------------------------------------------
	def get_parent(self):
		""""""
		res = cmds.listRelatives(self.name, parent=True, path=True)
		if not res:
			return False
		return Maya_Node(res[0])
	@property
	#----------------------------------------------------------------------
	def allParents(self):
		"""Returns all the parents of this dag node. Normally, this only returns the parent corresponding to the first instance of the object"""
		items = self.name.split("|")[1:]

		res = []
		for i in range(len(items)):
			name = "|".join(items[:i+1])
			name="|"+name
			res.append(name)
		return strings_to_Maya_Nodes(res)
	#----------------------------------------------------------------------
	def connected_Shader(self):
		""""""
		shader = cmds.listConnections(self,d=True,type='shadingEngine')
		if not shader==None:
			shader=Maya_Node(shader[0])
			return shader
		return None
	@property
	#----------------------------------------------------------------------
	def BBox_Center(self):
		bbox = cmds.exactWorldBoundingBox(self)
		x = ( bbox[0]+bbox[3] ) / 2
		y = ( bbox[1]+bbox[4] ) / 2
		z = ( bbox[2]+bbox[5] ) / 2
		vec = newOM.MVector(x, y, z)
		return vec
	@property
	#----------------------------------------------------------------------
	def object_Center(self):
		
		def Mesh_Verts():
			comps = cmds.ls(self.name+".vtx[*]", flatten=True)
			VertCount = len(comps)
			x,y,z = 0.0,0.0,0.0
			for comp in comps:
				pos =  cmds.pointPosition(comp, w=True)
				x += pos[0]
				y += pos[1]
				z += pos[2]
			x = x/VertCount
			y = y/VertCount
			z = z/VertCount
			vec = newOM.MVector(x, y, z)
			return vec
		if self.transfromType == "mesh":
			return Mesh_Verts()
		return self.BBox_Center
	#----------------------------------------------------------------------
	@property
	def children(self):
		""""""
		return strings_to_Maya_Nodes(cmds.listRelatives(self.name, children=True, path=True))
	#----------------------------------------------------------------------
	@property
	def shape_children(self):
		""""""
		return strings_to_Maya_Nodes(cmds.listRelatives(self.name, children=True, path=True, shapes=True))
	#----------------------------------------------------------------------
	@property
	def has_child_transforms(self):
		""""""
		return (cmds.listRelatives(self.name, children=True, path=True,type="transform") != None)
	#----------------------------------------------------------------------
	@property
	def child_transforms(self):
		""""""
		return strings_to_Maya_Nodes(cmds.ls(cmds.listRelatives(self.name, children=True, path=True),type='transform'))
	#----------------------------------------------------------------------
	@property
	def all_transform_Descendents(self):
		""""""
		return strings_to_Maya_Nodes(cmds.listRelatives(self.name, allDescendents=True, path=True, type='transform'))
	#----------------------------------------------------------------------
	@property
	def numberOfChildern(self):
		"""Returns A list of child nodes for the given node if node is not given the first item in the selection list is use"""
		childCount = len(self.children)
		return childCount
	#----------------------------------------------------------------------
	@property
	def allDescendents(self):
		"""all the children, grand-children etc. of this dag node. If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before childre"""
		return strings_to_Maya_Nodes(cmds.listRelatives(self,allDescendents=True,fullPath=True))
	#----------------------------------------------------------------------
	def isType(self,type):
		"true if the object is exactly of the specified type. False otherwise"
		return cmds.objectType(self,isType=type)
	#----------------------------------------------------------------------
	def listSets(self,extendToShape=False):
		sets = cmds.listSets(extendToShape=extendToShape, object=self)
		if sets is None:
			return []
		else:
			return [SelectionSet(s) for s in sets]
	#----------------------------------------------------------------------
	def assined_Container(self):
		""""""
		res = cmds.container(q=True, findContainer=self.name)
		if not res == None:
			res = Container(res)
		return res
	#----------------------------------------------------------------------
	@property
	def assinedDisplayLayer(self):
		"The name of the display layer that this object is assined to"
		if not self.attributeExists("drawOverride"):
			return []
		else:
			layer = cmds.listConnections( self.name+".drawOverride", destination=False, source=True, skipConversionNodes=True, shapes=False, type="displayLayer", exactType=True)
			if layer == None:
				return 'defaultLayer'
			return layer[0]
	#----------------------------------------------------------------------
	def attributeExists(self,attr):
		return cmds.attributeQuery( attr, node=self, exists=True )
	#----------------------------------------------------------------------
	def Add_Simple_Attribute(self,longName,mType,shortName=False,multi=False,defaultValue=False,parent=False,numberOfChildren=False,usedAsFilename=False,hidden=False,writable=True,readable=True,storable=True,keyable=True,enumName=False):
		kwargs = dict(longName=longName, multi=multi, hidden=hidden, writable=writable,readable=readable,storable=storable,keyable=keyable)
		if shortName:
			kwargs["shortName"]=shortName
		if mType in MTypes.DTS:
			kwargs["dataType"]=mType
		elif mType in MTypes.ATS:
			kwargs["attributeType"]=mType
		if not self.attributeExists(longName):
			cmds.addAttr(self,**kwargs)
			if mType in MTypes.CTS:
				if mType.endswith("2"):
					cmds.addAttr(self,dict(longName=longName+"X",at=mType.replace("2",""),parent=self.name+"."+longName))
					cmds.addAttr(self,dict(longName=longName+"Y",at=mType.replace("2",""),parent=self.name+"."+longName))
				elif mType.endswith("3"):
					cmds.addAttr(self,dict(longName=longName+"X",at=mType.replace("3",""),parent=self.name+"."+longName))
					cmds.addAttr(self,dict(longName=longName+"Y",at=mType.replace("3",""),parent=self.name+"."+longName))
					cmds.addAttr(self,dict(longName=longName+"Z",at=mType.replace("3",""),parent=self.name+"."+longName))
		return self.Make_Plug(longName)
	#----------------------------------------------------------------------
	def Add_Enum_Attribute(self,longName,enumNames, remake=True):
		if cmds.attributeQuery(longName, node=self, exists=True ) and remake:
			cmds.deleteAttr( self.name, attribute=longName)
		if not cmds.attributeQuery(longName,node=self, exists=True ):
			cmds.addAttr(self,ln=longName,at="enum",enumName=":".join(enumNames)+":")
		else:
			cmds.addAttr(self.name + "." + longName, edit=True, enumName=":".join(enumNames)+":")
		res = self.Make_Plug(longName)
		isinstance(res, Enum_MPLUG)
		return res
	#----------------------------------------------------------------------
	@nodeLockManager
	def delete(self):
		cmds.delete(self.name)
	#----------------------------------------------------------------------
	def lockNode(self):
		""""""
		cmds.lockNode(self,lock=True)
	#----------------------------------------------------------------------
	def unlockNode(self):
		""""""
		cmds.lockNode(self,lock=False)
	@property
	def isLocked(self):
		return cmds.lockNode(self, q=True, lock=True,lockName=False)
	#----------------------------------------------------------------------
	def toggle_nodeLock(self):
		""""""
		checks = []
		checks.extend(cmds.lockNode(self, query=True,lock=True))
		checks.extend(cmds.lockNode(self, query=True,lockUnpublished=True))
		checks.extend(cmds.lockNode(self, query=True,lockName=True))
		if any(checks):
			cmds.lockNode(self,lock=False)
		else:
			cmds.lockNode(self,lock=True)
	@property
	def plug_access(self):
		if not hasattr(self,"_plug_attriubte_access"):
			self._plug_attriubte_access = Attribute_Plug_Access(self)
		return self._plug_attriubte_access
	#----------------------------------------------------------------------
	@property
	def isFromReferencedFile(self):
		""""""
		return self._MFns.isFromReferencedFile()
	@property
	#----------------------------------------------------------------------
	def reference_node(self):
		""""""
		if self.isFromReferencedFile:
			return Maya_Node(cmds.referenceQuery(self.name,referenceNode=True))
		else:
			return None
	#----------------------------------------------------------------------
	def attributeInfo(self,**kwargs):
		"""([allAttributes=boolean], [bool=boolean], [enumerated=boolean], [hidden=boolean], [inherited=boolean], [internal=boolean], [leaf=boolean], [logicalAnd=boolean], [multi=boolean], [short=boolean], [type=string], [userInterface=boolean], [writable=boolean])"""
		kwargs["allAttributes"]=False
		res = []
		for att in cmds.attributeInfo( self.name , **kwargs):
			print att
			res.append(MPLUG(self.name,att))
		return res
	#----------------------------------------------------------------------
	def select_add(self, **kwargs):
		""""""
		cmds.select(self.name, add=True)
	#----------------------------------------------------------------------
	def select_replace(self, **kwargs):
		kwargs["replace"] = True
		cmds.select(self.name, replace=True)
	#----------------------------------------------------------------------
	def select_hierarchy(self, replace=True):
		self.select_commsnds.add(replace=replace, hierarchy=True)		
	name          = property(fget=__get_name, fset=__set_name)
	transfromType = property(ShapeType)
	try:
		objectType    = property(cmds.objectType)
		objectExists  = property(cmds.objExists)
	except AttributeError:
		pass
########################################################################
class AW_NODE(Maya_Node):
	""""""
########################################################################
class Network(Maya_Node):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, skipSelect=True):
		"""Constructor"""
		if not cmds.objExists(name):
			name = cmds.createNode("network",name=name, skipSelect=skipSelect)
		super(Network,self).__init__(name)
		self.affectedBy        = self.Make_Plug("affectedBy")
		self.affects           = self.Make_Plug("affects")
		#self.affected_By_Nodes = Attribute_Tools.Add_Message_M(self, "affected_By_Nodes", indexMatters=False)
		#self.affects_Nodes     = Attribute_Tools.Add_Message_M(self, "affects_Nodes", indexMatters=False)
		self.lockNode()
	def connect_Affect_By_NetWork(self, network):
		if isinstance(network, Network):
			next_input = self.affectedBy.numConnectedElements
			cmds.connectAttr("Network_A.affects_Nodes" ,"Network_B.affects_Nodes",nextAvailable=True,force=True)
########################################################################
class Script_Node(Maya_Node):
	########################################################################
	class SCRIPT_TYPES:
		Demand                = 0
		OpenClose             = 1
		GUI_OpenClose         = 2
		UI_Configuration      = 3
		Software_Render       = 4
		Software_Frame_Render = 5
		Scene_Configuration   = 6
		Time_Changed          = 7
	
	########################################################################
	class SOURCE_TYPES:
		mel    = 'mel'
		python = "python"
	#----------------------------------------------------------------------
	def __init__(self,name,afterScript="",beforeScript="",executeAfter=False, executeBefore=False, scriptType=0, sourceType="python"):
		kwargs = dict(afterScript=afterScript,beforeScript=beforeScript,executeAfter=executeAfter, executeBefore=executeBefore, name=name,scriptType=scriptType, sourceType=sourceType)
		if not cmds.objExists(name):
			name = cmds.scriptNode(**kwargs)
		super(Script_Node,self).__init__(name)
		self.before      = self.Make_Plug("before")
		self.after       = self.Make_Plug("after")
		self.scriptType  = self.Make_Plug("scriptType")
		self.sourceType  = self.Make_Plug("sourceType")

	#----------------------------------------------------------------------
	def executeAfter(self):
		cmds.scriptNode( self, executeAfter=True )

	#----------------------------------------------------------------------
	def executeBefore(self):
		cmds.scriptNode( self, executeBefore=True )
########################################################################
class RenderLayer(Maya_Node):
	#----------------------------------------------------------------------
	def __init__(self,name,makeCurrent=False,empty=True,noRecurse=True):
		kwargs = dict(name=name,makeCurrent=makeCurrent,empty=empty,noRecurse=noRecurse)

		if not cmds.objExists(name):
			name = cmds.createRenderLayer(**kwargs)

		super(RenderLayer,self).__init__(name)
	#----------------------------------------------------------------------
	@nodeLockManager
	def addMembers(self,items):
		if not items == None:
			if len(items):
				cmds.editRenderLayerMembers(self,items)
	#----------------------------------------------------------------------
	@nodeLockManager
	def include_special(self):
		self.addMembers(cmds.listRelatives(cmds.listRelatives(allDescendents=True,type=["mesh",'VRayLightRectShape',"light"],path=True),parent=True,type="transform",path=True))
	#----------------------------------------------------------------------
	@nodeLockManager
	def removeMembers(self,items):
		if len(items):
			cmds.editRenderLayerMembers( self, items, remove=True)
	#----------------------------------------------------------------------
	@nodeLockManager
	def remove_selected(self):
		self.removeMembers(cmds.ls(sl=True))
	#----------------------------------------------------------------------
	@property
	def baseID(self):
		return cmds.editRenderLayerGlobals(self,query=True, baseId=True )
	#----------------------------------------------------------------------
	def makeCurrent(self):
		try:
			cmds.editRenderLayerGlobals(currentRenderLayer=self)
		except RuntimeError:
			pass
	#----------------------------------------------------------------------
	@nodeLockManager
	def enable_Attribute_overRide(self,Plugs):
		cmds.editRenderLayerAdjustment(Plugs,layer=self.name)
	#----------------------------------------------------------------------
	@property
	def members(self):
		items = cmds.editRenderLayerMembers( self,fullNames=True, query=True )
		if items == None:
			return []
		else:
			return [Maya_Node(m) for m in items]
	#----------------------------------------------------------------------
	def select_Members(self):
		items = self.members
		if len(items):
			cmds.select(self.members,replace=True)
		else:
			cmds.select(clear=True)
	#----------------------------------------------------------------------
	def select_Set(self):
		cmds.select(self,replace=True)
########################################################################
class DisplayLayer(Maya_Node):
	Normal,Reference,Template = range(3)
	#----------------------------------------------------------------------
	def __init__(self,name,makeCurrent=False,empty=True,noRecurse=True):
		kwargs = dict(name=name,makeCurrent=makeCurrent,empty=empty,noRecurse=noRecurse)
		if not cmds.objExists(name):
			name = cmds.createDisplayLayer(**kwargs)

		super(DisplayLayer,self).__init__(name)
		if self.attributeExists("drawInfo"):
			self.drawinfo      = self.Make_Plug("drawInfo")
		if self.attributeExists("visibility"):
			self.visibility    = self.Make_Plug("visibility")
		if self.attributeExists("displayType"):
			self.displayType   = self.Make_Plug("displayType")
		if self.attributeExists("color"):
			self.color         = self.Make_Plug("color")
		if self.attributeExists("playback"):
			self.playback      = self.Make_Plug("playback")
		if self.attributeExists("shading"):
			self.shading       = self.Make_Plug("shading")
		if self.attributeExists("texturing"):
			self.texturing     = self.Make_Plug("texturing")
		if self.attributeExists("levelOfDetail"):
			self.levelOfDetail = self.Make_Plug("levelOfDetail")
		if self.attributeExists("displayOrder"):
			self.displayOrder  = self.Make_Plug("displayOrder")

	#----------------------------------------------------------------------
	@nodeLockManager
	def addMembers(self,*items, **kwargs):
		noRecurse = kwargs.get("noRecurse", False)
		items = flatten(items)
		items = [item for item in items if cmds.objExists(item)]
		if items:
			cmds.editDisplayLayerMembers(self, items, noRecurse=noRecurse)
	#----------------------------------------------------------------------
	@nodeLockManager
	def removeMembers(self,*items, **kwargs):
		noRecurse = kwargs.get("noRecurse", False)
		items = flatten(items)
		items = [item for item in items if cmds.objExists(item)]
		if items:
			cmds.editDisplayLayerMembers("defaultLayer", items,noRecurse=noRecurse)

	#----------------------------------------------------------------------
	@nodeLockManager
	def include_Selected(self):
		items = cmds.ls(sl=True)
		if items == None:
			items = []
		self.addMembers(items, noRecurse=True)

	#----------------------------------------------------------------------
	@nodeLockManager
	def clear(self):
		items = self.member_names
		if items:
			cmds.editDisplayLayerMembers("defaultLayer", items)

	#----------------------------------------------------------------------
	def makeCurrent(self):
		cmds.editDisplayLayerGlobals( cdl=self )

	#----------------------------------------------------------------------
	@property
	def members(self):
		items = cmds.editDisplayLayerMembers(self,q=True,fullNames=True)
		if items == None:
			return []
		else:
			return [Maya_Node(m) for m in items]

	#----------------------------------------------------------------------
	@property
	def member_names(self):
		return [unicode(item.name) for item in self.members]

	#----------------------------------------------------------------------
	def select_Members(self, replace=True, add=False, remove=False):
		if len(self.members):
			if add:
				cmds.select(self.members,add=True)
			elif remove:
				cmds.select(self.members,deselect=True)
			else:
				cmds.select(self.members,replace=True)
		else:
			cmds.select(clear=True)
	#----------------------------------------------------------------------
	def select_Set(self):
		cmds.select(self,replace=True)

	#----------------------------------------------------------------------
	def show(self):
		self.visibility.setValue(1)

	#----------------------------------------------------------------------
	def hide(self):
		self.visibility.setValue(0)
########################################################################
class Display_Layer_Manager(Maya_Node):
	#__metaclass__ = Scripts.Global_Constants.Singleton.Singleton
	#----------------------------------------------------------------------
	def __init__(self, name="layerManager"):
		""""""
		super(Display_Layer_Manager,self).__init__(name)
		self.message             = self.Make_Plug("message")
		self.currentDisplayLayer = self.Make_Plug("currentDisplayLayer")
		self.displayLayerId      = self.Make_Plug("displayLayerId")

	@property
	def layers(self):
		return [DisplayLayer(l) for l in self.displayLayerId.input_Nodes if not l.name == "defaultLayer"]
	@property
	def current_layer(self):
		return DisplayLayer(cmds.editDisplayLayerGlobals(query=True,currentDisplayLayer=True))
	#----------------------------------------------------------------------
	def clean_LayerId_Indexing(self):
		plug = self.displayLayerId
		if range(plug.numConnectedElements) != plug.multiIndices:
			connection_plgs = plug.element_plugs
			if len(connection_plgs) > 1:
				connection_plgs = connection_plgs[1:]
				with MayaUndoChunk():
					for plg in connection_plgs:
						for input_plg in plg.input_Plugs:
							cmds.disconnectAttr(input_plg, plg)
					for index, plg in enumerate(connection_plgs):
						index += 1
						try:
							cmds.connectAttr(plug.name+"[%i]" % index, plg.name,force=True)
						except:
							pass
		
					for plg in plug.multiElements:
						if not plg.isConnected:
							cmds.removeMultiInstance(plg.name,b=True)
########################################################################
class Render_Layer_Manager(Maya_Node):
	#__metaclass__ = Scripts.Global_Constants.Singleton.Singleton

	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		super(Render_Layer_Manager,self).__init__("renderLayerManager")
		self.message                   = self.Make_Plug("message")
		self.isHistoricallyInteresting = self.Make_Plug("isHistoricallyInteresting")
		self.nodeState                 = self.Make_Plug("nodeState")
		self.binMembership             = self.Make_Plug("binMembership")
########################################################################
class Partition(Maya_Node):
	def __init__(self,name, render=False, selection_sets=None):
		kwargs = dict(name=name)
		
		if render:
			kwargs["render"] = True
		
		if not cmds.objExists(name):
			if selection_sets is not None:
				name = cmds.partition(selection_sets, **kwargs)
			else:
				name = cmds.partition(**kwargs)
			
		super(Partition,self).__init__(name,**kwargs)
		
	#----------------------------------------------------------------------
	@nodeLockManager
	def delete(self):
		super(Partition,self).delete()
	#----------------------------------------------------------------------
	@nodeLockManager
	def removeSet(self,*items):
		items = flatten(items)
		if len(items):
			cmds.partition( items, removeSet=self)
	#----------------------------------------------------------------------
	@nodeLockManager
	def addSet(self,*items):
		items = flatten(items)
		if len(items):
			cmds.partition( items, addSet=self)
			
	#----------------------------------------------------------------------
	@property
	def members(self):
		sets = cmds.partition( self, q=True )
		if sets is not None:
			sets = [SelectionSet(s) for s in sets]
			return sets
		else:
			return []
########################################################################
class SelectionSet(Maya_Node):
	#sets( selectionList , [addElement=name], [afterFilters=boolean], [color=int], [copy=name], [edges=boolean], [editPoints=boolean], [empty=boolean], [facets=boolean], [flatten=name], [forceElement=name], [include=name], [intersection=name], [isIntersecting=name], [isMember=name], [layer=boolean], [name=string], [noSurfaceShader=boolean], [noWarnings=boolean], [nodesOnly=boolean], [remove=name], [renderable=boolean], [size=boolean], [split=name], [subtract=name], [text=string], [union=name], [vertices=boolean])
	def __init__(self,name,empty=False,copy=None,text="bookmarkModelView", edges=False, vertices=False, facets=False, editPoints=False, color=-1, elements=None):
		kwargs = dict(name=name, empty=empty, text=text)
		
		if edges:
			kwargs["edges"] = True
		if vertices and not any([edges]):
			kwargs["vertices"] = True
		if facets and not any([edges, vertices]):
			kwargs["facets"] = True
		if editPoints and not any([facets, edges, vertices]):
			kwargs["editPoints"] = True
			
		if copy and not any([edges, facets, edges, vertices]):
			kwargs["copy"]=copy
			
		if not cmds.objExists(name):
			name = cmds.sets(**kwargs)
			
		super(SelectionSet,self).__init__(name,**kwargs)

		if self.attributeExists("annotation"):
			self._annotation_plug    = self.Make_Plug("annotation")
		if self.attributeExists("message"):
			self._message_plug       = self.Make_Plug("message")
		if self.attributeExists("dnSetMembers"):
			self._dnSetMembers_plug  = self.Make_Plug("dnSetMembers")
		if self.attributeExists("dagSetMembers"):
			self._dagSetMembers_plug = self.Make_Plug("dagSetMembers")
	#----------------------------------------------------------------------
	@nodeLockManager
	def delete(self):
		self.remove(self.transform_members)
		super(SelectionSet,self).delete()
	#----------------------------------------------------------------------
	@nodeLockManager
	def clear(self):
		cmds.sets(clear=self)
	#----------------------------------------------------------------------
	def select_set(self):
		cmds.select(self,ne=True,replace=True)
	#----------------------------------------------------------------------
	def select_members(self):
		cmds.select(self,replace=True)
	#----------------------------------------------------------------------
	def copy(self, name=None):
		""""""
		if name is None:
			return SelectionSet(cmds.sets(copy=self))
		else:
			return SelectionSet(cmds.sets(copy=self, name=name))
	#----------------------------------------------------------------------
	@property
	def size(self):
		cmds.sets(size=True,q=True)
	#----------------------------------------------------------------------
	@nodeLockManager
	def remove(self,*items):
		items = flatten(items)
		if len(items):
			cmds.sets( items, remove=self)
	#----------------------------------------------------------------------
	@nodeLockManager
	def remove_selected(self):
		cmds.sets(cmds.ls(sl=True, long=True), remove=self)
	#----------------------------------------------------------------------
	@nodeLockManager
	def include(self,*items):
		#self.__rshift__(items)
		items = flatten(items)
		if len(items):
			cmds.sets( items, include=self)
	#----------------------------------------------------------------------
	@nodeLockManager
	def include_special(self,*items):
		items = flatten(items)
		if len(items):
			items_check =  cmds.listRelatives(cmds.listRelatives(items,allDescendents=True,type=["mesh",'VRayLightRectShape',"light"],path=True),parent=True,type="transform",path=True)
			if not items_check ==  None:
				self.include(items_check)
	#----------------------------------------------------------------------
	@nodeLockManager
	def addElement(self,*items):
		#self.__rshift__(items)
		items = flatten(items)
		if len(items):
			cmds.sets( items, addElement=self)
	#----------------------------------------------------------------------
	def intersecting_members(self,selectionSet):
		items = cmds.sets(selectionSet,intersection=self)
		return [Maya_Node(obj) for obj in items]
	#----------------------------------------------------------------------
	@property
	def memberNames(self):
		return [unicode(m) for m in self.members]
	#----------------------------------------------------------------------
	@property
	def query_members(self):
		""""""
		return cmds.sets( self, q=True )
	#----------------------------------------------------------------------
	@property
	def transform_members(self):
		try:
			return [Maya_Node(m) for m in cmds.listConnections(self._dagSetMembers_plug.name,type="transform",destination=False,source=True)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	@property
	def members(self):
		try:
			return [Maya_Node(m) for m in cmds.listConnections(self._dagSetMembers_plug.name,destination=False,source=True, shapes=True)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	def hasMembers(self, items):
		""""""
		return cmds.sets(items, isMember=self.name)
	#----------------------------------------------------------------------
	@property
	def parents(self):
		try:
			return [SelectionSet(m) for m in cmds.listConnections(self._message_plug.name,type="objectSet",destination=True,source=False)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	@property
	def absolute_Parents(self):
		#----------------------------------------------------------------------
		def parent_scan(child, res=[]):
			parents = child.parents
			if len(parents):
				for parent in parents:
					parent_scan(parent, res)
			else:
				if not str(child) in [str(item) for item in res]:
					res.append(child)
			return res
		scan_res = parent_scan(self)
		for item in scan_res:
			if not item.has_Child_Set(self):
				scan_res.remove(item)
		return scan_res
	#----------------------------------------------------------------------
	@property
	def children(self):
		try:
			return [SelectionSet(m) for m in cmds.listConnections(self._dnSetMembers_plug.name,type="objectSet",destination=True,source=True)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	@property
	def all_children(self):
		def _get_children_recursivly(root, collection=[]):
			for item in root.children:
				collection.append(item)
				_get_children_recursivly(item, collection)
			return collection
		try:
			return _get_children_recursivly(self)
		except TypeError:
			return []
	#----------------------------------------------------------------------
	def isSubSet(self,item):
		return str(item) in [str(m) for m in self.parents]
	#----------------------------------------------------------------------
	def hasSubSet(self,item):
		return str(item) in [str(m) for m in self.children]
	#----------------------------------------------------------------------
	def has_Child_Set(self,item):
		if self.hasSubSet(item):
			return True
		else:
			for item in item.parents:
				if self.has_Child_Set(item):
					return True
		return False
	#----------------------------------------------------------------------
	def has_Parent_Set(self,item):
		return item.has_Child_Set(self)
	#----------------------------------------------------------------------
	def __contains__(self,item):
		return Maya_Node(item.name)._MObject in [m._MObject for m in self.members]
	#----------------------------------------------------------------------
	@nodeLockManager
	def __rshift__(self,*items):
		items_to_add = []
		names = self.memberNames
		for item in flatten(items):
			if not str(item) in names:
				items_to_add.append(item)
		if len(items_to_add):
			cmds.sets( items_to_add, include=self)
		#self.include(items_to_add)
	#----------------------------------------------------------------------
	@nodeLockManager
	def __lshift__(self,*items):
		items_to_remove = []
		for item in flatten(items):
			if item in self:
				items_to_remove.append(item)

		self.remove(items_to_remove)
	#----------------------------------------------------------------------
	def Find_All_Sub_Set_Innersecting_Sets(self):
		children = self.children
		inersecting_sets = SelectionSet(self.name+"_Intersecting_SubSets", empty=True, text="")
		found_pairs = []
		for childA in children:
			for childB in [child for child in children if not child == childA]:
				intersecting_items = childA.intersecting_members(childB)
				if intersecting_items:
					if not [childA,childB] in found_pairs and not [childB,childA] in found_pairs:
						found_pairs.append([childA,childB])

						print "Intersecting Members found between Sets %s and %s with items %r" % (childA,childB,intersecting_items)
						cmds.select(intersecting_items)
						sub_set = SelectionSet(childA.name+"_"+childB.name)
						inersecting_sets >> sub_set
		return inersecting_sets
########################################################################
class Shading_Node(Maya_Node):
	def __init__(self, name, shaderType="surfaceShader"):
		if not cmds.objExists(name):
			name = cmds.shadingNode(shaderType,asShader=True,name=name)
			nameSG = cmds.sets( name=name+"SG", renderable=True, empty=True ) 
			cmds.surfaceShaderList( name, add=nameSG)
		super(Shading_Node,self).__init__(name)
		if self.attributeExists("outColor"):
			self.outColor = self.Make_Plug("outColor")
	@property
	def shading_engine(self):
		res = cmds.listConnections(self, s=0,d=1,type="shadingEngine")
		if res is None:
			nameSG = cmds.sets( name=self.short_name+"SG", renderable=True, empty=True )
			cmds.surfaceShaderList( self.name, add=nameSG)
			return Shading_Engine(nameSG)
		res =  Shading_Engine(res[0])
		return res
########################################################################
class Shading_Engine(SelectionSet):
	def __init__(self,name):
		kwargs = dict(renderable=True,empty=True,text="")
		if not cmds.objExists(name):
			name = cmds.sets(renderable=True,empty=True,text="",name=name)
		elif not cmds.objectType(name,isType="shadingEngine"):
			raise TypeError("The Object %r Could Not Assine To A Shader Engine")
		super(Shading_Engine,self).__init__(name,**kwargs)
		self.surfaceShader = self.Make_Plug("surfaceShader")
		if False:
			isinstance(self.assined_material, Shading_Node)
	#----------------------------------------------------------------------
	def select_set(self):
		cmds.select(self,ne=True,replace=True)
	#----------------------------------------------------------------------
	def select_members(self):
		cmds.select(self,replace=True)
	#----------------------------------------------------------------------
	@property
	def size(self):
		cmds.sets(self,size=True,q=True)
	#----------------------------------------------------------------------
	def remove(self,items):
		cmds.sets( items, remove=self)
	#----------------------------------------------------------------------
	def remove_selected(self):
		cmds.sets(cmds.ls(sl=True), remove=self)
	#----------------------------------------------------------------------
	def include(self,*items):
		#self.__rshift__(items)
		items = flatten(items)
		if len(items):
			cmds.sets(items,forceElement=self)
	#----------------------------------------------------------------------
	def addElement(self,*items):
		#self.__rshift__(items)
		items = flatten(items)
		items = [item for item in items if cmds.objExists(item)]
		if len(items):
			cmds.sets(items, edit=True, forceElement=self)
	#----------------------------------------------------------------------
	@property
	def memberNames(self):
		return [unicode(m) for m in self.members]
	#----------------------------------------------------------------------
	@property
	def members(self):
		try:
			return [Maya_Node(m) for m in cmds.listConnections(self._dagSetMembers_plug.name,shapes=True,destination=False,source=True) if not cmds.objectType(m) in ["renderLayer","displayLayer"]]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	@property
	def parents(self):
		try:
			return [SelectionSet(m) for m in cmds.listConnections(self._message_plug.name,type="objectSet",destination=True,source=False)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	def Assine_To_Material(self,shader):
		shader_plug = str(shader)+".outColor"
		try:
			cmds.connectAttr(shader_plug,self.surfaceShader,force=True)
		except:
			pass

	#----------------------------------------------------------------------
	@property
	def assined_material(self):
		nodes = self.surfaceShader.input_Nodes
		if not len(nodes):
			return None
		return Shading_Node(nodes[0].name)
########################################################################
class AnimCurve(Maya_Node):
	#----------------------------------------------------------------------
	def __init__(self,name):
		if not cmds.objExists(name):
			raise ValueError("The Anim Curve Name % Does Not Exist" % name)	
		super(AnimCurve,self).__init__(name)
	
		# Most common tangent type of keyframes in this curve.
		# Used as a performance optimization during file store/retrieve.
		# The following are legal values:
		# 1=Fixed, 2=Linear, 3=Flat, 5=Step, 6=Slow, 7=Fast, 9=Spline, 10=Clamped, 16 = Plateau, 17 = StepNext, 18 = Auto
		self.tangentType = self.Make_Enum_Plug("tangentType")
		
		# Specifies whether or not the tangents on the animCurve are weighted
		self.weightedTangents = self.Make_Plug("weightedTangents")
		
		# True makes the in- and out-tangents move together.
		# False makes them move separately.
		self.keyTanLocked = self.Make_Plug("keyTanLocked")
		
		# True prevents changes to the tangent weight.
		# False allows changes.
		self.keyWeightLocked = self.Make_Plug("keyWeightLocked")
		
		# The horizontal component of the keyframe in-tangent
		self.keyTanInX = self.Make_Plug("keyTanInX")
		
		# The vertical component of the keyframe in-tangent
		self.keyTanInY = self.Make_Plug("keyTanInY")
		
		# The horizontal component of the keyframe out-tangent
		self.keyTanOutX = self.Make_Plug("keyTanOutX")
		
		# The vertical component of the keyframe out-tangent
		self.keyTanOutY = self.Make_Plug("keyTanOutY")
		
		# The tangent type of the keyframe's in tangent.
		# The following are legal values:
		# 1=Fixed, 2=Linear, 3=Flat, 5=Step, 6=Slow, 7=Fast, 9=Spline, 10=Clamped, 16 = Plateau, 18 = Auto
		self.keyTanInType = self.Make_Enum_Plug("keyTanInType")
		
		# The tangent type of the keyframe's out tangent.
		# The following are legal values:
		# 1=Fixed, 2=Linear, 3=Flat, 5=Step, 6=Slow, 7=Fast, 9=Spline, 10=Clamped, 16 = Plateau, 17 = StepNext, 18 = Auto
		self.keyTanOutType = self.Make_Enum_Plug("keyTanOutType")
		
		# True makes this key act as a breakdown.
		# False makes this key a key.
		self.keyBreakdown = self.Make_Plug("keyBreakdown")
		
		# True causes the tick mark representing a given key to be drawn specially in the time-slider using the user-definable special tick color.
		# False causes the tick mark representing a given key to be drawn normally.
		self.keyTickDrawSpecial = self.Make_Plug("keyTickDrawSpecial")
		
		# This attribute specifies how the curve data is interpolated if the curve is being utilised for rotation.
		# The following are legal values:
		# 1="None" for Unsynchronized Euler angled curves, where keyframes on sibling curves are independent.
		# For non-rotational curves, this is the only possible setting.
		# 2="Euler" for synchronized Euler-angled curves where sibling curve keyframes are coincident in time sibling curve,
		# 3="Quaternion Tangent Dependent" for synchronized quaternion interpolation where sibling curve keyframes are coincident
		#    and quaternion interpolation is performed between keyframes, taking into account the tangents on individual keys.
		# 4="Quaternion Slerp" applies quaternion spherical linear interpolation, ignoring any tangents
		# 5="Quaternion Squad" applies a cubic interpolation in quaternion space, ignoring any tangents
		# "None" (1) for non-rotational curves as well as for pre-4.0 rotational behaviour.
		self.rotationInterpolation = self.Make_Enum_Plug("rotationInterpolation")
		
		# Controls how the curve is evaluated before the first keyframe.
		# The following are legal values:
		# 0=Constant, 1=Linear, 3=Cycle, 4=Cycle with Offset, 5=Oscillate
		self.preInfinity = self.Make_Enum_Plug("preInfinity")
		
		# Controls how the curve is evaluated after the last keyframe.
		# The following are legal values:
		# 0=Constant, 1=Linear, 3=Cycle, 4=Cycle with Offset, 5=Oscillate
		self.postInfinity = self.Make_Enum_Plug("postInfinity")
		
		# An Enum to set the stipple pattern for the sections of the anim curve that are specified by the stippleRegion attribute.
		# The default is long dotted (--- --- --- ---).
		self.stipplePattern = self.Make_Enum_Plug("stipplePattern")
		
		# If the anim curve gets at or below this value,
		# the outStippleRange will treat it as a region to stipple.
		self.outStippleThreshold = self.Make_Plug("outStippleThreshold")
		
		# A double array containing pairs of ranges 
		# (if time, in seconds) of regions when the anim curve is below the stippleThreshold.
		self.outStippleRange = self.Make_Plug("outStippleRange")
		
		# A double array that contains pairs of ranges to stipple.
		self.inStippleRange = self.Make_Plug("inStippleRange")
		
		# When true, the stippled regions will become unstippled, and the solid regions will become stippled.
		# This attribute will only have an effect if the inStippleRange attribute is connected.
		self.stippleReverse = self.Make_Plug("stippleReverse")
		
		# Specifies the display style for this curve.
		# If false, Maya's default color scheme is used for drawing the curve.
		# If true, the value of the curveColor attribute is used for drawing.
		self.useCurveColor = self.Make_Plug("useCurveColor")
	#----------------------------------------------------------------------
	@property
	def frame_count(self):
		return cmds.keyframe(self, query=True, keyframeCount=True )
	#----------------------------------------------------------------------
	@property
	def key_times(self):
		return cmds.keyframe(self,index=(0,self.frame_count),timeChange=True,query=True)
	#----------------------------------------------------------------------
	@property
	def key_values(self):
		return cmds.keyframe(self,index=(0,self.frame_count),valueChange=True,query=True)
	#----------------------------------------------------------------------
	@property
	def key_indices(self):
		return cmds.keyframe(self, query=True, indexValue=True)
	#----------------------------------------------------------------------
	@property
	def key_time_values(self):
		return cmds.keyframe(self,index=(0,self.frame_count),timeChange=True,valueChange=True,query=True)
	#----------------------------------------------------------------------
	@property
	def current_driven_key_driver(self):
		"""To query the current driver"""
		res = cmds.setDrivenKeyframe( self, q=True, cd=True )
		if res[0] == "No drivers.":
			return []
		return res
	#----------------------------------------------------------------------
	@property
	def driven_key_driver_plugs(self):
		"""Returns list of available drivers for the attribute."""
		plgs = self.connected_output_attribute_plugs
		if plgs:
			print plgs
			res = cmds.setDrivenKeyframe( plgs, q=True, dr=True )
			if res[0] == "No drivers.":
				return []
			return [MPLUG(node) for node in res]
		return []
	#----------------------------------------------------------------------
	@property
	def driven_key_plugs(self):
		"""To query the current driven"""
		plgs = self.connected_output_attribute_plugs
		if plgs:
			res = cmds.setDrivenKeyframe( plgs, q=True, dn=True )
			if res[0] == "No drivers.":
				return []
			return [MPLUG(node) for node in res]
		return []
########################################################################
class Container(Maya_Node):
	def __init__(self,name, clear_current=True, dagContainer=False, force=False,addNode=False,current=False,includeShaders=False,publishConnections=False,nodeNamePrefix=False,includeHierarchyAbove=False,includeHierarchyBelow=False):
		kwargs = dict(name=name,current=current,includeShaders=includeShaders,publishConnections=publishConnections,includeHierarchyAbove=includeHierarchyAbove,includeHierarchyBelow=includeHierarchyBelow)
		if publishConnections:
			kwargs["nodeNamePrefix"]=nodeNamePrefix
		if addNode:
			kwargs["addNode"]=addNode
			kwargs["force"]=force
		if dagContainer:
			kwargs["type"] = "dagContainer"
		if clear_current:
			cmds.ClearCurrentContainer()
		if not cmds.objExists(name):
			name = cmds.container(**kwargs)

		super(Container,self).__init__(name)


		self._make_plugs()
	#----------------------------------------------------------------------
	def _make_plugs(self):
		#The hyperLayout attribute that stores depend nodes belonging to this container node. 
		self.hyperLayout               = self.Make_Plug("hyperLayout")

		#collapsed state of container
		self.isCollapsed               = self.Make_Plug("isCollapsed")

		#Tells the UI to treat the container as a black box.
		#Only published nodes such as the root transform and published parent/children will be displayed
		self.blackBox                  = self.Make_Plug("blackBox")

		#Attributes on container nodes with connections to exterior nodes get connected to this attribute to indicate the exterior connection. 
		self.borderConnections         = self.Make_Plug("borderConnections")

		#Indicates which of the connections to the borderConnections
		#multi represents a hierarchical publishing connection.
		#Used by referencing to determine which alias to save as or resolve to.
		self.isHierarchicalConnection  = self.Make_Plug("isHierarchicalConnection")

		#Indicates the name of a mel file that will be called to populate the right-mouse-button (RMB)
		#with entries when a container member is RMBed on in the main scene.
		#The mel file must return an array of strings of the form:{"Label for menu entry 1", "CallbackToInvoke1", "Label for menu entry 2", "CallbackToInvoke2", ... }
		#The callback should be a global mel proc which takes a string argument.
		#The callback will be sent the name of the object which was RMBed on.
		#See the mel file containerRmbMenu.mel for an example.
		self.rmbCommand                = self.Make_Plug("rmbCommand")

		#Template name associated with this container.
		self.templateName              = self.Make_Plug("templateName")	

		#Template version.
		self.templateVersion           = self.Make_Plug("templateVersion")	

		#Template file path.
		self.templatePath              = self.Make_Plug("templatePath")

		#View selection mode  
		self.viewMode                  = self.Make_Plug("viewMode")

		#Icon filename for hyperGraph views. (jpg,jpeg,bmp or gif) 
		self.iconName                  = self.Make_Plug("iconName")

		#View selection mode  
		self.viewMode                  = self.Make_Plug("viewMode")

		#Set at creation time to the user who created the node. 
		self.creator                   = self.Make_Plug("creator")		

		#Set at creation time to the current date. 
		self.creationDate              = self.Make_Plug("creationDate")

		#Nodes inside container can connect to this attribute to indicate
		#that they should be selected if the user has enabled
		#container-centric selection and a child node is selected.
		#Also, when exporting a container proxy, any published root transformation attributes such as
		#translate, rotate or scale will be hooked up to attributes on a stand-in node.
		self.rootTransform               = self.Make_Plug("creationDate")


	#----------------------------------------------------------------------
	def bindAttr(self,nodeAttr,unboundName):
		"""
		Bind a contained attribute to an unbound published name on the interface of the container
		returns a list of bound published names.
		The first string specifies the node and attribute name to be bound in "node.attr" format.
		The second string specifies the name of the unbound published name.
		In query mode, returns a string array of the published names and their corresponding attributes.
		The flag can also be used in query mode in conjunction with the
		-publishName, -publishAsParent, and -publishAsChild flags.
		"""
		return cmds.container(self,edit=True,bindAttr=[nodeAttr,unboundName])
	#----------------------------------------------------------------------
	def unbindAttr(self,nodeAttr,unboundName):
		"""Unbind a published attribute from its published name on the interface of the container,
		leaving an unbound published name on the interface of the container
		returns a list of unbound published names.
		The first string specifies the node and attribute name to be unbound in "node.attr" format,
		and the second string specifies the name of the bound published name.
		In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
		"""
		return cmds.container(self,edit=True,unbindAttr=[nodeAttr,unboundName])
	#----------------------------------------------------------------------
	def unpublishName(self,name):
		"""Unpublish an unbound name from the interface of the container."""
		return cmds.container(self,edit=True,unpublishName=name)
	#----------------------------------------------------------------------
	def unbindAndUnpublish(self,name):
		""""""
		return cmds.container(self,edit=True,unbindAndUnpublish=name)
	#----------------------------------------------------------------------
	def publishName(self,name,bindTo=""):
		"""
		Publish a name to the interface of the container

		if bindTo is set with the format "node.attr"
		  Publish the given name and bind the attribute to the given name

		returns the actual name published to the interface.
		"""
		if (bindTo!=""):
			return cmds.container(self,edit=True,publishAndBind=[bindTo,name])
		else:
			return cmds.container(self,edit=True,publishName=name)
	#----------------------------------------------------------------------
	def publishAsParent(self,node,name):
		"""Publish contained node to the interface of the container to indicate it can be a parent to external nodes.
		The second string is the name of the published node.
		In query mode, 
		  returns a string of array of the published names and the corresponding nodes.

		If -publishName flag is used in query mode,
		  only returns the published names;

		if -bindAttr flag is used in query mode,
		  only returns the name of the published nodes."""
		return cmds.container(self,edit=True,publishAsParent=[node,name])
	#----------------------------------------------------------------------
	def unpublishParent(self,name):
		""""""
		return cmds.container(self,edit=True,unpublishParent=name)
	#----------------------------------------------------------------------
	def unpublishChild(self,name):
		""""""
		return cmds.container(self,edit=True,unpublishChild=name)
	#----------------------------------------------------------------------
	def publishAsChild(self,node,name):
		"""Publish contained node to the interface of the container to indicate it can be a child of external nodes.
		The second string is the name of the published node.
		In query mode,
		  returns a string of the published names and the corresponding nodes.

		If -publishName flag is used in query mode,
		  only returns the published names;

		if -bindAttr flag is used in query mode,
		  only returns the name of the published nodes."""

		return cmds.container(self,edit=True,publishAsChild=[node,name])
	#----------------------------------------------------------------------
	def publishedNames(self,bound=False,unBound=False,parents=False,children=False,NodeAttr=""):
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

		kwargs = dict(query=True,publishName=True)

		if (NodeAttr!=""):
			kwargs["publishAttr"]=NodeAttr
		else:
			if bound:
				kwargs["bindAttr"]=True
			elif unBound:
				kwargs["unbindAttr"]=True

			if parents:
				kwargs["publishAsParent"]=True
			elif children:
				kwargs["publishAsChild"]=True

		return cmds.container(self,**kwargs)
	#----------------------------------------------------------------------
	def addNode(self, nodes, includeNetwork=False, includeHierarchyBelow=False):
		""""""
		nodes = flatten(nodes)
		if len(nodes):
			return cmds.container(self,edit=True,addNode=nodes, includeNetwork=includeNetwork, includeHierarchyBelow=includeHierarchyBelow, force=True)
	#----------------------------------------------------------------------
	def addSelectedNodes(self, includeNetwork=False, includeHierarchyBelow=False):
		""""""
		nodes = cmds.ls(sl=True)
		if len(nodes):
			return cmds.container(self,edit=True,force=True, addNode=nodes, includeNetwork=includeNetwork, includeHierarchyBelow=includeHierarchyBelow)
	#----------------------------------------------------------------------
	def removeNode(self,*nodes):
		"""Specifies the list of nodes to remove from container."""
		nodes = flatten(nodes)
		if len(nodes):
			return cmds.container(self,edit=True,removeNode=[nodes])
	#----------------------------------------------------------------------
	@property
	def nodeList(self):
		"""Specifies the list of nodes to remove from container."""
		return strings_to_Maya_Nodes(cmds.container(self,query=True,nodeList=True))
	#----------------------------------------------------------------------
	@property
	def nodeListNames(self):
		"""Specifies the list of nodes to remove from container."""
		return cmds.container(self,query=True,nodeList=True)
	#----------------------------------------------------------------------
	@property
	def select_Container_Contents(self):
		cmds.SelectContainerContents(self)
	#----------------------------------------------------------------------
	@property
	def select_Transform_Descendents(self):
		cmds.select(self.all_transform_Descendents)
	#----------------------------------------------------------------------
	@property
	def select_All_Descendents(self):
		cmds.select(self.allDescendents)
	#----------------------------------------------------------------------
	@property
	def select_All_Parents(self):
		cmds.select(self.allParents)
	#----------------------------------------------------------------------
	@classmethod
	def fileName(cls,filepath):
		""""""
		return cmds.container(q=True,fileName=filepath)
	#----------------------------------------------------------------------
	def makeCurent(self):
		""""""
		return cmds.container(self,edit=True,current=True)

	#----------------------------------------------------------------------
	@property
	def parentContainer(self):
		""""""
		res = cmds.container(self,q=True,parentContainer=True)
		if res:
			res = Container(res)
		return res

	#----------------------------------------------------------------------
	def asset(self,*nodes):
		""""""
		nodes = flatten(nodes)
		return (cmds.container(self,q=True,asset=nodes)!="")

	#----------------------------------------------------------------------
	def removeContainer(self):
		""""""
		cmds.container(self,e=True,removeContainer=True)

	#----------------------------------------------------------------------
	def remove_All_Descendents_From_Render_Layer(self, layer=None):
		""""""
		if layer == None:
			layer = RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
		else:
			layer = RenderLayer(str(layer))
		if layer.name != "defaultRenderLayer":
			layer.removeMembers(self.allDescendents)

#----------------------------------------------------------------------
def strings_to_Maya_Nodes(strings):
	if isinstance(strings,list):
		return [Maya_Node(item) for item in strings]
	else:
		return []

#----------------------------------------------------------------------
def strings_to_MPLUGS(strings):
	if isinstance(strings,list):
		items = []
		for item in strings:
			plg = MPLUG(item)
			items.append(plg)
		return items
	else:
		return []
