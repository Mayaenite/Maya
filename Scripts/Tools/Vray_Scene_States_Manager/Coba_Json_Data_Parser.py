import pymel.core as pm
import maya.cmds as cmds
import json
from collections import OrderedDict


#----------------------------------------------------------------------
def build_Name_To_Layer_Data():
	""""""
	_G_ALL_DISPLAY_LAYERS = cmds.ls(typ="displayLayer")
	_G_ALL_DISPLAY_LAYER_Short_Names = [item.split("_",1)[-1] for item in _G_ALL_DISPLAY_LAYERS]
	return dict(list(zip(_G_ALL_DISPLAY_LAYER_Short_Names,_G_ALL_DISPLAY_LAYERS)))

_G_DISPLAY_LAYER_DICT = build_Name_To_Layer_Data()

#----------------------------------------------------------------------
def get_json_data():
	""""""
	if not cmds.objExists("JSON_document"):
		raise LookupError("JSON_document Script Node Does Not Exist")
	json_data     = eval(cmds.getAttr("JSON_document.before"))
	return json_data

########################################################################
class LAYER(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self,key,name):
		"""Constructor"""
		self.key  = key
		self.name = str(name)
		self.displayLayer = self._get_display_layer()
	#----------------------------------------------------------------------
	def _get_display_layer(self):
		
		if self.name in _G_DISPLAY_LAYER_DICT:
			return _G_DISPLAY_LAYER_DICT[self.name]
		else:
			raise LookupError("Could Not Find Display Layer Containing The Name {}".format(self.name))
	#----------------------------------------------------------------------
	def hide(self):
		cmds.setAttr(self.displayLayer+".visibility",0)
	#----------------------------------------------------------------------
	def show(self):
		cmds.setAttr(self.displayLayer+".visibility",1)
	#----------------------------------------------------------------------
	def __repr__(self):
		return self.displayLayer
	#----------------------------------------------------------------------
	def __str__(self):
		return self.displayLayer

########################################################################
class LAYERS(dict):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,json_data):
		"""Constructor"""
		super(LAYERS,self).__init__()
		self.lookup_errors = []

		for key in sorted(json_data["all_vses"]):
			name = json_data["all_vses"][key]
			try:
				layer = LAYER(key,name)
				self[key] = layer
			except LookupError as e:
				self.lookup_errors.append(name)
	

		
########################################################################
class EIM(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self,name,master_layer_dict,InteriorTrims=[],colors=[],layers=[]):
		"""Constructor"""
		self.name           = name
		self.Interior_Trims = InteriorTrims
		self.colors         = colors
		self.layers         = []
		for layer in layers:
			if layer in master_layer_dict:
				self.layers.append(master_layer_dict[layer])
	#----------------------------------------------------------------------
	def get_layer_names(self):
		""""""
		return [layer.displayLayer for layer in self.layers]
########################################################################
class EIMS(list):
	""""""

	#----------------------------------------------------------------------
	def __init__(self,json_data,master_layer_dict):
		"""Constructor"""
		super(EIMS,self).__init__()
		for eim_name in json_data["eims"]:
			eim_data = json_data["eims"][eim_name]
			Interior_Trims = eim_data["Interior Trims"]
			Colors         = eim_data["Colors"]
			contained_vses = eim_data["contained_vses"]
			eim_build      = EIM(eim_name,master_layer_dict,Interior_Trims,Colors,contained_vses)
			self.append(eim_build)
########################################################################
class Json_Config_Data(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self):
		json_data = get_json_data()
		self.master_layer_dict = LAYERS(json_data)
		self.Eim_Builds = EIMS(json_data,self.master_layer_dict)
		
	#----------------------------------------------------------------------
	def hide_all(self):
		for layer_item in self.master_layer_dict.values():
			layer_item.hide()
			
	def show_build(self,num):
		self.hide_all()
		for layer in self.Eim_Builds[num].layers:
			layer.show()




