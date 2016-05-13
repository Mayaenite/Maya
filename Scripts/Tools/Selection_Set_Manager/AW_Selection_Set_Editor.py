import os
import logging
import logging.handlers
import QT
import Scripts.UICls.mayaMixin
import Scripts.General_Maya_Util
import Scripts.OpenMaya_Util_API
import Scripts.Maya_Callback_Builders
import pymel.core
import itertools
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import shiboken
import Master_Icon_Resource_File_rc
from functools import wraps

QtGui                    = QT.QtGui
QtCore                   = QT.QtCore
QtSignal                 = QT.QtSignal
QtSlot                   = QT.QtSlot
Qt                       = QT.Qt
ui_Loader                = QT.ui_Loader
count                    = itertools.count
wrapInstance             = shiboken.wrapInstance
General_Util             = Scripts.General_Maya_Util
Util_API                 = Scripts.OpenMaya_Util_API
MayaQWidgetBaseMixin     = Scripts.UICls.mayaMixin.MayaQWidgetBaseMixin
MayaQWidgetDockableMixin = Scripts.UICls.mayaMixin.MayaQWidgetDockableMixin
CB_Builders              = Scripts.Maya_Callback_Builders
S_Msg_A_Flags            = CB_Builders.Scene_Message_After_Flags
S_Msg_B_Flags            = CB_Builders.Scene_Message_Before_Flags
S_Msg_Flags              = CB_Builders.Scene_Message_Flags
Node_Msg_Flags           = CB_Builders.Node_Message_Flages

#----------------------------------------------------------------------
def make_ui_code(path=None):
	if path == None:
		path = r"n:\User\dloveridge\Maya_App_Prefs\2015-x64\scripts\Selection_Set_Manager\AW_Selection_Set_Editor.ui"
	from lxml import etree
	tree = etree.parse(path)
	print "\t\t\t# Widgets"
	print_Widget(tree)
	print "\t\t\t# Actions"
	print_actions(tree)
#----------------------------------------------------------------------
def print_actions(tree):
	for action in sorted([elem.get("name") for elem in tree.findall(".//action")]):
		print "\t\t\tself.%s = QtGui.QAction()" % action
#----------------------------------------------------------------------
def print_Widget(tree):
	for elem in tree.findall(".//widget"):
		print "\t\t\tself.%s = QtGui.%s()" % (elem.get("name"), elem.get("class"))
#----------------------------------------------------------------------
def _Make_Maya_Node_Type_Icons():
	Icons = dict(
	    VRayObjectProperties           = QtGui.QPixmap(":/O/out_vrayobjectproperties"),
	    addDoubleLinear                = QtGui.QPixmap(":/O/out_adddoublelinear"),
	    addMatrix                      = QtGui.QPixmap(":/O/out_addmatrix"),
	    aimConstraint                  = QtGui.QPixmap(":/O/out_aimconstraint"),
	    airField                       = QtGui.QPixmap(":/O/out_airfield"),
	    alignCurve                     = QtGui.QPixmap(":/O/out_aligncurve"),
	    alignSurface                   = QtGui.QPixmap(":/O/out_alignsurface"),
	    ambientLight                   = QtGui.QPixmap(":/O/out_ambientlight"),
	    angleBetween                   = QtGui.QPixmap(":/O/out_anglebetween"),
	    angleDimension                 = QtGui.QPixmap(":/O/out_angledimension"),
	    animCurveTA                    = QtGui.QPixmap(":/O/out_animcurveta"),
	    animCurveTL                    = QtGui.QPixmap(":/O/out_animcurvetl"),
	    animCurveTT                    = QtGui.QPixmap(":/O/out_animcurvett"),
	    animCurveTU                    = QtGui.QPixmap(":/O/out_animcurvetu"),
	    animCurveUA                    = QtGui.QPixmap(":/O/out_animcurveua"),
	    animCurveUL                    = QtGui.QPixmap(":/O/out_animcurveul"),
	    animCurveUT                    = QtGui.QPixmap(":/O/out_animcurveut"),
	    animCurveUU                    = QtGui.QPixmap(":/O/out_animcurveuu"),
	    anisotropic                    = QtGui.QPixmap(":/O/out_anisotropic"),
	    annotationShape                = QtGui.QPixmap(":/O/out_annotationshape"),
	    arcLengthDimension             = QtGui.QPixmap(":/O/out_arclengthdimension"),
	    areaLight                      = QtGui.QPixmap(":/O/out_arealight"),
	    arrayMapper                    = QtGui.QPixmap(":/O/out_arraymapper"),
	    assemblyDefinition             = QtGui.QPixmap(":/O/out_assemblydefinition"),
	    assemblyReference              = QtGui.QPixmap(":/O/out_assemblyreference"),
	    attachCurve                    = QtGui.QPixmap(":/O/out_attachcurve"),
	    attachSurface                  = QtGui.QPixmap(":/O/out_attachsurface"),
	    audio                          = QtGui.QPixmap(":/O/out_audio"),
	    baseLattice                    = QtGui.QPixmap(":/O/out_baselattice"),
	    bezierCurve                    = QtGui.QPixmap(":/O/out_beziercurve"),
	    blendColors                    = QtGui.QPixmap(":/O/out_blendcolors"),
	    blendTwoAttr                   = QtGui.QPixmap(":/O/out_blendtwoattr"),
	    blinn                          = QtGui.QPixmap(":/O/out_blinn"),
	    brownian                       = QtGui.QPixmap(":/O/out_brownian"),
	    brush                          = QtGui.QPixmap(":/O/out_brush"),
	    bulge                          = QtGui.QPixmap(":/O/out_bulge"),
	    bulletInitialState             = QtGui.QPixmap(":/O/out_bulletinitialstate"),
	    bulletRigidBodyConstraintShape = QtGui.QPixmap(":/O/out_bulletrigidbodyconstraintshape"),
	    bulletRigidBodyShape           = QtGui.QPixmap(":/O/out_bulletrigidbodyshape"),
	    bulletRigidCollection          = QtGui.QPixmap(":/O/out_bulletrigidcollection"),
	    bulletRigidSet                 = QtGui.QPixmap(":/O/out_bulletrigidset"),
	    bulletSoftBodyShape            = QtGui.QPixmap(":/O/out_bulletsoftbodyshape"),
	    bulletSoftConstraintShape      = QtGui.QPixmap(":/O/out_bulletsoftconstraintshape"),
	    bulletSolverShape              = QtGui.QPixmap(":/O/out_bulletsolvershape"),
	    bump2d                         = QtGui.QPixmap(":/O/out_bump2d"),
	    bump3d                         = QtGui.QPixmap(":/O/out_bump3d"),
	    buttonManip                    = QtGui.QPixmap(":/O/out_buttonmanip"),
	    camera                         = QtGui.QPixmap(":/O/out_camera"),
	    character                      = QtGui.QPixmap(":/O/out_character"),
	    checker                        = QtGui.QPixmap(":/O/out_checker"),
	    choice                         = QtGui.QPixmap(":/O/out_choice"),
	    chooser                        = QtGui.QPixmap(":/O/out_chooser"),
	    clamp                          = QtGui.QPixmap(":/O/out_clamp"),
	    clampColors                    = QtGui.QPixmap(":/O/out_clampcolors"),
	    cloth                          = QtGui.QPixmap(":/O/out_cloth"),
	    cloud                          = QtGui.QPixmap(":/O/out_cloud"),
	    clusterHandle                  = QtGui.QPixmap(":/O/out_clusterhandle"),
	    collisionModel                 = QtGui.QPixmap(":/O/out_collisionmodel"),
	    colorProfile                   = QtGui.QPixmap(":/O/out_colorprofile"),
	    condition                      = QtGui.QPixmap(":/O/out_condition"),
	    container                      = QtGui.QPixmap(":/O/out_container"),
	    contrast                       = QtGui.QPixmap(":/O/out_contrast"),
	    cpClothProperty                = QtGui.QPixmap(":/O/out_cpclothproperty"),
	    cpClothSolver                  = QtGui.QPixmap(":/O/out_cpclothsolver"),
	    cpStitcher                     = QtGui.QPixmap(":/O/out_cpstitcher"),
	    crater                         = QtGui.QPixmap(":/O/out_crater"),
	    creaseSet                      = QtGui.QPixmap(":/O/out_creaseset"),
	    curveInfo                      = QtGui.QPixmap(":/O/out_curveinfo"),
	    curveVarGroup                  = QtGui.QPixmap(":/O/out_curvevargroup"),
	    dagContainer                   = QtGui.QPixmap(":/O/out_dagcontainer"),
	    dagNode                        = QtGui.QPixmap(":/O/out_dagnode"),
	    decomposeMatrix                = QtGui.QPixmap(":/O/out_decomposematrix"),
	    default                        = QtGui.QPixmap(":/O/out_default"),
	    defaultLightList               = QtGui.QPixmap(":/O/out_defaultlightlist"),
	    defaultOutliner                = QtGui.QPixmap(":/O/out_defaultoutliner"),
	    defaultShaderList              = QtGui.QPixmap(":/O/out_defaultshaderlist"),
	    defaultTextureList             = QtGui.QPixmap(":/O/out_defaulttexturelist"),
	    directionalLight               = QtGui.QPixmap(":/O/out_directionallight"),
	    displacementShader             = QtGui.QPixmap(":/O/out_displacementshader"),
	    displayLayer                   = QtGui.QPixmap(":/O/out_displaylayer"),
	    distanceDimShape               = QtGui.QPixmap(":/O/out_distancedimshape"),
	    doubleShadingSwitch            = QtGui.QPixmap(":/O/out_doubleshadingswitch"),
	    dragField                      = QtGui.QPixmap(":/O/out_dragfield"),
	    dynamicConstraint              = QtGui.QPixmap(":/O/out_dynamicconstraint"),
	    envBall                        = QtGui.QPixmap(":/O/out_envball"),
	    envChrome                      = QtGui.QPixmap(":/O/out_envchrome"),
	    envCube                        = QtGui.QPixmap(":/O/out_envcube"),
	    envFog                         = QtGui.QPixmap(":/O/out_envfog"),
	    envSky                         = QtGui.QPixmap(":/O/out_envsky"),
	    envSphere                      = QtGui.QPixmap(":/O/out_envsphere"),
	    expression                     = QtGui.QPixmap(":/O/out_expression"),
	    file                           = QtGui.QPixmap(":/O/out_file"),
	    fluidEmitter                   = QtGui.QPixmap(":/O/out_fluidemitter"),
	    fluidShape                     = QtGui.QPixmap(":/O/out_fluidshape"),
	    fluidTexture2D                 = QtGui.QPixmap(":/O/out_fluidtexture2d"),
	    fluidTexture3D                 = QtGui.QPixmap(":/O/out_fluidtexture3d"),
	    follicle                       = QtGui.QPixmap(":/O/out_follicle"),
	    fractal                        = QtGui.QPixmap(":/O/out_fractal"),
	    frameCache                     = QtGui.QPixmap(":/O/out_framecache"),
	    gammaCorrect                   = QtGui.QPixmap(":/O/out_gammacorrect"),
	    geoConnectable                 = QtGui.QPixmap(":/O/out_geoconnectable"),
	    geometryConstraint             = QtGui.QPixmap(":/O/out_geometryconstraint"),
	    gpuCache                       = QtGui.QPixmap(":/O/out_gpucache"),
	    granite                        = QtGui.QPixmap(":/O/out_granite"),
	    gravityField                   = QtGui.QPixmap(":/O/out_gravityfield"),
	    grid                           = QtGui.QPixmap(":/O/out_grid"),
	    hairSystem                     = QtGui.QPixmap(":/O/out_hairsystem"),
	    heightField                    = QtGui.QPixmap(":/O/out_heightfield"),
	    holder                         = QtGui.QPixmap(":/O/out_holder"),
	    hsvToRgb                       = QtGui.QPixmap(":/O/out_hsvtorgb"),
	    igmDescription                 = QtGui.QPixmap(":/O/out_igmdescription"),
	    ikEffector                     = QtGui.QPixmap(":/O/out_ikeffector"),
	    ikHandle                       = QtGui.QPixmap(":/O/out_ikhandle"),
	    ikHandleGadget                 = QtGui.QPixmap(":/O/out_ikhandlegadget"),
	    ikRPsolver                     = QtGui.QPixmap(":/O/out_ikrpsolver"),
	    ikSCsolver                     = QtGui.QPixmap(":/O/out_ikscsolver"),
	    ikSplineSolver                 = QtGui.QPixmap(":/O/out_iksplinesolver"),
	    imagePlane                     = QtGui.QPixmap(":/O/out_imageplane"),
	    implicitSphere                 = QtGui.QPixmap(":/O/out_implicitsphere"),
	    instancer                      = QtGui.QPixmap(":/O/out_instancer"),
	    joint                          = QtGui.QPixmap(":/O/out_joint"),
	    lambert                        = QtGui.QPixmap(":/O/out_lambert"),
	    lattice                        = QtGui.QPixmap(":/O/out_lattice"),
	    layeredShader                  = QtGui.QPixmap(":/O/out_layeredshader"),
	    leather                        = QtGui.QPixmap(":/O/out_leather"),
	    lightFog                       = QtGui.QPixmap(":/O/out_lightfog"),
	    lightInfo                      = QtGui.QPixmap(":/O/out_lightinfo"),
	    lightLinker                    = QtGui.QPixmap(":/O/out_lightlinker"),
	    lightList                      = QtGui.QPixmap(":/O/out_lightlist"),
	    linearLight                    = QtGui.QPixmap(":/O/out_linearlight"),
	    list                           = QtGui.QPixmap(":/O/out_list"),
	    locator                        = QtGui.QPixmap(":/O/out_locator"),
	    luminance                      = QtGui.QPixmap(":/O/out_luminance"),
	    marble                         = QtGui.QPixmap(":/O/out_marble"),
	    materialInfo                   = QtGui.QPixmap(":/O/out_materialinfo"),
	    mesh                           = QtGui.QPixmap(":/O/out_mesh"),
	    meshVarGroup                   = QtGui.QPixmap(":/O/out_meshvargroup"),
	    mountain                       = QtGui.QPixmap(":/O/out_mountain"),
	    multDoubleLinear               = QtGui.QPixmap(":/O/out_multdoublelinear"),
	    multiplyDivide                 = QtGui.QPixmap(":/O/out_multiplydivide"),
	    nCloth                         = QtGui.QPixmap(":/O/out_ncloth"),
	    nComponent                     = QtGui.QPixmap(":/O/out_ncomponent"),
	    nParticle                      = QtGui.QPixmap(":/O/out_nparticle"),
	    nRigid                         = QtGui.QPixmap(":/O/out_nrigid"),
	    newtonField                    = QtGui.QPixmap(":/O/out_newtonfield"),
	    noise                          = QtGui.QPixmap(":/O/out_noise"),
	    normalConstraint               = QtGui.QPixmap(":/O/out_normalconstraint"),
	    nucleus                        = QtGui.QPixmap(":/O/out_nucleus"),
	    nurbsCurve                     = QtGui.QPixmap(":/O/out_nurbscurve"),
	    nurbsSurface                   = QtGui.QPixmap(":/O/out_nurbssurface"),
	    objectSet                      = QtGui.QPixmap(":/O/out_objectset"),
	    opticalFX                      = QtGui.QPixmap(":/O/out_opticalfx"),
	    orientConstraint               = QtGui.QPixmap(":/O/out_orientconstraint"),
	    parentConstraint               = QtGui.QPixmap(":/O/out_parentconstraint"),
	    particle                       = QtGui.QPixmap(":/O/out_particle"),
	    particleCloud                  = QtGui.QPixmap(":/O/out_particlecloud"),
	    particleSamplerInfo            = QtGui.QPixmap(":/O/out_particlesamplerinfo"),
	    particleShape                  = QtGui.QPixmap(":/O/out_particleshape"),
	    partition                      = QtGui.QPixmap(":/O/out_partition"),
	    pfxHair                        = QtGui.QPixmap(":/O/out_pfxhair"),
	    phong                          = QtGui.QPixmap(":/O/out_phong"),
	    phongE                         = QtGui.QPixmap(":/O/out_phonge"),
	    place2dTexture                 = QtGui.QPixmap(":/O/out_place2dtexture"),
	    place3dTexture                 = QtGui.QPixmap(":/O/out_place3dtexture"),
	    place3dTx                      = QtGui.QPixmap(":/O/out_place3dtx"),
	    plusMinusAverage               = QtGui.QPixmap(":/O/out_plusminusaverage"),
	    pointConstraint                = QtGui.QPixmap(":/O/out_pointconstraint"),
	    pointEmitter                   = QtGui.QPixmap(":/O/out_pointemitter"),
	    pointLight                     = QtGui.QPixmap(":/O/out_pointlight"),
	    poleVectorConstraint           = QtGui.QPixmap(":/O/out_polevectorconstraint"),
	    polyCone                       = QtGui.QPixmap(":/O/out_polycone"),
	    polyCube                       = QtGui.QPixmap(":/O/out_polycube"),
	    polyCylinder                   = QtGui.QPixmap(":/O/out_polycylinder"),
	    polyPlane                      = QtGui.QPixmap(":/O/out_polyplane"),
	    polySphere                     = QtGui.QPixmap(":/O/out_polysphere"),
	    polyTorus                      = QtGui.QPixmap(":/O/out_polytorus"),
	    projection                     = QtGui.QPixmap(":/O/out_projection"),
	    psdFileTex                     = QtGui.QPixmap(":/O/out_psdfiletex"),
	    quadShadingSwitch              = QtGui.QPixmap(":/O/out_quadshadingswitch"),
	    radialField                    = QtGui.QPixmap(":/O/out_radialfield"),
	    radiusDimension                = QtGui.QPixmap(":/O/out_radiusdimension"),
	    ramp                           = QtGui.QPixmap(":/O/out_ramp"),
	    refLocked                      = QtGui.QPixmap(":/O/out_reflocked"),
	    reference                      = QtGui.QPixmap(":/O/out_reference"),
	    renderLayer                    = QtGui.QPixmap(":/O/out_renderlayer"),
	    renderPass                     = QtGui.QPixmap(":/O/out_renderpass"),
	    renderPassSet                  = QtGui.QPixmap(":/O/out_renderpassset"),
	    renderTarget                   = QtGui.QPixmap(":/O/out_rendertarget"),
		transform                      = QtGui.QPixmap(":/O/out_transform"),
	    xgmArchiveGuide                = QtGui.QPixmap(":/O/out_xgmarchiveguide"),
	    xgmCardGuide                   = QtGui.QPixmap(":/O/out_xgmcardguide"),
	    xgmDescription                 = QtGui.QPixmap(":/O/out_xgmdescription"),
	    xgmNurbsPatch                  = QtGui.QPixmap(":/O/out_xgmnurbspatch"),
	    xgmPalette                     = QtGui.QPixmap(":/O/out_xgmpalette"),
	    xgmPtexViz                     = QtGui.QPixmap(":/O/out_xgmptexviz"),
	    xgmSphereGuide                 = QtGui.QPixmap(":/O/out_xgmsphereguide"),
	    xgmSplineGuide                 = QtGui.QPixmap(":/O/out_xgmsplineguide"),
	    xgmSubdPatch                   = QtGui.QPixmap(":/O/out_xgmsubdpatch")
	)
	return Icons
#----------------------------------------------------------------------
def make_logger(name, level=logging.DEBUG):
	def get_log_file(name):
		name = name.replace(" ", "_")
		try:
			folder = os.path.join(os.environ["LOCALAPPDATA"], "ArmstrongWhite", "Maya", "Tools", "Selection_Set_Editor", "Logging", name)
		except KeyError:
			try:
				folder = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "ArmstrongWhite", "Maya", "Tools", "Selection_Set_Editor", "Logging", name)
			except KeyError:
				folder = os.path.join(os.environ["TEMP"], "ArmstrongWhite", "Maya", "Tools", "Selection_Set_Editor", "Logging", name)
	
		if not os.path.exists(folder):
			os.makedirs(folder)
		filename = os.path.join(folder, "Log.txt")
		return filename
	logger = logging.getLogger(name)
	logger.propagate=0   # do not propagate to the standard Maya logger or it will double-represent it in the logs
	logger.setLevel(level)
	
	if len(logger.handlers) == 0:
		logfile          = get_log_file(name)
		stream_formatter = logging.Formatter('[%(name)s %(levelname)s] %(message)s')
		file_formatter   = logging.Formatter('%(levelname)s %(funcName)s #%(lineno)d:%(message)s')
		
		stream_handler   = logging.StreamHandler()
		file_handler     = logging.handlers.RotatingFileHandler( logfile, mode='a', maxBytes=102400, backupCount=10, encoding=None, delay=0)
		
		stream_handler.setFormatter(stream_formatter)
		stream_handler.setLevel(level)
		logger.addHandler(stream_handler)
		
		file_handler.setFormatter(file_formatter)
		file_handler.setLevel(level)
		logger.addHandler(file_handler)
	return logger
#----------------------------------------------------------------------
def createColorIcon(color):
	pixmap = QtGui.QPixmap(16, 16)
	painter = QtGui.QPainter(pixmap)
	painter.setPen(QtCore.Qt.NoPen)
	painter.fillRect(QtCore.QRect(0, 0, 16, 16), color)
	painter.end()	
	return QtGui.QIcon(pixmap)

