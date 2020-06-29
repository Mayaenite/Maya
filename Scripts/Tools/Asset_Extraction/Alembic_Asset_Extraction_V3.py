
import os
import QT
import json
import maya.cmds as cmds
import maya.mel
import Scripts.OpenMaya_Util_API
import maya.api.OpenMaya as om
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
MNODE = Scripts.OpenMaya_Util_API.Maya_Node


########################################################################
class Global_Access(object):
	""""""
	Json_File_Path    = os.path.join(os.environ["TEMP"],'Alembic_Assets_Extractor_Data.json')
	Alembic_File_Path = os.path.join(os.environ["TEMP"],'Extracted.abc')
	Shader_File_Path  = os.path.join(os.environ["TEMP"],'shaders.mb')
	Mesh_Cleanup_Log  = os.path.join(os.environ["TEMP"],"Mesh_Cleanup_Script_Editor_Log.txt")
	All_Geometry_Descendents = []
	Json_Data         = {}
	Node_ID_Dict    = {}
	Top_Level_Node    = None
	if not cmds.pluginInfo("AbcExport", q=True,loaded=True,):
		cmds.loadPlugin("AbcExport")
	#----------------------------------------------------------------------
	@classmethod
	def load_Json_Data(cls):
		""""""
		with file(cls.Json_File_Path,"r") as f:
			cls.Json_Data = json.load(f)
		return cls.Json_Data
	#----------------------------------------------------------------------
	@classmethod
	def save_Json_Data(cls):
		""""""
		with file(cls.Json_File_Path,'w') as f:
			json.dump(cls.Json_Data, f, indent=4, sort_keys=True)
	#----------------------------------------------------------------------
	@classmethod
	def set_Top_Level_Node(cls,node):
		""""""
		cls.Top_Level_Node = Uuid_Named_Node(node)
	#----------------------------------------------------------------------
	@classmethod
	def Export_Shaders(cls):
		cmds.select(clear=True)
		if cls.Json_Data["shaders_should_be_loaded"]:
			for shader in cls.Json_Data["shading_engines"]:
				if shader_Engine_Has_Material(shader["name"]):
					assined_material = get_Shader_Engine_Material(shader["name"])
					cmds.select(shader["name"],ne=True,add=True)
					cmds.select(assined_material,add=True)
					items = cmds.listConnections(assined_material,destination=False,source=True)
					if not items == None:
						if len(items):
							cmds.select(items,add=True)
			cmds.file(cls.Shader_File_Path,force=True,op="v=1;",typ="mayaBinary",es=True)
	#----------------------------------------------------------------------
	@classmethod
	def Export_Alembic(cls):
		""""""
		if len(cmds.ls("*.BodyStyleTrim")) and len(cmds.ls("*.VVP_CATEGORY")):
			import Scripts.Tools.Vray_Scene_States_Manager.Honda_Data_Parser
			Scripts.Tools.Vray_Scene_States_Manager.Honda_Data_Parser.Store_Honda_MetaData(str(cls.Top_Level_Node))
		if not cmds.pluginInfo( "AbcExport", query=True, loaded=True):
			cmds.loadPlugin("AbcExport")
		cmds.select(cls.Top_Level_Node)
		cmds.AbcExport(jobArg='-frameRange 1 1 -attr AW_Extractor_ID -attr AW_Geo_Tracking_ID -attr hondaAssetId -attr hondaRebuildData -attr assined_display_layer -uvWrite -dataFormat HDF -eulerFilter -stripNamespaces -root %s -file %s' % (cls.Top_Level_Node,cls.Alembic_File_Path))
	#----------------------------------------------------------------------
	@classmethod
	def Import_Alembic(cls):
		start_Recording_History_File()
		cmds.file(cls.Alembic_File_Path,f=True,ignoreVersion=True,typ="Alembic",o=True)
		stop_Recording_History_File()
	#----------------------------------------------------------------------
	@classmethod
	def Import_Shaders(cls):
		if cls.Json_Data["shaders_should_be_loaded"]:
			#cmds.file("C:/temp/shaders.ma",i=True,type="mayaAscii", ignoreVersion=True, ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")
			cmds.file(cls.Shader_File_Path,i=True,type="mayaBinary", ignoreVersion=True, ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")


######################################################################## UTILTY LAMBDA FUNCTIONS
uuids_to_names                                    = lambda idlist:cmds.ls(idlist)
names_to_uuids                                    = lambda names:cmds.ls(names,uuid=True)
get_Node_Name                                     = lambda node:cmds.ls(cmds.ls(node))[0].split("|")[-1]
get_Node_Path                                     = lambda node:cmds.ls(node,l=True)[0]
get_Node_UUid                                     = lambda node:cmds.ls(node, uuid=True)[0]
get_Parent                                        = lambda node:none_To_List(cmds.listRelatives(node, parent=True, fullPath=True))
none_To_List                                      = lambda val:val if val is not None else []
get_All_Shader_Engines                            = lambda :cmds.ls(type="shadingEngine")
get_All_Non_Default_Shader_Engines                = lambda :[item for item in get_All_Shader_Engines() if not item.startswith("initial")]
get_Shader_Engine_Members                         = lambda shader_engine:[item for item in cmds.ls(cmds.listConnections(shader_engine+".dagSetMembers",shapes=True,destination=False,source=True),objectsOnly=True) if not cmds.objectType(item) in ["renderLayer","displayLayer"]]
add_Shader_Engine_Members                         = lambda items,shader_engine:cmds.sets(items,edit=True,forceElement=shader_engine)
shader_Engine_Has_Material                        = lambda shader_engine: True if len( none_To_List(cmds.listConnections( shader_engine+".surfaceShader",source=True,plugs=False,skipConversionNodes=True))) else False
get_Shader_Engine_Material                        = lambda shader_engine:cmds.listConnections( shader_engine+".surfaceShader",source=True,plugs=False,skipConversionNodes=True)[0]
get_All_Non_Default_Shader_Engines_With_Materials = lambda :[item for item in get_All_Non_Default_Shader_Engines() if shader_Engine_Has_Material(item)]
get_All_Shader_Engines_With_Materials             = lambda :[item for item in get_All_Shader_Engines() if shader_Engine_Has_Material(item)]
get_Camera_Transforms                             = lambda :none_To_List(cmds.listRelatives( cmds.ls( type="camera") , fullPath=True, parent=True))
get_Transform_Assemblies                          = lambda :[item for item in cmds.ls(cmds.ls( assemblies=True), exactType="transform",long=True) if not item in get_Camera_Transforms()]
get_All_Transform_Descendents                     = lambda node:none_To_List(cmds.listRelatives(node, allDescendents=True, fullPath=True, type='transform'))
get_All_Geometry_Descendents                      = lambda node:cmds.ls(cmds.listRelatives(node, allDescendents=True, path=True),geometry=True,l=True)
get_All_Descendents                               = lambda node:cmds.ls(cmds.listRelatives(node, allDescendents=True, path=True),l=True)
check_If_AW_Extractor_ID_Exists                   = lambda node:cmds.attributeQuery( "AW_Extractor_ID",node=node, exists=True )
add_AW_Extractor_ID                               = lambda node:cmds.addAttr(node, longName="AW_Extractor_ID",attributeType="long")
get_AW_Extractor_ID                               = lambda node:cmds.getAttr(node+".AW_Extractor_ID")
set_AW_Extractor_ID                               = lambda node,val:cmds.setAttr(node+".AW_Extractor_ID", val)
create_Lambert_Shader                             = lambda name:cmds.shadingNode("lambert",asShader=True,name=name)
create_Shader_Engine                              = lambda name:cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name=name.replace("SG","")+"SG")
assign_Material_To_Engine                         = lambda shader,engine:cmds.connectAttr(shader+".outColor",engine+".surfaceShader",force=True)
shading_Engine_Contains_Face_Assignments          = lambda engine:".f" in none_To_List(cmds.sets(engine,q=True))
set_Current_Render_Layer                          = lambda layer:cmds.editRenderLayerGlobals(currentRenderLayer=layer)
get_Current_Render_Layer                          = lambda :cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True)
get_All_Non_Default_Render_Layers                 = lambda :[layer for layer in cmds.ls(type="renderLayer") if not layer == "defaultRenderLayer"]
is_Node_Locked                                    = lambda node:all(cmds.lockNode( node,q=True,lock=True, lockName=True, lockUnpublished=True))
unlock_Node                                       = lambda node:cmds.lockNode( node,lock=False, lockName=False, lockUnpublished=False)
get_Display_Layer_Members                         = lambda node:cmds.editDisplayLayerMembers(node,q=True,fullNames=True)

