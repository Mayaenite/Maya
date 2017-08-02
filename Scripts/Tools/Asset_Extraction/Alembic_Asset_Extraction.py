import Scripts.NodeCls.M_Nodes
import Scripts.Global_Constants
import Scripts.General_Maya_Util
import Scripts.OpenMaya_Util_API
reload(Scripts.OpenMaya_Util_API)
import xml.etree.ElementTree as etree
# DisplayLayer   = Scripts.NodeCls.M_Nodes.DisplayLayer
DisplayLayer   = Scripts.OpenMaya_Util_API.DisplayLayer
# SelectionSet   = Scripts.NodeCls.M_Nodes.SelectionSet
SelectionSet   = Scripts.OpenMaya_Util_API.SelectionSet
# MNODE          = Scripts.NodeCls.M_Nodes.MNODE
MNODE          = Scripts.OpenMaya_Util_API.Maya_Node
Nodes          = Scripts.Global_Constants.Nodes
# Shading_Engine = Scripts.NodeCls.M_Nodes.Shading_Engine
Shading_Engine = Scripts.OpenMaya_Util_API.Shading_Engine

_Global_Member_ID_Data =  dict()
from maya import cmds
import json
import timeit
def get_Master_Item():
	cmds.select( cmds.ls(cmds.ls(assemblies=True,long=True),v=True,long=True) )
	cams = cmds.listRelatives(cmds.ls( ca=True,long=True), parent=True, fullPath=True, type="transform")
	cmds.select( cams, deselect=True)
	assemblies =  cmds.selectedNodes()
	largest_child_count = 0
	for item in assemblies:
		children = cmds.listRelatives(item, fullPath=True, allDescendents=True,type="transform")
		if not children is None:
			count = len(children)
			if count > largest_child_count:
				master_item = item
	cmds.select(master_item)

#----------------------------------------------------------------------
def get_Display_Layers():
	"""A List Of All DisplayLayer"""
	return [DisplayLayer(item) for item in cmds.ls(type="displayLayer") if not 'defaultLayer' in item]
#----------------------------------------------------------------------
def get_Shading_Engines():
	return [Shading_Engine(item) for item in cmds.ls(type="shadingEngine") if not "initial" in item]
#----------------------------------------------------------------------
def rename_polySurface_Shapes():
	for i, item in enumerate(cmds.ls("*polySurface*")):
		try:
			cmds.rename(item, "geo_poly_Surface_%i" % i)
		except:
			pass
def rename_bad_unicode():
	active_selection = cmds.ls(sl=True)
	for item in cmds.ls():
		try:
			str(item)
		except:
			if cmds.objExists(item):
				new_name = ""
				item_name = item
				if "|" in item_name:
					item_name = item_name.split("|")[-1]
				for letter in item_name:
					try:
						letter = str(letter)
						new_name += letter
					except UnicodeEncodeError:
						new_name += "_"
				cmds.rename(item, new_name)
	cmds.select(*active_selection)
########################################################################
class Extrator_XML_Data(etree.Element):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, tag_or_element=None, attrib={}):
		"""Constructor"""
		if isinstance(tag_or_element, etree.Element):
			super(Extrator_XML_Data, self).__init__(tag_or_element.tag, attrib=tag_or_element.attrib)
		else:
			tag_or_element = self.__class__.__name__ if tag_or_element is None else tag_or_element
			super(Extrator_XML_Data, self).__init__(tag_or_element, attrib=attrib)

