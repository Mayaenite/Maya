#q_command = "viewType filteredObjectList isFiltered panel control stateString colorMap textureMemoryUsed rendererDeviceName rendererList rendererListUI rendererOverrideList rendererOverrideListUI queryPluginObjects viewObjects cameraSetup objectFilterUI objectFilterList objectFilterListUI".split()
#qe_commands = "mainListConnection forceMainConnection selectionConnection highlightConnection filter docTag camera displayLights bufferMode activeOnly interactive default ignorePanZoom twoSidedLighting".split()
#qe_commands.extend("displayAppearance wireframeOnShaded headsUpDisplay selectionHiliteDisplay useDefaultMaterial useColorIndex userNode wireframeBackingStore useRGBImagePlane".split())
#qe_commands.extend("backfaceCulling xray jointXray activeComponentsXray maxConstantTransparency displayTextures smoothWireframe lineWidth textureMaxSize textureAnisotropic textureSampling".split())
#qe_commands.extend("textureDisplay textureHilight fogging fogSource fogMode fogDensity fogEnd fogStart fogColor shadows rendererName rendererOverrideName colorResolution bumpResolution".split())
#qe_commands.extend("transparencyAlgorithm transpInShadows cullingOverride lowQualityLighting occlusionCulling useBaseRenderer allObjects useInteractiveMode activeView sortTransparent viewSelected".split())
#qe_commands.extend("nurbsCurves nurbsSurfaces polymeshes subdivSurfaces planes lights cameras controlVertices grid hulls joints ikHandles deformers dynamics fluids hairSystems	nCloths nParticles nRigids dynamicConstraints locators manipulators dimensions handles pivots textures strokes".split())
#qe_commands.extend("editorChanged objectFilter objectFilterShowInHUD ".split())
#other = "lockMainConnection unlockMainConnection updateMainConnection cameraName updateColorMode setSelected addSelected removeSelected addObjects noUndo"
import lxml.html
import os
from  string import  Template
get_set_templet = Template('''
\t#----------------------------------------------------------------------
\tdef get_$name(self):
\t\t""""""
\t\treturn self.query($name=True)
\t#----------------------------------------------------------------------
\tdef set_$name(self, value):
\t\t""""""
\t\tself.edit($name=value)
\t#----------------------------------------------------------------------
\t$name = property(get_$name, set_$name)''')
get_templet = Template('''
\t#----------------------------------------------------------------------
\t@property
\tdef $name(self):
\t\t""""""
\t\treturn self.query($name=True)''')
set_templet = Template('''
\t#----------------------------------------------------------------------
\tdef $name(self,value):
\t\t""""""
\t\tself.edit($name=value)''')

class_templet = Template('''
########################################################################
class $class_name(UI_Object.UI):
\t""""""
\t#----------------------------------------------------------------------
\tdef __init__(self, name=None, **kwargs):
\t\tparent = None
\t\tif kwargs.has_key("qtParent"):
\t\t\tparent = kwargs.pop("qtParent")
\t\t\t
\t\tif name == None:
\t\t\tname = cmds.$command_name(**kwargs)
\t\t\tsuper($class_name, self).__init__(name, **dict(qtParent=parent))
\t\t\t
\t\telse:
\t\t\tif cmds.$command_name(name, exists=True):
\t\t\t\tsuper($class_name, self).__init__(name)
\t\t\telse:
\t\t\t\tname = cmds.$command_name(name, **kwargs)
\t\t\t\tsuper($class_name, self).__init__(name, **dict(qtParent=parent))''')
########################################################################
class Modual_Code(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		self.catagories = []
		self.folder = os.path.dirname(__file__)
	#----------------------------------------------------------------------
	def output_Code(self):
		for catagory in self.catagories:
			file_name = catagory.name+".py"
			with file(os.path.join(self.folder,file_name),"w") as f:
				catagory.output_Code(f)
    
	
########################################################################
class Catagory_Modual(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,name):
		"""Constructor"""
		self.name = name
		self.class_data = []
	#----------------------------------------------------------------------
	def output_Code(self,f):
		f.write("import maya.cmds as cmds\n")
		f.write("import UI_Object\n\n")
		for code in self.class_data:
			code.output_Code(f)
########################################################################
class CLASS_DATA(object):
	#----------------------------------------------------------------------
	def __init__(self,name,doc):
		self.name         = name
		self.document     = doc
		self.command_data = []
		
	#----------------------------------------------------------------------
	def output_Code(self,f):
		f.write(class_templet.substitute(class_name=self.name[0].upper()+self.name[1:],command_name=self.name))
		for code in self.command_data:
			f.write(code.output_Code())
########################################################################
class command_data(object):
	#----------------------------------------------------------------------
	def __init__(self,name,input_Type,options,doc):
		self.name       = name
		self.input_type = input_Type
		self.options    = options
		self.document   = doc
	#----------------------------------------------------------------------
	def output_Code(self):
		if "edit" in self.options and "query" in self.options:
			return get_set_templet.substitute(name=self.name)
		if "edit" in self.options and not "query" in self.options:
			return set_templet.substitute(name=self.name)
		if not "edit" in self.options and "query" in self.options:
			return get_templet.substitute(name=self.name)
		else:
			return ""



code_data = Modual_Code()
nav_Windows_Doc  = lxml.html.parse("file:///C:/Program%20Files%20(x86)/Autodesk/Maya2014/docs/Maya2014/en_US/CommandsPython/nav_Windows.html")
nav_Windows_Root = nav_Windows_Doc.getroot()
nav_Windows_Root.make_links_absolute()
for Ui_Catagroy_Header_Elem in nav_Windows_Root.getiterator("h2"):
	Ui_Catagroy_name = Ui_Catagroy_Header_Elem.text_content().strip()
	Ui_Catagroy_name = Ui_Catagroy_name.replace(".","").replace(" ","")
	catagory_data = Catagory_Modual(Ui_Catagroy_name)
	code_data.catagories.append(catagory_data)
	
	for alink in Ui_Catagroy_Header_Elem.getnext().xpath("./tr/td/a"):
		maya_ui_command_file = alink.get("href")
		maya_ui_command_Doc  = lxml.html.parse(maya_ui_command_file)
		maya_ui_command_root = maya_ui_command_Doc.getroot()
		isinstance(maya_ui_command_root,lxml.html.HtmlElement)
		
		command_Elem = maya_ui_command_root.find_class("command")[0]
		command_Header_Elem = command_Elem.find(".//h1")
		command_name = command_Header_Elem.text_content().strip()
		if not "Obsolete" in command_name:
			command_docs = "".join([line for line in command_Elem.xpath("./text()") if len(line.strip())>4]).strip()
			cls_data = CLASS_DATA(command_name, command_docs)
			catagory_data.class_data.append(cls_data)
			
			for item_scan in maya_ui_command_root.getiterator("th"):
				if item_scan.text == "Long name (short name)":
					maya_ui_command_attribute_table = item_scan.getparent().getparent()
					break
		
			for i , code_item in enumerate(maya_ui_command_attribute_table.getiterator(("code"))):
				if i % 2==0 or i == 0:
					name = code_item.text_content().split("(")[0]
				else:
					arg  = code_item.text_content()
					ops  = []
					for img_item in code_item.getparent().getparent().getiterator(("img")):
						ops.append(img_item.attrib.get("alt"))
						
					doc = code_item.getparent().getparent().getnext().text_content().strip()
					data = command_data(name, arg, ops, doc)
					
					cls_data.command_data.append(data)
				
