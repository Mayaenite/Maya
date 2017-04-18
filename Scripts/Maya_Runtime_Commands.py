import maya.cmds as cmds
import pymel.core as pm
import Scripts.OpenMaya_Util_API
import random

### HOT PIVOT ACTION ###
def HOT_PIVOT_ACTION():
	selection = pm.ls(sl = True)
	zero = [0,0,0]
	negative = [-1,-1,-1]
	
	for x in selection:
		print x
		originPivot = pm.xform(q=True, rp=True)
	
		invert = map(lambda x,y:x*y,originPivot,negative)
	
		print originPivot
		print invert
		pm.xform( t = invert)
		pm.makeIdentity(a=True, t=True)
		pm.xform( t = originPivot)

def Visibility_Connect_Maker():
	"Connect The Visibility Of The Currently Selected Nodes To The Last Node Selected"
	selection = pm.ls(selection = True)
	memberSet = selection[:-1]
	controller = selection[-1]
	
	for item in memberSet:
		print item, pm.nodeType(item)
		if pm.nodeType(item) == 'transform':
			pm.connectAttr( controller.visibility, item.visibility )

def randomize_Display_Layer_Colors():
	"""Sets The Color Of All The Display Layers Randomly"""
	colors     = [1,2,3,4,5,6,7,8,10,11,12,13,15,18,22,23,24,25,26,27,28,29,30,31]
	layers  =  [layer for layer in cmds.ls(et='displayLayer') if layer != 'defaultLayer']
	for layer in layers:
		n_colors  = len(colors)
		index     = random.randrange(0,n_colors)
		new_color = colors[index]
		colors.remove(new_color)
		if not len(colors):
			colors = [1,2,3,4,5,6,7,8,10,11,12,13,15,18,22,23,24,25,26,27,28,29,30,31]
		cmds.setAttr(layer+".color",new_color)

def Seperate_Poly_By_Shader():
	active_selection =  cmds.ls(sl=True)
	try:
		transform_meshes = cmds.listRelatives(cmds.listRelatives(cmds.ls(sl=True,type="transform"),type=["mesh"],path=True,noIntermediate=True,shapes=True),parent=True,type="transform",path=True)
		for transform_item in transform_meshes:
			cmds.select(transform_item)
			meshes = cmds.listRelatives(transform_item,type=["mesh"],path=True)
			mesh_item = meshes[0]
			#cmds.select(mesh_item)
			cmds.hyperShade(shaderNetworksSelectMaterialNodes=True)
			shaders = cmds.ls(sl=True)
			dont_skip=True
			for shader in shaders:
				cmds.hyperShade(objects=shader)
				faces = []
				for face in cmds.ls(sl=True,flatten=True,long=True):
					if "." in face:
						if face.split(".",1)[1].startswith("f") and face.split(".",1)[0].endswith(transform_item):
							faces.append(face)
				if len(faces):
					cmds.polyChipOff(faces, constructionHistory=1, duplicate=0, keepFacesTogether=1, offset=0)
				else:
					dont_skip = False
					break
			if dont_skip:
				rebuilt_seperated_Chip_Offs =  []
				cmds.select(transform_item)
				seperated_Chip_Offs = cmds.polySeparate(object=True,name="Seperated_Poly")
				for chip_off in seperated_Chip_Offs[:-1]:
					cmds.select(chip_off)
					cmds.hyperShade(shaderNetworksSelectMaterialNodes=True)
					shader            = cmds.ls(sl=True)[0]
					chip_off_name     = shader+"_Chip_Off"
					shadering_engines = cmds.listConnections(shader, destination=True, source=False, connections=False, type="shadingEngine")
					if not len(shadering_engines):
						shader_SG = cmds.sets( name=shader+"SG", renderable=True, empty=True )
						cmds.surfaceShaderList( shader, add=shader_SG)
					else:
						shader_SG = shadering_engines[0]
					# if not shader_SG == shader+"SG":
						# shader_SG = cmds.rename(shader_SG,shader+"SG")
	
					chip_off_name = cmds.rename(chip_off,chip_off_name)
					rebuilt_seperated_Chip_Offs.append(chip_off_name)
					cmds.select(chip_off_name)
					cmds.sets(edit=True,forceElement=shader_SG)
					cmds.delete(constructionHistory=True)
				for shader in shaders:
					cmds.select(clear=True)
					for chip in rebuilt_seperated_Chip_Offs:
						if cmds.objExists(chip):
							cmds.select(chip,add=True)
					chip_off_name = shader+"_Chip_Off"
					scan =  cmds.ls(chip_off_name+"*",sl=True)
					if len(scan) > 1:
						cmds.select(scan)
						Unite = cmds.polyUnite(ch=0,mergeUVSets=1,name=chip_off_name)
						cmds.parent(Unite, transform_item)
	except:
		pass
	cmds.select(active_selection)