########################################################################
class Extractor_Identifacation_Data(Extrator_XML_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, tag_or_element=None, attrib={}, id_num=None, name="", obj_typ=None):
		"""Constructor"""
		if isinstance(tag_or_element, etree.Element):
			super(Extractor_Identifacation_Data, self).__init__(tag_or_element)
		else:
			super(Extractor_Identifacation_Data, self).__init__(tag_or_element, attrib=attrib)
		
		if self.get("idNum") is None:
			self.set("idNum", str(id_num))
		
		if self.get("name") is None:
			self.set("name", name)
		
		if self.get("objectType") is None:
			self.set("objectType", obj_typ)
	
	@property
	def idNumber(self):
		return int(self.get("idNum"))
	
	@idNumber.setter
	def idNumber(self, value):
		self.set("idNum", str(value))
	
	@property
	def name(self):
		return self.get("name")
	
	@name.setter
	def name(self, value):
		self.set("name", str(value))
	
	@property
	def object_type(self):
		return self.get("objectType")
	
	@object_type.setter
	def object_type(self, value):
		self.set("objectType", str(value))
	
########################################################################
class Member_Assinment_Data(Extractor_Identifacation_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, member=None, tag_or_element=None):
		"""Constructor"""
		global _Global_Member_ID_Data
		if isinstance(tag_or_element, etree.Element):
			super(Member_Assinment_Data, self).__init__(tag_or_element)
			self._node = _Global_Member_ID_Data[int(tag_or_element.get("idNum"))]
		else:
			isinstance(member, MNODE)
			if not member.attributeExists("AW_Extractor_ID"):
				raise LookupError("Object Does Not Contain A Extractor ID")
			
			idnum =  member.plug_access.AW_Extractor_ID.value
			name  =  member.name
			obj_typ = member.objectType
			super(Member_Assinment_Data, self).__init__(tag_or_element=None, attrib={}, id_num=idnum, name=name, obj_typ=obj_typ)

########################################################################
class Extrator_Shading_Engine(Extractor_Identifacation_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, tag_or_element=None, attrib={}, id_num=None, name="", obj_typ=None, ):
		"""Constructor"""
		if isinstance(tag_or_element, etree.Element):
			super(Extrator_Shading_Engine, self).__init__(tag_or_element)
			self._node = Shading_Engine( "extracted_shaders:"+tag_or_element.get("name"))
			for member in tag_or_element.getchildren():
				subelement = Member_Assinment_Data(tag_or_element=member)
				self.append(subelement)
				self._node.addElement(subelement._node)
		else:
			super(Extrator_Shading_Engine, self).__init__(None, attrib, id_num, name, 'shadingEngine')

########################################################################
class Extrator_Shader_List(Extrator_XML_Data):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, tag_or_element=None):
		"""Constructor"""
		if isinstance(tag_or_element, etree.Element):
			super(Extrator_Shader_List, self).__init__(tag_or_element)
			for child in tag_or_element.getchildren():
				subelement = Extrator_Shading_Engine(tag_or_element=child)
		else:
			super(Extrator_Shader_List, self).__init__()
			self.shader_engines = get_Shading_Engines()
			self._active_shader_names = []
		
	def add_assined_materials(self, filter_members=[]):
		self.clear()
		if len(filter_members):
			filter_members =  [item.name for item in filter_members]
		self._active_shader_names = []
		for shader in self.shader_engines:
			section_timer_1 = Section_Timer("Scaning Shader Engines %s For Memeber Assinment" % shader.nice_name)
			isinstance(shader,Shading_Engine)
			if not shader.assined_material == None:
				if len(filter_members):
					for member in shader.members:
						if member.name in filter_members:
							idnum = shader.plug_access.AW_Extractor_ID.value
							name  = shader.name
							subelement = Extrator_Shading_Engine(id_num=idnum, name=name)
							self.append(subelement)
							for member in shader.members:
								if member.name in filter_members:
									subelement.append(Member_Assinment_Data(member=member))
									# print member.name + "Was Not Added To The Shader ssinments Object Does Not Contain A Extractor ID"
							self._active_shader_names.append(shader.name)
							break
				else:
					idnum = shader.plug_access.AW_Extractor_ID.value
					name  = shader.name
					subelement = Extrator_Shading_Engine(id_num=idnum, name=name)
					self.append(subelement)
					for member in shader.members:
						subelement.append(Member_Assinment_Data(member=member))
					self._active_shader_names.append(shader.name)
			section_timer_1.end_timer()
	def export_Shaders(self):
		cmds.select(clear=True)
		for shader in self.shader_engines:
			isinstance(shader,Shading_Engine)
			if not shader.assined_material == None:
				if not shader.assined_material.name == None:
					if shader.name in self._active_shader_names:
						cmds.select(shader.name,ne=True,add=True)
						cmds.select(shader.assined_material.name,add=True)
						items = cmds.listConnections(shader.assined_material.name,destination=False,source=True)
						if not items == None:
							if len(items):
								cmds.select(items,add=True)

		cmds.file("C:/temp/shaders.mb",force=True,op="v=1;",typ="mayaBinary",es=True)
