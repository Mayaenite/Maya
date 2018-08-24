import os
import QT
import json
import maya.cmds as cmds
import maya.mel
import pymel.core as pm
import Scripts.NodeCls.M_Nodes
import Scripts.Global_Constants
import Scripts.General_Maya_Util
import Scripts.OpenMaya_Util_API
DisplayLayer   = Scripts.OpenMaya_Util_API.DisplayLayer
SelectionSet   = Scripts.OpenMaya_Util_API.SelectionSet
MNODE          = Scripts.OpenMaya_Util_API.Maya_Node
Nodes          = Scripts.Global_Constants.Nodes
Shading_Engine = Scripts.OpenMaya_Util_API.Shading_Engine
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
_Global_Member_ID_Data = dict()


#----------------------------------------------------------------------
def kill_hyperShadePanel():
	""""""
	maya.mel.eval("closeHypershade")

def clean_maya_shader_file(path):
	with file(path,"r") as f:
		lines = f.readlines()
	new_lines = []
	for line in lines:
		if not '"Seamour"' in line and not '"ToolBox"' in line and not '"mayaswitchmtl2013"' in line and not '"Stitch"' in line:
			new_lines.append(line)
	with file(path,"w") as f:
		f.writelines(new_lines)

#----------------------------------------------------------------------
def remove_All_Render_Layers():
	cmds.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
	cmds.delete([layer for layer in cmds.ls(type="renderLayer") if not layer == "defaultRenderLayer"])


#----------------------------------------------------------------------
def perform_CleanUp():
	""""""
	maya.mel.eval('source "C:/Program Files/Autodesk/Maya2018/scripts/startup/cleanUpScene.mel"')
	for cmd in ['deleteUnusedNurbsSurfaces','deleteUnusedConstraints','deleteUnusedPairBlends','deleteUnusedLocators' ,'deleteUnusedSets' ,'deleteUnusedExpressions' ,'deleteUnknownNodes','deleteUnusedDeformers','deleteInvalidNurbs(0)','MLdeleteUnused' ,'RNdeleteUnused' ,'deleteUnusedBrushes' ,'deleteUnusedCommon( "groupId", 0, "")']:
		maya.mel.eval(cmd)


#----------------------------------------------------------------------
def check_If_Shading_Engine_Contains_Face_Assignments(engine,items,log_text):
	for item in items:
		if ".f" in item:
			log_text.insertHtml('<html><head/><body><p><span style=" font-size:8.25pt; color:#ff0000;">Warning:</span><span style=" font-size:8.25pt; color:#ffffff;"> Face Assinments Found On </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{} </span><span style=" font-size:8.25pt; color:#ffffff;">From </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{}<br/></span></p></body></html>'.format(engine,item))	
			
#----------------------------------------------------------------------
def Shader_Overides_To_Master_Layer(layer,log_text):
	#----------------------------------------------------------------------
	def get_ShadingEngine_dict():
		res    = dict()
		shading_Engines = cmds.ls(type="shadingEngine")
		for engine in shading_Engines:
			items = cmds.ls(cmds.sets(engine,q=True))
			check_If_Shading_Engine_Contains_Face_Assignments(engine, items, log_text)
			items = cmds.ls(items,objectsOnly=True)
			res[engine] = items
		return res
	#----------------------------------------------------------------------
	def apply_Shading_Engine_dict(data):
		for sg,items in data.iteritems():
			if len(items):
				cmds.sets(items,edit=True,forceElement=sg)
	
	cmds.editRenderLayerGlobals(currentRenderLayer=layer)
	cmds.refresh(f=True)
	overides_assignments = get_ShadingEngine_dict()
	cmds.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
	cmds.refresh(f=True)
	apply_Shading_Engine_dict(overides_assignments)

#----------------------------------------------------------------------
def replace_all_shaders_with_lambers(log_text,use_layer=False):
	#----------------------------------------------------------------------
	def get_ShadingNodes():
		res    = []
		shading_Engines = [item for item in cmds.ls(type="shadingEngine") if not item.startswith("initial")]
		for engine in shading_Engines:
			shader = cmds.listConnections(engine+".surfaceShader",d=True)
			if not shader == None:
				if len(shader):
					shader = shader[0]
					res.append((shader,engine))
		return res
	#----------------------------------------------------------------------
	def shader_To_Lamber(shader,engine):
		cmds.lockNode(shader,lock=False)
		cmds.lockNode(engine,lock=False)
		old_shader = cmds.rename(shader,shader+"_old")
		old_engine = cmds.rename(engine,engine+"_old")
	
		shader = cmds.shadingNode("lambert",asShader=True,name=shader)
		engine = cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name=shader+"SG")
		cmds.connectAttr(shader+".outColor",engine+".surfaceShader",force=True)
		try:
			cr,cb,cg = cmds.getAttr(old_shader+".color")[0]
			tr,tb,tg = cmds.getAttr(old_shader+".transparency")[0]
			cmds.setAttr(shader+".color",cr,cb,cg, type="double3")
			cmds.setAttr(shader+".transparency",tr,tb,tg, type="double3")
		except:
			pass
		items = cmds.ls(cmds.sets(old_engine,q=True))
		check_If_Shading_Engine_Contains_Face_Assignments(old_engine,items,log_text)
		items = cmds.ls(items,objectsOnly=True)
		if len(items):
			cmds.sets(items,edit=True,forceElement=engine)

	if use_layer:
		if cmds.objExists(use_layer) and cmds.objectType(use_layer)=="renderLayer":
			Shader_Overides_To_Master_Layer(log_text,use_layer)
	for item in get_ShadingNodes():
		shader_To_Lamber(item[0],item[1])


