import yaml
try:
	_maya_check = True
	import Scripts.NodeCls.M_Nodes
	Script_Node = Scripts.NodeCls.M_Nodes.Script_Node
	import maya.cmds as cmds
except:
	Script_Node =  object
	_maya_check = False
	
def find_yaml_config_scripts():
	for name in  cmds.ls(type="script"):
		if cmds.attributeQuery("Yaml_Config_Assets",node=name,exists=True):
			return YAML_Config_Script_Node(script_name=name)
	return YAML_Config_Script_Node()

def find_yaml_config_script_Refs():
	refs=cmds.ls(type="reference")
	res   = []
	if isinstance(refs,list):
		for r in refs:
			try:
				cmds.select(cmds.referenceQuery( r,dagPath=True, nodes=True ))
				for ref_script in cmds.ls(sl=True,type="script"):
					if cmds.attributeQuery("Yaml_Config_Assets",node=ref_script,exists=True):
						ref_script = YAML_Config_Script_Node(ref_script)
						data = ref_script.load_Config_Data()
						data.name_space = cmds.referenceQuery( r,namespace=True )[1:]
						data.assine_Maya_nodes()
						res.append(data)
			except:
				pass
	cmds.select(clear=True)
	return res

class YAML_Config_Script_Node(Script_Node):
	def __init__(self, script_name="AW_YAML_CONFIG_SCRIPT_DATA", namespace=None):
		if namespace != None:
			script_name = namespace + ":" + script_name
		super(YAML_Config_Script_Node, self).__init__(script_name, afterScript="",beforeScript="",executeAfter=False, executeBefore=False, scriptType=0, sourceType="python")
		self.yaml_plug = self.create_Message_M("Yaml_Config_Assets")
	#----------------------------------------------------------------------
	def save_Config_Data(self, data):
		""""""
		if not isinstance(data, Config_Data):
			raise TypeError("Input data must be an instance of Config_Data")
		else:
			value = yaml.dump(data)
			if self.before.value != value:
				self.before.setValue(value)
				cmds.file( save=True)
	#----------------------------------------------------------------------
	def load_Config_Data(self):
		""""""
		data = yaml.load(self.before.getValue())
		isinstance(data, Config_Data)
		if not data is None:
			data = data_cleaner(data)
		return data
#---------------------------------------------------------------------------------------------------
#_______________________________________________________________________ Taged Yaml Data Type
########################################################################
class Assets(yaml.YAMLObject):
	yaml_tag = u'!Assets'
	#----------------------------------------------------------------------
	def __init__(self, items=None, parent=None):
		self.parent = parent
		isinstance(self.parent, Config_Data)
		if not isinstance(items, list):
			items =  []
		self.items =  items
		for item in self.items:
			item.parent = self
			
	def assine_Maya_nodes(self):
		if _maya_check:
			for item in self.items:
				isinstance(item, Asset)
				item.assine_maya_node()
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(items=%r)" % (self.__class__.__name__, self.items)

