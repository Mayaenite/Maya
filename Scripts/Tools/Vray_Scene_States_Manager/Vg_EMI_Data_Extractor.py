import pickle
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mm
import xml.etree.ElementTree as etree
import os
class EIM_Config_Data(object):
	def __init__(self, code, layers):
		self.code = code
		self.layers = layers

#----------------------------------------------------------------------
def Get_XML_EMI_Data():
	""""""
	def find_by_id(idnum):
		Options = root.findall("*//Option")
		displayLayers = cmds.ls(typ="displayLayer")
		res = []
		for child in Options:
			if child.get("id")==idnum:
				if child.tag == "Option":
					for layer in child.findall("Asset//Layer"):
						for dispLayer in displayLayers:
							if dispLayer[5:] == layer.get("name"):
								res.append(dispLayer)
								break
		return res
	
	vg_script = pm.ls("VGConfigXMLScriptNode")[0]
	data = etree.fromstring(vg_script.before.get())
	root = data
	pickle_file            = os.path.join(os.environ["temp"],"EMI_BUILD_DATA.pkl")
	pickle_Data            = list()
	SavedStates = root.find("SavedStates")
	ProductConfigurations = SavedStates.findall("ProductConfiguration")
	for config in ProductConfigurations:
		config_data=dict(code=config.get('name')[0:18],dls=[],rls=[])
		choosenOptions = config.findall("choosenOption")
		layers = []
		for option in choosenOptions:
			found_layers = find_by_id(option.get("id"))
			if len(found_layers):
				layers.extend(found_layers)
		config_data['dls']= list(set(layers))
		pickle_Data.append(config_data)
	with file(pickle_file,'w') as pkf:
		pickle.dump(pickle_Data,pkf)
#----------------------------------------------------------------------
def Get_EIM_Data():
	try:
		pm.mel.VGConfigWindow()
		cmds.deleteUI("windowVGConfigWindow",window=True)
		adjustDisplayLayer = pm.mel.adjustDisplayLayer
		adjustRenderLayer = pm.mel.adjustRenderLayer
		pickle_file            = os.path.join(os.environ["temp"],"EMI_BUILD_DATA.pkl")
		displayLayerController = pm.melGlobals["displayLayerController"]
		renderLayerController  = pm.melGlobals["renderLayerController"]
		displayLayers          = pm.melGlobals["displayLayers"]
		renderLayers           = pm.melGlobals["renderLayers"]
		exteriorColors         = pm.melGlobals["exteriorColors"]
		modelCodes             = pm.melGlobals["modelCodes"]
		pickle_Data            = list()
		code_count             = len(modelCodes)
		all_display_layers     = [layer for layer in cmds.ls(typ="displayLayer") if not layer == "defaultLayer"]
		for i,code in enumerate(modelCodes):
			config_data=dict(code=code,dls=[],rls=[])
			adjustDisplayLayer(displayLayerController,code)
			cmds.inViewMessage( statusMessage='<hl>Collecting Data For Eim %i of %i\n"%s"</hl>.' % (i+1,code_count,code), fadeInTime=0, fadeOutTime=0, fadeStayTime=200,fontSize=20, pos='midCenter', fade=True )
			cmds.refresh()
			active_dls =  []
			for layer in all_display_layers:
				if cmds.getAttr(layer+".v"):
					active_dls.append(layer)
			config_data['dls']= list(set(active_dls))
			#adjustRenderLayer(renderLayerController, code)
			#actvie_rls = []
			#for layer in renderLayers:
			#	cmds.refresh()
			#	if cmds.objExists(layer):
			#		if cmds.getAttr(layer+".renderable"):
			#			actvie_rls.append(layer)
			#config_data['rls']=actvie_rls
			pickle_Data.append(config_data)
		with file(pickle_file,'w') as pkf:
			pickle.dump(pickle_Data,pkf)
	except MelUnknownProcedureError:
		cmds.error("Cannot find procedure VGConfigWindow")
#----------------------------------------------------------------------
def dump_EIM_Data():
	if pm.objExists("VGConfigXMLScriptNode"):
		Get_XML_EMI_Data()
	else:
		Get_EIM_Data()
#----------------------------------------------------------------------
def load_EIM_Data():
	res = []
	pickle_file            = os.path.join(os.environ["temp"],"EMI_BUILD_DATA.pkl")
	with file(pickle_file,'r') as pkf:
		pickle_Data = pickle.load(pkf)
	for item in pickle_Data:
		res.append(EIM_Config_Data(item['code'],item['dls']))
	return res