########################################################################
class Extrator_Display_Layer(Extrator_XML_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, tag_or_element=None, attrib={}, id_num=None, name=None, obj_typ=None, node=None):
		"""Constructor"""
		self._node = node
		
		if isinstance(tag_or_element, etree.Element):
			super(Extrator_Display_Layer, self).__init__(tag_or_element)
			for member in tag_or_element.getchildren():
				self.append(Member_Assinment_Data(tag_or_element=member))
			self.create_display_layer()
		else:
			if name is None and self._node is None:
				raise ValueError("Eather A name or the node must be given when creating and instance of this class")
			else:
				if name is None:
					if not isinstance(node, DisplayLayer):
						raise TypeError("The Input node must Be an instance of a DisplayLayer")
					else:
						name = node.name
				elif self._node is None:
					self._node = DisplayLayer(name)
			super(Extrator_Display_Layer, self).__init__()
			self.set("color", str(self._node.color.value))
			self.set("name", self._node.name)
			self.add_assined_members()
			
	def add_assined_members(self):
		data =  {}
		for key, value in self.attrib.iteritems():
			data[key] = value
			
		self.clear()
		
		for key, value in data.iteritems():
			self.set(key, value)
		subelement_list = []
		for member in self._node.members:
			if member.attributeExists("AW_Extractor_ID"):
				isinstance(member, MNODE)
				subelement_list.append(Member_Assinment_Data(member=member, tag_or_element=None))
				
		if len(subelement_list):
			self.extend(subelement_list)
		# self.append(subelement)

	def create_display_layer(self):
			dl = DisplayLayer(self.get("name"))
			dl.color.value = self.color
			for child in self.getchildren():
				dl.addMembers(child._node, noRecurse=True)
			self._node = dl
	@property
	def color(self):
		return int(self.get("color"))
	
	@color.setter
	def color(self, value):
		self.set("color", str(value))

########################################################################
class Extrator_Display_Layer_List(Extrator_XML_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, tag_or_element=None, attrib={}):
		"""Constructor"""
		if isinstance(tag_or_element, etree.Element):
			super(Extrator_Display_Layer_List, self).__init__(tag_or_element)
			self.display_layers  = get_Display_Layers()
			self.clone_Element_Childern(tag_or_element)
		else:
			super(Extrator_Display_Layer_List, self).__init__()
			self.display_layers  = get_Display_Layers()
		
		
	def clone_Element_Childern(self, element):
		isinstance(element, etree.Element)
		for elem in element.getchildren():
			subelement = Extrator_Display_Layer(tag_or_element=elem)
			self.append(subelement)
			
	def add_assined_display_layers(self, member_filter=[]):
		if len(member_filter):
			member_filter = [item.name for item in member_filter]
			subelement_list = []
		for dl in self.display_layers:
			section_timer_1 = Section_Timer("Scaning Display Layer %s For Memeber Assinment" % dl.name)
			isinstance(dl, DisplayLayer)
			if len(member_filter):
				for member in dl.member_names:
					if member in member_filter:
						subelement = Extrator_Display_Layer(node=dl)
						self.append(subelement)
						break
			else:
				subelement = Extrator_Display_Layer(node=dl)
				self.append(subelement)
			section_timer_1.end_timer()
		# self.extend(subelement_list)