########################################################################
class Asset(yaml.YAMLObject):
	yaml_tag = u'!Asset'
	#----------------------------------------------------------------------
	def __init__(self, name=None, render_states=None, part_sets=None, child_assets=None, parent=None):
		self.name          = name
		self.Render_States = render_states
		self.Part_Sets     = part_sets
		self.Child_Assets  = child_assets
		self.parent        = parent
		isinstance(self.parent, Assets)
		if not isinstance(self.Render_States, Render_States):
			self.Render_States = Render_States(parent=self)
			
		if not isinstance(self.Part_Sets, Part_Sets):
			self.Part_Sets = Part_Sets(parent=self)
			
		if not isinstance(self.Child_Assets, list):
			self.Child_Assets = []
			
	def assine_maya_node(self):
		self.Part_Sets.parent = self
		self.Part_Sets.assine_Maya_nodes()
		for item in  self.Child_Assets:
			item.parent = self
			item.assine_maya_node()
		if _maya_check:
			name = self.name
			p = self.parent
			while not hasattr(p, "name_space"):
				p = p.parent
				if p == None:
					break
			if p.name_space:
				name = p.name_space + ":" + name
			if cmds.objExists(name):
				self.maya_node = Scripts.NodeCls.M_Nodes.Container(name)
				
	def set_render_state_overides(self, render_state):
		isinstance(render_state, Render_State)
		for link in render_state.Beauty.links:
			isinstance(link, Part_Set)
			link.maya_node.apply_Beauty_Layer_Override()
		for link in render_state.Invisible.links:
			isinstance(link, Part_Set)
			link.maya_node.apply_Invisible_Layer_Override()
		for link in render_state.Matte.links:
			isinstance(link, Part_Set)
			link.maya_node.apply_Matte_Layer_Override()
		for link in render_state.Unassined.links:
			isinstance(link, Part_Set)
			link.maya_node.Remove_Members_From_Render_Layer()
			
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(%r)" % (self.__class__.__name__, self.name)
########################################################################
class Part_Sets(yaml.YAMLObject):
	yaml_tag = u'!Part_Sets'
	#----------------------------------------------------------------------
	def __init__(self, parts=None, parent=None):
		self.parent = parent
		isinstance(self.parent, Asset)
		if not isinstance(parts, list):
			parts =  []
		self.parts =  parts
	def assine_Maya_nodes(self):
		for part in self.parts:
			part.parent = self
		if _maya_check:
			for item in self.parts:
				item.parent = self
				isinstance(item, Part_Set)
				item.assine_maya_node()
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(parts=%r)" % (self.__class__.__name__, self.parts)
########################################################################
class Render_States(yaml.YAMLObject):
	yaml_tag = u'!Render_States'
	#----------------------------------------------------------------------
	def __init__(self, states=None, parent=None):
		self.parent = parent
		isinstance(self.parent, Asset)
		if not isinstance(states, list):
			states =  []
		self.states =  states
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(states=%r,parent=%r)" % (self.__class__.__name__, self.states, self.parent)
########################################################################
class Overides_Container(yaml.YAMLObject):
	yaml_tag = u'!Overides_Container'
	#----------------------------------------------------------------------
	def __init__(self, links=None, parent=None):
		self.parent = parent
		if not isinstance(links, list):
			links =  []
		self.links =  links
		isinstance(self.parent, Render_State)
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(links=%r,parent=%r))" % (self.__class__.__name__, self.links, self.parent.name)

########################################################################
class Beauty_Overides(Overides_Container):
	yaml_tag = u'!Beauty_Overides'
########################################################################
class Matte_Overides(Overides_Container):
	yaml_tag = u'!Matte_Overides'
########################################################################
class Invisible_Overides(Overides_Container):
	yaml_tag = u'!Invisible_Overides'
########################################################################
class Unassined_Overides(Overides_Container):
	yaml_tag = u'!Unassined_Overides'

########################################################################
class Render_State(yaml.YAMLObject):
	yaml_tag = u'!Render_State'
	#----------------------------------------------------------------------
	def __init__(self, name=None, Unassined=None, Matte=None, Invisible=None, Beauty=None, parent=None, favorit=0, uid=None, asset_assembly_ref_id=None, asset_assembly_ref_type=None):
		self.name      = name
		self.parent    = parent
		self.Unassined = Unassined
		self.Matte     = Matte
		self.Invisible = Invisible
		self.Beauty    = Beauty
		self.favorit   = favorit
		self.uid       = uid
		self.asset_assembly_ref_id   = asset_assembly_ref_id
		self.asset_assembly_ref_type = asset_assembly_ref_type
		isinstance(self.parent, Render_States)
		
		if not isinstance(self.Unassined, Unassined_Overides):
			self.Unassined = Unassined_Overides(parent=self)
			
		if not isinstance(self.Matte, Matte_Overides):
			self.Matte = Matte_Overides(parent=self)
			
		if not isinstance(self.Invisible, Invisible_Overides):
			self.Invisible = Invisible_Overides(parent=self)
		
		if not isinstance(self.Beauty, Beauty_Overides):
			self.Beauty = Beauty_Overides(parent=self)
		
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(name=%r, Unassined=%r, Matte=%r, Invisible=%r, Beauty=%r, parent=%r)" % (self.__class__.__name__, self.name, self.Unassined, self.Matte, self.Invisible, self.Beauty, self.parent)
	
########################################################################
class Part_Set(yaml.YAMLObject):
	yaml_tag = u'!Part_Set'
	#----------------------------------------------------------------------
	def __init__(self, name=None, parent=None, uid=None,asset_assembly_ref_id=None, asset_assembly_ref_type=None):
		self.name                    = name
		self.parent                  = parent
		self.uid                     = uid
		self.asset_assembly_ref_id   = asset_assembly_ref_id
		self.asset_assembly_ref_type = asset_assembly_ref_type
		isinstance(self.parent, Part_Sets)
		#self.maya_node = None
	def assine_maya_node(self):
		if _maya_check:
			name = self.name
			scan = self.parent
			while not isinstance(scan, Config_Data):
				scan = scan.parent
				if scan == None:
					break
			if not scan == None:
				if scan.name_space:
					name =  scan.name_space + ":" + name
				if cmds.objExists(name):
					self.maya_node = Scripts.NodeCls.M_Nodes.VRayRenderState(name)
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(name=%r,parent=%r)" % (self.__class__.__name__, self.name, self.parent.parent.name)
	
