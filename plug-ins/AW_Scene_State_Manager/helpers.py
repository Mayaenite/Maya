#!/usr/bin/env python
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import re
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
		return obj.hasFn(OpenMaya.MFn.kDependencyNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValidMDagNode(obj):
	if _isValidMObject(obj) :
		return obj.hasFn(OpenMaya.MFn.kDagNode)
	else :
		return False
#----------------------------------------------------------------------
def _isValidMNodeOrPlug(obj):
	return _isValidMPlug(obj) or _isValidMNode (obj)
#----------------------------------------------------------------------
def toMObject(nodeName):
	""" Get the API MObject given the name of an existing node """
	result = None
	# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
	obj = OpenMaya.MObject()
	
	# MAKE A SELECTIONLIST STORAGE CONTAINER
	sel = OpenMaya.MSelectionList()
	
	# CHECK IF THE USER INPUT A NAME TO BE USED
	if nodeName == None:
		# GET THE CURRENTLY ACTIVE SELECTIONLIST
		OpenMaya.MGlobal.getActiveSelectionList(sel)
		# ASSINE THE FIRST SELECTED ITEM
		sel.getDependNode( 0, obj )
	else:
		try :
			# ADD IT TO STORAGE CONTAINER
			sel.add( nodeName )
			# ASSINE THE FIRST SELECTED ITEM
			sel.getDependNode( 0, obj )
		except :
			return result
		
	if _isValidMObject(obj) :
		result = obj
	return result
#----------------------------------------------------------------------
def create_Drag_Path(obj):
	# CREATE A DAGPATH
	dagFn   = OpenMaya.MFnDagNode(obj)
	dagPath = OpenMaya.MDagPath()
	dagFn.getPath ( dagPath )
	return dagPath
#----------------------------------------------------------------------
def toMFnDependencyNode(obj):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if not _isValidMObject(obj):
		obj = toMObject(obj)
		
	if not obj:
		return None
	
	# CREATE A DAGPATH
	resFn = OpenMaya.MFnDependencyNode(obj)
	return resFn
#----------------------------------------------------------------------
def toMFnDagNode(obj):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if not _isValidMObject(nodeName):
		obj = toMObject(nodeName)
		
	if not obj:
		return None
	
	# CREATE A DAGPATH
	dagPath = create_Drag_Path(obj)
	resFn   = OpenMaya.MFnDagNode(dagPath)
	return resFn
#----------------------------------------------------------------------
def toMFnTransform(obj):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if not _isValidMObject(nodeName):
		obj = toMObject(nodeName)
		
	if not obj:
		return None
	
	# CREATE A DAGPATH
	dagPath = create_Drag_Path(obj)
	resFn   = OpenMaya.MFnTransform(dagPath)
	return resFn
#----------------------------------------------------------------------
def toMFnMesh(obj):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if not _isValidMObject(nodeName):
		obj = toMObject(nodeName)
		
	if not obj:
		return None
	
	# CREATE A DAGPATH
	dagPath = create_Drag_Path(obj)
	resFn   = OpenMaya.MFnMesh(dagPath)
	return resFn

#----------------------------------------------------------------------
def toMFnSet(obj):
	""" Get an API MDagPAth to the node, given the name of an existing dag node """
	if not _isValidMObject(obj):
		obj = toMObject(obj)
		
	if not obj:
		return None
	
	# CREATE A DAGPATH
	resFn = OpenMaya.MFnSet(obj)
	return resFn
#----------------------------------------------------------------------
def nameToNode( nodeName=None ,asobj=False):
	"""function that returns a node object given a name"""
	# CREATE A MOBJECT
	obj     = toMObject(nodeName)

	# THIS is The Maya Function Set That Will Be Returned
	if asobj:
		return obj
	resFn = None
	
	if obj.hasFn(OpenMaya.MFn.kTransform):
		resFn = toMFnTransform(obj)

	elif obj.hasFn(OpenMaya.MFn.kMesh):
		try:
			resFn = toMFnMesh(obj)
		except:
			resFn = toMFnDependencyNode(obj)

	elif obj.hasFn(OpenMaya.MFn.kDagNode):
		resFn = toMFnDagNode(obj)
		
	elif obj.hasFn(OpenMaya.MFn.kDependencyNode):
		resFn = toMFnDependencyNode(obj)

	return resFn
#----------------------------------------------------------------------
def nameToNodePlug( attrName, node ):
	"""function that finds a plug given a node object and plug name"""
	# CONVERT IT TO A NODE
	obj        = toMObject(node)
	depNodeFn  = toMFnDependencyNode(obj)
	attrObject = depNodeFn.attribute( attrName )
	plug = OpenMaya.MPlug( obj, attrObject )
	return plug
#----------------------------------------------------------------------
def plugElementIter(plug):
	for i in range(plug.numElements()):
		plg = plug.elementByLogicalIndex(i)
		yield plg
		
#----------------------------------------------------------------------
def plugChildrenIter(plug):
	for i in range(plug.numChildren()):
		plg = plug.child(i)
		yield plg
		
#----------------------------------------------------------------------
def ObjectArrayIter(objects):
	for i in range(objects.length()):
		obj = objects[i]
		yield obj
#----------------------------------------------------------------------
def is_Child_In_PlugChildren(child, plug):
	for elem in plugElementIter(plug):
		if elem == child:
			return True
	return False
#----------------------------------------------------------------------
def is_Object_In_Connected_PlugChildren(obj, plug, asDst=True, asSrc=False):
	for elem in plugElementIter(plug):
		objects = get_connected_plug_objects(elem, asDst, asSrc)
		for node in  ObjectArrayIter(objects):
			if obj == node:
				return True
	return False
#----------------------------------------------------------------------
def get_connected_plug_objects(plug, asDst=True, asSrc=False):
	isinstance(plug, OpenMaya.MPlug)
	items = OpenMaya.MPlugArray()
	objects = OpenMaya.MObjectArray()
	plug.connectedTo(items, asDst, asSrc)
	for i in range(items.length()):
		item = items[i]
		isinstance(item, OpenMaya.MPlug)
		objects.append(item.node())
	return objects

#----------------------------------------------------------------------
def get_connected_plugs(plug, asDst=True, asSrc=False):
	isinstance(plug, OpenMaya.MPlug)
	items = OpenMaya.MPlugArray()
	res = []
	plug.connectedTo(items, asDst, asSrc)
	for i in range(items.length()):
		item = items[i]
		res.append(item)
	return res
#----------------------------------------------------------------------
def get_active_selectionList():
	selList = OpenMaya.MSelectionList()
	OpenMaya.MGlobal.getActiveSelectionList(selList)
	return selList
#----------------------------------------------------------------------
def get_active_selectionStrings():
	selList = get_active_selectionList()
	res =  []
	selList.getSelectionStrings(res)
	return res