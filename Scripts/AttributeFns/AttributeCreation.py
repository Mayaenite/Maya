import maya.cmds as cmds
#----------------------------------------------------------------------
def flatten(x):
	result = []
	for el in x:
		if hasattr(el, "__iter__") and not isinstance(el, str):
			result.extend(flatten(el))
		else:
			result.append(el)
	return result

#--------------------------------------------------------------------------------------------------------------------------------------
# listAttr( [objects] array=boolean     , caching=boolean       , category=string    , changedSinceFileOpen=boolean, leaf=boolean
#                     channelBox=boolean, connectable=boolean   , extension=boolean  , fromPlugin=boolean          , readOnly=boolean
#                     hasData=boolean   , hasNullData=boolean   , inUse=boolean      , keyable=boolean             , read=boolean
#                     locked=boolean    , multi=boolean         , output=boolean     , ramp=boolean                , string=string
#                     scalar=boolean    , scalarAndArray=boolean, settable=boolean   , shortNames=boolean          , write=boolean
#                     unlocked=boolean  , usedAsFilename=boolean, userDefined=boolean, visible=boolean    )
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
# addAttr( 
#        attributeType=string    , cachedInternally=boolean, exists=boolean
#        category=string         , dataType=string         , defaultValue=float      , enumName=string
#        fromPlugin=boolean      , hasMaxValue=boolean     , hasMinValue=boolean     , hasSoftMaxValue=boolean
#        writable=boolean        , hasSoftMinValue=boolean , hidden=boolean          , indexMatters=boolean
#        internalSet=boolean     , keyable=boolean         , usedAsFilename=boolean  , shortName=string
#        longName=string         , maxValue=float          , minValue=float          , multi=boolean          
#        niceName=string         , numberOfChildren=uint   , parent=string           , readable=boolean
#        softMaxValue=float      , softMinValue=float      , storable=boolean        , usedAsColor=boolean,)
#-------------------------------------------------------------------------------------------------------------------------------------
# longName          : string  : create,query               :  Sets the long name of the attribute.
# shortName         : string  : create,query               :  Sets the short name of the attribute.
# niceName          : string  : create,query,edit          :  Sets the nice name of the attribute for display in the UI
# attributeType     : string  : create,query               :  Specifies the attribute type
# dataType          : string  : create,query,multiuse      :  Specifies the data type
# defaultValue      : float   : create,query,edit          :  Specifies the default value for the attribute
# multi             : boolean : create,query               :  Makes the new attribute a multi-attribute.
# indexMatters      : boolean : create,query               :  Sets whether an index must be used when connecting to this multi-attribute
# minValue          : float   : create,query,edit          :  Specifies the minimum value for the attribute	mesh
# hasMinValue       : boolean : create,query,edit          :  Flag indicating whether an attribute has a minimum value
# maxValue          : float   : create,query,edit          :  Specifies the maximum value for the attribute	nurbsSurface
# hasMaxValue       : boolean : create,query,edit          :  Flag indicating whether an attribute has a maximum value
# cachedInternally  : boolean : create,query               :  Whether or not attribute data is cached internally in the node
# internalSet       : boolean : create,query               :  Whether or not the internal cached value is set when this attribute value is changed
# parent            : string  : create,query               :  Attribute that is to be the new attribute's parent.
# numberOfChildren  : uint    : create,query               :  How many children will the new attribute have?
# usedAsColor       : boolean : create,query               :  Is the attribute to be used as a color definition
# usedAsFilename    : boolean : create,query               :  Is the attribute to be treated as a filename definition?
# hidden            : boolean : create,query               :  Will this attribute be hidden from the UI?
# readable          : boolean : create,query               :  Can outgoing connections be made from this attribute?
# writable          : boolean : create,query               :  Can incoming connections be made to this attribute?
# storable          : boolean : create,query               :  Can the attribute be stored out to a file?
# keyable           : boolean : create,query               :  Is the attribute keyable by default?
# fromPlugin        : boolean : create,query               :  Was the attribute originally created by a plugin
# softMinValue      : float   : create,query,edit          :  Soft minimum
# hasSoftMinValue   : boolean : create,query               :  Flag indicating whether a numeric attribute has a soft minimum
# softMaxValue      : float   : create,query,edit          :  Soft maximum
# hasSoftMaxValue   : boolean : create,query               :  Flag indicating whether a numeric attribute has a soft maximum.
# category          : string  : create,query,edit,multiuse :  An attribute category is a string associated with the attribute to identify it
# enumName          : string  : create,query,edit          :  Flag used to specify the ui names corresponding to the enum values
# exists            : boolean : create,query               :  Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
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
	STS = ['bool', 'byte', 'char','double', 'doubleAngle', 'doubleLinear','float','long', 'reflectance', 'short','spectrum','time']
	CTS = ['double2', 'double3','float2', 'float3','long2', 'long3','short2', 'short3']
	