#----------------------------------------------------------------------
def remap_Index_To_Source(func):
	'''
	This decorator is used to manage the unlocking of self for all calls that
	require change access rights to the 'network' node itself.
	'''
	@wraps(func)
	def wrapper(*args, **kws):
		view = args[0]  # args[0] is self
		index = args[1]  # args[0] is a QModelIndex
		if isinstance(view, QtGui.QAbstractItemView):
			view_model = self.model()
			if isinstance(view_model, QtGui.QSortFilterProxyModel):
				index = view_model.mapToSource(index)
		return func(self, index)
	return wrapper

#----------------------------------------------------------------------
def remap_Index_From_Source(func):
	'''
	This decorator is used to manage the unlocking of self for all calls that
	require change access rights to the 'network' node itself.
	'''
	@wraps(func)
	def wrapper(*args, **kws):
		view = args[0]  # args[0] is self
		index = args[1]  # args[0] is a QModelIndex
		if isinstance(view, QtGui.QAbstractItemView):
			view_model = self.model()
			if isinstance(view_model, QtGui.QSortFilterProxyModel):
				index = view_model.mapFromSource(index)
		return func(self, index)
	return wrapper

########################################################################
class Counter(object):
	#----------------------------------------------------------------------
	def __init__(self,start=1):
		self.num = count(int(start))
	#----------------------------------------------------------------------
	def __call__(self):
		return self.num.next()
_userRole_counter    = Counter(QtCore.Qt.ItemDataRole.UserRole)
_userType_counter    = Counter(QtGui.QStandardItem.UserType)
########################################################################
class _Global_Options(object):
	display_show_name_spaces  = General_Util.OptionVar("aw_selection_set_editor_tools_namespaces", True)
	display_option_Tools      = General_Util.OptionVar("aw_selection_set_editor_tools_visablity", True)
	display_option_Creation   = General_Util.OptionVar("aw_selection_set_editor_creation_tools_visablity", True)
	display_option_Assinments = General_Util.OptionVar("aw_selection_set_editor_assinments_tools_visablity", True)
	display_option_Selection  = General_Util.OptionVar("aw_selection_set_editor_selection_tools_visablity", True)
	display_option_Viewport   = General_Util.OptionVar("aw_selection_set_editor_viewport_tools_visablity", True)
	selection_set_outliner_option_Filter_Syntax = General_Util.OptionVar("aw_selection_set_editor_outlineer_filter_syntax", 1)
	selection_set_outliner_option_Filter_Case_Sensitivity = General_Util.OptionVar("aw_selection_set_editor_outlineer_filter_case_sensitivity", 0)
	selection_set_outliner_option_Filter_Scan_Type = General_Util.OptionVar("aw_selection_set_editor_outlineer_filter_scan_type", 0)
########################################################################
class ActiveSelectionRestore(object):
	''''''
	#----------------------------------------------------------------------
	def __enter__(self):
		self.active_Selection = Util_API.get_Active_Selection_List(OldApi=False)
		return None
	#----------------------------------------------------------------------
	def __exit__(self, type, value, traceback):
		cmds.select(self.active_Selection.getSelectionStrings())
########################################################################
class AW_Master_Selection_Set(Util_API.SelectionSet):
	#----------------------------------------------------------------------
	def __init__(self):
		super(AW_Master_Selection_Set,self).__init__(self.__class__.__name__,empty=True,copy=None,text="bookmarkModelView")
		
	#----------------------------------------------------------------------
	@property
	def members(self):
		try:
			return [Maya_Node(m) for m in cmds.listConnections(self._dagSetMembers_plug.name,destination=False,source=True, shapes=True)]
		except TypeError:
			return []
########################################################################
class Root_Selection_Set(Util_API.SelectionSet):
	#----------------------------------------------------------------------
	def __init__(self,name=None):
		if name is None:
			super(Root_Selection_Set,self).__init__(cmds.sets(name="Seperation_Set_0", text="bookmarkModelView", empty=True, renderable=False))
			self.Origanal_Object_set = Scripts.OpenMaya_Util_API.SelectionSet(cmds.sets(name="Orig_Objects_Set_0", text="bookmarkModelView", empty=True, renderable=False))
			self.Master_Object_Set   = Scripts.OpenMaya_Util_API.SelectionSet(cmds.sets(name="Master_Object_Set_0", text="bookmarkModelView", empty=True, renderable=False))
			self.Slave_Object_Set    = Scripts.OpenMaya_Util_API.SelectionSet(cmds.sets(name="Slave_Objects_Set_0", text="bookmarkModelView", empty=True, renderable=False))

			self.include(self.Origanal_Object_set)
			self.include(self.Master_Object_Set)
			self.include(self.Slave_Object_Set)
		else:
			super(Root_Selection_Set,self).__init__(name)
			for child in self.children:
				if child.name.startswith("Orig_Objects_Set"):
					self.Origanal_Object_set = child
				if child.name.startswith("Master_Object_Set"):
					self.Master_Object_Set = child
				if child.name.startswith("Slave_Objects_Set"):
					self.Slave_Object_Set = child
		self.lockNode()
		self.Origanal_Object_set.lockNode()
		self.Master_Object_Set.lockNode()
		self.Slave_Object_Set.lockNode()
	#----------------------------------------------------------------------
	def add_orig_object(self,obj):
		set_list = cmds.listSets( o=obj)
		if set_list is not None:
			for item in set_list:
				if item.statswith("Orig_Objects_Set") or item.startswith("Master_Object_Set") or item.startwtih("Slave_Objects_Set"):
					return False
		self.Origanal_Object_set.include(obj)
		return True
########################################################################
class Maya_QWidget(Scripts.UICls.mayaMixin.MayaQWidgetBaseMixin, QtGui.QWidget):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Maya_QWidget, self).__init__(parent=parent)
########################################################################
class OptionVariable_Bool_Action(QT.QtGui.QAction):
	def __init__(self, name, var_name, var_val=True, parent=None):
		super(OptionVariable_Bool_Action, self).__init__(name, parent)
		if isinstance(var_name, General_Util.OptionVar):
			self._variable = var_name
		else:
			self._variable = General_Util.OptionVar(var_name, var_val)
		self.setCheckable(True)
		self.setChecked(Qt.Checked if self.variable_value else Qt.Unchecked)
		self.changed.connect(self.update_variable)
	#----------------------------------------------------------------------
	@QtSlot()
	def update_variable(self):
		""""""
		self.variable_value =  self.isChecked()
	#----------------------------------------------------------------------
	@property
	def variable_value(self):
		""""""
		return self._variable.value
	#----------------------------------------------------------------------
	@variable_value.setter
	def variable_value(self, val):
		""""""
		self._variable.value = val
########################################################################
class Display_Option_Tool_Button(QT.QtGui.QToolButton):
	def run_setup(self):
		self.setText("Display Options")
		self.option_Tools      = OptionVariable_Bool_Action("Tools", _Global_Options.display_option_Tools, parent=self)
		self.option_Creation   = OptionVariable_Bool_Action("Creation", _Global_Options.display_option_Creation, parent=self)
		self.option_Assinments = OptionVariable_Bool_Action("Assinments", _Global_Options.display_option_Assinments, parent=self)
		self.option_Selection  = OptionVariable_Bool_Action("Selection", _Global_Options.display_option_Selection, parent=self)
		self.option_Viewport   = OptionVariable_Bool_Action("Viewport", _Global_Options.display_option_Viewport, parent=self)
		self.addActions([self.option_Tools, self.option_Creation, self.option_Assinments, self.option_Selection, self.option_Viewport])
########################################################################
class Surface_Shader_Types_QComboBox(QT.QtGui.QComboBox):
	def __init__(self, parent=None):
		super(Surface_Shader_Types_QComboBox, self).__init__(parent=parent)
		items = cmds.listNodeTypes( 'shader/surface', ex='shader/volume' )
		items.sort()
		self.addItems(items)

########################################################################
class OptionVariable_ComboBox(QT.QtGui.QComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None, var_name=None, var_val=0):
		super(OptionVariable_ComboBox, self).__init__(parent)
		if isinstance(var_name, General_Util.OptionVar):
			self._variable = var_name
		else:
			self._variable = General_Util.OptionVar(var_name, var_val)
	#----------------------------------------------------------------------
	def _inishalize(self):
		""""""
		self.setCurrentIndex(self._variable.value)
		self.currentIndexChanged.connect(self.update_variable)
	#----------------------------------------------------------------------
	@QtSlot(int)
	def update_variable(self, index):
		""""""
		self._variable.value =  index

########################################################################
class Filter_Syntax_Options_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Filter_Syntax_Options_ComboBox, self).__init__(parent=parent, var_name=_Global_Options.selection_set_outliner_option_Filter_Syntax, var_val=0)
		self.addItem("Regular expression",QtCore.QRegExp.RegExp)
		self.addItem("Wildcard",QtCore.QRegExp.Wildcard)
		self.addItem("Fixed string",QtCore.QRegExp.FixedString)
		self._inishalize()
########################################################################
class Filter_Case_Sensitivity_Options_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Filter_Case_Sensitivity_Options_ComboBox, self).__init__(parent=parent, var_name=_Global_Options.selection_set_outliner_option_Filter_Case_Sensitivity, var_val=0)
		self.addItem("Insensitive",QtCore.Qt.CaseSensitivity.CaseInsensitive)
		self.addItem("Sensitive",QtCore.Qt.CaseSensitivity.CaseSensitive)
		self._inishalize()
########################################################################
class Filter_Scan_Options_ComboBox(OptionVariable_ComboBox):
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Filter_Scan_Options_ComboBox, self).__init__(parent=parent, var_name=_Global_Options.selection_set_outliner_option_Filter_Scan_Type, var_val=0)
		self.addItem("Simple")
		self.addItem("Complex")
		self._inishalize()
		
########################################################################
class Tool_Button(QtGui.QToolButton):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		"""Constructor"""
		super(Tool_Button, self).__init__(parent=parent)
########################################################################
class ITEM_DATA_GLOBAL_DEFAULT_VALUES:
	""""""
	class FONT:
		family          = "Arial"
		pointSize       = 7
		weight          = QtGui.QFont.Weight.Normal
		capitalization  = QtGui.QFont.MixedCase
	class DISPLAY:
		background_color = QtGui.QColor(QtCore.Qt.GlobalColor.black)
		foreground_color = QtGui.QColor(QtCore.Qt.GlobalColor.white)
		icon_color       = QtGui.QColor(QtCore.Qt.GlobalColor.red)
		brush            = QtGui.QBrush(QtCore.Qt.GlobalColor.red)
		alignment        = QtCore.Qt.AlignmentFlag(QtCore.Qt.AlignmentFlag.AlignLeft)

	font             = QtGui.QFont(FONT.family, FONT.pointSize)
	font.setCapitalization(FONT.capitalization)
	font.setWeight(FONT.weight)
	icon             = None
########################################################################
class Alignment:
	""""""
	class Horizontal:
		Left    = QtCore.Qt.AlignmentFlag.AlignLeft
		Right   = QtCore.Qt.AlignmentFlag.AlignRight
		Center  = QtCore.Qt.AlignmentFlag.AlignHCenter
		Values  = {'Center' : Center, Center: "Center",
		           'Left'   : Left,   Left  : "Left",
		           'Right'  : Right,  Right : "Right"}
	class Vertical:
		Top     = QtCore.Qt.AlignmentFlag.AlignTop
		Bottom  = QtCore.Qt.AlignmentFlag.AlignBottom
		Center  = QtCore.Qt.AlignmentFlag.AlignVCenter
		Values  = {'Top'    : Top   , Top     : "Top",
		           'Bottom' : Bottom, Bottom  : "Bottom",
		           'Center' : Center, Center  : "Center"}
########################################################################
class ITEM_DATA_ROLE:
	""""""
	DisplayRole               = QtCore.Qt.ItemDataRole.DisplayRole
	EditRole                  = QtCore.Qt.ItemDataRole.EditRole
	ForegroundRole            = QtCore.Qt.ItemDataRole.ForegroundRole
	BackgroundRole            = QtCore.Qt.ItemDataRole.BackgroundRole
	SizeHintRole              = QtCore.Qt.ItemDataRole.SizeHintRole
	ToolTipRole               = QtCore.Qt.ItemDataRole.ToolTipRole
	StatusTipRole             = QtCore.Qt.ItemDataRole.StatusTipRole
	FontRole                  = QtCore.Qt.ItemDataRole.FontRole
	TextAlignmentRole         = QtCore.Qt.ItemDataRole.TextAlignmentRole
	DecorationRole            = QtCore.Qt.ItemDataRole.DecorationRole
	CheckStateRole            = QtCore.Qt.ItemDataRole.CheckStateRole
	UserRole                  = _userRole_counter()
	NameSpaceRole             = _userRole_counter()
	FullNameRole              = _userRole_counter()
	IconColorRole             = _userRole_counter() 
	IconVisableRole           = _userRole_counter()
	FontSizeRole              = _userRole_counter()
	FontFamilyRole            = _userRole_counter()
	FontWeightRole            = _userRole_counter()
	FontCapitalizationRole    = _userRole_counter()
	SelectableRole            = _userRole_counter()
	EnabledRole               = _userRole_counter()
	EditableRole              = _userRole_counter()
	DragableRole              = _userRole_counter()
	DropableRole              = _userRole_counter()
	CheckableRole             = _userRole_counter()
	TristateRole              = _userRole_counter()
	Horizontal_AlignmentRole  = _userRole_counter()
	Vertical_AlignmentRole    = _userRole_counter()
	Internal_Data_Role        = _userRole_counter()
	Item_Type_Role            = _userRole_counter()
	Tree_Item_Role            = _userRole_counter()
########################################################################
class WidgetDelegate(QtGui.QStyledItemDelegate):
	"""A delegate for drawing a arbitrary QWidget"""
	#----------------------------------------------------------------------
	def __init__(self, item_data, parent=None):
		""""""
		super(WidgetDelegate, self).__init__(parent)
		self.item_data = item_data
		isinstance(self.item_data, Item_Data)
	#----------------------------------------------------------------------
	def paint(self, painter, option, index):
		""""""
		QtGui.QStyledItemDelegate.paint(self, painter, option, index)
	#----------------------------------------------------------------------
	def editorEvent(self, event, model, option, index):
		""""""
		return super(WidgetDelegate, self).editorEvent(event, model, option, index)
	#----------------------------------------------------------------------
	def helpEvent(self, event, view, option, index):
		""""""
		super(WidgetDelegate, self).helpEvent(event, view, option, index)
	#----------------------------------------------------------------------
	def sizeHint(self, option, index):
		""""""
		return QtGui.QStyledItemDelegate.sizeHint(self, option, index)
	#----------------------------------------------------------------------
	def commitData(self, editor):
		""""""
		super(WidgetDelegate, self).commitData(editor)
	#----------------------------------------------------------------------
	def createEditor(self, parent, option, index):
		""" Creates and returns the custom object we'll use to edit."""
		editor = self.item_data.create_editor(parent)
		if editor is None:
			return QtGui.QStyledItemDelegate.createEditor(self, parent, option, index)
		else:
			return editor
	#----------------------------------------------------------------------
	def closeEditor(self, editor, endedithint=QtGui.QAbstractItemDelegate.NoHint):
		""""""
		super(WidgetDelegate, self).closeEditor(editor, endedithint)
	#----------------------------------------------------------------------
	def setEditorData(self, editor, index):
		""" Sets the data to be displayed and edited by our custom editor. """
		QtGui.QStyledItemDelegate.setEditorData(self, editor, index)
	#----------------------------------------------------------------------
	def setModelData(self, editor, model, index):
		""" Get the data from our custom editor and stuffs it into the model."""
		QtGui.QStyledItemDelegate.setModelData(self, editor, model, index) 
