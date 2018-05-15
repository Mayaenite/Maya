try:
	import pymel.core as pm
	import maya.cmds as cmds
	import maya.mel as mel
	_maya_check = True
except:
	_maya_check = False
	
import xml.etree.ElementTree as etree
import re
pattern = re.compile('(\([^\)]+\))')
########################################################################
class Coba_Element_Base(etree.Element):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent, tag, attrib={}, **extra):
		"""Constructor"""
		super(Coba_Element_Base,self).__init__(tag, attrib)
		self._parent = parent
		self._root_element = None
		isinstance(self.root_element,ConfigurationLogic)
	#----------------------------------------------------------------------
	@property
	def parent_element(self):
		""""""
		return self._parent
	#----------------------------------------------------------------------
	@property
	def children(self):
		""""""
		return self._children
	#----------------------------------------------------------------------
	@property
	def root_element(self):
		""""""
		if self._root_element == None:
			elem = self
			while not elem._parent == None:
				elem = elem._parent
			self._root_element = elem
		return self._root_element


########################################################################
class SavedStates(Coba_Element_Base):
	""""""
	#----------------------------------------------------------------------
	@property
	def ProductConfigurations(self):
		''' '''
		return self.getiterator(tag="ProductConfiguration")
########################################################################
class Coba_Named_Element(Coba_Element_Base):
	""""""
	#----------------------------------------------------------------------
	@property
	def name(self):
		""""""
		return self.get("name")
	
########################################################################
class Coba_ID_Element(Coba_Element_Base):
	""""""
	#----------------------------------------------------------------------
	@property
	def id(self):
		""""""
		return int(self.get("id",default=-1))
	
########################################################################
class ProductConfiguration(Coba_Named_Element):
	""""""
	@property
	def eim_name(self):
		''' '''
		return self.name[0:18]
	@property
	def Options(self):
		''' '''
		return [child.Option for child in self.choosenOptions]
	@property
	def choosenOptions(self):
		''' '''
		return self.getiterator(tag="choosenOption")
	@property
	def choosen_ids(self):
		''' '''
		return [child.id for child in self.choosenOptions]
	#----------------------------------------------------------------------
	def valid_layers(self):
		""""""
		layers = []
		for option in self.Options:
			isinstance(option,Option)
			for asset in option.Assets:
				if isinstance(asset,Asset_Layerset):
					if asset.has_Condition:
						if asset.AssetCondition.eval_Boolean_Expression(self.choosen_ids):
							for layer in asset.Layers:
								layers.append(layer.name)
					else:
						for layer in asset.Layers:
							layers.append(layer.name)
		return layers
	#----------------------------------------------------------------------
	def expersions_list(self):
		""""""
		expressions = []
		for option in self.Options:
			isinstance(option,Option)
			for asset in option.Assets:
				if isinstance(asset,Asset_Layerset):
					if asset.has_Condition:
						expressions.append(asset.AssetCondition.formate_Boolean_Expression(self.choosen_ids))
		return expressions
	#----------------------------------------------------------------------
	def maya_display_layers(self):
		""""""
		res = []
		if _maya_check:
			all_display_layers = [layer for layer in cmds.ls(typ="displayLayer") if not str(layer) == 'defaultLayer']
			valid_layers = self.valid_layers()
			#mel.eval('setLayerTo all".visibility" 0')
			for dl in all_display_layers:
				for vl in valid_layers:
					if vl == dl[5:]:
						res.append(dl)
						break
		return list(set(res))