######################################################################## EXTRATORS

########################################################################
class Node_Extrator_Data(dict):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,node):
		"""Constructor"""
		isinstance(node,MNODE)
		super(Node_Extrator_Data,self).__init__()
		self["objectType"] = node.objectType
########################################################################
class Extrator_Display_Layer(Node_Extrator_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,node):
		"""Constructor"""
		isinstance(node,DisplayLayer)
		super(Extrator_Display_Layer,self).__init__(node)
		self["name"] = node.name
		self["color"] = node.color.value
		assignment_ids = []
		for member in node.members:
			if member.attributeExists("AW_Extractor_ID"):
				isinstance(member, MNODE)
				plug = member.Make_Plug("AW_Extractor_ID")
				assignment_ids.append(plug.value)
			else:
				raise AttributeError("Could Not Find AW_Extractor_ID for node {}".format(member.name))
		self["assignment_ids"]=assignment_ids
########################################################################
class Extrator_Shader_Engine(Node_Extrator_Data):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,node):
		"""Constructor"""
		isinstance(node,Shading_Engine)
		super(Extrator_Shader_Engine,self).__init__(node)
		self["name"] = node.name
		if not node.attributeExists("AW_Extractor_ID"):
			raise AttributeError("Could Not Find AW_Extractor_ID for node {}".format(node.name))
		self["idnum"]  = node.Make_Plug("AW_Extractor_ID").value
		assignment_ids = []
		if not node.assined_material == None:
			for member in node.members:
				if member.attributeExists("AW_Extractor_ID"):
					isinstance(member, MNODE)
					plug = member.Make_Plug("AW_Extractor_ID")
					assignment_ids.append(plug.value)
				else:
					raise AttributeError("Could Not Find AW_Extractor_ID for node {}".format(member.name))
		self["assignment_ids"]=assignment_ids
########################################################################
class Extrator_Shader_List(list):
	""""""

	#----------------------------------------------------------------------
	def __init__(self,shaders,progressBar):
		"""Constructor"""
		super(Extrator_Shader_List,self).__init__()
		for shader in shaders:
			isinstance(shader,Shading_Engine)
			data = Extrator_Shader_Engine(shader)
			self.append(data)
			progressBar.add_Tick()
########################################################################
class Extrator_Display_Layer_List(list):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,layers,progressBar):
		"""Constructor"""
		super(Extrator_Display_Layer_List,self).__init__()
		for dl in layers:
			data = Extrator_Display_Layer(dl)
			self.append(data)
			progressBar.add_Tick()
########################################################################
class Extractor_Collector(dict):
	"""This Class Is Responsable For Storing The Data That Needs To Be Extracted"""
	def __init__(self,shaders,shaders_progressBar,layers,layers_progressBar):
		"""Constructor"""
		super(Extractor_Collector, self).__init__()
		display_Layers = Extrator_Display_Layer_List(layers,layers_progressBar)
		shading_engines = Extrator_Shader_List(shaders,shaders_progressBar)
		self["display_Layers"]=display_Layers
		self["shading_engines"]=shading_engines

######################################################################## CONSTRUCTORS
########################################################################
class Constructor_Display_Layer(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,data):
		"""Constructor"""
		global _Global_Member_ID_Data
		self.name = data["name"]
		self.color = data["color"]
		self.assignment_ids = data["assignment_ids"]
		self.assignment_nodes = []
		for idnum in self.assignment_ids:
			node = _Global_Member_ID_Data.get(idnum)
			self.assignment_nodes.append(node)
		self.node = DisplayLayer(self.name)
		self.node.color.value = self.color
		self.node.addMembers(self.assignment_nodes, noRecurse=True)
########################################################################
class Constructor_Shader_Engine(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,data):
		"""Constructor"""
		global _Global_Member_ID_Data
		self.name = data["name"]
		self.idnum  = data["idnum"]
		self.assignment_ids = data["assignment_ids"]
		self.node = Shading_Engine(_Global_Member_ID_Data.get(self.idnum).name)
		isinstance(self.node,Shading_Engine)
		self.assignment_nodes = []
		for idnum in self.assignment_ids:
			node = _Global_Member_ID_Data.get(idnum)
			self.assignment_nodes.append(node)
		self.node.addElement(self.assignment_nodes)
########################################################################
class Constructor_Display_Layer_List(list):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,layers):
		"""Constructor"""
		super(Constructor_Display_Layer_List,self).__init__()
		for layer in layers:
			data = Constructor_Display_Layer(layer)
			self.append(data)
########################################################################
class Constructor_Shader_Engine_List(list):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,shaders):
		"""Constructor"""
		super(Constructor_Shader_Engine_List,self).__init__()
		for shader in shaders:
			data = Constructor_Shader_Engine(shader)
			self.append(data)
########################################################################
class Constructor_Collector(object):
	"""This Class Is Responsable For Storing The Data That Needs To Be Extracted"""
	def __init__(self,data):
		"""Constructor"""
		display_Layers = data["display_Layers"]
		shading_engines = data["shading_engines"]
		self.layers = Constructor_Display_Layer_List(display_Layers)
		self.shaders = Constructor_Shader_Engine_List(shading_engines)
