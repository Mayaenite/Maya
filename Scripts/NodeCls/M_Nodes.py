#!/usr/bin/env python
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import re
import Scripts.AttributeFns.AttributeCreation
#import Scripts.Global_Constants.Singleton
import NodeTypes
import Scripts.Maya_Exceptions as Exceptions
NT = NodeTypes
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
def nameToNode( name=None ,asobj=False):
	"""function that returns a node object given a name"""
	# MAKE A SELECTIONLIST STORAGE CONTAINER
	selectionList = OpenMaya.MSelectionList()
	# CHECK IF THE USER INPUT A NAME TO BE USED
	if name == None:
		# IF NOT GET THE CURRENTLY ACTIVE SELECTIONLIST
		OpenMaya.MGlobal.getActiveSelectionList(selectionList)
	else:
		# IF SO ADD IT TO STORAGE CONTAINER
		selectionList.add( name )

	# CREATE A MOBJECT AND A DAGPATH MEMORY OBJECT VARIBLE
	obj     = OpenMaya.MObject()
	dagnode = OpenMaya.MDagPath()

	# THIS is The Maya Function Set That Will Be Returned
	resFn = None

	# GET THE DEPENDNODE FOR THE FIST INDEX OF THE SELLIST STOARGE
	# AND ASSINE IT TO OUR MOBJECT OBJ
	selectionList.getDependNode(0,obj)

	if asobj:
		return obj

	if obj.hasFn(OpenMaya.MFn.kTransform):
		# IF SO WE WILL NEED TO BE ABLE TO GET THE FULLPATH NAME
		# TO DO THIS WE WILL NEED TO GET THE DAGPATH NODE FROM THE SELECTIONLIST
		selectionList.getDagPath(0,dagnode)
		resFn = OpenMaya.MFnTransform(dagnode)

	elif obj.hasFn(OpenMaya.MFn.kMesh):
		# IF SO WE WILL NEED TO BE ABLE TO GET THE FULLPATH NAME
		# TO DO THIS WE WILL NEED TO GET THE DAGPATH NODE FROM THE SELECTIONLIST
		selectionList.getDagPath(0,dagnode)
		try:
			resFn = OpenMaya.MFnMesh(dagnode)
		except:
			resFn = OpenMaya.MFnDependencyNode(obj)
			print resFn.name()

	elif obj.hasFn(OpenMaya.MFn.kDagNode):
		# IF SO WE WILL NEED TO BE ABLE TO GET THE FULLPATH NAME
		# TO DO THIS WE WILL NEED TO GET THE DAGPATH NODE FROM THE SELECTIONLIST
		selectionList.getDagPath(0,dagnode)
		resFn = OpenMaya.MFnDagNode(dagnode)

	# CHECK IF THE NODE IS NOT PART OF THE NODEGRAPH
	elif obj.hasFn(OpenMaya.MFn.kDependencyNode):
		# IF NOT RETURN THE DEPENDNODE
		resFn = OpenMaya.MFnDependencyNode(obj)

	return resFn
#----------------------------------------------------------------------
def nameToNodePlug( attrName, node , index=-1):
	"""function that finds a plug given a node object and plug name"""
	# CHECK IF THE INPUT NODE IS NOT AND NODE OBJECT BUT THE NAME OF AN OBJECT
	if isinstance(node,(str,unicode)):
		# IF SO CONVERT IT TO A NODE
		node = nameToNode(node,True)
	elif isinstance(node,MNODE):
		# IF SO CONVERT IT TO A NODE
		node = nameToNode(node.name,True)

	depNodeFn = OpenMaya.MFnDependencyNode( node )
	# CHECK IF THE INPUT Attribute NAME Is and Element From A Muli Attrube
	if attrName.endswith("]"):
		# Replace The Brackets Sarounding the index number
		attrName = attrName.replace("[", " ").replace("]", "")
		# Seperate The Attribute name and the index number
		attrName, index = attrName.split(" ", 1)
		# convert the index number into an int
		index = int(index.strip())
	# get the class version of the attribute
	attrObject = depNodeFn.attribute( attrName )
	# Convert it to and MPlug
	plug = OpenMaya.MPlug( node, attrObject )
	if index is not -1:
		# get the plug for the index Element
		plug = plug.elementByLogicalIndex(index)
	return plug

#----------------------------------------------------------------------
def create_Shading_Engine_For_Material(material):
	shading_engine_name = str(material)
	while shading_engine_name.endswith("_"):
		shading_engine_name = shading_engine_name[:-1]
	shading_engine_name += "_SG"
	SG = Shading_Engine(shading_engine_name)
	SG.Assine_To_Material(material)
	return SG
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

########################################################################
class MTypes(object):
	DTS = ['Int32Array', 'doubleArray', 'lattice', 'matrix', 'mesh', 'nurbsCurve', 'nurbsSurface', 'pointArray', 'string', 'stringArray', 'vectorArray']
	ATS = ['bool', 'byte', 'char', 'TdataCompound','compound', 'double', 'double2', 'double3', 'doubleAngle', 'doubleLinear', 'enum', 'float', 'float2', 'float3', 'fltMatrix', 'long', 'long2', 'long3', 'message', 'reflectance', 'short', 'short2', 'short3', 'spectrum', 'time']
	NTS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	STS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	CTS = ['double2', 'double3','float2', 'float3','long2', 'long3','short2', 'short3']


########################################################################
class Named_Object(object):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	def __init__(self,name):
		self._name = name
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
	def __eq__(self, other):
		return unicode(self.name) == unicode(other)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return unicode(self.name) != unicode(other)
	#----------------------------------------------------------------------
	def __get_name(self):
		return unicode(self._name)
	#----------------------------------------------------------------------
	name          = property(fget=__get_name)