########################################################################
class Property(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def Options(self):
		''' '''
		return self.getiterator(tag="Option")
	#----------------------------------------------------------------------
	@property
	def isPseudoCode(self):
		''' '''
		return self.get("isPseudoCode")
	#----------------------------------------------------------------------
	@property
	def name(self):
		''' '''
		return self.get("name")
	#----------------------------------------------------------------------
	@property
	def optionDisplayType(self):
		''' '''
		return self.get("optionDisplayType")
	#----------------------------------------------------------------------
	@property
	def order(self):
		''' '''
		return int(self.get("order"))
	#----------------------------------------------------------------------
	@property
	def tabName(self):
		''' '''
		return self.get("tabName")
########################################################################
class Option(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def Assets(self):
		''' '''
		return self.getiterator(tag="Asset")
	#----------------------------------------------------------------------
	@property
	def code(self):
		''' '''
		return self.get("code")
	#----------------------------------------------------------------------
	@property
	def displayName(self):
		''' '''
		return self.get("displayName")
	#----------------------------------------------------------------------
	@property
	def iconName(self):
		''' '''
		return self.get("iconName")
	#----------------------------------------------------------------------
	@property
	def liveSwitcherTooltip(self):
		''' '''
		return self.get("liveSwitcherTooltip")
	#----------------------------------------------------------------------
	@property
	def order(self):
		''' '''
		return self.get("order")

########################################################################
class choosenOption(Coba_ID_Element):
	""""""
	@property
	def Option(self):
		''' '''
		return self.root_element.find("./Property/Option[@id='%i']" % self.id)
########################################################################
class Asset(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def fromMjAj(self):
		''' '''
		return self.get("fromMjAj")
	#----------------------------------------------------------------------
	@property
	def name(self):
		''' '''
		return self.get("name")
	#----------------------------------------------------------------------
	@property
	def type(self):
		''' '''
		return self.get("type")
	#----------------------------------------------------------------------
	@property
	def AssetCondition(self):
		''' '''
		return self.find("AssetCondition")
	#----------------------------------------------------------------------
	@property
	def has_Condition(self):
		""""""
		return self.AssetCondition is not None
########################################################################
class Asset_Layerset(Asset):
	""""""
	#----------------------------------------------------------------------
	@property
	def Layers(self):
		''' '''
		return self.getiterator(tag="Layer")
########################################################################
class Asset_MaterialScheme3d(Asset):
	""""""	
########################################################################
class AssetCondition(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def booleanExpression(self):
		''' '''
		return self.get("booleanExpression")
	#----------------------------------------------------------------------
	@property
	def py_booleanExpression(self):
		''' '''
		res = self.get("booleanExpression").replace("!", 'not')
		print res
		return res
	#----------------------------------------------------------------------
	@property
	def Asset(self):
		""""""
		return self.parent_element
	#----------------------------------------------------------------------
	def formate_Boolean_Expression(self,option_ids_list):
		""""""
		option_ids_list = [str(val) for val in option_ids_list]
		items = self.py_booleanExpression.split()
		expression = [item for item in items]
		for id_num in option_ids_list:
			for index,val in enumerate(items):
				if id_num == val:
					expression[index]="1"
		for id_num in option_ids_list:
			for index , val in enumerate(expression):
				if val != "not" and val != "and" and val != "or" and val != "(" and val != ")" and val != "1" and val != id_num:
					expression[index]="0"
		expression = " ".join(expression)
		if expression == "":
			expression = "1"
		return expression
	#----------------------------------------------------------------------
	def eval_Boolean_Expression(self,option_ids_list):
		return eval(self.formate_Boolean_Expression(option_ids_list))
########################################################################
class Asset_Layer(Coba_ID_Element):
	""""""
	@property
	def Real_Layer(self):
		''' '''
		return self.root_element.find("./LayerContainer/Layer[@id='%i']" % self.id)
	#----------------------------------------------------------------------
	@property
	def is2dRendering(self):
		''' '''
		return bool(int(self.get("is2dRendering")))
	#----------------------------------------------------------------------
	@property
	def is3dRendering(self):
		''' '''
		return bool(int(self.get("is3dRendering")))
	#----------------------------------------------------------------------
	@property
	def isGeometryLayer(self):
		''' '''
		return bool(int(self.get("isGeometryLayer")))
	#----------------------------------------------------------------------
	@property
	def matte(self):
		''' '''
		return int(self.get("matte"))
	#----------------------------------------------------------------------
	@property
	def name(self):
		''' '''
		return self.Real_Layer.name
	#----------------------------------------------------------------------
	@property
	def visibility(self):
		''' '''
		return bool(int(self.get("visibility")))
	#----------------------------------------------------------------------
	@property
	def visibleToCam(self):
		''' '''
		return bool(int(self.get("visibleToCam")))
########################################################################
class Layer(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def compound(self):
		''' '''
		return self.get("compound")
	#----------------------------------------------------------------------
	@property
	def msExt(self):
		''' '''
		return bool(int(self.get("msExt")))
	#----------------------------------------------------------------------
	@property
	def msInt(self):
		''' '''
		return bool(int(self.get("msInt")))
	#----------------------------------------------------------------------
	@property
	def name(self):
		''' '''
		return self.get("name")
	#----------------------------------------------------------------------
	@property
	def radiogroup(self):
		''' '''
		return self.get("radiogroup")
	#----------------------------------------------------------------------
	@property
	def visExt(self):
		''' '''
		return bool(int(self.get("visExt")))
	#----------------------------------------------------------------------
	@property
	def visInt(self):
		''' '''
		return bool(int(self.get("visInt")))
########################################################################
class Material(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def name(self):
		''' '''
		return self.get("name")
	#----------------------------------------------------------------------
	@property
	def MaterialContainer(self):
		""""""
		return self.parent_element
########################################################################
class ConfigurationLogic(Coba_ID_Element):
	""""""
	#----------------------------------------------------------------------
	@property
	def Property(self):
		""""""
		return self.getiterator(tag="Property")
	@property
	def SavedStates(self):
		''' '''
		return self.find("SavedStates")
	@property
	def LayerContainer(self):
		''' '''
		return self.find("LayerContainer")
	@property
	def MaterialContainer(self):
		''' '''
		return self.find("MaterialContainer")
	@property
	def MaterialContainer(self):
		''' '''
		return self.find("MaterialContainer")
	#----------------------------------------------------------------------
	@property
	def customer(self):
		""""""
		return self.get("customer",default="")
	#----------------------------------------------------------------------
	@property
	def hashMaterialCodes(self):
		""""""
		return self.get("hashMaterialCodes") == "True"
	#----------------------------------------------------------------------
	@property
	def isPictureShooterMode(self):
		""""""
		return self.get("isPictureShooterMode") == "True"
	#----------------------------------------------------------------------
	@property
	def manufacturer(self):
		""""""
		return self.get("manufacturer",default="")
	#----------------------------------------------------------------------
	@property
	def mayaLayerMode(self):
		""""""
		return self.get("mayaLayerMode",default="")
	#----------------------------------------------------------------------
	@property
	def name(self):
		""""""
		return self.get("name",default="")
	#----------------------------------------------------------------------
	@property
	def previewImagePath(self):
		""""""
		return self.get("previewImagePath",default="")
	#----------------------------------------------------------------------
	@property
	def productDescription(self):
		""""""
		return self.get("productDescription",default="")
	#----------------------------------------------------------------------
	@property
	def productDisplayName(self):
		""""""
		return self.get("productDisplayName",default="")
	#----------------------------------------------------------------------
	@property
	def productName(self):
		""""""
		return self.get("productName",default="")
	#----------------------------------------------------------------------
	@property
	def project_settings_file(self):
		""""""
		return self.get("project_settings_file",default="")
	#----------------------------------------------------------------------
	@property
	def stringLevel(self):
		""""""
		return self.get("stringLevel",default="")
	#----------------------------------------------------------------------
	@property
	def version(self):
		""""""
		return int(self.get("version"))
#----------------------------------------------------------------------
def Coba_Element_Factory(parent,tag, attrib={}, **extra):
	""""""
	if tag in ["ConfigurationLogic","Property","AssetCondition","Option","Material","SavedStates","ProductConfiguration","choosenOption"]:
		cls = globals().get(tag)
		return cls(parent, tag, attrib)
	elif tag == "Asset":
		asset_type = attrib.get("type")
		if asset_type == "Layerset":
			return Asset_Layerset(parent, tag, attrib)
		elif asset_type == "MaterialScheme3d":
			return Asset_MaterialScheme3d(parent, tag, attrib)
		else:
			return Asset(parent, tag, attrib)
	elif tag == "Layer":
		if "is3dRendering" in attrib.keys():
			return Asset_Layer(parent, tag, attrib)
		elif "compound" in attrib.keys():
			return Layer(parent, tag, attrib)
	else:
		return Coba_Element_Base(parent,tag, attrib)
########################################################################
class Coba_Tree_Builder(etree.TreeBuilder):
	""""""
	def __init__(self):
		super(Coba_Tree_Builder,self).__init__(element_factory=Coba_Element_Factory)
		
	def start(self, tag, attrs):
		self._flush()
		self._last = elem = self._factory(self._last,tag, attrs)
		if self._elem:
			self._elem[-1].append(elem)
		self._elem.append(elem)
		self._tail = 0
		return elem

#----------------------------------------------------------------------
def Xml_From_File(file_path):
	parser = etree.XMLParser(target=Coba_Tree_Builder())
	tree = etree.parse(file_path,parser=parser)
	root = tree.getroot()
	return root

#----------------------------------------------------------------------
def Xml_From_Script(script="VGConfigXMLScriptNode"):
	if _maya_check:
		if cmds.objExists(script):
			parser = etree.XMLParser(target=Coba_Tree_Builder())
			xml_text = cmds.scriptNode(script, q=1, bs=1)
		root = etree.fromstring(xml_text, parser=parser)
		return root
	
if __name__ == "__main__":
	data = Xml_From_File(r"U:\dloveridge\Untitled-1.xml")