######################################################################## READERS AND WRITER
########################################################################
class Alembic_Asset_Writer(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,gui_widget):
		"""Constructor"""
		self.gui_widget = gui_widget
		isinstance(self.gui_widget,Alembic_Asset_Extraction_GUI)


		self.all_top_level_node_transform_descendent_node_names        = []
		self.all_top_level_node_transform_descendent_node_names_count  = 0
		
		self.all_transform_nodes       = []
		self.all_transform_node_count  = 0
		
		self.all_top_level_node_geometry_descendent_node_names   = []
		self.all_top_level_node_geometry_descendent_node_names_count  = 0
		
		self.all_top_level_node_geometry_descendent_nodes        = []
		self.all_top_level_node_geometry_descendent_nodes_count  = 0
		
		self.all_node_names_to_be_taged  = []
		self.all_node_names_to_be_taged_count = 0
		
		self.all_shader_engine_names  = [item for item in cmds.ls(type="shadingEngine") if not "initial" in item]
		self.all_shader_engine_names_count = len(self.all_shader_engine_names)
		
		self._all_shader_engines_dict = dict()
		
		self.all_nodes_to_be_taged       = []
		self.all_nodes_to_be_taged_count = 0
		
		self.polySurface_node_names               = []
		self.polySurface_node_name_count          = 0
		
		self.active_shaders = []
		self.active_shader_count = 0
		
		self.active_layers = []
		self.active_layer_count = 0
		
		self.bad_geometry_node_names = []
		self.bad_geometry_node_names_count = 0
		
		self.bad_unicode_node_names = []
		self.bad_unicode_node_name_count = 0
		
		self.bad_intermediate_object_nodes = []
		self.bad_intermediate_object_node_count = 0
		
		self.bad_inherit_transform_plugs = []
		self.bad_inherit_transform_plug_count = 0
		
		self.bad_visible_in_reflection_plugs = []
		self.bad_visible_in_reflection_plug_count = 0
		
		self.bad_visible_in_refraction_plugs = []
		self.bad_visible_in_refraction_plug_count = 0
		
	#----------------------------------------------------------------------
	def set_Top_Level_Node(self,top_level_node):
		""""""
		if top_level_node != None and cmds.objExists(top_level_node) and len(cmds.ls(top_level_node))==1:
			self.top_level_node                                           = MNODE(top_level_node)
			self.top_level_node_nice_name                                 = self.top_level_node.nice_name
			return True
		else:
			return False
	#----------------------------------------------------------------------
	def scan_Top_Level_Node(self):
		""""""
		self.RUN_SCANS()
	#----------------------------------------------------------------------
	def Run_Export(self):
		""""""
		self.APPLY_FIXES()
		self.gui_widget.collecting_Display_Layer_Assignments_ProgressBar.setMaximum(self.active_layer_count)
		self.gui_widget.collecting_Shader_Assignments_ProgressBar.setMaximum(self.active_shader_count)
		self.item_Collector = Extractor_Collector(self.active_shaders,self.gui_widget.collecting_Shader_Assignments_ProgressBar,self.active_layers,self.gui_widget.collecting_Display_Layer_Assignments_ProgressBar)
		self.export_AbcExport()
		self.export_Shaders()
		self.save_json_file()
	#----------------------------------------------------------------------
	def save_json_file(self):
		""""""
		with file('C:/temp/Alembic_Assets_Extractor_Data.json','w') as f:
			self.item_Collector["shader_file_is_ascii"] = self._shader_file_is_ascii
			json.dump(self.item_Collector, f, indent=4, sort_keys=True)
	#----------------------------------------------------------------------
	def find_Most_Likely_Master_Item(self):
		active_selection = cmds.ls(sl=True)
		cmds.select( cmds.ls(cmds.ls(assemblies=True,long=True),v=True,long=True) )
		cams = cmds.listRelatives(cmds.ls( cameras=True,long=True), parent=True, fullPath=True, type="transform")
		cmds.select( cams, deselect=True)
		assemblies =  cmds.selectedNodes()
		largest_child_count = 0
		for item in assemblies:
			children = cmds.listRelatives(item, fullPath=True, allDescendents=True,type="transform")
			if not children is None:
				count = len(children)
				if count > largest_child_count:
					master_item = item
		cmds.select( active_selection )
		return master_item
	#----------------------------------------------------------------------
	def get_top_level_node(self):
		""""""
		# Get The Curently Selected Node In The Scene
		active_selection = cmds.ls(sl=True)

		# Make Sure Somthing Is Selected
		if not len(active_selection):
			most_likely = self.find_Most_Likely_Master_Item()
			if most_likely is not None:
				cmds.inViewMessage( amg='<hl>No Active Selection Selecting Most Likly Group</hl.', fontSize=50, pos='midCenter', fadeInTime=700,fadeStayTime=700,fadeOutTime=700, fade=True )
				cmds.select(self.find_Most_Likely_Master_Item())
				top_level_node = most_likely
		else:
			top_level_node = active_selection[0]

		# Make Sure The Selected Root Node Has A Unique Name
		if top_level_node.startswith("|"): 
			cmds.inViewMessage( amg='The Root Item Selected\n<hl>%s</hl>\nIs Not Unique.' % top_level_node, fontSize=50, pos='midCenter', fadeInTime=700,fadeStayTime=700,fadeOutTime=700, fade=True)
			self._no_error_found = False
		else:
			self.top_level_node      = MNODE(top_level_node)
			self.top_level_node_nice_name = self.top_level_node.nice_name
	#----------------------------------------------------------------------
	def RUN_SCANS(self):
		""""""
		#----------------------------------------------------------------------
		def scan_For_Shape_Nodes_With_No_Geo():
			progressBar = self.gui_widget.shapeNodesWithNoGeometryprogressBar
			progressBar.setMaximum(self.all_top_level_node_geometry_descendent_node_names_count)
			
			self.bad_geometry_node_names = []
			self.all_top_level_node_geometry_descendent_nodes = []
			temp = self.all_top_level_node_geometry_descendent_node_names[::]
			for item in temp:
				try:
					item_node = MNODE(item)
					self.all_top_level_node_geometry_descendent_nodes.append(item_node)
				except StandardError:
					self.bad_geometry_node_names.append(item)
					self.all_top_level_node_geometry_descendent_node_names.remove(item)
				progressBar.add_Tick()
			
			self.bad_geometry_node_names_count = len(self.bad_geometry_node_names)
			self.all_top_level_node_geometry_descendent_nodes_count = len(self.all_top_level_node_geometry_descendent_nodes)
			self.gui_widget.shapeNodesWithNoGeometrySpinBox.setValue(self.bad_geometry_node_names_count)
		#----------------------------------------------------------------------
		def scan_All_Top_Level_Node_Descendents():
			""""""
			progressBar = self.gui_widget.all_descendents_scan_progressBar
			
			self._all_shader_engines_dict = dict()
			
			progressBar.setMaximum(self.all_top_level_node_transform_descendent_node_names_count + self.all_shader_engine_names_count)
			
			self.all_transform_nodes = [self.top_level_node]
			all_shader_engine_nodes  = []
			all_shape_nodes = []
			
			for child in self.all_top_level_node_transform_descendent_node_names:
				self.all_transform_nodes.append(MNODE(child))
				progressBar.add_Tick()
			
			for item in self.all_shader_engine_names:
				item_node = Shading_Engine(item)
				all_shader_engine_nodes.append(item_node)
				self._all_shader_engines_dict[item]=item_node
				progressBar.add_Tick()
			
			self.all_transform_node_count  = len(self.all_transform_nodes)
			
			self.all_nodes_to_be_taged       = self.all_transform_nodes + self.all_top_level_node_geometry_descendent_nodes + all_shader_engine_nodes
			self.all_nodes_to_be_taged_count = len(self.all_nodes_to_be_taged)
			
			self.gui_widget.Number_Of_Transfoms_To_Be_Exported_SpinBox.setValue(self.all_transform_node_count)
		#----------------------------------------------------------------------
		def scan_Bad_PolySurface_Node_Names():
			""""""
			self.polySurface_node_names               = cmds.ls("*polySurface*")
			self.polySurface_node_name_count          = len(self.polySurface_node_names)
			self.gui_widget.illegalPolySurfaceNameLengthCountSpinBox.setValue(self.polySurface_node_name_count)
		#----------------------------------------------------------------------
		def scan_Active_Shader_Engines():
			""""""
			progressBar = self.gui_widget.exportShaderCountprogressBar
			items = cmds.listConnections(cmds.listRelatives(cmds.listRelatives(self.top_level_node.name,fullPath=True, allDescendents=True, type="transform"), shapes=True, fullPath=True),t="shadingEngine")
			if items is not None:
				items = list(set(items))
			else:
				items = []
			if "initialShadingGroup" in items:
				items.remove("initialShadingGroup")
			progressBar.setMaximum(len(items))
			res = []
			for item in items:
				if not item in self._all_shader_engines_dict.keys():
					item_node = Shading_Engine(item)
					self._all_shader_engines_dict[item] = item_node
				res.append(self._all_shader_engines_dict[item])
				progressBar.add_Tick()
			self.active_shaders = res
			self.active_shader_count = len(res)
			self.gui_widget.exportShaderCountSpinBox.setValue(self.active_shader_count)
		#----------------------------------------------------------------------
		def scan_Active_Display_Layers():
			""""""
			progressBar = self.gui_widget.exportLayerCountprogressBar
			scan = []
			scanA = cmds.listConnections(self.top_level_node.name,t="displayLayer")
			if scanA is not None:
				scan.extend(scanA)
				
			scanB = cmds.listConnections(cmds.listRelatives(self.top_level_node.name,fullPath=True, allDescendents=True),t="displayLayer")
			
			if scanB is not None:
				scan.extend(scanB)
			
			items = list(set(scan))
			
			if 'defaultLayer' in items:
				items.remove('defaultLayer')
			
			progressBar.setMaximum(len(items))
			res = []
			for item in items:
				res.append(DisplayLayer(item))
				progressBar.add_Tick()
			self.active_layers = res
			self.active_layer_count = len(items)
			self.gui_widget.exportLayerCountSpinBox.setValue(self.active_layer_count)
		#----------------------------------------------------------------------
		def scan_Bad_Unicode_Node_Names():
			""""""
			res = []
			progressBar = self.gui_widget.badUnicodeNameCountprogressBar
			all_items = cmds.ls()
			progressBar.setMaximum(len(all_items))
			for item in all_items:
				try:
					str(item)
				except:
					if cmds.objExists(item):
						res.append(item)
						
				progressBar.add_Tick()
				
			self.bad_unicode_node_names = res
			self.bad_unicode_node_name_count = len(res)
			self.gui_widget.badUnicodeNameCountSpinBox.setValue(self.bad_unicode_node_name_count)
		#----------------------------------------------------------------------
		def scan_Bad_Intermediate_Objects():
			""""""
			progressBar = self.gui_widget.intermediateObjectCountprogressBar
			res = []
			all_items = cmds.ls("*.intermediateObject")
			progressBar.setMaximum(len(all_items))
			
			for node_attr in all_items:
				if cmds.getAttr(node_attr):
					node = node_attr.split(".")[0]
					if cmds.objectType(node,isType="mesh"):
						res.append(node)
				progressBar.add_Tick()
			self.gui_widget.intermediateObjectCountSpinBox.setValue(len(res))
			self.bad_intermediate_object_nodes = res
			self.bad_intermediate_object_node_count = len(res)
			self.gui_widget.intermediateObjectCountSpinBox.setValue(self.bad_intermediate_object_node_count)
		#----------------------------------------------------------------------
		def scan_Bad_Inherits_Transform_Plugs():
			""""""
			progressBar = self.gui_widget.brokenTransformInheritanceprogressBar
			res = []
			items = cmds.ls("*.inheritsTransform")
			progressBar.setMaximum(len(items))
			for node in items:
				if not cmds.getAttr(node):
					res.append(node)
				progressBar.add_Tick()
			self.bad_inherit_transform_plugs = res
			self.bad_inherit_transform_plug_count = len(res)
			self.gui_widget.brokenTransformInheritanceSpinBox.setValue(self.bad_inherit_transform_plug_count)
		#----------------------------------------------------------------------
		def scan_Bad_Visible_In_Reflection_Plugs():
			""""""
			res = []
			progressBar = self.gui_widget.incorrectVisibleInReflectionPlugsprogressBar
			items = cmds.ls("*.visibleInReflections")
			progressBar.setMaximum(len(items))
			for node in items:
				if not cmds.getAttr(node):
					res.append(node)
				progressBar.add_Tick()
			self.bad_visible_in_reflection_plugs = res
			self.bad_visible_in_reflection_plug_count = len(res)
			self.gui_widget.incorrectVisibleInReflectionPlugsSpinBox.setValue(self.bad_visible_in_reflection_plug_count)
		#----------------------------------------------------------------------
		def scan_Bad_Visible_In_Refraction_Plugs():
			""""""
			res = []
			progressBar = self.gui_widget.incorrectVisibleInRefractionPlugsprogressBar
			items = cmds.ls("*.visibleInRefractions")
			progressBar.setMaximum(len(items))
			for node in items:
				if not cmds.getAttr(node):
					res.append(node)
				progressBar.add_Tick()
			self.bad_visible_in_refraction_plugs = res
			self.bad_visible_in_refraction_plug_count = len(res)
			self.gui_widget.incorrectVisibleInRefractionPlugsSpinBox.setValue(self.bad_visible_in_refraction_plug_count)
		
		self.all_top_level_node_transform_descendent_node_names       = cmds.listRelatives(self.top_level_node.name, allDescendents=True, path=True, type='transform')
		self.all_top_level_node_transform_descendent_node_names_count = len(self.all_top_level_node_transform_descendent_node_names)
		
		self.all_top_level_node_geometry_descendent_node_names       =  cmds.ls(cmds.listRelatives(self.top_level_node.name, allDescendents=True, path=True),geometry=True,l=True)
		self.all_top_level_node_geometry_descendent_node_names_count = len(self.all_top_level_node_geometry_descendent_node_names)
			
		self.all_shader_engine_names  = [item for item in cmds.ls(type="shadingEngine") if not "initial" in item]
		self.all_shader_engine_names_count = len(self.all_shader_engine_names)
		
		scan_For_Shape_Nodes_With_No_Geo()
		scan_All_Top_Level_Node_Descendents()
		scan_Bad_PolySurface_Node_Names()
		scan_Active_Shader_Engines()
		scan_Active_Display_Layers()
		scan_Bad_Intermediate_Objects()
		scan_Bad_Unicode_Node_Names()
		scan_Bad_Inherits_Transform_Plugs()
		scan_Bad_Visible_In_Reflection_Plugs()
		scan_Bad_Visible_In_Refraction_Plugs()
	#----------------------------------------------------------------------
	def APPLY_FIXES(self):
		""""""
		#----------------------------------------------------------------------
		def remove_Shapes_With_No_Geometry():
			""""""
			progressBar = self.gui_widget.deletingAllShapesWithNoGeometry_ProgressBar
			if self.bad_geometry_node_names_count:
				progressBar.setMaximum(self.bad_geometry_node_names_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
				
			for item in self.bad_geometry_node_names:
				cmds.delete(item)
				progressBar.add_Tick()
		#----------------------------------------------------------------------
		def fix_PolySurface_Names():
			""""""
			progressBar = self.gui_widget.renaming_PolySurface_Shapes_ProgressBar
			progressBar.setMaximum(self.polySurface_node_name_count)
			if self.polySurface_node_name_count:
				progressBar.setMaximum(self.polySurface_node_name_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
			
			for i, item in enumerate(self.polySurface_node_names):
				try:
					cmds.rename(item, "geo_poly_Surface_%i" % i)
				except:
					pass
				progressBar.add_Tick()
		#----------------------------------------------------------------------
		def fix_Bad_Unicode_Names():
			progressBar = self.gui_widget.correctingInvalidUnicodeNamesProgressBar
			if self.bad_unicode_node_name_count:
				progressBar.setMaximum(self.bad_unicode_node_name_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
				
			for item in self.bad_unicode_node_names:
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
				progressBar.add_Tick()
		#----------------------------------------------------------------------
		def add_Extractor_Id_Tags():
			global id_extractor_counter
			id_extractor_counter = 1
			progressBar = self.gui_widget.apply_Extractor_Ids_ProgressBar
			progressBar.setMaximum(self.all_nodes_to_be_taged_count)
			for node in self.all_nodes_to_be_taged:
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
				progressBar.add_Tick()
		#----------------------------------------------------------------------		
		def fix_Attribute_Connections():
			progressBar = self.gui_widget.unlocking_And_Break_Attr_Connections_ProgressBar
			progressBar.setMaximum(self.all_transform_node_count*9)
			for node in self.all_transform_nodes:
				try:
					cmds.lockNode(node,lock=False)
				except:
					pass
				for att in ["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]:
					attr = node.name+"."+att
					if cmds.getAttr(attr,lock=True ):
						cmds.setAttr(attr,lock=False)
						# try:
							# cmds.setAttr(attr,lock=False)
						# except:
							# plg = node.Make_Plug(att)
							# plg.unlock()
					conns = cmds.listConnections(attr,d=True,plugs=True)
					if not conns == None:
						for con in conns:
							try:
								cmds.disconnectAttr(con,attr)
							except:
								self.gui_widget.Extraction_Log_Text.insertHtml('<html><head/><body><p><span style=" font-size:8.25pt; color:#ff0000;">Warning:</span><span style=" font-size:8.25pt; color:#ffffff;"> Could Not Dissconnect </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{} </span><span style=" font-size:8.25pt; color:#ffffff;">From </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{}<br/></span></p></body></html>'.format(con,attr))
								# print "Could Not Dissconect {} from {}".format(con,attr)
								continue
						# try:
							# plg.Disconnect_All_Inputs()
						# except:
							# pass
					progressBar.add_Tick()
		#----------------------------------------------------------------------
		def remove_Intermediate_Objects():
			""""""
			progressBar = self.gui_widget.removing_Intermediate_Objects_ProgressBar
			if self.bad_intermediate_object_node_count:
				progressBar.setMaximum(self.bad_intermediate_object_node_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
			if self.bad_intermediate_object_node_count:
				for item in self.bad_intermediate_object_nodes:
					try:
						cmds.delete(item)
					except:
						pass
					progressBar.add_Tick()
		#----------------------------------------------------------------------
		def fix_Bad_Inherit_Transform_Plugs():
			""""""
			progressBar = self.gui_widget.fix_Inherit_Transform_ProgressBar
			if self.bad_inherit_transform_plug_count:
				progressBar.setMaximum(self.bad_inherit_transform_plug_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
			for node in self.bad_inherit_transform_plugs:
				if not cmds.getAttr(node):
					cmds.setAttr(node,True)
				progressBar.add_Tick()
		#----------------------------------------------------------------------
		def fix_Bad_Visible_In_Reflection_Plugs():
			""""""
			progressBar = self.gui_widget.fix_VisibleIn_Reflections_ProgressBar
			if self.bad_visible_in_reflection_plug_count:
				progressBar.setMaximum(self.bad_visible_in_reflection_plug_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
			
			for node in self.bad_visible_in_reflection_plugs:
				cmds.setAttr(node,True)
				progressBar.add_Tick()
		#----------------------------------------------------------------------
		def fix_Visible_In_Refraction_Plugs():
			""""""
			progressBar = self.gui_widget.fix_Visible_In_Refractions_ProgressBar
			if self.bad_visible_in_refraction_plug_count:
				progressBar.setMaximum(self.bad_visible_in_refraction_plug_count)
			else:
				progressBar.setMaximum(100)
				progressBar.setValue(100)
				
			for node in self.bad_visible_in_refraction_plugs:
				cmds.setAttr(node,True)
				progressBar.add_Tick()
		#----------------------------------------------------------------------
		def apply_Freeze_Transforms():
			""""""
			progressBar = self.gui_widget.apply_Freeze_Transforms_ProgressBar
			progressBar.setMaximum(self.all_transform_node_count*2)
			for node in self.all_transform_nodes:
				try:
					cmds.makeIdentity(node,apply=True,t=True,r=True,s=True,n=False, pn=True)
				except:
					pass
				progressBar.add_Tick()
	
			for node in self.all_transform_nodes:
				try:
					cmds.makeIdentity(node,apply=False,t=True,r=True,s=True,n=False, pn=True)
				except:
					pass
				progressBar.add_Tick()

		remove_Shapes_With_No_Geometry()
		fix_PolySurface_Names()
		fix_Bad_Unicode_Names()
		add_Extractor_Id_Tags()
		fix_Attribute_Connections()
		remove_Intermediate_Objects()
		fix_Bad_Inherit_Transform_Plugs()
		fix_Bad_Visible_In_Reflection_Plugs()
		fix_Visible_In_Refraction_Plugs()
		apply_Freeze_Transforms()
	#----------------------------------------------------------------------
	def export_AbcExport(self):
		cmds.select(self.top_level_node)
		cmds.AbcExport(jobArg='-frameRange 1 1 -attr AW_Extractor_ID -attr assined_display_layer -uvWrite -dataFormat HDF -eulerFilter -stripNamespaces -root %s -file C:/temp/Extracted.abc' % self.top_level_node.name)
	#----------------------------------------------------------------------
	def export_Shaders(self):
		cmds.select(clear=True)
		for shader in self.active_shaders:
			isinstance(shader,Shading_Engine)
			if not shader.assined_material == None:
				if not shader.assined_material.name == None:
					cmds.select(shader.name,ne=True,add=True)
					cmds.select(shader.assined_material.name,add=True)
					items = cmds.listConnections(shader.assined_material.name,destination=False,source=True)
					if not items == None:
						if len(items):
							cmds.select(items,add=True)
		
		try:
			cmds.file("C:/temp/shaders.ma",force=True,op="v=1;",typ="mayaAscii",es=True)
			clean_maya_shader_file("C:/temp/shaders.ma")
			self._shader_file_is_ascii = True
		except:
			cmds.file("C:/temp/shaders.mb",force=True,op="v=1;",typ="mayaBinary",es=True)
			self._shader_file_is_ascii = False
########################################################################
class Alembic_Asset_Reader(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		global _Global_Member_ID_Data
		_Global_Member_ID_Data.clear()
		with file('C:/temp/Alembic_Assets_Extractor_Data.json',"r") as f:
			self.json_data = json.load(f)
		
		self.import_AbcExport()
		self.import_Shaders()
		for item in cmds.ls("*.AW_Extractor_ID",recursive=True):
			plug = Scripts.OpenMaya_Util_API.MPLUG(item)
			_Global_Member_ID_Data[plug.value] = plug.node

		self.item_Collector = Constructor_Collector(self.json_data)
		#cmds.namespace(removeNamespace="extracted_shaders",mergeNamespaceWithRoot=True)
	def import_AbcExport(self):
		cmds.AbcImport("C:/temp/Extracted.abc",mode="open")
		# self.top_level_node = MNODE(self.top_level_node_name)

	def import_Shaders(self):
		if self.json_data["shader_file_is_ascii"]:
			cmds.file("C:/temp/shaders.ma",i=True,type="mayaAscii", ignoreVersion=True, ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")
		else:
			cmds.file("C:/temp/shaders.mb",i=True,type="mayaBinary", ignoreVersion=True, ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")

######################################################################## CUSTOM QT WIDGETS
########################################################################
class Extraction_Step_Label(QT.QLabel):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Extraction_Step_Label,self).__init__(parent)
########################################################################
class Tickalbe_ProgressBar(QT.QProgressBar):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Tickalbe_ProgressBar,self).__init__(parent)
	#----------------------------------------------------------------------
	def add_Tick(self):
		""""""
		self.setValue(self.value()+1)
		
QT.ui_Loader.registerCustomWidget(Tickalbe_ProgressBar)

########################################################################
class _CODE_COMPLEATION_HELPER(QT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		''''''
		super(_CODE_COMPLEATION_HELPER,self).__init__(parent=parent)
		if False:
			self.tabWidget = QT.QTabWidget()
			self.tab = QT.QWidget()
			self.FRAME_Extraction_Scan_Data = QT.QFrame()
			self.GBX_Extraction_Scan_Data = QT.QGroupBox()
			self.shapeNodesWithNoGeometryLabel = QT.QLabel()
			self.shapeNodesWithNoGeometrySpinBox = QT.QSpinBox()
			self.shapeNodesWithNoGeometryprogressBar = Tickalbe_ProgressBar()
			self.totalNumberOfTransfomsExportedLabel = QT.QLabel()
			self.Number_Of_Transfoms_To_Be_Exported_SpinBox = QT.QSpinBox()
			self.all_descendents_scan_progressBar = Tickalbe_ProgressBar()
			self.exportShaderCountLabel = QT.QLabel()
			self.exportShaderCountSpinBox = QT.QSpinBox()
			self.exportShaderCountprogressBar = Tickalbe_ProgressBar()
			self.exportLayerCountLabel = QT.QLabel()
			self.exportLayerCountSpinBox = QT.QSpinBox()
			self.exportLayerCountprogressBar = Tickalbe_ProgressBar()
			self.intermediateObjectCountLabel = QT.QLabel()
			self.intermediateObjectCountSpinBox = QT.QSpinBox()
			self.intermediateObjectCountprogressBar = Tickalbe_ProgressBar()
			self.illegalPolySurfaceNameLengthCountLabel = QT.QLabel()
			self.illegalPolySurfaceNameLengthCountSpinBox = QT.QSpinBox()
			self.badUnicodeNameCountLabel = QT.QLabel()
			self.badUnicodeNameCountSpinBox = QT.QSpinBox()
			self.badUnicodeNameCountprogressBar = Tickalbe_ProgressBar()
			self.brokenTransformInheritanceLabel = QT.QLabel()
			self.brokenTransformInheritanceSpinBox = QT.QSpinBox()
			self.brokenTransformInheritanceprogressBar = Tickalbe_ProgressBar()
			self.incorrectVisibleInReflectionPlugsLabel = QT.QLabel()
			self.incorrectVisibleInReflectionPlugsSpinBox = QT.QSpinBox()
			self.incorrectVisibleInReflectionPlugsprogressBar = Tickalbe_ProgressBar()
			self.incorrectVisibleInRefractionPlugsLabel = QT.QLabel()
			self.incorrectVisibleInRefractionPlugsSpinBox = QT.QSpinBox()
			self.incorrectVisibleInRefractionPlugsprogressBar = Tickalbe_ProgressBar()
			self.FRAME_Export_Steps = QT.QFrame()
			self.GBX_Export_Steps = QT.QGroupBox()
			self.deletingAllShapesWithNoGeometryLabel = QT.QLabel()
			self.deletingAllShapesWithNoGeometry_ProgressBar = Tickalbe_ProgressBar()
			self.renamingPolySurfaceShapesLabel = QT.QLabel()
			self.renaming_PolySurface_Shapes_ProgressBar = Tickalbe_ProgressBar()
			self.correctingInvalidUnicodeNamesLabel = QT.QLabel()
			self.correctingInvalidUnicodeNamesProgressBar = Tickalbe_ProgressBar()
			self.addingExtractorIdsLabel = QT.QLabel()
			self.apply_Extractor_Ids_ProgressBar = Tickalbe_ProgressBar()
			self.unlockingBreakAttrConnectionsLabel = QT.QLabel()
			self.unlocking_And_Break_Attr_Connections_ProgressBar = Tickalbe_ProgressBar()
			self.removingIntermediateObjectsLabel = QT.QLabel()
			self.removing_Intermediate_Objects_ProgressBar = Tickalbe_ProgressBar()
			self.forcingInheritTransformLabel = QT.QLabel()
			self.fix_Inherit_Transform_ProgressBar = Tickalbe_ProgressBar()
			self.forcingVisibleInReflectionsLabel = QT.QLabel()
			self.fix_VisibleIn_Reflections_ProgressBar = Tickalbe_ProgressBar()
			self.forcingVisibleInRefractionsLabel = QT.QLabel()
			self.fix_Visible_In_Refractions_ProgressBar = Tickalbe_ProgressBar()
			self.zeroingOutTransformsLabel = QT.QLabel()
			self.apply_Freeze_Transforms_ProgressBar = Tickalbe_ProgressBar()
			self.collectingDisplayLayerAssignmentsLabel = QT.QLabel()
			self.collecting_Display_Layer_Assignments_ProgressBar = Tickalbe_ProgressBar()
			self.collectingShaderAssignmentsLabel = QT.QLabel()
			self.collecting_Shader_Assignments_ProgressBar = Tickalbe_ProgressBar()
			self.Plain_Boxed_Frame = QT.QFrame()
			self.groupBox = QT.QGroupBox()
			self.performSceneCleanUpLabel = QT.QLabel()
			self.useRenderLayerLabel = QT.QLabel()
			self.useRenderLayerComboBox = QT.QComboBox()
			self.topLevelNodeLabel = QT.QLabel()
			self.Top_Level_Node_Input = QT.QLineEdit()
			self.Set_To_Selected_Button = QT.QPushButton()
			self.replaceShadersWithLambertsLabel = QT.QLabel()
			self.replaceShadersWithLambertsCheckBox = QT.QCheckBox()
			self.removeOtherLayersLabel = QT.QLabel()
			self.removeOtherLayersCheckBox = QT.QCheckBox()
			self.performSceneCleanUpCheckBox = QT.QCheckBox()
			self.Export_Button = QT.QPushButton()
			self.tab_2 = QT.QWidget()
			self.Import_Button = QT.QPushButton()
			self.tab_3 = QT.QWidget()
			self.FRAME_Extraction_Log = QT.QFrame()
			self.GBX_Extraction_Log = QT.QGroupBox()
			self.Extraction_Log_Text = QT.QTextEdit()
########################################################################
class Alembic_Asset_Extraction_GUI(MayaQWidgetBaseMixin,_CODE_COMPLEATION_HELPER):
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		""""""
		super(Alembic_Asset_Extraction_GUI,self).__init__(parent)
		self.alembic_asset_writer = Alembic_Asset_Writer(self)
	#----------------------------------------------------------------------
	def reset(self):
		""""""
		for progressBar in self.findChildren(QT.QProgressBar):
			progressBar.setValue(0)
		
		for spinbox in self.findChildren(QT.QSpinBox):
			spinbox.setValue(0)
	#----------------------------------------------------------------------
	def _run_setup(self):
		""""""
		self.Set_To_Selected_Button.clicked.connect(self.on_Set_To_Selected_Button_Clicked)
		self.Top_Level_Node_Input.textChanged.connect(self.on_Top_Level_Input_Changed)
		self.Export_Button.clicked.connect(self.on_Export_Button_Clicked)
		self.Import_Button.clicked.connect(self.on_Import_Button_Clicked)
		for layer in sorted(cmds.ls(type="renderLayer")):
			if not layer == "defaultRenderLayer":
				self.useRenderLayerComboBox.addItem(layer)
	#----------------------------------------------------------------------
	def on_Set_To_Selected_Button_Clicked(self):
		""""""
		active_selection = cmds.ls(sl=True)
		if len(active_selection):
			self.Top_Level_Node_Input.setText(active_selection[0])
	#----------------------------------------------------------------------
	def on_Top_Level_Input_Changed(self):
		""""""
		text_value = self.Top_Level_Node_Input.text()
		if len(text_value) and cmds.objExists(text_value):
			if self.alembic_asset_writer.set_Top_Level_Node(text_value):
				self.reset()
				self.Export_Button.setEnabled(True)
			else:
				self.Export_Button.setEnabled(False)
		else:
			self.Export_Button.setEnabled(False)
	#----------------------------------------------------------------------
	def on_Export_Button_Clicked(self):
		""""""
		try:
			kill_hyperShadePanel()
		except:
			pass
		if not self.useRenderLayerComboBox.currentText() == "defaultRenderLayer":
			Shader_Overides_To_Master_Layer(self.useRenderLayerComboBox.currentText(),self.Extraction_Log_Text)
		if self.replaceShadersWithLambertsCheckBox.isChecked():
			replace_all_shaders_with_lambers(self.Extraction_Log_Text)
		if self.removeOtherLayersCheckBox.isChecked():
			remove_All_Render_Layers()
		if self.performSceneCleanUpCheckBox.isChecked():
			perform_CleanUp()
		self.alembic_asset_writer.RUN_SCANS()
		self.alembic_asset_writer.Run_Export()
		self.Export_Button.setEnabled(False)
	#----------------------------------------------------------------------
	def on_Import_Button_Clicked(self):
		""""""
		try:
			kill_hyperShadePanel()
		except:
			pass
		Alembic_Asset_Reader()
				
QT.ui_Loader.registerCustomWidget(Alembic_Asset_Extraction_GUI)

#----------------------------------------------------------------------
def load_Gui():
	""""""
	gui = QT.ui_Loader.load(os.path.join( os.path.dirname(__file__), "Alembic_Asset_Extraction_V2.ui") )
	gui._run_setup()
	gui.show()
	return gui
