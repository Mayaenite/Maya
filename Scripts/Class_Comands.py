import maya.cmds
import string
from functools import partial

#################################################################################
class Dynamic_Attribute_Object(object):
	invalid_chars = list(string.punctuation.replace("_", "") + string.whitespace)
	string_digits = list(string.digits)
	#----------------------------------------------------------------------
	def __init__(self, data={}):
		for key, value in data.iteritems():
			self.add(key, value)
	#----------------------------------------------------------------------
	def add(self,key,value):
		key_chars    = [k for k in list(key) if not k in Dynamic_Attribute_Object.invalid_chars]
		key_chars[0] = key_chars[0] if not key_chars[0] in Dynamic_Attribute_Object.string_digits else str("n_" + key_chars[0])
		key          = "".join(key_chars)
		if isinstance(value, dict):
			self.__dict__[key] = Dynamic_Attribute_Object(value)
		elif isinstance(value, list):
			new_val = []
			for val in value:
				if isinstance(val, dict):
					val = Dynamic_Attribute_Object(val)
				new_val.append(val)
			self.__dict__[key] = new_val
		else:
			self.__dict__[key] = value
#########################################################################
class Command_Caller(object):
	Args_And_Keys = 1
	Args_Only     = 2
	Keys_Only     = 3
	No_Inputs     = 4
	#----------------------------------------------------------------------
	def __init__(self, func,args=[],kwargs={},modifier=[]):
		self.func                   = func
		self.args                   = args
		self.kwargs                 = kwargs
		self.modifier               = modifier
		self.modifier_attribute_obj = Dynamic_Attribute_Object()
		[self.modifier_attribute_obj.add(m.name,m) for m in self.modifier]
	#----------------------------------------------------------------------
	def _modified_Inputs(self, *args, **kwargs):
		""""""
		args   = self.args if not len(args) else args
		kwargs = self.kwargs if not len(kwargs) else kwargs.update(self.kwargs)
		[kwargs.setdefault(m.name, m.value) for m in self.modifier if m.active]
		return [args, kwargs]
	#----------------------------------------------------------------------
	def _get_call_version(self, *args, **kwargs):
		""""""
		if len(args) and len(kwargs):
			return self.Args_And_Keys
		elif len(args) and not len(kwargs):
			return self.Args_Only
		elif not len(args) and len(kwargs):
			return self.Keys_Only
		else:
			return self.No_Inputs
	#----------------------------------------------------------------------
	def __call__(self, *args, **kwargs):
		args, kwargs = self._modified_Inputs(*args, **kwargs)
		call_version = self._get_call_version(*args, **kwargs)
		if call_version == self.Args_And_Keys:
			return self.func(*args,**kwargs)
		elif call_version == self.Args_Only:
			return self.func(*args)
		elif call_version == self.Keys_Only:
			return self.func(**kwargs)
		elif call_version == self.No_Inputs:
			return self.func()
#########################################################################
class Modifier_Flag(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, active=False, value=None):
		"""Constructor"""
		self._name   = name
		self._active = active
		self._value  = value
	#----------------------------------------------------------------------
	def _get_name(self):
		return self._name
	#----------------------------------------------------------------------
	def _get_active(self):
		return self._active
	#----------------------------------------------------------------------
	def _set_active(self,val):
		self._active = val
	#----------------------------------------------------------------------
	def toggle_active(self):
		if self.active:
			self._set_active(False)
		else:
			self._set_active(True)
	#----------------------------------------------------------------------
	def _get_Value(self):
		return self._value
	#----------------------------------------------------------------------
	def _set_Value(self, val):
		self._value  = val
	#----------------------------------------------------------------------
	name   = property(_get_name)
	active = property(_get_active,_set_active)	
	value  = property(_get_Value, _set_Value)
########################################################################
class Command_Content_MetaClass(type):
	""""""
	#----------------------------------------------------------------------
	def __init__(cls, name, bases, kwds):
		super(Command_Content_MetaClass, cls).__init__(name, bases, kwds)
		cls.cmd = getattr(maya.cmds, cls.cmd)
		Mod_flags=[]
		for sec_flag in cls.secondary_flags:
			mod_flag = partial(Modifier_Flag,sec_flag)
			Mod_flags.append(mod_flag)
		cls.modifier_flags=Mod_flags
########################################################################
class Select_Command_Content(object):
	""""""
	__metaclass__ = Command_Content_MetaClass
	secondary_flags   = ["noExpand", "visible", "hierarchy"]
	primary_flags     = ["add","clear","deselect","toggle"]
	primary_comands   = []
	modifier_flags    = []
	cmd               = "select"
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		"""Constructor"""
		self.primary_comands =[]
		for flag in self.primary_flags:
			kws = {flag:True}
			mods = [m()for m in self.modifier_flags]
			if len(kwargs):
				for m in mods:
					if m.name in kwargs:
						m.active = True
						m.value = kwargs.get(m.name)
			fn=Command_Caller(self.cmd,args=args,kwargs=kws,modifier=mods)
			self.primary_comands.append(fn)
			setattr(self,flag,fn)
	#----------------------------------------------------------------------
	def set_primary_comands_args(self,args):
		if isinstance(args,(list,tuple)):
			for prim_cmd in self.primary_comands:
				prim_cmd.args=args
	#----------------------------------------------------------------------
	def set_primary_comands_kwargs(self,**kwargs):
		if isinstance(kwargs,dict):
			for prim_cmd in self.primary_comands:
				prim_cmd.kwargs=kwargs
########################################################################
class List_Attr_Command_Content(Select_Command_Content):
	""""""
	__metaclass__ = Command_Content_MetaClass
	secondary_flags   = ["array", "caching" , "changedSinceFileOpen", "category", "extension", "fromPlugin", "hasData", "hasNullData", "inUse", "leaf", "multi", "output", "read", "ramp", "readOnly", "scalar", "scalarAndArray", "settable", "shortNames", "string", "unlocked", "userDefined", "usedAsFilename", "visible", "write"]
	primary_flags     = ["connectable","channelBox","keyable","locked"]
	primary_comands   = []
	modifier_flags    = []
	cmd               = "listAttr"

########################################################################
class List_Select_Command_Content(Select_Command_Content):
	""""""
	__metaclass__ = Command_Content_MetaClass
	secondary_flags   = ["long","leaf","noIntermediate","nodeTypes","objectsOnly","orderedSelection","recursive","renderGlobals","referencedNodes","readOnly","shapes","sets","selection","shortNames","showNamespace","showType","textures","tail","templated","transforms","type","undeletable","untemplated","visible", "invisible"]
	primary_flags     = ["lockedNodes","materials","modified","live","lights","planes","partitions", "references", "visible", "persistentNodes", "sets", "selection", "textures", "transforms", "invisible"]
	primary_comands   = []
	modifier_flags    = []
	cmd               = "ls"