########################################################################
class Part_Set_Refence(yaml.YAMLObject):
	yaml_tag = u'!Part_Set_Refence'
	#----------------------------------------------------------------------
	def __init__(self, link, parent):
		self.link   = link
		self.parent = parent
		isinstance	(self.link, Part_Set)
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(%r,%r)" % (self.__class__.__name__, self.link, self.parent)
########################################################################
class Config_Data(yaml.YAMLObject):
	yaml_tag = u'!Config_Data'
	#----------------------------------------------------------------------
	def __init__(self, assets=None):
		self.Assets = assets
		self.name_space = ""
		if not isinstance(self.Assets, Assets):
			self.Assets = Assets(parent=self)
	def assine_Maya_nodes(self):
		self.Assets.assine_Maya_nodes()
		
	#----------------------------------------------------------------------
	def __repr__(self):
		return "%s(assets=%r)" % (self.__class__.__name__, self.Assets)
	#----------------------------------------------------------------------
	def apply_States_To_Diaplay_Layers(self, state_name):
		""""""
		self.assine_Maya_nodes()
		for asset_item in self.Assets.items:
			for render_state_item in asset_item.Render_States.states[1:]:
				if render_state_item.name == state_name:
					for link in render_state_item.Beauty.links:
						cmds.setAttr(link.maya_node.assinedDisplayLayer+".visibility",1)
			
					for link in render_state_item.Matte.links:
						cmds.setAttr(link.maya_node.assinedDisplayLayer+".visibility",1)
			
					for link in render_state_item.Invisible.links:
						cmds.setAttr(link.maya_node.assinedDisplayLayer+".visibility",1)
			
					for link in render_state_item.Unassined.links:
						cmds.setAttr(link.maya_node.assinedDisplayLayer+".visibility",0)