########################################################################
class SelectionConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		if not cmds.selectionConnection(name,exists=True):
			name = cmds.selectionConnection(name, **kwargs)
		super(SelectionConnection, self).__init__(name)

	def __lshift__(self, other):
		cmds.selectionConnection(self.name,e=True,select=other)

	def __rshift__(self, other):
		cmds.selectionConnection(self.name,e=True,deselect=other)

	def get_objects(self):
		"""will return all the members of the selection connection (if the connection wraps a set, the set members will be returned)"""
		return cmds.selectionConnection(self.name,q=True,object=True)

	def select_objects(self):
		cmds.select(self.name)

	def clear(self):
		cmds.selectionConnection(self.name,e=True,clear=True)

	def add_connection(self,name):
		cmds.selectionConnection(name,e=True,addTo=self.name)

	def remove_connection(self,name):
		cmds.selectionConnection(self.name,e=True,remove=name)

	def addScript(self,fn):
		cmds.selectionConnection(self.name,e=True,addScript=fn)

	def removeScript(self,fn):
		cmds.selectionConnection(self.name,e=True,removeScript=fn)

	def identify(self):
		return cmds.selectionConnection(self.name,q=True,identify=True)

	def add_objects(self,*objects):
		try:
			for item in objects:
				if isinstance(item,(list,tuple)):
					for obj in item:
						cmds.selectionConnection(self.name,e=True,select=obj)
				else:
					cmds.selectionConnection(self.name,e=True,select=item)
		except:
			cmds.selectionConnection(self.name,e=True,select=objects)

	def remove_objects(self,*objects):
		try:
			for item in objects:
				if isinstance(item,(list,tuple)):
					for obj in item:
						cmds.selectionConnection(self.name,e=True,deselect=obj)
				else:
					cmds.selectionConnection(self.name,e=True,deselect=item)
		except:
			cmds.selectionConnection(self.name,e=True,deselect=objects)

	def connect_to_editor_MainList(self,editor):
		cmds.editor( str(editor), edit=True, mainListConnection=self)
		
	def connect_to_editor_Selection(self,editor):
		cmds.editor( str(editor), edit=True, selectionConnection=self)
		
	def connect_to_editor_Highlight(self,editor):
		cmds.editor( str(editor), edit=True, highlightConnection=self)
		
	def delete(self):
		if cmds.selectionConnection(self._name,exists=True):
			cmds.deleteUI(self._name)
			
	def __delete__(self):
		self.delete()
		super(SelectionConnection,self).__delete__()


########################################################################
class ActiveListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["activeList"]=True
		super(ActiveListConnection, self).__init__(name,**kwargs)

########################################################################
class ModelListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["modelList"]=True
		super(ModelListConnection, self).__init__(name,**kwargs)

########################################################################
class KeyframeListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["keyframeList"]=True
		super(KeyframeListConnection, self).__init__(name,**kwargs)

########################################################################
class WorldListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["worldList"]=True
		super(WorldListConnection, self).__init__(name,**kwargs)

########################################################################
class ObjectListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["objectList"]=True
		super(ObjectListConnection, self).__init__(name,**kwargs)

########################################################################
class ListListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["listList"]=True
		super(ListListConnection, self).__init__(name,**kwargs)

########################################################################
class EditorListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["editorList"]=True
		super(EditorListConnection, self).__init__(name,**kwargs)

########################################################################
class SetListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["setList"]=True
		super(SetListConnection, self).__init__(name,**kwargs)

########################################################################
class CharacterListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["characterList"]=True
		super(CharacterListConnection, self).__init__(name,**kwargs)

########################################################################
class HighlightListConnection(SelectionConnection):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["highlightList"]=True
		super(HighlightListConnection, self).__init__(name,**kwargs)