#----------------------------------------------------------------------
def build_kwargs(create=None           , query=None           , edit=None    , multiuse=None,
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
def make_plug_path(node=None,attr=None):
	if node == None:
		node = cmds.ls(sl=True)
	if attr == None:
		if "." in node:
			attr = ".".join(node.split(".")[1:])
			node = node.split(".")[0]
		else:
			raise ValueError("input was not a valid Plug")
	full_plug_path = ".".join([node,attr])
	return full_plug_path, node, attr
#----------------------------------------------------------------------
def Attribute_Exists(node,attr=None):
	plug, node, attr = make_plug_path(node, attr)
	return cmds.objExists( plug )
#----------------------------------------------------------------------
def Delete_Attribute(node,attr=None):
	plug, node, attr = make_plug_path(node, attr)
	if Attribute_Exists(node,attr):
		cmds.deleteAttr( node, attribute=attr )

def add_Attr(at, node, attr=None, multi=None, longName=None, shortName=None,niceName=None, indexMatters=None, numberOfChildren=None, parent=None, defaultValue=None, storable=None, keyable=None, readable=None, hidden=None, writable=None, maxValue=None, minValue=None, softMaxValue=None, softMinValue=None):
	""""""
	build_kwargs(attributeType=at, storable=storable, defaultValue=defaultValue, writable=writable,hidden=hidden, indexMatters=indexMatters,keyable=keyable, shortName=shortName, longName=longName, maxValue=maxValue, minValue=minValue, multi=multi, niceName=niceName, numberOfChildren=numberOfChildren, parent=parent, readable=readable, softMaxValue=softMaxValue, softMinValue=softMinValue)
	plug, node, attr = make_plug_path(node, attr)
	if not Attribute_Exists(node, attr):
		cmds.addAttr(node,longName=attr,attributeType=at, multi=multi, )
	return plug
#----------------------------------------------------------------------
def add_Simple_Attr(at, node, attr=None, multi=False, parent=False):
	""""""
	plug, node, attr = make_plug_path(node, attr)
	if not Attribute_Exists(node, attr):
		if parent:
			cmds.addAttr(node,longName=attr,attributeType=at, multi=multi, parent=parent)
		else:
			cmds.addAttr(node,longName=attr,attributeType=at, multi=multi)
	return plug
#----------------------------------------------------------------------
def add_2_Item_Attr(at, node, attr=None, multi=False, parent=False):
	plug, node, attr = make_plug_path(node, attr)
	if not Attribute_Exists(node, attr):
		if parent:
			cmds.addAttr(node,longName=attr,at=str(at+'2'), multi=multi, parent=parent)
		else:
			cmds.addAttr(node,longName=attr,at=str(at+'2'), multi=multi)
		cmds.addAttr(node,longName=(attr + "X"),parent=attr,attributeType=at)
		cmds.addAttr(node,longName=(attr + "Y"),parent=attr,attributeType=at)
	return plug
#----------------------------------------------------------------------
def add_3_Item_Attr(at, node, attr=None, multi=False, parent=False):
	plug, node, attr = make_plug_path(node, attr)
	if not Attribute_Exists(node, attr):
		if parent:
			cmds.addAttr(node,longName=attr,attributeType=at+'3', multi=multi, parent=parent)
		else:
			cmds.addAttr(node,longName=attr,attributeType=at+'3', multi=multi)
		cmds.addAttr(node,longName=(attr + "X"),parent=attr,attributeType=at)
		cmds.addAttr(node,longName=(attr + "Y"),parent=attr,attributeType=at)
		cmds.addAttr(node,longName=(attr + "Z"),parent=attr,attributeType=at)
	return plug
#----------------------------------------------------------------------
def get_Simple_Value(node, attr=None):
	plug, node, attr = make_plug_path(node, attr)
	plug_type = cmds.getAttr(plug, type=True)
	if plug_type in MTypes.STS or plug_type == "string":
		return cmds.getAttr(plug)
	elif plug_type in MTypes.CTS:
		return list(cmds.getAttr(plug)[0])
	return cmds.getAttr(plug)
#----------------------------------------------------------------------
def get_Simple_Multi_Index_Value(node, attr=None):
	plug, node, attr = make_plug_path(node, attr)
	plug_type = cmds.getAttr(plug, type=True)
	if plug_type in MTypes.STS or plug_type == "string":
		return cmds.getAttr(plug)
	elif plug_type in MTypes.CTS:
		return list(cmds.getAttr(plug)[0])
	return cmds.getAttr(plug)
#----------------------------------------------------------------------
def set_Simple_Value(node, value, attr=None):
	plug, node, attr = make_plug_path(node, attr)
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
def Add_Simple_Data(dt, node, attr=None, multi=False, parent=False):
	""""""
	plug, node, attr = make_plug_path(node, attr)
	if not Attribute_Exists(node, attr):
		if parent:
			cmds.addAttr(node,longName=attr,dt=dt, multi=multi, parent=parent)
		else:
			cmds.addAttr(node,longName=attr,dt=dt, multi=multi)
	return plug


#----------------------------------------------------------------------
def Add_Char(node, attr=None, parent=False):
	return add_Simple_Attr('char', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Multi_Char(node,attr=None, parent=False):
	return add_Simple_Attr('char', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Byte(node,attr=None, parent=False):
	return add_Simple_Attr('byte', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Byte_M(node,attr=None, parent=False):
	return add_Simple_Attr('byte', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Bool(node,attr=None, parent=False):
	return add_Simple_Attr('bool', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Bool_M(node,attr=None, parent=False):
	return add_Simple_Attr('bool', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Short(node,attr=None, parent=False):
	return add_Simple_Attr('short', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Short_M(node,attr=None, parent=False):
	return add_Simple_Attr('short', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Short2(node,attr=None, parent=False):
	return add_2_Item_Attr('short', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Short2_M(node,attr=None, parent=False):
	return add_2_Item_Attr('short', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Short3(node,attr=None, parent=False):
	return add_3_Item_Attr("short", node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Long(node,attr=None, parent=False):
	return add_Simple_Attr('long', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Long_M(node,attr=None, parent=False):
	return add_Simple_Attr('long', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Long2(node,attr=None, parent=False):
	return add_2_Item_Attr('long', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Long2_M(node,attr=None, parent=False):
	return add_2_Item_Attr('long', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Long3(node,attr=None, parent=False):
	return add_3_Item_Attr('long', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Long3_M(node,attr=None, parent=False):
	return add_3_Item_Attr('long', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Float(node,attr=None, parent=False):
	return add_Simple_Attr("float", node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Float2(node,attr=None, parent=False):
	return add_2_Item_Attr("float", node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Float3(node,attr=None, parent=None):
	return add_3_Item_Attr("float", node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Double_Angle(node,attr=None, parent=False):
	return add_Simple_Attr("doubleAngle", node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Double_Linear(node,attr=None, parent=False):
	return add_Simple_Attr("doubleLinear", node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Message(node,attr=None, parent=False):
	return add_Simple_Attr('message', node, attr=attr, multi=False, parent=parent)
#----------------------------------------------------------------------
def Add_Message_M(node,attr=None, parent=False):
	return add_Simple_Attr('message', node, attr=attr, multi=True, parent=parent)
#----------------------------------------------------------------------
def Add_Enum(node,attr=None, enumName="Green:Blue:", parent=False):
	plug, node, attr = make_plug_path(node, attr)
	if not Attribute_Exists(node, attr):
		if parent:
			cmds.addAttr( node, shortName=attr, longName=attr, at="enum",enumName=enumName, parent=parent)
		else:
			cmds.addAttr( node, shortName=attr, longName=attr, at="enum",enumName=enumName)
	return plug
#----------------------------------------------------------------------
def Add_String(node,attr=None, parent=False):
	if parent:
		return Add_Simple_Data("string", node, attr=attr, multi=False, parent=parent)
	else:
		return Add_Simple_Data("string", node, attr=attr, multi=False)
#----------------------------------------------------------------------
def Add_String_M(node,attr=None):
	return Add_Simple_Data("string", node, attr=attr, multi=True)
#----------------------------------------------------------------------
def Add_String_Array(node,attr=None):
	return Add_Simple_Data("stringArray", node, attr=attr, multi=False)
#----------------------------------------------------------------------
def Add_String_Array_M(node,attr=None):
	return Add_Simple_Data("stringArray", node, attr=attr, multi=True)
#----------------------------------------------------------------------
def Add_Float_Matrix(node,attr=None):
	return Add_Simple_Data("fltMatrix", node, attr=attr, multi=False)
#----------------------------------------------------------------------
def Add_Float_Matrix_M(node,attr=None):
	return Add_Simple_Data("fltMatrix", node, attr=attr, multi=True)
#----------------------------------------------------------------------
def Add_Int32_Array(node,attr=None):
	return Add_Simple_Data("Int32Array", node, attr=attr, multi=False)
#----------------------------------------------------------------------
def Add_Int32_Array_M(node,attr=None):
	return Add_Simple_Data("Int32Array", node, attr=attr, multi=True)	
#----------------------------------------------------------------------
def Add_Double_Array(node,attr=None):
	return Add_Simple_Data("doubleArray", node, attr=attr, multi=False)
#----------------------------------------------------------------------
def Add_Double_Array_M(node,attr=None):
	return Add_Simple_Data("doubleArray", node, attr=attr, multi=True)
#----------------------------------------------------------------------
def Set_String_M_Item(node,attr,Value,Index):
	cmds.setAttr((node + "." + attr + "[" + str(Index) + "]"),Value,type=("string"))
#----------------------------------------------------------------------
def Set_Float_Matrix(node,attr,M):
	plug   = node + "." + attr
	values = flatten(M)
	cmds.setAttr((plug),values,type=("matrix"))
#----------------------------------------------------------------------
def Set_Float_Matrix_M(node,attr,M,Index):
	plug   = node + "." + attr + "[" + str(Index) + "]"
	values = flatten(M)
	cmds.setAttr((plug),values,type=("matrix"))
#----------------------------------------------------------------------
def Set_Int32_Array(node,attr,IntValues):
	plug = node + "." + attr
	cmds.setAttr(plug,IntValues,type="Int32Array")
#----------------------------------------------------------------------
def Set_Int32_Array_M(node,attr,IntValues,Index):
	plug = node + "." + attr + "[" + str(Index) + "]"
	cmds.setAttr(plug,IntValues,type="Int32Array")
#----------------------------------------------------------------------
def Set_Double_Array(node,attr,FltValues):
	plug = node + "." + attr
	cmds.setAttr(plug,FltValues,type="doubleArray")
#----------------------------------------------------------------------
def Set_Double_Array_M(node,attr,FltValues,Index):
	plug = node + "." + attr + "[" + str(Index) + "]"
	cmds.setAttr(plug,FltValues,type="doubleArray")
#----------------------------------------------------------------------
def Set_String_Array(node,attr,StrValues):
	plug = node + "." + attr
	len(StrValues)
	args = [plug, len(StrValues)] + StrValues
	cmds.setAttr(*args,type="stringArray")
#----------------------------------------------------------------------
def Set_String_Array_M(node,attr,StrValues,Index):
	plug = node + "." + attr + "[" + str(Index) + "]"
	cmds.setAttr(plug,StrValues,type="stringArray")
	
#Adds a compond attribute
def Add_Compound_Attribute(node, attrName, child_attribs):
	if not Attribute_Exists( node, attrName):
		child_count = len(child_attribs)
		print((cmds.addAttr(node, shortName=attrName, longName=attrName, numberOfChildren=child_count, attributeType='compound' )))
		for typ, name in child_attribs:
			if typ == "bool":
				Add_Bool(node, attr=name, parent=attrName)
			elif typ == "byte":
				Add_Byte(node, attr=name, parent=attrName)
			elif typ == "char":
				Add_Char(node, attr=name, parent=attrName)
			elif typ == "enum":
				Add_Enum(node, attr=name, enumName="Green:Blue:", parent=attrName)
			elif typ.startswith("long"):
				if typ.endswith("2"):
					Add_Long2(node, attr=name, parent=attrName)
				elif typ.endswith("3"):
					Add_Long3(node, attr=name, parent=attrName)
				else:
					Add_Long(node, attr=name, parent=attrName)
			elif typ.startswith("short"):
				if typ.endswith("2"):
					Add_Short2(node, attr=name, parent=attrName)
				elif typ.endswith("3"):
					Add_Short3(node, attr=name, parent=attrName)
				else:
					Add_Short(node, attr=name, parent=attrName)
			elif typ.startswith("float"):
				if typ.endswith("2"):
					Add_Float2(node, attr=name, parent=attrName)
				elif typ.endswith("3"):
					Add_Float3(node, attr=name, parent=attrName)
				else:
					Add_Float(node, attr=name, parent=attrName)
			elif typ == "string":
				Add_String(node, attr=name, parent=attrName)
			elif typ == "stringArray":
				Add_String_Array(node, attr=name, parent=attrName)