class Extractor_Item_Storage_Collector(Extrator_XML_Data):
	"""This Class Is Responsable For Storing The Data That Needs To Be Extracted"""
	def __init__(self, tag_or_element=None, attrib={}):
		"""Constructor"""
		if isinstance(tag_or_element, etree.Element):
			super(Extractor_Item_Storage_Collector, self).__init__(tag_or_element)
			display_Layers  = tag_or_element.find(".//Extrator_Display_Layer_List")
			shading_engines = tag_or_element.find(".//Extrator_Shader_List")
			self.display_Layers  = Extrator_Display_Layer_List(display_Layers)
			self.shading_engines = Extrator_Shader_List(shading_engines)
			self.append(self.display_Layers)
			self.append(self.shading_engines)
			
		else:
			super(Extractor_Item_Storage_Collector, self).__init__()
			timmer_1 =  Section_Timer("Creation Of Extrator_Display_Layer_List")
			self.display_Layers = Extrator_Display_Layer_List()
			timmer_1.end_timer()
			
			timmer_1 =  Section_Timer("Creation Of Extrator_Shader_List")
			self.shading_engines = Extrator_Shader_List()
			timmer_1.end_timer()
			
			self.append(self.display_Layers)
			self.append(self.shading_engines)

class Function_Timer(object):
	def __init__(self, fn):
		self.fn  = fn
		self.result = None
		self.runit()
	def runit(self):
		start_time =  cmds.timerX()
		self.result = self.fn()
		end_time   =  cmds.timerX(startTime=start_time)
		print self.fn.__name__ + " Took %f To Run" % end_time
		
		
class Section_Timer(object):
	def __init__(self, message):
		self.message  = message
		self.start_timer()
	def start_timer(self):
		self._start_time = cmds.timerX()
	def end_timer(self):
		self._end_time = cmds.timerX(startTime=self._start_time)
		print self.message, "Elapsed Time = %f" % self._end_time
	