#---------------------------------------------------------------------------
def aw_hub_check_Ctr1_Hotkey():
	""""""
	aw_hub_cmd_name = "aw_modeleditorheadsupdisplaycontrols"
	cmds.nameCommand(aw_hub_cmd_name, annotation="Armstrong White model Editor Heads Up Display Contorls", command='python("import Scripts.UIFns.AW_Master_Control_HUB\\nScripts.UIFns.AW_Master_Control_HUB.AW_HUB_Master_Control()")',)
	cmds.hotkey( altModifier=True, ctrlModifier=True, keyShortcut="A", name=aw_hub_cmd_name)
#----------------------------------------------------------------------
def aw_Box_Map_Selected():
	""""""
	_g_reselect = cmds.ls(sl=True)
	if not _g_reselect == None:
		try:
			cmds.refresh( suspend=True)
			for item in cmds.listRelatives((cmds.listRelatives(cmds.ls(long=True,sl=True),path=True,children=True,shapes=True,type="mesh")),path=True,parent=True,type="transform"):
				cmds.select(item,replace=True)
				cmds.polyAutoProjection( layoutMethod=0, projectBothDirections=0, insertBeforeDeformers=1, scale=[1,1,1], createNewMap=False,layout=0, scaleMode=0, optimize=0,planes=6,ps=0.2,worldSpace=0,constructionHistory=False)
			cmds.refresh( suspend=False)
			cmds.refresh( force=True)
			cmds.select(_g_reselect)
		except:
			cmds.refresh( suspend=False)
			cmds.refresh(  force=True)
	
	
def Planar_Proj_Unforld():
	cmds.selectMode(object=True)
	_G_current_selections = cmds.ls(long=True,sl=True,objectsOnly=True)
	_All_UVs = []
	for item in cmds.listRelatives((cmds.listRelatives(_G_current_selections,noIntermediate=True,path=True,children=True,shapes=True,type="mesh")),noIntermediate=True,path=True,parent=True,type="transform"):
		item_faces = item + ".f[*]"
		item_UVs   = item + ".map[*]"
		_All_UVs.append(item_UVs)
		cmds.select(item_faces,replace=True)
		polyPlanarProj = cmds.polyProjection(constructionHistory=True,type="Planar",insertBeforeDeformers=True,mapDirection="c")[0]
		for att in ["projectionHeight","projectionWidth"]:
			att = polyPlanarProj+"."+att
			cmds.setAttr(att,1)
		cmds.select(clear=True)
		cmds.Unfold3D(item_UVs,unfold=True,iterations=10,pack=False,borderintersection=False,triangleflip=False,mapsize=1024,roomspace=2)
	if len(_All_UVs):
		cmds.select(_All_UVs)
	else:
		cmds.select(_G_current_selections,replace=True)