class Uuid_Named_Node(object):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node
	it can be sent to maya.cmds as itself and acts like a string useing uuid pointer to repesent itself
	"""
	#----------------------------------------------------------------------
	def __init__(self,name):
		self._uuid = get_Node_UUid(name)
	#----------------------------------------------------------------------
	def __str__(self):
		return get_Node_Path(self._uuid)
	#----------------------------------------------------------------------
	def __repr___(self):
		return get_Node_Path(self._uuid)
	#----------------------------------------------------------------------
	def __get_name(self):
		return unicode(get_Node_Name(self._uuid))
	#----------------------------------------------------------------------
	name          = property(fget=__get_name)


#----------------------------------------------------------------------
def start_Recording_History_File():
	""""""
	if os.path.exists(Global_Access.Mesh_Cleanup_Log):
		stop_Recording_History_File()
		os.remove(Global_Access.Mesh_Cleanup_Log)
	cmds.scriptEditorInfo(writeHistory=True,historyFilename=Global_Access.Mesh_Cleanup_Log)
	Global_Access.Mesh_Cleanup_Log = cmds.scriptEditorInfo(q=True,historyFilename=True)
#----------------------------------------------------------------------
def stop_Recording_History_File():
	""""""
	cmds.scriptEditorInfo(writeHistory=False)

######################################################################## TO BE CATAGORIZED
#----------------------------------------------------------------------
def Remove_Unknown_Plugins():
	""""""
	oldplugins = cmds.unknownPlugin(q=True, list=True)
	unknown_nodes = cmds.ls(type="unknown")
	for node in unknown_nodes :
		try:
			cmds.delete(node)
		except:
			pass
	if not oldplugins == None:
		for plugin in oldplugins:
			try:
				cmds.unknownPlugin(plugin, remove=True)
				print "Removed Unknown Plugin {}".format(plugin)
			except:
				print "Did Not Remove Unknown Plugin {}".format(plugin)

#----------------------------------------------------------------------
def find_Most_Likely_Master_Item():
	assemblies = get_Transform_Assemblies()
	master_item = ""
	largest_child_count = 0
	for item in assemblies:
		children = get_All_Transform_Descendents(item)
		count = len(children)
		if count > largest_child_count:
			largest_child_count = count
			master_item = item
	return master_item

#----------------------------------------------------------------------
def create_Log_Text_Template():
	""""""
	res = '<html><head/><body><p>'
	res += '<span style=" font-size:8.25pt; color:#ff0000;">'
	res += 'Warning:'
	res += '</span>'
	res += '<span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">'
	res += '{}' 
	res += '</span>'
	res += '</p></body></html>'
	return res

#----------------------------------------------------------------------
def mesh_Has_Multi_Uv_Sets(mesh):
	""""""
	all_uv_sets = cmds.polyUVSet( mesh, query=True, allUVSets=True)
	if not all_uv_sets == None:
		if len(all_uv_sets) > 1:
			return True
	return False
#----------------------------------------------------------------------
def mesh_Remove_Multi_Uv_Sets(mesh):
	""""""
	try:
		default_uv_set = cmds.getAttr(mesh+".uvSet[0].uvSetName")

		if not default_uv_set == "map1":
			cmds.polyUVSet(mesh, rename=True, newUVSet='map1', uvSet=default_uv_set)

		if not cmds.polyUVSet( mesh ,query=True, currentUVSet=True) == 'map1':
			cmds.polyUVSet(mesh,currentUVSet=True, uvSet='map1')

		for uv_set in cmds.polyUVSet( mesh, query=True, allUVSets=True):
			if not uv_set == "map1":
				cmds.polyUVSet(mesh, delete=True, uvSet=uv_set)
	except:
		pass

#----------------------------------------------------------------------
def kill_hyperShadePanel():
	""""""
	maya.mel.eval("closeHypershade")
#----------------------------------------------------------------------
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
	layers = [layer for layer in cmds.ls(type="renderLayer") if not layer == "defaultRenderLayer"]
	if len(layers):
		cmds.delete([layer for layer in cmds.ls(type="renderLayer") if not layer == "defaultRenderLayer"])

#----------------------------------------------------------------------
def perform_CleanUp():
	""""""
	maya.mel.eval('source "C:/Program Files/Autodesk/Maya2018/scripts/startup/cleanUpScene.mel"')
	for cmd in ['deleteUnusedNurbsSurfaces','deleteUnusedConstraints','deleteUnusedPairBlends','deleteUnusedLocators' ,'deleteUnusedSets' ,'deleteUnusedExpressions' ,'deleteUnknownNodes','deleteUnusedDeformers','deleteInvalidNurbs(0)','MLdeleteUnused' ,'RNdeleteUnused' ,'deleteUnusedBrushes' ,'deleteUnusedCommon( "groupId", 0, "")']:
		maya.mel.eval(cmd)
	cmds.delete(all=True,constructionHistory=True)

#----------------------------------------------------------------------
def names_To_MSelectionList(names):		
	sellist = om.MSelectionList()
	[sellist.add(node) for node in names]
	return sellist

#----------------------------------------------------------------------
def is_Transform_A_Group(node):
	""""""
	typ  = cmds.objectType(node)
	if typ == 'transform':
		if len(none_To_List(cmds.listRelatives(node,shapes=True))):
			return True
	return False

#----------------------------------------------------------------------
def check_If_Shading_Engine_Contains_Face_Assignments(engine,items,log_text):
	for item in items:
		if ".f" in item:
			log_text.insertHtml('<html><head/><body><p><span style=" font-size:8.25pt; color:#ff0000;">Warning:</span><span style=" font-size:8.25pt; color:#ffffff;"> Face Assinments Found On </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{} </span><span style=" font-size:8.25pt; color:#ffffff;">From </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{}<br/></span></p></body></html>'.format(engine,item))


########################################################################################################## BASE WIDGETS USED FOR SCANNING FIXING AND EDITING 
########################################################################
class Extraction_Action_Widget(QT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Extraction_Action_Widget,self).__init__(parent=parent)
		self.setLayout(Zero_Content_Margines_HBoxLayout())
		self.setSizePolicy(QT.QSizePolicy(QT.QSizePolicy.Policy.Minimum,QT.QSizePolicy.Policy.Maximum))
		self._depends_on = None
	#----------------------------------------------------------------------
	def get_Items_Of_Interset(self):
		""""""
		return []
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		return True
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
	#----------------------------------------------------------------------
	def set_Depends_On_Widget(self,widget):
		""""""
		self._depends_on = widget
	#----------------------------------------------------------------------
	def had_Depends_On_Widget(self):
		""""""
		return isinstance(self._depends_on,QT.QWidget)
	#----------------------------------------------------------------------
	def do_Run_Action(self):
		if self.isVisible():
			if self.had_Depends_On_Widget():
				if self._depends_on._result:
					self.run_Action()
			else:
				self.run_Action()

########################################################################
class Scan_Progress_Action_Widget(Extraction_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Scan_Progress_Action_Widget,self).__init__(parent=parent)
		self.progressBar = Widget_Action_ProgressBar()
		self.layout().addWidget(self.progressBar)
########################################################################
class Multi_Scan_Progress_Action_Widget(Extraction_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Multi_Scan_Progress_Action_Widget,self).__init__(parent=parent)
		self.progressBarA = Widget_Action_ProgressBar()
		self.progressBarB = Widget_Action_ProgressBar()
		self.layout().addWidget(self.progressBarA)
		self.layout().addWidget(self.progressBarB)
########################################################################
class Fixed_Items_Progress_Action_Widget(Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Fixed_Items_Progress_Action_Widget,self).__init__(parent=parent)
		self.spinbox = Changed_Item_Count_SpinBox()
		self.layout().insertWidget(0,self.spinbox)


########################################################################################################## EXTRACTION
########################################################################
class Widget_Action_Add_Extractor_Id_Tags(Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()

		global id_extractor_counter

		id_extractor_counter = 1

		assembly_nodes       = get_Transform_Assemblies()

		geometry_nodes       = cmds.ls(cmds.listRelatives(assembly_nodes, allDescendents=True, path=True), geometry=True,l=True)

		transform_nodes      = cmds.listRelatives(assembly_nodes, allDescendents=True, path=True, type='transform')

		shader_engine_nodes  = get_All_Non_Default_Shader_Engines()

		items_to_scan        = assembly_nodes + transform_nodes + geometry_nodes + shader_engine_nodes
		
		self.progressBar.set_Progress_Message("Applying Ids", max_value=len(items_to_scan), resetValue=True)

		for item in items_to_scan:

			cmds.lockNode(item, lock=False, lockName=False, lockUnpublished=False)

			if not check_If_AW_Extractor_ID_Exists(item):
				try:
					add_AW_Extractor_ID(item)
				except:
					print "Did Not Add Id To %s" % item	
					continue
			set_AW_Extractor_ID(item,id_extractor_counter)
			id_extractor_counter += 1
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Get_Display_Layers_Data(Multi_Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def Build_Display_Layer_Data(self,node):
		""""""
		self.progressBarB.set_Calculating()
		
		data = dict(name=node,color=cmds.getAttr(node+".color"))
		assignment_ids = []
		members = get_Display_Layer_Members(node)
		
		self.progressBarB.set_Progress_Message("Collecting Members", max_value=len(members), resetValue=True)

		for member in members:
			if check_If_AW_Extractor_ID_Exists(member):
				assignment_ids.append(get_AW_Extractor_ID(member))
			else:
				raise AttributeError("Could Not Find AW_Extractor_ID for node {}".format(member))
			self.progressBarB.add_Tick()

		data["assignment_ids"]=assignment_ids
		self.progressBarB.reset()
		return data
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBarA.set_Calculating()
		self.progressBarB.reset()
		
		self.result = []
		items_to_scan = none_To_List(cmds.listConnections(Global_Access.Top_Level_Node,type="displayLayer"))
		items_to_scan.extend( none_To_List(cmds.listConnections(cmds.listRelatives(Global_Access.Top_Level_Node,fullPath=True, allDescendents=True), t="displayLayer") ) )
		items_to_scan = list(set(items_to_scan))

		if 'defaultLayer' in items_to_scan:
			items_to_scan.remove('defaultLayer')


		if len(items_to_scan):
			self.progressBarA.set_Progress_Message("Building Layers",max_value=len(items_to_scan),resetValue=True)
			for item in items_to_scan:
				data = self.Build_Display_Layer_Data(item)
				self.result.append(data)
				self.progressBarA.add_Tick()
		else:
			self.progressBarA.setRange(0,100)
			self.progressBarA.setValue(100)
########################################################################
class Widget_Action_Get_Shader_Engine_Data(Multi_Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def Build_Shader_Engine_Data(self,node):
		""""""
		self.progressBarB.set_Calculating()

		if not check_If_AW_Extractor_ID_Exists(node):
			raise AttributeError("Could Not Find AW_Extractor_ID for node {}".format(node))

		data = dict(name=node,idnum=get_AW_Extractor_ID(node))

		assignment_ids = []

		if shader_Engine_Has_Material(node):
			members = get_Shader_Engine_Members(node)
			if len(members):
				self.progressBarB.set_Progress_Message("Collecting Members",max_value=len(members),resetValue=True)
				
				for member in members:
					if check_If_AW_Extractor_ID_Exists(member):
						assignment_ids.append(get_AW_Extractor_ID(member))
					else:
						raise AttributeError("Could Not Find AW_Extractor_ID for node {}".format(member))
					self.progressBarB.add_Tick()
		
		data["assignment_ids"]=assignment_ids
		
		self.progressBarB.reset()

		return data
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBarA.set_Calculating()
		self.progressBarB.reset()

		self.result = []
		
		relatives      = none_To_List(cmds.listRelatives(Global_Access.Top_Level_Node, fullPath=True, allDescendents=True, type="transform"))
		relatives      = none_To_List(cmds.listRelatives(relatives, shapes=True, fullPath=True))

		items_to_scan  = none_To_List(cmds.listConnections(relatives,t="shadingEngine"))
		items_to_scan = list(set(items_to_scan))

		if "initialShadingGroup" in items_to_scan:
			items_to_scan.remove("initialShadingGroup")
		
		if not len(items_to_scan):
			self.progressBarA.reset()
		else:
			self.progressBarA.set_Progress_Message("Building Shaders", max_value=len(items_to_scan), resetValue=True)
			for item in items_to_scan:
				data = self.Build_Shader_Engine_Data(item)
				self.result.append(data)
				self.progressBarA.add_Tick()
				
########################################################################################################## MANIPULATING
########################################################################
class Widget_Action_Does_Scene_Contain_Instances(Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		iterDag = om.MItDag(om.MItDag.kBreadthFirst,om.MFn.kDagNode)
		count = 0
		while not iterDag.isDone():
			count += 1
			iterDag.next()
		iterDag.reset()
		
		self.progressBar.set_Progress_Message("Scaning Dag Nodes",count,True)

		while not iterDag.isDone():
			if iterDag.isInstanced():
				self.progressBar.setValue(count)
				self.progressBar.setStyleSheet("QProgressBar {\n    border: 1px solid yellow;\n    border-radius: 1px;\n}\n\nQProgressBar::chunk {\n    background-color: red;\n    width: 10px;\n}")
				self.progressBar.setFormat("Instances Found Preforming Convershions")
				self._result = True
				return True
			self.progressBar.add_Tick()
			iterDag.next()
			
		self.progressBar.setStyleSheet("QProgressBar {color:black;\n    border: 2px solid blue;\n    border-radius: 5px;\n}\n\nQProgressBar::chunk {\n    \n	background-color: rgb(0, 255, 0);\n    width: 10px;\n}")
		self.progressBar.setFormat("No Instances Found")
		self._result = False
		return False
########################################################################
class Base_Widget_Action_Convert_Instances(Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def convert_Instance(self,uid):
		old_item_name     = get_Node_Name(uid)
		old_item_new_name = "To_Be_Deleted_"+old_item_name.replace("To_Be_Deleted_","")
		new_item_name     = "New_Item_"+old_item_name.replace("To_Be_Deleted_","")
		cmds.rename(get_Node_Path(uid),old_item_new_name)
	
		new_item = cmds.duplicate(get_Node_Path(uid),name=old_item_name,returnRootsOnly=True)[0]
		new_item_uuid = get_Node_UUid(new_item)
		return new_item_uuid
	
	#----------------------------------------------------------------------
	def get_Total_Instance_Associations_Count(self,associations):
		""""""
		total_count = 0
		for item in associations:
			total_count += len(item[1])
		return total_count
	#----------------------------------------------------------------------
	def get_Unique_Instance_Uuids(self,fnType=om.MFn.kDagNode):
		"""Returns A List Of The The Unique Instance UUids"""
		
		self.progressBar.set_Calculating()
		
		iterDag = om.MItDag(om.MItDag.kBreadthFirst,fnType)
		instances = []
		
		count = 0
		while not iterDag.isDone():
			count += 1
			iterDag.next()
			self.progressBar.setValue(0)
		iterDag.reset()
		
		self.progressBar.set_Progress_Message("Finding Unique Instances", max_value=count, resetValue=True)
		
		while not iterDag.isDone():
			if iterDag.isInstanced():
				instances.append(iterDag.fullPathName())
			iterDag.next()
			self.progressBar.add_Tick()
		
		uuids            = cmds.ls(instances, uuid=True)
		unique_uuids     = list(set(uuids))
		
		return unique_uuids
	#----------------------------------------------------------------------
	def create_Instance_Parents_Data(self,fnType=om.MFn.kDagNode):
		""""""
		unique_uuids = self.get_Unique_Instance_Uuids(fnType=fnType)
		
		self.progressBar.set_Progress_Message("Building Master Slave Instance Associations", max_value=len(unique_uuids), resetValue=True)
		
		associations = []
		for uid in unique_uuids:
			name =  cmds.ls(uid)[0]
			all_parents       = cmds.listRelatives(name, allParents=True, fullPath=True,)
			all_parent_uuids  = cmds.ls(all_parents, uuid=True)
			associations.append([uid,all_parent_uuids])
			self.progressBar.add_Tick()
		return associations
	#----------------------------------------------------------------------
	def get_Instance_Associations(self,fnType=om.MFn.kDagNode,objectType=None):
		data = self.create_Instance_Parents_Data(fnType=fnType)
		if objectType == None or not len(data):
			return data
		else:
			self.progressBar.set_Progress_Message("Filtering For {}".format(objectType), max_value=len(data), resetValue=True)
			
		res = []
		
		for data_item in data:
			instances_name,instances_parents = data_item
			name = get_Node_Path(instances_name)
			if objectType is not None:
				if objectType == "group" and cmds.objectType(name) == 'transform':
					if cmds.listRelatives(name,shapes=True) == None:
						res.append(data_item)
				elif cmds.objectType(name) == objectType:
					res.append(data_item)
			else:
				res.append(data_item)
				
			self.progressBar.add_Tick()
			
		return res
	#----------------------------------------------------------------------
	def run_Instance_Convershion(self,fnType=om.MFn.kDagNode,objectType=None):
		
		items_to_scan = self.get_Instance_Associations(fnType=fnType,objectType=objectType)
		
		if len(items_to_scan):
			
			self.progressBar.set_Calculating()
			
			count = self.get_Total_Instance_Associations_Count(items_to_scan)
			
			self.progressBar.set_Progress_Message("Converting Instances",count,True)

			for item in items_to_scan:
				item_uid,item_parent_uids = item
				for item_parent in item_parent_uids:
					self.convert_Instance(item_parent)
					self.progressBar.add_Tick()
			
			cmds.delete(cmds.ls("To_Be_Deleted_*"))
		else:
			self.progressBar.set_Progress_Message("No Items Found".format(objectType))
			self.progressBar.setRange(0,100)
			self.progressBar.setValue(100)
			
########################################################################
class Widget_Action_Convert_Group_Instances(Base_Widget_Action_Convert_Instances):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.run_Instance_Convershion(fnType=om.MFn.kTransform,objectType="group")
########################################################################
class Widget_Action_Convert_Transform_Instances(Base_Widget_Action_Convert_Instances):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.run_Instance_Convershion(fnType=om.MFn.kTransform,objectType="transform")		
########################################################################
class Widget_Action_Convert_Shape_Instances(Base_Widget_Action_Convert_Instances):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.run_Instance_Convershion(fnType=om.MFn.kShape,objectType=None)
########################################################################
class Widget_Action_Remove_Intermediate_Objects(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		for item in cmds.ls("*.intermediateObject"):
			if cmds.getAttr(item) and cmds.objectType(item.split(".")[0],isType="mesh"):
				return True
		return False
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		items_to_scan = cmds.ls("*.intermediateObject")
		
		self.progressBar.set_Progress_Message("Scanning Items", len(items_to_scan), resetValue=True)

		for item in items_to_scan:
			node = item.split(".")[0]
			if cmds.getAttr(item) and cmds.objectType(node,isType="mesh"):
				cmds.delete(node)
				self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Remove_NameSpaces(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		return len([ns for ns in cmds.namespaceInfo( listOnlyNamespaces=True, recurse=True) if not ns in ['UI','shared']]) >= 1
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		items_to_scan = [item for item in cmds.namespaceInfo( listOnlyNamespaces=True, recurse=True) if not item in ['UI','shared']]
		items_to_scan.reverse()
		if len(items_to_scan):
			self.progressBar.set_Progress_Message("Removing Name Spaces",len(items_to_scan),True)
			for item in items_to_scan:
				if cmds.namespace( exists=item):
					cmds.namespace(removeNamespace=item,mergeNamespaceWithRoot=True)
					self.spinbox.setValue(self.spinbox.value()+1)
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Name Spaces To Remove",100,True)
			self.progressBar.setValue(100)
########################################################################
class Widget_Action_Remove_Unknown_Plugins(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		return len(none_To_List(cmds.unknownPlugin(q=True, list=True))) >= 1
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		items_to_scan = none_To_List(cmds.unknownPlugin(q=True, list=True))
		
		if len(items_to_scan):
			
			self.progressBar.set_Progress_Message("Removing Plugins", max_value=len(items_to_scan), resetValue=True)
			
			for item in items_to_scan:
				try:
					cmds.unknownPlugin(item, remove=True)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					pass
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Unknown Plugins To Remove", max_value=100, resetValue=True)
			self.progressBar.setValue(100)
########################################################################
class Widget_Action_Remove_Unknown_Nodes(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		return len(none_To_List(cmds.ls(type="unknown"))) >= 1
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = none_To_List(cmds.ls(type="unknown"))
		
		if len(items_to_scan):
			
			self.progressBar.set_Progress_Message("Removing Unknown Nodes", max_value=len(items_to_scan), resetValue=True)
			
			for item in items_to_scan:
				try:
					cmds.delete(item)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					pass
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Unknown Nodes To Remove", max_value=100, resetValue=True)
			self.progressBar.setValue(100)
########################################################################
class Widget_Action_Delete_Constraint(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		return len(none_To_List(cmds.ls(type="pointConstraint parentConstraint orientConstraint scaleConstraint aimConstraint".split()))) >= 1
	
	#----------------------------------------------------------------------
	def get_Items_Of_Interset(self):
		""""""
		return none_To_List(cmds.ls(type="pointConstraint parentConstraint orientConstraint scaleConstraint aimConstraint".split()))
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = self.get_Items_Of_Interset()
		
		if len(items_to_scan):
			self.progressBar.set_Progress_Message("Deleting Constraints", max_value=len(items_to_scan), resetValue=True)
			
			for item in items_to_scan:
				try:
					cmds.delete(item)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					pass
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Constraints To Delete", max_value=100, resetValue=True)
			self.progressBar.setValue(100)
########################################################################
class Widget_Action_Delete_Animation_Curves(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		iterDepend = om.MItDependencyNodes(om.MFn.kAnimCurve)
		return not iterDepend.isDone()
	#----------------------------------------------------------------------
	def get_Items_Of_Interset(self):
		""""""
		iterDepend = om.MItDependencyNodes(om.MFn.kAnimCurve)
		fn = om.MFnDependencyNode()
		curves = []
		while not iterDepend.isDone():
			fn.setObject(iterDepend.thisNode())
			curves.append(fn.name())
			iterDepend.next()
		return curves
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = self.get_Items_Of_Interset()
		if len(items_to_scan):
			
			self.progressBar.set_Progress_Message("Deleting Animation Curves", max_value=len(items_to_scan), resetValue=True)
			
			for item in items_to_scan:
				try:
					cmds.delete(item)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					pass
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Animation Curves Found", max_value=100, resetValue=True)
			self.progressBar.setValue(100)

########################################################################
class Widget_Action_Disassembling_Joint_Hierarchy(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		return len(none_To_List(cmds.ls(type="joint",l=True))) >= 1
	#----------------------------------------------------------------------
	def get_Cloest_Partent_Tranform(self,item):
		parent_item = get_Parent(item)
		while len(parent_item) and not cmds.objectType(parent_item[0],isType="transform"):
			parent_item = get_Parent(parent_item)
		if not len(parent_item):
			return None
		return parent_item[0]
	#----------------------------------------------------------------------
	def set_Parent_To_Nerest_Tranform(self,current_parent,items):
		current_parent = cmds.ls(get_Node_Path(current_parent),l=True)[0]
		cloest_tranform_parent = self.get_Cloest_Partent_Tranform(current_parent)
		if not current_parent == cloest_tranform_parent:
			cmds.parent(uuids_to_names(items),cloest_tranform_parent)
	#----------------------------------------------------------------------
	def get_Items_Of_Interset(self):
		""""""
		res = names_to_uuids( list(reversed(none_To_List(cmds.ls(type="joint",l=True)))))
		return res
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = self.get_Items_Of_Interset()
		self.progressBar.set_Progress_Message("Disassembling Joint Hierarchy", max_value=len(items_to_scan), resetValue=True)
		if len(items_to_scan):
			self.progressBar.set_Progress_Message("Disassembling Joint Hierarchy", max_value=len(items_to_scan), resetValue=True)	
			for item in items_to_scan:
				child_Transforms = none_To_List(cmds.listRelatives(get_Node_Path(item),type="transform",fullPath=True))
				if len(child_Transforms):
					child_Transforms_uuids = names_to_uuids(child_Transforms)
					self.set_Parent_To_Nerest_Tranform(item,child_Transforms_uuids)
					self.spinbox.setValue(self.spinbox.value()+1)
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Joints Found", max_value=100, resetValue=True)
			self.progressBar.setValue(100)
########################################################################################################## FIXES
########################################################################
class Widget_Action_Fix_Shape_Nodes_With_No_Geo(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()

		if not Global_Access.Top_Level_Node == None:
			items_to_scan = get_All_Geometry_Descendents(Global_Access.Top_Level_Node)
		else:
			items_to_scan = get_All_Geometry_Descendents(get_Transform_Assemblies())
			
		
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)

		for item in items_to_scan[::]:
			try:
				item_node = MNODE(item)
				if cmds.objectType(item,isType="mesh"):
					data = cmds.polyEvaluate(item, edge=True, face=True, triangle=True, vertex=True)
					if not any(data.values()):
						cmds.delete(item)
						self.spinbox.setValue(self.spinbox.value()+1)
			except StandardError:
				cmds.delete(item)
				self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Fix_Illegal_Unicode_Names(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = cmds.ls()
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)

		for item in items_to_scan:
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
					self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()			

########################################################################
class Widget_Action_Fix_PolySurface_Node_Names(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		return len(cmds.ls("*polySurface*"))>= 1
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = cmds.ls("*polySurface*")
		if len(items_to_scan):
			
			self.progressBar.set_Progress_Message("Fixing PolySurface Names",len(items_to_scan),True)
	
			for i, item in enumerate(items_to_scan):
				try:
					cmds.rename(item, "geo_poly_Surface_%i" % i)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					pass
				self.progressBar.add_Tick()
		else:
			self.progressBar.set_Progress_Message("No Items To Fix",100,True)
			self.progressBar.setValue(100)
########################################################################
class Widget_Action_Fix_Non_Unique_Transform_Names(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		return True
	#----------------------------------------------------------------------
	def get_Items_Of_Interset(self):
		""""""
		self.progressBar.set_Calculating()
		names_dict = {}
		iterDag = om.MItDag(om.MItDag.kBreadthFirst,om.MFn.kTransform)
		dagFn = om.MFnDagNode()
		
		while not iterDag.isDone():
			dagFn.setObject(iterDag.currentItem())
			if not dagFn.hasUniqueName():
				name     = dagFn.name()
				uid      = str(dagFn.uuid())
				if not name in names_dict.keys():
					names_dict[name]=[]
				names_dict[name].append(uid)
			iterDag.next()
		
		return names_dict
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		base_sufix = "_AWID_"
		
		items_to_scan = self.get_Items_Of_Interset()
		if len(items_to_scan.keys()):
			total_count = 0
			for name,uids in items_to_scan.iteritems():
				total_count += len(uids)
			
			self.progressBar.set_Progress_Message("Making Names Unique",total_count,True)
			
			for name,uids in items_to_scan.iteritems():
				new_base_name = name + base_sufix
				for idnum,uid in enumerate(uids):
					new_name       = new_base_name + str(idnum).zfill(4)
					try:
						cmds.rename(get_Node_Path(uid),new_name,ignoreShape=True)
						self.spinbox.setValue(self.spinbox.value()+1)
						self.progressBar.add_Tick()
					except:
						om.MGlobal.displayWarning("Could Not Unlock {}".format(get_Node_Path(uid)))
		else:
			self.progressBar.set_Progress_Message("Making Names Unique",100,True)
			self.progressBar.setValue(100)
########################################################################
class Widget_Action_Fix_Inherits_Transform(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		for item in cmds.ls("*.inheritsTransform"):
			if not cmds.getAttr(item):
				return True
		return False
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		items_to_scan = cmds.ls("*.inheritsTransform")
		
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)

		for item in items_to_scan:
			if not cmds.getAttr(item):
				cmds.setAttr(item,True)
				self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()	
########################################################################
class Widget_Action_Fix_Visible_In_Reflection_And_Refractions(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		for item in get_All_Geometry_Descendents(Global_Access.Top_Level_Node):
			if not cmds.getAttr(item+".visibleInReflections") or not cmds.getAttr(item+".visibleInRefractions"):
				return True
		return False
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		items_to_scan = get_All_Geometry_Descendents(Global_Access.Top_Level_Node)
		[item for item in cmds.ls("*.visibleInReflections") if not cmds.getAttr(item)] + [item for item in cmds.ls("*.visibleInRefractions") if not cmds.getAttr(item)]
		
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)

		for item in items_to_scan:
			
			if not cmds.getAttr(item+".visibleInReflections"):
				cmds.setAttr(item+".visibleInReflections",True)
				self.spinbox.setValue(self.spinbox.value()+1)
				
			if not cmds.getAttr(item+".visibleInRefractions"):
				cmds.setAttr(item+".visibleInRefractions",True)
				self.spinbox.setValue(self.spinbox.value()+1)
				
			self.progressBar.add_Tick()

########################################################################
class Widget_Action_Fix_Default_Uv_Set_Name(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		for item in cmds.ls("*.uvSet[0].uvSetName"):
			if not cmds.getAttr(item) == "map1" and not cmds.getAttr(item) == None:
				return True
		return False
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = cmds.ls("*.uvSet[0].uvSetName")
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)

		for item in items_to_scan:
			default_uv_set = cmds.getAttr(item)
			if default_uv_set != "map1" and not default_uv_set == None:
				node = item.split(".")[0]
				cmds.polyUVSet(node, rename=True, newUVSet='map1', uvSet=default_uv_set)
				if not cmds.polyUVSet( node, query=True, currentUVSet=True) == 'map1':
					cmds.polyUVSet(node,currentUVSet=True, uvSet='map1')
					self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Fix_Dirty_Meshs(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def read_History_File(self):
		""""""
		with open(Global_Access.Mesh_Cleanup_Log,"r") as f:
			data = f.read()
			lines = data.splitlines()
		return lines
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = self.read_History_File()
		self.progressBar.set_Progress_Message("Cleaning Dirty Polys",len(items_to_scan),True)
		
		for item in items_to_scan:
			if item.startswith("# Warning: The mesh ") and item.endswith(" contains invalid or unused components.  These can be cleaned up using the Mesh Cleanup dialog. # "):
				name = item.replace("# Warning: The mesh ","").replace(" contains invalid or unused components.  These can be cleaned up using the Mesh Cleanup dialog. # ","")
				if cmds.objExists(name):
					cmds.polyClean(name,cleanVertices=True)
					self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()
		cmds.delete( all=True, constructionHistory=True)

########################################################################################################## EDITS
########################################################################
class Widget_Action_Freeze_All_Transforms(Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()

		if not Global_Access.Top_Level_Node == None:
			items_to_scan = [Global_Access.Top_Level_Node]
		else:
			items_to_scan = get_Transform_Assemblies()

		items_to_scan.extend(cmds.listRelatives(items_to_scan, allDescendents=True, path=True, type='transform'))
		
		self.progressBar.set_Progress_Message("Freezing Transforms",len(items_to_scan)*2,True)

		for item in items_to_scan:
			try:
				cmds.makeIdentity(item,apply=True,t=True,r=True,s=True,n=False, pn=True)
			except:
				pass
			self.progressBar.add_Tick()

		self.progressBar.set_Progress_Message("Zeroing Pivots")

		for item in items_to_scan:
			try:
				cmds.makeIdentity(item,apply=False,t=True,r=True,s=True,n=False, pn=True)
			except:
				pass
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Break_Attribute_Connections(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		
		items_to_scan = get_All_Transform_Descendents(Global_Access.Top_Level_Node)
		
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan)*9,True)

		for item in items_to_scan:
			for att in [".translateX",".translateY",".translateZ",".rotateX",".rotateY",".rotateZ",".scaleX",".scaleY",".scaleZ"]:
				cons = none_To_List(cmds.listConnections(item+att,d=True,plugs=True))
				for con in cons:
					try:
						cmds.disconnectAttr(con,attr)
						self.spinbox.setValue(self.spinbox.value()+1)
					except:
						#self.gui_widget.Extraction_Log_Text.insertHtml('<html><head/><body><p><span style=" font-size:8.25pt; color:#ff0000;">Warning:</span><span style=" font-size:8.25pt; color:#ffffff;"> Could Not Dissconnect </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{} </span><span style=" font-size:8.25pt; color:#ffffff;">From </span><span style=" font-size:8.25pt; font-weight:600; color:#55ff00;">{}<br/></span></p></body></html>'.format(con,attr))
						continue
				self.progressBar.add_Tick()
########################################################################
class Widget_Action_Unlock_Dag_Objects(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = get_All_Descendents(Global_Access.Top_Level_Node)
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)
		
		for item in items_to_scan:
			if is_Node_Locked(item):
				unlock_Node(item)
				self.spinbox.setValue(self.spinbox.value()+1)
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Unlock_Transform_Attributes(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = cmds.ls(["*.translateX","*.translateY","*.translateZ","*.rotateX","*.rotateY","*.rotateZ","*.scaleX","*.scaleY","*.scaleZ"])
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)
		
		for item in items_to_scan:
			if cmds.getAttr(item,lock=True):
				try:
					cmds.setAttr(item,lock=False)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					pass
			self.progressBar.add_Tick()	

########################################################################################################## OPTIONAL
########################################################################
class Widget_Action_Replace_All_Shaders_With_Lambers(Multi_Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBarA.set_Calculating()
		self.progressBarB.reset()
		
		shading_Engines = get_All_Non_Default_Shader_Engines_With_Materials()
		
		if len(shading_Engines):
			self.progressBarA.set_Progress_Message("Replacing Shaders With Lamberts",len(shading_Engines),True)
			for engine in shading_Engines:
				
				shader = get_Shader_Engine_Material(engine)
				
				cmds.lockNode(shader,lock=False)
				cmds.lockNode(engine,lock=False)
	
				old_shader = cmds.rename(shader,shader+"_old")
				old_engine = cmds.rename(engine,engine+"_old")
	
				shader = create_Lambert_Shader(shader)
				engine = create_Shader_Engine(shader)
				
				assign_Material_To_Engine(shader,engine)
				
				for att,typ in [(".color","double3"),(".transparency","double3")]:
					try:
						r,g,b = cmds.getAttr(old_shader+att)[0]
						cmds.setAttr(shader+att,r,g,b, type=typ)
					except:
						pass
					
				self.progressBarB.set_Calculating()
				members =  get_Shader_Engine_Members(old_engine)
				
				if len(members):
					self.progressBarB.set_Progress_Message("Assigning Members To Lambert",len(members),True)
					for member in members:
						try:
							add_Shader_Engine_Members(member,engine)
						except:
							pass
						self.progressBarB.add_Tick()
					self.progressBarB.reset()
				self.progressBarA.add_Tick()
		else:
			self.progressBarA.reset()
########################################################################
class Widget_Action_Replace_Master_Layer_Shader_Assignments(Multi_Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def get_ShadingEngine_dict(self,shading_Engines):
		res    = dict()
		self.progressBarB.set_Progress_Message("Collection Shadering Assignments",len(shading_Engines),True)
		for engine in shading_Engines:
			material = get_Shader_Engine_Material(engine)
			self.progressBarB.set_Progress_Message("Scanning {}".format(material))
			#check_If_Shading_Engine_Contains_Face_Assignments(engine, items, log_text)
			items = get_Shader_Engine_Members(engine)
			res[engine] = items
			self.progressBarB.add_Tick()
		self.progressBarB.reset()
		return res
	#----------------------------------------------------------------------
	def apply_Shading_Engine_dict(self,data):
		
		self.progressBarB.set_Progress_Message("Applying Shading Assignments",len(data.keys()),True)
		
		for sg,items in data.iteritems():
			if len(items):
				material = get_Shader_Engine_Material(sg)
				self.progressBarB.set_Progress_Message("Assigning {} Objects to {}".format(len(items),material))
				add_Shader_Engine_Members(items,sg)
			self.progressBarB.add_Tick()
		self.progressBarB.reset()
	#----------------------------------------------------------------------
	def Shader_Overides_To_Master_Layer(self,layer,shading_Engines):
		""""""
		self.progressBarA.set_Progress_Message("Switching To Layer {}".format(layer),4,True)
		
		set_Current_Render_Layer(layer)
		
		cmds.refresh(f=True)
		
		self.progressBarA.add_Tick()
		
		self.progressBarA.set_Progress_Message("Collecting Assignments For Layer {}".format(layer))
		
		overides_assignments = self.get_ShadingEngine_dict(shading_Engines)

		self.progressBarA.add_Tick()
		
		self.progressBarA.set_Progress_Message("Switching To Layer defaultRenderLayer")
		
		set_Current_Render_Layer("defaultRenderLayer")
		
		cmds.refresh(f=True)
		
		self.progressBarA.add_Tick()
		
		self.progressBarA.set_Progress_Message("Apply Collected Assignments")
		
		self.apply_Shading_Engine_dict(overides_assignments)
		
		self.progressBarA.add_Tick()
		
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		use_layer = self.window().useRenderLayerComboBox.currentText()
		if cmds.objExists(use_layer) and cmds.objectType(use_layer)=="renderLayer" and not use_layer == "defaultRenderLayer":
			self.progressBarA.set_Calculating()
			
			shading_Engines = get_All_Non_Default_Shader_Engines_With_Materials()
			
			self.Shader_Overides_To_Master_Layer(use_layer,shading_Engines)
			
########################################################################
class Widget_Action_Remove_Multiple_UV_Sets_From_Meshes(Fixed_Items_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def is_Scan_Needed(self):
		""""""
		meshs = cmds.ls(type="mesh")
		return len(meshs) == len(cmds.polyUVSet(meshs,query=True, allUVSets=True))
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		items_to_scan = cmds.ls(type="mesh",l=True)
		self.progressBar.set_Progress_Message("Scanning Items",len(items_to_scan),True)
		
		for item in items_to_scan:
			uv_sets = none_To_List(cmds.polyUVSet( item, query=True, allUVSets=True))
			if len(uv_sets) > 1:
				try:
					default_uv_set = cmds.getAttr(item+".uvSet[0].uvSetName")
					#print "trying"

					if not default_uv_set == "map1":
						cmds.polyUVSet(item, rename=True, newUVSet='map1', uvSet=default_uv_set)

					if not cmds.polyUVSet( item, query=True, currentUVSet=True) == 'map1':
						cmds.polyUVSet(item, currentUVSet=True, uvSet='map1')

					for uv_set in cmds.polyUVSet( item, query=True, allUVSets=True):
						if not uv_set == "map1":
							cmds.polyUVSet(item, delete=True, uvSet=uv_set)
					self.spinbox.setValue(self.spinbox.value()+1)
				except:
					#print "Failed"
					pass
			self.progressBar.add_Tick()

########################################################################
class Widget_Action_Remove_All_Render_Layers(Scan_Progress_Action_Widget):
	""""""
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Calculating()
		set_Current_Render_Layer("defaultRenderLayer")
		layers = get_All_Non_Default_Render_Layers()
		self.progressBar.set_Progress_Message("Removing Render Layers",len(layers),True)

		for layer in layers:
			cmds.delete(layer)
			self.progressBar.add_Tick()

########################################################################################################## REBUILDING
########################################################################
class Widget_Action_Import_Extracted_Data(Scan_Progress_Action_Widget):
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Progress_Message("Loading Extracted Json Data",3,True)
		Global_Access.load_Json_Data()
		
		self.progressBar.set_Progress_Message("Opening Extract Alembic File")
		self.progressBar.add_Tick()
		
		Global_Access.Import_Alembic()
		
		if Global_Access.Json_Data["shaders_should_be_loaded"]:
			self.progressBar.set_Progress_Message("Importing Extract Shader File")
			self.progressBar.add_Tick()
			Global_Access.Import_Shaders()
		else:
			self.progressBar.set_Progress_Message("Skiped Shader File")
			self.progressBar.add_Tick()
		
		self.progressBar.add_Tick()
########################################################################
class Widget_Action_Create_Display_Layer_Data(Scan_Progress_Action_Widget):
	
	#----------------------------------------------------------------------
	def add_Members(self,layer_data):
		""""""
		members = []
		for idnum in layer_data['assignment_ids']:
			node = Global_Access.Node_ID_Dict.get(idnum)
			members.append(node)
		cmds.editDisplayLayerMembers(layer_data['name'], members, noRecurse=True)
		
	#----------------------------------------------------------------------
	def create(self,layer_data):
		""""""
		node_name = cmds.createDisplayLayer(name=layer_data['name'], makeCurrent=False, empty=True, noRecurse=True)
		layer_data['name'] = node_name
		cmds.setAttr(node_name+".color", layer_data['color'])

	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		if len(Global_Access.Json_Data["display_Layers"]):			
			self.progressBar.set_Progress_Message("Building Layers", max_value=len(Global_Access.Json_Data["display_Layers"]), resetValue=True)
			
			for layer_data in Global_Access.Json_Data["display_Layers"]:
				self.create(layer_data)
				self.add_Members(layer_data)
				self.progressBar.add_Tick()
		else:
			self.progressBar.reset()
########################################################################
class Widget_Action_Assign_Shader_Engine_Members(Scan_Progress_Action_Widget):
	#----------------------------------------------------------------------
	def add_Members(self,shader_data):
		""""""
		shader = Global_Access.Node_ID_Dict.get(shader_data["idnum"])
		members = []
		for id_num in shader_data["assignment_ids"]:
			members.append(Global_Access.Node_ID_Dict.get(id_num))
		try:
			cmds.sets(members, edit=True, forceElement=shader)
		except Exception as e:
			om.MGlobal.displayWarning("There Was And Problem Assigning {} With an error message of {}".format(str(shader),e.message))

	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		self.progressBar.set_Progress_Message("Assigning Shaders", max_value=len(Global_Access.Json_Data["shading_engines"]), resetValue=True)
		
		for shader_data in Global_Access.Json_Data["shading_engines"]:
			self.add_Members(shader_data)
			self.progressBar.add_Tick()
########################################################################
class Widget_Action_Populate_Node_Id_Dict(Scan_Progress_Action_Widget):
	#----------------------------------------------------------------------
	def run_Action(self):
		""""""
		Global_Access.Node_ID_Dict = {}
		self.progressBar.set_Calculating()
		
		items_to_scan = cmds.ls("*.AW_Extractor_ID",recursive=True,l=True)
		
		self.progressBar.set_Progress_Message("Scanning IDs",len(items_to_scan),True)
		
		for item in items_to_scan:
			value = cmds.getAttr(item)
			node = item.split(".")[0]
			Global_Access.Node_ID_Dict[value] = node
			self.progressBar.add_Tick()

########################################################################################################## ACTION STATUS FEEDBACK WIDGETS
########################################################################
class Tickalbe_ProgressBar(QT.QProgressBar):
	""""""
	progress_look   = 'QProgressBar {font: 75 10pt ; background-color:black; color:yellow; border: 1px solid red; border-radius: 1px;} QProgressBar::chunk {background-color: green;}'
	calculating_look = 'QProgressBar {font: 75 10pt; background-color:black; color:yellow; border: 1px solid red; border-radius: 1px;} QProgressBar::chunk {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.5 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 0));}'
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Tickalbe_ProgressBar,self).__init__(parent)
		self.setStyleSheet(self.progress_look)
		self.setAlignment(QT.Qt.AlignCenter)
	#----------------------------------------------------------------------
	def add_Tick(self):
		""""""
		self.setValue(self.value()+1)
	#----------------------------------------------------------------------
	def set_Calculating(self,on=True):
		""""""
		if on:
			self.setFormat("Calculating")
			self.setRange(0,100)
			self.setValue(100)
		else:
			self.setStyleSheet(self.progress_look)
		
QT.ui_Loader.registerCustomWidget(Tickalbe_ProgressBar)

########################################################################
class Widget_Action_ProgressBar(Tickalbe_ProgressBar):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Widget_Action_ProgressBar,self).__init__(parent)
		self.setSizePolicy(QT.QSizePolicy(QT.QSizePolicy.Expanding,QT.QSizePolicy.Expanding))
		f = self.font()
		f.setPointSize(8)
		self.setFont(f)
	
	#----------------------------------------------------------------------
	def set_Progress_Message(self,message,max_value=0,resetValue=False):
		""""""
		self.setFormat( message +" %p%")
		if max_value:
			self.setRange(0,max_value)
		if resetValue:
			self.setValue(0)
		if max_value or resetValue:
			self.set_Calculating(False)
########################################################################
class Changed_Item_Count_SpinBox(QT.QSpinBox):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Changed_Item_Count_SpinBox,self).__init__()
		self.setMaximum(99999)
		self.setReadOnly(True)
		self.setSizePolicy(QT.QSizePolicy(QT.QSizePolicy.Minimum,QT.QSizePolicy.Expanding))
		self.setButtonSymbols(self.ButtonSymbols.NoButtons)

########################################################################################################## CUSTOM LAYOUTS
########################################################################
class Zero_Content_Margines_VBoxLayout(QT.QVBoxLayout):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Zero_Content_Margines_VBoxLayout,self).__init__(parent)
		self.setSpacing(0)
		self.setContentsMargins(0,0,0,0)
########################################################################
class Zero_Content_Margines_HBoxLayout(QT.QHBoxLayout):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Zero_Content_Margines_HBoxLayout,self).__init__(parent)
		self.setSpacing(5)
		self.setContentsMargins(0,0,0,0)
########################################################################################################## WIDGET ACTION CONTAINERS
########################################################################
class Widget_Actions_Form(QT.QFormLayout):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Widget_Actions_Form,self).__init__(parent)
		self.setSpacing(5)
		self.setContentsMargins(1,1,1,1)

	#----------------------------------------------------------------------
	def add_Widget_Action(self,actionName,widget,hidden=False):
		""""""
		wig = widget()
		isinstance(wig,Extraction_Action_Widget)
		self.addRow(actionName,wig)
		label = self.labelForField(wig)
		effect = QT.QGraphicsDropShadowEffect(label)
		effect.setColor(QT.Qt.black)
		effect.setOffset(1)
		effect.setBlurRadius(2)
		label.setGraphicsEffect(effect)
		f = label.font()
		f.setPointSize(12)
		label.setFont(f)
		if hidden:
			self.hide_Action(wig)
		return wig
	#----------------------------------------------------------------------
	def get_Action_Widgets(self):
		""""""
		return [self.itemAt(index,self.ItemRole.FieldRole).widget() for index in range(self.rowCount())]
	#----------------------------------------------------------------------
	action_Widgets = property(get_Action_Widgets)
	#----------------------------------------------------------------------
	def run_Optimize_Check(self):
		""""""
		for wig in self.action_Widgets:
			if not wig.is_Scan_Needed():
				self.hide_Action(wig)
				
	#----------------------------------------------------------------------
	def run_Actions(self):
		""""""
		for wig in self.action_Widgets:
			wig.do_Run_Action()
	#----------------------------------------------------------------------
	def has_A_Visable_Action(self):
		""""""
		for wig in self.action_Widgets:
			if wig.isVisible():
				return True
		return False
	#----------------------------------------------------------------------
	def hide_Action(self,widget):
		""""""
		label = self.labelForField(widget)
		widget.setVisible(False)
		label.setVisible(False)
		
		if not self.has_A_Visable_Action():
			self.parentWidget().setVisible(False)
	#----------------------------------------------------------------------
	def show_Action(self,widget):
		""""""
		label = self.labelForField(widget)
		widget.setVisible(True)
		label.setVisible(True)
		self.parentWidget().setVisible(True)

########################################################################
class Widget_Actions_Group(QT.QGroupBox):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		"""Constructor"""
		super(Widget_Actions_Group,self).__init__(parent)
		layout = Widget_Actions_Form()
		self.setLayout(layout)
		self.setSizePolicy(QT.QSizePolicy(QT.QSizePolicy.Policy.Minimum,QT.QSizePolicy.Policy.Maximum))
		if False:
			isinstance(self.action_items_form_layout,Widget_Actions_Form)
	#----------------------------------------------------------------------
	def layout(self):
		""""""
		res = super(Widget_Actions_Group,self).layout()
		isinstance(res,Widget_Actions_Form)
		return res
	#----------------------------------------------------------------------
	def get_Action_Items_Form_Layout(self):
		""""""
		return self.layout()
	#----------------------------------------------------------------------
	action_items_form_layout = property(fget=get_Action_Items_Form_Layout)
	#----------------------------------------------------------------------
	def add_Widget_Action(self,actionName,widget,hidden=False):
		""""""
		return self.action_items_form_layout.add_Widget_Action(actionName, widget, hidden)
	#----------------------------------------------------------------------
	def get_Action_Widgets(self):
		""""""
		return self.action_items_form_layout.get_Action_Widgets()
	#----------------------------------------------------------------------
	def run_Optimize_Check(self):
		""""""
		self.action_items_form_layout.run_Optimize_Check()
	#----------------------------------------------------------------------
	def run_Actions(self):
		""""""
		self.action_items_form_layout.run_Actions()
	#----------------------------------------------------------------------
	def has_A_Visable_Action(self):
		""""""
		return self.action_items_form_layout.has_A_Visable_Action()
	#----------------------------------------------------------------------
	def hide_Action(self,widget):
		""""""
		self.action_items_form_layout.hide_Action(widget)
	#----------------------------------------------------------------------
	def show_Action(self,widget):
		""""""
		self.action_items_form_layout.show_Action(widget)

########################################################################
class Alembic_Extraction_Widget_Action_Group_Builder(QT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def add_Action_Group(self,name):
		""""""
		grp = Widget_Actions_Group()
		grp.setTitle(name)
		self.layout().addWidget(grp)
		return grp

QT.ui_Loader.registerCustomWidget(Alembic_Extraction_Widget_Action_Group_Builder)

########################################################################
class _CODE_COMPLEATION_HELPER(QT.QWidget):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		''''''
		super(_CODE_COMPLEATION_HELPER,self).__init__(parent=parent)
		if False:
			self.tabWidget                              = QT.QTabWidget()
			self.Extraction_Tab                         = QT.QWidget()
			self.Extraction_Contorls_Frame              = QT.QFrame()
			self.groupBox                               = QT.QGroupBox()
			self.Extraction_Collection_Groups_frame_2   = QT.QFrame()
			self.auto_import_CheckBox                   = QT.QCheckBox()
			self.perform_Scene_CleanUp_CheckBox         = QT.QCheckBox()
			self.replace_Shaders_With_Lamberts_CheckBox = QT.QCheckBox()
			self.remove_Non_Default_UV_Sets_CheckBox    = QT.QCheckBox()
			self.GBX_Options                            = QT.QGroupBox()
			self.Frame                                  = QT.QFrame()
			self.Top_Level_Node_Input                   = QT.QLineEdit()
			self.Set_To_Selected_Button                 = QT.QPushButton()
			self.useRenderLayer_Frame                   = QT.QFrame()
			self.useRenderLayerLabel                    = QT.QLabel()
			self.useRenderLayerComboBox                 = QT.QComboBox()
			self.removeOtherLayersCheckBox              = QT.QCheckBox()
			self.Scene_Scan_progressBar                 = Tickalbe_ProgressBar()
			self.Extraction_Action_Groups_scrollArea    = QT.QScrollArea()
			self.Extraction_Action_Groups               = Alembic_Extraction_Widget_Action_Group_Builder()
			self.Extraction_Data_Collection_Groups      = Alembic_Extraction_Widget_Action_Group_Builder()
			self.Export_Button                          = QT.QPushButton()
			self.FRAME_Extraction_Log                   = QT.QFrame()
			self.GBX_Extraction_Log                     = QT.QGroupBox()
			self.Extraction_Log_Text                    = QT.QTextEdit()
			self.Import_Last_Extraction_Tab             = QT.QWidget()
			self.Rebuild_Collection_Groups_widget       = Alembic_Extraction_Widget_Action_Group_Builder()
			self.Import_Button                          = QT.QPushButton()
			self.Rebuild_Log_Frame                      = QT.QFrame()
			self.Rebuild_Log_GBX                        = QT.QGroupBox()
			self.Rebuild_Log_Text                       = QT.QTextEdit()
			self.verticalLayout_16                      = QT.QVBoxLayout()
			self.horizontalLayout_3                     = QT.QHBoxLayout()
			self.verticalLayout_10                      = QT.QVBoxLayout()
			self.verticalLayout_7                       = QT.QVBoxLayout()
			self.verticalLayout_9                       = QT.QVBoxLayout()
			self.verticalLayout_14                      = QT.QVBoxLayout()
			self.gridLayout                             = QT.QGridLayout()
			self.verticalLayout_11                      = QT.QVBoxLayout()
			self.horizontalLayout_2                     = QT.QHBoxLayout()
			self.verticalLayout                         = QT.QVBoxLayout()
			self.horizontalLayout                       = QT.QHBoxLayout()
			self.verticalLayout_4                       = QT.QVBoxLayout()
			self.verticalLayout_13                      = QT.QVBoxLayout()
			self.verticalLayout_5                       = QT.QVBoxLayout()
			self.verticalLayout_3                       = QT.QVBoxLayout()
			self.verticalLayout_2                       = QT.QVBoxLayout()
			self.verticalLayout_8                       = QT.QVBoxLayout()
			self.horizontalLayout_4                     = QT.QHBoxLayout()
			self.verticalLayout_15                      = QT.QVBoxLayout()
			self.Rebuild_Collection_Groups_Layout       = QT.QVBoxLayout()
			self.verticalLayout_6                       = QT.QVBoxLayout()
			self.verticalLayout_12                      = QT.QVBoxLayout()

master_StyleSheet = """
.QGroupBox, .QFrame, .QWidget,.QScrollArea{  
	color: rgb(255, 0, 0);
	background-color: rgb(0, 0, 0);
}