########################################################################
class Yaml_Differences_Data(object):
	"""Used To Compare And Store Data From 2 Different State Manager Yaml Data Files"""

	def __init__(self,old_yaml,new_yaml):
		"""Constructor"""
		self.old_yaml         = old_yaml
		self.new_yaml         = new_yaml
		self.added_render_states   = []
		self.added_part_sets       = []
		self.changed_render_states = []

		self.old_render_states     = dict()
		self.old_part_sets         = dict()
		self.new_render_states     = dict()
		self.new_part_sets         = dict()
		self.render_state_Changes  = dict()

		self._Run_Data_Collection()

		for changed_state in self.changed_render_states:
			self.render_state_Changes[changed_state[0].name] = self.get_Render_State_Changes(changed_state[0], changed_state[1])

	#----------------------------------------------------------------------
	def _Run_Data_Collection(self):
		""""""

		# The Fallowing Code Is For Collection Of Data

		# Scan Over The Assets Of The Old Yaml Data
		for old_asset in self.old_yaml.Assets.items:

			# Scan Over The Render States Of The Old Yaml Data
			for old_render_state in old_asset.Render_States.states:
				# Collect The Render State as its name
				self.old_render_states[old_render_state.name] = old_render_state

			# Scan Over The Part Sets Of The Old Yaml Data
			for old_part_set in old_asset.Part_Sets.parts:
				# Collect The Part Set as its name
				self.old_part_sets[old_part_set.name] = old_part_set

		# Scan Over The Assets Of The New Yaml Data
		for new_asset in self.new_yaml.Assets.items:

			# Scan Over The Render States Of The New Yaml Data
			for new_render_state in new_asset.Render_States.states:
				# Collect The Render State as its name
				self.new_render_states[new_render_state.name] = new_render_state

			# Scan Over The Part Sets Of The Old Yaml Data
			for new_part_set in new_asset.Part_Sets.parts:
				# Collect The Part Set as its name
				self.new_part_sets[new_part_set.name] = new_part_set


		# The Fallowing Code Is For Collection Of Added Data

		# Scan Over The New Yaml Render State And Check If
		# It Does Not Exist in the old Yaml Render States
		for new_render_state in self.new_render_states:
			# Get The Data For The interation key
			new_render_state = self.new_render_states[new_render_state]
			# Check If The Old Render States Contains A Item 
			# With The Same Name As This New Render State 
			if not new_render_state.name in self.old_render_states:
				# If It Does Not Then A New State Was Found
				self.added_render_states.append(new_render_state)

		# Scan Over The New Yaml Part Sets And Check If
		# It Does Not Exist in the old Yaml Part Sets
		for new_part_set in self.new_part_sets:
			# Get The Data For The interation key
			new_part_set = self.new_part_sets[new_part_set]
			# Check If The Old Part Sets Contains A Item 
			# With The Same Name As This New Part Set 
			if not new_part_set.name in self.old_part_sets:
				# If It Does Not Then A Part Set Was Found
				self.added_part_sets.append(new_part_set)


		# The Fallowing Code Is For Collection Of Changed Data

		# Scan Over The Old Render States
		for old_render_state in self.old_render_states:
			# Get The Data For The interation key
			old_render_state = self.old_render_states[old_render_state]
			# Check new render state with the same name as the old render state
			if old_render_state.name in self.new_render_states:
				# Get The Data For The interation key
				new_render_state = self.new_render_states[old_render_state.name]

				# This Will Store The Names Of All The Parts Sets That Have Been Linked To Old Render State
				old_render_state_assignments = []
				new_render_state_assignments = []

				# Iterate Over Off The Different Assinment Containes Of The Old Render State
				for container in [old_render_state.Beauty,old_render_state.Invisible,old_render_state.Matte]:
					# Iterate Over The Part Sets Linked To The Container
					for link in container.links:
						# Collect Its Name For Layer use
						old_render_state_assignments.append(link.name)

				# Iterate Over Off The Different Assinment Containes Of The Old Render State
				for container in [new_render_state.Beauty,new_render_state.Invisible,new_render_state.Matte]:
					# Iterate Over The Part Sets Linked To The Container
					for link in container.links:
						# Collect Its Name For Layer use
						new_render_state_assignments.append(link.name)

				# The Scan To Deeper Then 1 A Single Break will not work so this will be used to break for full loop
				do_brake = False
				# Iterate Over Off The Different Assinment Containes Of The New Render State
				for container in [new_render_state.Beauty,new_render_state.Invisible,new_render_state.Matte]:
					# Iterate Over The Part Sets Linked To The Container
					for link in container.links:
						# Check If This Part Set Name Is In The list Collected From The Old Render State
						if not link.name in old_render_state_assignments:
							# If Not Then There Is Some Kind Of Differencs BeTween The 2 
							self.changed_render_states.append([old_render_state,new_render_state])
							# Set This So loop before this also knows To Stop
							do_brake = True
							break
					if do_brake:
						break

				# The Scan To Deeper Then 1 A Single Break will not work so this will be used to break for full loop
				do_brake = False
				# Iterate Over Off The Different Assinment Containes Of The New Render State
				for container in [old_render_state.Beauty,old_render_state.Invisible,old_render_state.Matte]:
					# Iterate Over The Part Sets Linked To The Container
					for link in container.links:
						# Check If This Part Set Name Is In The list Collected From The Old Render State
						if not link.name in new_render_state_assignments:
							# If Not Then There Is Some Kind Of Differencs BeTween The 2
							if not link.name in [old_render_state,new_render_state]  in self.changed_render_states:
								self.changed_render_states.append([old_render_state,new_render_state])
							# Set This So loop before this also knows To Stop
							do_brake = True
							break
					if do_brake:
						break

	#----------------------------------------------------------------------
	def get_Render_State_Changes(self,old,new):
		isinstance(old,Scripts.Tools.Vray_Scene_States_Manager.Yaml_Config_Data.Render_State)
		isinstance(new,Scripts.Tools.Vray_Scene_States_Manager.Yaml_Config_Data.Render_State)

		Beauty_Res    = dict(Added=[],Removed=[])
		Invisible_Res = dict(Added=[],Removed=[])
		Matte_Res     = dict(Added=[],Removed=[])
		data_keys     = ["Beauty","Invisible","Matte"]
		res           = dict(Beauty=Beauty_Res,Invisible=Invisible_Res,Matte=Matte_Res)

		# Make A list of containes for each of the states
		old_containers = [old.Beauty,old.Invisible,old.Matte]
		new_containers = [new.Beauty,new.Invisible,new.Matte]
		# scan over a new and the equal old container
		for old_container,new_container,data_key in zip(old_containers, new_containers, data_keys):

			# This Will Store The Names Of All The Parts Sets That Have Been Linked To Old Render State
			old_container_assignments = [link.name for link in old_container.links]
			new_container_assignments = [link.name for link in new_container.links]

			# Get The dict that we will be adding the changes to 
			key_data = res[data_key]
			# Iterate Over The Part Sets Linked To The New Container
			for link in new_container.links:
				if not link.name in old_container_assignments:
					key_data["Added"].append(link)

			# Iterate Over The Part Sets Linked To The New Container
			for link in old_container.links:
				if not link.name in new_container_assignments:
					key_data["Removed"].append(link)
		return res