def AW_PolyUnite():
	class AW_Poly_Unite_Result_Options(object):
		def __init__(self,objects,Display_Layers=[],Parents=[]):
			self.objects = objects
			self.Display_Layers = Display_Layers
			self.Parent_Objects = Parents
			self.active_layer  = Display_Layers[0]
			self.active_parent = Parents[0]
			self.create_Window()
	
	
		def create_Window(self):
			import pymel.core as pm
			#    Create a window with two option menu groups.
			#
			self.window = pm.window( title='AW Poly Unite Result')
			self.col_1 = pm.rowColumnLayout(numberOfColumns=2)
			#self.row1 = pm.rowLayout(numberOfColumns=2)
			#    Create a couple of option menu groups.
			#
			self.result_layer_grp = pm.optionMenu("AW_Layer_Unite_Group",label='Result Layer')
			for item in self.Display_Layers:
				pm.menuItem(parent=self.result_layer_grp, label=item )
			self.result_parent_grp = pm.optionMenu("AW_Parent_Unite_Group",label='Result Parent')
			for item in self.Parent_Objects:
				pm.menuItem(parent=self.result_parent_grp, label=item )
			#self.row2 = pm.rowLayout(numberOfColumns=2)
			self.OK_bnt     = pm.button(label="OK",command=self.accept)
			self.Cancel_bnt = pm.button(label="Cancel",command=self.close)
		def close(self,*args):
			pm.deleteUI(self.window,window=True)
		def accept(self,*args):
			cmds.parent(self.objects, world=True)
			united_objs = cmds.polyUnite(self.objects, ch=0,mergeUVSets=1,name="AW_United_Poly");
			cmds.parent(united_objs,self.result_parent_grp.getValue())
			dl = Scripts.OpenMaya_Util_API.DisplayLayer(self.result_layer_grp.getValue())
			dl.addMembers(united_objs)
			pm.deleteUI(self.window,window=True)
	
	display_layer_list=set()
	selected_transforms = cmds.ls( objectsOnly=True, selection=True,typ=["transform"])
	selected_meshes     = cmds.ls( objectsOnly=True, selection=True,typ=["mesh"])
	selected_meshes.extend(cmds.listRelatives(selected_transforms, shapes=True,noIntermediate=True,c=True, type="mesh",fullPath=True))
	cmds.select(cmds.listRelatives(selected_meshes,p=True,typ="transform", fullPath=True))
	selected_objects = Scripts.OpenMaya_Util_API.strings_to_Maya_Nodes(cmds.ls(sl=True))
	for obj in Scripts.OpenMaya_Util_API.strings_to_Maya_Nodes(cmds.ls(selection=True)):
		display_layer_list.add(obj.assinedDisplayLayer)
	display_layer_list=list(display_layer_list)

	selected_parents = list(set(cmds.listRelatives(p=True,typ="transform")))

	if len(display_layer_list)>1 or len(selected_parents)>1:
		win = AW_Poly_Unite_Result_Options(selected_objects,display_layer_list,selected_parents)
		pm.showWindow()
	else:
		cmds.parent( world=True)
		united_objs = cmds.polyUnite(ch=0,mergeUVSets=1,name="AW_United_Poly");
		cmds.parent(united_objs,selected_parents[0])
		dl = Scripts.OpenMaya_Util_API.DisplayLayer(display_layer_list[0])
		dl.addMembers(united_objs)
		
aw_hub_check_Ctr1_Hotkey()
cmds.runTimeCommand("Planar_Proj_Unforld_RTC", annotation="Does Some Cool Stuff Now Fuck Off", command=__name__+".Planar_Proj_Unforld()", category="User", commandLanguage="python", default=True)
cmds.runTimeCommand("randomizeDisplayLayerColors", annotation="Sets The Color Of All The Display Layers Randomly", command=__name__+".randomize_Display_Layer_Colors()", category="User", commandLanguage="python", default=True)
cmds.runTimeCommand("VisibilityConnectMaker", annotation="Connect The Visibility Of The Currently Selected Nodes To The Last Node Selected", command=__name__+".Visibility_Connect_Maker()", category="User", commandLanguage="python", default=True)
cmds.runTimeCommand("SeperatePolyByShader", annotation="Seperate Selected Polys By There Face Shading Assinments", command=__name__+".Seperate_Poly_By_Shader()", category="User", commandLanguage="python", default=True)
cmds.runTimeCommand("aw_Box_Map_Selected_RTC", annotation="Run polyAutoProjection With Box Map Settings On All Selected Items", command=__name__+".aw_Box_Map_Selected()", category="User", commandLanguage="python", default=True)
cmds.runTimeCommand("aw_Poly_Unite_RTC", annotation="Run polyUnite And Sets The Resault Back To Its Parent And Display Layer", command=__name__+".AW_PolyUnite()", category="User", commandLanguage="python", default=True)
cmds.runTimeCommand("aw_HOT_PIVOT_ACTION", annotation="Resets The Transform Matrix", command=__name__+".HOT_PIVOT_ACTION()", category="User", commandLanguage="python", default=True)