.QTextEdit{  
	color: rgb(255, 0, 0);
	background-color: rgb(0, 0, 0);
}

.QLabel{
color: rgb(255,0, 0);
}

.QProgressBar{
color: rgb(0, 0,0);
}

.QCheckBox{
color: rgb(255, 255, 255);
}
"""

########################################################################
class Alembic_Asset_Extraction_GUI(MayaQWidgetBaseMixin,_CODE_COMPLEATION_HELPER):
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		""""""
		super(Alembic_Asset_Extraction_GUI,self).__init__(parent)
	#----------------------------------------------------------------------
	def showEvent(self,event):
		""""""
		super(Alembic_Asset_Extraction_GUI, self).showEvent(event)
	#----------------------------------------------------------------------
	def reset(self):
		""""""
		for progressBar in self.findChildren(QT.QProgressBar):
			progressBar.setValue(0)

		for spinbox in self.findChildren(QT.QSpinBox):
			spinbox.setValue(0)
	
	#----------------------------------------------------------------------
	def _set_Option_Values(self):
		""""""
		if not len(get_All_Non_Default_Render_Layers()):
			self.useRenderLayer_Frame.setVisible(False)
			self.removeOtherLayersCheckBox.setChecked(False)
		else:
			for layer in sorted(get_All_Non_Default_Render_Layers()):
				self.useRenderLayerComboBox.addItem(layer)
				
		meshs = cmds.ls(type="mesh")
		if len(meshs) == len(none_To_List(cmds.polyUVSet(meshs,query=True, allUVSets=True))):
			self.remove_Non_Default_UV_Sets_CheckBox.setVisible(False)
	#----------------------------------------------------------------------
	def _make_Signal_Connections(self):
		""""""
		self.Set_To_Selected_Button.clicked.connect(self.on_Set_To_Selected_Button_Clicked)
		#self.Export_Button.clicked.connect(self.action_group_Extraction_Fixing_And_Standedize.run_Optimize_Check)
		self.Export_Button.clicked.connect(self.on_Export_Button_Clicked)
		self.remove_Non_Default_UV_Sets_CheckBox.stateChanged.connect(self.on_remove_Non_Default_UV_Sets_CheckBox_stateChanged)
		self.replace_Shaders_With_Lamberts_CheckBox.stateChanged.connect(self.on_replace_Shaders_With_Lamberts_CheckBox_stateChanged)
		self.removeOtherLayersCheckBox.stateChanged.connect(self.on_remove_Other_Layers_CheckBox_stateChanged)
		self.useRenderLayerComboBox.currentIndexChanged.connect(self.on_use_Render_Layer_ComboBox_currentIndexChanged)
		self.Import_Button.clicked.connect(self.on_Import_Button_Clicked)
	#----------------------------------------------------------------------
	def _run_setup(self):
		""""""
		self.setStyleSheet(master_StyleSheet)
		self._insetup = True
		
		self.Top_Level_Node_Input.textChanged.connect(self.on_Top_Level_Input_Changed)
		self.Top_Level_Node_Input.setText(find_Most_Likely_Master_Item())
		
		self.Scene_Scan_progressBar.setVisible(False)
		
		self._set_Option_Values()
		
		#----------------------------------------------------------------------
		self.action_group_Instances_Removal = self.Extraction_Action_Groups.add_Action_Group("Instances Removal")
		
		self.wig_action_check_for_instances                = self.action_group_Instances_Removal.add_Widget_Action("Check If Instances Exist", Widget_Action_Does_Scene_Contain_Instances)
		self.wig_action_convert_group_instances            = self.action_group_Instances_Removal.add_Widget_Action("Convert Group Instances", Widget_Action_Convert_Group_Instances)
		self.wig_action_convert_transform_instances        = self.action_group_Instances_Removal.add_Widget_Action("Convert Transform Instances", Widget_Action_Convert_Transform_Instances)
		self.wig_action_convert_shape_instances            = self.action_group_Instances_Removal.add_Widget_Action("Convert Shape Instances", Widget_Action_Convert_Shape_Instances)
		
		for wig in [self.wig_action_convert_group_instances,self.wig_action_convert_transform_instances,self.wig_action_convert_shape_instances]:
			wig.set_Depends_On_Widget(self.wig_action_check_for_instances)
		
		self.action_group_Pre_Scan_Actions = self.Extraction_Action_Groups.add_Action_Group("Pre Scan Actions")
		self.wig_action_Replace_Master_Layer_Shader_Assignments = self.action_group_Pre_Scan_Actions.add_Widget_Action("Set Shader Assignment With Layer", Widget_Action_Replace_Master_Layer_Shader_Assignments,hidden=True)
		self.wig_action_Remove_All_Render_Layers                = self.action_group_Pre_Scan_Actions.add_Widget_Action("Remove Non Default Render Layers", Widget_Action_Remove_All_Render_Layers, hidden = not self.removeOtherLayersCheckBox.isChecked())
		self.wig_action_Replace_All_Shaders_With_Lambers        = self.action_group_Pre_Scan_Actions.add_Widget_Action("Replace Shaders With Lamberts", Widget_Action_Replace_All_Shaders_With_Lambers,hidden=True)
		
		#----------------------------------------------------------------------
		self.action_group_Extraction_Fixing_And_Standedize = self.Extraction_Action_Groups.add_Action_Group("Extraction Fixing And Standedize")
		
		self.wig_action_Remove_NameSpaces                                 = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Remove NameSpaces", Widget_Action_Remove_NameSpaces)
		self.wig_action_Remove_Unknown_Nodes                              = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Remove Unknown Nodes", Widget_Action_Remove_Unknown_Nodes)
		self.wig_action_Remove_Unknown_Plugins                            = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Remove Unknown Plugins", Widget_Action_Remove_Unknown_Plugins)
		self.wig_action_Unlock_Dag_Objects                                = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Unlock Dag Objects", Widget_Action_Unlock_Dag_Objects)
		self.wig_action_Unlock_Transform_Attributes                       = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Unlock Transform Attributes", Widget_Action_Unlock_Transform_Attributes)
		self.wig_action_Fix_Shape_Nodes_With_No_Geo                       = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Remove Shapes With No Geo", Widget_Action_Fix_Shape_Nodes_With_No_Geo)
		self.wig_action_Action_Delete_Constraint                          = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Delete Constraints", Widget_Action_Delete_Constraint)
		self.wig_action_Action_Delete_Animation_Curves                    = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Delete Animation Curves", Widget_Action_Delete_Animation_Curves)
		self.wig_action_Fix_Bad_Unicode_Node_Names                        = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Fix Bad Unicode Names", Widget_Action_Fix_Illegal_Unicode_Names)
		self.wig_action_Fix_Non_Unique_Transform_Names                    = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Fix Non Unique Transform Names", Widget_Action_Fix_Non_Unique_Transform_Names)
		self.wig_action_Fix_PolySurface_Node_Names                        = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Fix PolySurface Names", Widget_Action_Fix_PolySurface_Node_Names)
		self.wig_action_Break_Attribute_Connections                       = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Break Connections", Widget_Action_Break_Attribute_Connections)
		self.wig_action_Fix_Bad_Intermediate_Objects                      = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Remove Intermediate Objects", Widget_Action_Remove_Intermediate_Objects)
		self.wig_action_Fix_Disassembling_Joint_Hierarchy                 = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Disassembling Joint Hierarchy", Widget_Action_Disassembling_Joint_Hierarchy)
		self.wig_action_Fix_Bad_Default_Uv_Sets                           = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Standerdize Default Uv Set", Widget_Action_Fix_Default_Uv_Set_Name)
		self.wig_action_Fix_Fix_Bad_Visible_In_Reflection_And_Refractions = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Force Reflection & Refractions", Widget_Action_Fix_Visible_In_Reflection_And_Refractions)
		self.wig_action_fix_Bad_Inherits_Transform_Plugs                  = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Force Inherits Transforms", Widget_Action_Fix_Inherits_Transform)
		self.wig_action_Freeze_All_Transforms                             = self.action_group_Extraction_Fixing_And_Standedize.add_Widget_Action("Freeze Transforms", Widget_Action_Freeze_All_Transforms)
		
		#---------------------------------------------------------------------- optional_extraction_steps
		self.action_group_optional_extraction_steps = self.Extraction_Action_Groups.add_Action_Group("Optional Extraction Steps")
		self.wig_action_Remove_Non_Default_UV_Sets  = self.action_group_optional_extraction_steps.add_Widget_Action("Remove Non Default UV Sets", Widget_Action_Remove_Multiple_UV_Sets_From_Meshes, hidden=True)
		
		#---------------------------------------------------------------------- extraction_data
		self.action_group_extraction_data = self.Extraction_Data_Collection_Groups.add_Action_Group("Extraction Data")
		
		self.wig_action_Add_Extractor_Id_Tags   = self.action_group_extraction_data.add_Widget_Action("Add Extractor Ids", Widget_Action_Add_Extractor_Id_Tags)
		self.wig_action_Get_Display_Layers_Data = self.action_group_extraction_data.add_Widget_Action("Building Display Layers Data", Widget_Action_Get_Display_Layers_Data)
		self.wig_action_Get_Shader_Engine_Data  = self.action_group_extraction_data.add_Widget_Action("Building Material Data", Widget_Action_Get_Shader_Engine_Data)
		
		#---------------------------------------------------------------------- rebuild_data
		self.action_group_rebuild_data         = self.Rebuild_Collection_Groups_widget.add_Action_Group("Rebuild")
		
		self.wig_action_Import_Extracted_Data         = self.action_group_rebuild_data.add_Widget_Action("Importing Extracted Files", Widget_Action_Import_Extracted_Data)
		self.wig_action_Populate_Node_Id_Dict         = self.action_group_rebuild_data.add_Widget_Action("Populating AW Extraction ID Data", Widget_Action_Populate_Node_Id_Dict)
		self.wig_action_Fix_Dirty_Meshs               = self.action_group_rebuild_data.add_Widget_Action("Fixing Diry Mesh Verts", Widget_Action_Fix_Dirty_Meshs)
		self.wig_action_Create_Display_Layer_Data     = self.action_group_rebuild_data.add_Widget_Action("Create And Populate Display Layers", Widget_Action_Create_Display_Layer_Data)
		self.wig_action_Assign_Shader_Engine_Members  = self.action_group_rebuild_data.add_Widget_Action("Reassigning Materials", Widget_Action_Assign_Shader_Engine_Members)
		
		self._make_Signal_Connections()
		self._insetup = False
		
	#----------------------------------------------------------------------
	def load_Json_Data(self):
		""""""
		Global_Access.load_Json_Data()
	#----------------------------------------------------------------------
	def save_Json_Data(self):
		""""""
		Global_Access.Json_Data = dict()
		Global_Access.Json_Data["display_Layers"] = self.wig_action_Get_Display_Layers_Data.result
		Global_Access.Json_Data["shading_engines"] = self.wig_action_Get_Shader_Engine_Data.result
		Global_Access.Json_Data["shaders_should_be_loaded"] = True
		if not len(self.wig_action_Get_Shader_Engine_Data.result):
			Global_Access.Json_Data["shaders_should_be_loaded"] = False
		Global_Access.save_Json_Data()
	#----------------------------------------------------------------------
	def on_remove_Non_Default_UV_Sets_CheckBox_stateChanged(self,val):
		""""""
		if val==2:
			self.action_group_optional_extraction_steps.show_Action(self.wig_action_Remove_Non_Default_UV_Sets)
		else:
			self.action_group_optional_extraction_steps.hide_Action(self.wig_action_Remove_Non_Default_UV_Sets)
	#----------------------------------------------------------------------
	def on_replace_Shaders_With_Lamberts_CheckBox_stateChanged(self,val):
		""""""
		if val==2:
			self.action_group_Pre_Scan_Actions.show_Action(self.wig_action_Replace_All_Shaders_With_Lambers)
		else:
			self.action_group_Pre_Scan_Actions.hide_Action(self.wig_action_Replace_All_Shaders_With_Lambers)
	#----------------------------------------------------------------------
	def on_remove_Other_Layers_CheckBox_stateChanged(self,val):
		""""""
		if val==2:
			self.action_group_Pre_Scan_Actions.show_Action(self.wig_action_Remove_All_Render_Layers)
		else:
			self.action_group_Pre_Scan_Actions.hide_Action(self.wig_action_Remove_All_Render_Layers)
	#----------------------------------------------------------------------
	@QT.Slot(str)
	def on_use_Render_Layer_ComboBox_currentIndexChanged(self,val):
		""""""
		if not val == 0:
			self.action_group_Pre_Scan_Actions.show_Action(self.wig_action_Replace_Master_Layer_Shader_Assignments)
		else:
			self.action_group_Pre_Scan_Actions.hide_Action(self.wig_action_Replace_Master_Layer_Shader_Assignments)
	#----------------------------------------------------------------------
	def on_Set_To_Selected_Button_Clicked(self):
		""""""
		active_selection = none_To_List(cmds.selectedNodes( dagObjects=True))
		if len(active_selection):
			self.Top_Level_Node_Input.setText(active_selection[0])
			Global_Access.set_Top_Level_Node(active_selection[0])
	#----------------------------------------------------------------------
	def on_Top_Level_Input_Changed(self):
		""""""
		text_value = self.Top_Level_Node_Input.text()
		if len(text_value) and cmds.objExists(text_value):
			Global_Access.set_Top_Level_Node(text_value)
			self.Export_Button.setEnabled(True)
		else:
			self.Export_Button.setEnabled(False)
	#----------------------------------------------------------------------
	def on_Export_Button_Clicked(self):
		""""""
		try:
			kill_hyperShadePanel()
		except:
			pass
		#self.action_group_Extraction_Fixing_And_Standedize.run_Optimize_Check()
		timer = QT.QTimer(self)
		timer.singleShot(1000, self.do_export)
	#----------------------------------------------------------------------
	def do_export(self):
		""""""
		
		if self.perform_Scene_CleanUp_CheckBox.isChecked():
			perform_CleanUp()
		
		self.action_group_Instances_Removal.run_Actions()
		self.action_group_Pre_Scan_Actions.run_Actions()
		self.action_group_Extraction_Fixing_And_Standedize.run_Actions()
		self.action_group_optional_extraction_steps.run_Actions()
		self.action_group_extraction_data.run_Actions()
		self.save_Json_Data()
		Global_Access.Export_Alembic()
		Global_Access.Export_Shaders()
		self.Export_Button.setEnabled(False)
		if self.auto_import_CheckBox.isChecked():
			self.tabWidget.setCurrentIndex(1)
			self.on_Import_Button_Clicked()
	#----------------------------------------------------------------------
	def on_Import_Button_Clicked(self):
		""""""
		try:
			kill_hyperShadePanel()
		except:
			pass
		self.action_group_rebuild_data.run_Actions()
		if len(cmds.ls("*.hondaRebuildData")):
			import Scripts.Tools.Vray_Scene_States_Manager.Honda_Data_Parser
			data = Scripts.Tools.Vray_Scene_States_Manager.Honda_Data_Parser.build_Honda_MetaData()
			data.trims.create_Display_Layers()
			import Scripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Manager
			ui = Scripts.Tools.Vray_Scene_States_Manager.Vray_Scene_States_Manager.make_ui()
			ui.Construst_Honda_Rebuild_Data()
QT.ui_Loader.registerCustomWidget(Alembic_Asset_Extraction_GUI)

#----------------------------------------------------------------------
def load_Gui():
	""""""
	gui = QT.ui_Loader.load(os.path.join( os.path.dirname(__file__), "Alembic_Asset_Extraction_V3.ui") )
	gui.show()
	gui._run_setup()
	return gui