# ======================================================================
# DATA MODEL STANDERD ITEMS TYPES
# ----------------------------------------------------------------------
# Synopsis:
#     Each Items Constains All The Information Needed To Display Itself
#     In A Column for View such as
#     font size, font color, display name ect.
# ======================================================================
########################################################################
class _Standered_Item_Data_Storage(object):
	#----------------------------------------------------------------------
	def __init__(self,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None):
		""""""
		#if not isinstance(tree_item, Tree_Item):
			#raise ValueError("tree_item input must be and instance or subclass of Tree_Item and a %r was found" % type(tree_item))
		self.tree_item                  = tree_item
		isinstance(self.tree_item, Tree_Item)
		
		self._item_selectable           = selectable
		self._item_enabled              = enabled
		self._item_editable             = editable
		self._item_dragable             = dragable
		self._item_dropable             = dropable
		self._item_checkable            = checkable
		self._item_tristate             = tristate
		self._item_display_name         = display_name
		self._item_font_family          = font_family
		self._item_font_size            = font_size
		self._item_font_weight          = font_weight
		self._item_font_capitalization  = font_capitalization
		self._item_background_color     = background_color
		self._item_foreground_color     = foreground_color
		self._item_brush                = brush
		self._item_icon_visable         = icon_visable
		self._item_icon_color           = icon_color
		self._item_size_hint            = size_hint
		self._item_status_tip           = status_tip
		self._item_tool_tip             = tool_tip
		self._item_horizontal_alignment = horizontal_alignment
		self._item_vertical_alignment   = vertical_alignment
		self._data_icon                 = None
		self._data_font                 = None
		self._data_foreground_color     = None
		self._data_background_color     = None
		self._data_alignment            = None
		self._data_flags                = Qt.ItemFlags()
		self._update_flags()
		if False:
			isinstance(self.background_color,QtGui.QColor)
			isinstance(self.foreground_color,QtGui.QColor)
			isinstance(self.brush,QtGui.QBrush)
			isinstance(self.size_hint,QtCore.QSize)
			isinstance(self.status_tip,str)
			isinstance(self.tool_tip,str) 
			isinstance(self.text_font,QtGui.QFont)   
	#----------------------------------------------------------------------
	def create_editor(self, parent=None):
		editor = QtGui.QLineEdit(parent)
		return editor
	#----------------------------------------------------------------------
	def create_Widget_Delegate(self, parent=None):
		return WidgetDelegate(self, parent=parent)
	#----------------------------------------------------------------------
	def createColorIcon(self, color):
		pixmap = QtGui.QPixmap(16, 16)
		painter = QtGui.QPainter(pixmap)
		painter.setPen(QtCore.Qt.NoPen)
		painter.fillRect(QtCore.QRect(0, 0, 16, 16), color)
		#painter.fillRect(QtCore.QRect(0, 10, 20, 10), QtCore.Qt.GlobalColor.green)
		painter.end()
		return QtGui.QIcon(pixmap)
	#----------------------------------------------------------------------
	def get_Current_State(self):
		""""""
		state = dict()
		for key in self.__dict__.keys():
			if key.startswith("_item_"):
				val = getattr(self, key)
				if not val is None:
					key = key.replace("_item_", "")
					state[key] = val
		return state
	#----------------------------------------------------------------------
	def set_Current_State(self, state):
		""""""
		if not isinstance(state,dict):
			raise ValueError("input state must be a dict and a %r was given" % type(state))
		for key, val in state.iteritems():
			if hasattr(self, "_item_"+key):
				if val is not None:
					try:
						setattr(self, key, val)
					except AttributeError:
						pass
	#----------------------------------------------------------------------
	@property
	def icon_visable(self):
		"""Returns Weather Or Not The Icon Is Visable"""
		if self._item_icon_visable is None:
			return False
		else:
			return self._item_icon_visable
	#----------------------------------------------------------------------
	@icon_visable.setter
	def icon_visable(self, value):
		"""Set Weather Or Not The Icon Is Visable"""
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be of type bool or int and a %r was given" % type(value))
		self._item_icon_visable = value
	#----------------------------------------------------------------------
	@property
	def background_color(self):
		"""Get The Backround Color Of A Item"""
		if self._data_background_color is None:
			return None
		return self._data_background_color
	#----------------------------------------------------------------------
	@background_color.setter
	def background_color(self, value):
		if value is None:
			self._item_background_color = value
		elif isinstance(value,QtGui.QColor):
			self._item_background_color = value.getRgb()
		else:
			raise ValueError("input value must be an instance of QtGui.QColor and a %r was given" % type(value))
		self._update_background_color()
	#----------------------------------------------------------------------
	@property
	def foreground_color(self):
		if self._data_foreground_color is None:
			return None
		return self._data_foreground_color
	#----------------------------------------------------------------------
	@foreground_color.setter
	def foreground_color(self, value):
		if value is None:
			self._item_foreground_color = value
		elif isinstance(value,QtGui.QColor):
			self._item_foreground_color = value.getRgb()
		else:
			raise ValueError("input value must be an instance of QtGui.QColor and a %r was given" % type(value))
		self._update_foregound_color()
	#----------------------------------------------------------------------
	@property
	def brush(self):
		if self._item_brush is None:
			return QtGui.QBrush(QtCore.Qt.GlobalColor.red)
		else:
			return self._item_brush
	#----------------------------------------------------------------------
	@brush.setter
	def brush(self, value):
		if not isinstance(value,QtGui.QBrush):
			raise ValueError("input value must be an instance of QtGui.QBrush and a %r was given" % type(value))
		self._item_bush = value
	#----------------------------------------------------------------------
	@property
	def size_hint(self):
		return self._item_size_hint
	#----------------------------------------------------------------------
	@size_hint.setter
	def size_hint(self, value):
		if not isinstance(value,QtCore.QSize):
			raise ValueError("input value must be an instance of QtCore.QSize and a %r was given" % type(value))
		self._item_size_hint = value	
	#----------------------------------------------------------------------
	@property
	def status_tip(self):
		if self._item_status_tip is None:
			return ""
		else:
			return self._item_status_tip
	#----------------------------------------------------------------------
	@status_tip.setter
	def status_tip(self, value):
		if not isinstance(value,(str,unicode)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_status_tip = value
	#----------------------------------------------------------------------
	@property
	def tool_tip(self):
		if self._item_tool_tip is None:
			return ""
		else:
			return self._item_tool_tip
	#----------------------------------------------------------------------
	@tool_tip.setter
	def tool_tip(self, value):
		if not isinstance(value,(str,unicode)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_tool_tip = value
	#----------------------------------------------------------------------
	@property
	def vertical_alignment(self):
		if self._item_vertical_alignment is None:
			return Alignment.Vertical.Center
		return Alignment.Vertical.Values[self._item_vertical_alignment]
	#----------------------------------------------------------------------
	@vertical_alignment.setter
	def vertical_alignment(self, value):
		if value is None:
			self._item_vertical_alignment = value
		elif value in Alignment.Vertical.Values.keys():
			if not isinstance(value,(str,unicode)):
				value = Alignment.Vertical.Values[value]
			self._item_vertical_alignment = value
		else:
			raise ValueError("input value must be an instance of (str,unicode,int) and a %r was given" % type(value))
		self._update_text_alignment()
	#----------------------------------------------------------------------
	@property
	def horizontal_alignment(self):
		if self._item_horizontal_alignment is None:
			return Alignment.Horizontal.Left
		return Alignment.Horizontal.Values[self._item_horizontal_alignment]
	#----------------------------------------------------------------------
	@horizontal_alignment.setter
	def horizontal_alignment(self, value):
		if value is None:
			self._item_horizontal_alignment = value
		elif value in Alignment.Horizontal.Values.keys():
			if not isinstance(value,(str,unicode)):
				value = Alignment.Horizontal.Values[value]
			self._item_horizontal_alignment = value
		else:
			raise ValueError("input value must be an instance of (str,unicode,int) and a %r was given" % type(value))
		self._update_text_alignment()
	#----------------------------------------------------------------------
	@property
	def text_alignment(self):
		if self._data_alignment is None:
			return self._update_text_alignment()
		return self._data_alignment
	#----------------------------------------------------------------------
	@property
	def font_family(self):
		if self._item_font_family is None:
			return False
		else:
			return self._item_font_family
	#----------------------------------------------------------------------
	@font_family.setter
	def font_family(self, value):
		if not isinstance(value,(str, unicode)):
			raise ValueError("input value must be an instance of str, unicode and a %r was given" % type(value))
		self._item_font_family = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def font_size(self):
		if self._item_font_size is None:
			return False
		else:
			return self._item_font_size
	#----------------------------------------------------------------------
	@font_size.setter
	def font_size(self, value):
		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		self._item_font_size = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def font_weight(self):
		if self._item_font_weight is None:
			return False
		else:
			return self._item_font_weight
	#----------------------------------------------------------------------
	@font_weight.setter
	def font_weight(self, value):

		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		if int(value) == 0:
			value = None
		elif not int(value) in [25, 50, 63, 75, 87]:
			raise ValueError("input value must be one of the fallowing values of 25, 50, 63, 75, 87 and %i was given" % int(value))
		self._item_font_weight = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def font_capitalization(self):
		if self._item_font_capitalization is None:
			return False
		else:
			return self._item_font_capitalization
	#----------------------------------------------------------------------
	@font_capitalization.setter
	def font_capitalization(self, value):
		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		self._item_font_capitalization = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def selectable(self):
		if self._item_selectable is None:
			return True
		else:
			return self._item_selectable
	#----------------------------------------------------------------------
	@selectable.setter
	def selectable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_selectable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def enabled(self):
		if self._item_enabled is None:
			return True
		else:
			return self._item_enabled
	#----------------------------------------------------------------------
	@enabled.setter
	def enabled(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_enabled = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def editable(self):
		if self._item_editable is None:
			return True
		else:
			return self._item_editable 
	#----------------------------------------------------------------------
	@editable.setter
	def editable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_editable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def dragable(self):
		if self._item_dragable is None:
			return True
		else:
			return self._item_dragable
	#----------------------------------------------------------------------
	@dragable.setter
	def dragable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_dragable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def dropable(self):
		if self._item_dropable is None:
			return True
		else:
			return self._item_dropable 
	#----------------------------------------------------------------------
	@dropable.setter
	def dropable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_dropable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def checkable(self):
		if self._item_checkable is None:
			return False
		else:
			return self._item_checkable
	#----------------------------------------------------------------------
	@checkable.setter
	def checkable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_checkable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def tristate(self):
		if self._item_tristate is None:
			return False
		else:
			if self.checkable:
				return self._item_tristate
			else:
				return False
	#----------------------------------------------------------------------
	@tristate.setter
	def tristate(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_tristate = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def display_name(self):
		if self._item_display_name is None:
			return False
		else:
			return self._item_display_name
	#----------------------------------------------------------------------
	@display_name.setter
	def display_name(self, value):
		if not isinstance(value,(str, unicode)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_display_name = value
	#----------------------------------------------------------------------
	@property
	def icon_color(self):
		if self._item_icon_color is None:
			return ITEM_DATA_GLOBAL_DEFAULT_VALUES.DISPLAY.icon_color
		else:
			return self._item_icon_color
	#----------------------------------------------------------------------
	@icon_color.setter
	def icon_color(self, value):
		if not isinstance(value,(QtGui.QColor, QtCore.Qt.GlobalColor)):
			raise ValueError("input value must be an instance of (QtGui.QColor, QtCore.Qt.GlobalColor) and a %r was given" % type(value))
		self._item_icon_color = value
		self._data_icon  = self.createColorIcon(self._item_icon_color)
	#----------------------------------------------------------------------
	@property
	def font(self):
		""""""
		if any([val is not False for val in self.font_attributes]):
			return self._data_font
		else:
			return ITEM_DATA_GLOBAL_DEFAULT_VALUES.font
	#----------------------------------------------------------------------
	@property
	def icon(self):
		""""""
		if self.icon_visable:
			if self._data_icon is None:
				if ITEM_DATA_GLOBAL_DEFAULT_VALUES.icon is None:
					ITEM_DATA_GLOBAL_DEFAULT_VALUES.icon = createColorIcon(QtGui.QColor(ITEM_DATA_GLOBAL_DEFAULT_VALUES.DISPLAY.icon_color))
				return ITEM_DATA_GLOBAL_DEFAULT_VALUES.icon
			else:
				return self._data_icon
		else:
			return None
	#----------------------------------------------------------------------
	@icon.setter
	def icon(self, pixmap):
		""""""
		if not isinstance(pixmap,(QtGui.QPixmap)):
			raise ValueError("input value must be an instance of (QtGui.QPixmap) and a %r was given" % type(pixmap))
		else:
			self._data_icon = pixmap
		return None
	@property
	#----------------------------------------------------------------------
	def column(self):
		""""""
		return self.tree_item._column_items.items.index(self)
	@property
	#----------------------------------------------------------------------
	def index(self):
		""""""
		return self.tree_item.model.indexFromItemData(self)
	#----------------------------------------------------------------------
	@property
	def flags(self):
		""""""
		return self._data_flags
	@property
	def font_attributes(self):
		return [self.font_family, self.font_size, self.font_weight, self.font_capitalization]
	#----------------------------------------------------------------------
	def _update_font(self):
		""""""
		local_font_atts = self.font_attributes
		global_font_attrs = [ITEM_DATA_GLOBAL_DEFAULT_VALUES.FONT.family, ITEM_DATA_GLOBAL_DEFAULT_VALUES.FONT.pointSize, ITEM_DATA_GLOBAL_DEFAULT_VALUES.FONT.weight, ITEM_DATA_GLOBAL_DEFAULT_VALUES.FONT.capitalization]

		if any([val is not False for val in local_font_atts]):
			if self._data_font is None:
				self._data_font = QtGui.QFont(ITEM_DATA_GLOBAL_DEFAULT_VALUES.font)
			fn_list = [self._data_font.setFamily, self._data_font.setPointSize, self._data_font.setWeight, self._data_font.setCapitalization]
			self._data_font.setFamily
			for loc, glob, fn in zip(local_font_atts, global_font_attrs, fn_list):
				if not loc is False:
					fn(loc)
				else:
					fn(glob)
	#----------------------------------------------------------------------
	def _update_flags(self):
		""""""
		flgs = QtCore.Qt.ItemFlags()
		if self.selectable:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsSelectable
		if self.editable:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsEditable
		if self.enabled:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsEnabled
		if self.dragable:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsDragEnabled
		if self.dropable:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsDropEnabled
		if self.checkable:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsUserCheckable
		if self.tristate:
			flgs =  flgs | QtCore.Qt.ItemFlag.ItemIsTristate
		self._data_flags = flgs
	#----------------------------------------------------------------------
	def _update_text_alignment(self):
		""""""
		self._data_alignment = QtCore.Qt.AlignmentFlag(self.horizontal_alignment|self.vertical_alignment)
	#----------------------------------------------------------------------
	def _update_foregound_color(self):
		""""""
		if self._item_foreground_color is None:
			self._data_foreground_color = ITEM_DATA_GLOBAL_DEFAULT_VALUES.DISPLAY.foreground_color
		else:
			self._data_foreground_color = QtGui.QColor(*self._item_foreground_color)
	#----------------------------------------------------------------------
	def _update_background_color(self):
		""""""
		if self._item_background_color is None:
			self._data_background_color = ITEM_DATA_GLOBAL_DEFAULT_VALUES.DISPLAY.background_color
		else:
			self._data_background_color = QtGui.QColor(*self._item_background_color)
	#----------------------------------------------------------------------
	def data(self, role=ITEM_DATA_ROLE.DisplayRole):
		if role in [ITEM_DATA_ROLE.DisplayRole, ITEM_DATA_ROLE.EditRole]:
			return self.display_name
		elif role == ITEM_DATA_ROLE.ForegroundRole:
			return self.foreground_color
		elif role == ITEM_DATA_ROLE.BackgroundRole:
			return self.background_color
		elif role == ITEM_DATA_ROLE.SizeHintRole:
			return self.size_hint
		elif role == ITEM_DATA_ROLE.ToolTipRole:
			return self.tool_tip
		elif role == ITEM_DATA_ROLE.StatusTipRole:
			return self.status_tip
		elif role == ITEM_DATA_ROLE.FontRole:
			return self.font
		elif role == ITEM_DATA_ROLE.TextAlignmentRole:
			return self.text_alignment
		elif role == ITEM_DATA_ROLE.DecorationRole:
			if self.icon_visable:
				return self.icon
			else:
				return None
		elif role == ITEM_DATA_ROLE.IconColorRole:
			return self.icon_color
		elif role == ITEM_DATA_ROLE.FontSizeRole:
			return self.text_size
		elif role == ITEM_DATA_ROLE.FontWeightRole:
			return self.font_weight
		elif role == ITEM_DATA_ROLE.Horizontal_AlignmentRole:
			return self.horizontal_alignment
		elif role == ITEM_DATA_ROLE.Vertical_AlignmentRole:
			return self.vertical_alignment
		elif role == ITEM_DATA_ROLE.CheckStateRole:
			return None #Qt.CheckState(Qt.CheckState.Unchecked)
		elif role == ITEM_DATA_ROLE.UserRole:
			return self
		elif role == ITEM_DATA_ROLE.Tree_Item_Role:
			return self.tree_item
		return None
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role in [ITEM_DATA_ROLE.DisplayRole, ITEM_DATA_ROLE.EditRole]:
			self.display_name = value
		elif role == ITEM_DATA_ROLE.ForegroundRole:
			self.foreground_color = value
		elif role == ITEM_DATA_ROLE.BackgroundRole:
			self.background_color = value
		elif role == ITEM_DATA_ROLE.SizeHintRole:
			self.size_hint        = value
		elif role == ITEM_DATA_ROLE.ToolTipRole:
			self.tool_tip         = value
		elif role == ITEM_DATA_ROLE.StatusTipRole:
			self.status_tip       = value
		elif role == ITEM_DATA_ROLE.FontRole:
			self.text_font        = value
		elif role == ITEM_DATA_ROLE.TextAlignmentRole:
			self.text_alignment   = value
		elif role == ITEM_DATA_ROLE.DecorationRole:
			self.brush            = value
		elif role == ITEM_DATA_ROLE.IconColorRole:
			self.icon_color       = value
		elif role == ITEM_DATA_ROLE.FontSizeRole:
			self.text_size        = value
		elif role == ITEM_DATA_ROLE.FontWeightRole:
			self.font_weight      = value
		elif role == ITEM_DATA_ROLE.FontFamilyRole:
			self.font_family         = value
		elif role == ITEM_DATA_ROLE.FontCapitalizationRole:
			self.font_capitalization = value
		elif role == ITEM_DATA_ROLE.SelectableRole:
			self.selectable        = value
		elif role == ITEM_DATA_ROLE.EnabledRole:
			self.enabled =  value
		elif role == ITEM_DATA_ROLE.EditableRole:
			self.editable = value
		elif role == ITEM_DATA_ROLE.DragableRole:
			self.dragable = value
		elif role == ITEM_DATA_ROLE.DropableRole:
			self.dropable = value
		elif role == ITEM_DATA_ROLE.CheckableRole:
			self.checkable = value
		elif role == ITEM_DATA_ROLE.TristateRole:
			self.tristate = value
		elif role == ITEM_DATA_ROLE.Horizontal_AlignmentRole:
			self.horizontal_alignment = value
		elif role == ITEM_DATA_ROLE.Vertical_AlignmentRole:
			self.vertical_alignment = value
		else:
			return False
	#----------------------------------------------------------------------
	def update(self):
		return self.tree_item.model.dataChanged(self.index, self.index)	
########################################################################
class Item_Data(_Standered_Item_Data_Storage):
	#----------------------------------------------------------------------
	def __init__(self,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None,
	             internal_data = None):
		""" """
		super(Item_Data, self).__init__(tree_item,
		                                selectable           = selectable          , enabled             = enabled            , editable     = editable,
		                                dragable             = dragable            , dropable            = dropable           , checkable    = checkable,
		                                tristate             = tristate            , font_family         = font_family        , font_size    = font_size,
		                                size_hint            = size_hint           , status_tip          = status_tip         , tool_tip     = tool_tip,
		                                brush                = brush               , icon_visable        = icon_visable       , icon_color   = icon_color,
		                                font_weight          = font_weight         , font_capitalization = font_capitalization, display_name = display_name,
		                                background_color     = background_color    , foreground_color    = foreground_color,
		                                horizontal_alignment = horizontal_alignment, vertical_alignment  = vertical_alignment)
		self._internal_data = internal_data
	#----------------------------------------------------------------------
	def data(self, role):
		if role == ITEM_DATA_ROLE.Internal_Data_Role:
			return self.internal_data
		return super(Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role == ITEM_DATA_ROLE.Internal_Data_Role:
			self.internal_data = value
		else:
			super(Item_Data, self).setData(role, value)
	#----------------------------------------------------------------------
	@property
	def internal_data(self):
		""""""
		return self._internal_data
	#----------------------------------------------------------------------
	@internal_data.setter
	def internal_data(self, value):
		""""""
		self._internal_data = value
########################################################################
class MPLUG_Item_Data(Item_Data):
	#----------------------------------------------------------------------
	def __init__(self, maya_node,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None):
		""" """
		super(MPLUG_Item_Data, self).__init__(tree_item,
		                                     selectable           = selectable          , enabled             = enabled            , editable     = editable,
		                                     dragable             = dragable            , dropable            = dropable           , checkable    = checkable,
		                                     tristate             = tristate            , font_family         = font_family        , font_size    = font_size,
		                                     size_hint            = size_hint           , status_tip          = status_tip         , tool_tip     = tool_tip,
		                                     brush                = brush               , icon_visable        = icon_visable       , icon_color   = icon_color,
		                                     font_weight          = font_weight         , font_capitalization = font_capitalization, display_name = display_name,
		                                     background_color     = background_color    , foreground_color    = foreground_color,
		                                     horizontal_alignment = horizontal_alignment, vertical_alignment  = vertical_alignment,
		                                     internal_data        = maya_node)
		isinstance(self.internal_data, Util_API.MPLUG)
		# if str(self.internal_data.objectType) in _Maya_Node_Type_Icons.keys():
			# self.icon = QtGui.QPixmap(_Maya_Node_Type_Icons[str(self.internal_data.objectType)])
			# self.icon_visable = True
		# if self.internal_data.transfromType == "group" and self.internal_data.objectType == "transform":
			# self.icon = QtGui.QPixmap(":/G/group")
		# elif self.internal_data.transfromType == "mesh":
			# self.icon = QtGui.QPixmap(":/O/out_mesh")

			# self.icon_visable = True
	#----------------------------------------------------------------------
	def data(self, role=ITEM_DATA_ROLE.DisplayRole):
		if role in [ITEM_DATA_ROLE.DisplayRole, ITEM_DATA_ROLE.EditRole]:
			if _Global_Options.display_show_name_spaces.value:
				return self.internal_data.longName
			else:
				return self.internal_data.nice_name_wo_ns

		if role in [ITEM_DATA_ROLE.ForegroundRole]:
			active_selection = cmds.ls(sl=True, long=True)
			if self.internal_data.name in active_selection:
				return QtGui.QColor(Qt.green)

		if role == ITEM_DATA_ROLE.NameSpaceRole:
			return self.internal_data.namespace
		if role == ITEM_DATA_ROLE.FullNameRole:
			return self.internal_data.name
		return super(MPLUG_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role in [ITEM_DATA_ROLE.EditRole]:
			if _Global_Options.display_show_name_spaces.value:
				self.internal_data.name = value
			else:
				self.internal_data.name = self.internal_data.namespace + ":" + value
		else:
			super(MPLUG_Item_Data, self).setData(role, value)
########################################################################
class Maya_Item_Data(Item_Data):
	#----------------------------------------------------------------------
	def __init__(self, maya_node,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None):
		""" """
		super(Maya_Item_Data, self).__init__(tree_item,
		                                     selectable           = selectable          , enabled             = enabled            , editable     = editable,
		                                     dragable             = dragable            , dropable            = dropable           , checkable    = checkable,
		                                     tristate             = tristate            , font_family         = font_family        , font_size    = font_size,
		                                     size_hint            = size_hint           , status_tip          = status_tip         , tool_tip     = tool_tip,
		                                     brush                = brush               , icon_visable        = icon_visable       , icon_color   = icon_color,
		                                     font_weight          = font_weight         , font_capitalization = font_capitalization, display_name = display_name,
		                                     background_color     = background_color    , foreground_color    = foreground_color,
		                                     horizontal_alignment = horizontal_alignment, vertical_alignment  = vertical_alignment,
		                                     internal_data        = maya_node)
		isinstance(self.internal_data, Util_API.Maya_Node)
		self._py_node = pymel.core.PyNode(self.internal_data.name)
		isinstance(self._py_node, pymel.core.nodetypes.DependNode)
		if str(self.internal_data.objectType) in _Maya_Node_Type_Icons.keys():
			self.icon = QtGui.QPixmap(_Maya_Node_Type_Icons[str(self.internal_data.objectType)])
			self.icon_visable = True
		if self.internal_data.transfromType == "group" and self.internal_data.objectType == "transform":
			self.icon = QtGui.QPixmap(":/G/group")
			self.icon_visable = True
	#----------------------------------------------------------------------
	def data(self, role=ITEM_DATA_ROLE.DisplayRole):
		if role in [ITEM_DATA_ROLE.DisplayRole, ITEM_DATA_ROLE.EditRole]:
			if _Global_Options.display_show_name_spaces.value:
				return self.internal_data.name
			else:
				return self.internal_data.nice_name_wo_ns
			
		if role in [ITEM_DATA_ROLE.ForegroundRole]:
			active_selection = cmds.ls(sl=True, long=True)
			if self.internal_data.name in active_selection:
				return QtGui.QColor(Qt.green)
		
		if role == ITEM_DATA_ROLE.NameSpaceRole:
			return self._py_node.namespace()
		if role == ITEM_DATA_ROLE.FullNameRole:
			return self._py_node.longName()
		return super(Maya_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role in [ITEM_DATA_ROLE.EditRole]:
			if _Global_Options.display_show_name_spaces.value:
				self.internal_data.name = value
			else:
				self.internal_data.name = self.internal_data.namespace + ":" + value
		else:
			super(Maya_Item_Data, self).setData(role, value)
########################################################################
class Shader_Item_Data(Maya_Item_Data):
	#----------------------------------------------------------------------
	def __init__(self, maya_node,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None):
		""" """
		super(Shader_Item_Data, self).__init__(maya_node, tree_item=tree_item,
		                                     selectable           = selectable          , enabled             = enabled            , editable     = editable,
		                                     dragable             = dragable            , dropable            = dropable           , checkable    = checkable,
		                                     tristate             = tristate            , font_family         = font_family        , font_size    = font_size,
		                                     size_hint            = size_hint           , status_tip          = status_tip         , tool_tip     = tool_tip,
		                                     brush                = brush               , icon_visable        = icon_visable       , icon_color   = icon_color,
		                                     font_weight          = font_weight         , font_capitalization = font_capitalization, display_name = display_name,
		                                     background_color     = background_color    , foreground_color    = foreground_color,
		                                     horizontal_alignment = horizontal_alignment, vertical_alignment  = vertical_alignment)
		isinstance(self.internal_data, Util_API.Shading_Node)

	#----------------------------------------------------------------------
	def data(self, role=ITEM_DATA_ROLE.DisplayRole):
		return super(Shader_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		super(Shader_Item_Data, self).setData(role, value)
########################################################################
class Selection_Set_Item_Data(Maya_Item_Data):
	#----------------------------------------------------------------------
	def __init__(self, maya_node,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None):
		""" """
		super(Selection_Set_Item_Data, self).__init__(maya_node, tree_item=tree_item,
		                                       selectable           = selectable          , enabled             = enabled            , editable     = editable,
		                                       dragable             = dragable            , dropable            = dropable           , checkable    = checkable,
		                                       tristate             = tristate            , font_family         = font_family        , font_size    = font_size,
		                                       size_hint            = size_hint           , status_tip          = status_tip         , tool_tip     = tool_tip,
		                                       brush                = brush               , icon_visable        = icon_visable       , icon_color   = icon_color,
		                                       font_weight          = font_weight         , font_capitalization = font_capitalization, display_name = display_name,
		                                       background_color     = background_color    , foreground_color    = foreground_color,
		                                       horizontal_alignment = horizontal_alignment, vertical_alignment  = vertical_alignment)
		isinstance(self._py_node, pymel.core.nodetypes.ObjectSet)
		isinstance(self.internal_data, Util_API.SelectionSet)
		
	#----------------------------------------------------------------------
	def data(self, role=ITEM_DATA_ROLE.DisplayRole):
		# if role in [ITEM_DATA_ROLE.ForegroundRole]:
			# active_selection = cmds.ls(sl=True, long=True)
			# if not self.internal_data.name in active_selection:
				# for member_name in self.internal_data.memberNames:
					# if member_name in active_selection:
						# return QtGui.QColor(Qt.GlobalColor.darkGreen)
				# for child in self.internal_data.all_children:
					# if child.name in active_selection:
						# return QtGui.QColor(Qt.GlobalColor.darkGreen)
					# for member_name in child.memberNames:
						# if member_name in active_selection:
							# return QtGui.QColor(Qt.GlobalColor.darkGreen)
		return super(Selection_Set_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		super(Selection_Set_Item_Data, self).setData(role, value)
# ======================================================================
# DATA MODEL STANDERD ITEM CONTAINERS
# ----------------------------------------------------------------------
# Synopsis:
#     Like A StanderedItem 
# ======================================================================	
########################################################################
class Item_Data_List(object):
	#----------------------------------------------------------------------
	def __init__(self, tree_item):
		""" """
		if not isinstance(tree_item, Tree_Item):
			raise ValueError("tree_item input must be and instance or subclass of Tree_Item and a %r was found" % type(tree_item))
		self.tree_item = tree_item
		self.items     = []
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self.items:
			yield item
	#----------------------------------------------------------------------
	def data(self, column=0, role=ITEM_DATA_ROLE.DisplayRole):
		item = self.items[column]
		return item.data(role)
	#----------------------------------------------------------------------
	def setData(self, value, column=0, role=ITEM_DATA_ROLE.DisplayRole):
		item = self.items[column]
		item.setData(role, value)
	#----------------------------------------------------------------------
	def get_item(self, index):
		item = self.items[index]
		isinstance(item, Item_Data)
		return item
	#----------------------------------------------------------------------
	def get_Item_Flags(self, index):
		item = self.get_item(index)
		if item is None:
			res = QtCore.Qt.ItemFlag.NoItemFlags
		else:
			res = item.flags
		return res
########################################################################
class Tree_Item(object):
	_Item_Type_ID = _userType_counter()
	CHILDREN_CONTEXT, ITEMS_CONTEXT =  range(2)
	_Context_Attribute_Return = {CHILDREN_CONTEXT: "childItems", ITEMS_CONTEXT: "_column_items",}
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[], column_count=1):
		self._column_items       = Item_Data_List(self)
		self.childItems          = []
		self._with_Context_Depth = 0
		self._model              = model
		self._isVisable          = True
		
		
		#if not isinstance(parent_item, Tree_Item) and parent_item is not None:
			#raise ValueError("parent_item arg must be and instance or subclass of Tree_Item and a %r was found" % type(parent_item))
		self.parentItem    = parent_item
		isinstance(self.parentItem, Tree_Item)
					
		if len(items):
			for i, column_item in enumerate(items):
				if isinstance(column_item, dict ):
					column_item = Item_Data(self, **column_item)
				elif isinstance(column_item, Item_Data ):
					column_item.tree_item = self
				else:
					raise ValueError("index %i in child_items arg must be a instance of Tree_Item and a %r was found" % (i, type(child_item)) )
				self._column_items.items.append(column_item)
		else:
			column_items = []
			for i in range(column_count):
				item = Item_Data(self)
				item.display_name = "column %i" % i
				self._column_items.items.append(item)
		
		if self.parentItem is not None:
			self.parentItem.appendChild(self)
		if False:
			isinstance(self.model, TreeModel)
			isinstance(self.root_item, Tree_Item)
			isinstance(self.index, QtCore.QModelIndex)
			isinstance(self.parent, Tree_Item)
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self.context_data:
			yield item
	#----------------------------------------------------------------------
	def data(self, column=0, role=QtCore.Qt.DisplayRole):
		if role == ITEM_DATA_ROLE.Item_Type_Role:
			return self._Item_Type_ID
		else:
			return self._column_items.data(column, role)
	#----------------------------------------------------------------------
	def setData(self, value, column=0, role=QtCore.Qt.DisplayRole):
		self._column_items.setData(value, column,role)
	#----------------------------------------------------------------------
	def _is_parent_in_list(self, list_of_parents):
		""""""
		for parent_item in self.all_parents:
			if parent_item in list_of_parents:
				return parent_item
		return False
	#----------------------------------------------------------------------
	def contains_Child(self, child_item):
		ac = self.all_childern
		if child_item in ac:
			return child_item
		return False
	@property
	#----------------------------------------------------------------------
	def current_context_state(self):
		""""""
		return self._with_Context_Depth
	@property
	#----------------------------------------------------------------------
	def context_data(self):
		""""""
		if self.current_context_state in self._Context_Attribute_Return.keys():
			return getattr(self, self._Context_Attribute_Return[self.current_context_state])
		else:
			return self.childItems
	@property
	#----------------------------------------------------------------------
	def isRoot(self):
		""""""
		return self.root_item == self
	#----------------------------------------------------------------------
	def insertChildren(self, position, items):
		if not isinstance(items, list):
			return False
		if not len(items):
			return False
		
		if self.isRoot:
			parent_index = QtCore.QModelIndex()
		else:
			parent_index = self.index

		position = position if position > 0 else 0
		position = position if position <= self.child_Count else self.child_Count
		
		for item in items:
			self.model.beginInsertRows(parent_index, position, position - 1)
			self.childItems.insert(position, item)
			item.parentItem = self
			self.model.endInsertRows()
		return True
	#----------------------------------------------------------------------
	def insertChild(self, position, child_Item):
		isinstance(child_Item,Tree_Item)
		self.insertChildren(position, [child_Item])
	#----------------------------------------------------------------------
	def appendChild(self, child_Item):
		isinstance(child_Item,Tree_Item)
		self.insertChildren(self.child_Count, [child_Item])
	#----------------------------------------------------------------------
	def takeChildren(self, items):
		res = []
		if self.isRoot:
			parent_index = QtCore.QModelIndex()
			parentItem   = self
		else:
			parent_index = self.index
			parentItem   = self
		
		for item in items:
			position = item.row
			self.model.beginRemoveRows(parent_index, position, position+1)
			item = parentItem.childItems.pop(position)
			item.parentItem = None
			res.append(item)
			self.model.endRemoveRows()
		return res
	#----------------------------------------------------------------------
	def removeChildren(self, items):
		res = []
		if self.isRoot:
			parent_index = QtCore.QModelIndex()
			parentItem   = self
		else:
			parent_index = self.index
			parentItem   = self
		try:
			for item in items:
				if hasattr(item, "Unregister_Node_Callbacks"):
					item.Unregister_Node_Callbacks()
					item.clear_Children()
				position = item.row
				self.model.beginRemoveRows(parent_index, position, position+1)
				item = parentItem.childItems.pop(position)
				self.model.endRemoveRows()
				del item
			return True
		except:
			return False
	#----------------------------------------------------------------------
	def removeChild(self, child_item):
		return self.removeChildren([child_item])
	#----------------------------------------------------------------------
	def clear_Children(self):
		""""""
		return self.removeChildren(self.childItems)
	#----------------------------------------------------------------------
	def child(self, row):
		child_item = self.childItems[row]
		isinstance(child_item, Tree_Item)
		return child_item
	#----------------------------------------------------------------------
	def update(self):
		return self.root_item.model.dataChanged.emit(self.index, self.index)
	#----------------------------------------------------------------------
	def update_Children(self):
		for child in self.childItems:
			child.update()
	#----------------------------------------------------------------------
	def update_All_Children(self):
		for child in self.all_childern:
			child.update()
	#----------------------------------------------------------------------
	@property
	def parent(self):
		return self.parentItem
	#----------------------------------------------------------------------
	@property
	def all_parents(self):
		res = []
		if self.isRoot:
			return res

		item = self
		while not item.isRoot:
			item = item.parentItem
			res.append(item)
		return res
	#----------------------------------------------------------------------
	@property
	def all_childern(self):
		def scan_childern(parent, item_list=[]):
			if parent.child_Count:
				item_list.extend(parent.childItems)
				for child in parent.childItems:
					scan_childern(child, item_list)
			return item_list
		res = []
		if not self.child_Count:
			return res
		res = scan_childern(self)
		return res
	#----------------------------------------------------------------------
	@property
	def row(self):
		if self.parentItem:
			return self.parentItem.childItems.index(self)
		return 0
	#----------------------------------------------------------------------
	@property
	def column_Count(self):
		return len(self._column_items.items)
	#----------------------------------------------------------------------
	@property
	def root_item(self):
		item = self
		while item.parentItem is not None:
			item = item.parentItem
		return item
	#----------------------------------------------------------------------
	@property
	def model(self):
		return self.root_item._model
	#----------------------------------------------------------------------
	@property
	def index(self):
		""""""
		return self.model.indexFromItem(self)
	#----------------------------------------------------------------------
	@property
	def child_Count(self):
		return len(self.childItems)
	#----------------------------------------------------------------------
	def find_child(self, value, column=0, role=ITEM_DATA_ROLE.DisplayRole):
		res = None
		for child in self.all_childern:
			if child.data(column, role) == value:
				res = child
				break
		isinstance(res, Tree_Item)
		return res
	#----------------------------------------------------------------------
	def find_childern(self, value, column=0, role=ITEM_DATA_ROLE.DisplayRole):
		res = []
		for child in self.all_childern:
			if child.data(column, role) == value:
				res.append(child)
		return res
	#----------------------------------------------------------------------
	def flags(self, column=0):
		return self._column_items.get_Item_Flags(column)
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = self.data(column=column, role=ITEM_DATA_ROLE.Internal_Data_Role)
		isinstance(res, Item_Data)
		return res
	#----------------------------------------------------------------------
	def set_internal_Data(self, value, column=0):
		""""""
		self.setData(value, column=column, role=ITEM_DATA_ROLE.Internal_Data_Role)
########################################################################
class Maya_Node_Tree_Item(Tree_Item):
	_Item_Type_ID = _userType_counter()
	logger = make_logger("Maya Node Tree Items", logging.INFO)
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[], column_count=1):
		
		Tree_Item.__init__(self, model, parent_item, items, column_count)
		self._maya_callback_pointers = []
		self.Register_Node_Callbacks()
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = self.data(column=column, role=ITEM_DATA_ROLE.Internal_Data_Role)
		isinstance(res, Util_API.Maya_Node)
		isinstance(res, Util_API.SelectionSet)
		return res
	#----------------------------------------------------------------------
	def Register_Node_Callbacks(self):
		'''
		Add the Maya node callbacks
		and register them with the widget (so they can be cleaned up).
		'''
		internal_data = self.get_internal_Data()
		self.logger.debug("Adding Name Changed Callback For %r" % internal_data.nice_name)
		# Name changed callback
		cb = CB_Builders.create_Name_Changed_Callback(internal_data._MObject, self.update_Name_Changed_CB, None)
		self._maya_callback_pointers.append(cb)
	#----------------------------------------------------------------------	
	def Unregister_Node_Callbacks(self):
		'''Remove per-node Maya callbacks. For The input Maya_Node_Tree_Item'''
		internal_data = self.get_internal_Data()
		self.logger.debug('removing Callbacks For Node %r' % internal_data.nice_name)
		self._maya_callback_pointers = []
	#----------------------------------------------------------------------
	def update_Name_Changed_CB(self, newName, previousName, tree_item):
		isinstance(tree_item, Maya_Node_Tree_Item)
		internal_data = self.get_internal_Data()
		self.logger.debug("Updating A Name Change From %r to %r" % (previousName, internal_data.nice_name))
		# self.model.dataChanged.emit(self._column_items.get_item(0).index, self._column_items.get_item(0).index)
		# if hasattr(tree_item, "update"):
			# tree_item.update()
########################################################################
class Selection_Set_Tree_Item(Maya_Node_Tree_Item):
	_Item_Type_ID = _userType_counter()
	logger = make_logger("Selection Set Tree Item", logging.INFO)
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[], column_count=1):
		super(Selection_Set_Tree_Item, self).__init__(model, parent_item, items, column_count)
		self.get_internal_Data().lockNode()
	#----------------------------------------------------------------------
	def Register_Node_Callbacks(self):
		'''
		Add the Maya per-node callbacks for the specified item
		and register them with the widget (so they can be cleaned up).
		'''
		super(Selection_Set_Tree_Item, self).Register_Node_Callbacks()
		internal_data = self.get_internal_Data()
		self.logger.debug("Adding Attribute Changed Callback For %r" % internal_data.nice_name)
		# Member Assinments Changed Callback
		cb = CB_Builders.create_Attribute_Changed_Callback(internal_data._MObject, self.Update_Connections_Changed_Callback, None)
		self._maya_callback_pointers.append(cb)
	#----------------------------------------------------------------------
	def Update_Connections_Changed_Callback(self, msg, plg, other, client):
		if Node_Msg_Flags.OtherPlugSet & msg:
			if plg.isElement():
				name = plg.name().split(".")[-1]
				M_plg  = Util_API.MPLUG(plg)
				O_plg  = Util_API.MPLUG(other)
				M_node = M_plg.node
				O_node = O_plg.node
				if name.startswith("dagSetMembers"):
					
					if str(M_plg) in [str(p) for p in O_plg.output_Plugs]:
						self.logger.debug('%r Dag Node Was Added To %r' % (O_node.nice_name, M_node.nice_name))
						item_data     = Maya_Item_Data(O_node)
						tree_item     = Maya_Node_Tree_Item(model=None, parent_item=self, items=[item_data])
					else:
						self.logger.debug('%r Dag Node Was Removed From %r' % (O_node.nice_name, M_node.nice_name))
						child_item = self.find_child(O_node.nice_name)
						if not child_item is None:
							self.removeChild(child_item)

				elif name.startswith("dnSetMembers"):
					O_node = Util_API.SelectionSet(O_node.name, text="bookmarkModelView")
					if str(M_plg) in [str(p) for p in O_plg.output_Plugs]:
						self.logger.debug('%r Dependency Node Was Add To %r' % (O_node.nice_name, M_node.nice_name))
						item_data     = Selection_Set_Item_Data(O_node)
						tree_item     = Selection_Set_Tree_Item(model=None, parent_item=self, items=[item_data])
						tree_item.repopulate()
					else:
						self.logger.debug('%r Dependency Node Was Removed From %r' % (O_node.nice_name, M_node.nice_name))
						child_item = self.find_child(O_node.nice_name)
						self.logger.debug('Removed Node')
						self.removeChild(child_item)
	#----------------------------------------------------------------------
	def repopulate(self):
		'''Clear and populate the table with data retrieved from the Maya scene.
		Add Maya callbacks for creaseSet changes to trigger UI updates.
		'''
		# Remove existing per-set callbacks
		# MCallbackWrapper objects auto-remove themselves.
		# See also self.removePerNodeMayaCallbacks()
		self.logger.debug("repopulating Selection Set %r" % self.data())
		# Clear items in QTreeWidget
		self.clear_Children()
		object_set = self.get_internal_Data()
		for child in object_set.children:
			isinstance(child, Util_API.SelectionSet)
			item_data     = Selection_Set_Item_Data(child)
			tree_item     = Selection_Set_Tree_Item(model=None, parent_item=self, items=[item_data])
			tree_item.repopulate()
		for member in object_set.members:
			isinstance(member, Util_API.Maya_Node)
			member_data      = Maya_Item_Data(member)
			member_tree_item = Maya_Node_Tree_Item(model=None, parent_item=self, items=[member_data])
	#----------------------------------------------------------------------
	def node_addElement(self, *items):
		""""""
		self.get_internal_Data().addElement(*items)
# ======================================================================
# DATA MODEL ROOT TREE ITEM
# ----------------------------------------------------------------------
# Synopsis:
#     This Is Special It Needs To Be The Root Of Any Data Model
#     Because All Elements Use It To Find Themself Within There Tree
# ======================================================================
########################################################################
class Root_Tree_Item(Tree_Item):
	_Item_Type_ID = _userType_counter()
	#----------------------------------------------------------------------
	def __init__(self, model, header_names=["Name"]):
		items = []
		for header in header_names:
			item = Item_Data( self, display_name=header )
			item.icon_visable = False
			items.append(item)
		super(Root_Tree_Item, self).__init__(model=model, items=items)
########################################################################
class Tree_View(QtGui.QTreeView):
	UPDATE_SELECTION = QtSignal()
	ACTIVE_SELECTION_CHANGED = QtSignal(*(QtCore.QModelIndex, ))
	SELECTION_CHANGED        = QtSignal(QtGui.QItemSelection, QtGui.QItemSelection)
	CURRENT_CHANGED          = QtSignal(QtCore.QModelIndex, QtCore.QModelIndex)
	# ======================================
	# Function Overloaders
	# ======================================
	#----------------------------------------------------------------------
	def selectionChanged(self,selected,deselected):
		"""
		selectionChanged(selected,deselected)
			selected=QtGui.QItemSelection
			deselected=QtGui.QItemSelection

		This slot is called when the selection is changed
		The previous selection (which may be empty), is specified by deselected , and the new selection by selected.
		"""
		isinstance(selected, QT.QtGui.QItemSelection)
		isinstance(deselected, QT.QtGui.QItemSelection)
		QtGui.QTreeView.selectionChanged(self, selected, deselected)
		self.UPDATE_SELECTION.emit()
		self.SELECTION_CHANGED.emit(selected, deselected)
		if selected.count() >= 1:
			first_index = selected.indexes()[0]
			self.ACTIVE_SELECTION_CHANGED.emit(first_index)
	#----------------------------------------------------------------------
	def currentChanged(self,current,previous):
		"""
		currentChanged(current,previous)
			current=QtCore.QModelIndex
			previous=QtCore.QModelIndex

		This slot is called when a new item becomes the current item
		The previous current item is specified by the previous index, and the new item by the current index.
		If you want to know about changes to items see the PySide.QtGui.QAbstractItemView.dataChanged() signal.
		"""
		res = super(Tree_View,self).currentChanged(current,previous)
		return res
	#----------------------------------------------------------------------
	def dragEnterEvent(self,event):
		"""
		dragEnterEvent(event)
			event=QtGui.QDragEnterEvent

		This event handler is called when a drag is in progress and the mouse enters this widget
		The event is passed in the event parameter.
		If the event is ignored, the widget wont receive any drag move events .
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Tree_View,self).dragEnterEvent(event)
		# event.setAccepted(True)
		# event.setDropAction(Qt.DropAction.CopyAction)
		event.acceptProposedAction()
		return res
	#----------------------------------------------------------------------
	def dragLeaveEvent(self,event):
		"""
		dragLeaveEvent(event)
			event=QtGui.QDragLeaveEvent

		This event handler is called when a drag is in progress and the mouse leaves this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Tree_View,self).dragLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragMoveEvent(self,event):
		"""
		dragMoveEvent(event)
			event=QtGui.QDragMoveEvent

		This event handler is called if a drag is in progress, and when any of the following conditions occur: the cursor enters this widget, the cursor moves within this widget, or a modifier key is pressed on the keyboard while this widget has the focus
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		isinstance(event, QtGui.QDropEvent)
		res = super(Tree_View,self).dragMoveEvent(event)
		data = event.mimeData()
		if isinstance(data, MimeData):
			data.set_Dest_Item(self, event)
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		"""
		dropEvent(event)
			event=QtGui.QDropEvent

		This event handler is called when the drag is dropped on this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(Tree_View,self).dropEvent(event)
		data = event.mimeData()
		if isinstance(data, MimeData):
			data.set_Dest_Item(self, event)
			data.on_drop_event_Move_Items()
		event.setDropAction(Qt.DropAction.IgnoreAction)
	#----------------------------------------------------------------------
	def mouseDoubleClickEvent(self,event):
		"""
		mouseDoubleClickEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse double click events for the widget.
		The default implementation generates a normal mouse press event.
		"""
		res = super(Tree_View,self).mouseDoubleClickEvent(event)
	#----------------------------------------------------------------------
	def mouseMoveEvent(self,event):
		"""
		mouseMoveEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse move events for the widget.
		If mouse tracking is switched off, mouse move events only occur if a mouse button is pressed while the mouse is being moved
		If mouse tracking is switched on, mouse move events occur even if no mouse button is pressed.
		QMouseEvent.pos() reports the position of the mouse cursor, relative to this widget
		For press and release events, the position is usually the same as the position of the last mouse move event, but it might be different if the users hand shakes
		This is a feature of the underlying window system, not Qt.
		If you want to show a tooltip immediately, while the mouse is moving (e.g., to get the mouse coordinates with QMouseEvent.pos() and show them as a tooltip), you must first enable mouse tracking as described above
		Then, to ensure that the tooltip is updated immediately, you must call QToolTip.showText() instead of PySide.QtGui.QWidget.setToolTip() in your implementation of PySide.QtGui.QWidget.mouseMoveEvent() .
		"""
		res = super(Tree_View,self).mouseMoveEvent(event)
	#----------------------------------------------------------------------
	def mouseReleaseEvent(self,event):
		"""
		mouseReleaseEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse release events for the widget.
		"""
		res = super(Tree_View,self).mouseReleaseEvent(event)
	# ======================================
	# Custom Helper Function
	# ======================================
	#----------------------------------------------------------------------
	@QtSlot(QtCore.QModelIndex)
	def _do_Full_Expand(self, index):
		""""""
		if QtGui.QApplication.keyboardModifiers() == Qt.KeyboardModifier.ShiftModifier:
			item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
			if not item is None:
				for child in item.all_childern:
					if child._Item_Type_ID == Selection_Set_Tree_Item._Item_Type_ID:
						self.expand(self.remap_Index_From_Source(child.index))
	#----------------------------------------------------------------------
	@QtSlot(QtCore.QModelIndex)
	def _do_Full_Collapse(self, index):
		""""""
		if QtGui.QApplication.keyboardModifiers() == Qt.KeyboardModifier.ShiftModifier:
			item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
			for child in reversed(item.all_childern):
				if child._Item_Type_ID == Selection_Set_Tree_Item._Item_Type_ID:
					self.collapse(self.remap_Index_From_Source(child.index))
	#----------------------------------------------------------------------
	def iter_selectedIndexes_By_ID(self, idNum):
		""""""
		for index in self.selectedIndexes():
			if index.data(ITEM_DATA_ROLE.Item_Type_Role) == idNum:
				yield index
	#----------------------------------------------------------------------
	def selectedIndexes_By_ID(self, idNum):
		""""""
		res = []
		for index in self.selectedIndexes():
			if index.data(ITEM_DATA_ROLE.Item_Type_Role) == idNum:
				res.append(index)
		return res
	#----------------------------------------------------------------------
	def selected_Selection_Set_Indexes(self):
		""""""
		return [index for index in self.selectedIndexes() if index.data(ITEM_DATA_ROLE.Item_Type_Role) == Selection_Set_Tree_Item._Item_Type_ID]
	#----------------------------------------------------------------------
	def get_expanded_items(self):
		""""""
		def scanner(root,res=[]):
			index = self.remap_Index_From_Source(root.index)
			if self.isExpanded(index):
				res.append(root)
				for child in root.childItems: 
					scanner(child,res)
			return res
		
		root_index = self.rootIndex()
		if not root_index.isValid():
			root_index = self.model().sourceModel().rootItem.index
		root_item = root_index.data(ITEM_DATA_ROLE.Tree_Item_Role)
		expaded_items = []
		for child in root_item.childItems: 
			scanner(child,expaded_items)
		
		res = [item.data(0, ITEM_DATA_ROLE.FullNameRole) for item in expaded_items]
		return res
	#----------------------------------------------------------------------
	def set_expand_item_by_name(self, items):
		""""""
		view_model = self.model()
		root_index = self.rootIndex()
		if not root_index.isValid():
			root_index = self.model().sourceModel().rootItem.index
		root_item = root_index.data(ITEM_DATA_ROLE.Tree_Item_Role)
		long_name = root_item.data(0, ITEM_DATA_ROLE.FullNameRole)
		if long_name in items:
			self.expand(self.remap_Index_From_Source(root_item.index))
		for child in root_item.all_childern:
			long_name = child.data(0, ITEM_DATA_ROLE.FullNameRole)
			if long_name in items:
				index = self.remap_Index_From_Source(child.index)
				self.expand(index)
	# ======================================
	# Slots That Interact With Maya
	# ======================================
	#----------------------------------------------------------------------
	@QtSlot()
	def unlock_Highlighted_Sets(self):
		""""""
		selected_indices = self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			with Util_API.MayaUndoChunk():
				cmds.lockNode(set_nodes, lock=False)
	#----------------------------------------------------------------------
	@QtSlot()
	def lock_Highlighted_Sets(self):
		""""""
		selected_indices = self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			with Util_API.MayaUndoChunk():
				cmds.lockNode(set_nodes, lock=True)
	#----------------------------------------------------------------------
	@QtSlot()
	def select_Highlighted_Sets(self):
		""""""
		selected_indices = self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			with Util_API.MayaUndoChunk():
				cmds.select(set_nodes, noExpand=True)
	#----------------------------------------------------------------------
	@QtSlot()
	def select_Highlighted_Set_Members(self):
		""""""
		selected_indices = self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			all_members = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				all_members.extend(item_set.members)
			if len(all_members):
				cmds.select(item_set.members)
	#----------------------------------------------------------------------
	@QtSlot()
	def select_Hilighted_Child_Sets(self):
		""""""
		selected_indices = self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			with Util_API.MayaUndoChunk():
				cmds.select(clear=True)
				for index in selected_indices:
					item_set  = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
					cmds.select(item_set.children, noExpand=True, add=True)
	#----------------------------------------------------------------------
	@QtSlot()
	def frame_Highlighted_Contents(self):
		""""""
		selected_indices = self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			with ActiveSelectionRestore():
				cmds.select(set_nodes)
				cmds.viewFit()
	#----------------------------------------------------------------------
	@QtSlot()
	def frame_Highlighted_Items(self):
		""""""
		selected_indices = [index for index in self.selectedIndexes() if index.data(ITEM_DATA_ROLE.Item_Type_Role) >= Maya_Node_Tree_Item._Item_Type_ID]
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			with ActiveSelectionRestore():
				cmds.select(set_nodes)
				cmds.viewFit()
	#----------------------------------------------------------------------
	@QtSlot(QtCore.QModelIndex)
	def frame_Input_Index(self, index):
		""""""
		item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
		if item._Item_Type_ID in [Maya_Node_Tree_Item._Item_Type_ID, Selection_Set_Tree_Item._Item_Type_ID]:
			maya_item = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
			with ActiveSelectionRestore():
				cmds.select(maya_item)
				if len(cmds.ls(sl=True)):
					cmds.viewFit(animate=True)
	#----------------------------------------------------------------------
	@QtSlot(QtCore.QModelIndex)
	def select_Input_Index(self, index):
		""""""
		item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
		if item._Item_Type_ID in [Maya_Node_Tree_Item._Item_Type_ID, Selection_Set_Tree_Item._Item_Type_ID]:
			maya_item = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
			cmds.select(maya_item)
	#----------------------------------------------------------------------
	def maya_style_setSelection(self, index):
		""""""
		item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
		if item._Item_Type_ID  == Maya_Node_Tree_Item._Item_Type_ID:
			rect = self.visualRect(index)
			self.setSelection(rect, QtGui.QItemSelectionModel.SelectionFlag.ClearAndSelect)
		else:
			cleared = False
			recolaps_indices = []
			for child in item.all_childern:
				child_index = self.remap_Index_From_Source(child.index)
				if child._Item_Type_ID == Maya_Node_Tree_Item._Item_Type_ID:
					rect = self.visualRect(child_index)
					if not cleared:
						self.setSelection(rect, QtGui.QItemSelectionModel.SelectionFlag.ClearAndSelect)
						cleared = True
					else:
						self.setSelection(rect, QtGui.QItemSelectionModel.SelectionFlag.Select)
				elif child._Item_Type_ID == Selection_Set_Tree_Item._Item_Type_ID:
					if not self.isExpanded(child_index):
						recolaps_indices.append(child_index)
					self.expand(child_index)
			for child_index in recolaps_indices:
				self.collapse(child_index)
	#----------------------------------------------------------------------
	@QtSlot()
	def reveal_Highlighted_In_Outliner(self):
		""""""
		if cmds.outlinerEditor("outlinerPanel1",query=True, exists=True):
			selected_indices = [index for index in self.selectedIndexes() if index.data(ITEM_DATA_ROLE.Item_Type_Role) >= Maya_Node_Tree_Item._Item_Type_ID]
			if len(selected_indices):
				set_nodes = []
				for index in selected_indices:
					item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
					set_nodes.append(item_set)
				with ActiveSelectionRestore():
					cmds.select(set_nodes)
					cmds.outlinerEditor("outlinerPanel1",edit=True, showSelected=True)
	#----------------------------------------------------------------------
	@QtSlot()
	def select_Highlighted_Contents(self):
		""""""
		selected_indices = [index for index in self.selectedIndexes() if index.data(ITEM_DATA_ROLE.Item_Type_Role) >= Maya_Node_Tree_Item._Item_Type_ID]
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			cmds.select(set_nodes, noExpand=True)
	#----------------------------------------------------------------------
	@QtSlot()
	def select_Highlighted_Hierarchy(self):
		""""""
		selected_indices = [index for index in self.selectedIndexes() if index.data(ITEM_DATA_ROLE.Item_Type_Role) >= Maya_Node_Tree_Item._Item_Type_ID]
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			cmds.select(set_nodes)
	#----------------------------------------------------------------------
	@QtSlot()
	def remove_Selected_From_Sets(self):
		""""""
		selected_indices =  self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			with Util_API.MayaUndoChunk():
				for index in selected_indices:
					item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
					item_set.remove(cmds.ls(sl=True, long=True))
	#----------------------------------------------------------------------
	@QtSlot()
	def remove_Hilighted_From_Parents(self):
		""""""
		selected_node_indices = self.selectedIndexes_By_ID(Maya_Node_Tree_Item._Item_Type_ID)
		selected_set_indices = self.selectedIndexes_By_ID(Selection_Set_Tree_Item._Item_Type_ID)
		if len(selected_node_indices):
			for index in selected_node_indices:
				tree_item   = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
				item_set    = tree_item.get_internal_Data()
				parent_item = tree_item.parent
				parent_set  = parent_item.get_internal_Data()
				parent_set.remove([item_set])
		
		if len(selected_set_indices):
			for index in selected_set_indices:
				tree_item   = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
				parent_item = tree_item.parent
				item_set    = tree_item.get_internal_Data()
				parent_set  = parent_item.get_internal_Data()
				if len(item_set.parents) > 1 or ( len(item_set.members) > 0 and len(item_set.children) > 0):
					parent_set.remove([item_set])
	#----------------------------------------------------------------------
	@QtSlot()
	def add_Hilighted_To_Highlighted(self):
		""""""
		selected_node_indices = self.selectedIndexes_By_ID(Maya_Node_Tree_Item._Item_Type_ID)
		selected_set_indices = self.selectedIndexes_By_ID(Selection_Set_Tree_Item._Item_Type_ID)
		with Util_API.MayaUndoChunk():
			if len(selected_node_indices) and len(selected_set_indices):
				for node_index in selected_node_indices:
					node_tree_item = node_index.data(ITEM_DATA_ROLE.Tree_Item_Role)
					node_item  = node_tree_item.get_internal_Data()
					for set_index in selected_set_indices:
						set_tree_item = set_index.data(ITEM_DATA_ROLE.Tree_Item_Role)
						set_item  = set_tree_item.get_internal_Data()
						if not node_item in set_item:
							set_item.addElement(node_item)
			
			if len(selected_set_indices):
				last_set_index = selected_set_indices.pop(-1)
				last_set_tree_item = last_set_index.data(ITEM_DATA_ROLE.Tree_Item_Role)
				last_set_item = last_set_tree_item.get_internal_Data()
				for set_index in selected_set_indices:
					set_tree_item     = set_index.data(ITEM_DATA_ROLE.Tree_Item_Role)
					set_item          = set_tree_item.get_internal_Data()
					if not set_item.name in [v.name for v in last_set_item.children] and not last_set_item.name in [v.name for v in set_item.children]:
						last_set_item.addElement([set_item])
	#----------------------------------------------------------------------
	@QtSlot()
	def add_Selected_To_Sets(self):
		""""""
		selected_indices =  self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			with Util_API.MayaUndoChunk():
				for index in selected_indices:
					item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
					item_set.addElement(cmds.ls(sl=True, long=True))
	#----------------------------------------------------------------------
	@QtSlot()
	def lock_Hilighted_Sets(self):
		""""""
		selected_indices =  self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			selected_nodes = [index.data(ITEM_DATA_ROLE.Tree_Item_Role).get_internal_Data() for index in selected_indices]
			with Util_API.MayaUndoChunk():
				cmds.lockNode(selected_nodes, lock=True)
	#----------------------------------------------------------------------
	@QtSlot()
	def unlock_Hilighted_Sets(self):
		""""""
		selected_indices =  self.selected_Selection_Set_Indexes()
		if len(selected_indices):
			selected_nodes = [index.data(ITEM_DATA_ROLE.Tree_Item_Role).get_internal_Data() for index in selected_indices]
			with Util_API.MayaUndoChunk():
				cmds.lockNode(selected_nodes, lock=False)
	#----------------------------------------------------------------------
	@QtSlot()
	def move_Hilighted_Up(self):
		""""""
		selected_node_indices = self.selectedIndexes()
		if len(selected_node_indices):
			same_parents = dict()
			for index in selected_node_indices:
				tree_item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
				current_parent = tree_item.parent
				if not current_parent in same_parents.keys():
					same_parents[current_parent] = []
				same_parents[current_parent].append(tree_item)
			for parent in same_parents.keys():
				items = same_parents[parent]
				first_row = min([i.row for i in items])
				if not first_row == 0:
					items.reverse()
					parent.takeChildren(items)
					parent.insertChildren(first_row-1, items)
	#----------------------------------------------------------------------
	@QtSlot()
	def move_Hilighted_Down(self):
		""""""
		selected_node_indices = self.selectedIndexes()
		if len(selected_node_indices):
			same_parents = dict()
			for index in selected_node_indices:
				tree_item = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
				current_parent = tree_item.parent
				if not current_parent in same_parents.keys():
					same_parents[current_parent] = []
				same_parents[current_parent].append(tree_item)
			for parent in same_parents.keys():
				items = same_parents[parent]
				last_row = max([i.row for i in items])
				if not parent.child_Count == last_row + 1:
					items.reverse()
					parent.takeChildren(items)
					parent.insertChildren(last_row+1, items)
	#----------------------------------------------------------------------
	@QtSlot(bool)
	def set_Isolate_State(self, value):
		""""""
		selected_indices = [index for index in self.selectedIndexes() if index.data(ITEM_DATA_ROLE.Item_Type_Role) >= Maya_Node_Tree_Item._Item_Type_ID]
		if len(selected_indices):
			set_nodes = []
			for index in selected_indices:
				item_set = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				set_nodes.append(item_set)
			cmds.select(set_nodes)
	#----------------------------------------------------------------------
	def remap_Index_To_Source(self, index):
		""""""
		view_model = self.model()
		if isinstance(view_model, QtGui.QSortFilterProxyModel):
			index = view_model.mapToSource(index)
		return index
	#----------------------------------------------------------------------
	def remap_Index_From_Source(self, index):
		""""""
		view_model = self.model()
		if isinstance(view_model, QtGui.QSortFilterProxyModel):
			index = view_model.mapFromSource(index)
		return index
########################################################################
class Selection_Set_Tree_View(Tree_View):
	#----------------------------------------------------------------------
	def _run_setup(self, main_window):
		self._main_window = main_window
		self.expanded.connect(self._do_Full_Expand)
		self.collapsed.connect(self._do_Full_Collapse)
		# self.expanded.connect(self._add_Expaded)
		# self.collapsed.connect(self._remove_Expaded)
		isinstance(self._main_window, AW_Selection_Set_Editor)
		self._Create_Context_Menus()
		self._Isolate_Contents_State = False
		self._skip_expanded_indices_scan = False
		self.expaded_indices = []
	#----------------------------------------------------------------------
	@QtSlot(QtCore.QModelIndex)
	def _add_Expaded(self, index):
		""""""
		if not self._skip_expanded_indices_scan:
			self.expaded_indices.append(index)
	#----------------------------------------------------------------------
	@QtSlot(QtCore.QModelIndex)
	def _remove_Expaded(self, index):
		""""""
		if not self._skip_expanded_indices_scan:
			if index in self.expaded_indices:
				self.expaded_indices.remove(index)
	#----------------------------------------------------------------------
	def restore_expaded(self):
		""""""
		for index in self.expaded_indices:
			self.expand(index)
	#----------------------------------------------------------------------
	def _Create_Context_Menus(self):
		""""""
		self._context_menu   = QtGui.QMenu(self)
		# Options_Menu         = self.selection_set_view_set_item_context_menu.addMenu("Options")
		# Display_Options_Menu = Options_Menu.addMenu("Display")
		placement_menu       = self._context_menu.addMenu("Placement")
		node_locking_menu    = self._context_menu.addMenu("Locking")
		selection_Menu       = self._context_menu.addMenu("Selecting")
		Assinments_Menu      = self._context_menu.addMenu("Assinments")
		Viewport_Menu        = self._context_menu.addMenu("Viewport")
		
		## Color ConText Menus
		placement_menu.addAction(self._main_window.action_Move_Highlighted_Up)
		placement_menu.addAction(self._main_window.action_Move_Highlighted_Down)
		
		node_locking_menu.addAction(self._main_window.action_Lock_Highlighted_Sets)
		node_locking_menu.addAction(self._main_window.action_Unlock_Highlighted_Sets)
		
		selection_Menu.addAction(self._main_window.action_Select_Highlighted_Sets)
		selection_Menu.addAction(self._main_window.action_Select_Highlighted_Child_Sets)
		selection_Menu.addAction(self._main_window.action_Select_Highlighted_Set_Members)
		selection_Menu.addAction(self._main_window.action_Select_Highlighted_Set_Member_Recursively)

		Assinments_Menu.addAction(self._main_window.action_Add_Selection_To_Highlighted_Sets)
		Assinments_Menu.addAction(self._main_window.action_Remove_Selection_From_Highlighted_Sets)
		Assinments_Menu.addSeparator()
		Assinments_Menu.addAction(self._main_window.action_Add_Highlighted_Nodes_To_Highlighted_Set)
		Assinments_Menu.addAction(self._main_window.action_Remove_Highlighted_From_Parent_Sets)

		Viewport_Menu.addAction(self._main_window.action_Frame_Highlighted_Set_Members)
		Viewport_Menu.addAction(self._main_window.action_Frame_Highlighted)
		Viewport_Menu.addAction(self._main_window.action_Reveal_Highlighted_Outliner_Panel)
	# ======================================
	# Function Overloaders
	# ======================================
	#----------------------------------------------------------------------
	def contextMenuEvent(self, event):
		mods     = event.modifiers()
		key_mods = Qt.KeyboardModifier
		if mods == key_mods.NoModifier:
			if not self._context_menu is None:
				self._context_menu.exec_(event.globalPos())
	#----------------------------------------------------------------------
	def mousePressEvent(self,event):
		"""
		mousePressEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse press events for the widget.
		If you create new widgets in the PySide.QtGui.QWidget.mousePressEvent() the PySide.QtGui.QWidget.mouseReleaseEvent() may not end up where you expect, depending on the underlying window system (or X11 window manager), the widgets location and maybe more.
		The default implementation implements the closing of popup widgets when you click outside the window
		For other widget types it does nothing.
		"""
		mods     = event.modifiers()
		button   = event.button()
		key_mods = Qt.KeyboardModifier
		buttons  = Qt.MouseButton
		if mods == key_mods.AltModifier or mods == key_mods.AltModifier | key_mods.ShiftModifier:
			index = self.indexAt(event.pos())
			if index.isValid():
				if button == buttons.RightButton:
					self.frame_Input_Index(index)
					if mods == key_mods.AltModifier | key_mods.ShiftModifier:
						self.select_Input_Index(index)
						self.maya_style_setSelection(index)
				elif button == buttons.LeftButton:
					self.select_Input_Index(index)
					if mods == key_mods.AltModifier | key_mods.ShiftModifier:
						self.maya_style_setSelection(index)
		else:
			res = super(Selection_Set_Tree_View,self).mousePressEvent(event)

########################################################################
class List_View(QtGui.QListView):
	UPDATE_SELECTION = QtSignal()
	ACTIVE_SELECTION_CHANGED = QtSignal(*(QtCore.QModelIndex, ))
	SELECTION_CHANGED        = QtSignal(QtGui.QItemSelection, QtGui.QItemSelection)
	CURRENT_CHANGED          = QtSignal(QtCore.QModelIndex, QtCore.QModelIndex)
	def __init__(self, parent=None):
		super(List_View, self).__init__(parent)
	#----------------------------------------------------------------------
	def dragEnterEvent(self,event):
		"""
		dragEnterEvent(event)
			event=QtGui.QDragEnterEvent

		This event handler is called when a drag is in progress and the mouse enters this widget
		The event is passed in the event parameter.
		If the event is ignored, the widget wont receive any drag move events .
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(List_View,self).dragEnterEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragLeaveEvent(self,event):
		"""
		dragLeaveEvent(event)
			event=QtGui.QDragLeaveEvent

		This event handler is called when a drag is in progress and the mouse leaves this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(List_View,self).dragLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragMoveEvent(self,event):
		"""
		dragMoveEvent(event)
			event=QtGui.QDragMoveEvent

		This event handler is called if a drag is in progress, and when any of the following conditions occur: the cursor enters this widget, the cursor moves within this widget, or a modifier key is pressed on the keyboard while this widget has the focus
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(List_View,self).dragMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		"""
		dropEvent(event)
			event=QtGui.QDropEvent

		This event handler is called when the drag is dropped on this widget
		The event is passed in the event parameter.
		See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.
		"""
		res = super(List_View,self).dropEvent(event)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self,selected,deselected):
		"""
		selectionChanged(selected,deselected)
			selected=QtGui.QItemSelection
			deselected=QtGui.QItemSelection

		This slot is called when the selection is changed
		The previous selection (which may be empty), is specified by deselected , and the new selection by selected.
		"""
		isinstance(selected, QT.QtGui.QItemSelection)
		isinstance(deselected, QT.QtGui.QItemSelection)
		QtGui.QListView.selectionChanged(self, selected, deselected)
		self.UPDATE_SELECTION.emit()
		self.SELECTION_CHANGED.emit(selected, deselected)
		if selected.count() >= 1:
			first_index = selected.indexes()[0]
			self.ACTIVE_SELECTION_CHANGED.emit(first_index)
	#----------------------------------------------------------------------
	def currentChanged(self,current,previous):
		"""
		currentChanged(current,previous)
			current=QtCore.QModelIndex
			previous=QtCore.QModelIndex

		This slot is called when a new item becomes the current item
		The previous current item is specified by the previous index, and the new item by the current index.
		If you want to know about changes to items see the PySide.QtGui.QAbstractItemView.dataChanged() signal.
		"""
		QtGui.QListView.currentChanged(self, current,previous)
		self.CURRENT_CHANGED.emit(current,previous)
	#----------------------------------------------------------------------
	def mouseDoubleClickEvent(self,event):
		"""
		mouseDoubleClickEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse double click events for the widget.
		The default implementation generates a normal mouse press event.
		"""
		res = super(List_View,self).mouseDoubleClickEvent(event)
	#----------------------------------------------------------------------
	def mouseMoveEvent(self,event):
		"""
		mouseMoveEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse move events for the widget.
		If mouse tracking is switched off, mouse move events only occur if a mouse button is pressed while the mouse is being moved
		If mouse tracking is switched on, mouse move events occur even if no mouse button is pressed.
		QMouseEvent.pos() reports the position of the mouse cursor, relative to this widget
		For press and release events, the position is usually the same as the position of the last mouse move event, but it might be different if the users hand shakes
		This is a feature of the underlying window system, not Qt.
		If you want to show a tooltip immediately, while the mouse is moving (e.g., to get the mouse coordinates with QMouseEvent.pos() and show them as a tooltip), you must first enable mouse tracking as described above
		Then, to ensure that the tooltip is updated immediately, you must call QToolTip.showText() instead of PySide.QtGui.QWidget.setToolTip() in your implementation of PySide.QtGui.QWidget.mouseMoveEvent() .
		"""
		res = super(List_View,self).mouseMoveEvent(event)
		
	#----------------------------------------------------------------------
	def mousePressEvent(self,event):
		"""
		mousePressEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse press events for the widget.
		If you create new widgets in the PySide.QtGui.QWidget.mousePressEvent() the PySide.QtGui.QWidget.mouseReleaseEvent() may not end up where you expect, depending on the underlying window system (or X11 window manager), the widgets location and maybe more.
		The default implementation implements the closing of popup widgets when you click outside the window
		For other widget types it does nothing.
		"""
		res = super(List_View,self).mousePressEvent(event)
	#----------------------------------------------------------------------
	def mouseReleaseEvent(self,event):
		"""
		mouseReleaseEvent(event)
			event=QtGui.QMouseEvent

		This event handler, for event event , can be reimplemented in a subclass to receive mouse release events for the widget.
		"""
		res = super(List_View,self).mouseReleaseEvent(event)
	#----------------------------------------------------------------------
	def get_index(self, index):
		""""""
		if isinstance(self.model(), QT.QtGui.QSortFilterProxyModel):
			index = self.model().mapFromSource(index)
		return index
	#----------------------------------------------------------------------
	def Modify_Selection_Of_Index(self, item, command):
		""""""
		if issubclass(item.__class__, Tree_Item):
			index = self.get_index(item.index)
		elif issubclass(item.__class__, QT.QtCore.QModelIndex):
			index = self.get_index(item)
		else:
			raise ValueError("input Must Be a Tree_Item Or QModelIndex")
		
		rec = self.visualRect(index)
		self.setSelection(rec, command)
########################################################################
class MimeData(QtCore.QMimeData):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, indexs=[], copyFrom=None):
		"""Constructor"""
		super(MimeData, self).__init__()
		self.indexs = indexs
		self.dest_view   = None
		self.dest_item   = None
		self.dest_index  = None
		self.dest_object = None
		self.drop_action = None
		# if isinstance(copyFrom, QtCore.QMimeData):
			# for format in copyFrom.formats():
				# self.setData(format, copyFrom.data(format))
	#----------------------------------------------------------------------
	def set_Drop_Action(self, event):
		""""""
		key_mods = event.keyboardModifiers()
		mods = Qt.KeyboardModifier
		acts = Qt.DropAction
		if key_mods == mods.NoModifier or key_mods == mods.ShiftModifier:
			self.drop_action = acts.MoveAction
			event.setDropAction(acts.MoveAction)
		elif key_mods == mods.ControlModifier:
			self.drop_action = acts.CopyAction
			event.setDropAction(acts.CopyAction)
		else:
			self.drop_action = acts.IgnoreAction
			event.setDropAction(acts.IgnoreAction)
		
	#----------------------------------------------------------------------
	def set_Dest_Item(self, view, event):
		""""""
		self.dest_view = view
		index = view.indexAt(event.pos())
		if not index.isValid():
			index = view.rootIndex()
		if index.isValid():
			if index.data(ITEM_DATA_ROLE.Item_Type_Role) == Selection_Set_Tree_Item._Item_Type_ID:
				self.set_Drop_Action(event)
				self.dest_index  = index
				self.dest_item   = index.data(ITEM_DATA_ROLE.Tree_Item_Role)
				self.dest_object = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
				event.setAccepted(True)
			else:
				event.setAccepted(False)
		else:
			event.setAccepted(False)
	#----------------------------------------------------------------------
	def on_drop_event_Move_Items(self):
		""""""
		set_items = [item for item in self.indexs if item._Item_Type_ID == Selection_Set_Tree_Item._Item_Type_ID]
		obj_items = [item for item in self.indexs if item._Item_Type_ID == Maya_Node_Tree_Item._Item_Type_ID]		
		with Util_API.MayaUndoChunk():
			for item in set_items:
				if not item.data() == self.dest_item.data():
					internal_data = item.get_internal_Data()
					if not self.dest_object.has_Parent_Set(internal_data):
						if self.drop_action == QtCore.Qt.DropAction.MoveAction:
							item.parent.get_internal_Data().remove(internal_data)
						self.dest_object.addElement(internal_data)
			for item in obj_items:
				if self.drop_action == QtCore.Qt.DropAction.MoveAction:
					item_parent_set = item.parent.get_internal_Data().remove(item.get_internal_Data())
				self.dest_object.addElement(item.get_internal_Data())
########################################################################
class TreeModel(QtCore.QAbstractItemModel):
	def __init__(self, parent=None, root_item=None, headers=[], drag_n_drop_actions=None):
		super(TreeModel, self).__init__(parent)
		
		if len(headers) == 0:
			headers.append("First Name")
			headers.append("Last Name")
		if drag_n_drop_actions is None:
			drag_n_drop_actions = Qt.DropActions(Qt.DropAction.CopyAction | Qt.DropAction.MoveAction | Qt.DropAction.LinkAction)
			
		if root_item is None:
			root_item = Root_Tree_Item(self, header_names=headers)
			
		self.rootItem = root_item
		self.setSupportedDragActions(drag_n_drop_actions)
	#----------------------------------------------------------------------
	def columnCount(self, parent):
		if parent.isValid():
			return parent.internalPointer().column_Count
		else:
			return self.rootItem.column_Count
	#----------------------------------------------------------------------
	def data(self, index, role):
		if not index.isValid():
			return None
		item = index.internalPointer()
		return item.data(index.column(),role)
	#----------------------------------------------------------------------
	def setData(self, index, value, role):
		if not index.isValid():
			return True
		item = index.internalPointer()
		item.setData(value, index.column(),role)
		return True
	#----------------------------------------------------------------------
	def flags(self, index):
		if not index.isValid():
			return QtCore.Qt.NoItemFlags
		item = index.internalPointer()
		isinstance(item, Tree_Item)
		return item.flags(column=index.column())
	#----------------------------------------------------------------------
	def headerData(self, section, orientation, role):
		""""""
		if orientation == QtCore.Qt.Horizontal:
			d = self.rootItem.data(section, role)
			if d is None and role == QtCore.Qt.DisplayRole:
				return str(section+1)
			return d
		if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
			return str(section+1)
	#----------------------------------------------------------------------
	def index(self, row, column, parent):
		try:
			if not self.hasIndex(row, column, parent):
				return QtCore.QModelIndex()
		except RuntimeError:
			pass

		if not parent.isValid():
			parentItem = self.rootItem
		else:
			parentItem = parent.internalPointer()

		childItem = parentItem.child(row)
		try:
			return self.createIndex(row, column, childItem)
		except:
			print "Can Not Create Index"
		
		if childItem:
			return self.createIndex(row, column, childItem)
		else:
			return QtCore.QModelIndex()
	#----------------------------------------------------------------------
	def getItem(self, index):
		item = self.rootItem
		if index.isValid():
			internal_item = index.internalPointer()
			if internal_item:
				item = internal_item
		isinstance(item, Tree_Item)
		isinstance(item, Maya_Node_Tree_Item)
		isinstance(item, Selection_Set_Tree_Item)
		return item
	#----------------------------------------------------------------------
	def indexFromItem(self, item):
		root_index = self.index(0, 0, QtCore.QModelIndex())
		row_path = [item.row]
		current_item = item.parent
		if not hasattr(current_item, "row"):
			return root_index
		if item == self.rootItem:
			return root_index
		while current_item != self.rootItem:
			row_path.append(current_item.row)
			current_item = current_item.parent
		#row_path = row_path[:-1]
		row_path.reverse()
		#row_path.append(item.row)
		current_index = root_index.sibling(row_path.pop(0), 0)
		for row in row_path:
			current_index = current_index.child(row, 0)
		return current_index
	#----------------------------------------------------------------------
	def indexFromItemData(self, itemData):
		isinstance(itemData, Item_Data)
		item = itemData.tree_item
		root_index = self.index(0, 0, QtCore.QModelIndex())
		row_path = [item.row]
		current_item = item.parent
		if not hasattr(current_item, "row"):
			return root_index
		if item == self.rootItem:
			return root_index
		while current_item != self.rootItem:
			row_path.append(current_item.row)
			current_item = current_item.parent
		#row_path = row_path[:-1]
		row_path.reverse()
		#row_path.append(item.row)
		current_index = root_index.sibling(row_path.pop(0), itemData.column)
		for row in row_path:
			current_index = current_index.child(row, itemData.column)
		return current_index
	#----------------------------------------------------------------------
	def parent(self, index):
		if not index.isValid():
			return QtCore.QModelIndex()

		childItem = index.internalPointer()
		isinstance(childItem, Tree_Item)
		parentItem = childItem.parent
		if childItem == self.rootItem:
			return QtCore.QModelIndex()
		if parentItem == self.rootItem or parentItem is None:
			return QtCore.QModelIndex()

		return self.createIndex(parentItem.row, 0, parentItem)
	#----------------------------------------------------------------------
	def rowCount(self, parent):
		if parent.column() > 0:
			return 0

		if not parent.isValid():
			parentItem = self.rootItem
		else:
			parentItem = parent.internalPointer()

		return parentItem.child_Count
	#----------------------------------------------------------------------
	def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
		parentItem = self.getItem(parent)
		items = [parentItem.childItems[position]]
		success = parentItem.removeChildren(items)
		return success
	#----------------------------------------------------------------------
	def insertRows(self, position, items, parent=QtCore.QModelIndex()):
		parentItem = self.getItem(parent)
		count = len(items)
		success = parentItem.insertChildren(position, items)
		return success
	#----------------------------------------------------------------------
	def _display_output(self, item, tabs=0):
		""""""
		isinstance(item, Tree_Item)
		print "\t" * tabs, item.row, item.column_Count
		for i, col_item in enumerate(item.get_internal_Data().items):
			isinstance(col_item, Item_Data)
			state = col_item.get_Current_State()
			print "\t" * (tabs + 1), "column #%i" % i
			for key in sorted(state.keys()):
				print "\t" * (tabs + 2), key, state[key]
		for child in item.childItems:
			self._display_output(child, tabs+1)
	#----------------------------------------------------------------------
	def save_data(self):
		res = dict()
		for child in self.rootItem.childItems:
			self._display_output(child)
	#----------------------------------------------------------------------
	def dropMimeData(self, data, action, row, column, parent):
		""""""
		if isinstance(data, MimeData):
			if data.drop_action == QtCore.Qt.DropAction.MoveAction:
				dest = self.getItem(data.dest_item)
		return True
	#----------------------------------------------------------------------
	def mimeData(self, indexs):
		""""""
		items = []
		for index in indexs:
			# index = index.sibling(index.row(), 0)
			items.append(self.getItem(index))
		data = super(TreeModel, self).mimeData(indexs)
		mimedata = MimeData(items, data)
		return mimedata
	#----------------------------------------------------------------------
	def update_All_Items(self):
		""""""
		self.rootItem.update_All_Children()
########################################################################
class Selection_Set_Model(TreeModel):
	''''''
	# ==============
	# OVERRIDDEN FUNCTIONS
	# ==============
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		'''		'''
		self.logger = make_logger("Selection Set Model", logging.INFO)
		super(Selection_Set_Model, self).__init__(parent=parent, headers=["Set Name"])
		self._registered_PerNode_Maya_Callbacks = {}
	# #----------------------------------------------------------------------
	# def dropMimeData(self, data, action, row, column, parent):
		# """"""
		# if isinstance(data, MimeData):
			# if data.drop_action in [QtCore.Qt.DropAction.MoveAction, QtCore.Qt.DropAction.CopyAction]:
				# if data.dest_item._Item_Type_ID == Selection_Set_Tree_Item._Item_Type_ID:
					# isinstance(data.dest_item, Selection_Set_Tree_Item)
					# set_item  = data.dest_object
					# set_items = []
					# obj_items = []
					# for item in data.indexs:
						# if item._Item_Type_ID == Selection_Set_Tree_Item._Item_Type_ID:
							# set_items.append(item)
						# elif item._Item_Type_ID == Maya_Node_Tree_Item._Item_Type_ID:
							# obj_items.append(item)
					# with Util_API.MayaUndoChunk():
						# for item in set_items:
							# if data.drop_action == QtCore.Qt.DropAction.MoveAction:
								# item_parent_set = item.parent.get_internal_Data()
								# item_parent_set.remove(item.get_internal_Data())
							# set_item.addElement(item.get_internal_Data())
						# for item in obj_items:
							# if data.drop_action == QtCore.Qt.DropAction.MoveAction:
								# item_parent_set = item.parent.get_internal_Data()
								# item_parent_set.remove(item.get_internal_Data())
							# set_item.addElement(item.get_internal_Data())
		# return False
	#----------------------------------------------------------------------
	def mimeData(self, indexs):
		""""""
		items = []
		for index in indexs:
			# index = index.sibling(index.row(), 0)
			items.append(self.getItem(index))
		data = super(Selection_Set_Model, self).mimeData(indexs)
		mimedata = MimeData(items, data)
		return mimedata
	#----------------------------------------------------------------------
	def cleanup(self):
		'''Cleanup environment by removing the Maya callbacks, etc.'''
		self.logger.debug("running cleanup")
		self.logger.debug('removing All PerNode Maya Callbacks.')
		
		# Scan Through All The Childern
		for item in self.rootItem.all_childern:
			
			# Make Sure That Child Item Is A Maya Node Type
			if item._Item_Type_ID >= Maya_Node_Tree_Item._Item_Type_ID:
				
				# Remove All The Maya Callbacks Befor We Clear The Root
				self.Unregister_Single_Node_Callbacks(item)
				
		# This Function Removes All The child Tree Items
		# and removes That PerNode Callbacks
		self.rootItem.clear_Children()
	#----------------------------------------------------------------------
	def Register_PerNode_Maya_Callbacks(self, item):
		'''
		Add the Maya per-node callbacks for the specified item
		and register them with the widget (so they can be cleaned up).

		:Parameters:
		    nodeObj (MObject)
		'''
		# Check If The input is Maya Node
		# If So Add A Named Changed Callback
		if item._Item_Type_ID >= Maya_Node_Tree_Item._Item_Type_ID:
			self.logger.debug("Adding Name Changed Callback For %r" % item.get_internal_Data().nice_name)
			
			# Create The Callback Id
			cb = CB_Builders.create_Name_Changed_Callback(item.get_internal_Data()._MObject, item.update_Name_Changed_CB, None)
			
			# Add The Callback Id To This Items List Of Callbacks
			item._maya_callback_pointers.append(cb)
			
		# Check If The input is an Object Set
		# If So Add A Member Assinments Changed Callback
		if isinstance(item, Selection_Set_Tree_Item):
			self.logger.debug("Adding Attribute Changed Callback For %r" % item.get_internal_Data().nice_name)
			
			# Create The Callback Id
			cb = CB_Builders.create_Attribute_Changed_Callback(item.get_internal_Data()._MObject, self.Update_Connections_Changed_Callback, item)
			
			# Add The Callback Id To This Items List Of Callbacks
			item._maya_callback_pointers.append(cb)
	#----------------------------------------------------------------------	
	def Unregister_Single_Node_Callbacks(self, item):
		'''Remove per-node Maya callbacks. For The input Maya_Node_Tree_Item'''
		self.logger.debug('removing Callbacks For Node %r' % item.get_internal_Data().nice_name)
		
		# By Reinstasheating The List The Callback Automaticly Delete Themselfs
		item._maya_callback_pointers = []
	#----------------------------------------------------------------------
	def repopulate(self):
		'''Clear and populate the table with data retrieved from the Maya scene. Add Maya callbacks for changes to trigger UI updates.
		'''
		# Remove existing per-set callbacks
		# MCallbackWrapper objects auto-remove themselves.
		self.logger.debug("repopulating Selection Set Model")
		
		# Clear items in QTreeWidget
		self.cleanup()
		self.logger.debug("Creating AW Master Selection Set Grouping Node")
		
		# Create The Root Selection Set That Will Represent The Master Container
		self.AW_Master_Selection_Set = AW_Master_Selection_Set()
		
		# Create The Root Selection Set Item Data That QT Views Use To Know How To Display The Info  
		self.AW_Master_Item_Data     = Selection_Set_Item_Data(self.AW_Master_Selection_Set)
		
		# Create The Root Selection Set Tree Item That Is Used For Traversing A QT Item Data Model
		self.AW_Master_Tree_Item     = Selection_Set_Tree_Item(model=None, parent_item=self.rootItem, items=[self.AW_Master_Item_Data])
		
		# This Function Scans The Root Selection Set For Allready Existing Data
		self.AW_Master_Tree_Item.repopulate()
		
		# This Function Tells All The Attached Qt Views That The Informaion in the Data Model Has Changed
		self.layoutChanged.emit()
	#----------------------------------------------------------------------
	def _repopulate_Recersivly(self, parent_tree_item):
		isinstance(parent_tree_item, Selection_Set_Tree_Item)
		object_set = parent_tree_item.get_internal_Data()
		for child in object_set.children:
			isinstance(child, Util_API.SelectionSet)
			# Create The Item Data That QT Views Use To Know How To Display The Info  
			item_data     = Selection_Set_Item_Data(child)
			# Create The Tree Item That Is Used For Traversing A QT Item Data Model
			tree_item     = Selection_Set_Tree_Item(model=None, parent_item=parent_tree_item, items=[item_data])
			
			self.Register_PerNode_Maya_Callbacks(tree_item)
			self._repopulate_Recersivly(tree_item)
		for member in object_set.members:
			isinstance(member, Util_API.Maya_Node)
			# Create The Item Data That QT Views Use To Know How To Display The Info  
			member_data      = Maya_Item_Data(member)
			# Create The Tree Item That Is Used For Traversing A QT Item Data Model
			member_tree_item = Maya_Node_Tree_Item(model=None, parent_item=parent_tree_item, items=[member_data])
			self.Register_PerNode_Maya_Callbacks(member_tree_item)
	# ==============
	# CALLBACK FUNCTIONS FOR ITEM CHANGES WITHIN MAYA
	# ==============
	#----------------------------------------------------------------------
	def Update_Connections_Changed_Callback(self, msg, plg, other, client):
		isinstance(client, Tree_Item)
		# Check That Was Another Plug Invalved With The Changed
		# Meaning That Its Not A Value Cnaged But A Connecction Change
		if Node_Msg_Flags.OtherPlugSet & msg:
			# Check If The Plug That Changed Is A Index Of An Array Attribute
			if plg.isElement():
				# Remove Any Possable Compound Values And Get The Base Attribute Name  
				name = plg.name().split(".")[-1]
				# Check If The Attribute Plug That Was Changed Is Eather The Dagsetmembers Or Dnsetmembers
				# The dagSetMembers And Dnsetmembers Are The Two Attribures Used By Object Sets To Store What Has Ben Assined To Them
				# The dagSetMembers Attribure Stores Dag Graph Nodes Such As Mesh And Transforms
				# The dnSetMembers Attribure Stores Dependencey Graph Nodes Such As Other Object Sets Constrants And Shaders That Have No Hiarky
				if name.startswith("dagSetMembers") or name.startswith("dnSetMembers"):
					# Convert The Plgs Into A Custom Wrapper Class
					M_plg  = Util_API.MPLUG(plg)
					O_plg  = Util_API.MPLUG(other)
					# Get The Nodes That The Plugs Belong To
					M_node = M_plg.node
					O_node = O_plg.node
					
					# Check If The Plug That Changed Was The Dagsetmembers
					# And If The Old Plug Is Currenlty Connected To The Changed Plug
					# If So Then We Know A Connection Was Made And Not Broken 
					# So A New Tree Item Will Be Added To The Tree Item That this attribute is part of
					# Otherwise The A Connection Was Broken And Not Made
					# And The Tree Item That The Old Node Was Attached To Will Need To Be Removed And The Callbacks Deleated
					if name.startswith("dagSetMembers") and O_plg.is_Connected_To_Source(M_plg):
						# And Because The Plug That Was Changed was the dagSetMembers We Will Use A Maya Node Tree item
						# Create The Item Data That QT Views Use To Know How To Display The Info  
						item_data     = Maya_Item_Data(O_node)
						
						# Create The Tree Item That Is Used For Traversing A QT Item Data Model
						tree_item     = Maya_Node_Tree_Item(model=None, parent_item=client, items=[item_data])
						
						# Add The Call Back Needed For UI Updates For This Node
						self.Register_PerNode_Maya_Callbacks(tree_item)
						
					elif name.startswith("dnSetMembers") and O_plg.is_Connected_To_Source(M_plg):
						# Because The Plug That Was Changed was the dnSetMembers We Will Use A Selection Set Tree Item
						# Create The Item Data That QT Views Use To Know How To Display The Info  
						item_data     = Selection_Set_Item_Data(O_node)
						# Create The Tree Item That Is Used For Traversing A QT Item Data Model
						tree_item     = Selection_Set_Tree_Item(model=None, parent_item=client, items=[item_data])
						
						self.Register_PerNode_Maya_Callbacks(tree_item)
						
						self._repopulate_Recersivly(tree_item)
						
					elif name.startswith("dagSetMembers") and not O_plg.is_Connected_To_Source(M_plg):
						
						child_item = client.find_child(O_node.nice_name)
						self.Unregister_Single_Node_Callbacks(child_item)
						client.removeChildren([child_item])
							
					elif name.startswith("dnSetMembers") and not O_plg.is_Connected_To_Source(M_plg):
						
						child_item = client.find_child(O_node.nice_name)
						self.Unregister_Single_Node_Callbacks(child_item)
						for sub_child in client.all_childern:
							if sub_child._Item_Type_ID >= Maya_Node_Tree_Item._Item_Type_ID:
								self.Unregister_Single_Node_Callbacks(sub_child)
						client.removeChildren([child_item])
	#----------------------------------------------------------------------
	def get_expaded(self):
		for child in Root_Tree_Item.all_childern:
			isinstance(child, Tree_Item)
			child.index
########################################################################
class Selection_Set_Proxy_Model(QtGui.QSortFilterProxyModel):
	""""""
	def __init__(self, parent=None):
		super(Selection_Set_Proxy_Model, self).__init__(parent=parent)
		self._scan_type = 0
		self._filter_type =  QtCore.QRegExp.Wildcard
	#----------------------------------------------------------------------
	def filterAcceptsRow(self, sourceRow, sourceParent):
		regex = self.filterRegExp()
		if not sourceParent.isValid():
			model = self.sourceModel()
			sourceParent = model.rootItem.index
		
		item  = sourceParent.data(ITEM_DATA_ROLE.Tree_Item_Role)
		if item is None:
			return True
		if regex.isEmpty():
			return True
		else:
			child = item.child(sourceRow)	
			if regex.exactMatch(child.data()):
				return True
			elif self._scan_type == 0:
				return False
			else:
				for child in child.all_childern:
					if regex.exactMatch(child.data()):
						return True
				return False
########################################################################
class AW_Selection_Set_Editor(Scripts.UICls.mayaMixin.MayaQWidgetDockableMixin, QtGui.QWidget):
	ISOLATE_STATE_CHANGED    = QtSignal(bool)
	#----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(AW_Selection_Set_Editor, self).__init__(parent=parent)
		if False:
			# Widgets
			self.Selection_Set_Editor                             = AW_Selection_Set_Editor()
			self.Display_Options_GroupBox                         = QtGui.QGroupBox()
			self.Display_Options_Frame                            = QtGui.QFrame()
			self.Button_Display_Options_GroupBox                  = QtGui.QGroupBox()
			self.Button_Display_Options_Frame                     = QtGui.QFrame()
			self.radioButton_3                                    = QtGui.QRadioButton()
			self.radioButton_2                                    = QtGui.QRadioButton()
			self.radioButton                                      = QtGui.QRadioButton()
			self.Tool_Windows_Toggle_GroupBox                     = QtGui.QGroupBox()
			self.Tool_Windows_Toggle_Frame                        = QtGui.QFrame()
			self.Locking_Window_Toggle_checkBox                   = QtGui.QCheckBox()
			self.Viewport_Window_Toggle_checkBox                  = QtGui.QCheckBox()
			self.Assinments_Window_Toggle_checkBox                = QtGui.QCheckBox()
			self.Creation_Window_Toggle_checkBox                  = QtGui.QCheckBox()
			self.Tools_Window_Toggle_checkBox                     = QtGui.QCheckBox()
			self.Selection_Window_Toggle_checkBox                 = QtGui.QCheckBox()
			self.Outline_Container_Widget                         = QtGui.QWidget()
			self.Selection_Set_Outliner_groupBox                  = QtGui.QGroupBox()
			self.Selection_Set_Outliner_Frame                     = QtGui.QFrame()
			self.Selection_Set_Outliner_Tree_View                 = Selection_Set_Tree_View()
			self.Tools_GroupBox                                   = QtGui.QGroupBox()
			self.Tools_Frame                                      = QtGui.QFrame()
			self.SSets_Maya_Content_Creation_GroupBox             = QtGui.QGroupBox()
			self.SSets_Maya_Content_Creation_Frame                = QtGui.QFrame()
			self.Create_Empty_Set_Button                          = QtGui.QToolButton()
			self.Copy_Highlighted_Sets_Button                     = QtGui.QToolButton()
			self.Delete_Highlighted_Sets_Button                   = QtGui.QToolButton()
			self.SSets_Membership_Assinment_GroupBox              = QtGui.QGroupBox()
			self.SSets_Membership_Assinment_Frame                 = QtGui.QFrame()
			self.Add_Selection_To_Highlighted_Sets_Button         = QtGui.QToolButton()
			self.Remove_Selection_From_Highlighted_Sets_Button    = QtGui.QToolButton()
			self.Add_Highlighted_Nodes_To_Highlighted_Set_Button  = QtGui.QToolButton()
			self.Remove_Highlighted_From_Parent_Sets_Button       = QtGui.QToolButton()
			self.SSets_Selections_GroupBox                        = QtGui.QGroupBox()
			self.SSets_Selections_Frame                           = QtGui.QFrame()
			self.Select_Highlighted_Sets_Button                   = QtGui.QToolButton()
			self.Select_Highlighted_Set_Members_Button            = QtGui.QToolButton()
			self.Select_Highlighted_Child_Sets_Button             = QtGui.QToolButton()
			self.Select_Highlighted_Set_Member_Recursively_Button = QtGui.QToolButton()
			self.SSets_Maya_Viewport_GroupBox                     = QtGui.QGroupBox()
			self.SSets_Maya_Viewport_Frame                        = QtGui.QFrame()
			self.Frame_Highlighted_Set_Members_Button             = QtGui.QToolButton()
			self.SSets_Isolate_Contents_Tool_Button               = QtGui.QToolButton()
			self.Reveal_Highlighted_Outliner_Panel_Button         = QtGui.QToolButton()
			self.Frame_Highlighted_Button                         = QtGui.QToolButton()
			self.SSets_Locking_GroupBox                           = QtGui.QGroupBox()
			self.SSets_Locking_Frame                              = QtGui.QFrame()
			self.Unlock_Highlighted_Sets_Button                   = QtGui.QToolButton()
			self.Lock_Highlighted_Sets_Button                     = QtGui.QToolButton()
			self.Display_Options_toolButton                       = Display_Option_Tool_Button()
			self.Outliner_Item_Filter_lineEdit                    = QtGui.QLineEdit()
			self.Filter_Options_Button                            = QtGui.QPushButton()
			# Actions
			self.action_Add_Highlighted_Nodes_To_Highlighted_Set  = QtGui.QAction()
			self.action_Add_Selection_To_Highlighted_Sets         = QtGui.QAction()
			self.action_Copy_Highlighted_Sets                     = QtGui.QAction()
			self.action_Create_Empty_Set                          = QtGui.QAction()
			self.action_Delete_Highlighted_Sets                   = QtGui.QAction()
			self.action_Frame_Highlighted                         = QtGui.QAction()
			self.action_Frame_Highlighted_Set_Members             = QtGui.QAction()
			self.action_Lock_Highlighted_Sets                     = QtGui.QAction()
			self.action_Move_Highlighted_Down                     = QtGui.QAction()
			self.action_Move_Highlighted_Up                       = QtGui.QAction()
			self.action_Remove_Highlighted_From_Parent_Sets       = QtGui.QAction()
			self.action_Remove_Selection_From_Highlighted_Sets    = QtGui.QAction()
			self.action_Reveal_Highlighted_Outliner_Panel         = QtGui.QAction()
			self.action_Select_Highlighted_Child_Sets             = QtGui.QAction()
			self.action_Select_Highlighted_Set_Member_Recursively = QtGui.QAction()
			self.action_Select_Highlighted_Set_Members            = QtGui.QAction()
			self.action_Select_Highlighted_Sets                   = QtGui.QAction()
			self.action_Set_Inerface_To_Icons_Only                = QtGui.QAction()
			self.action_Set_Inerface_To_Text_And_Icons            = QtGui.QAction()
			self.action_Set_Inerface_To_Text_Only                 = QtGui.QAction()
			self.action_Toggle_Isolate_Highlighted                = QtGui.QAction()
			self.action_Unlock_Highlighted_Sets                   = QtGui.QAction()
	#----------------------------------------------------------------------
	def _run_setup(self):
		""""""
		self.logger = make_logger("Editor", logging.INFO)
		file_path = os.path.dirname(__file__) + "\\\\Filter_Options.ui"
		mayaMainWindowPtr = omui.MQtUtil.mainWindow()
		maya_main_window = wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)
		self.Filter_Options_Widget = ui_Loader.load(file_path, self)
		self.Filter_Options_Widget.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.CustomizeWindowHint)
		
		self.display_option_Show_Name_Space  = OptionVariable_Bool_Action("Show Name Space", _Global_Options.display_show_name_spaces, parent=self)
		self.display_option_Show_Name_Space.setIcon(self.action_Show_Name_Spaces.icon())
		self._ignore_Selection_update = True
		self._disable_Update_UI_Stack = []
		self._disable_Update_For_Rebuild       =  False
		self._disable_Update_For_Rescan_Add    =  False
		self._disable_Update_For_Rescan_Remove =  False
		self._registered_Maya_Callbacks = []
		self._Items_To_Be_Added_After_Update = []
		self._previous_Selected_Items = []
		self.selection_set_model = Selection_Set_Model(parent=self)
		self.selection_set_model_proxy = Selection_Set_Proxy_Model(self)
		self.selection_set_model_proxy.setDynamicSortFilter(True)
		self.selection_set_model_proxy.setSourceModel(self.selection_set_model)
		self.setAttribute(Qt.WA_DeleteOnClose, True)
		self.selection_set_model.repopulate()
		self.Selection_Set_Outliner_Tree_View.setModel(self.selection_set_model_proxy)
		self.Display_Options_toolButton.run_setup()
		# self.Selection_Set_Outliner_Tree_View.setRootIndex(self.selection_set_model_proxy.mapFromSource(self.selection_set_model.rootItem.index))
		self._connect_default_actions()
		self._attach_action_triggers()
		# self._Create_Context_Menus()
		self.add_Maya_Scene_Callbacks()
		self.destroyed.connect(self.cleanup)
		self._first_run = True
		self.setMinimumWidth(530)
		self.Selection_Set_Outliner_Tree_View._run_setup(self)
		self.Selection_Set_Outliner_Tree_View.setDefaultDropAction(Qt.DropAction.CopyAction)
		self.Selection_Set_Outliner_Tree_View.setDropIndicatorShown(False)
		self.Outliner_Item_Filter_lineEdit.textChanged.connect(self.filterRegExpChanged)
		self.Filter_Options_Button.toggled.connect(self.show_Filter_Options_Window)
		# self.Selection_Set_Outliner_Tree_View.set(Qt.DropAction.TargetMoveAction)
	#----------------------------------------------------------------------
	def filter_Options_Changed(self):
		self.selection_set_model_proxy._scan_type = self.Filter_Options_Widget.Scan_Type.currentIndex()
		syntax          = QtCore.QRegExp.PatternSyntax(self.Filter_Options_Widget.RegExp_Syntax.itemData(self.Filter_Options_Widget.RegExp_Syntax.currentIndex()))
		caseSensitivity = [QtCore.Qt.CaseSensitivity.CaseInsensitive, QtCore.Qt.CaseSensitivity.CaseSensitive][self.Filter_Options_Widget.Case_Sensitivity.currentIndex()]
		val = self.Outliner_Item_Filter_lineEdit.text()
		# if val.strip() == "":
			# val = "*"
		regExp = QtCore.QRegExp()
		regExp.setCaseSensitivity(caseSensitivity)
		regExp.setPattern(val)
		regExp.setPatternSyntax(syntax)
		self.selection_set_model_proxy.setFilterRegExp(regExp)
		# self.Selection_Set_Outliner_Tree_View.setRootIndex(self.selection_set_model_proxy.mapFromSource(self.selection_set_model.rootItem.index))
		
	#----------------------------------------------------------------------
	def filterRegExpChanged(self):
		regExp = self.selection_set_model_proxy.filterRegExp()
		val = self.Outliner_Item_Filter_lineEdit.text()
		# if val.strip() == "":
			# val = "*"
		regExp.setPattern(val)
		self.selection_set_model_proxy.setFilterRegExp(regExp)
		# self.Selection_Set_Outliner_Tree_View.setRootIndex(self.selection_set_model_proxy.mapFromSource(self.selection_set_model.rootItem.index))
	#----------------------------------------------------------------------
	def _update_on_top_level_Changed(self, val):
		if not val:
			self.setMinimumWidth(530)
		else:
			self.setMinimumWidth(0)
	#----------------------------------------------------------------------
	def _connect_default_actions(self):
		""""""
		self.Copy_Highlighted_Sets_Button.setDefaultAction(self.action_Copy_Highlighted_Sets)
		self.Delete_Highlighted_Sets_Button.setDefaultAction(self.action_Delete_Highlighted_Sets)
		self.Add_Selection_To_Highlighted_Sets_Button.setDefaultAction(self.action_Add_Selection_To_Highlighted_Sets)
		self.Remove_Selection_From_Highlighted_Sets_Button.setDefaultAction(self.action_Remove_Selection_From_Highlighted_Sets)
		self.Add_Highlighted_Nodes_To_Highlighted_Set_Button.setDefaultAction(self.action_Add_Highlighted_Nodes_To_Highlighted_Set)
		self.Remove_Highlighted_From_Parent_Sets_Button.setDefaultAction(self.action_Remove_Highlighted_From_Parent_Sets)
		self.Select_Highlighted_Sets_Button.setDefaultAction(self.action_Select_Highlighted_Sets)
		self.Select_Highlighted_Set_Members_Button.setDefaultAction(self.action_Select_Highlighted_Set_Members)
		self.Select_Highlighted_Child_Sets_Button.setDefaultAction(self.action_Select_Highlighted_Child_Sets)
		self.Select_Highlighted_Set_Member_Recursively_Button.setDefaultAction(self.action_Select_Highlighted_Set_Member_Recursively)
		self.Frame_Highlighted_Set_Members_Button.setDefaultAction(self.action_Frame_Highlighted_Set_Members)
		# self.SSets_Isolate_Contents_Tool_Button.setDefaultAction()
		self.Reveal_Highlighted_Outliner_Panel_Button.setDefaultAction(self.action_Reveal_Highlighted_Outliner_Panel)
		self.Frame_Highlighted_Button.setDefaultAction(self.action_Frame_Highlighted)
		self.Show_Name_Spaces_Tool_Button.setDefaultAction(self.display_option_Show_Name_Space)
	#----------------------------------------------------------------------
	def _attach_action_triggers(self):
		""""""
		isinstance(self.Display_Options_toolButton, Display_Option_Tool_Button)
		self.action_Add_Selection_To_Highlighted_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.add_Selected_To_Sets)
		self.action_Add_Highlighted_Nodes_To_Highlighted_Set.triggered.connect(self.Selection_Set_Outliner_Tree_View.add_Hilighted_To_Highlighted)
		# self.action_Copy_Highlighted_Sets.triggered.connect()
		self.action_Create_Empty_Set.triggered.connect(self._Action_Create_New_Set)
		self.action_Delete_Highlighted_Sets.triggered.connect(self._Action_Delete_Set)
		self.action_Frame_Highlighted.triggered.connect(self.Selection_Set_Outliner_Tree_View.frame_Highlighted_Items)
		self.action_Frame_Highlighted_Set_Members.triggered.connect(self.Selection_Set_Outliner_Tree_View.frame_Highlighted_Contents)
		self.action_Lock_Highlighted_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.lock_Highlighted_Sets)
		self.action_Unlock_Highlighted_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.unlock_Highlighted_Sets)
		self.action_Move_Highlighted_Down.triggered.connect(self.Selection_Set_Outliner_Tree_View.move_Hilighted_Down)
		self.action_Move_Highlighted_Up.triggered.connect(self.Selection_Set_Outliner_Tree_View.move_Hilighted_Up)
		self.action_Remove_Highlighted_From_Parent_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.remove_Hilighted_From_Parents)
		self.action_Remove_Selection_From_Highlighted_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.remove_Selected_From_Sets)
		self.action_Reveal_Highlighted_Outliner_Panel.triggered.connect(self.Selection_Set_Outliner_Tree_View.reveal_Highlighted_In_Outliner)
		self.action_Select_Highlighted_Child_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.select_Hilighted_Child_Sets)
		self.action_Select_Highlighted_Set_Member_Recursively.triggered.connect(self.Selection_Set_Outliner_Tree_View.select_Highlighted_Hierarchy)
		self.action_Select_Highlighted_Set_Members.triggered.connect(self.Selection_Set_Outliner_Tree_View.select_Highlighted_Set_Members)
		self.action_Select_Highlighted_Sets.triggered.connect(self.Selection_Set_Outliner_Tree_View.select_Highlighted_Contents)
		self.Display_Options_toolButton.option_Tools.toggled.connect(self.Tools_GroupBox.setVisible)
		self.Display_Options_toolButton.option_Creation.toggled.connect(self.SSets_Maya_Content_Creation_GroupBox.setVisible)
		self.Display_Options_toolButton.option_Assinments.toggled.connect(self.SSets_Membership_Assinment_GroupBox.setVisible)
		self.Display_Options_toolButton.option_Selection.toggled.connect(self.SSets_Selections_GroupBox.setVisible)
		self.Display_Options_toolButton.option_Viewport.toggled.connect(self.SSets_Maya_Viewport_GroupBox.setVisible)
		self.display_option_Show_Name_Space.toggled.connect(self.selection_set_model.update_All_Items)
	#----------------------------------------------------------------------
	def _set_first_run_settings(self):
		""""""
		self.Tools_GroupBox.setVisible(self.Display_Options_toolButton.option_Tools.isChecked())
		self.SSets_Maya_Content_Creation_GroupBox.setVisible(self.Display_Options_toolButton.option_Creation.isChecked())
		self.SSets_Membership_Assinment_GroupBox.setVisible(self.Display_Options_toolButton.option_Assinments.isChecked())
		self.SSets_Selections_GroupBox.setVisible(self.Display_Options_toolButton.option_Selection.isChecked())
		self.SSets_Maya_Viewport_GroupBox.setVisible(self.Display_Options_toolButton.option_Viewport.isChecked())
		self.Filter_Options_Widget.Scan_Type.currentIndexChanged.connect(self.filter_Options_Changed)
		self.Filter_Options_Widget.RegExp_Syntax.currentIndexChanged.connect(self.filter_Options_Changed)
		self.Filter_Options_Widget.Case_Sensitivity.currentIndexChanged.connect(self.filter_Options_Changed)
		self.filter_Options_Changed()
	#----------------------------------------------------------------------
	def _Create_Context_Menus(self):
		""""""
		self.selection_set_view_set_item_context_menu = QtGui.QMenu(self)
		Options_Menu         = self.selection_set_view_set_item_context_menu.addMenu("Options")
		Display_Options_Menu = Options_Menu.addMenu("Display")
		placement_menu       = self.selection_set_view_set_item_context_menu.addMenu("Placement")
		node_locking_menu    = self.selection_set_view_set_item_context_menu.addMenu("Locking")
		selection_Menu       = self.selection_set_view_set_item_context_menu.addMenu("Selecting")
		Assinments_Menu      = self.selection_set_view_set_item_context_menu.addMenu("Assinments")
		Viewport_Menu        = self.selection_set_view_set_item_context_menu.addMenu("Viewport")
		## Color ConText Menus
		placement_menu.addAction(self.action_Move_Highlighted_Up)
		placement_menu.addAction(self.action_Move_Highlighted_Down)
		
		node_locking_menu.addAction(self.action_Lock_Highlighted_Sets)
		node_locking_menu.addAction(self.action_Unlock_Highlighted_Sets)
		
		selection_Menu.addAction(self.action_Select_Highlighted_Sets)
		selection_Menu.addAction(self.action_Select_Highlighted_Child_Sets)
		selection_Menu.addAction(self.action_Select_Highlighted_Set_Members)
		selection_Menu.addAction(self.action_Select_Highlighted_Set_Member_Recursively)
		
		Assinments_Menu.addAction(self.action_Add_Selection_To_Highlighted_Sets)
		Assinments_Menu.addAction(self.action_Remove_Selection_From_Highlighted_Sets)
		Assinments_Menu.addSeparator()
		Assinments_Menu.addAction(self.action_Add_Highlighted_Nodes_To_Highlighted_Set)
		Assinments_Menu.addAction(self.action_Remove_Highlighted_From_Parent_Sets)
		
		Viewport_Menu.addAction(self.action_Frame_Highlighted_Set_Members)
		Viewport_Menu.addAction(self.action_Frame_Highlighted)
		Viewport_Menu.addAction(self.action_Reveal_Highlighted_Outliner_Panel)
		
		Display_Options_Menu.addAction(self.Display_Options_toolButton.option_Tools)
		Display_Options_Menu.addAction(self.Display_Options_toolButton.option_Creation)
		Display_Options_Menu.addAction(self.Display_Options_toolButton.option_Assinments)
		Display_Options_Menu.addAction(self.Display_Options_toolButton.option_Selection)
		Display_Options_Menu.addAction(self.Display_Options_toolButton.option_Viewport)
		
		# self.selection_set_view_set_item_context_menu.addAction(self.action_Selection_Set_Select_Child_Sets)
		# self.selection_set_view_set_item_context_menu.addAction(self.action_Selection_Set_Select_Child_Nodes)
		# self.selection_set_view_set_item_context_menu.addAction(self.action_Selection_Set_Add_Active_Selection)
		# self.selection_set_view_set_item_context_menu.addAction(self.action_Selection_Set_Remove_Active_Selection)
		# self.selection_set_view_set_item_context_menu.addAction(self.action_Selection_Set_Delete_Set)
		self.Selection_Set_Outliner_Tree_View._context_menu = self.selection_set_view_set_item_context_menu
	#----------------------------------------------------------------------
	@QtSlot()
	def _Action_Create_New_Set(self):
		""""""
		selected_indices = self.Selection_Set_Outliner_Tree_View.selected_Selection_Set_Indexes()
		if not len(selected_indices):
			selected_indices = [self.selection_set_model.AW_Master_Tree_Item.index]
		if len(selected_indices):
			with Util_API.MayaUndoChunk():
				new_set = Util_API.SelectionSet("NEW_AW_SELECTION_SET", empty=True, copy=None)
				new_set.name = "Selection_Set_Goup_0"
				for index in selected_indices:
					item_set  = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
					item_set.include(new_set)
				new_set.lockNode()
	#----------------------------------------------------------------------
	@QtSlot()
	def _Action_Delete_Set(self):
		""""""
		#----------------------------------------------------------------------
		def Remove_Recursively(selection_set):
			for child in selection_set.children:
				Remove_Recursively(child)
			selection_set.delete()
		
		selected_indices =  self.Selection_Set_Outliner_Tree_View.selected_Selection_Set_Indexes()
		if len(selected_indices):
			with Util_API.MayaUndoChunk():
				for index in selected_indices:
					item_set  = index.data(ITEM_DATA_ROLE.Internal_Data_Role)
					Remove_Recursively(item_set)
	#----------------------------------------------------------------------	
	def showEvent(self, event):
		if self._first_run:
			self._set_first_run_settings()
			nav_par = self.nativeParentWidget()
			nav_par.topLevelChanged.connect(self._update_on_top_level_Changed)
			self._first_run =  False
		# self.add_Maya_Scene_Callbacks()
		# self.selection_set_model.repopulate()
		super(AW_Selection_Set_Editor, self).showEvent(event)
	#----------------------------------------------------------------------
	def hideEvent(self, *args):
		'''When widget is hidden, remove the Maya callbacks and clean up.'''
		# self.cleanup()
		# NOTE: Not using super() as hideEvent could be called after it seems that self is deleted with __del__ and super does not work then
		return QtGui.QWidget.hideEvent(self, *args)
	#----------------------------------------------------------------------
	def cleanup(self):
		'''Cleanup environment by removing the Maya callbacks, etc.
		'''
		# MCallbackWrapper items automatically clean themselves up on deletion
		self.logger.debug("Runing Cleanup")
		self.remove_Maya_Scene_CallBacks()
		self._registeredMayaCallbacks = []
		self.selection_set_model.cleanup()
	# ===================
	# Global Callbacks
	# ===================
	#----------------------------------------------------------------------
	def remove_Maya_Scene_CallBacks(self):
		self.logger.debug('Removing Maya Scene Call Backs.')
		while len(self._registered_Maya_Callbacks):
			cb = self._registered_Maya_Callbacks.pop()
			del cb
	#----------------------------------------------------------------------
	def add_Maya_Scene_Callbacks(self):
		""""""
		self.logger.debug('Adding Maya Scene Call Backs.')
		# cb = CB_Builders.Event_Callback_Creators.create_Event_SelectionChanged_Callback(self.mayaSelectionChangedCB)
		# self._registered_Maya_Callbacks.append(cb)
	
		# cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.CreateReference, self.After_Scene_Update_CB, 'BeforeReference') 
		# self._registered_Maya_Callbacks.append(cb)
		# cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.RemoveReference, self.After_Scene_Update_CB, 'BeforeRemoveReference') 
		# self._registered_Maya_Callbacks.append(cb)
		# cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.ImportReference, self.After_Scene_Update_CB, 'BeforeImportReference') 
		# self._registered_Maya_Callbacks.append(cb)
		# cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.LoadReference  , self.After_Scene_Update_CB, 'BeforeLoadReference') 
		# self._registered_Maya_Callbacks.append(cb)
		# cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.UnloadReference, self.After_Scene_Update_CB, 'BeforeUnloadReference')
		# self._registered_Maya_Callbacks.append(cb)
		def create_Scene_Message_Callbacks(self):
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.New            , self.Before_Scene_Rebuild_CB, 'BeforeNew') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.Open           , self.Before_Scene_Rebuild_CB, 'BeforeOpen') 
			self._registered_Maya_Callbacks.append(cb)
		
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.New            , self.After_Scene_Rebuild_CB, 'BeforeNew') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.Open           , self.After_Scene_Rebuild_CB, 'BeforeOpen') 
			self._registered_Maya_Callbacks.append(cb)
			
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.Import         , self.Before_Scene_Update_CB, 'BeforeImport') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.CreateReference, self.Before_Scene_Update_CB, 'BeforeReference') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.RemoveReference, self.Before_Scene_Update_CB, 'BeforeRemoveReference') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.ImportReference, self.Before_Scene_Update_CB, 'BeforeImportReference') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.LoadReference  , self.Before_Scene_Update_CB, 'BeforeLoadReference') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_B_Flags.UnloadReference, self.Before_Scene_Update_CB, 'BeforeUnloadReference') 
			self._registered_Maya_Callbacks.append(cb)
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_Flags.MayaExiting      , self.Before_Scene_Rebuild_CB, 'MayaExiting') 
			self._registered_Maya_Callbacks.append(cb)
		
			cb = CB_Builders.create_Scene_Message_Callback(S_Msg_A_Flags.Import         , self.After_Scene_Update_CB, 'BeforeImport') 
			self._registered_Maya_Callbacks.append(cb)
			
		def create_Node_Added_And_Removed_Callbacks(self):
			for node_type in ["objectSet"]:
				cb = CB_Builders.create_NodeAdded_Callback(node_type, self.nodeAddedCB, node_type)
				self._registered_Maya_Callbacks.append(cb)
		
				cb = CB_Builders.create_NodeRemoved_Callback(node_type , self.nodeRemovedCB, node_type)
				self._registered_Maya_Callbacks.append(cb)
			
		self._registered_Maya_Callbacks = []
		
		create_Node_Added_And_Removed_Callbacks(self)
		
		create_Scene_Message_Callbacks(self)
	# ==============
	# MAYA MMessage SCENE CALLBACKS
	#   These are the Maya callbacks that update the Qt widget from the Maya scene changes.
	#   Maya Scene changed -> Qt widget updated
	#   These are distinctly separate from and should not be confused with the
	#   Popup menu action callbacks above.
	# ==============
	#----------------------------------------------------------------------
	def Before_Scene_Rebuild_CB(self, clientData):
		'''
		Freeze the callbacks before the entire scene is being reloaded or cleared.
		Unfreezing the callbacks is handled in the afterSceneChangedCB.
		'''
		self.logger.debug('Executing Before Rebuild Call Back For "%s"' % (clientData) )
		self._disable_Update_For_Rebuild = True
		self.selection_set_model.cleanup()
	#----------------------------------------------------------------------
	def After_Scene_Rebuild_CB(self, clientData):
		'''
		Freeze the callbacks before the entire scene is being reloaded or cleared.
		Unfreezing the callbacks is handled in the afterSceneChangedCB.
		'''
		self.logger.debug('Executing After Rebuild Call Back For "%s"' % (clientData) )
		self.add_Maya_Scene_Callbacks()
		self.selection_set_model.repopulate()
		# self.Selection_Set_Outliner_Tree_View.setRootIndex(self.selection_set_model_proxy.mapFromSource(self.selection_set_model.rootItem.index))
	#----------------------------------------------------------------------
	def Before_Check_CB(self, other, clientData):
		''''''
		self.logger.debug('Executing Before Check Call Back For "%s"' % (clientData) )
		self.cleanup()
		#if clientData in ["Before_New_Check", "Before_Open_Check"]:
			#self._disable_Update_For_Rebuild = True
			#other.next()
			#
		#elif clientData in ["Before_Import_Check", "Before_Load_Reference_Check", "Before_Create_Reference_Check"]:
			#self._disable_Update_For_Rescan_Add = True
			#other.next()
		#else:
			#other.next()
		return True
	#----------------------------------------------------------------------
	def nodeAddedCB(self, nodeObj, clientData):
		'''Selectively update the widget tree for the specified item when a shader is added to the Maya scene

		:Parameters:
		    nodeObj (MObject)
		        MObject depend node for the node added
		    clientData
		        container of the Maya client data for the event
		'''
		#if len(self._disable_Update_UI_Stack) > 0:
			#if self._disable_Update_For_Rescan_Add:
				#item_name    = Util_API.nameToNode(nodeObj).name()
				#if not item_name in self._Items_To_Be_Added_After_Update:
					#logger.debug('shader Node %s Will Be Added After Maya Has Finished ' %  (item_name))
					#self._Items_To_Be_Added_After_Update.append(item_name)
		#else:
			#nodeFn    = Util_API.nameToNode(nodeObj)
			#for model in [self.selection_set_model, self.shader_model_B]:
				#item = model.rootItem.find_child(nodeFn.name())
				#if item is None:
					#logger.debug('shader Node "%s" of Type %s Added' %  (nodeFn.name(), clientData))
					#shader    = Util_API.Shading_Node(nodeFn.name())
					#item      = Shader_Item_Data(shader)
					#tree_item = Tree_Item(model=None, parent_item=model.rootItem, items=[item])
					## Surgically add the item (and callbacks) to the UI (instead of repopulating entire widget)
					#model.addPerNodeMayaCallbacks(item)
					#model.layoutChanged.emit()
				#else:
		self.logger.debug('Bypassing shader Node Added because a node with the same name exists within the data model')
	#----------------------------------------------------------------------
	def nodeRemovedCB(self, nodeObj, clientData):
		'''Selectively update the model for the specified item when a shader is removed from the Maya scene

		:Parameters:
		    nodeObj (MObject)
		        MObject depend node for the node added
		    clientData
		        container of the Maya client data for the event
		'''    
		#else:
			#logger.debug('shader Node %s Type Removed' %  clientData)
			#nodeName = Util_API.nameToNode(nodeObj).name()
			#logger.debug('Scaning For Node: "%s"' % nodeName)
			#for model in [self.selection_set_model, self.shader_model_B]:
				## Surgically remove the item from the UI (instead of repopulating entire widget)
				#item = model.rootItem.find_child(nodeName, role=ITEM_DATA_ROLE.FullNameRole)
				#if item is not None:
					#isinstance(item, Tree_Item)
					#logger.debug('Removing node from UI: %s'%nodeName)
					#item.parentItem.removeChildren([item])
				#else:
					#logger.debug('Could not find a match for "%s".  Skipping update in UI.' % nodeName)
		
				## Remove node callbacks
				#model.removePerNodeMayaCallbacks([nodeObj])
		self.logger.debug('Bypassing shader Node Removed')
	#----------------------------------------------------------------------
	def mayaSelectionChangedCB(self, clientData):
		'''The selection has changed.  Update the background coloring of the items
		using the secondary highlight color (used by the Maya Outliner) to reflect member-set relationships.

		:Parameters:
		    clientData
		        container of the Maya client data for the event

		:Return: None
		'''
		self.logger.debug("In mayaSelectionChangedCB()")
		if len(self._disable_Update_UI_Stack) == 0:
			self.requestUpdateHighlightedItems()
	#----------------------------------------------------------------------
	def requestUpdateHighlightedItems(self):
		'''Request deferred update of the highlighted items to when Maya is idle.
		This improves performance when doing large operations like duplicating
		hundreds of objectSets.
		'''
		self.logger.debug("In requestUpdateHighlightedItems()")
		if len(self._disable_Update_UI_Stack) == 0:
			
			# If updateHighlightedItems is not already in the 
			# queue to be updated, add it to the idle event queue
			if self._ignore_Selection_update:
				self._ignore_Selection_update = False
				cmds.evalDeferred(self.updateHighlightedItems_execute, low=True)
			else:
				self.logger.debug("Skipping on idle execute of updateHighlightedItems_execute(). Already queued.")
	#----------------------------------------------------------------------
	def updateHighlightedItems_execute(self):
		'''Update the highlighted items (visualized by changing the background
		color of the item) to indicate the items that the Maya selected items
		are members of.
		'''
		self.logger.debug("In updateHighlightedItems_execute()")

		# Set the dirty flag to clean as updateHighlightedItems_execute
		# is being executed
		self._ignore_Selection_update = True
		
		# Get list of selected Nodes
		# active_items = cmds.ls(sl=True,long=True)
		# names        = [m.get_internal_Data(0).name for m in self.selection_set_model.AW_Master_Tree_Item.all_childern]
		# s1           = set(active_items)
		# s2           = set(names)
		# resalt       = list(s1.intersection(s2))
		
		# if len(self._previous_Selected_Items):
			# for child in self._previous_Selected_Items:
				# child.update()
			# self._previous_Selected_Items = []
		
		self.selection_set_model.AW_Master_Tree_Item.update_All_Children()
		# # Update if needed
		# if len(resalt):
			# for name in resalt:
				# for child in self.selection_set_model.AW_Master_Tree_Item.find_childern(name, column=0, role=ITEM_DATA_ROLE.FullNameRole):
					# self._previous_Selected_Items.append(child)
					# child.update()
					# if child._Item_Type_ID == Maya_Node_Tree_Item._Item_Type_ID:
						# for p in child.all_parents:
							# if not p in self._previous_Selected_Items:
								# self._previous_Selected_Items.append(p)
								# p.update()
		self.logger.debug("Exiting updateHighlightedItems_execute()")
	#----------------------------------------------------------------------
	def Before_Scene_Update_CB(self, clientData):
		'''
		Freeze the callbacks before the entire scene is being reloaded or cleared.
		Unfreezing the callbacks is handled in the afterSceneChangedCB.
		'''
		if clientData in ["BeforeImport", "BeforeReference", "BeforeLoadReference", "BeforeImportReference"]:
			self._disable_Update_For_Rescan_Add = True
			self.logger.info('Disable UI Update For Rescan Add: %s.' % (clientData) )
		elif clientData in ["BeforeRemoveReference", "BeforeUnloadReference", "BeforeLoadReference", "BeforeImportReference"]:
			self._disable_Update_For_Rescan_Remove = True
			self.logger.info('Disable UI Update For Rescan Remove: %s.' % (clientData) )
		self._disable_Update_UI_Stack.append(clientData)
	#----------------------------------------------------------------------		
	def After_Scene_Update_CB(self, clientData):
		'''The entire scene is being reloaded or cleared. Repopulate the entire widget.'''
		# Expect that beforeSceneUpdatedCB() was called before to push an item onto the stack
		self.logger.debug('runing After_Scene_Update_CB with clientData %r' % clientData)
		
		if self._disable_Update_For_Rescan_Add:
			self._disable_Update_For_Rescan_Add = False
			if clientData == "BeforeImport":
				self._update_on_file_imported()
		elif self._disable_Update_For_Rescan_Remove:
			self._disable_Update_For_Rescan_Remove = False
		
		if len(self._disable_Update_UI_Stack) > 0:
			disableUpdateItem = self._disable_Update_UI_Stack.pop()
			if disableUpdateItem != clientData:
				self.logger.warning('Unexpected item on "%s" disable_Update_UI_Stack. Expected "%s"' % (disableUpdateItem, clientData) )
			else:
				self.logger.info('Removed "%s" From The disable_Update_UI_Stack.' % (disableUpdateItem) )
		else:
			self.logger.info('No items to pop on disable_Update_UI_Stack. Expected beforeSceneUpdatedCB() to add one.')
	#----------------------------------------------------------------------
	def _update_on_file_imported(self):
		""""""
		master_set = self.selection_set_model.rootItem.child(0).get_internal_Data()
		imported_sets = [Util_API.SelectionSet(s) for s in cmds.ls(sets=True) if "AW_Master_Selection_Set" in s and s != "AW_Master_Selection_Set"]
		for imported_set in imported_sets:
			master_set.addElement(imported_set.children)
			imported_set.clear()
			imported_set.delete()
	#----------------------------------------------------------------------
	def _force_name_refresh(self):
		self.Selection_Set_Outliner_Tree_View.collapse(self.selection_set_model.rootItem.index)
		self.Selection_Set_Outliner_Tree_View.expand(self.selection_set_model.rootItem.index)
	#----------------------------------------------------------------------
	@QtSlot(bool)
	def show_Filter_Options_Window(self, value):
		""""""
		if value == True:
			y = self.Filter_Options_Button.mapToGlobal(self.Filter_Options_Button.pos()).y() + 30
			x = self.Filter_Options_Button.mapToGlobal(self.Filter_Options_Button.pos()).x() - self.Filter_Options_Button.pos().x() - self.Filter_Options_Widget.rect().center().x()
			self.Filter_Options_Widget.move(x, y)
			self.Filter_Options_Widget.setVisible(True)
			self.Filter_Options_Widget.show()
		else:
			self.Filter_Options_Widget.setVisible(False)
			self.Filter_Options_Widget.hide()		
#______________________________________________________________________________________________
_Maya_Node_Type_Icons = _Make_Maya_Node_Type_Icons()
ui_Loader.registerCustomWidget(Display_Option_Tool_Button)
ui_Loader.registerCustomWidget(Surface_Shader_Types_QComboBox)
ui_Loader.registerCustomWidget(Filter_Syntax_Options_ComboBox)
ui_Loader.registerCustomWidget(Filter_Case_Sensitivity_Options_ComboBox)
ui_Loader.registerCustomWidget(Filter_Scan_Options_ComboBox)
ui_Loader.registerCustomWidget(Tree_View)
ui_Loader.registerCustomWidget(Selection_Set_Tree_View)
ui_Loader.registerCustomWidget(List_View)
ui_Loader.registerCustomWidget(AW_Selection_Set_Editor)
ui_Loader.registerCustomWidget(Maya_QWidget)

def UI_LOADER():
	mayaMainWindowPtr = omui.MQtUtil.mainWindow()
	rootWidget = wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)
	found_children = rootWidget.findChildren(Scripts.UICls.mayaMixin.MayaQWidgetDockableMixin)
	if len(found_children):
		for found_child in found_children:
			if found_child.objectName() == "Selection_Set_Editor":
				return found_child
	
	file_path = os.path.dirname(__file__) + "\\\\AW_Selection_Set_Editor.ui"
	wig = ui_Loader.load(file_path)
	wig._run_setup()
	wig.show(dockable=True, floating=False, area='right', allowedArea='left right')
	return wig