########################################################################
class Alembic_Asset_Writer(etree.ElementTree):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		full_section_timer = Section_Timer("Extraction Time")
		self._no_error_found = True
		self._get_top_level_node()
		if self._no_error_found:
			print "a"
			Function_Timer(rename_polySurface_Shapes)
			Function_Timer(rename_bad_unicode)
			print "b"
			Function_Timer(self.add_Extractor_Ids)
			print "c"
			Function_Timer(self.unlock_and_break_Attr_connections)
			# section_timer_1 = Section_Timer("Creation Of Extractor_Item_Storage_Collector")
			self.item_Collector = Extractor_Item_Storage_Collector()
			# section_timer_1.end_timer()
			
			section_timer_1 = Section_Timer("adding assined display layers")
			self.item_Collector.display_Layers.add_assined_display_layers(member_filter=[self.top_level_node]+self.top_level_node.allDescendents)
			section_timer_1.end_timer()
			
			section_timer_1 = Section_Timer("adding assined Shading Engines")
			self.item_Collector.shading_engines.add_assined_materials(filter_members=[self.top_level_node]+self.top_level_node.allDescendents)
			section_timer_1.end_timer()
			super(Alembic_Asset_Writer, self).__init__(self.item_Collector)
			
			Function_Timer(self.export_AbcExport)
			Function_Timer(self.item_Collector.shading_engines.export_Shaders)
			self.write('C:/temp/Alembic_Assets_Extractor_Data.xml')
			full_section_timer.end_timer()
	#----------------------------------------------------------------------
	def _get_top_level_node(self):
		""""""
		# Get The Curently Selected Node In The Scene
		active_selection = cmds.ls(sl=True)
		
		# Make Sure Somthing Is Selected
		if not len(active_selection):
			cmds.inViewMessage( amg='<hl>Please Select A Group Node</hl.', fontSize=50, pos='midCenter', fadeInTime=700,fadeStayTime=700,fadeOutTime=700, fade=True )
			self._no_error_found = False
		else:
			top_level_node = active_selection[0]
		
		# Make Sure The Selected Root Node Has A Unique Name
		if top_level_node.startswith("|"): 
			cmds.inViewMessage( amg='The Root Item Selected\n<hl>%s</hl>\nIs Not Unique.' % top_level_node, fontSize=50, pos='midCenter', fadeInTime=700,fadeStayTime=700,fadeOutTime=700, fade=True)
			self._no_error_found = False
		else:
			self.top_level_node      = MNODE(top_level_node)
			self.top_level_node_name = self.top_level_node.nice_name
		
	def unlock_and_break_Attr_connections(self):
		nodes = [self.top_level_node]+self.top_level_node.all_transform_Descendents
		for node in nodes:
			for att in ["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]:
				plg = node.Make_Plug(att)
				plg.unlock()
				try:
					plg.Disconnect_All_Inputs()
				except:
					pass
		for node in cmds.ls("*.intermediateObject"):
			if cmds.getAttr(node):
				cmds.setAttr(node,False)
		for node in cmds.ls("*.inheritsTransform"):
			if not cmds.getAttr(node):
				cmds.setAttr(node,True)

		for node in cmds.ls("*.visibleInReflections"):
			if not cmds.getAttr(node):
				cmds.setAttr(node,True)

		for node in cmds.ls("*.visibleInRefractions"):
			if not cmds.getAttr(node):
				cmds.setAttr(node,True)
		for node in nodes:
			try:
				cmds.makeIdentity(node,apply=True,t=True,r=True,s=True,n=False, pn=True)
			except:
				pass

		for node in nodes:
			try:
				cmds.makeIdentity(node,apply=False,t=True,r=True,s=True,n=False, pn=True)
			except:
				pass
			# cmds.xform(node,cp=True)
	def add_Extractor_Ids(self):
		global id_extractor_counter
		id_extractor_counter = 1
		shader_engines = get_Shading_Engines()
		nodes = [self.top_level_node]+self.top_level_node.allDescendents + shader_engines
		print "Nodes"
		for node in nodes:
			node.unlockNode()
			if not node.attributeExists("AW_Extractor_ID"):
				try:
					cmds.addAttr(node,longName="AW_Extractor_ID",attributeType="long")
					cmds.setAttr(node.name+".AW_Extractor_ID", id_extractor_counter)
					id_extractor_counter += 1
				except:
					print "Did Not Add Id To %s" % node.name
			else:
				cmds.setAttr(node.name+".AW_Extractor_ID", id_extractor_counter)
				id_extractor_counter += 1
			
	def export_AbcExport(self):
		cmds.select(self.top_level_node)
		cmds.AbcExport(jobArg='-frameRange 1 1 -attr AW_Extractor_ID -attr assined_display_layer -uvWrite -dataFormat HDF -eulerFilter -stripNamespaces -root %s -file C:/temp/Extracted.abc' % self.top_level_node.name)

########################################################################
class Alembic_Asset_reader(etree.ElementTree):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		global _Global_Member_ID_Data
		_Global_Member_ID_Data.clear()
		self.import_AbcExport()
		self.import_Shaders()
		
		super(Alembic_Asset_reader, self).__init__(file='C:/temp/Alembic_Assets_Extractor_Data.xml')
		idlist = set()
		
		for member in self.findall(".//Member_Assinment_Data"):
			idlist.add(int(member.get("idNum")))
		idlist =  sorted(list(idlist))
		
		for item in cmds.ls("*.AW_Extractor_ID"):
			plug = Scripts.OpenMaya_Util_API.MPLUG(item)
			if plug.value in idlist:
				idlist.remove(plug.value)
				_Global_Member_ID_Data[plug.value] = plug.node
		root =  self.getroot()
		
		self.item_Collector = Extractor_Item_Storage_Collector(tag_or_element=root)
		
		cmds.namespace(removeNamespace="extracted_shaders",mergeNamespaceWithRoot=True)
	def import_AbcExport(self):
		cmds.AbcImport("C:/temp/Extracted.abc",mode="open")
		# self.top_level_node = MNODE(self.top_level_node_name)
		
	def import_Shaders(self):
		cmds.file("C:/temp/shaders.mb",i=True,type="mayaBinary", ignoreVersion=True, ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")
class Asset_Extractor(object):
	def __init__(self, autofind=False):
		self.rename_polySurface_Shapes()
		if not len(cmds.ls(sl=True)):
			if autofind:
				get_Master_Item()
		if cmds.ls(sl=True)[0].startswith("|"):
			cmds.inViewMessage( amg='The Root Item Selected\n<hl>%s</hl>\nIs Not Unique.' % cmds.ls(sl=True)[0], fontSize=50, pos='midCenter', fadeInTime=700,fadeStayTime=700,fadeOutTime=700, fade=True )
		else:
			self.top_level_node      = MNODE(cmds.ls(sl=True)[0])
			self.top_level_node_name = self.top_level_node.nice_name
			self.dl_dict     = {}
			self.shader_dict = {}
			self.shading_engines = get_Shading_Engines()
			self.display_layers  = get_Display_Layers()
			self.dlnames = [layer.name for layer in self.display_layers]
			self.dlcolors= [layer.color.value for layer in self.display_layers]
			#self.top_level_node.create_String("Display_Layer_Names").value = " ".join(self.dlnames)
			#self.top_level_node.create_String("Master_Node").value = self.top_level_node.nice_name

			self.do_it()
	def rename_polySurface_Shapes(self):
		for i, item in enumerate(cmds.ls("*polySurface*")):
			try:
				cmds.rename(item, "geo_poly_Surface_%i" % i)
			except:
				pass

	def do_it(self):
		nodes = [self.top_level_node]+self.top_level_node.all_transform_Descendents
		count  = len(self.dlnames)
		count += len(self.shading_engines)
		count += len(nodes) * 4
		count += len(cmds.ls("*.inheritsTransform"))
		count += len(cmds.ls("*.visibleInReflections"))
		count += len(cmds.ls("*.visibleInRefractions"))

		self.ProgressBar = Scripts.General_Maya_Util.ProgressBarContext(count, 1 , False)
		with self.ProgressBar:
			self.unlock_and_break_Attr_connections()
			self.add_assined_display_layers()
			self.add_assined_materials()

		self.export_AbcExport()
		self.export_Shaders()
		# self.force_new_scene()
		# self.import_AbcExport()
		# self.import_Shaders()

		# count  = len(self.dlnames)
		# count += len(self.shader_dict.keys())
		# self.ProgressBar = Scripts.General_Maya_Util.ProgressBarContext(count, 1 , False)
		# with self.ProgressBar:
			# self.remake_display_layers()
			# self.reasine_shaders()
		#self.reassine_Custom_Attr_Values()

	def add_assined_display_layers(self):
		for dl in self.display_layers:
			isinstance(dl, DisplayLayer)
			self.ProgressBar.increment()
			id_list =  []
			for member in dl.members:
				if member.attributeExists("AW_Extractor_ID"):
					id_list.append(cmds.getAttr(member.name+".AW_Extractor_ID"))
				else:
					raise LookupError("Was Not Able To Get The Extraction ID For The Node Named %s" % member.name)
			self.dl_dict[dl.name]= dict(names=dl.member_names, ids=id_list)

	def reassine_Custom_Attr_Values(self):
		# Scan Through All Root Level Tranform Nodes
		tags = "BodyType Engine Axle Drive Grade Transmission Model Intake Zone Equipment OptionCode_1 OptionCode_2 OptionCode_3 OptionCode_4 OptionCode_5 Shader".split()
		for tag in tags:
			for obj in cmds.ls('*.'+tag):
				val = cmds.getAttr(obj)
				cmds.setAttr(obj, " "+val,type="string")

	def add_assined_materials(self):
		for shader in self.shading_engines:
			self.ProgressBar.increment()
			isinstance(shader,Shading_Engine)
			id_list = []
			if not shader.assined_material == None:
				for member in shader.members:
					self.shader_dict[shader.name]=shader.memberNames

	def remake_display_layers(self):
		for name,color in zip(self.dlnames,self.dlcolors):
			dl = DisplayLayer(name)
			dl.color.value = color
			self.ProgressBar.increment()
			if name in self.dl_dict.keys():
				dl.addMembers(self.dl_dict[name], noRecurse=True)

	def reasine_shaders(self):
		for shader in self.shader_dict.keys():
			self.ProgressBar.increment()
			shader_name = "extracted_shaders:"+shader
			if cmds.objExists(shader_name):
				members = self.shader_dict[shader]
				SG = Shading_Engine(shader_name)
				SG.addElement(members)

	def export_Shaders(self):
		cmds.select(clear=True)
		for shader in self.shading_engines:
			isinstance(shader,Shading_Engine)
			cmds.select(shader.name,ne=True,add=True)
			if not shader.assined_material == None:
				if not shader.assined_material.name == None:
					cmds.select(shader.assined_material.name,add=True)
					items = cmds.listConnections(shader.assined_material.name,destination=False,source=True)
					if not items == None:
						if len(items):
							cmds.select(items,add=True)

		cmds.file("C:/temp/shaders.mb",force=True,op="v=1;",typ="mayaBinary",es=True)
		
	def export_AbcExport(self):
		cmds.select(self.top_level_node)
		cmds.AbcExport(jobArg='-frameRange 1 1 -attr AW_Extractor_ID -attr assined_display_layer -uvWrite -worldSpace -dataFormat HDF -eulerFilter -stripNamespaces -root %s -file C:/temp/Extracted.abc' % self.top_level_node.name)
		
	def import_Shaders(self):
		cmds.file("C:/temp/shaders.mb",i=True,type="mayaBinary",ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")

	def force_new_scene(self):
		cmds.file(force=True,new=True)

	def import_AbcExport(self):
		cmds.AbcImport("C:/temp/Extracted.abc",mode="open")
		self.top_level_node = MNODE(self.top_level_node_name)

	def unlock_and_break_Attr_connections(self):
		nodes = [self.top_level_node]+self.top_level_node.all_transform_Descendents
		for node in nodes:
			self.ProgressBar.increment()
			for att in ["tx","ty","tz","rx","ry","rz","sx","sy","sz"]:
				plg = node.Make_Plug(att)
				plg.unlock
				try:
					plg.Disconnect_All_Inputs()
				except:
					pass

		for node in cmds.ls("*.inheritsTransform"):
			self.ProgressBar.increment()
			if not cmds.getAttr(node):
				cmds.setAttr(node,True)

		for node in cmds.ls("*.visibleInReflections"):
			self.ProgressBar.increment()
			if not cmds.getAttr(node):
				cmds.setAttr(node,True)

		for node in cmds.ls("*.visibleInRefractions"):
			self.ProgressBar.increment()
			if not cmds.getAttr(node):
				cmds.setAttr(node,True)

		for node in nodes:
			self.ProgressBar.increment()
			cmds.makeIdentity(node,apply=True,t=True,r=True,s=True,n=False, pn=True)

		for node in nodes:
			self.ProgressBar.increment()
			cmds.makeIdentity(node,apply=False,t=True,r=True,s=True,n=False, pn=True)
			# cmds.xform(node,cp=True)

		counter = 1
		nodes = [self.top_level_node]+self.top_level_node.top_level_node.allDescendents
		for node in nodes:
			self.ProgressBar.increment()
			if not node.attributeExists("AW_Extractor_ID"):
				cmds.addAttr(node,longName="AW_Extractor_ID",attributeType="long")
			cmds.setAttr(node.name+".AW_Extractor_ID", counter)
			counter += 1