########################################################################
class MPLUG(object):
	"""
	This Class Is A Base Class That Holds The A Memeory Pointer to a Nodes Attribute
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	def __init__(self,node,att=None):
		if isinstance(node, MPLUG):
			self.obj  = node.obj
			self.node = node.node
		else:
			if isinstance(node, OpenMaya.MPlug):
				self.obj  = node
				node, att = node.name().split(".", 1)
				self.node = MNODE(node)
			elif isinstance(node, (str, unicode)):
				if att == None:
					node, att  = node.split(".", 1)
				self.obj  = nameToNodePlug( att, node )
				self.node = MNODE(node)

	#----------------------------------------------------------------------
	def __str__(self):
		return self.name
	#----------------------------------------------------------------------
	def __repr__(self):
		return self.name
	#----------------------------------------------------------------------
	def getValue(self):
		if self.type in MTypes.STS or self.type == "string":
			return cmds.getAttr(self)
		elif self.type in MTypes.CTS:
			return list(cmds.getAttr(self)[0])
		elif self.type == "message":
			nodes = self.get_Input_Nodes()
			if len(nodes):
				return nodes[0]
			else:
				return None
		return cmds.getAttr(self)
	#----------------------------------------------------------------------
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
	def get_Input_Plugs(self):
		""""""
		res = []
		source = cmds.listConnections( self ,source=True,plugs=True,skipConversionNodes=True)
		if source:
			inputs = [s.split('.') for s in source]
			for s in source:
				n,a = s.split('.')
				plg = MPLUG(n,a)
				res.append(plg)
		return res
	#----------------------------------------------------------------------
	def get_Output_Plugs(self):
		""""""
		res = []
		source = cmds.listConnections( self ,source=False,destination=True,plugs=True,skipConversionNodes=True)
		if source:
			inputs = [s.split('.') for s in source]
			for s in source:
				n,a = s.split('.')
				plg = MPLUG(n,a)
				res.append(plg)
		return res
	#----------------------------------------------------------------------
	def get_Input_Nodes(self):
		""""""
		res = strings_to_MNODES(cmds.listConnections( self ,source=True,plugs=False,skipConversionNodes=True))
		return res
	#----------------------------------------------------------------------
	def get_Output_Nodes(self):
		""""""
		res = strings_to_MNODES(cmds.listConnections( self ,source=False,destination=True,plugs=False,skipConversionNodes=True))
		return res
	#----------------------------------------------------------------------
	def Disconnect_All_Inputs(self):
		""""""
		for plg in self.get_Input_Plugs():
			cmds.disconnectAttr(plg,self)
	#----------------------------------------------------------------------
	def simple_Disconnect(self,plug):
		cmds.disconnectAttr(self, plug)

	#----------------------------------------------------------------------
	def Simple_Connect(self,plg):
		""""""
		if not cmds.isConnected(self,plg):
			cmds.connectAttr(self,plg,force=True)
	#----------------------------------------------------------------------
	@property
	def lock(self):
		cmds.setAttr(self,lock=True)
	#----------------------------------------------------------------------
	@property
	def unlock(self):
		cmds.setAttr(self,lock=False)
	#----------------------------------------------------------------------
	@property
	def name(self):
		return self.node.name+"."+self.partialName
	#----------------------------------------------------------------------
	@property
	def partialName(self):
		return self.obj.partialName()
	#----------------------------------------------------------------------
	@property
	def keyable(self):
		"""Return the keyable status of the attribute """
		return cmds.attributeQuery( self.partialName,node=self.node , keyable=True )
	#----------------------------------------------------------------------
	def make_keyable(self,val):
		"""Return the keyable status of the attribute """
		return cmds.setAttr(self,k=val)
	#----------------------------------------------------------------------
	@property
	def exists(self):
		"""Return true if the attribute exists"""
		return cmds.attributeQuery( self.partialName,node=self.node, exists=True )
	#----------------------------------------------------------------------
	def enable_Render_Layer_Overide(self,layer=None):
		"""Return true if the attribute exists"""
		if layer:
			cmds.editRenderLayerAdjustment( self.name, layer=layer )
		else:
			cmds.editRenderLayerAdjustment( self.name)
	#----------------------------------------------------------------------
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
		return cmds.attributeQuery( self.partialName,node=self.node,  connectable=True )
	#----------------------------------------------------------------------
	@property
	def message(self):
		"""Return true if the attribute is a message attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  message=True )
	#----------------------------------------------------------------------
	@property
	def enum(self):
		"""Return true if the attribute is a enum attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  enum=True )
	#----------------------------------------------------------------------
	@property
	def hidden(self):
		"""Return the hidden status of the attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  hidden=True )
	#----------------------------------------------------------------------
	@property
	def indexMatters(self):
		"""Return the indexMatters status of the attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  indexMatters=True )
	#----------------------------------------------------------------------
	@property
	def readable(self):
		"""Return the readable status of the attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  readable=True )
	#----------------------------------------------------------------------
	@property
	def storable(self):
		"""Return true if the attribute is storable"""
		return cmds.attributeQuery( self.partialName,node=self.node,  storable=True )
	#----------------------------------------------------------------------
	@property
	def writable(self):
		"""Return true if the attribute is a message attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  writable=True )
	#----------------------------------------------------------------------
	@property
	def multi(self):
		"""Return true if the attribute is a multi-attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  multi=True )
	#----------------------------------------------------------------------
	@property
	def isArray(self):
		""""""
		return self.obj.isArray()
	#----------------------------------------------------------------------
	@property
	def usesMultiBuilder(self):
		"""Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data"""
		return cmds.attributeQuery( self.partialName,node=self.node,  usesMultiBuilder=True )
	#----------------------------------------------------------------------
	@property
	def minimum(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  minimum=True )
	#----------------------------------------------------------------------
	@property
	def getSetAttrCmds(self):
		data = []
		self.obj.getSetAttrCmds(data)
		return data
	#----------------------------------------------------------------------
	def getElementByIndex(self, index):
		try:
			res = self.obj.elementByLogicalIndex(index)
			res = MPLUG(res)
		except:
			res = None
		return res
	#----------------------------------------------------------------------
	@property
	def has_source_connections(self):
		return cmds.listConnections( self ,source=True,plugs=True,skipConversionNodes=True) != None
	#----------------------------------------------------------------------
	@property
	def has_destination_connections(self):
		return cmds.listConnections( self ,source=False,destination=True,plugs=True,skipConversionNodes=True) != None
	#----------------------------------------------------------------------
	@property
	def maximum(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  maximum=True )
	#----------------------------------------------------------------------
	@property
	def range(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  range=True )
	#----------------------------------------------------------------------
	@property
	def usedAsColor(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  usedAsColor=True )
	#----------------------------------------------------------------------
	@property
	def softRange(self):
		"""Return true if the attribute is a message attribute"""
		return cmds.attributeQuery( self.partialName,node=self.node,  softRange=True )
	#----------------------------------------------------------------------
	@property
	def softMin(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  softMin=True )
	#----------------------------------------------------------------------
	@property
	def softMax(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  softMax=True )
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  numberOfChildren=True )
	#----------------------------------------------------------------------
	@property
	def numElements(self):
		if self.multi:
			return self.obj.numElements()
		else:
			return -1
	#----------------------------------------------------------------------
	@property
	def numConnectedElements(self):
		if self.multi:
			return self.obj.numConnectedElements()
		else:
			return -1

	#----------------------------------------------------------------------
	@property
	def listSiblings(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  listSiblings=True )
	#----------------------------------------------------------------------
	@property
	def listChildren(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  listChildren=True )
	#----------------------------------------------------------------------
	@property
	def listParent(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  listParent=True )
	#----------------------------------------------------------------------
	@property
	def listEnum(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  listEnum=True )
	#----------------------------------------------------------------------
	@property
	def listEnumNames(self):
		if self.listEnum == None:
			return []
		return self.listEnum[0].split(":")
	#----------------------------------------------------------------------
	@property
	def listDefault(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  listDefault=True )
	#----------------------------------------------------------------------
	@property
	def minExists(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  minExists=True )
	#----------------------------------------------------------------------
	@property
	def maxExists(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  maxExists=True )
	#----------------------------------------------------------------------
	@property
	def rangeExists(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  rangeExists=True )
	#----------------------------------------------------------------------
	@property
	def softMinExists(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  softMinExists=True )
	#----------------------------------------------------------------------
	@property
	def softMaxExists(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  softMaxExists=True )
	#----------------------------------------------------------------------
	@property
	def softRangeExists(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  softRangeExists=True )
	#----------------------------------------------------------------------
	@property
	def niceName(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  niceName=True )
	#----------------------------------------------------------------------
	@property
	def longName(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  longName=True )
	#----------------------------------------------------------------------
	@property
	def shortName(self):
		return cmds.attributeQuery( self.partialName,node=self.node,  shortName=True )
	#----------------------------------------------------------------------
	@property
	def type(self):
		return cmds.getAttr(self.node.name+"."+self.partialName,typ=True )
	#----------------------------------------------------------------------
	@property
	def multiIndices(self):
		cmds.getAttr(layer.plug_access.displayLayerId, multiIndices=True)
		
	def iter_element_plugs(self):
		for index in self.multiIndices:
			plg = self.getElementByIndex(index)
			yield plg
	#----------------------------------------------------------------------
	value = property(getValue,setValue)