#----------------------------------------------------------------------
def save_config_data_to_file(data, file_path):
	""""""
	data = data_cleaner(data)
	with file(file_path, mode="w") as f:
		yaml.dump(data, stream=f)
	return yaml.dump(data)

#----------------------------------------------------------------------
def load_config_data_from_file(file_path):
	""""""
	with file(file_path, mode="r") as f:
		data = yaml.load(f)
		data = data_cleaner(data)
	isinstance(data, Config_Data)
	return data

#----------------------------------------------------------------------
def save_config_data_to_script_node(data, script_node):
	""""""
	if not isinstance(data, Config_Data):
		raise TypeError("Input data must be an instance of Config_Data")
	if not isinstance(script_node, (str, Scripts.NodeCls.M_Nodes.Script_Node)):
		raise TypeError("Input script_node must be an instance of Scripts.NodeCls.M_Nodes.Script_Node or str")
	Scripts.NodeCls.M_Nodes.Script_Node.GUI_OpenClose
	if isinstance(script_node, str):
		script_node = Scripts.NodeCls.M_Nodes.Script_Node(script_node, afterScript="", beforeScript="", executeAfter=False, executeBefore=False, scriptType=0, sourceType="python")
		
	if script.after.value != value:
		script.after.setValue(value)
		cmds.file( save=True)
		
	return value
def data_cleaner(data):
	if not isinstance(data, Config_Data):
		raise TypeError("Input data must be an instance of Config_Data")
	found_check = True
	stop = 10
	while found_check and stop:
		found_check = False
		for item in data.Assets.items:
			for part in item.Part_Sets.parts:
				if not len(part.name):
					found_check = True
					for state in item.Render_States.states:
						if part in state.Beauty.links:
							del state.Beauty.links[state.Beauty.links.index(part)]
						elif part in state.Invisible.links:
							del state.Invisible.links[state.Invisible.links.index(part)]
						elif part in state.Matte.links:
							del state.Matte.links[state.Matte.links.index(part)]
						elif part in state.Unassined.links:
							del state.Unassined.links[state.Unassined.links.index(part)]
					print "remove Part At Index %i for asset %r because it has no valid name" % (item.Part_Sets.parts.index(part), item.name)
					del item.Part_Sets.parts[item.Part_Sets.parts.index(part)]
		stop -= 1
	return data
#----------------------------------------------------------------------
def load_config_Script(namespace="AW_Yaml_Config_Data"):
	""""""
	if not cmds.objExists(script_name):
		data = get_default_Yaml_Data()
	else:
		script = Scripts.NodeCls.M_Nodes.Script_Node(script_name, afterScript="", beforeScript="", executeAfter=False,executeBefore=False,scriptType=0, sourceType="python")
		data = yaml.load(script.after.getValue())
		data = data_cleaner(data)
		ns = ":".join(script.name.split(":")[:-1])
		data.active_namespace = ns
		data.assine_Maya_nodes()
	isinstance(data, Config_Data)
	return data

#----------------------------------------------------------------------
def get_default_Yaml_Data():
	value = """&id005 !Config_Data
Assets: &id004 !Assets
  items:
  - &id001 !Asset
    Part_Sets: !Part_Sets
      parent: *id001
      parts: []
    Render_States: &id003 !Render_States
      parent: *id001
      states:
      - &id002 !Render_State
        Beauty: !Beauty_Overides
          links: []
          parent: *id002
        Invisible: !Invisible_Overides
          links: []
          parent: *id002
        Matte: !Matte_Overides
          links: []
          parent: *id002
        Unassined: !Unassined_Overides
          links: []
          parent: *id002
        name: Default
        parent: *id003
    name: Config_Asset
    parent: *id004
  parent: *id005"""
	return yaml.load(value)

if __name__ == "__main__":
	print yaml.dump(Config_Data())
