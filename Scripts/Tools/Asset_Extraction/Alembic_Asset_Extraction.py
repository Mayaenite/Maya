import Scripts.NodeCls.M_Nodes
import Scripts.Global_Constants
import Scripts.General_Maya_Util
DisplayLayer   = Scripts.NodeCls.M_Nodes.DisplayLayer
SelectionSet   = Scripts.NodeCls.M_Nodes.SelectionSet
MNODE          = Scripts.NodeCls.M_Nodes.MNODE
Nodes          = Scripts.Global_Constants.Nodes
Shading_Engine = Scripts.NodeCls.M_Nodes.Shading_Engine
from maya import cmds

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

class Asset_Extractor(object):
	def __init__(self, autofind=False):
		self.rename_polySurface_Shapes()
		if not len(cmds.ls(sl=True)):
			if autofind:
				get_Master_Item()
		if cmds.ls(sl=True)[0].startswith("|"):
			cmds.inViewMessage( amg='The Root Item Selected\n<hl>%s</hl>\nIs Not Unique.' % cmds.ls(sl=True)[0], fontSize=50, pos='midCenter', fadeInTime=700,fadeStayTime=700,fadeOutTime=700, fade=True )
		else:
			self.top_level_node      = MNODE()
			self.top_level_node_name = self.top_level_node.nice_name
			self.dl_dict     = {}
			self.shader_dict = {}
			self.shading_engines = Nodes.Shading_Engines()
			self.display_layers  = Nodes.Display_Layers()
			self.dlnames = [layer.name for layer in self.display_layers]
			self.dlcolors= [layer.color.value for layer in Nodes.Display_Layers()]
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
			self.add_assined_display_layers()
			self.add_assined_materials()
			self.unlock_and_break_Attr_connections()

		self.export_AbcExport()
		self.export_Shaders()
		self.force_new_scene()
		self.import_AbcExport()
		self.import_Shaders()

		count  = len(self.dlnames)
		count += len(self.shader_dict.keys())
		self.ProgressBar = Scripts.General_Maya_Util.ProgressBarContext(count, 1 , False)
		with self.ProgressBar:
			self.remake_display_layers()
			self.reasine_shaders()
		#self.reassine_Custom_Attr_Values()

	def add_assined_display_layers(self):
		for dl in self.display_layers:
			isinstance(dl, DisplayLayer)
			self.ProgressBar.increment()
			self.dl_dict[dl.name]=dl.member_names

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
			if not shader.assined_material == None:
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

	def import_Shaders(self):
		cmds.file("C:/temp/shaders.mb",i=True,type="mayaBinary",ra=1,mergeNamespacesOnClash=0,namespace="extracted_shaders",options="v=0;",pr=True,loadReferenceDepth="all")

	def force_new_scene(self):
		cmds.file(force=True,new=True)

	def export_AbcExport(self):
		cmds.select(self.top_level_node)
		cmds.AbcExport(jobArg='-frameRange 1 1 -attr AW_Extractor_ID -attr assined_display_layer -uvWrite -worldSpace -dataFormat HDF -eulerFilter -stripNamespaces -root %s -file C:/temp/Extracted.abc' % self.top_level_node.name)

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
		for node in nodes:
			self.ProgressBar.increment()
			if not node.attributeExists("AW_Extractor_ID"):
				cmds.addAttr(node,longName="AW_Extractor_ID",attributeType="long")
			cmds.setAttr(node.name+".AW_Extractor_ID", counter)
			counter += 1