########################################################################
class Enum_MPLUG(MPLUG):
	"""
	This Class Is A Base Class That Holds The A Memeory Pointer to a Nodes Attribute
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	def set_Enums(self,enumNames):
		cmds.addAttr(self.name, edit=True,  enumName=":".join(enumNames)+":")
		
		
########################################################################
class Attribute_Plug_Access(object):
	#----------------------------------------------------------------------
	def __init__(self,mnode):
		""""""
		#cmds.listAttr(mnode)#multi=False,scalar=False,hasData=True,connectable=True,string=(name+"*")
		for item in cmds.listAttr(mnode):
			if not hasattr(self,item):
				setattr(self, item, MPLUG(mnode.name, att=item))
		self._obj = mnode

	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		if not name == "_obj":
			att_list = cmds.listAttr(self._obj,multi=False,scalar=False,hasData=True,connectable=True)#string=(name+"*")
			if not att_list == None:
				if name in att_list:
					return MPLUG(self._obj.name, att=name)
		return object.__getattribute__(self,name)

########################################################################
class Attribute_Creator(object):
	#----------------------------------------------------------------------
	def Attribute_Exists(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Attribute_Exists(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def Delete_Attribute(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Delete_Attribute(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Char(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Char(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Char_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Multi_Char(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Byte(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Byte(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Byte_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Byte_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Bool(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Bool(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Bool_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Bool_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Short(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Short(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Short_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Short_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Short2(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Short2(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Short3(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_At_Short3(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Long(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Long(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Long_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Long_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Float(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Float(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Float2(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Float2(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Float3(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Float3(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Double_Angle(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Double_Angle(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Double_Linear(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Double_Linear(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Message(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Message(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Message_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Message_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_String(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_String(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_String_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_String_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Float_Matrix(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Float_Matrix(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Int32_Array(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Int32_Array(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_Int32_Array_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_Int32_Array_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_String_Array(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_String_Array(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def create_String_Array_M(self,attribute_long_name):
		Scripts.AttributeFns.AttributeCreation.Add_String_Array_M(self.name, attribute_long_name)
		return MPLUG(self.name, attribute_long_name)
	#----------------------------------------------------------------------
	def set_Double_Array(self,attribute_long_name, values):
		Scripts.AttributeFns.AttributeCreation.Set_Double_Array(self.name, attribute_long_name, values)
	#----------------------------------------------------------------------
	def set_Double_Array_M(self,attribute_long_name, values, Index):
		Scripts.AttributeFns.AttributeCreation.Set_Double_Array_M(self.name, attribute_long_name, values, Index)
	#----------------------------------------------------------------------
	def set_Float_Matrix(self,attribute_long_name, values):
		Scripts.AttributeFns.AttributeCreation.Set_Float_Matrix(self.name, attribute_long_name, values)
	#----------------------------------------------------------------------
	def set_Float_Matrix_M(self,attribute_long_name, values, index):
		Scripts.AttributeFns.AttributeCreation.Set_Float_Matrix_M(self.name, attribute_long_name, values, index)
	#----------------------------------------------------------------------
	def set_Int32_Array(self,attribute_long_name, values):
		Scripts.AttributeFns.AttributeCreation.Set_Int32_Array(self.name, attribute_long_name, values)
	#----------------------------------------------------------------------
	def set_Int32_Array_M(self,attribute_long_name, values, index):
		Scripts.AttributeFns.AttributeCreation.Set_Int32_Array_M(self.name, attribute_long_name, values, index)
	#----------------------------------------------------------------------
	def set_String_Array(self,attribute_long_name, values):
		Scripts.AttributeFns.AttributeCreation.Set_String_Array(self.name, attribute_long_name, values)
	#----------------------------------------------------------------------
	def set_String_Array_M(self,attribute_long_name, values, index):
		Scripts.AttributeFns.AttributeCreation.Set_String_Array_M(self.name, attribute_long_name, values, index)
	#----------------------------------------------------------------------
	def set_String_M_Item(self,attribute_long_name, values):
		Scripts.AttributeFns.AttributeCreation.Set_String_M_Item(self.name, attribute_long_name, values)

########################################################################
class MNODE(Attribute_Creator):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	def __new__(cls,*args,**kwargs):
		if len(args):
			nodeName = args[0]
		else:
			nodeName = kwargs.get("nodeName",kwargs.get("name",None))
		if isinstance(nodeName,MNODE):
			return nodeName
		obj = object.__new__(cls)
		return obj
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		if len(args):
			nodeName = args[0]
		else:
			nodeName = kwargs.get("nodeName",kwargs.get("name",None))
		self.obj = nameToNode(nodeName)

	#----------------------------------------------------------------------
	def __str__(self):
		return self.name
	#----------------------------------------------------------------------
	def __repr__(self):
		return self.name

	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		return unicode(self.name) == unicode(other)
	def __ne__(self, other):
		return unicode(self.name) != unicode(other)
	#----------------------------------------------------------------------
	def __get_name(self):
		if hasattr(self.obj,"fullPathName"):
			return self.obj.fullPathName()
		else:
			return self.obj.name()
	#----------------------------------------------------------------------
	def __set_name(self,value):
		cmds.rename(self.name,str(value))
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
	def short_name(self):
		if hasattr(self.obj,"partialPathName"):
			return self.obj.partialPathName()
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
	#----------------------------------------------------------------------
	def get_parent(self):
		""""""
		res = cmds.listRelatives(self.name, parent=True, path=True)
		if not res:
			return False
		return MNODE(res[0])
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
		return strings_to_MNODES(res)

	#----------------------------------------------------------------------
	def connected_Shader(self):
		""""""
		shader = cmds.listConnections(self,d=True,type='shadingEngine')
		if not shader==None:
			shader=MNODE(shader[0])
			return shader
		return None
	#----------------------------------------------------------------------
	@property
	def children(self):
		""""""
		return strings_to_MNODES(cmds.listRelatives(self.name, children=True, path=True))
	#----------------------------------------------------------------------
	@property
	def has_child_transforms(self):
		""""""
		return (cmds.listRelatives(self.name, children=True, path=True,type="transform") != None)
	#----------------------------------------------------------------------
	@property
	def child_transforms(self):
		""""""
		return strings_to_MNODES(cmds.ls(cmds.listRelatives(self.name, children=True, path=True),type='transform'))
	#----------------------------------------------------------------------
	@property
	def all_transform_Descendents(self):
		""""""
		return strings_to_MNODES(cmds.listRelatives(self.name, allDescendents=True, path=True, type='transform'))
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
		return strings_to_MNODES(cmds.listRelatives(self,allDescendents=True,fullPath=True))
	#----------------------------------------------------------------------
	def isType(self,type):
		"true if the object is exactly of the specified type. False otherwise"
		return cmds.objectType(self,isType=type)
	#----------------------------------------------------------------------
	def listSets(self,allSets=False,extendToShape=True):
		return cmds.listSets(allSets=allSets, extendToShape=extendToShape, object=self)
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
		layer = cmds.listConnections(self,type="displayLayer",destination=True,source=True)
		if layer == None:
			return 'defaultLayer'
		return layer[0]
	#----------------------------------------------------------------------
	def attributeExists(self,attr):
		return cmds.attributeQuery( attr,node=self, exists=True )
	#----------------------------------------------------------------------
	def Add_Simple_Attribute(self,longName,mType,shortName=False,multi=False,defaultValue=False,parent=False,numberOfChildren=False,usedAsFilename=False,hidden=False,writable=True,readable=True,storable=True,keyable=True,enumName=False):
		kwargs = dict(longName=longName)
		if shortName:
			kwargs["shortName"]=shortName
		if mType in MTypes.DTS:
			kwargs["dataType"]=mType
		elif mType in MTypes.ATS:
			kwargs["attributeType"]=mType

		if not cmds.attributeQuery(longName,node=self, exists=True ):
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
		
	#----------------------------------------------------------------------
	def toggle_nodeLock(self):
		""""""
		checks = []
		checks.extend(cmds.lockNode(self, query=True,lock=True))
		checks.extend(cmds.lockNode(self, query=True,lockUnpublished=True))
		checks.extend(cmds.lockNode(self, query=True,lockName=True))
		if any(checks):
			cmds.lockNode(self,lock=False,lockName=False,lockUnpublished=False)
		else:
			cmds.lockNode(self,lock=True,lockName=True,lockUnpublished=True)
	@property
	def plug_access(self):
		if not hasattr(self,"_plug_attriubte_access"):
			self._plug_attriubte_access = Attribute_Plug_Access(self)
		return self._plug_attriubte_access
	#----------------------------------------------------------------------
	@property
	def isFromReferencedFile(self):
		""""""
		return self.obj.isFromReferencedFile()
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
	name          = property(fget=__get_name, fset=__set_name)
	transfromType = property(ShapeType)
	try:
		objectType    = property(cmds.objectType)
		objectExists  = property(cmds.objExists)
	except AttributeError:
		pass


########################################################################
class RenderLayer(MNODE):
	#----------------------------------------------------------------------
	def __init__(self,name,makeCurrent=False,empty=True,noRecurse=True):
		kwargs = dict(name=name,makeCurrent=makeCurrent,empty=empty,noRecurse=noRecurse)

		if not cmds.objExists(name):
			name = cmds.createRenderLayer(**kwargs)

		super(RenderLayer,self).__init__(name)


	#----------------------------------------------------------------------
	def addMembers(self,items):
		if not items == None:
			if len(items):
				cmds.editRenderLayerMembers(self,items, noRecurse=True)
	#----------------------------------------------------------------------
	def include_special(self):
		self.addMembers(cmds.listRelatives(cmds.listRelatives(allDescendents=True,type=["mesh",'VRayLightRectShape',"light"],path=True),parent=True,type="transform",path=True))

	#----------------------------------------------------------------------
	def removeMembers(self,items):
		if len(items):
			cmds.editRenderLayerMembers( self, items, remove=True)
	#----------------------------------------------------------------------
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
	def enable_Attribute_overRide(self,Plugs):
		cmds.editRenderLayerAdjustment(Plugs,layer=self.name)

	#----------------------------------------------------------------------
	@property
	def members(self):
		items = cmds.editRenderLayerMembers( self,fullNames=True, query=True )
		if items == None:
			return []
		else:
			return [MNODE(m) for m in items]

	#----------------------------------------------------------------------
	def select_members(self):
		items = self.members
		if len(items):
			cmds.select(self.members,replace=True)
		else:
			cmds.select(clear=True)

	#----------------------------------------------------------------------
	def select_set(self):
		cmds.select(self,replace=True)

########################################################################
class DisplayLayer(MNODE):
	Normal,Reference,Template = range(3)
	#----------------------------------------------------------------------
	def __init__(self,name,makeCurrent=False,empty=True,noRecurse=True):
		kwargs = dict(name=name,makeCurrent=makeCurrent,empty=empty,noRecurse=noRecurse)
		if not cmds.objExists(name):
			name = cmds.createDisplayLayer(**kwargs)

		super(DisplayLayer,self).__init__(name)
		self.drawinfo      = self.Make_Plug("drawInfo")
		self.visibility    = self.Make_Plug("visibility")
		self.displayType   = self.Make_Plug("displayType")
		self.color         = self.Make_Plug("color")
		self.playback      = self.Make_Plug("playback")
		self.shading       = self.Make_Plug("shading")
		self.texturing     = self.Make_Plug("texturing")
		self.levelOfDetail = self.Make_Plug("levelOfDetail")
		self.displayOrder  = self.Make_Plug("displayOrder")

	#----------------------------------------------------------------------	
	def addMembers(self,*items, **kwargs):
		noRecurse = kwargs.get("noRecurse", True)
		items = flatten(items)
		items = [item for item in items if cmds.objExists(item)]
		if items:
			cmds.editDisplayLayerMembers(self, items, noRecurse=noRecurse)
	#----------------------------------------------------------------------
	def removeMembers(self,*items, **kwargs):
		noRecurse = kwargs.get("noRecurse", False)
		items = flatten(items)
		items = [item for item in items if cmds.objExists(item) and item in self.member_names]
		if items:
			cmds.editDisplayLayerMembers("defaultLayer", items,noRecurse=noRecurse)
			
	#----------------------------------------------------------------------
	def include_Selected(self):
		items = cmds.ls(sl=True)
		if items == None:
			items = []
		self.addMembers(items)
		
	#----------------------------------------------------------------------
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
			return [MNODE(m) for m in items]

	#----------------------------------------------------------------------
	@property
	def member_names(self):
		return [unicode(item.name) for item in self.members]

	#----------------------------------------------------------------------
	def select_members(self, replace=True, add=False, remove=False):
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
	def select_set(self):
		cmds.select(self,replace=True)

	#----------------------------------------------------------------------
	def show(self):
		self.visibility.setValue(1)

	#----------------------------------------------------------------------
	def hide(self):
		self.visibility.setValue(0)
########################################################################
class SelectionSet(MNODE):
	#sets( selectionList , [addElement=name], [afterFilters=boolean], [color=int], [copy=name], [edges=boolean], [editPoints=boolean], [empty=boolean], [facets=boolean], [flatten=name], [forceElement=name], [include=name], [intersection=name], [isIntersecting=name], [isMember=name], [layer=boolean], [name=string], [noSurfaceShader=boolean], [noWarnings=boolean], [nodesOnly=boolean], [remove=name], [renderable=boolean], [size=boolean], [split=name], [subtract=name], [text=string], [union=name], [vertices=boolean])
	def __init__(self,name,empty=False,copy=None,text="",renderable=False):
		kwargs = dict(name=name,empty=empty,text=text)
		if copy:
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
	def delete(self):
		self.remove(self.members)
		super(SelectionSet,self).delete()
	#----------------------------------------------------------------------
	def clear(self):
		cmds.sets(clear=self)
	#----------------------------------------------------------------------
	def select_set(self):
		cmds.select(self,ne=True,replace=True)
	#----------------------------------------------------------------------
	def select_members(self, replace=True, add=False, remove=False):
		if len(self.members):
			if add:
				cmds.select(self.members,add=True)
			elif remove:
				cmds.select(self.members,remove=True)
			else:
				cmds.select(self.members,replace=True)
		else:
			cmds.select(clear=True)
	#----------------------------------------------------------------------
	@property
	def size(self):
		cmds.sets(size=True,q=True)
	#----------------------------------------------------------------------
	def remove(self,*items):
		items = flatten(items)
		if len(items):
			cmds.sets( items, remove=self)
	#----------------------------------------------------------------------
	def remove_selected(self):
		cmds.sets(cmds.ls(sl=True), remove=self)
	#----------------------------------------------------------------------
	def include(self,*items):
		#self.__rshift__(items)
		items = flatten(items)
		if len(items):
			cmds.sets( items, include=self)
	#----------------------------------------------------------------------
	def include_Selected(self):
		items = cmds.ls(sl=True, type="transform")
		if items == None:
			items = []
		self.include(items)
	#----------------------------------------------------------------------
	def include_special(self,*items):
		items = flatten(items)
		if len(items):
			items_check =  cmds.listRelatives(cmds.listRelatives(items,allDescendents=True,type=["mesh",'VRayLightRectShape',"light"],path=True),parent=True,type="transform",path=True)
			if not items_check ==  None:
				self.include(items_check)
	#----------------------------------------------------------------------
	def addElement(self,*items):
		#self.__rshift__(items)
		items = flatten(items)
		if len(items):
			cmds.sets( items, addElement=self)
	#----------------------------------------------------------------------
	def intersecting_members(self,selectionSet):
		items = cmds.sets(selectionSet,intersection=self)
		return [MNODE(obj) for obj in items]
	#----------------------------------------------------------------------
	@property
	def memberNames(self):
		return [unicode(m) for m in self.members]
	#----------------------------------------------------------------------
	@property
	def members(self):
		try:
			return [MNODE(m) for m in cmds.listConnections(self._dagSetMembers_plug.name,type="transform",destination=False,source=True)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	@property
	def members_and_all_transform_descendents(self):
		res = []
		try:
			for member in self.members:
				res.append(member)
				res.extend(member.all_transform_Descendent)
			return res
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
	@property
	def children(self):
		try:
			return [SelectionSet(m) for m in cmds.listConnections(self._dnSetMembers_plug.name,type="objectSet",destination=True,source=True)]
		except TypeError:
			return []
	#----------------------------------------------------------------------
	def isSubSet(self,item):
		return str(item) in [str(m) for m in self.parents]
	#----------------------------------------------------------------------
	def hasSubSet(self,item):
		return str(item) in [str(m) for m in self.children]
	#----------------------------------------------------------------------
	def __contains__(self,item):
		return str(item) in self.memberNames
	#----------------------------------------------------------------------
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
class ShadingNode(MNODE):
	def __init__(self, name, shaderType="surfaceShader"):
		if not cmds.objExists(name):
			name = cmds.shadingNode(shaderType,asShader=True,name=name)
		super(ShadingNode,self).__init__(name)
		self.outColor = self.Make_Plug("outColor")
	
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
			cmds.sets(items,forceElement=self)
	#----------------------------------------------------------------------
	@property
	def memberNames(self):
		return [unicode(m) for m in self.members]
	#----------------------------------------------------------------------
	@property
	def members(self):
		try:
			return [MNODE(m) for m in cmds.listConnections(self._dagSetMembers_plug.name,shapes=True,destination=False,source=True) if not cmds.objectType(m) in ["renderLayer","displayLayer"]]
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
		nodes = self.surfaceShader.get_Input_Nodes()
		if len(nodes):
			return nodes[0]
		else:
			return None

########################################################################
class VRayObjectProperties(SelectionSet):
	def __init__(self,name):
		if not cmds.objExists(name):
			name = cmds.createNode("VRayObjectProperties",name=name)
		self._active_Overide_state = None

		super(VRayObjectProperties,self).__init__(name)

		self._giVisibility_plug           = self.Make_Plug('giVisibility')
		self._primaryVisibility_plug      = self.Make_Plug('primaryVisibility')
		self._reflectionVisibility_plug   = self.Make_Plug('reflectionVisibility')
		self._refractionVisibility_plug   = self.Make_Plug('refractionVisibility')
		self._shadowVisibility_plug       = self.Make_Plug('shadowVisibility')
		self._matteSurface_plug           = self.Make_Plug('matteSurface')
		self._generateRenderElements_plug = self.Make_Plug('generateRenderElements')
		self._shadows_plug                = self.Make_Plug('shadows')
		self._affectAlpha_plug            = self.Make_Plug('affectAlpha')
		self._generateGI_plug             = self.Make_Plug('generateGI')
		self._receiveGI_plug              = self.Make_Plug('receiveGI')
		self._generateCaustics_plug       = self.Make_Plug('generateCaustics')
		self._receiveCaustics_plug        = self.Make_Plug('receiveCaustics')
		self._ignore_plug                 = self.Make_Plug('ignore')
		self._overrideMBSamples_plug      = self.Make_Plug('overrideMBSamples')
		self._objectIDEnabled_plug        = self.Make_Plug('objectIDEnabled')
		self._alphaContribution_plug      = self.Make_Plug('alphaContribution')
		self._reflectionAmount_plug       = self.Make_Plug('reflectionAmount')
		self._refractionAmount_plug       = self.Make_Plug('refractionAmount')

########################################################################
class VRayRenderState(VRayObjectProperties):
	script_Job_pattern = re.compile("(?P<jobid>([1-9]+)): (?P<event>([a-zA-Z]+))=\['(?P<node>([a-zA-Z]['a-zA-Z1-9_]+)\.([a-zA-Z][a-zA-Z1-9_]+))'")

	UnAssined,Beauty,Matte,Invisable = range(4)
	def __init__(self,name):
		super(VRayRenderState,self).__init__(name)
		#self.vrayRenderPassState        = self.Add_Enum_Attribute('vrayRenderPassState', ["UnAssined","Beauty","Matte","Invisable"])
		#self.old_state                  = self.Add_Enum_Attribute('old_state', ["UnAssined","Beauty","Matte","Invisable"])
		#self.display_layer_link         = self.Add_Simple_Attribute('display_layer_link',"message")
		#self.renderState_script_job_id  = self.Add_Simple_Attribute('renderState_script_job_id',"int")


		#self.vrayRenderPassState.make_keyable(True)
		#self.apply_vray_pass_state_overide_to_all_layers()

	def Add_Members_To_Render_Layer(self,layer=None):
		if layer == None:
			layer = RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
		else:
			layer = RenderLayer(layer)
		layer.addMembers(self.members)

	def Remove_Members_From_Render_Layer(self,layer=None):
		if layer == None:
			layer = RenderLayer(cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
		else:
			layer = RenderLayer(layer)
		layer.removeMembers(self.members)

	def clear_Scene_State_Overides(self,layer=None):
		self._matteSurface_plug.disable_Render_Layer_Overide(layer=layer)
		self._affectAlpha_plug.disable_Render_Layer_Overide(layer=layer)
		self._alphaContribution_plug.disable_Render_Layer_Overide(layer=layer)
		self._primaryVisibility_plug.disable_Render_Layer_Overide(layer=layer)
		self._reflectionAmount_plug.disable_Render_Layer_Overide(layer=layer)
		self._refractionAmount_plug.disable_Render_Layer_Overide(layer=layer)
		
	def apply_Scene_State_Overides(self,layer=None):
		self._matteSurface_plug.enable_Render_Layer_Overide(layer=layer)
		self._affectAlpha_plug.enable_Render_Layer_Overide(layer=layer)
		self._alphaContribution_plug.enable_Render_Layer_Overide(layer=layer)
		self._primaryVisibility_plug.enable_Render_Layer_Overide(layer=layer)
		self._reflectionAmount_plug.enable_Render_Layer_Overide(layer=layer)
		self._refractionAmount_plug.enable_Render_Layer_Overide(layer=layer)
		
	def set_Default_Override_Values(self,layer=None):
		self.apply_Scene_State_Overides()
		self._matteSurface_plug.value      = 0
		self._affectAlpha_plug.value       = 0
		self._alphaContribution_plug.value = 1.0
		self._primaryVisibility_plug.value = 1
		self._reflectionAmount_plug.value   = 0.0
		self._refractionAmount_plug.value   = 0.0
		
	def set_Matte_Override_Values(self,layer=None):
		self.set_Default_Override_Values(layer)
		
		self._matteSurface_plug.value       = 1
		self._affectAlpha_plug.value        = 1
		self._alphaContribution_plug.value  = -1.0
		self._reflectionAmount_plug.value   = 0.0
		self._refractionAmount_plug.value   = 0.0
		
	def set_Invisible_Override_Values(self,layer=None):
		self.set_Default_Override_Values(layer)
		
		self._primaryVisibility_plug.value = 0
		
	def apply_Matte_Layer_Override(self,layer=None):
		self.set_Default_Override_Values(layer)
		self.set_Matte_Override_Values(layer)

	def apply_Invisible_Layer_Override(self,layer=None):
		self.set_Default_Override_Values(layer)
		self.set_Invisible_Override_Values(layer)

	def apply_Beauty_Layer_Override(self,layer=None):
		self.set_Default_Override_Values(layer)

	def state_switch_action(self,layer=None):
		stat = self.vrayRenderPassState.value
		old_stat = self.old_state.value
		if not old_stat == stat:
			try:
				if stat == self.UnAssined:
					self.Remove_Members_From_Render_Layer(layer)
				if stat == self.Beauty:
					self.apply_Beauty_Layer_Override(layer)
				if stat == self.Matte:
					self.apply_Matte_Layer_Override(layer)
				if stat == self.Invisable:
					self.apply_Invisible_Layer_Override(layer)
			except RuntimeError:
				pass
			self.old_state.value = stat
########################################################################
class Container(MNODE):
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
		return strings_to_MNODES(cmds.container(self,query=True,nodeList=True))
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
		
########################################################################
class SCRIPT_TYPE:
	Demand                = 0
	OpenClose             = 1
	GUI_OpenClose         = 2
	UI_Configuration      = 3
	Software_Render       = 4
	Software_Frame_Render = 5
	Scene_Configuration   = 6
	Time_Changed          = 7
	
########################################################################
class SOURCE_TYPE:
	mel    = 'mel'
	python = "python"
	
########################################################################
class Script_Node(MNODE):
	source_types = SOURCE_TYPE
	script_types = SCRIPT_TYPE
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
class AnimCurve(MNODE):
	#----------------------------------------------------------------------
	def __init__(self,name):
		if not cmds.objExists(name):
			raise ValueError("The Anim Curve Name % Does Not Exist" % name)	
		super(AnimCurve,self).__init__(name)
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
	def connected_output_attribute_plugs(self):
		return self.Make_Plug("output").get_Input_Plugs()
	#----------------------------------------------------------------------
	@property
	def connected_input_attribute_plugs(self):
		return self.Make_Plug("output").get_Input_Plugs()
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
class Display_Layer_Manager(MNODE):
	#__metaclass__ = Scripts.Global_Constants.Singleton.Singleton
	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		super(Display_Layer_Manager,self).__init__("layerManager")
		self.message             = self.Make_Plug("message")
		self.currentDisplayLayer = self.Make_Plug("currentDisplayLayer")
		self.displayLayerId      = self.Make_Plug("displayLayerId")
		
	@property
	def current_layer(self):
		return DisplayLayer(cmds.editDisplayLayerGlobals(query=True,currentDisplayLayer=True))
	
	
########################################################################
class Render_Layer_Manager(MNODE):
	#__metaclass__ = Scripts.Global_Constants.Singleton.Singleton

	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		super(Render_Layer_Manager,self).__init__("renderLayerManager")
		self.message = self.plug_access.message
		self.isHistoricallyInteresting
		self.nodeState
		self.binMembership
		
_wraper_classes = dict()
_wraper_classes[NT.displayLayer]=DisplayLayer
_wraper_classes[NT.renderLayer]=RenderLayer
_wraper_classes[NT.objectSet]=SelectionSet
_wraper_classes[NT.VRAY.VRayObjectProperties]=VRayRenderState
_wraper_classes[NT.script]=Script_Node
_wraper_classes[NT.blinn]=ShadingNode
_wraper_classes[NT.lambert]=ShadingNode
_wraper_classes[NT.phong]=ShadingNode

#----------------------------------------------------------------------
def To_MNode(name=None):
	if name is None:
		selection  = cmds.ls(sl=True)
		if not len(selection):
			raise Scripts.Exceptions.No_Input_Nothing_Selected_Error(To_MNode)
		name = selection[0]
	if not cmds.objExists(name):
		raise Scripts.Exceptions.Object_Does_Not_Exist_Error(name)
	typ = cmds.objectType(name)
	res = _wraper_classes.get(typ,MNODE)(name)
	isinstance(res, MNODE)
	isinstance(res, SelectionSet)
	isinstance(res, DisplayLayer)
	isinstance(res, RenderLayer)
	isinstance(res, VRayRenderState)
	return res

#----------------------------------------------------------------------
def strings_to_MNODES(strings):
	if isinstance(strings,list):
		return [MNODE(item) for item in strings]
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
