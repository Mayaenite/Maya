# script created by pymel.tools.mel2py from mel file:
# \\blue\app_config\deadline\DeadlineRepository6\submission\Maya\Main\SubmitMayaToDeadline.mel

import os
import math
import pymel.core as pm
import maya.cmds  as cmds
import maya.mel   as mel
import DeadLine_Access
import Job_Data_Model
import Helpers
reload(DeadLine_Access)
reload(Job_Data_Model)
reload(Helpers)
mydata = None
from functools import partial
try:
	import subprocess_original as subprocess
except:
	import subprocess

def addText(ui, val):
	ui.setText(ui.getText()+val)

def update_text_field(input_ui, output_ui, extra):
	output_ui.setText(os.path.join(input_ui.getText().strip(), extra).replace("\\", "/"))
	
def update_UI_Text_Persistent_Attribute(attrName, val):
	att = Helpers.AddStringAttribute(attrName, default="")
	att.set(val)
	
def update_UI_Option_Persistent_Attribute(attrName, val):
	att = Helpers.AddStringAttribute(attrName, default="")
	att.set(val)

#----------------------------------------------------------------------
def set_Current_Render_Layer(renderLayer):
	""""""
	pm.editRenderLayerGlobals(currentRenderLayer=renderLayer)

_defaultRenderGlobals = pm.PyNode("defaultRenderGlobals")
isinstance(_defaultRenderGlobals, pm.nodetypes.DependNode)
# ===============================================================================================================
# Globals
# ===============================================================================================================

#=================================================================
# SHOTGUN
class Shotgun_Globals:
	SGInfoKeys        = []
	SGInfoValues      = []


class UI_Globals(object):
	DeadlineSubmitterWindow           = "DeadlineSubmitWindow"
	MainTabLayout                     = "frw_mainTabLayout"
	ProjectPathGrp                    = "frw_projectPath"
	ImageOutputPathGrp                = "frw_outputFilePath"
	StartupScriptPathGrp              = "frw_startupScript"
	MentalRayFilenameGrp              = "frw_mentalRayFilePath"
	VRayFilenameGrp                   = "frw_vrayFilePath"
	LimitGroupGrp                     = "frw_limitGroups"
	DependenciesGrp                   = "frw_dependencies"
	MachineListGrp                    = "frw_machineList"
	JobNameGrp                        = "frw_JobName"
	MayaRenderOptionsRollout          = "frameLayout10"
	MayaRenderOptionsArnoldRollout    = "frameLayout11"
	MayaRenderOptionsMentalRayRollout = "frameLayout12"
	MayaRenderOptionsVRayRollout      = "frameLayout13"
	MayaRenderOptionsTileRollout      = "frameLayout14"
	MentalRayExportRollout            = "frameLayout15"
	MentalRayExportRenderJobRollout   = "frameLayout16"
	VrayExportRollout                 = "frameLayout17"
	VrayExportRenderJobRollout        = "frameLayout18"
	VrayExportVrimgJobRollout         = "frameLayout19"
	RendermanExportRollout            = "frameLayout20"
	RendermanExportRenderJobRollout   = "frameLayout21"
	ArnoldExportRollout               = "frameLayout22"
	ArnoldExportRenderJobRollout      = "frameLayout23"
	OverrideLayerSettingsDialog       = ""
	DeadlineRepositoryRoot            = ""
	ShotgunResultsBox                 = ""
	ShotgunDetailLabel                = "frw_ShotgunDetailLabel"
	UseShotgunCheckBox                = "frw_useShotgun"
	ShotgunVersion                    = "frw_ShotgunVersion"
	ShotgunDescription                = "frw_ShotgunDescription"
	SubmitDraftJob                    = "frw_submitDraftJob"
	UploadDraftToShotgun              = "frw_uploadDraftToShotgun"
	UseShotgunDataButton              = "frw_UseShotgunDataButton"
	DraftUser                         = "frw_DraftUser"
	DraftTemplate                     = "frw_DraftTemplate"
	DraftEntity                       = "frw_DraftEntity"
	DraftVersion                      = "frw_DraftVersion"
	DraftExtraArgs                    = "frw_DraftExtraArgs"
	VrayImageFormatMenu               = "vrayImageFormatMenu"
	ProgBar                           = "frw_progBar"
	SubmitEachCamera                  = "frw_submitEachCamera"
	IgnoreDefaultCameras              = "frw_ignoreDefaultCameras"
	UseMayaBatchPlugin                = "frw_useMayaBatchPlugin"
	Job_Strict_Error_Checking         = "frw_strictErrorChecking"
	LocalRendering                    = "frw_localRendering"
	MayaArgs                          = "frw_mayaArgs"
	TilesInX                          = "frw_tilesInX"
	TilesInY                          = "frw_tilesInY"
	SubmitTileSingleJob               = "frw_submitTileSingleJob"
	SubmitTileDependentJob            = "frw_submitTileDependentJob"
	SubmitTileCleanupJob              = "frw_submitTileCleanupJob"
	SubmitTileUseDraft                = "frw_submitTileUseDraft"
	SubmitTileErrorOnMissing          = "frw_submitTileErrorOnMissing"
	SubmitMentalRayJob                = "frw_submitMentalRayJob"
	MentalRayThreads                  = "frw_mentalRayThreads"
	MentalRayOffset                   = "frw_mentalRayOffset"
	MentalRayLocalRendering           = "frw_mentalRayLocalRendering"
	MentalRayArgs                     = "frw_mentalRayArgs"
	SubmitVRayJob                     = "frw_submitVRayJob"
	VrayThreads                       = "frw_vrayThreads"
	SubmitVrimg2ExrJob                = "frw_submitVrimg2ExrJob"
	Job_Delete_Vrimg_Files            = "frw_deleteVrimgFiles"
	ExportPRManThreads                = "frw_exportPRManThreads"
	SubmitPRManJob                    = "frw_submitPRManJob"
	PrmanThreads                      = "frw_prmanThreads"
	PrmanArgs                         = "frw_prmanArgs"
	SubmitArnoldJob                   = "frw_submitArnoldJob"
	ArnoldThreads                     = "frw_arnoldThreads"
	ArnoldArgs                        = "frw_arnoldArgs"
	JobName                           = "frw_JobName"
	JobComment                        = "frw_JobComment"
	Department                        = "frw_Department"
	Group                             = "frw_Group"
	DeadlinePool                      = "frw_deadlinePool"
	JobPriority                       = "frw_JobPriority"
	LimitCount                        = "frw_LimitCount"
	ConcurrentTasks                   = "frw_ConcurrentTasks"
	SlaveTimeout                      = "frw_SlaveTimeout"
	MinSlaveTimeout                   = "frw_MinSlaveTimeout"
	LimitGroups                       = "frw_limitGroups"
	MachineList                       = "frw_machineList"
	IsBlacklist                       = "frw_isBlacklist"
	SubmitAsSuspended                 = "frw_submitAsSuspended"
	FrameGroup                        = "frw_FrameGroup"
	SubmitMayaScene                   = "frw_submitMayaScene"
	VrayAutoMemoryEnabled             = "frw_vrayAutoMemoryEnabled"
	VrayAutoMemoryBuffer              = "frw_vrayAutoMemoryBuffer"
	MayaJobType                       = "frw_mayaJobType"
	MayaRenderJobType                 = 1
	MentalRayExportJobType            = 2
	VRayExportJobType                 = 3
	RendermanExportJobType            = 4
	ArnoldExportJobType               = 5

########################################################################
def GetTileOutputPrefix(outputPrefix,x,y,xCount,yCount):
	path=os.path.dirname(outputPrefix)
	if path != "":
		path=path + "/"

	base=str(pm.mel.basename(outputPrefix, ""))
	tile="_tile_" + str(x) + "x" + str(y) + "_" + str(xCount) + "x" + str(yCount) + "_"
	return path + tile + base

def GetMayaOutputPrefix(currCamera):
	prefix=""
	# Source a CustomOutputPrefix.mel file, if it exists.
	outputPrefixPath=str(CheckSlashes(UI_Globals.DeadlineRepositoryRoot + "/submission/Maya/CustomOutputPrefix.mel"))
	if cmds.file(outputPrefixPath,q=1,exists=1):
		print "sourcing custom outputprefix file: " + outputPrefixPath + "\n"
		pm.mel.eval("source \"" + outputPrefixPath + "\";")
		prefix=str(pm.mel.GetCustomMayaOutputPrefix(currCamera))


	else:
		renderer=str(Helpers.Data_Access.currentRenderer)
		if renderer != "vray":
			prefix=str(pm.getAttr('defaultRenderGlobals.imageFilePrefix'))


		else:
			prefix=str(pm.getAttr('vraySettings.fileNamePrefix'))

		if prefix == "":
			prefix=str(Helpers.Data_Access.StrippedSceneFileName)


	return prefix

def IsDefaultCamera(cameraName):
	if cameraName in ["front","frontShape","persp","perspShape","side","sideShape","top","topShape"]:
		return True
	else:
		return False

def IsCameraRenderable(cameraName):
	#print "Checking if camera is renderable: " + cameraName + "\n"
	if not cmds.objectType(cameraName,isType="camera"):
		relatives=cmds.listRelatives(cameraName,s=True)
		cameraName=relatives[0]

	cameraRenderable=0
	if cmds.attributeQuery( "renderable",node=cameraName, exists=True ):
		cameraRenderable=int(pm.getAttr(cameraName + ".renderable"))

	return cameraRenderable

# Opens the mental ray export settings dialog.
def OpenExportSettings(*args):
	pm.mel.fileOptions("ExportAll", "projectViewer ExportAll")
# Launches the Maya online help
def OnlineHelp():
	DeadLine_Access.Start_Process("http://www.thinkboxsoftware.com/support/")
#--------------------------------------------------------
# Utility Functions
# --------------------------------------------------------
# Waits for a fixed amount of time (in milliseconds)
def Wait(waitTime):
	startTime=cmds.timerX()
	while cmds.timerX(startTime=startTime) * 1000<waitTime:
		pass
		""" Do nothing... weeeee! """

# Ensures that all slashes are consistant throughout the filename.
def CheckSlashes(filename):
	result=filename
	newResult=''
	newResult=result.replace("\\\\","/")

	while newResult != result:
		result=newResult
		newResult=result.replace("\\\\","/")

	result=newResult

	newResult=result.replace("//","/")

	while newResult != result:
		result=newResult
		newResult=result.replace("//","/")

	if newResult.startswith("/"):
		newResult="/" + newResult

	return newResult
# Returns true if the path is on the c:, d:, or e:.
def IsLocalDrive(path):
	return os.path.splitdrive(path)[0] != ""

class Layer_Settings_Dialog(object):
	def __init__(self, ui):
		isinstance(ui, SubmitToDeadLine_UI)
		self.renderLayerList_val = pm.ls(exactType="renderLayer")
		self.chunkSize_val       = iu.FrameGroup.getValue()
		self.jobName_val         = ui.JobNameGrp.getText()
		# Add controls to the submission dialog.
		self.windowWidth=470
		self.windowHeight=500
		self.labelWidth=110
		self.controlWidth=320
		# Get the dialog's formLayout.
		#
		form=str(pm.setParent(q=1))
		pm.formLayout(form, width=(self.windowWidth + 8),e=1,height=self.windowHeight)
		window=str(pm.formLayout(form,q=1,p=1))
		print form + "\n"
		mainScrollLayout = pm.scrollLayout(width=self.windowWidth,horizontalScrollBarThickness=0)
		pm.columnLayout(adjustableColumn=True,columnAttach=("both", 0))
		# Store the currently selected render layer
		currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
		for i in range(0,len(self.renderLayerList_val)):
			isReferenceLayer=int(pm.referenceQuery(inr=self.renderLayerList_val[i]))
			# Only submit if layer is not referenced.
			if not isReferenceLayer:
				renderable=int(pm.getAttr(self.renderLayerList_val[i] + ".renderable"))
				# Submit only if the renderable attribute is on
				if renderable:
					if not pm.catch( lambda: pm.editRenderLayerGlobals(currentRenderLayer=self.renderLayerList_val[i]) ):
						frameRange=str(pm.textFieldGrp('frw_FrameList',q=1,text=1))
						frameRangeEnabled=int(Helpers.Data_Access.IsAnimatedOn)
						pm.frameLayout(borderStyle="etchedIn",collapsable=True,labelVisible=True,borderVisible=True,label=self.renderLayerList_val[i])
						pm.columnLayout(adj=True,columnAttach=("both", 0),rowSpacing=4)
						layerJobName=self.jobName_val + " - " + self.renderLayerList_val[i]
						FieldName="frw_JobName_" + self.renderLayerList_val[i]
						pm.textFieldGrp(FieldName,
						                text=layerJobName,cw2=(self.labelWidth, 320),label="Job Name",changeCommand=lambda *args: Old_SavePersistentDeadlineOptions(),annotation="The name of the job",cl2=("left", "left"))
						FieldName="frw_FrameList_" + self.renderLayerList_val[i]
						pm.textFieldGrp(FieldName,
						                en=frameRangeEnabled,text=frameRange,cw2=(self.labelWidth, 320),label="Frame List",changeCommand=lambda *args: Old_SavePersistentDeadlineOptions(),annotation="Enter a list of frames to render, seperated by commas for seperate frames, or dashes for continuous sequences of frames. e.g. 1, 5-10, 100",cl2=("left", "left"))
						FieldName="frw_FrameGroup_" + self.renderLayerList_val[i]
						pm.intSliderGrp(FieldName,
						                v=self.chunkSize_val,maxValue=1000,minValue=1,field=True,changeCommand=lambda *args: Old_SavePersistentDeadlineOptions(),cal=(1, "left"),label="Task Size",cw=(1, self.labelWidth),annotation="Each task for the job will consist of this many frames")
						pm.setParent('..')
						pm.setParent('..')




		pm.editRenderLayerGlobals(currentRenderLayer=currentRenderLayer)
		# Reselect the current render layer
		pm.setParent('..')
		pm.setParent('..')
		buttonColumnLayout = pm.columnLayout(adj=True,columnAttach=("both", 2),rowSpacing=4)
		pm.rowLayout(numberOfColumns=2,cw2=((self.windowWidth / 2), (self.windowWidth / 2)))
		self.Submit_Job_Button = pm.button(c=lambda *args: SetupSubmission(),align="center",height=26,width=(self.windowWidth / 2 - 4),label="Submit Job",annotation="Submits this job to Deadline")
		pm.button(c=lambda *args: DismissLayoutDialog(),align="center",height=26,width=(self.windowWidth / 2 - 4),label="Close",annotation="Closes this window")
		pm.setParent('..')
		pm.setParent('..')
		pm.formLayout(form,
		              ac=(mainScrollLayout, 'bottom', 0, buttonColumnLayout),
		              e=1,af=[(buttonColumnLayout, 'bottom', 0), (buttonColumnLayout, 'right', 0), (buttonColumnLayout, 'left', 0), (mainScrollLayout, 'top', 0), (mainScrollLayout, 'left', 3)])
#----------------------------------------------------------------------
def LayerSettingsDialog(*args):
	renderLayerList=pm.ls(exactType="renderLayer")
	chunkSize=int(pm.intSliderGrp(UI_Globals.FrameGroup,q=1,v=1))
	jobName=str(pm.mel.attributeExists('deadlineJobName', 'defaultRenderGlobals') and pm.getAttr('defaultRenderGlobals.deadlineJobName') or Helpers.Data_Access.StrippedSceneFileName)
	# Add controls to the submission dialog.
	windowWidth=470
	windowHeight=500
	labelWidth=110
	controlWidth=320
	# Get the dialog's formLayout.
	#
	form=str(pm.setParent(q=1))
	pm.formLayout(form,width=(windowWidth + 8),e=1,height=windowHeight)
	window=str(pm.formLayout(form,q=1,p=1))
	print form + "\n"
	mainScrollLayout = pm.scrollLayout(width=windowWidth,horizontalScrollBarThickness=0)
	pm.columnLayout(adjustableColumn=True,columnAttach=("both", 0))
	# Store the currently selected render layer
	currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
	for i , layer in enumerate(renderLayerList):
		# Only submit if layer is not referenced.
		if not layer.isReferenced():
			# Submit only if the renderable attribute is on
			if layer.renderable.get():
				layer.setCurrent()
				frameRange=UI_Globals.FrameListGrp.getText()
				frameRangeEnabled=int(Helpers.Data_Access.IsAnimatedOn)
				pm.frameLayout(borderStyle="etchedIn",collapsable=True,labelVisible=True,borderVisible=True,label=layer.name())
				pm.columnLayout(adj=True,columnAttach=("both", 0),rowSpacing=4)
				layerJobName=jobName + " - " + layer.name()
				FieldName="frw_JobName_" + layer.name()
				pm.textFieldGrp(FieldName,text=layerJobName,cw2=(labelWidth, 320),label="Job Name",changeCommand=lambda *args: Old_SavePersistentDeadlineOptions(),annotation="The name of the job",cl2=("left", "left"))
				FieldName="frw_FrameList_" + layer.name()
				pm.textFieldGrp(FieldName,en=frameRangeEnabled,text=frameRange,cw2=(labelWidth, 320),label="Frame List",changeCommand=lambda *args: Old_SavePersistentDeadlineOptions(),annotation="Enter a list of frames to render, seperated by commas for seperate frames, or dashes for continuous sequences of frames. e.g. 1, 5-10, 100",cl2=("left", "left"))
				FieldName="frw_FrameGroup_" + layer.name()
				pm.intSliderGrp(FieldName,v=chunkSize,maxValue=1000,minValue=1,field=True,changeCommand=lambda *args: Old_SavePersistentDeadlineOptions(),cal=(1, "left"),label="Task Size",cw=(1, labelWidth),annotation="Each task for the job will consist of this many frames")
				pm.setParent('..')
				pm.setParent('..')




	pm.editRenderLayerGlobals(currentRenderLayer=currentRenderLayer)
	# Reselect the current render layer
	pm.setParent('..')
	pm.setParent('..')
	buttonColumnLayout = pm.columnLayout(adj=True,columnAttach=("both", 2),rowSpacing=4)
	pm.rowLayout(numberOfColumns=2,cw2=((windowWidth / 2), (windowWidth / 2)))
	pm.button(c=SetupSubmission,align="center",height=26,width=(windowWidth / 2 - 4),label="Submit Job",annotation="Submits this job to Deadline")
	pm.button(c=DismissLayoutDialog,align="center",height=26,width=(windowWidth / 2 - 4),label="Close",annotation="Closes this window")
	pm.setParent('..')
	pm.setParent('..')
	pm.formLayout(form,ac=(mainScrollLayout, 'bottom', 0, buttonColumnLayout),
	              e=1,af=[(buttonColumnLayout, 'bottom', 0), (buttonColumnLayout, 'right', 0), (buttonColumnLayout, 'left', 0), (mainScrollLayout, 'top', 0), (mainScrollLayout, 'left', 3)])
#---------------------------------------------------------
# Event handler functions.
#---------------------------------------------------------
def DismissLayoutDialog(*args):
	pm.layoutDialog(dismiss="")
#----------------------------------------------------------------------
def add_menu_items(items):
	""""""
	res = []
	for item in items:
		m = pm.menuItem(label=item)
		res.append(m)
	return res
# ===============================================================================================================
# The main function called by the Maya proxy script
# ===============================================================================================================
########################################################################
class SubmitToDeadLine_UI(UI_Globals):

	def __init__(self):
		self._PD                  = Persistent_Data_Access(self)
		self.defaultRenderGlobals = _defaultRenderGlobals
		self.Data_Access          = Helpers.Data_Access_Uitls()
		self.frame_range          = Helpers.Frame_Range()
		self._UI                  = UI_Data_Access(self)
		Helpers.AddStringAttribute("imageNamePrefix")
		UI_Globals.DeadlineRepositoryRoot = DeadLine_Access.RepositoryRoot()
		
		self.regionRendering_val          = False
		self.mayaBuildEnabled_val         = True

		# Get the frame range.
		Shotgun_Globals.SGInfoKeys=self.defaultRenderGlobals.deadlineSGInfoKeys.get([])
		Shotgun_Globals.SGInfoValues=self.defaultRenderGlobals.deadlineSGInfoValues.get([])

		# Read in maximum priority.
		self.maximumPriority_val = DeadLine_Access.Get_MaximumPriority()
		if self.maximumPriority_val == 0:
			self.maximumPriority_val=100
		
		# Get if layers are enabled

		if pm.window(str(UI_Globals.DeadlineSubmitterWindow), exists=True):
			pm.deleteUI(str(UI_Globals.DeadlineSubmitterWindow), window=True)
			# Create a new submission dialog window.
		self.halfFramesEnabled_val= self.Data_Access.ShowHalfFramesOption
		# Add controls to the submission dialog.
		self.windowWidth=800
		self.windowHeight=1200
		self.labelWidth=110
		self.controlWidth=320

		mainTopLeft = pm.window('MayaWindow',q=1,topLeftCorner=1)

		self._main_window = pm.window(UI_Globals.DeadlineSubmitterWindow,
		                              sizeable=True,
		                              title="Submit Job To Deadline",
		                              topLeftCorner=[mainTopLeft[0] + 50, mainTopLeft[1] + 50],
		                              height=self.windowWidth + 8, 
		                              resizeToFitChildren=True)
		isinstance(self._main_window, pm.uitypes.Window)
		UI_Globals.DeadlineSubmitterWindow = self._main_window
		isinstance(UI_Globals.DeadlineSubmitterWindow, pm.uitypes.Window)
		isinstance(self.DeadlineSubmitterWindow, pm.uitypes.Window)
		if pm.windowPref(str(UI_Globals.DeadlineSubmitterWindow), exists=True):
			# reset preference
			# Get the location of the main window.
			pm.windowPref(str(UI_Globals.DeadlineSubmitterWindow), remove=True)

		mainFormLayout = pm.formLayout('mainFormLayout',
		                               width=(self.windowWidth + 16),
		                               numberOfDivisions=100)
		isinstance(mainFormLayout, pm.uitypes.FormLayout)

		mainScrollLayout = pm.scrollLayout('mainScrollLayout',
		                                   width=(self.windowWidth + 8),
		                                   horizontalScrollBarThickness=0,
		                                   childResizable=True)
		isinstance(mainScrollLayout, pm.uitypes.ScrollLayout)
		UI_Globals.MainScrollLayout = mainScrollLayout
		isinstance(self.MainScrollLayout, pm.uitypes.ScrollLayout)
		MainTabLayout = pm.tabLayout(UI_Globals.MainTabLayout, childResizable=True)
		isinstance(MainTabLayout, pm.uitypes.TabLayout)
		UI_Globals.MainTabLayout = MainTabLayout
		isinstance(self.MainTabLayout, pm.uitypes.TabLayout)

		mayaTabLayout = pm.columnLayout('mayaTabLayout',
		                                adjustableColumn=True,
		                                columnAttach=("both", 4))
		isinstance(mayaTabLayout, pm.uitypes.ColumnLayout)
		###########################################################################
		# JOB DESCRIPTION
		###########################################################################
		self.Build_Job_Description_Frame()		
		#scan_up_parents(2)
		pm.setParent(mayaTabLayout)
		###########################################################################
		# JOB SCHEDULING
		###########################################################################
		self.Build_Job_Scheduling_Frame()
		#scan_up_parents(3)
		pm.setParent(mayaTabLayout)
		###########################################################################
		# RENDER OPTIONS
		###########################################################################
		self.build_Render_Options_Frame()
		###########################################################################
		# MAYA RENDER JOB
		###########################################################################
		self.Build_Maya_Render_Job_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# ARNOLD OPTIONS
		###########################################################################
		self.Build_Arnold_Options_Frame()
		#scan_up_parents(2)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# MENTAL RAY OPTIONS
		###########################################################################
		self.Build_Mental_Ray_Options_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# VRAY OPTIONS
		###########################################################################
		self.Build_VRay_Options_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# TILE RENDERING
		###########################################################################
		self.Build_Tile_Rendering_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# MENTAL RAY EXPORT JOB
		###########################################################################
		self.Build_Mental_Ray_Export_Job_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# MENTAL RAY RENDER JOB
		###########################################################################
		self.Build_Mental_Ray_Render_Job_Frame()
		#scan_up_parents(2)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# VRAY EXPORT JOB
		###########################################################################
		self.Build_VRay_Export_Job_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# VRAY RENDER JOB
		###########################################################################
		self.Build_VRay_Render_Job_Frame()
		#scan_up_parents(2)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# VRIMG2EXR CONVERSION JOB
		###########################################################################
		self.Build_Vrimg2Exr_Conversion_Job_Frame()
		#scan_up_parents(2)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# VRIMG2EXR CONVERSION OPTIONS
		###########################################################################
		self.Build_Vrimg2Exr_Conversion_Options_Frame()
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# RENDERMAN EXPORT JOB
		###########################################################################
		self.Build_Renderman_Export_Job_Frame()
		#scan_up_parents(2)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# PRMAN RENDER JOB
		###########################################################################
		self.Build_PRMan_Render_Job_Frame()
		#scan_up_parents(2)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# ARNOLD EXPORT JOB
		###########################################################################
		self.Build_Arnold_Export_Job_Frame()
		#scan_up_parents(3)
		pm.setParent(self.render_options_column_layout)
		###########################################################################
		# ARNOLD RENDER JOB
		###########################################################################
		self.Build_Arnold_Render_Job_Frame()
		#p = scan_up_parents(3)
		pm.setParent(MainTabLayout)

		###########################################################################
		# SHOTGUN
		###########################################################################
		self.Build_Shotgun_Tab()
		pm.setParent(self.shotgun_tab_layout)
		#temp = scan_up_parents(3)
		###########################################################################
		# DRAFT
		###########################################################################
		self.Build_Draft_Frame()
		pm.setParent(mainFormLayout)
		#temp = scan_up_parents(6)
		self.On_User_DraftChanged()
		MainTabLayout.setTabLabel(['mayaTabLayout', "Maya"])
		MainTabLayout.setTabLabel([self.shotgun_tab_layout, "Shotgun/Draft"])
		buttonColumnLayout = pm.columnLayout('buttonColumnLayout',
		                                     adjustableColumn=True,
		                                     columnAttach=("both", 4),
		                                     rowSpacing=4)
		pm.rowLayout(numberOfColumns=5,
		             cw5=(75, 105, 105, 105, 105))

		ProgBar = pm.progressBar(UI_Globals.ProgBar,
		                         width=65,
		                         annotation="Deadline Submission Progress",
		                         minValue=0,
		                         maxValue=100,
		                         height=26)
		isinstance(ProgBar, pm.uitypes.ProgressBar)
		UI_Globals.ProgBar = ProgBar

		bnt_GlobalsButton = pm.button('frw_GlobalsButton',width=95,c=lambda *args: pm.mel.unifiedRenderGlobalsWindow(),height=26,annotation="Opens the Maya Render Globals Dialog",label="Render Globals...")
		pm.button(width=95,c=lambda *args: pm.ProjectWindow(),height=26,annotation="Opens the Maya Edit Project Dialog",label="Edit Project...")
		pm.button(width=95,c=lambda *args: OnlineHelp(),height=26,annotation="Opens the Online Help page in the Default Web Browser",label="Online Help...")
		self.Submit_Job_Button = pm.button(width=95,c=self.DeadlineSubmitterOnOk,height=26,annotation="Submits this job to Deadline",label="Submit Job")
		pm.setParent('..')
		pm.setParent('..')
		mainFormLayout.attachControl('mainScrollLayout', 'bottom', 5, buttonColumnLayout)
		mainFormLayout.attachForm(buttonColumnLayout, 'bottom', 5)
		mainFormLayout.attachForm(buttonColumnLayout, 'left', 5)
		mainFormLayout.attachForm('mainScrollLayout', 'top', 5)
		mainFormLayout.attachForm('mainScrollLayout', 'left', 5)
		mainFormLayout.attachForm('mainScrollLayout', 'right', 5)
		self._PD.SavePersistentDeadlineOptions()
		self.UpdateJobType()

		# Add Text Field Changed Commands
		self.ImageOutputPathGrp.textChangedCommand(lambda *args:update_text_field(self.ImageOutputPathGrp, self.VRay_File_Name,"<Layer>/<Layer>"))
		# Show the submission dialog window.
		##cmds.scriptJob( parent='DeadlineSubmitWindow', attributeChange=['defaultRenderGlobals.currentRenderer', self.UpdateJobType] )
		pm.showWindow('DeadlineSubmitWindow')
	#----------------------------------------------------------------------
	def Build_Job_Description_Frame(self):
		""""""

		self.Job_Description_frame = pm.frameLayout(borderStyle="etchedIn",
		                                            collapsable=True,
		                                            labelVisible=True,
		                                            borderVisible=True,
		                                            label="Job Description")
		isinstance(self.Job_Description_frame, pm.uitypes.FrameLayout)
		UI_Globals.Job_Description_frame = self.Job_Description_frame

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		self.JobNameGrp = pm.textFieldButtonGrp("frw_JobName",
		                                        text=Helpers.Data_Access.StrippedSceneFileName,
		                                        label="Job Name",
		                                        #changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                        columnAlign=(1, "left"),
		                                        annotation="The name of the job (press '<' button to use the scene file name)",
		                                        columnWidth=[(1, self.labelWidth), (2, 300)],
		                                        rowAttach=[1,"both",1],
		                                        adjustableColumn=2,
		                                        buttonCommand=self.SetJobName,
		                                        buttonLabel="<")
		isinstance(self.JobNameGrp, pm.uitypes.TextFieldButtonGrp)
		self.JobNameGrp.textChangedCommand(partial(update_UI_Text_Persistent_Attribute,"deadlineJobName"))
		
		UI_Globals.JobNameGrp = self.JobNameGrp

		self.Job_Comment_Grp = pm.textFieldGrp(UI_Globals.JobComment,
		                                       text=self.defaultRenderGlobals.deadlineJobComment.get(""),
		                                       columnWidth2=(self.labelWidth, 320),
		                                       label="Comment",
		                                       #changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                       annotation="A brief comment about the job",
		                                       rowAttach=[1,"both",1],
		                                       adjustableColumn=2,
		                                       columnAlign2=("left", "left"))
		isinstance(self.Job_Comment_Grp, pm.uitypes.TextFieldGrp)
		self.Job_Comment_Grp.textChangedCommand(partial(update_UI_Text_Persistent_Attribute,"deadlineJobComment"))
		UI_Globals.JobComment = self.Job_Comment_Grp

		self.Job_Department_Grp = pm.textFieldGrp(UI_Globals.Department,
		                                          text=self.defaultRenderGlobals.deadlineDepartment.get(""),
		                                          columnWidth2=(self.labelWidth, 320),
		                                          rowAttach=[1,"both",1],
		                                          adjustableColumn=2,
		                                          label="Department",
		                                          #changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                          annotation="The department the job (or the job's user) belongs to",
		                                          columnAlign2=("left", "left"))
		isinstance(self.Job_Department_Grp, pm.uitypes.TextFieldGrp)
		self.Job_Department_Grp.textChangedCommand(partial(update_UI_Text_Persistent_Attribute, "deadlineDepartment"))
		UI_Globals.Department = self.Job_Department_Grp
	#----------------------------------------------------------------------
	def Build_Job_Scheduling_Frame(self):
		""""""		
		self.Job_Scheduling_Frame = pm.frameLayout("Job_Scheduling_Frame",
		                                           borderStyle="etchedIn",
		                                           collapsable=True,
		                                           labelVisible=True,
		                                           borderVisible=True,
		                                           label="Job Scheduling")
		isinstance(self.Job_Scheduling_Frame, pm.uitypes.FrameLayout)

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		self.Job_Pools = pm.optionMenuGrp(UI_Globals.DeadlinePool,
		                                  annotation="The pool the job belongs to",
		                                  columnWidth2=(self.labelWidth, 160),
		                                  #changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                  columnAlign2=("left", "left"),
		                                  rowAttach=[1,"both",1],
		                                  adjustableColumn=2,
		                                  label="Pool")
		menus = add_menu_items(self.Data_Access.deadline_pools)	
		isinstance(self.Job_Pools, pm.uitypes.OptionMenuGrp)
		self.Job_Pools.changeCommand(partial(update_UI_Option_Persistent_Attribute,"deadlineJobPool"))
		
		UI_Globals.DeadlinePool = self.Job_Pools
		self.Job_Pools.setSelect(self.Data_Access.deadline_pools.index(self._PD.deadlineJobPool.get())+1)
		
		self.Secondary_Job_Pools = pm.optionMenuGrp("frw_deadlineSecondaryPool",
		                                            annotation="The secondary pool lets you specify a Pool to use if the primary Pool does not have any available Slaves",
		                                            columnWidth2=(self.labelWidth, 160),
		                                            #changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            columnAlign2=("left", "left"),
		                                            rowAttach=[1,"both",1],
		                                            adjustableColumn=2,
		                                            label="Secondary Pool")
		add_menu_items(self.Data_Access.deadline_pools)
		self.Secondary_Job_Pools.setSelect(self.Data_Access.deadline_pools.index(self._PD.deadlineJobSecondaryPool.get())+1)
		isinstance(self.Secondary_Job_Pools, pm.uitypes.OptionMenuGrp)
		UI_Globals.Secondary_Job_Pools = self.Secondary_Job_Pools	

		self.Job_Goups = pm.optionMenuGrp(UI_Globals.Group,
		                                  annotation="The group the job belongs to",
		                                  columnWidth2=(self.labelWidth, 320),
		                                  rowAttach=[1,"both",1],
		                                  adjustableColumn=2,		                             
		                                  changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                  columnAlign2=("left", "left"),label="Group")
		add_menu_items(self.Data_Access.deadline_groups)
		isinstance(self.Job_Goups, pm.uitypes.OptionMenuGrp)
		self.Job_Goups.setSelect(self.Data_Access.deadline_groups.index(self._PD.deadlineGroup.get())+1)
		UI_Globals.Group = self.Job_Goups

		self.Job_Priority = pm.intSliderGrp(UI_Globals.JobPriority,
		                                    value=self.defaultRenderGlobals.deadlineJobPriority.get(50),
		                                    maxValue=self.maximumPriority_val,
		                                    minValue=0,
		                                    field=True,
		                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                    columnAlign=(1, "left"),
		                                    label="Priority",
		                                    columnWidth=(1, self.labelWidth),
		                                    annotation="The job's priority (0 is the lowest, 100 is the highest)")
		isinstance(self.Job_Priority, pm.uitypes.IntSliderGrp)
		UI_Globals.JobPriority     = self.Job_Priority

		self.Job_Limit_Count      = pm.intSliderGrp(UI_Globals.LimitCount,
		                                            value=self.defaultRenderGlobals.deadlineLimitCount.get(0),
		                                            maxValue=1000,
		                                            minValue=0,
		                                            field=True,
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            columnAlign=(1, "left"),
		                                            label="Machine Limit",
		                                            columnWidth=(1, self.labelWidth),
		                                            annotation="Limit the number of machines that can render this job concurrently (specify 0 for no machine limit)")
		isinstance(self.Job_Limit_Count, pm.uitypes.IntSliderGrp)
		UI_Globals.LimitCount      = self.Job_Limit_Count



		self.Job_Concurrent_Tasks = pm.intSliderGrp(UI_Globals.ConcurrentTasks,
		                                            value=self.defaultRenderGlobals.deadlineConcurrentTasks.get(1),
		                                            maxValue=16,
		                                            minValue=1,
		                                            field=True,
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            columnAlign=(1, "left"),
		                                            label="Concurrent Tasks",
		                                            columnWidth=(1, self.labelWidth),
		                                            annotation="The number of tasks a slave can dequeue for this job simultaneously")
		isinstance(self.Job_Concurrent_Tasks, pm.uitypes.IntSliderGrp)
		UI_Globals.ConcurrentTasks = self.Job_Concurrent_Tasks

		self.Job_Slave_Timeout    = pm.intSliderGrp(UI_Globals.SlaveTimeout,
		                                            value=self.defaultRenderGlobals.deadlineSlaveTimeout.get(0),
		                                            maxValue=5000,
		                                            minValue=0,
		                                            field=True,
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            columnAlign=(1, "left"),
		                                            label="Task Timeout",
		                                            columnWidth=(1, self.labelWidth),
		                                            annotation="The number of minutes a slave has to render an individual task before timing out (specify 0 for no limit)")
		isinstance(self.Job_Slave_Timeout, pm.uitypes.IntSliderGrp)
		UI_Globals.SlaveTimeout= self.Job_Slave_Timeout


		self.Job_Min_Slave_Timeout = pm.intSliderGrp(UI_Globals.MinSlaveTimeout,
		                                             value=self.defaultRenderGlobals.deadlineMinSlaveTimeout.get(0),
		                                             maxValue=5000,
		                                             minValue=0,
		                                             field=True,
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             columnAlign=(1, "left"),
		                                             label="Minimum Task Time",
		                                             columnWidth=(1, self.labelWidth),
		                                             annotation="The minimum number of minutes a slave should render a task for, otherwise an error will be reported (specify 0 for no minimum)")
		isinstance(self.Job_Min_Slave_Timeout, pm.uitypes.IntSliderGrp)
		UI_Globals.MinSlaveTimeout = self.Job_Min_Slave_Timeout



		self.Job_Limit_Groups   = pm.textFieldButtonGrp(UI_Globals.LimitGroups,
		                                                text=self.defaultRenderGlobals.deadlineLimitGroups.get(""),
		                                                label="Limit Groups",
		                                                changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                buttonCommand=self.user_Input_Limit_Groups_Dialog, 
		                                                columnAlign=(1, "left"),
		                                                annotation="The limit groups that this job requires.",
		                                                columnWidth=[(1, self.labelWidth), (2, 300)],
		                                                rowAttach=[1,"both",1],
		                                                adjustableColumn=2,		                                        
		                                                buttonLabel="...")
		isinstance(self.Job_Limit_Groups, pm.uitypes.TextFieldButtonGrp)
		UI_Globals.LimitGroupGrp   = self.Job_Limit_Groups

		#int $deleteOnComplete = `attributeExists deadlineDeleteOnComplete defaultRenderGlobals` ? `getAttr defaultRenderGlobals.deadlineDeleteOnComplete` : false;


		self.Job_Dependencies_List= pm.textFieldButtonGrp('frw_dependencies',
		                                                  text=self.defaultRenderGlobals.deadlineDependinceList.get(""),
		                                                  label="Dependencies",
		                                                  changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                  buttonCommand=self.user_Input_Dependencies_Dialog, 
		                                                  columnAlign=(1, "left"),
		                                                  annotation="The jobs that this job is dependent on.",
		                                                  columnWidth=[(1,self.labelWidth), (2, 300)],
		                                                  rowAttach=[1,"both",1],
		                                                  adjustableColumn=2,
		                                                  buttonLabel="...")
		isinstance(self.Job_Dependencies_List, pm.uitypes.TextFieldButtonGrp)
		UI_Globals.DependenciesGrp = self.Job_Dependencies_List



		self.Job_Machines_List = pm.textFieldButtonGrp(UI_Globals.MachineList,
		                                               text=self.defaultRenderGlobals.deadlineMachineList.get(""),
		                                               label="Machine List",
		                                               changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                               columnAlign=(1, "left"),
		                                               annotation="The whitelist or blacklist for the job.",
		                                               columnWidth=[(1, self.labelWidth), (2, 300)],
		                                               buttonCommand=self.user_Input_Machine_List_Dialog,
		                                               rowAttach=[1,"both",1],
		                                               adjustableColumn=2,
		                                               buttonLabel="...")
		isinstance(self.Job_Machines_List, pm.uitypes.TextFieldButtonGrp)
		UI_Globals.MachineListGrp = self.Job_Machines_List

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=((160 + self.labelWidth), 160),
		             columnAttach2=("left", "left"))

		self.Job_On_Complete=pm.optionMenuGrp('frw_onComplete',
		                                      annotation="What to do with the job after it completes.",
		                                      columnWidth2=(self.labelWidth, 160),
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      columnAlign2=("left", "left"),
		                                      label="On Complete")
		add_menu_items("Nothing Archive Delete".split())
		self.Job_On_Complete.setSelect("Nothing Archive Delete".split().index(self._PD.deadlineJobOnCompleat.get())+1)
		isinstance(self.Job_On_Complete, pm.uitypes.OptionMenuGrp)

		self.Job_Is_Blacklist = pm.checkBox(UI_Globals.IsBlacklist,
		                                    value=self.defaultRenderGlobals.deadlineIsBlacklist.get(False),
		                                    annotation="If checked, the machine list will be a blacklist. Otherwise, it is a whitelist.",
		                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                    label="Machine List is a Blacklist")
		isinstance(self.Job_Is_Blacklist, pm.uitypes.CheckBox)
		UI_Globals.IsBlacklist = self.Job_Is_Blacklist

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(self.labelWidth, 158),
		             columnAttach2=("left", "left"))

		pm.text('frw_dummySubmitSuspendedLabel',
		        align="left",
		        label="")

		self.Job_Submit_As_Suspended = pm.checkBox(UI_Globals.SubmitAsSuspended,
		                                           value=self.defaultRenderGlobals.deadlineSubmitAsSuspended.get(False),
		                                           annotation="If checked, this job will be submitted in the suspended state",
		                                           changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                           label="Submit As Suspended")
		isinstance(self.Job_Submit_As_Suspended, pm.uitypes.CheckBox)
		UI_Globals.SubmitAsSuspended = self.Job_Submit_As_Suspended
	#----------------------------------------------------------------------
	def build_Render_Options_Frame(self):
		""""""
		pm.frameLayout(borderStyle="etchedIn",
		               collapsable=True,
		               labelVisible=True,
		               borderVisible=True,
		               label="Render Options")

		self.render_options_column_layout = pm.columnLayout(adjustableColumn=True,
		                                                    columnAttach=("both", 4),
		                                                    rowSpacing=4)

		self.FrameListGrp = pm.textFieldGrp('frw_FrameList',
		                                    en=self.defaultRenderGlobals.deadlineOverrideLayerSettings.get(False) and Helpers.Data_Access.IsAnimatedOn and self.defaultRenderGlobals.deadlineSubmitEachRenderLayer.get(True),
		                                    text=self.defaultRenderGlobals.deadlineFramesList.get(""),
		                                    columnWidth2=(self.labelWidth, 320),
		                                    label="Frame List",
		                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                    annotation="Enter a list of frames to render, seperated by commas for seperate frames, or dashes for continuous sequences of frames. e.g. 1, 5-10, 100",
		                                    columnAlign2=("left", "left"))
		isinstance(self.FrameListGrp, pm.uitypes.TextFieldGrp)
		UI_Globals.FrameListGrp = self.FrameListGrp

		self.Job_Chunk_Size = pm.intSliderGrp(UI_Globals.FrameGroup,
		                                      value=self.defaultRenderGlobals.deadlineChunkSize.get(1),
		                                      maxValue=10000,
		                                      minValue=1,
		                                      field=True,
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      columnAlign=(1, "left"),
		                                      label="Task Size/Chunk Size",
		                                      columnWidth=(1, self.labelWidth),
		                                      annotation="Each task for the job will consist of this many frames")
		isinstance(self.Job_Chunk_Size, pm.uitypes.IntSliderGrp)
		UI_Globals.FrameGroup = self.Job_Chunk_Size

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")

		self.Job_Render_Camera_List= pm.optionMenuGrp('frw_camera',
		                                              annotation="Leave blank to render using the default camera settings.",
		                                              columnWidth2=(self.labelWidth, 320),
		                                              changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                              columnAlign2=("left", "left"),
		                                              label="Camera")
		isinstance(self.Job_Render_Camera_List, pm.uitypes.OptionMenuGrp)
		cams = [" "] + self.Data_Access.all_Renderable_Cameras
		add_menu_items(cams)
		try:
			self.Job_Render_Camera_List.setSelect(cams.index(self._PD.deadlineRenderCamera.get())+1)
		except:
			self.Job_Render_Camera_List.setSelect(1)

		pm.setParent('..')

		self.ProjectPathGrp = pm.textFieldButtonGrp('frw_projectPath',
		                                            text=Helpers.Data_Access.project_workspace,
		                                            label="Project Path",
		                                            #changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            columnAlign=(1, "left"),
		                                            annotation="Use this Maya project path to load the Maya scene",
		                                            columnWidth=[(1, self.labelWidth), (2, 300)],
		                                            rowAttach=[1,"both",1],
		                                            adjustableColumn=2,		                                       
		                                            buttonLabel="...")
		isinstance(self.ProjectPathGrp, pm.uitypes.TextFieldButtonGrp)
		self.ProjectPathGrp.buttonCommand(partial(self.user_Input_Directory_Dialog,self.ProjectPathGrp))
		self.ProjectPathGrp.changeCommand(partial(self._PD.SavePersistentDeadlineOptions, self.ProjectPathGrp))
		UI_Globals.ProjectPathGrp = self.ProjectPathGrp		

		self.ImageOutputPathGrp = pm.textFieldButtonGrp('frw_outputFilePath',
		                                                text=self.Data_Access.imageDirectory,
		                                                label="Output Path",
		                                                changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                columnAlign=(1, "left"),
		                                                annotation="The path to which the output files will be sent. Must be network accessible.",
		                                                columnWidth=[(1, self.labelWidth), (2, 300)],
		                                                rowAttach=[1,"both",1],
		                                                adjustableColumn=2,		                                           
		                                                buttonLabel="...")
		isinstance(self.ImageOutputPathGrp, pm.uitypes.TextFieldButtonGrp)
		self.ImageOutputPathGrp.buttonCommand(partial(self.user_Input_Directory_Dialog,self.ImageOutputPathGrp))
		UI_Globals.ImageOutputPathGrp = self.ImageOutputPathGrp

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=((160 + self.labelWidth), 160),
		             columnAttach2=("left", "left"))

		self.mayaBuildBox = pm.optionMenuGrp('frw_mayaBuild',
		                                     en=self.mayaBuildEnabled_val,
		                                     columnWidth2=(self.labelWidth, 160),
		                                     label="Maya Build",
		                                     changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                     annotation="Force Deadline to render using the specified build of Maya",
		                                     columnAlign2=("left", "left"))
		add_menu_items("None 32bit 64bit".split())
		isinstance(self.mayaBuildBox, pm.uitypes.OptionMenuGrp)

		if self.mayaBuildEnabled_val:
			if cmds.about(is64=True):
				self.mayaBuildBox.setSelect(3)
			else:
				self.mayaBuildBox.setSelect(2)
		else:
			self.mayaBuildBox.setSelect(1)



		self.Job_submit_Maya_Scene= pm.checkBox(UI_Globals.SubmitMayaScene,
		                                        value=self.defaultRenderGlobals.deadlineSubmitMayaScene.get(False),
		                                        annotation="If unchecked, the Maya scene file should be network accessable",
		                                        changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                        label="Submit Maya Scene File")
		isinstance(self.Job_submit_Maya_Scene, pm.uitypes.CheckBox)
		UI_Globals.SubmitMayaScene = self.Job_submit_Maya_Scene

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=3,
		             cw3=(self.labelWidth, 158, 160),
		             ct3=("left", "left", "left"))

		pm.text('frw_dummyMayaBatchLabel',
		        align="left",
		        label="")

		self.Job_Use_Maya_Batch_Plugin = pm.checkBox(UI_Globals.UseMayaBatchPlugin,
		                                             align="left",
		                                             value=self.defaultRenderGlobals.deadlineUseMayaBatchPlugin.get(True),
		                                             annotation="The MayaBatch plugin is a new Maya plugin which keeps the scene loaded between frames",
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             label="Use MayaBatch Plugin")
		isinstance(self.Job_Use_Maya_Batch_Plugin, pm.uitypes.CheckBox)
		UI_Globals.UseMayaBatchPlugin = self.Job_Use_Maya_Batch_Plugin



		self.IgnoreError211 = pm.checkBox('frw_ignoreError211',
		                                  align="left",
		                                  enable=(not self.defaultRenderGlobals.deadlineUseMayaBatchPlugin.get(True)),
		                                  value=0,
		                                  annotation="Does not fail and requeue the render on an Exit Code of 211. Useful if the render actually succeeds and is still throwing this error.",
		                                  label="Ignore Error Code 211")
		isinstance(self.IgnoreError211, pm.uitypes.CheckBox)
		pm.setParent('..')

		self.Job_Startup_Script_Path = pm.textFieldButtonGrp(UI_Globals.StartupScriptPathGrp,
		                                                     text=self.defaultRenderGlobals.deadlineStartupScript.get(""),
		                                                     label="Startup Script",
		                                                     changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                     columnAlign=(1, "left"),
		                                                     annotation="Maya will source the specified script file on startup",
		                                                     columnWidth=[(1, self.labelWidth), (2, 300)],
		                                                     rowAttach=[1,"both",1],
		                                                     adjustableColumn=2,
		                                                     buttonLabel="...")
		isinstance(self.Job_Startup_Script_Path, pm.uitypes.TextFieldButtonGrp)
		self.Job_Startup_Script_Path.buttonCommand(partial(self.user_Input_Load_File_Dialog, self.Job_Startup_Script_Path, "Melscript(*.mel);;Python(*.py);;All(*)"))
		UI_Globals.StartupScriptPathGrp = self.Job_Startup_Script_Path

		self.Job_Maya_Command_Line_Args = pm.textFieldGrp(UI_Globals.MayaArgs,
		                                                  enable=(not self.defaultRenderGlobals.deadlineUseMayaBatchPlugin.get(True)),
		                                                  text=self.defaultRenderGlobals.deadlineMayaArgs.get(""),
		                                                  columnWidth2=(self.labelWidth, 320),
		                                                  rowAttach=[1,"both",1],
		                                                  adjustableColumn=2,
		                                                  label="Command Line Args",
		                                                  changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                  annotation="Additional command line options to pass to Maya",
		                                                  columnAlign2=("left", "left"))
		isinstance(self.Job_Maya_Command_Line_Args, pm.uitypes.TextFieldGrp)
		UI_Globals.MayaArgs = self.Job_Maya_Command_Line_Args

		self.MayaJobType = pm.optionMenuGrp(UI_Globals.MayaJobType,
		                                    annotation="Select the type of job that you want to submit to Deadline",
		                                    columnWidth2=(self.labelWidth, 160),
		                                    changeCommand=self.UpdateJobType,
		                                    columnAlign2=("left", "left"),
		                                    label="Deadline Job Type")
		isinstance(self.MayaJobType, pm.uitypes.OptionMenuGrp)
		UI_Globals.MayaJobType = self.MayaJobType
		add_menu_items(["Maya Render Job","Mental Ray Export Job","VRay Export Job","Renderman Export Job","Arnold Export Job"])
		#add_menu_items(["Maya Render Job","VRay Export Job"])
		self.MayaJobType.setSelect(self.VRayExportJobType)
	#----------------------------------------------------------------------
	def Build_Maya_Render_Job_Frame(self):
		""""""
		self.Maya_Render_Options_FrameLayout= pm.frameLayout(borderStyle="etchedIn",
		                                                     collapsable=True,
		                                                     labelVisible=True,
		                                                     borderVisible=True,
		                                                     label="Maya Render Job")
		isinstance(self.Maya_Render_Options_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.MayaRenderOptionsRollout =  self.Maya_Render_Options_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")

		pm.text('frw_tileLabel',
		        align="left",
		        label="Renders a normal Maya job using the current Maya renderer.")

		pm.setParent('..')

		self.Job_Max_Cpus = pm.intSliderGrp('frw_MaxCPUs',
		                                    en=self.Data_Access.EnableCpuOption,
		                                    value=self.Data_Access.cpuSetting,
		                                    maxValue=64,
		                                    minValue=0,
		                                    field=True,
		                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                    columnAlign=(1, "left"),
		                                    label="Threads",
		                                    columnWidth=(1, self.labelWidth),
		                                    annotation="The number of processors to use during rendering (specify 0 to use all processors available)")
		isinstance(self.Job_Max_Cpus, pm.uitypes.IntSliderGrp)
		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(240, 160),
		             columnAttach2=("left", "left"))

		self.Job_Submit_Each_Render_Layer = pm.checkBox('frw_submitEachRenderLayer',
		                                                en=Helpers.Data_Access.IsRenderLayersOn,
		                                                value=self.defaultRenderGlobals.deadlineSubmitEachRenderLayer.get(True),
		                                                annotation="Check this to submit each renderable Render Layer as a seperate Deadline job. Note that the frame range will be pulled from the render globals for each layer.",
		                                                changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                label="Submit Render Layers As Seperate Jobs")
		isinstance(self.Job_Submit_Each_Render_Layer, pm.uitypes.CheckBox)

		self.Job_Override_Layer_Settings = pm.checkBox('frw_overrideLayerSettings',
		                                               enable=self.defaultRenderGlobals.deadlineOverrideLayerSettings.get(False),
		                                               value=self.defaultRenderGlobals.deadlineOverrideLayerSettings.get(False),
		                                               annotation="If checked, the job name, frame range, and task size can be set for each render layer when submitting a separate job for each layer",
		                                               changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                               label="Override Layer Job Settings")
		isinstance(self.Job_Override_Layer_Settings, pm.uitypes.CheckBox)

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(240, 160),
		             columnAttach2=("left", "left"))

		self.Job_Submit_Each_Camera = pm.checkBox(UI_Globals.SubmitEachCamera,
		                                          align="left",
		                                          value=self.defaultRenderGlobals.deadlineSubmitEachCamera.get(False),
		                                          annotation="Check this to submit each renderable Camera as a separate Deadline job.",
		                                          changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                          label="Submit Cameras As Separate Jobs")
		isinstance(self.Job_Submit_Each_Camera, pm.uitypes.CheckBox)
		UI_Globals.SubmitEachCamera = self.Job_Submit_Each_Camera

		self.Job_Ignore_Default_Cameras = pm.checkBox(UI_Globals.IgnoreDefaultCameras,
		                                              enable=self.defaultRenderGlobals.deadlineSubmitEachCamera.get(False),
		                                              align="left",
		                                              label="Ignore Default Cameras",
		                                              changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                              value=self.defaultRenderGlobals.deadlineIgnoreDefaultCameras.get(False),
		                                              annotation="Check this to ignore default cameras (persp, top, etc) when submitting each renderable Camera as a separate Deadline job.")
		isinstance(self.Job_Ignore_Default_Cameras, pm.uitypes.CheckBox)
		UI_Globals.IgnoreDefaultCameras = self.Job_Ignore_Default_Cameras

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(240, 160),
		             columnAttach2=("left", "left"))

		self.Job_Local_Rendering = pm.checkBox(UI_Globals.LocalRendering,
		                                       align="left",
		                                       value=self.defaultRenderGlobals.deadlineLocalRendering.get(False),
		                                       annotation="If this option is set to true, the slaves will render locally, and then copy the images to the network output directory on completion",
		                                       changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                       label="Enable Local Rendering")
		isinstance(self.Job_Local_Rendering, pm.uitypes.CheckBox)
		UI_Globals.LocalRendering = self.Job_Local_Rendering

		self.Job_Strict_Error_Checking = pm.checkBox(UI_Globals.Job_Strict_Error_Checking,
		                                             align="left",
		                                             value=self.defaultRenderGlobals.deadlineStrictErrorChecking.get(True),
		                                             annotation="If checked, Deadline will fail the render job if any error message is detected",
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             label="Strict Error Checking")
		isinstance(self.Job_Strict_Error_Checking, pm.uitypes.CheckBox)
		UI_Globals.Job_Strict_Error_Checking = self.Job_Strict_Error_Checking

		pm.setParent('..')
		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(240, 160),
		             columnAttach2=("left", "left"))


		self.Render_Half_Frames_CheckBox = pm.checkBox('frw_renderHalfFrames',
		                                               enable=self.Data_Access.ShowHalfFramesOption,
		                                               value=self.frame_range.frameStep == 0.5,
		                                               annotation="If checked, frames will be split into two using a step of 0.5",
		                                               changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                               label="Render Half Frames")
		isinstance(self.Render_Half_Frames_CheckBox, pm.uitypes.CheckBox)
	#----------------------------------------------------------------------
	def Build_Arnold_Options_Frame(self):
		""""""
		self.Maya_Render_Options_Arnold_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                             label="Arnold Options",
		                                                             visible=(Helpers.Data_Access.currentRenderer == "arnold"),
		                                                             borderStyle="etchedIn",
		                                                             collapsable=True,
		                                                             labelVisible=True)
		isinstance(self.Maya_Render_Options_Arnold_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.MayaRenderOptionsArnoldRollout = self.Maya_Render_Options_Arnold_FrameLayout

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		arnoldVerboseEnabled=(Helpers.Data_Access.currentRenderer == "arnold")

		self.arnoldVerboseBox= pm.optionMenuGrp('frw_arnoldVerbose',
		                                        en=arnoldVerboseEnabled,
		                                        columnWidth2=(self.labelWidth, 160),
		                                        label="Arnold Verbosity",
		                                        changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                        annotation="Set the verbosity level for Arnold renders",
		                                        columnAlign2=("left", "left"))
		isinstance(self.arnoldVerboseBox, pm.uitypes.OptionMenuGrp)
		add_menu_items(["0","1","2"])
		self.arnoldVerboseBox.setSelect(1)
	#----------------------------------------------------------------------
	def Build_Mental_Ray_Options_Frame(self):
		""""""
		self.Maya_Render_Options_MentalRay_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                                label="Mental Ray Options",
		                                                                visible=(Helpers.Data_Access.currentRenderer == "mentalRay"),
		                                                                borderStyle="etchedIn",
		                                                                collapsable=True,
		                                                                labelVisible=True)
		isinstance(self.Maya_Render_Options_MentalRay_FrameLayout, pm.uitypes.FrameLayout)

		UI_Globals.MayaRenderOptionsMentalRayRollout = self.Maya_Render_Options_MentalRay_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		mentalRayVerboseEnabled=(Helpers.Data_Access.currentRenderer == "mentalRay")

		self.mentalRayVerboseBox = pm.optionMenuGrp('frw_mentalRayVerbose',
		                                            en=mentalRayVerboseEnabled,
		                                            columnWidth2=(self.labelWidth, 160),
		                                            label="Mental Ray Verbosity",
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            annotation="Set the verbosity level for Mental Ray renders",
		                                            columnAlign2=("left", "left"))
		isinstance(self.mentalRayVerboseBox, pm.uitypes.OptionMenuGrp)
		add_menu_items(["No Messages","Fatal Messages Only","Error Messages","Warning Messages","Info Messages", "Progress Messages", "Detailed Messages (Debug)"])
		self.mentalRayVerboseBox.setSelect(1)

		self.Job_MentalRay_Auto_Memory = pm.checkBox('frw_autoMemoryLimit',
		                                             align="left",
		                                             value=self.defaultRenderGlobals.deadlineMentalRayAutoMemoryLimit.get(True),
		                                             annotation="If checked, Mental Ray will automatically detect the optimal memory limit when rendering",
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             label="Auto Memory Limit")

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, (320 + self.labelWidth)),
		             ct1="right")

		self.Job_MentalRay_Auto_Memory_Limit = pm.intSliderGrp('frw_memoryLimit',
		                                                       enable=(not self.defaultRenderGlobals.deadlineMentalRayAutoMemoryLimit.get(True)),
		                                                       value=self.defaultRenderGlobals.deadlineMentalRayMemoryLimit.get(0),
		                                                       maxValue=100000,
		                                                       minValue=0,
		                                                       field=True,
		                                                       changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                       columnAlign=(1, "left"),
		                                                       label="Memory Limit (MB)",
		                                                       columnWidth=(1, self.labelWidth),
		                                                       annotation="Soft limit (in MB) for the memory used by Mental Ray (specify 0 for unlimited memory)")
	#----------------------------------------------------------------------
	def Build_VRay_Options_Frame(self):
		""""""
		self.Maya_Render_Options_VRay_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                           label="VRay Options",
		                                                           visible=(Helpers.Data_Access.currentRenderer == "vray"),
		                                                           borderStyle="etchedIn",
		                                                           collapsable=True,
		                                                           labelVisible=True)
		UI_Globals.MayaRenderOptionsVRayRollout = self.Maya_Render_Options_VRay_FrameLayout

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		useMayaBatchPlugin=int(pm.mel.attributeExists('deadlineUseMayaBatchPlugin', 'defaultRenderGlobals') and pm.getAttr('defaultRenderGlobals.deadlineUseMayaBatchPlugin') or True)

		self.Job_Vray_Auto_Memory_Enabled =  pm.checkBox(UI_Globals.VrayAutoMemoryEnabled,
		                                                 enable=useMayaBatchPlugin,
		                                                 align="left",
		                                                 label="Auto Memory Limit Detection (Requires the MayaBatch Plugin)",
		                                                 changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                 value=self.defaultRenderGlobals.deadlineVrayAutoMemoryEnabled.get(False),
		                                                 annotation="If checked, Deadline will automatically detect the dynamic memory limit for VRay prior to rendering.")
		isinstance(self.Job_Vray_Auto_Memory_Enabled, pm.uitypes.CheckBox)
		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, (320 + self.labelWidth)),
		             ct1="right")

		self.Job_Vray_Auto_Memory_Buffer = pm.intSliderGrp(UI_Globals.VrayAutoMemoryBuffer,
		                                                   enable=(useMayaBatchPlugin and self.defaultRenderGlobals.deadlineVrayAutoMemoryEnabled.get(False)),
		                                                   value=self.defaultRenderGlobals.deadlineVrayAutoMemoryBuffer.get(500),
		                                                   maxValue=100000,
		                                                   minValue=0,
		                                                   field=True,
		                                                   changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                   columnAlign=(1, "left"),
		                                                   label="Memory Buffer (MB)",
		                                                   columnWidth=(1, self.labelWidth),
		                                                   annotation="Deadline subtracts this value from the system's unused memory to determine the dynamic memory limit for VRay.")
		isinstance(self.Job_Vray_Auto_Memory_Buffer, pm.uitypes.IntSliderGrp)
	#----------------------------------------------------------------------
	def Build_Tile_Rendering_Frame(self):
		""""""
		self.Maya_Render_Options_Tile_FrameLayout= pm.frameLayout(collapse=True,
		                                                          borderVisible=True,
		                                                          label="Tile Rendering",
		                                                          borderStyle="etchedIn",
		                                                          collapsable=True,
		                                                          labelVisible=True)
		isinstance(self.Maya_Render_Options_Tile_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.MayaRenderOptionsTileRollout = self.Maya_Render_Options_Tile_FrameLayout

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")

		pm.text('frw_tileLabel',
		        align="left",
		        label="For arnold, mayaSoftware, mentalRay, renderMan, finalRender, turtle, and vray jobs only.\nIf you have multiple layers, this only works if you submit each layer as a seperate job.")

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, self.labelWidth),
		             ct1="left")

		self.RegionRendering_CheckBox = pm.checkBox('frw_regionRendering',
		                                            enable=True,
		                                            value=self.regionRendering_val,
		                                            annotation="Tile rendering splits up a frame between multiple machines (the assembly is done automatically for bmp, exr, jpg, png, tga, and tif)",
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            label="Enable Tile Rendering")
		isinstance(self.RegionRendering_CheckBox, pm.uitypes.CheckBox)
		self.RegionRendering_CheckBox.changeCommand(partial(self._PD.SavePersistentDeadlineOptions, self.RegionRendering_CheckBox))

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, (320 + self.labelWidth)),
		             ct1="right")

		self.Job_Tiles_In_X = pm.intSliderGrp(UI_Globals.TilesInX,
		                                      enable=self.regionRendering_val,
		                                      value=self.defaultRenderGlobals.deadlineTilesInX.get(2),
		                                      maxValue=200,
		                                      minValue=1,
		                                      field=True,
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      columnAlign=(1, "left"),
		                                      label="Tiles In X",
		                                      columnWidth=(1, self.labelWidth),
		                                      annotation="The number of tiles in the X direction")
		isinstance(self.Job_Tiles_In_X, pm.uitypes.IntSliderGrp)
		UI_Globals.TilesInX = self.Job_Tiles_In_X

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, (320 + self.labelWidth)),
		             ct1="right")

		self.Job_Tiles_In_Y = pm.intSliderGrp(UI_Globals.TilesInY,
		                                      enable=self.regionRendering_val,
		                                      value=self.defaultRenderGlobals.deadlineTilesInY.get(2),
		                                      maxValue=200,
		                                      minValue=1,
		                                      field=True,
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      columnAlign=(1, "left"),
		                                      label="Tiles In Y",
		                                      columnWidth=(1, self.labelWidth),
		                                      annotation="The number of tiles in the Y direction")
		isinstance(self.Job_Tiles_In_Y, pm.uitypes.IntSliderGrp)
		UI_Globals.TilesInY = self.Job_Tiles_In_Y

		pm.setParent('..')

		self.Submit_Tiles_As_Single_Job_CheckBox = pm.checkBox(UI_Globals.SubmitTileSingleJob,
		                                                       en=self.regionRendering_val,
		                                                       align="left",
		                                                       label="Submit All Tiles As A Single Job",
		                                                       changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                       value=self.defaultRenderGlobals.deadlineTileSingleJob.get(True),
		                                                       annotation="Check this to combine all tiles into a single job.")
		isinstance(self.Submit_Tiles_As_Single_Job_CheckBox, pm.uitypes.CheckBox)
		self.Submit_Tiles_As_Single_Job_CheckBox.changeCommand(partial(self._PD.SavePersistentDeadlineOptions, self.Submit_Tiles_As_Single_Job_CheckBox))
		UI_Globals.SubmitTileSingleJob = self.Submit_Tiles_As_Single_Job_CheckBox

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, (320 + self.labelWidth)),
		             ct1="right")

		currTime=int(pm.currentTime(query=1))

		self.Job_Tile_Single_Frame = pm.intSliderGrp('frw_tileSingleFrame',
		                                             enable=self.regionRendering_val,
		                                             value=currTime,
		                                             maxValue=100000,
		                                             minValue=-100000,
		                                             field=True,
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             columnAlign=(1, "left"),
		                                             label="Single Job Frame",
		                                             columnWidth=(1, self.labelWidth),
		                                             annotation="The single frame to render.")
		isinstance(self.Job_Tile_Single_Frame, pm.uitypes.IntSliderGrp)

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(240, 160),
		             columnAttach2=("left", "right"))

		self.Job_Submit_Tile_Dependent = pm.checkBox(UI_Globals.SubmitTileDependentJob,
		                                             en=self.regionRendering_val,
		                                             align="left",
		                                             label="Submit Dependent Assembly Job",
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             value=self.defaultRenderGlobals.deadlineTileDependentJob.get(True),
		                                             annotation="Check this submit an assembly job that is dependent on the first job.")
		isinstance(self.Job_Submit_Tile_Dependent, pm.uitypes.CheckBox)
		UI_Globals.SubmitTileDependentJob = self.Job_Submit_Tile_Dependent
		self.Job_Submit_Tile_Dependent.changeCommand(partial(self._PD.SavePersistentDeadlineOptions, self.Job_Submit_Tile_Dependent))

		self.Job_Submit_Tile_Cleanup = pm.checkBox(UI_Globals.SubmitTileCleanupJob,
		                                           en=self.regionRendering_val,
		                                           align="left",
		                                           label="Cleanup Tiles After Assembly",
		                                           changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                           value=self.defaultRenderGlobals.deadlineTileCleanupJob.get(False),
		                                           annotation="Check this to delete the tile jobs after the assembly job completes.")
		isinstance(self.Job_Submit_Tile_Cleanup, pm.uitypes.CheckBox)
		UI_Globals.SubmitTileCleanupJob = self.Job_Submit_Tile_Cleanup

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(203, 160),
		             columnAttach2=("left", "right"))

		self.Job_Submit_Tile_Use_Draft = pm.checkBox(UI_Globals.SubmitTileUseDraft,
		                                             en=self.regionRendering_val,
		                                             align="left",
		                                             label="Assemble Using Draft",
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             value=self.defaultRenderGlobals.deadlineTileUseDraft.get(True),
		                                             annotation="Check this to assemble tiles using draft")
		UI_Globals.SubmitTileUseDraft = self.Job_Submit_Tile_Use_Draft
		isinstance(self.Job_Submit_Tile_Use_Draft, pm.uitypes.CheckBox)
		self.Job_Submit_Tile_Use_Draft.changeCommand(partial(self._PD.SavePersistentDeadlineOptions, self.Job_Submit_Tile_Use_Draft))

		self.Job_Submit_Tile_Error_On_Missing = pm.checkBox(UI_Globals.SubmitTileErrorOnMissing,
		                                                    en=(self.defaultRenderGlobals.deadlineTileUseDraft.get(True) and self.regionRendering_val),
		                                                    align="left",
		                                                    label="Error on Missing Tiles",
		                                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                    value=self.defaultRenderGlobals.deadlineTileErrorOnMissing.get(True),
		                                                    annotation="Check this force the render to fail on a missing tile")
		isinstance(self.Job_Submit_Tile_Error_On_Missing, pm.uitypes.CheckBox)
		UI_Globals.SubmitTileErrorOnMissing = self.Job_Submit_Tile_Error_On_Missing
	#----------------------------------------------------------------------
	def Build_Mental_Ray_Export_Job_Frame(self):
		""""""
		self.MentalRay_Export_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                   label="Mental Ray Export Job",
		                                                   visible=False,
		                                                   borderStyle="etchedIn",
		                                                   collapsable=True,
		                                                   labelVisible=True)
		isinstance(self.MentalRay_Export_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.MentalRayExportRollout = self.MentalRay_Export_FrameLayout
		self.Ccheck_layout = pm.columnLayout(adjustableColumn=True,
		                                     columnAttach=("both", 4),
		                                     rowSpacing=4)

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")

		pm.text('frw_tileLabel',
		        align="left",
		        label="Uses Mental Ray to export mi files instead of rendering.")

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             adjustableColumn=1,
		             #columnAttach=[1,"right",1],
		             #columnWidth2=(labelWidth, 320),
		             columnAttach2=("right", "right"))

		self.Job_MentalRay_File_Name = pm.textFieldButtonGrp('frw_mentalRayFilePath',
		                                                     text=self.defaultRenderGlobals.deadlineMentalRayFilename.get(""),
		                                                     label="Output File",
		                                                     changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                     columnAlign=(1, "left"),
		                                                     annotation="The full filename of the Mental Ray files that will be exported (padding is handled automatically by the exporter)",
		                                                     #columnWidth=[(1, labelWidth), (2, 300)],
		                                                     rowAttach=[1,"both",1],
		                                                     adjustableColumn=2,
		                                                     buttonLabel="...")
		isinstance(self.Job_MentalRay_File_Name, pm.uitypes.TextFieldButtonGrp)
		self.Job_MentalRay_File_Name.buttonCommand(partial(self.user_Input_Save_File_Dialog, self.Job_MentalRay_File_Name, "Mental_Ray(*.mi);;All_Files(*)"))
		UI_Globals.MentalRayFilenameGrp = self.Job_MentalRay_File_Name

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(110, 290),
		             columnAttach2=("left", "left"))

		pm.button(width=100,
		          c=OpenExportSettings,
		          height=26,
		          annotation="Opens the Export Settings dialog",
		          label="Export Settings...")
		pm.text(label="(This dialog must be open when submitting the job)")
	#----------------------------------------------------------------------
	def Build_Mental_Ray_Render_Job_Frame(self):
		""""""
		self.MentalRay_Export_Render_Job_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                              label="Mental Ray Render Job",
		                                                              visible=False,
		                                                              borderStyle="etchedIn",
		                                                              collapsable=True,
		                                                              labelVisible=True)
		UI_Globals.MentalRayExportRenderJobRollout = self.MentalRay_Export_Render_Job_FrameLayout

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)
		self.Job_Submit_MentalRay_Job = pm.checkBox(UI_Globals.SubmitMentalRayJob,
		                                            align="left",
		                                            value=self.defaultRenderGlobals.deadlineSubmitMentalRayJob.get(False),
		                                            annotation="If this option is set to true, a Mental Ray Standalone job that is dependent on the export job will also be submitted",
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            label="Submit Dependent Mental Ray Standalone Render Job")
		isinstance(self.Job_Submit_MentalRay_Job, pm.uitypes.CheckBox)
		UI_Globals.SubmitMentalRayJob = self.Job_Submit_MentalRay_Job

		self.Job_MentalRay_Threads = pm.intSliderGrp(UI_Globals.MentalRayThreads,
		                                             value=self.defaultRenderGlobals.deadlineMentalRayThreads.get(0),
		                                             maxValue=16,
		                                             minValue=0,
		                                             field=True,
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             columnAlign=(1, "left"),
		                                             label="Threads",
		                                             columnWidth=(1, self.labelWidth),
		                                             annotation="The number of threads to use during rendering (specify 0 to use all processors available)")
		isinstance(self.Job_MentalRay_Threads, pm.uitypes.IntSliderGrp)
		UI_Globals.MentalRayThreads = self.Job_MentalRay_Threads

		self.Job_MentalRay_Offset = pm.intSliderGrp(UI_Globals.MentalRayOffset,
		                                            value=self.defaultRenderGlobals.deadlineMentalRayOffset.get(0),
		                                            maxValue=10000,
		                                            minValue=-10000,
		                                            field=True,
		                                            changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                            columnAlign=(1, "left"),
		                                            label="Frame Offset",
		                                            columnWidth=(1, self.labelWidth),
		                                            annotation="The value to offset the frame numbers by when rendering separate mi files per frame")
		isinstance(self.Job_MentalRay_Offset, pm.uitypes.IntSliderGrp)
		UI_Globals.MentalRayOffset = self.Job_MentalRay_Offset

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=((160 + self.labelWidth), 160),
		             columnAttach2=("left", "left"))

		self.mentalRayBuildBox = pm.optionMenuGrp('frw_mentalRayBuild',
		                                          annotation="Force Deadline to render using the specified build of Maya",
		                                          columnWidth2=(self.labelWidth, 160),
		                                          changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                          columnAlign2=("left", "left"),
		                                          label="Mental Ray Build")
		isinstance(self.mentalRayBuildBox, pm.uitypes.OptionMenuGrp)
		add_menu_items("None 32bit 64bit".split())
		mayaBuildEnabled = True
		if mayaBuildEnabled:
			if cmds.about(is64=True):
				self.mentalRayBuildBox.setSelect(3)
			else:
				self.mentalRayBuildBox.setSelect(2)
		else:
			self.mentalRayBuildBox.setSelect(1)

		self.MentalRay_Local_Rendering = pm.checkBox(UI_Globals.MentalRayLocalRendering,
		                                             value=self.defaultRenderGlobals.deadlineMentalRayLocalRendering.get(False),
		                                             annotation="If this option is set to true, the slaves will render locally, and then copy the images to the network output directory on completion",
		                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                             label="Enable Local Rendering")
		isinstance(self.MentalRay_Local_Rendering, pm.uitypes.CheckBox)
		UI_Globals.MentalRayLocalRendering = self.MentalRay_Local_Rendering

		pm.setParent('..')

		self.MentalRay_Command_Line_Args = pm.textFieldGrp(UI_Globals.MentalRayArgs,
		                                                   text=self.defaultRenderGlobals.deadlineMentalRayArgs.get(""),
		                                                   columnWidth2=(self.labelWidth, 320),
		                                                   label="Command Line Args",
		                                                   changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                   annotation="Additional command line options to pass to mental ray",
		                                                   rowAttach=[1,"both",1],
		                                                   adjustableColumn=2,
		                                                   columnAlign2=("left", "left"))
		isinstance(self.MentalRay_Command_Line_Args, pm.uitypes.TextFieldGrp)
		UI_Globals.MentalRayArgs = self.MentalRay_Command_Line_Args
	#----------------------------------------------------------------------
	def Build_VRay_Export_Job_Frame(self):
		""""""
		self.Vray_Export_FrameLayout = pm.frameLayout(borderVisible=True,
		                                              label="VRay Export Job",
		                                              visible=False,
		                                              borderStyle="etchedIn",
		                                              collapsable=True,
		                                              labelVisible=True)
		isinstance(self.Vray_Export_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.VrayExportRollout = self.Vray_Export_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")

		pm.text('frw_tileLabel',
		        align="left",
		        label="Uses VRay to export vrscene files instead of rendering.")

		pm.setParent('..')

		pm.rowLayout(numberOfColumns=2,
		             adjustableColumn=1,
		             columnWidth2=(self.labelWidth, 320),
		             columnAttach2=("right", "right"))

		self.VRay_File_Name = pm.textFieldGrp('frw_vrayFilePath',
		                                      text=self.ImageOutputPathGrp.getText()+"/<Layer>/<Layer>",
		                                      editable=False,
		                                      label="Vray Scene File",
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      columnAlign=(1, "left"),
		                                      rowAttach=[1,"both",1],
		                                      adjustableColumn=2,
		                                      annotation="The full filename of the VRay files that will be exported (padding is handled automatically by the exporter)",
		                                      columnWidth=[(1, self.labelWidth), (2, 300)])
		isinstance(self.VRay_File_Name, pm.uitypes.TextFieldGrp)

		#self.VRay_File_Name.buttonCommand( partial(self.Set_File_Save_Path, self.VRay_File_Name, "VRay_Scene(*.vrscene);;All_Files(*)") )
		UI_Globals.VRayFilenameGrp = self.VRay_File_Name
	#----------------------------------------------------------------------
	def Build_VRay_Render_Job_Frame(self):
		""""""
		self.Vray_Export_Render_Job_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                         label="VRay Render Job",
		                                                         visible=False,
		                                                         borderStyle="etchedIn",
		                                                         collapsable=True,
		                                                         labelVisible=True)
		isinstance(self.Vray_Export_Render_Job_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.VrayExportRenderJobRollout = self.Vray_Export_Render_Job_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		self.Submit_VRay_Job = pm.checkBox(UI_Globals.SubmitVRayJob,
		                                   align="left",
		                                   value=self.defaultRenderGlobals.deadlineSubmitVRayJob.get(False),
		                                   annotation="If this option is set to true, a VRay Standalone job that is dependent on the export job will also be submitted",
		                                   changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                   label="Submit Dependent VRay Standalone Render Job")
		isinstance(self.Submit_VRay_Job, pm.uitypes.CheckBox)
		UI_Globals.SubmitVRayJob = self.Submit_VRay_Job

		self.Job_Vray_Threads = pm.intSliderGrp(UI_Globals.VrayThreads,
		                                        value=self.defaultRenderGlobals.deadlineVRayThreads.get(0),
		                                        maxValue=16,
		                                        minValue=0,
		                                        field=True,
		                                        changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                        columnAlign=(1, "left"),
		                                        label="Threads",
		                                        columnWidth=(1, self.labelWidth),
		                                        annotation="The number of threads to use during rendering (specify 0 to use all processors available)")
		isinstance(self.Job_Vray_Threads, pm.uitypes.IntSliderGrp)
		UI_Globals.VrayThreads = self.Job_Vray_Threads			
	#----------------------------------------------------------------------
	def Build_Vrimg2Exr_Conversion_Job_Frame(self):
		""""""
		self.Vray_Export_Vrimg_Job_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                        label="Vrimg2Exr Conversion Job",
		                                                        visible=False,
		                                                        borderStyle="etchedIn",
		                                                        collapsable=True,
		                                                        labelVisible=True)
		isinstance(self.Vray_Export_Vrimg_Job_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.VrayExportVrimgJobRollout = self.Vray_Export_Vrimg_Job_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)
		vrimg2ExrEnabled = True
		self.Submit_Vrimg_2_Exr_Job = pm.checkBox(UI_Globals.SubmitVrimg2ExrJob,
		                                          enable=vrimg2ExrEnabled,
		                                          align="left",
		                                          label="Convert vrimg Files To exr With Dependent Job",
		                                          changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                          value=True,
		                                          annotation="Enable this option to submit a dependent job that converts the vrimg output files to exr files")
		isinstance(self.Submit_Vrimg_2_Exr_Job, pm.uitypes.CheckBox)
		UI_Globals.SubmitVrimg2ExrJob = self.Submit_Vrimg_2_Exr_Job
	#----------------------------------------------------------------------
	def Build_Vrimg2Exr_Conversion_Options_Frame(self):
		""""""
		self.Vrimg2Exr_Conversion_Options_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                               label="Vrimg2Exr Conversion Options",
		                                                               visible=self.Submit_Vrimg_2_Exr_Job.getValue(),
		                                                               borderStyle="etchedIn",
		                                                               collapsable=True,
		                                                               labelVisible=True)
		isinstance(self.Vrimg2Exr_Conversion_Options_FrameLayout, pm.uitypes.FrameLayout)
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		pm.rowLayout(numberOfColumns=2,
		             adjustableColumn=2,
		             columnWidth2=(self.labelWidth+125, 250),
		             columnAttach2=("left", "right"))

		self.Delete_Vrimg_Files   = pm.checkBox(UI_Globals.Job_Delete_Vrimg_Files,
		                                        enable=self.Submit_Vrimg_2_Exr_Job.getValue(),
		                                        align="left",
		                                        label="Delete Input vrimg Files After Conversion",
		                                        changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                        value=self.defaultRenderGlobals.deadlineDeleteVrimgFiles.get(False),
		                                        annotation="Enable this option to delete the input vrimg file after the conversion has finished.")
		isinstance(self.Delete_Vrimg_Files, pm.uitypes.CheckBox)
		UI_Globals.Job_Delete_Vrimg_Files = self.Delete_Vrimg_Files


		self.Vrimg2Exr_Conversion_Crop_EXR_CheckBox =pm.checkBox("Vrimg2Exr_Conversion_Crop_EXR_CheckBox",
		                                                         enable=True,
		                                                         align="left",
		                                                         label="Crop EXR Data Window",
		                                                         changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                         value=True,
		                                                         annotation="")
		isinstance(self.Vrimg2Exr_Conversion_Crop_EXR_CheckBox, pm.uitypes.CheckBox)

		pm.setParent("..")
		pm.rowLayout(numberOfColumns=2,
		             adjustableColumn=2,
		             columnWidth2=(self.labelWidth-40, 450),
		             columnAttach2=("right", "right"))

		self.Vrimg2Exr_Conversion_Memory_Limit_Checkbox =pm.checkBox("Vrimg2Exr_Conversion_Memory_Limit_Checkbox",
		                                                             enable=True,
		                                                             align="left",
		                                                             label="Set Buffer Size",
		                                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                             value=True,
		                                                             annotation="Enable this option to set the maximum allocated buffer size per channel in megabytes.\nIf the image does not fit into the max buffer size\nit is converted in several passes.")
		isinstance(self.Vrimg2Exr_Conversion_Memory_Limit_Checkbox, pm.uitypes.CheckBox)

		#pm.rowLayout(numberOfColumns=2,
					#adjustableColumn=1,
					#columnWidth2=(self.labelWidth, 320),
					#columnAttach2=("right", "right"))

		self.Vrimg2Exr_Conversion_Memory_Limit_Slider = pm.intSliderGrp("Vrimg2Exr_Conversion_Memory_Limit_Slider",
		                                                                enable=self.Vrimg2Exr_Conversion_Memory_Limit_Checkbox.getValue(),
		                                                                value=self.defaultRenderGlobals.deadlineVrayAutoMemoryBuffer.get(500),
		                                                                maxValue=100000,
		                                                                minValue=0,
		                                                                field=True,
		                                                                changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                                columnAlign=(1, "right"),
		                                                                label="Memory Buffer Size (MB)",
		                                                                columnWidth=(1, self.labelWidth),
		                                                                annotation="")
		isinstance(self.Vrimg2Exr_Conversion_Memory_Limit_Slider, pm.uitypes.IntSliderGrp)

		pm.setParent("..")
		pm.rowLayout(numberOfColumns=2,
		             adjustableColumn=2,
		             columnWidth2=(self.labelWidth-40, 450),
		             columnAttach2=("right", "right"))
		self.Vrimg2Exr_Conversion_Compression_CheckBox  =pm.checkBox("Vrimg2Exr_Conversion_Compression_CheckBox",
		                                                             enable=True,
		                                                             align="left",
		                                                             label="Exr Compression",
		                                                             changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                             value=True,
		                                                             annotation="Enable this option to set the compression type. The Zip method is used by default.")
		isinstance(self.Vrimg2Exr_Conversion_Compression_CheckBox, pm.uitypes.CheckBox)

		self.Vrimg2Exr_Conversion_Compression_MenuGroup = pm.optionMenuGrp('Vrimg2Exr_Conversion_Compression_MenuGroup',
		                                                                   annotation="",
		                                                                   columnWidth2=(self.labelWidth, 160),
		                                                                   changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                                   columnAlign2=("left", "left"),
		                                                                   label="Compression Type")
		isinstance(self.Vrimg2Exr_Conversion_Compression_MenuGroup, pm.uitypes.OptionMenuGrp)
		add_menu_items(["none","piz","pxr24","zip","zips"])
		self.Vrimg2Exr_Conversion_Compression_MenuGroup.setSelect(5)

		pm.setParent("..")
		pm.rowLayout(numberOfColumns=2,
		             adjustableColumn=2,
		             columnWidth2=(self.labelWidth-40, 450),
		             columnAttach2=("right", "right"))

		self.Vrimg2Exr_Conversion_Specify_Channel_CheckBox =pm.checkBox("Vrimg2Exr_Conversion_Specify_Channel_CheckBox",
		                                                                enable=True,
		                                                                align="left",
		                                                                label="Specify Channel",
		                                                                changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                                value=False,
		                                                                annotation="Enable this option to read the specified channel from the vrimg file and write it as the RGB channel in the output file.")
		isinstance(self.Vrimg2Exr_Conversion_Specify_Channel_CheckBox, pm.uitypes.CheckBox)

		self.Vrimg2Exr_Conversion_Specify_Channel_TextField = pm.textFieldGrp("Vrimg2Exr_Conversion_Specify_Channel_TextField",
		                                                                      text="",
		                                                                      columnWidth2=(self.labelWidth, 320),
		                                                                      label="Channal Name",
		                                                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                                                      annotation="channel from the vrimg file and write it as the RGB channel in the output file",
		                                                                      rowAttach=[1,"both",1],
		                                                                      adjustableColumn=2,
		                                                                      columnAlign2=("left", "left"))
		isinstance(self.Vrimg2Exr_Conversion_Specify_Channel_TextField, pm.uitypes.TextFieldGrp)
	#----------------------------------------------------------------------
	def Build_Renderman_Export_Job_Frame(self):
		""""""
		self.Renderman_Export_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                   label="Renderman Export Job",
		                                                   visible=False,
		                                                   borderStyle="etchedIn",
		                                                   collapsable=True,
		                                                   labelVisible=True)
		isinstance(self.Renderman_Export_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.RendermanExportRollout = self.Renderman_Export_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)
		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")
		pm.text('frw_exportPRManLabel',
		        align="left",
		        label="Uses Renderman to export rib files instead of rendering.")

		pm.setParent('..')

		self.ExportPRManThreads = pm.intSliderGrp(UI_Globals.ExportPRManThreads,
		                                          value=self.defaultRenderGlobals.deadlineExportPRManThreads.get(0),
		                                          maxValue=16,
		                                          minValue=0,
		                                          field=True,
		                                          changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                          columnAlign=(1, "left"),
		                                          label="Threads",
		                                          columnWidth=(1, self.labelWidth),
		                                          annotation="The number of threads to use during exporting (specify 0 to use all processors available)")
		isinstance(self.ExportPRManThreads, pm.uitypes.IntSliderGrp)
		UI_Globals.ExportPRManThreads = self.ExportPRManThreads
	#----------------------------------------------------------------------
	def Build_PRMan_Render_Job_Frame(self):
		""""""
		self.Renderman_Export_Render_Job_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                              label="PRMan Render Job",
		                                                              visible=False,
		                                                              borderStyle="etchedIn",
		                                                              collapsable=True,
		                                                              labelVisible=True)
		isinstance(self.Renderman_Export_Render_Job_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.RendermanExportRenderJobRollout = self.Renderman_Export_Render_Job_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		self.SubmitPRManJob = pm.checkBox(UI_Globals.SubmitPRManJob,
		                                  align="left",
		                                  value=self.defaultRenderGlobals.deadlineSubmitPRManJob.get(False),
		                                  annotation="If this option is set to true, a PRMan Standalone job that is dependent on the export job will also be submitted",
		                                  changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                  label="Submit Dependent PRMan Standalone Render Job")
		isinstance(self.SubmitPRManJob, pm.uitypes.CheckBox)
		UI_Globals.SubmitPRManJob = self.SubmitPRManJob

		self.PrmanThreads = pm.intSliderGrp(UI_Globals.PrmanThreads,
		                                    value=self.defaultRenderGlobals.deadlinePRManThreads.get(0),
		                                    maxValue=16,
		                                    minValue=0,
		                                    field=True,
		                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                    columnAlign=(1, "left"),
		                                    label="Threads",
		                                    columnWidth=(1, self.labelWidth),
		                                    annotation="The number of threads to use during rendering (specify 0 to use all processors available)")
		isinstance(self.PrmanThreads, pm.uitypes.IntSliderGrp)
		UI_Globals.PrmanThreads = self.PrmanThreads

		self.PrmanArgs = pm.textFieldGrp(UI_Globals.PrmanArgs,
		                                 text=self.defaultRenderGlobals.deadlinePRManArgs.get(""),
		                                 columnWidth2=(self.labelWidth, 320),
		                                 label="Command Line Args",
		                                 changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                 rowAttach=[1,"both",1],
		                                 adjustableColumn=2,
		                                 annotation="Additional command line options to pass to PRMan",
		                                 columnAlign2=("left", "left"))
		isinstance(self.PrmanArgs, pm.uitypes.TextFieldGrp)
		UI_Globals.PrmanArgs = self.PrmanArgs
	#----------------------------------------------------------------------
	def Build_Arnold_Export_Job_Frame(self):
		""""""
		self.Arnold_Export_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                label="Arnold Export Job",
		                                                visible=False,
		                                                borderStyle="etchedIn",
		                                                collapsable=True,
		                                                labelVisible=True)
		isinstance(self.Arnold_Export_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.ArnoldExportRollout = self.Arnold_Export_FrameLayout
		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		pm.rowLayout(numberOfColumns=1,
		             columnWidth=(1, 400),
		             ct1="left")
		pm.text('frw_exportArnoldLabel',
		        align="left",
		        label="Uses Arnold to export ass files instead of rendering.")
	#----------------------------------------------------------------------
	def Build_Arnold_Render_Job_Frame(self):
		""""""
		self.Arnold_Export_Render_Job_FrameLayout = pm.frameLayout(borderVisible=True,
		                                                           label="Arnold Render Job",
		                                                           visible=False,
		                                                           borderStyle="etchedIn",
		                                                           collapsable=True,
		                                                           labelVisible=True)
		isinstance(self.Arnold_Export_Render_Job_FrameLayout, pm.uitypes.FrameLayout)
		UI_Globals.ArnoldExportRenderJobRollout = self.Arnold_Export_Render_Job_FrameLayout

		pm.columnLayout(adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		self.SubmitArnoldJob = pm.checkBox(UI_Globals.SubmitArnoldJob,
		                                   align="left",
		                                   value=self.defaultRenderGlobals.deadlineSubmitArnoldJob.get(False),
		                                   annotation="If this option is set to true, an Arnold Standalone job that is dependent on the export job will also be submitted",
		                                   changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                   label="Submit Dependent Arnold Standalone Render Job")
		isinstance(self.SubmitArnoldJob, pm.uitypes.CheckBox)
		UI_Globals.SubmitArnoldJob = self.SubmitArnoldJob

		self.ArnoldThreads   = pm.intSliderGrp(UI_Globals.ArnoldThreads,
		                                       value=self.defaultRenderGlobals.deadlineArnoldThreads.get(0),
		                                       maxValue=16,
		                                       minValue=0,field=True,
		                                       changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                       columnAlign=(1, "left"),
		                                       label="Threads",
		                                       columnWidth=(1, self.labelWidth),
		                                       annotation="The number of threads to use during rendering (specify 0 to use all processors available)")
		isinstance(self.ArnoldThreads, pm.uitypes.IntSliderGrp)
		UI_Globals.ArnoldThreads = self.ArnoldThreads

		self.ArnoldArgs      = pm.textFieldGrp(UI_Globals.ArnoldArgs,
		                                       text=self.defaultRenderGlobals.deadlineArnoldArgs.get(""),
		                                       columnWidth2=(self.labelWidth, 320),
		                                       label="Command Line Args",
		                                       changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                       annotation="Additional command line options to pass to Arnold",
		                                       rowAttach=[1,"both",1],
		                                       adjustableColumn=2,
		                                       columnAlign2=("left", "left"))
		isinstance(self.ArnoldArgs, pm.uitypes.TextFieldGrp)
		UI_Globals.ArnoldArgs = self.ArnoldArgs
	#----------------------------------------------------------------------
	def Build_Shotgun_Tab(self):
		""""""
		self.shotgun_tab_layout = pm.columnLayout('shotgunTabLayout',
		                                          adjustableColumn=True,
		                                          columnAttach=("both", 4))

		self.frw_SHOTGUN = pm.frameLayout(collapse=False,
		                                  borderVisible=True,
		                                  label="Shotgun",
		                                  borderStyle="etchedIn",
		                                  collapsable=True,
		                                  labelVisible=True)
		isinstance(self.frw_SHOTGUN, pm.uitypes.FrameLayout)

		pm.columnLayout(columnAlign="left",
		                adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)
		pm.rowLayout(numberOfColumns=3,
		             cw3=(self.labelWidth, 160, 160))
		#dummy label
		pm.text(label="")

		self.bnt_connect_to_shotgun = pm.button(width=150,
		                                        command=self.user_Input_Shotgun_Info_Dialog,
		                                        label="Connect to Shotgun...")
		isinstance(self.bnt_connect_to_shotgun, pm.uitypes.Button)

		enable=len(Shotgun_Globals.SGInfoKeys)>0

		self.UseShotgunCheckBox = pm.checkBox(UI_Globals.UseShotgunCheckBox,
		                                      changeCommand=self.On_Use_ShotgunChanged,
		                                      enable=enable,
		                                      annotation="Check to use Shotgun.",
		                                      value=False,
		                                      label="Submit Shotgun Info With Job")
		isinstance(self.UseShotgunCheckBox, pm.uitypes.CheckBox)
		UI_Globals.UseShotgunCheckBox = self.UseShotgunCheckBox

		pm.setParent('..')

		self.ShotgunVersion = pm.textFieldGrp(UI_Globals.ShotgunVersion,
		                                      enable=False,
		                                      text=self.defaultRenderGlobals.deadlineSGVersionName.get(""),
		                                      columnWidth2=(self.labelWidth, 325),
		                                      label="Version Name",
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      annotation="The name of the Version that will be created in Shotgun.",
		                                      columnAlign2=("left", "left"))
		isinstance(self.ShotgunVersion, pm.uitypes.TextFieldGrp)
		UI_Globals.ShotgunVersion = self.ShotgunVersion

		self.ShotgunDescription = pm.textFieldGrp(UI_Globals.ShotgunDescription,
		                                          enable=False,
		                                          text=self.defaultRenderGlobals.deadlineSGDescription.get(""),
		                                          columnWidth2=(self.labelWidth, 325),
		                                          label="Description",
		                                          changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                          annotation="The description of the Version that will be created in Shotgun.",
		                                          columnAlign2=("left", "left"))
		isinstance(self.ShotgunDescription, pm.uitypes.TextFieldGrp)
		UI_Globals.ShotgunDescription = self.ShotgunDescription

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(self.labelWidth, 300))

		self.ShotgunDetailLabel = pm.text(UI_Globals.ShotgunDetailLabel,
		                                  enable=False,
		                                  annotation="Details of the selected Shotgun entity to which the created Version will be attached.",
		                                  label="Selected Entity")
		isinstance(self.ShotgunDetailLabel, pm.uitypes.Text)
		UI_Globals.ShotgunDetailLabel = self.ShotgunDetailLabel

		self.ShotgunResultsBox = pm.scrollField(enable=False,
		                                        text=self.defaultRenderGlobals.deadlineSGDisplayInfo.get(""),
		                                        editable=False,
		                                        height=140,
		                                        width=325,
		                                        wordWrap=False)
		isinstance(self.ShotgunResultsBox, pm.uitypes.ScrollField)
		UI_Globals.ShotgunResultsBox = self.ShotgunResultsBox
	#----------------------------------------------------------------------
	def Build_Draft_Frame(self):
		""""""
		self.frw_Draft = pm.frameLayout(collapse=False,
		                                borderVisible=True,
		                                label="Draft",
		                                borderStyle="etchedIn",
		                                collapsable=True,
		                                labelVisible=True)
		isinstance(self.frw_Draft, pm.uitypes.FrameLayout)

		pm.columnLayout(columnAlign="left",
		                adjustableColumn=True,
		                columnAttach=("both", 4),
		                rowSpacing=4)

		pm.rowLayout(numberOfColumns=3,
		             cw3=(self.labelWidth, 180, 140))

		#dummy label
		pm.text(label="")
		self.SubmitDraftJob = pm.checkBox(UI_Globals.SubmitDraftJob,
		                                  annotation="Check to submit a Draft job in addition to the Maya job.",
		                                  enable=True,
		                                  changeCommand=self.On_User_DraftChanged,
		                                  value=self.defaultRenderGlobals.deadlineUseDraft.get(False),
		                                  label="Submit Draft Job On Completion")
		isinstance(self.SubmitDraftJob, pm.uitypes.CheckBox)
		UI_Globals.SubmitDraftJob = self.SubmitDraftJob

		self.UploadDraftToShotgun = pm.checkBox(UI_Globals.UploadDraftToShotgun,
		                                        annotation="Check to upload Draft output to Shotgun.",
		                                        enable=False,
		                                        changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                        value=self.defaultRenderGlobals.deadlineUploadDraftToShotgun.get(False),
		                                        label="Upload to Shotgun")
		isinstance(self.UploadDraftToShotgun, pm.uitypes.CheckBox)
		UI_Globals.UploadDraftToShotgun = self.UploadDraftToShotgun

		pm.setParent('..')

		self.DraftTemplate = pm.textFieldButtonGrp(UI_Globals.DraftTemplate,
		                                           text=self.defaultRenderGlobals.deadlineDraftTemplate.get(""),
		                                           changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                           label="Draft Template",
		                                           columnAlign=(1, "left"),
		                                           annotation="The path to the Draft Template to use.",
		                                           columnWidth=[(1, self.labelWidth), (2, 300)],
		                                           buttonLabel="...")
		isinstance(self.DraftTemplate, pm.uitypes.TextFieldButtonGrp)
		self.DraftTemplate.buttonCommand(partial(self.user_Input_Load_File_Dialog, self.DraftTemplate, 'Python_Script(*.py);;All Files (*)'))
		UI_Globals.DraftTemplate = self.DraftTemplate

		self.DraftUser = pm.textFieldGrp(UI_Globals.DraftUser,
		                                 enable=True,
		                                 changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                 text=self.defaultRenderGlobals.deadlineDraftUser.get(""),
		                                 columnWidth2=(self.labelWidth, 325),
		                                 label="User",
		                                 annotation="The name of the user (used by Draft templates).",
		                                 columnAlign2=("left", "left"))
		isinstance(self.DraftUser, pm.uitypes.TextFieldGrp)
		UI_Globals.DraftUser = self.DraftUser

		self.DraftEntity = pm.textFieldGrp(UI_Globals.DraftEntity,
		                                   enable=True,
		                                   text=self.defaultRenderGlobals.deadlineDraftEntity.get(""),
		                                   columnWidth2=(self.labelWidth, 325),
		                                   label="Entity",
		                                   changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                   annotation="The name of the entity (used by Draft templates).",
		                                   columnAlign2=("left", "left"))
		isinstance(self.DraftEntity, pm.uitypes.TextFieldGrp)
		UI_Globals.DraftEntity = self.DraftEntity

		self.DraftVersion = pm.textFieldGrp(UI_Globals.DraftVersion,
		                                    enable=True,
		                                    text=self.defaultRenderGlobals.deadlineDraftVersion.get(""),
		                                    columnWidth2=(self.labelWidth, 325),
		                                    label="Version",
		                                    changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                    annotation="The version name (used by Draft templates).",
		                                    columnAlign2=("left", "left"))
		isinstance(self.DraftVersion, pm.uitypes.TextFieldGrp)
		UI_Globals.DraftVersion = self.DraftVersion

		self.DraftExtraArgs = pm.textFieldGrp(UI_Globals.DraftExtraArgs,
		                                      enable=True,
		                                      text=self.defaultRenderGlobals.deadlineDraftExtraArgs.get(""),
		                                      columnWidth2=(self.labelWidth, 325),
		                                      label="Additional Args",
		                                      changeCommand=self._PD.SavePersistentDeadlineOptions,
		                                      annotation="The additional arguments (used by Draft templates).",
		                                      columnAlign2=("left", "left"))
		isinstance(self.DraftExtraArgs, pm.uitypes.TextFieldGrp)
		UI_Globals.DraftExtraArgs = self.DraftExtraArgs

		pm.rowLayout(numberOfColumns=2,
		             columnWidth2=(self.labelWidth, 325))
		#dummy label
		pm.text(label="")
		self.UseShotgunDataButton = pm.button(UI_Globals.UseShotgunDataButton,
		                                      width=200,
		                                      height=26,
		                                      command=self.Use_Shotgun_Values, 
		                                      annotation="Uses data from Shotgun to fill out the Draft settings.",
		                                      label="Use Shotgun Values")
		isinstance(self.UseShotgunDataButton, pm.uitypes.Button)
		UI_Globals.UseShotgunDataButton = self.UseShotgunDataButton
	#----------------------------------------------------------------------
	def UpdateJobType(self, *args, **kwargs):
		jobType  = self.MayaJobType.getSelect()
		jobValue = self.MayaJobType.getValue()
		renderer=str(Helpers.Data_Access.currentRenderer)

		self._render_options_dict = dict()
		self._render_options_dict['arnold']    = self.Maya_Render_Options_Arnold_FrameLayout
		self._render_options_dict['mentalRay'] = self.Maya_Render_Options_MentalRay_FrameLayout
		self._render_options_dict['vray']      = self.Maya_Render_Options_VRay_FrameLayout

		self._render_job_types_dict = dict()
		self._render_job_types_dict[self.MayaRenderJobType]      = [self.Maya_Render_Options_FrameLayout, self.Maya_Render_Options_Tile_FrameLayout]
		self._render_job_types_dict[self.MentalRayExportJobType] = [self.MentalRay_Export_FrameLayout, self.MentalRay_Export_Render_Job_FrameLayout]
		self._render_job_types_dict[self.VRayExportJobType]      = [self.Vray_Export_FrameLayout, self.Vray_Export_Render_Job_FrameLayout, self.Vray_Export_Vrimg_Job_FrameLayout]
		self._render_job_types_dict[self.RendermanExportJobType] = [self.Renderman_Export_FrameLayout, self.Renderman_Export_Render_Job_FrameLayout]
		self._render_job_types_dict[self.ArnoldExportJobType]    = [self.Arnold_Export_FrameLayout, self.Arnold_Export_Render_Job_FrameLayout]
		
		for frame in [self.Maya_Render_Options_FrameLayout,self.Maya_Render_Options_Arnold_FrameLayout,self.Maya_Render_Options_MentalRay_FrameLayout,self.Maya_Render_Options_VRay_FrameLayout,self.Maya_Render_Options_Tile_FrameLayout,self.MentalRay_Export_FrameLayout,self.MentalRay_Export_Render_Job_FrameLayout,self.Vray_Export_FrameLayout,self.Vray_Export_Render_Job_FrameLayout,self.Vray_Export_Vrimg_Job_FrameLayout,self.Renderman_Export_FrameLayout,self.Renderman_Export_Render_Job_FrameLayout,self.Arnold_Export_FrameLayout,self.Arnold_Export_Render_Job_FrameLayout, self.Vrimg2Exr_Conversion_Options_FrameLayout]:
			frame.setVisible(False)
		
		if not jobType == self.VRayExportJobType:
			self.MayaJobType.setSelect(self.VRayExportJobType)
			self.UpdateJobType()
		else:
			if jobType == self.MayaRenderJobType:
				self.Maya_Render_Options_FrameLayout.setVisible(True)
				self.Maya_Render_Options_Tile_FrameLayout.setVisible(True)
	
				if renderer == "arnold":
					self.Maya_Render_Options_Arnold_FrameLayout.setVisible(True)
				if renderer == "mentalRay":
					self.Maya_Render_Options_MentalRay_FrameLayout.setVisible(True)
				if renderer == "vray":
					self.Maya_Render_Options_VRay_FrameLayout.setVisible(True)
	
			elif jobType == self.MentalRayExportJobType:
				self.MentalRay_Export_FrameLayout.setVisible(True)
				self.MentalRay_Export_Render_Job_FrameLayout.setVisible(True)
	
			elif jobType == self.VRayExportJobType:
				self.Vray_Export_FrameLayout.setVisible(True)
				self.Vray_Export_Render_Job_FrameLayout.setVisible(True)
				self.Vray_Export_Vrimg_Job_FrameLayout.setVisible(True)
				self.Vrimg2Exr_Conversion_Options_FrameLayout.setVisible(True)
	
			elif jobType == self.RendermanExportJobType:
				self.Renderman_Export_FrameLayout.setVisible(True)
				self.Renderman_Export_Render_Job_FrameLayout.setVisible(True)
	
			elif jobType == self.ArnoldExportJobType:
				self.Arnold_Export_FrameLayout.setVisible(True)
				self.Arnold_Export_Render_Job_FrameLayout.setVisible(True)
	#----------------------------------------------------------------------	
	def Use_Shotgun_Values(self, *args):
		"""Use values from Shotgun to fill out the Draft fields"""
		task    = ""
		project = ""
		entity  = ""
		for i, key in enumerate(Shotgun_Globals.SGInfoKeys):
			value = Shotgun_Globals.SGInfoValues[i]
			if key == "UserName":
				self.DraftUser.setText(value)
			elif key == "DraftTemplate":
				self.DraftTemplate.setText(value)
			elif key == "TaskName":
				task    = value
			elif key == "ProjectName":
				project = value
			elif key == "EntityName":
				entity  = value


		if len(task)>0:
			self.DraftEntity.setText(task)
		elif len(project)>0 and len(entity)>0:
			self.DraftEntity.setText(project + " > " + entity)

		self.DraftVersion.setText(self.ShotgunVersion.getText())
	#----------------------------------------------------------------------	
	def user_Input_Load_File_Dialog(self, ui, filters="All(*)"):
		"""Set the file path in the text field"""
		text = ui.getText()
		if not len(text):
			text = cmds.workspace(q=True,active=True)
		newpath= DeadLine_Access.Select_FilenameLoad(text, filters)
		if newpath:
			ui.setText(newpath)
			self._PD.SavePersistentDeadlineOptions()
	#----------------------------------------------------------------------	
	def user_Input_Save_File_Dialog(self, ui, filters="All(*)"):
		"""Set the file path in the text field."""
		text = ui.getText()
		if not len(text):
			text = cmds.workspace(q=True,active=True)
		newpath= DeadLine_Access.Select_FilenameSave(text, filters)
		if newpath:
			ui.setText(newpath)
			self._PD.SavePersistentDeadlineOptions()	
	#----------------------------------------------------------------------	
	def user_Input_Directory_Dialog(self, ui, default=None):
		"""Set the directory in a the text field"""
		text = ui.getText()
		if not len(text):
			if default == None:
				text = cmds.workspace(q=True,active=True)
			else:
				text = default
		newdir = DeadLine_Access.Select_Directory(text)
		if newdir:
			ui.setText(newdir)
			self._PD.SavePersistentDeadlineOptions(ui)
	#----------------------------------------------------------------------
	def user_Input_Limit_Groups_Dialog(self):
		"""Set the limit groups in the limit group field."""
		text = self.Job_Limit_Groups.getText()
		newLimitGroups= DeadLine_Access.Select_LimitGroups(text)
		if newLimitGroups:
			self.Job_Limit_Groups.setText(newLimitGroups)
			self._PD.SavePersistentDeadlineOptions()
	#----------------------------------------------------------------------		
	def user_Input_Machine_List_Dialog(self, *args):
		"""Set the machine list in the machine list field."""
		text = self.Job_Machines_List.getText()
		newMachineList = DeadLine_Access.Select_MachineList(text)
		if newMachineList != "Action was cancelled by user":
			self.Job_Machines_List.setText(newMachineList)
			self._PD.SavePersistentDeadlineOptions()
	#----------------------------------------------------------------------		
	def user_Input_Dependencies_Dialog(self):
		"""Set the dependencies in the job dependency field."""
		text = self.Job_Dependencies_List.getText()
		newDependencies=DeadLine_Access.Select_Dependencies(text) 
		if newDependencies:
			self.Job_Dependencies_List.setText(newDependencies)
			self._PD.SavePersistentDeadlineOptions()
	#----------------------------------------------------------------------
	def SetJobName(self):
		"""Set the job name to be the scene name."""
		newJobName = Helpers.Data_Access.StrippedSceneFileName
		self.JobNameGrp.setText(newJobName)
		self._PD.SavePersistentDeadlineOptions()
	#----------------------------------------------------------------------
	def user_Input_Shotgun_Info_Dialog(self, *args):
		"""Pop a GUI prompting the user to enter in Shotgun info"""
		UI_Globals.DeadlineRepositoryRoot = DeadLine_Access.RepositoryRoot()
		script = UI_Globals.DeadlineRepositoryRoot + "\\events\\Shotgun\\ShotgunUI.py Maya"
		sgResults                         = DeadLine_Access.ExecuteScript(script)
		tempJobInfo                       = sgResults

		if len(tempJobInfo)>0:
			Shotgun_Globals.SGInfoKeys=[]
			Shotgun_Globals.SGInfoValues=[]
			keyCount=0
			displayValues=""
			for i, v in enumerate(tempJobInfo):
				if "=" in v:
					tokens = v.split("=")
					value=""
					if len(tokens)>1:
						key, value = tokens[0], tokens[1]
						if key == "VersionName":
							pm.textFieldGrp(UI_Globals.ShotgunVersion,text=value,enable=True,e=1)
							self._PD.AW_SG_VersionName.set(value)
						elif key == "Description":
							pm.textFieldGrp(UI_Globals.ShotgunDescription,text=value,enable=True,e=1)
							self._PD.AW_SG_Description.set(value)
						elif key == "UserName":
							displayValues+="User Name: " + value + "\n"
							self._PD.AW_SG_UserName.set(value)
						elif key == "TaskName":
							displayValues+="Task Name: " + value + "\n"
							self._PD.AW_SG_TaskName.set(value)
						elif key == "ProjectName":
							displayValues+="Project Name: " + value + "\n"
							self._PD.AW_SG_ProjectName.set(value)
						elif key == "EntityName":
							displayValues+="Entity Name: " + value + "\n"
							self._PD.AW_SG_EntityName.set(value)
						elif key == "EntityType":
							displayValues+="Entity Type: " + value + "\n"
							self._PD.AW_SG_EntityType.set(value)
						elif key == "DraftTemplate":
							displayValues+="DraftTemplate: " + value + "\n"
							self._PD.AW_SG_DraftTemplate.set(value)
						elif key == "TaskId":
							self._PD.AW_SG_TaskId.set(int(value))
						elif key == "EntityId":
							self._PD.AW_SG_EntityId.set(int(value))
						elif key == "ProjectId":
							self._PD.AW_SG_ProjectId.set(int(value))
						#put the key/value in the parallel arrays
						keyCount+=1
						Shotgun_Globals.SGInfoKeys.insert(keyCount,key)
						Shotgun_Globals.SGInfoValues.insert(keyCount,value)


			if keyCount>0:
				pm.text(self.ShotgunDetailLabel,enable=True,e=1)
				self.ShotgunResultsBox.setEnable(True)
				self.UseShotgunCheckBox.setEnable(True)
				self.UseShotgunCheckBox.setValue(True)
				self.ShotgunResultsBox.setText(displayValues)
				self._PD.SavePersistentDeadlineOptions()
				self.On_Use_ShotgunChanged()
	#----------------------------------------------------------------------
	def On_Use_ShotgunChanged(self, *args):
		_enable   = self.SubmitDraftJob.getValue()
		_sgEnable = self.UseShotgunCheckBox.getValue()
		enable    = _enable and _sgEnable
		self.UploadDraftToShotgun.setEnable(enable)
		self.UseShotgunDataButton.setEnable(enable)
		self.ShotgunVersion.setEnable(_sgEnable)
		self.ShotgunDescription.setEnable(_sgEnable)
		self.ShotgunResultsBox.setEnable(_sgEnable)
	#----------------------------------------------------------------------
	def On_User_DraftChanged(self, *args):
		enable       =  self.SubmitDraftJob.getValue()
		sgEnable     = self.UseShotgunCheckBox.getValue()
		both_enabled = enable and sgEnable
		self.UploadDraftToShotgun.setEnable(both_enabled)
		self.DraftTemplate.setEnable(enable)
		self.DraftUser.setEnable(enable)
		self.DraftEntity.setEnable(enable)
		self.DraftVersion.setEnable(enable)
		self.DraftExtraArgs.setEnable(enable)
		self.UseShotgunDataButton.setEnable(both_enabled)
		self._PD.SavePersistentDeadlineOptions()
	#----------------------------------------------------------------------
	def _SubmitDependentVRayJob(self,jobId):
		submitCounter=0
		layerCount=1
		submitLayers=int(False)
		currentRenderLayer = self.Data_Access.currentRenderLayer
		layerCount=len(self.Data_Access.valid_Render_Layers)
		if self.Data_Access.IsRenderLayersOn:
			submitLayers=True
		i=0
		for layer in self.Data_Access.valid_Render_Layers:
			job_info = Job_Data_Model.Job_Info_File()
			job_info.Plugin = "Vray"
			
			renderLayerName=layer.name()
			job_info.Name    = self._PD.deadlineJobName.get() + " -Vray " + renderLayerName
			job_info.Comment = self._PD.deadlineJobComment.get()
			job_info.Department = self._PD.deadlineDepartment.get()
			job_info.Frames  = self._PD.deadlineFramesList.get()
			job_info.Pool    = self._PD.deadlineJobPool.get()
			job_info.SecondaryPool = self._PD.deadlineJobSecondaryPool.get()
			job_info.Priority = self._PD.deadlineJobPriority.get()
			job_info.OnJobComplete = self._PD.deadlineJobOnCompleat.get()
			job_info.Group = self._PD.deadlineGroup.get()
			job_info.MachineLimit = self._PD.deadlineLimitCount.get()
			job_info.LimitGroups  = self._PD.deadlineLimitGroups.get()
			job_info.OutputFilenames = [renderLayerName+"_.vrimg"]
			job_info.OutputDirectorys = [os.path.dirname(self._PD.deadlineVRayFilename.get().replace("<Layer>", layer.name()))]
			job_info.JobDependencies = jobId
			job_info.ChunkSize = self._PD.deadlineChunkSize.get()
			job_info.IsBlacklist = self._PD.deadlineIsBlacklist.get()
			job_info.Machinelist = self._PD.deadlineMachineList.get()
			
			if self.UseShotgunCheckBox.getValue():
				job_info.Submit_To_ShotGun = self.UseShotgunCheckBox.getValue()
				job_info.SG_TaskName       = self._PD.AW_SG_TaskName.get()
				job_info.SG_ProjectName    = self._PD.AW_SG_ProjectName.get()
				job_info.SG_EntityName     = self._PD.AW_SG_EntityName.get()
				job_info.SG_VersionName    = self._PD.AW_SG_VersionName.get()
				job_info.SG_Description    = renderLayerName + "-" + self._PD.deadlineJobComment.get()
				job_info.SG_UserName       = self._PD.AW_SG_UserName.get()
				job_info.SG_Path_To_File   = Helpers.Data_Access.scene_File_Path
				job_info.SG_TaskId         = self._PD.AW_SG_TaskId.get()
				job_info.SG_ProjectId      = self._PD.AW_SG_ProjectId.get()
				job_info.SG_EntityId       = self._PD.AW_SG_EntityId.get()
				job_info.SG_EntityType     = self._PD.AW_SG_EntityType.get()
			
			# Select the render layer to make sure the render settings are updated
			try:
				set_Current_Render_Layer(layer)
			except:
				continue

			if renderLayerName=="defaultRenderLayer":
				renderLayerName="masterLayer"
			
			inputPath       = self._PD.deadlineVRayFilename.get().replace("<Layer>", layer.name()) + ".vrscene"
			outputFilename  = self._PD.deadlineVRayFilename.get().replace("<Layer>", layer.name()) + "_.vrimg"
			plugin_info     = Job_Data_Model.Vray_Standalone_Info_File(InputFilename=inputPath, OutputFilename=outputFilename)
			
			submiter = Job_Data_Model.Job_Submitter(job_info, plugin_info)
			submiter.Submit_the_job_to_Deadline()
			submitCounter+=1
			# Show results
			print "\n\nSubmission Results For Job " + submiter.job.Name + ":\n---------------------------------------------------------------------------\n" + submiter.submitResults + "\n"
			
			if self.Submit_Vrimg_2_Exr_Job.getValue():
				conver_job_info = Job_Data_Model.Job_Info_File()
				conver_job_info.Plugin        = "Vrimg2Exr"
				conver_job_info.Name          = self._PD.deadlineJobName.get() + " -Vrimg2Exr" + renderLayerName
				conver_job_info.Comment       = self._PD.deadlineJobComment.get() + " - " + renderLayerName
				conver_job_info.Department    = self._PD.deadlineDepartment.get()
				conver_job_info.Frames        = self._PD.deadlineFramesList.get()
				conver_job_info.Pool          = self._PD.deadlineJobPool.get()
				conver_job_info.SecondaryPool = self._PD.deadlineJobSecondaryPool.get()
				conver_job_info.Priority      = self._PD.deadlineJobPriority.get()
				conver_job_info.OnJobComplete = self._PD.deadlineJobOnCompleat.get()
				conver_job_info.Group         = self._PD.deadlineGroup.get()
				conver_job_info.MachineLimit  = self._PD.deadlineLimitCount.get()
				conver_job_info.LimitGroups   = self._PD.deadlineLimitGroups.get()
				conver_job_info.OutputFilenames  = [layer.name() + "_####.exr"]
				conver_job_info.OutputDirectorys = [os.path.dirname(self._PD.deadlineVRayFilename.get().replace("<Layer>", layer.name()))]
				conver_job_info.JobDependencies  = submiter.jobId
				conver_job_info.ChunkSize        = 1
				conver_job_info.IsBlacklist      = self._PD.deadlineIsBlacklist.get()
				conver_job_info.Machinelist      = self._PD.deadlineMachineList.get()
				
				conver_plugin_info = Job_Data_Model.Vray_Image_To_Exr_Info_File()
				conver_plugin_info.InputFile = self._PD.deadlineVRayFilename.get().replace("<Layer>", layer.name()) + "_0001.vrimg"
				conver_plugin_info.BufferSize = self.Vrimg2Exr_Conversion_Memory_Limit_Slider.getValue()
				conver_plugin_info.Compression    = self.Vrimg2Exr_Conversion_Compression_MenuGroup.getValue()
				conver_plugin_info.DataWindow = self.Vrimg2Exr_Conversion_Crop_EXR_CheckBox.getValue()
				conver_plugin_info.DeleteInputFiles = self._PD.deadlineDeleteVrimgFiles.get()
				conver_plugin_info.SetChannel = self.Vrimg2Exr_Conversion_Specify_Channel_CheckBox.getValue()
				conver_plugin_info.Channel = self.Vrimg2Exr_Conversion_Specify_Channel_TextField.getText()
				conver_submitter = Job_Data_Model.Job_Submitter(conver_job_info, conver_plugin_info)
				conver_submitter.Submit_the_job_to_Deadline()
				print "\n\nSubmission Results For Job " + conver_submitter.job.Name + ":\n---------------------------------------------------------------------------\n" + conver_submitter.submitResults + "\n"
				submitCounter+=1


		if submitLayers:
			pm.editRenderLayerGlobals(currentRenderLayer=currentRenderLayer)
			# Reselect the current render layer

		return submitCounter
	#----------------------------------------------------------------------
	def generate_render_layer_frames_list(self):
		""""""
		fromFrame,toFrame,byFrame = Helpers.Data_Access.frameRange
		if byFrame>1:
			return "%.0f-%.0fx%.0f" % (fromFrame, toFrame, byFrame)
		else:
			return "%.0f-%.0f" % (fromFrame, toFrame)
	#----------------------------------------------------------------------
	def generate_render_layer_job_name(self):
		jobName = self.JobNameGrp.getText()
		# Get The Current Render Layer
		currentRenderLayer = Helpers.Data_Access.currentRenderLayer
		# Check If The User Wants To Overide The Default Render Layer Output Data 
		# Otherwise use a standered nameing convenshion
		if self.override_layer_settings:
			# Get The Name Of The UI That This Render Layer Is Set To
			jobField = "frw_JobName_" + currentRenderLayer
			# Get The input text field value from the ui
			jobName  = str(pm.textFieldGrp(jobField,q=1,text=1))
		else:
			jobName += " - " + currentRenderLayer
		return jobName
	#----------------------------------------------------------------------
	def generate_Vray_Scene_Render_Layer_SubFolder_Paths(self):
		""""""
		vrayFilename = self.VRay_File_Name.getText()
		res = []
		if Helpers.Data_Access.IsRenderLayersOn:
			renderLayerList=pm.ls(exactType="renderLayer")
			for layer in renderLayerList:
				if not layer.isReferenced() and layer.renderable.get():
					layerPath = vrayFilename.replace("<Layer>", str(layer.name()))
					layerPath = os.path.dirname(layerPath)
					res.append(layerPath)
		return res
	#----------------------------------------------------------------------
	def _Write_Vray_Export_Job_Files_And_Submit(self,showDialog):
		# Get the deadline temp directory.
		job_Info =  Job_Data_Model.Maya_Job_Info_File(OutputDirectorys=self.vray_Scene_File_SubFolders)
		
		camera = self.Job_Render_Camera_List.getValue()
		job_Info.ChunkSize            = 10000
		
		# Create the plugin info file.
		plugin_Info = Job_Data_Model.Maya_Batch_Vray_Export_Info_File()
		plugin_Info.Animation = False
		
		submit_Info = Job_Data_Model.Job_Submitter(job_Info, plugin_Info)
		submit_Info.Submit_the_job_to_Deadline()
		# Submit the job to Deadline

		# Specify which renderer is being used.
		if showDialog:
			pm.confirmDialog(message=submit_Info.submitResults,button="Ok",parent=self._main_window,title="Submission Results")
		else:
			print "\n\nSubmission Results For Job " + job_Info.Name + ":\n---------------------------------------------------------------------------\n" + submit_Info.submitResults + "\n"
		return submit_Info
	#----------------------------------------------------------------------
	def _WriteJobFilesAndSubmit(self, renderer,showDialog,regionRendering,jobType,cameraOverride):
		#----------------------------------------------------------------------
		def generate_render_layer_frames_list():
			""""""
			fromFrame,toFrame,byFrame = Helpers.Data_Access.frameRange
			if byFrame>1:
				return "%.0f-%.0fx%.0f" % (fromFrame, toFrame, byFrame)
			else:
				return "%.0f-%.0f" % (fromFrame, toFrame)
		#----------------------------------------------------------------------
		def generate_render_layer_job_name():
			jobName = self.JobNameGrp.getText()
			# Get The Current Render Layer
			currentRenderLayer = pm.editRenderLayerGlobals(currentRenderLayer=1,query=1)
			# Check If The User Wants To Overide The Default Render Layer Output Data 
			# Otherwise use a standered nameing convenshion
			if self.override_layer_settings:
				# Get The Name Of The UI That This Render Layer Is Set To
				jobField = "frw_JobName_" + currentRenderLayer
				# Get The input text field value from the ui
				jobName  = str(pm.textFieldGrp(jobField,q=1,text=1))
			else:
				jobName += " - " + currentRenderLayer
			return jobName
		# Get the deadline temp directory.
		tempDir = DeadLine_Access.Get_CurrentUserHomeDirectory() + "\\temp"

		# Get the output file path and prefix.
		outputFilePath    = CheckSlashes(self.ImageOutputPathGrp.getText())
		mentalRayFilename = CheckSlashes(self.Job_MentalRay_File_Name.getText())
		vrayFilename      = CheckSlashes(self.VRay_File_Name.getText())


		# Get some initial settings.
		render_layers_on      = Helpers.Data_Access.IsRenderLayersOn
		useMayaBatchPlugin = self.Job_Use_Maya_Batch_Plugin.getValue()

		# Get Job Name and frame list from the input fields.
		jobName   = self.JobNameGrp.getText()
		frameList = self.FrameListGrp.getText()
		# If the submit each render layer check is on
		# Set the job name to the current render layer name.
		# Set the Frame List The current Render layer settings.
		if self.is_render_layers_on and self.is_maya_render_job and self.submit_each_render_layer:
			jobName   = generate_render_layer_job_name()
			frameList = generate_render_layer_frames_list()		


		# Get region rendering settings.
		tilesInX           = self.Job_Tiles_In_X.getValue()
		tilesInY           = self.Job_Tiles_In_Y.getValue()
		singleRegionJob    = self.Submit_Tiles_As_Single_Job_CheckBox.getValue(),
		singleRegionFrame  = self.Job_Tile_Single_Frame.getValue()
		singleRegionTiles  = 0
		singleRegionLeft   = ""
		singleRegionTop    = ""
		singleRegionRight  = ""
		singleRegionBottom = ""
		singleRegionPrefix = ""

		# Append tile information to job name if doing a region render.
		if self.is_maya_render_job and regionRendering:
			if not singleRegionJob:
				regionLeft  = self._PD.deadlineRegionLeft.get()
				regionTop   = self._PD.deadlineRegionTop.get()
				regionRight = self._PD.deadlineRegionRight.get()
				regionBottom= self._PD.deadlineRegionBottom.get()
				currX       = self._PD.deadlineCurrX.get()
				currY       = self._PD.deadlineCurrY.get()
				currTile    = self._PD.deadlineCurrTile.get()
				jobName     += " (Tile " + str(currTile) + " : " + str(currX) + "x" + str(currY) + " of " + str(tilesInX) + "x" + str(tilesInY) + ")"
			else:
				singleRegionTiles  = self._PD.deadlineRegionSingleTiles.get()
				singleRegionLeft   = self._PD.deadlineRegionSingleLeft.get()
				singleRegionTop    = self._PD.deadlineRegionSingleTop.get()
				singleRegionRight  = self._PD.deadlineRegionSingleRight.get()
				singleRegionBottom = self._PD.deadlineRegionSingleBottom.get()
				singleRegionPrefix = self._PD.deadlineRegionSinglePrefix.get()
				jobName+=" (Frame " + str(singleRegionFrame) + " - " + str(singleRegionTiles) + " Tiles)"

		camera=""
		# Figure out the camera to use (if specified).
		if cameraOverride != "":
			camera=cameraOverride
		else:
			selectedCamera = self.Job_Render_Camera_List.getValue()
			for cameraName in pm.mel.listTransforms("-cameras"):
				if cameraName == selectedCamera:
					camera=selectedCamera
					break

		if camera != "":
			jobName += " - " + camera

		submitFilename=str(CheckSlashes(tempDir + "\maya_deadline_info.job"))
		# Create the job info file.
		with file(submitFilename,"w") as fileId:
			if self.Job_Use_Maya_Batch_Plugin.getValue():
				fileId.write(("Plugin=MayaBatch\n"))
			else:
				fileId.write(("Plugin=MayaCmd\n"))

			Comment              = self.Job_Comment_Grp.getText()
			Pool                 = self.Job_Pools.getValue()
			MachineLimit         = self.Job_Limit_Count.getValue()
			Priority             = str(self.Job_Priority.getValue())
			OnJobComplete        = self.Job_On_Complete.getValue()
			TaskTimeoutMinutes   = str(self.Job_Slave_Timeout.getValue())
			MinRenderTimeMinutes = str(self.Job_Min_Slave_Timeout.getValue())
			ConcurrentTasks      = str(self.Job_Concurrent_Tasks.getValue())
			Department           = self.Job_Department_Grp.getText()
			Group                = self.Job_Goups.getValue()
			LimitGroups          = self.Job_Limit_Groups.getText()
			JobDependencies      = self.Job_Dependencies_List.getText()
			MachineList          = self.Job_Machines_List.getText()

			fileId.write(("Name="                 + jobName + "\n"))
			fileId.write(("Comment="              + str(Comment) + "\n"))
			fileId.write(("Pool="                 + str(Pool) + "\n"))
			fileId.write(("MachineLimit="         + str(MachineLimit) + "\n"))
			fileId.write(("Priority="             + str(Priority) + "\n"))
			fileId.write(("OnJobComplete="        + str(OnJobComplete) + "\n"))
			fileId.write(("TaskTimeoutMinutes="   + str(TaskTimeoutMinutes) + "\n"))
			fileId.write(("MinRenderTimeMinutes=" + str(MinRenderTimeMinutes) + "\n"))
			fileId.write(("ConcurrentTasks="      + str(ConcurrentTasks) + "\n"))
			fileId.write(("Department="           + str(Department) + "\n"))
			fileId.write(("Group="                + str(Group) + "\n"))
			fileId.write(("LimitGroups="          + str(LimitGroups) + "\n"))
			fileId.write(("JobDependencies="      + str(JobDependencies) + "\n"))

			if self.Job_Is_Blacklist.getValue():
				fileId.write(("Blacklist=" + str(MachineList) + "\n"))
			else:
				fileId.write(("Whitelist=" + str(MachineList) + "\n"))

			if self.Job_Submit_As_Suspended.getValue():
				fileId.write(("InitialStatus=Suspended\n"))

			if self.is_maya_render_job:
				counter=0
				currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
				if self.is_render_layers_on and not self.submit_each_render_layer:
					# Store the currently selected render layer
					currentRenderLayer= pm.PyNode(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
					# Loop through the render layer if the checkbox is on
					for layer in pm.ls(exactType="renderLayer"):
						# Only get output if this is not a referenced layer
						if not layer.isReferenced():
							# Only get output if the renderable attribute is on
							if layer.renderable.get():
								# Select the render layer to make sure the render settings are updated
								layer.setCurrent()
								tempOutputFilePath=outputFilePath
								if renderer == "renderMan":
									tempOutputFilePath=str(pm.mel.rmanGetImageDir())
									tempCurrentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
									if pm.mel.gmatch(tempCurrentRenderLayer, "defaultRenderLayer") == 1:
										tempOutputFilePath=tempOutputFilePath + "/masterLayer"
									else:
										tempOutputFilePath=tempOutputFilePath + "/" + tempCurrentRenderLayer

								if camera != "":
									outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(0, 0, layer.name(), camera)))
									if jobType == UI_Globals.MayaRenderJobType and regionRendering:
										if not singleRegionJob:
											outputPrefix=str(GetTileOutputPrefix(outputPrefix, currX, currY, tilesInX, tilesInY))


										else:
											outputPrefix=str(Helpers.GetOutputPrefix(1, singleRegionFrame, layer.name(), camera))


									fileId.write(("OutputFilename" + str(counter) + "=" + str(CheckSlashes(tempOutputFilePath + "/" + outputPrefix)) + "\n"))
									counter+=1


								else:
									cameraNames=pm.ls(type="camera")
									for cameraName in cameraNames:
										if cameraName.renderable.get():
											outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(0, 0, layer.name(), cameraName.name())))
											if jobType == UI_Globals.MayaRenderJobType and regionRendering:
												if not singleRegionJob:
													outputPrefix=str(GetTileOutputPrefix(outputPrefix, currX, currY, tilesInX, tilesInY))


												else:
													outputPrefix=str(Helpers.GetOutputPrefix(1, singleRegionFrame, layer.name(), cameraName.name()))


											fileId.write(("OutputFilename" + str(counter) + "=" + str(CheckSlashes(tempOutputFilePath + "/" + outputPrefix)) + "\n"))
											counter+=1

					pm.editRenderLayerGlobals(currentRenderLayer=currentRenderLayer)
					# Reselect the current render layer
				else:

					tempOutputFilePath=outputFilePath
					if renderer == "renderMan":
						tempOutputFilePath=str(pm.mel.rmanGetImageDir())
						if Helpers.Data_Access.IsRenderLayersOn and submitEachRenderLayer:
							currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
							if pm.mel.gmatch(currentRenderLayer, "defaultRenderLayer") == 1:
								tempOutputFilePath=tempOutputFilePath + "/masterLayer"


							else:
								tempOutputFilePath=tempOutputFilePath + "/" + currentRenderLayer



					if camera != "":
						outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(0, 0, currentRenderLayer, camera)))
						if jobType == UI_Globals.MayaRenderJobType and regionRendering:
							if not singleRegionJob:
								outputPrefix=str(GetTileOutputPrefix(outputPrefix, currX, currY, tilesInX, tilesInY))


							else:
								outputPrefix=str(Helpers.GetOutputPrefix(1, singleRegionFrame, currentRenderLayer, camera))


						fileId.write(("OutputFilename" + str(counter) + "=" + str(CheckSlashes(tempOutputFilePath + "/" + outputPrefix)) + "\n"))
						counter+=1


					else:
						cameraNames=pm.mel.listTransforms("-cameras")
						for cameraName in cameraNames:
							if IsCameraRenderable(cameraName):
								outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(0, 0, currentRenderLayer, cameraName)))
								#string $relatives[] = `listRelatives -s $cameraName`;
								#string $cameraShape = $relatives[0];
								#if( !IsDefaultCamera( $cameraShape ) )
								#if( `getAttr( $cameraShape + ".renderable" )` )
								if jobType == UI_Globals.MayaRenderJobType and regionRendering:
									if not singleRegionJob:
										outputPrefix=str(GetTileOutputPrefix(outputPrefix, currX, currY, tilesInX, tilesInY))


									else:
										outputPrefix=str(Helpers.GetOutputPrefix(1, singleRegionFrame, currentRenderLayer, cameraName))


								fileId.write(("OutputFilename" + str(counter) + "=" + str(CheckSlashes(tempOutputFilePath + "/" + outputPrefix)) + "\n"))
								counter+=1

			elif self.is_mentalRay_Export_Job:
				fileId.write(("OutputDirectory0=" + str(pm.mel.dirname(mentalRayFilename)) + "\n"))

			elif self.is_vray_export_job:
				fileId.write(("OutputDirectory0=" + str(os.path.dirname(vrayFilename)) + "\n"))

			elif self.is_renderman_export_job:
				fileId.write(("OutputDirectory0=" + str(CheckSlashes(str(pm.textFieldGrp('frw_projectPath',q=1,text=1)) + "/renderman/" + str(Helpers.Data_Access.StrippedSceneFileName))) + "\n"))

			elif self.is_arnold_export_Job:
				fileId.write(("OutputDirectory0=" + str(CheckSlashes(str(pm.textFieldGrp('frw_projectPath',q=1,text=1)) + "/data")) + "\n"))

			if self.is_maya_render_job and regionRendering and singleRegionJob:
				fileId.write(("TileJob=True\n"))
				fileId.write(("TileJobFrame=" + str(singleRegionFrame) + "\n"))
				fileId.write(("TileJobTilesInX=" + str(tilesInX) + "\n"))
				fileId.write(("TileJobTilesInY=" + str(tilesInY) + "\n"))

			elif self.is_maya_render_job and self.submit_each_render_layer:
				if self.override_layer_settings:
					currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
					field="frw_FrameList_" + currentRenderLayer
					fileId.write(("Frames=" + str(pm.textFieldGrp(field,q=1,text=1)) + "\n"))
					field="frw_FrameGroup_" + currentRenderLayer
					fileId.write(("ChunkSize=" + str(pm.intSliderGrp(field,q=1,v=1)) + "\n"))
				else:
					fileId.write(("Frames=" + frameList + "\n"))
					fileId.write(("ChunkSize=" + str(self.Job_Chunk_Size.getValue()) + "\n"))
			else:
				fileId.write(("Frames=" + frameList + "\n"))
				# Regular renders and Arnold exports can be split across machines, but other exports (AFAIK) must be done on a single machine.
				if self.is_maya_render_job or self.is_arnold_export_Job:
					fileId.write(("ChunkSize=" + str(self.Job_Chunk_Size.getValue()) + "\n"))
				else:
					fileId.write(("ChunkSize=100000\n"))

			if self.is_maya_render_job and regionRendering and useMayaBatchPlugin and renderer == "vray":
				fileId.write(("ForceReloadPlugin=True\n"))
			kvpIndex=0
			#============================================
			#  SHOTGUN
			if self.UseShotgunCheckBox.getValue() and not self.is_vray_export_job:
				for i, v in enumerate(Shotgun_Globals.SGInfoKeys):
					if v == "TaskName":
						fileId.write(("ExtraInfo0=" + Shotgun_Globals.SGInfoValues[i] + "\n"))
					elif v == "ProjectName":
						fileId.write(("ExtraInfo1=" + Shotgun_Globals.SGInfoValues[i] + "\n"))
					elif v == "EntityName":
						fileId.write(("ExtraInfo2=" + Shotgun_Globals.SGInfoValues[i] + "\n"))
					elif v == "UserName":
						fileId.write(("ExtraInfo5=" + Shotgun_Globals.SGInfoValues[i] + "\n"))
					elif v != "DraftTemplate":
						fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=" + v + "=" + Shotgun_Globals.SGInfoValues[i] + "\n"))
						#DON'T put in the Draft template -- if we're doing Draft, let Draft put that stuff in
						kvpIndex+=1

				fileId.write(("ExtraInfo3=" + str(self.ShotgunVersion.getText()) + "\n"))
				fileId.write(("ExtraInfo4=" + str(self.ShotgunDescription.getText()) + "\n"))

			if self.SubmitDraftJob.getValue():
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftTemplate=" + str(pm.textFieldButtonGrp(UI_Globals.DraftTemplate,q=1,text=1)) + "\n"))
				#============================================
				kvpIndex+=1
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftUsername=" + str(pm.textFieldGrp(UI_Globals.DraftUser,q=1,text=1)) + "\n"))
				kvpIndex+=1
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftEntity=" + str(pm.textFieldGrp(UI_Globals.DraftEntity,q=1,text=1)) + "\n"))
				kvpIndex+=1
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftVersion=" + str(pm.textFieldGrp(UI_Globals.DraftVersion,q=1,text=1)) + "\n"))
				kvpIndex+=1
				res=Helpers.Data_Access.globalsResolution
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftFrameWidth=" + str(res[0]) + "\n"))
				kvpIndex+=1
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftFrameHeight=" + str(res[1]) + "\n"))
				kvpIndex+=1
				if pm.checkBox(UI_Globals.UploadDraftToShotgun,q=1,value=1) and pm.checkBox(UI_Globals.UploadDraftToShotgun,q=1,enable=1):
					fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftUploadToShotgun=True\n"))


				else:
					fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftUploadToShotgun=False\n"))

				kvpIndex+=1
				fileId.write(("ExtraInfoKeyValue" + str(kvpIndex) + "=DraftExtraArgs=" + str(pm.textFieldGrp(UI_Globals.DraftExtraArgs,q=1,text=1)) + "\n"))
				kvpIndex+=1

		# Create the plugin info file.
		jobFilename=str(CheckSlashes(tempDir + "\maya_deadline_job.job"))
		with file(jobFilename,"w") as fileId:

			fileId.write(("Animation=" + str(Helpers.Data_Access.IsAnimatedOn) + "\n"))

			if self.is_mentalRay_Export_Job:
				fileId.write(("Renderer=mentalRayExport\n"))
				fileId.write(("UsingRenderLayers=false\n"))
				fileId.write(("MentalRayExportfile=" + mentalRayFilename + "\n"))
				fileId.write(("MentalRayExportBinary=" + str(((pm.radioButton('MayatomrExport_Binary',query=1,select=1)) and 1 or 0)) + "\n"))
				fileId.write("MentalRayExportTabStop=" + str( tabstop=pm.intField('MayatomrExport_TabSize',query=1,value=1) ) + "\n")
				perframe=0
				padframe=0
				if pm.checkBoxGrp('MayatomrExport_FilePerFrame',query=1,value1=1):
					perframe=int(pm.optionMenuGrp('MayatomrExport_FrameExtension',q=1,select=1))
					padframe=int(pm.intFieldGrp('MayatomrExport_FramePadding',q=1,value1=1))
					if padframe>9:
						padframe=9


				fileId.write(("MentalRayExportPerFrame=" + str(perframe) + "\n"))
				fileId.write(("MentalRayExportPadFrame=" + str(padframe) + "\n"))
				fileId.write(("MentalRayExportPerLayer=" + str(pm.checkBoxGrp('MayatomrExport_FilePerLayer',query=1,value1=1)) + "\n"))
				pathnames=""
				if pm.checkBoxGrp('MayatomrExport_Pathes',query=1,value1=1):
					for cnt in range(0,len(pm.melGlobals['gExportPathesCheckBoxes'])):
						pathnames+=pm.optionMenuGrp(pm.melGlobals['gExportPathesCheckBoxes'][cnt],
						                            query=1,sl=1)



				else:
					pathnames="n"

				fileId.write(("MentalRayExportPathNames=" + str(pathnames) + "\n"))
				fragment=(pm.optionMenuGrp('MayatomrExport_Fragment',q=1,select=1) - 1)
				fileId.write(("MentalRayExportFragment=" + str(fragment) + "\n"))
				fileId.write(("MentalRayExportFragmentMaterials=" + str(((pm.checkBoxGrp('MayatomrExport_FragmentMaterials',q=1,v1=1)) and 1 or 0)) + "\n"))
				fileId.write(("MentalRayExportFragmentShaders=" + str(((pm.checkBoxGrp('MayatomrExport_FragmentIncomingShdrs',q=1,v1=1)) and 1 or 0)) + "\n"))
				fileId.write(("MentalRayExportFragmentChildDag=" + str(((pm.checkBoxGrp('MayatomrExport_FragmentChildDag',q=1,v1=1)) and 1 or 0)) + "\n"))
				fileId.write(("MentalRayExportPassContributionMaps=" + str(((pm.checkBoxGrp('MayatomrExport_PassContributionMaps',q=1,v1=1)) and 1 or 0)) + "\n"))
				fileId.write(("MentalRayExportPassUserData=" + str(((pm.checkBoxGrp('MayatomrExport_PassUserData',q=1,v1=1)) and 1 or 0)) + "\n"))
				filter=""
				if pm.checkBoxGrp('MayatomrExport_Filters',query=1,value1=1):
					for cnt in range(0,len(pm.melGlobals['gExportFilterCheckBoxes'])):
						filter+=(pm.checkBoxGrp(pm.melGlobals['gExportFilterCheckBoxes'][cnt],
						                        query=1,value1=1))
						filter and "0" or "1"


				fileId.write(("MentalRayExportFilterString=" + str(filter) + "\n"))

			elif self.is_vray_export_job:
				fileId.write(("Renderer=vrayExport\n"))
				fileId.write(("VRayExportFile=" + vrayFilename + "\n"))


			elif self.is_renderman_export_job:
				fileId.write(("Renderer=rendermanExport\n"))
				fileId.write(("MaxProcessors=" + str(self.ExportPRManThreads.getValue()) + "\n"))


			elif self.is_arnold_export_Job:
				fileId.write(("Renderer=arnoldExport\n"))


			else:
				renderHalfFrames    = int(self.Data_Access.ShowHalfFramesOption and self.Render_Half_Frames_CheckBox.getValue() or 0)
				strictErrorChecking = int(self.Job_Strict_Error_Checking.getValue())
				localRendering      = int(self.Job_Local_Rendering.getValue())
				currentRenderLayer  = str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))

				fileId.write(("Renderer=" + renderer + "\n"))
				fileId.write(("UsingRenderLayers=" + str(Helpers.Data_Access.IsRenderLayersOn) + "\n"))
				fileId.write(("RenderLayer=" + currentRenderLayer + "\n"))
				fileId.write(("RenderHalfFrames=" + str(renderHalfFrames) + "\n"))
				fileId.write(("LocalRendering=" + str(localRendering) + "\n"))
				fileId.write(("StrictErrorChecking=" + str(strictErrorChecking) + "\n"))
				if regionRendering:
					fileId.write(("RegionRendering=True\n"))
					if not singleRegionJob:
						fileId.write(("RegionLeft=" + str(regionLeft) + "\n"))
						fileId.write(("RegionTop=" + str(regionTop) + "\n"))
						fileId.write(("RegionRight=" + str(regionRight) + "\n"))
						fileId.write(("RegionBottom=" + str(regionBottom) + "\n"))
					else:
						fileId.write((singleRegionLeft + "\n"))
						fileId.write((singleRegionTop + "\n"))
						fileId.write((singleRegionRight + "\n"))
						fileId.write((singleRegionBottom + "\n"))
						fileId.write((singleRegionPrefix + "\n"))


				if self.Data_Access.EnableCpuOption:
					fileId.write(("MaxProcessors=" + str(self.Job_Max_Cpus.getValue()) + "\n"))

				if renderer == "mayaSoftware":
					rendQual=pm.listConnections('defaultRenderGlobals.qual')
					# render globals qualification
					# get antialising quality level and turn it into a string
					intAntialiasing=int(pm.getAttr(rendQual[0] + ".edgeAntiAliasing"))
					if intAntialiasing == 1:
						strAntialiasing="high"

					if intAntialiasing == 2:
						strAntialiasing="medium"

					if intAntialiasing == 3:
						strAntialiasing="low"

					else:
						strAntialiasing="highest"

					fileId.write(("AntiAliasing=" + strAntialiasing + "\n"))

				if useMayaBatchPlugin and renderer == "MayaKrakatoa":
					boolVal=""
					# Krakatoa options currently only supported by the MayaBatch plugin.
					krakatoaFinalPassDensity=float(pm.getAttr("MayaKrakatoaRenderSettings.finalPassDensity"))
					fileId.write(("KrakatoaFinalPassDensity=" + str(krakatoaFinalPassDensity) + "\n"))
					krakatoaFinalPassDensityExponent=int(pm.getAttr("MayaKrakatoaRenderSettings.finalPassDensityExponent"))
					fileId.write(("KrakatoaFinalPassDensityExponent=" + str(krakatoaFinalPassDensityExponent) + "\n"))
					krakatoaUseLightingPassDensity=int(pm.getAttr("MayaKrakatoaRenderSettings.useLightingPassDensity"))
					if krakatoaUseLightingPassDensity == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaUseLightingPassDensity=" + boolVal + "\n"))
					krakatoaLightingDensity=float(pm.getAttr("MayaKrakatoaRenderSettings.lightingPassDensity"))
					fileId.write(("KrakatoaLightingPassDensity=" + str(krakatoaLightingDensity) + "\n"))
					krakatoaLightingDensityExponent=int(pm.getAttr("MayaKrakatoaRenderSettings.lightingPassDensityExponent"))
					fileId.write(("KrakatoaLightingPassDensityExponent=" + str(krakatoaLightingDensityExponent) + "\n"))
					krakatoaUseEmissionStrength=int(pm.getAttr("MayaKrakatoaRenderSettings.useEmissionStrength"))
					if krakatoaUseEmissionStrength == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaUseEmissionStrength=" + boolVal + "\n"))
					krakatoaEmissionStrength=float(pm.getAttr("MayaKrakatoaRenderSettings.emissionStrength"))
					fileId.write(("KrakatoaEmissionStrength=" + str(krakatoaEmissionStrength) + "\n"))
					krakatoaEmissionStrengthExponent=int(pm.getAttr("MayaKrakatoaRenderSettings.emissionStrengthExponent"))
					fileId.write(("KrakatoaEmissionStrengthExponent=" + str(krakatoaEmissionStrengthExponent) + "\n"))
					krakatoaUseEmission=int(pm.getAttr("MayaKrakatoaRenderSettings.useEmission"))
					if krakatoaUseEmission == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaUseEmission=" + boolVal + "\n"))
					krakatoaUseAbsorption=int(pm.getAttr("MayaKrakatoaRenderSettings.useAbsorption"))
					if krakatoaUseAbsorption == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaUseAbsorption=" + boolVal + "\n"))
					krakatoaEnableMotionBlur=int(pm.getAttr("MayaKrakatoaRenderSettings.enableMotionBlur"))
					if krakatoaEnableMotionBlur == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableMotionBlur=" + boolVal + "\n"))
					krakatoaMotionBlurParticleSegments=int(pm.getAttr("MayaKrakatoaRenderSettings.motionBlurParticleSegments"))
					fileId.write(("KrakatoaMotionBlurParticleSegments=" + str(krakatoaMotionBlurParticleSegments) + "\n"))
					krakatoaJitteredMotionBlur=int(pm.getAttr("MayaKrakatoaRenderSettings.jitteredMotionBlur"))
					if krakatoaJitteredMotionBlur == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaJitteredMotionBlur=" + boolVal + "\n"))
					krakatoaShutterAngle=float(pm.getAttr("MayaKrakatoaRenderSettings.shutterAngle"))
					fileId.write(("KrakatoaShutterAngle=" + str(krakatoaShutterAngle) + "\n"))
					krakatoaEnableDOF=int(pm.getAttr("MayaKrakatoaRenderSettings.enableDOF"))
					if krakatoaEnableDOF == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableDOF=" + boolVal + "\n"))
					krakatoaSampleRateDOF=float(pm.getAttr("MayaKrakatoaRenderSettings.sampleRateDOF"))
					fileId.write(("KrakatoaSampleRateDOF=" + str(krakatoaSampleRateDOF) + "\n"))
					krakatoaEnableMatteObjects=int(pm.getAttr("MayaKrakatoaRenderSettings.enableMatteObjects"))
					if krakatoaEnableMatteObjects == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableMatteObjects=" + boolVal + "\n"))
					krakatoaEnableOverrideBG=int(pm.getAttr("MayaKrakatoaRenderSettings.overrideBG"))
					if krakatoaEnableOverrideBG == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableOverrideBG=" + boolVal + "\n"))
					#float $krakatoaBGOverride[] = `getAttr "MayaKrakatoaRenderSettings.backgroundColor"`;
					#fprint $fileId ( "KrakatoaBGOverride=" + $krakatoaBGOverride[0]+ " "+ $krakatoaBGOverride[1] + " " + $krakatoaBGOverride[2] + "\n" );
					krakatoaEnableOverrideColor=int(pm.getAttr("MayaKrakatoaRenderSettings.overrideColor"))
					if krakatoaEnableOverrideColor == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableOverrideColor=" + boolVal + "\n"))
					#float $krakatoaColorOverride[] = `getAttr "MayaKrakatoaRenderSettings.colorChannelOverride"`;
					#fprint $fileId ( "KrakatoaColorOverride=" + $krakatoaColorOverride[0]+ " "+ $krakatoaColorOverride[1] + " " + $krakatoaColorOverride[2] + "\n" );
					krakatoaEnableOverrideEmission=int(pm.getAttr("MayaKrakatoaRenderSettings.overrideEmission"))
					if krakatoaEnableOverrideEmission == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableOverrideEmission=" + boolVal + "\n"))
					#float $krakatoaEmissionOverride[] = `getAttr "MayaKrakatoaRenderSettings.emissionChannelOverride"`;
					#fprint $fileId ( "KrakatoaEmissionOverride=" + $krakatoaEmissionOverride[0]+ " "+ $krakatoaEmissionOverride[1] + " " + $krakatoaEmissionOverride[2] + "\n" );
					krakatoaEnableOverrideAbsorption=int(pm.getAttr("MayaKrakatoaRenderSettings.overrideAbsorption"))
					if krakatoaEnableOverrideAbsorption == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaEnableOverrideAbsorption=" + boolVal + "\n"))
					#float $krakatoaAbsorptionOverride[] = `getAttr "MayaKrakatoaRenderSettings.absorptionChannelOverride"`;
					#fprint $fileId ( "krakatoaAbsorptionOverride=" + $krakatoaAbsorptionOverride[0]+ " "+ $krakatoaAbsorptionOverride[1] + " " + $krakatoaAbsorptionOverride[2] + "\n" );
					krakatoaRenderingMethod=str(pm.getAttr(asString="MayaKrakatoaRenderSettings.renderingMethod"))
					fileId.write(("KrakatoaRenderingMethod=" + krakatoaRenderingMethod + "\n"))
					if krakatoaRenderingMethod == "Voxels":
						krakatoaVoxelSize=float(pm.getAttr("MayaKrakatoaRenderSettings.voxelSize"))
						fileId.write(("KrakatoaVoxelSize=" + str(krakatoaVoxelSize) + "\n"))
						krakatoaVoxelFilterRadius=float(pm.getAttr("MayaKrakatoaRenderSettings.voxelFilterRadius"))
						fileId.write(("KrakatoaVoxelFilterRadius=" + str(krakatoaVoxelFilterRadius) + "\n"))

					krakatoaForceEXROutput=int(pm.getAttr("MayaKrakatoaRenderSettings.forceEXROutput"))
					if krakatoaForceEXROutput == 1:
						boolVal="True"


					else:
						boolVal="False"

					fileId.write(("KrakatoaForceEXROutput=" + boolVal + "\n"))

				if renderer == "arnold":
					arnoldVerbose=str(pm.optionMenuGrp('frw_arnoldVerbose',q=1,value=1))
					fileId.write(("ArnoldVerbose=" + arnoldVerbose + "\n"))

				if renderer == "mentalRay":
					mentalRayVerbose=str(pm.optionMenuGrp('frw_mentalRayVerbose',q=1,value=1))
					fileId.write(("MentalRayVerbose=" + mentalRayVerbose + "\n"))
					autoMemoryLimit=int(pm.checkBox('frw_autoMemoryLimit',q=1,value=1))
					fileId.write(("AutoMemoryLimit=" + str(autoMemoryLimit) + "\n"))
					memoryLimit=int(pm.intSliderGrp('frw_memoryLimit',q=1,v=1))
					fileId.write(("MemoryLimit=" + str(memoryLimit) + "\n"))

				if renderer == "vray":
					if useMayaBatchPlugin:
						fileId.write(("VRayAutoMemoryEnabled=" + str(self.Job_Vray_Auto_Memory_Enabled.getValue()) + "\n"))
						fileId.write(("VRayAutoMemoryBuffer=" + str(self.Job_Vray_Auto_Memory_Buffer.getValue()) + "\n"))

				if renderer == "maxwell":
					fileId.write(("MaxwellRenderTime=" + str(pm.getAttr("maxwellRenderOptions.renderTime")) + "\n"))
					fileId.write(("MaxwellSamplingLevel=" + str(pm.getAttr("maxwellRenderOptions.samplingLevel")) + "\n"))
					fileId.write(("MaxwellResumeRender=false\n"))

				if renderer == "OctaneRender":
					fileId.write(("OctaneMaxSamples=" + str(pm.getAttr("octaneSettings.MaxSamples")) + "\n"))

			fileId.write(("Version=" + str(Helpers.Data_Access.mayaVersion) + "\n"))
			fileId.write(("Build=" + str(self.mayaBuildBox.getValue()) + "\n"))
			fileId.write(("ProjectPath=" + str(self.ProjectPathGrp.getText()) + "\n"))
			if not useMayaBatchPlugin:
				fileId.write(("CommandLineOptions=" + str(self.Job_Maya_Command_Line_Args.getText()) + "\n"))
			else:
				fileId.write(("StartupScript=" + str(self.Job_Startup_Script_Path.getText()) + "\n"))

			res=Helpers.Data_Access.globalsResolution
			fileId.write(("ImageWidth=" + str(res[0]) + "\n"))
			fileId.write(("ImageHeight=" + str(res[1]) + "\n"))
			fileId.write(("OutputFilePath=" + outputFilePath + "\n"))
			if Helpers.Data_Access.IsRenderLayersOn and not self.submit_each_render_layer:
				fileId.write(("OutputFilePrefix=\n"))


			else:
				mayaOutputFilePrefix=str(GetMayaOutputPrefix(camera))
				if self.is_maya_render_job and regionRendering:
					mayaOutputFilePrefix=str(GetTileOutputPrefix(mayaOutputFilePrefix, currX, currY, tilesInX, tilesInY))
					if renderer == "renderMan":
						mayaOutputFilePrefix="_" + mayaOutputFilePrefix

				fileId.write(("OutputFilePrefix=" + mayaOutputFilePrefix + "\n"))

			fileId.write(("Camera=" + camera + "\n"))

			# If the user has specified a camera, make it the default
			# Now list all the camera options
			fileId.write(("Camera0=\n"))
			cameraNames=pm.mel.listTransforms("-cameras")
			for i, v in enumerate(cameraNames):
				fileId.write(("Camera" + str(i+1) + "=" + v + "\n"))

			sceneFilePath=str(CheckSlashes(pm.cmds.file(q=1,sceneName=1)))
			submitMayaSceneFile=int(self.Job_submit_Maya_Scene.getValue())
			if not submitMayaSceneFile:
				fileId.write(("SceneFile=" + sceneFilePath + "\n"))

			ignoreError211=int(self.IgnoreError211.getValue())
			fileId.write(("IgnoreError211=" + str(ignoreError211) + "\n"))

		# Submit the job to Deadline
		submissionCommand= submitFilename + " " + jobFilename
		if submitMayaSceneFile:
			submissionCommand+=" " + sceneFilePath
		Result, jobId , submitResults = DeadLine_Access.Submit_Deadline_Job(submitFilename, jobFilename)


		# Specify which renderer is being used.
		if self.is_mentalRay_Export_Job:
			submitResults=submitResults + "\n\nUsing renderer: mentalRayExport\n"
		elif self.is_vray_export_job:
			submitResults=submitResults + "\n\nUsing renderer: vrayExport\n"
		elif self.is_renderman_export_job:
			submitResults=submitResults + "\n\nUsing renderer: rendermanExport\n"
		elif self.is_arnold_export_Job:
			submitResults=submitResults + "\n\nUsing renderer: arnoldExport\n"
		else:
			submitResults=submitResults + "\n\nUsing renderer: " + renderer + "\n"
		if showDialog:
			pm.confirmDialog(message=submitResults,button="Ok",parent=self._main_window,title="Submission Results")
		else:
			print "\n\nSubmission Results For Job " + jobName + ":\n---------------------------------------------------------------------------\n" + submitResults + "\n"
		return jobId
	#----------------------------------------------------------------------
	def _Run_Vray_Export_Checks(self):
		""""""
		outputFilePath      = CheckSlashes(self.ImageOutputPathGrp.getText())
		vrimgOutputPrefix   = str(CheckSlashes(Helpers.GetOutputPrefix(0, 0, "", "")))
		vrimgOutputFilename = str(CheckSlashes(outputFilePath + "/" + vrimgOutputPrefix))
		for path in self.vray_Scene_File_SubFolders:
			if not os.path.exists(path):
				os.makedirs(path)
		vrayFilename  = path
		# Get The Directory Path From The Vray File Path
		vrayPath=os.path.dirname(vrayFilename)
		# Check To Make Sure Directory Exists
		message = ""
		if not os.path.isdir( vrayPath ):
			message=message + "VRay export path \"" + vrayPath + "\" does not exist!  Your VRay files will be lost!\n\n"
		# Check If vrayFilename Is on a local drive
		elif IsLocalDrive(vrayFilename):
			message=message + "VRay output file \"" + vrayFilename + "\" is on a local drive.\nSlaves will not be able to copy the exported VRay files to this drive.\n\n"
		# Check If vrayFilename has been set
		elif len(vrayFilename) == 0:
			message=message + "VRay output file is blank! Your exported VRay files will be lost!\n\n"

		if self.Submit_VRay_Job.getValue() and pm.getAttr("vraySettings.misc_separateFiles"):
			message=message + "Dependent VRay standalone job option is not compatible with the 'Separate Files' option in the VRay Translator settings. No dependent jobs will be submitted.\n\n"

		if self.Submit_Vrimg_2_Exr_Job.getValue():
			if pm.mel.fileExtension(vrimgOutputFilename) != "vrimg":
				message=message + "Dependent Vrimg2Exr job is enabled, but the output format is not vrimg!\n\n"

		return message
	#----------------------------------------------------------------------
	def _Submit_Vray_Export_Job(self):
		submitCounter=0
		submit_info = self._Write_Vray_Export_Job_Files_And_Submit(0)
		submitCounter+=1
		if self.Submit_VRay_Job.getValue():
			if not pm.getAttr("vraySettings.misc_separateFiles"):
				submitCounter = submitCounter + self._SubmitDependentVRayJob(submit_info.jobId)
				
		pm.confirmDialog(message=("Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."),button="Close",parent=self._main_window,title="Submission Results")
	#----------------------------------------------------------------------
	def _save_scene(self):
		""""""
		# Save scene, if necessary
		if pm.cmds.file(q=1,modified=1):
			print "Maya scene has been modified, saving file\n"
			pm.cmds.file()
		else:
			print "Maya scene has not been modified, skipping save\n"
	#----------------------------------------------------------------------
	def Run_Pre_Submit_Checks(self):
		""""""
		# Get the current renderer
		renderer = Helpers.Data_Access.currentRenderer
		# Check if we are doing a mental ray export
		jobType=self.MayaJobType.getSelect()
		# Check all the paths for problems, and warn the user if any are found
		projectPath           = CheckSlashes(self.ProjectPathGrp.getText())
		outputFilePath        = CheckSlashes(self.ImageOutputPathGrp.getText())
		sceneFilePath         = CheckSlashes(pm.cmds.file(q=1,sceneName=1))
		mentalRayFilename     = CheckSlashes(self.Job_MentalRay_File_Name.getText())
		vrayFilename          = CheckSlashes(self.VRay_File_Name.getText())
		submitMayaSceneFile   = self.Job_submit_Maya_Scene.getValue()
		submitEachRenderLayer = int(Helpers.Data_Access.IsRenderLayersOn and self.Job_Submit_Each_Render_Layer.getValue() or False)
		regionRendering       = int(self.RegionRendering_CheckBox.getValue())
		exportDependentJob    = int(False)
		submitDependentJob    = int(self.Submit_VRay_Job.getValue())
		message=""

		if not self.Job_submit_Maya_Scene.getValue() and IsLocalDrive(sceneFilePath):
			message = "Maya Scene file, " + repr(sceneFilePath) + " is on a local drive and is not being submitted.\nSlaves will not be able to access the scene file.\n\n"

		if IsLocalDrive(projectPath):
			message=message + "Project path, " + repr(projectPath) + " is on a local drive.\nParticle caching and other Maya features will not be available.\n\n"


		# Submit MentalRay Export JobType
		if jobType == UI_Globals.MentalRayExportJobType:
			if pm.radioButton('MayatomrExport_Binary',query=1,select=1):
				result=str(pm.confirmDialog(parent=self._main_window,title="Error Reading Export Options",cancelButton="Cancel",defaultButton="Export Settings...",message="Could not read in Mental Ray Export settings. Please ensure that the Mental Ray Export settings dialog is open when submitting the job to Deadline.",button=["Export Settings...", "Cancel"]))
				if result == "Export Settings...":
					OpenExportSettings()

				return False

			mentalRayPath=str(pm.mel.dirname(mentalRayFilename))
			if not os.path.isdir( mentalRayPath ):
				message=message + "Mental Ray output path \"" + mentalRayPath + "\" does not exist!  Your Mental Ray files will be lost!\n\n"


			elif IsLocalDrive(mentalRayFilename):
				message=message + "Mental Ray output file \"" + mentalRayFilename + "\" is on a local drive.\nSlaves will not be able to copy the Mental Ray files to this drive.\n\n"


			elif len(mentalRayFilename) == 0:
				message=message + "Mental Ray output file is blank! Your Mental Ray files will be lost!\n\n"

			exportDependentJob=int(pm.checkBox(UI_Globals.SubmitMentalRayJob,q=1,v=1))
		# Submit Vray Export JobType
		elif jobType == UI_Globals.VRayExportJobType:
			message += self._Run_Vray_Export_Checks()

		# Submit Renderman Export JobType
		elif jobType == UI_Globals.RendermanExportJobType:
			exportDependentJob=int(pm.checkBox(UI_Globals.SubmitPRManJob,q=1,v=1))
		# Submit Arnold Export JobType
		elif jobType == UI_Globals.ArnoldExportJobType:
			exportDependentJob=int(pm.checkBox(UI_Globals.SubmitArnoldJob,q=1,v=1))
		# Submit Maya Render JobType
		if jobType == UI_Globals.MayaRenderJobType or submitDependentJob:
			if not os.path.isdir( outputFilePath ):
				message=message + "Image Output Path \"" + outputFilePath + "\" does not exist! Your final images will be lost!\n\n"
				# If not an export job, or it is an export job with a dependent job, warn about the output.


			elif IsLocalDrive(outputFilePath):
				message=message + "Image Output Path \"" + outputFilePath + "\" is on a local drive.\nSlaves will not be able to copy images to this drive.\n\n"


			elif len(outputFilePath) == 0:
				message=message + "Image Output Path is blank! Your final images will be lost!\n\n"
		# Use Maya Batch
		if pm.checkBox(UI_Globals.UseMayaBatchPlugin,q=1,v=1):
			startupScript=str(pm.textFieldButtonGrp(UI_Globals.StartupScriptPathGrp,
			                                        q=1,text=1))
			# If there is a startup script, make sure it exists and that it isn't local.
			startupScript=startupScript.strip()
			if startupScript != "":
				if not pm.mel.filetest(-e, startupScript):
					message=message + "Startup Script \"" + startupScript + "\" does not exist!\n\n"


				elif IsLocalDrive(startupScript):
					message=message + "Startup Script \"" + startupScript + "\" is on a local drive.\nSlaves will not be able to access it at render time.\n\n"
		# Submit Each Render Layer
		if jobType == UI_Globals.MayaRenderJobType and Helpers.Data_Access.IsRenderLayersOn and submitEachRenderLayer:
			tempMessage=""
			# Loop through the render layer if the checkbox is on
			for layer in pm.ls(exactType="renderLayer"):
				# Only submit if layer is not referenced.
				if layer.isReferenced():
					# Submit only if the renderable attribute is on
					if layer.renderable.get():
						tempMessage=tempMessage + "  " + layer.name() + "\n"



			if tempMessage != "":
				message=message + "The following renderable referenced layers will not be submitted with the job:\n" + tempMessage + "\n"

		# Submit Region Rendering
		if regionRendering:
			extension=str(pm.mel.fileExtension(Helpers.GetOutputPrefix(0, 0, "", "")))
			print "extension = " + extension
			extension=extension.lower()
			if extension != "bmp" and extension != "dds" and extension != "exr" and extension != "jpg" and extension != "png" and extension != "sgi" and extension != "tga" and extension != "tif":
				message=message + "The image format used is not compatible with the Tile Assembler, so you will have to assemble the final image manually.\nThe following formats are currently supported: bmp, dds, exr, jpg, png, sgi, tga, tif.\n\n"


		if len(message)>0:
			message=message + "\nAre you sure you want to submit this job?"
			# Display any warning messages
			result=str(pm.confirmDialog(parent=self._main_window,title="Confirm",cancelButton="No",dismissString="No",defaultButton="Yes",message=(message),button=["Yes", "No"]))
			if result == "No":
				return False
		return True
	#----------------------------------------------------------------------
	def SetupSubmission(self):
		self._PD.SavePersistentDeadlineOptions()
		print "Submitting job to Deadline...\n"
		# Get the current renderer
		renderer = Helpers.Data_Access.currentRenderer
		# Check if we are doing a mental ray export
		jobType=self.MayaJobType.getSelect()
		# Check all the paths for problems, and warn the user if any are found
		projectPath           = CheckSlashes(self.ProjectPathGrp.getText())
		outputFilePath        = CheckSlashes(self.ImageOutputPathGrp.getText())
		sceneFilePath         = CheckSlashes(pm.cmds.file(q=1,sceneName=1))
		mentalRayFilename     = CheckSlashes(self.Job_MentalRay_File_Name.getText())
		vrayFilename          = CheckSlashes(self.VRay_File_Name.getText())
		submitMayaSceneFile   = self.Job_submit_Maya_Scene.getValue()
		submitEachRenderLayer = int(Helpers.Data_Access.IsRenderLayersOn and self.Job_Submit_Each_Render_Layer.getValue() or False)
		regionRendering       = int(self.RegionRendering_CheckBox.getValue())
		exportDependentJob    = int(False)
		submitDependentJob    = int(self.Submit_VRay_Job.getValue())
		message=""
		if not self.Run_Pre_Submit_Checks():
			return
		# Save scene, if necessary
		self._save_scene()

		# If this is not a mental ray export job, check if we need to submit each layer as a separate job.
		if self.is_maya_render_job and Helpers.Data_Access.IsRenderLayersOn and self.submit_each_render_layer:
			submitCounter=0
			# Store the currently selected render layer
			currentRenderLayer=pm.editRenderLayerGlobals(currentRenderLayer=1,query=1)
			# Loop through the render layer if the checkbox is on
			for layer in pm.ls(exactType="renderLayer"):
				# Only submit if layer is not referenced.
				if not layer.isReferenced():
					# Submit only if the renderable attribute is on
					if layer.renderable.get():
						# Select the render layer to make sure the render settings are updated
						layer.setCurrent()
						# Check if we're submitting each camera as a separate job.
						if self.Job_Submit_Each_Camera.getValue():
							for cameraName in pm.ls(type="camera"):
								# Only submit default cameras if the setting to ignore them is disabled.
								if not self.Job_Ignore_Default_Cameras.getValue() or not IsDefaultCamera(cameraName):
									# Only submit renderable cameras.
									if cameraName.renderable.get():
										# Set up a tile rendering job if necessary.
										if regionRendering and Helpers.Data_Access.SupportsRegionRendering:
											submitCounter+=int(_SetupRegionRenderingJob(renderer, cameraName))


										else:
											self._WriteJobFilesAndSubmit(renderer, 0, 0, jobType, cameraName)
											submitCounter+=1






						elif regionRendering and Helpers.Data_Access.SupportsRegionRendering:
							submitCounter+=int(_SetupRegionRenderingJob(renderer, ""))
							# Set up a tile rendering job if necessary.


						else:
							self._WriteJobFilesAndSubmit(renderer, 0, 0, jobType, "")
							submitCounter+=1





			pm.editRenderLayerGlobals(currentRenderLayer=currentRenderLayer)
			# Reselect the current render layer
			submitsResults="Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."
			pm.confirmDialog(message=submitsResults,button="Close",parent=self._main_window,title="Submission Results")
		# Submit MentalRay Export JobType
		elif jobType == UI_Globals.MentalRayExportJobType:
			submitCounter=int(_SetupMentalRayExportJob(renderer))
			pm.confirmDialog(message=("Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."),button="Close",parent=self._main_window,title="Submission Results")
		# Submit Vray Export JobType
		elif jobType == UI_Globals.VRayExportJobType:
			self._Submit_Vray_Export_Job()
		# Submit Renderman Export JobType
		elif jobType == UI_Globals.RendermanExportJobType:
			submitCounter=int(_SetupRendermanExportJob(renderer))
			pm.confirmDialog(message=("Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."),button="Close",parent=self._main_window,title="Submission Results")
		# Submit Arnold Export JobType
		elif jobType == UI_Globals.ArnoldExportJobType:
			submitCounter=int(_SetupArnoldExportJob(renderer))
			pm.confirmDialog(message=("Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."),button="Close",parent=self._main_window,title="Submission Results")
		# Submit Each Camera
		elif self.Job_Submit_Each_Camera.getValue():
			submitCounter=0
			# Check if we're submitting each camera as a separate job.
			ignoreDefaultCameras=int(pm.checkBox(UI_Globals.IgnoreDefaultCameras,q=1,v=1))
			cameraNames=pm.mel.listTransforms("-cameras")
			for cameraName in cameraNames:
				relatives=pm.listRelatives(s=cameraName)
				cameraShape=relatives[0]
				# Only submit default cameras if the setting to ignore them is disabled.
				if not ignoreDefaultCameras or not IsDefaultCamera(cameraShape):
					if IsCameraRenderable(cameraName):
						if regionRendering and Helpers.Data_Access.SupportsRegionRendering:
							submitCounter+=int(_SetupRegionRenderingJob(renderer, cameraName))
							# Only submit renderable cameras.
							#if( `getAttr( $cameraShape + ".renderable" )` )
							# Only setup a tile rendering job if it is enabled.


						else:
							self._WriteJobFilesAndSubmit(renderer, 0, 0, jobType, cameraName)
							submitCounter+=1




			submitsResults="Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."
			pm.confirmDialog(message=submitsResults,button="Close",parent=self._main_window,title="Submission Results")
		# Submit Region Rendering
		elif regionRendering and Helpers.Data_Access.SupportsRegionRendering:
			submitCounter=int(_SetupRegionRenderingJob(renderer, ""))
			# Only setup a tile rendering job if it is enabled.
			pm.confirmDialog(message=("Done submitting " + str(submitCounter) + " jobs.\nSee script history log for complete details."),button="Close",parent=self._main_window,title="Submission Results")


		else:
			jobId=str(self._WriteJobFilesAndSubmit(renderer, 1, 0, jobType, ""))
			print "JOB ID = " + jobId + "\n"
	# Sets some region rendering settings before submitting the job to Deadline.
	#----------------------------------------------------------------------
	def _SetupRegionRenderingJob(self, renderer, cameraOverride):
		submitCounter=0
		width,height = Helpers.Data_Access.globalsResolution
		# vray is very picky about the height. Not width for some reason.
		if renderer == "vray":
			height=height - 0

		tilesInX   = self.Job_Tiles_In_X.getValue()
		tilesInY   = self.Job_Tiles_In_Y.getValue()
		deltaX     = int(math.floor(1.0 * width / tilesInX))
		deltaY     = int(math.floor(1.0 * height / tilesInY))
		totalTiles = tilesInX * tilesInY
		currTile   = 0
		camera     = ""

		# Figure out the camera to use (if specified).
		if cameraOverride != "":
			camera=cameraOverride
		else:
			selectedCamera = self.Job_Render_Camera_List.getValue()
			for cameraName in pm.mel.listTransforms("-cameras"):
				if cameraName == selectedCamera:
					camera=selectedCamera
					break

		if not self.Submit_Tiles_As_Single_Job_CheckBox.getValue():
			for y in range(1,tilesInY+1):
				for x in range(1,tilesInX+1):
					currTile+=1
					newY=y
					if renderer != "renderMan" and renderer != "vray" and renderer != "arnold":
						newY=tilesInY - y + 1

					self._PD.deadlineRegionLeft.set(deltaX * (x - 1))
					self._PD.deadlineRegionTop.set(deltaY * (newY - 1))
					tempRight=0
					if x == tilesInX:
						tempRight=width - 1
					else:
						tempRight=(deltaX * x) - 1

					if renderer == "mentalRay":
						tempRight+=1

					self._PD.deadlineRegionRight.set(tempRight)

					tempBottom=0
					if newY == tilesInY:
						tempBottom=height - 1
					else:
						tempBottom=(deltaY * newY) - 1

					if renderer == "mentalRay":
						tempBottom+=1

					if renderer == "vray":
						tempBottom=tempBottom + 2

					self._PD.deadlineRegionBottom.set(tempBottom)
					self._PD.deadlineCurrX.set(x)
					self._PD.deadlineCurrY.set(y)
					self._PD.deadlineCurrTile.set(currTile)
					self._WriteJobFilesAndSubmit(renderer, 0, 1, UI_Globals.MayaRenderJobType, camera)
					submitCounter+=1

		else:
			self._PD.deadlineRegionSingleLeft.set("")
			self._PD.deadlineRegionSingleTop.set("")
			self._PD.deadlineRegionSingleRight.set("")
			self._PD.deadlineRegionSingleBottom.set("")
			self._PD.deadlineRegionSinglePrefix.set("")
			for y in range(1,tilesInY+1):
				for x in range(1,tilesInX+1):
					newY=y
					if renderer != "renderMan" and renderer != "vray" and renderer != "arnold":
						newY=tilesInY - y + 1

					regionSingleLeft =  self._PD.deadlineRegionSingleLeft.get()
					regionSingleLeft += "RegionLeft" + str(currTile) + "=" + str((deltaX * (x - 1))) + "\n"
					self._PD.deadlineRegionSingleLeft.set(regionSingleLeft)
					regionSingleTop  =  self._PD.deadlineRegionSingleTop.get()
					regionSingleTop  += "RegionTop" + str(currTile) + "=" + str((deltaY * (newY - 1))) + "\n"
					self._PD.deadlineRegionSingleTop.set(regionSingleTop)
					tempRight=0
					if x == tilesInX:
						tempRight=width - 1
					else:
						tempRight=(deltaX * x) - 1

					if renderer == "mentalRay":
						tempRight+=1

					regionSingleRight =  self._PD.deadlineRegionSingleRight.get()
					regionSingleRight += "RegionRight" + str(currTile) + "=" + str(tempRight) + "\n"
					self._PD.deadlineRegionSingleRight.set(regionSingleRight)
					tempBottom=0
					if newY == tilesInY:
						tempBottom=height - 1
					else:
						tempBottom=(deltaY * newY) - 1

					if renderer == "mentalRay":
						tempBottom+=1

					regionSingleBottom=self._PD.deadlineRegionSingleBottom.get()
					regionSingleBottom+="RegionBottom" + str(currTile) + "=" + str(tempBottom) + "\n"
					self._PD.deadlineRegionSingleBottom.set(regionSingleBottom)
					regionSinglePrefix = self._PD.deadlineRegionSinglePrefix.get()
					outputFilePrefix   = str(GetMayaOutputPrefix(camera))
					outputFilePrefix   = str(GetTileOutputPrefix(outputFilePrefix, x, y, tilesInX, tilesInY))
					if renderer == "renderMan":
						outputFilePrefix="_" + outputFilePrefix

					regionSinglePrefix+="RegionPrefix" + str(currTile) + "=" + outputFilePrefix + "\n"
					self._PD.deadlineRegionSinglePrefix.set(regionSinglePrefix)
					currTile+=1


			self._PD.deadlineRegionSingleTiles.set(currTile)
			jobId=str(self._WriteJobFilesAndSubmit(renderer, 0, 1, UI_Globals.MayaRenderJobType, camera))
			submitCounter+=1
			## Needs Clean UP
			if self.Job_Submit_Tile_Dependent.getValue():
				frameNumber=int(pm.intSliderGrp('frw_tileSingleFrame',q=1,v=1))
				outputFilePath=str(CheckSlashes(pm.textFieldGrp('frw_outputFilePath',q=1,text=1)))
				submitEachRenderLayer=int(Helpers.Data_Access.IsRenderLayersOn and pm.checkBox('frw_submitEachRenderLayer',q=1,value=1) or False)
				if Helpers.Data_Access.IsRenderLayersOn and not submitEachRenderLayer:
					currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
					# Store the currently selected render layer
					renderLayerList=pm.ls(exactType="renderLayer")
					# Loop through the render layer if the checkbox is on
					for i in range(0,len(renderLayerList)):
						isReferenceLayer=int(pm.referenceQuery(inr=renderLayerList[i]))
						# Only get output if this is not a referenced layer
						if not isReferenceLayer:
							renderable=int(pm.getAttr(renderLayerList[i] + ".renderable"))
							# Only get output if the renderable attribute is on
							if renderable:
								if not pm.catch( lambda: pm.editRenderLayerGlobals(currentRenderLayer=renderLayerList[i]) ):
									tempOutputFilePath=outputFilePath
									# Select the render layer to make sure the render settings are updated
									if renderer == "renderMan":
										tempOutputFilePath=str(pm.mel.rmanGetImageDir())
										tempCurrentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
										if pm.mel.gmatch(tempCurrentRenderLayer, "defaultRenderLayer") == 1:
											tempOutputFilePath=tempOutputFilePath + "/masterLayer"


										else:
											tempOutputFilePath=tempOutputFilePath + "/" + tempCurrentRenderLayer


									if camera != "":
										outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(1, frameNumber, renderLayerList[i], camera)))
										count=int(_SetupDependentTileAssemblerJob(renderer, jobId, frameNumber, tilesInX, tilesInY, outputPrefix, renderLayerList[i], camera))
										submitCounter+=count


									else:
										cameraNames=pm.mel.listTransforms("-cameras")
										for cameraName in cameraNames:
											if IsCameraRenderable(cameraName):
												outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(1, frameNumber, renderLayerList[i], cameraName)))
												#string $relatives[] = `listRelatives -s $cameraName`;
												#string $cameraShape = $relatives[0];
												#if( !IsDefaultCamera( $cameraShape ) )
												#if( `getAttr( $cameraShape + ".renderable" )` )
												count=int(_SetupDependentTileAssemblerJob(renderer, jobId, frameNumber, tilesInX, tilesInY, outputPrefix, renderLayerList[i], cameraName))
												submitCounter+=count







					pm.editRenderLayerGlobals(currentRenderLayer=currentRenderLayer)
					# Reselect the current render layer


				else:
					tempOutputFilePath=outputFilePath
					currentRenderLayer=""
					if Helpers.Data_Access.IsRenderLayersOn and submitEachRenderLayer:
						currentRenderLayer=str(pm.editRenderLayerGlobals(currentRenderLayer=1,query=1))
						if renderer == "renderMan":
							tempOutputFilePath=str(pm.mel.rmanGetImageDir())
							if pm.mel.gmatch(currentRenderLayer, "defaultRenderLayer") == 1:
								tempOutputFilePath=tempOutputFilePath + "/masterLayer"


							else:
								tempOutputFilePath=tempOutputFilePath + "/" + currentRenderLayer



					if camera != "":
						outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(1, frameNumber, currentRenderLayer, camera)))
						count=int(_SetupDependentTileAssemblerJob(renderer, jobId, frameNumber, tilesInX, tilesInY, outputPrefix, currentRenderLayer, camera))
						submitCounter+=count


					else:
						cameraNames=pm.mel.listTransforms("-cameras")
						for cameraName in cameraNames:
							if IsCameraRenderable(cameraName):
								outputPrefix=str(CheckSlashes(Helpers.GetOutputPrefix(1, frameNumber, currentRenderLayer, cameraName)))
								#string $relatives[] = `listRelatives -s $cameraName`;
								#string $cameraShape = $relatives[0];
								#if( !IsDefaultCamera( $cameraShape ) )
								#if( `getAttr( $cameraShape + ".renderable" )` )
								count=int(_SetupDependentTileAssemblerJob(renderer, jobId, frameNumber, tilesInX, tilesInY, outputPrefix, currentRenderLayer, cameraName))
								submitCounter+=count

		return submitCounter
	# Event when Submit Job button is pressed
	#----------------------------------------------------------------------
	def DeadlineSubmitterOnOk(self, *args):
		jobType=self.MayaJobType.getSelect()
		# Check if we are doing a mental ray export
		if self.Job_Submit_Each_Render_Layer.getValue() and self.Job_Override_Layer_Settings.getValue() and jobType == UI_Globals.MayaRenderJobType:
			pm.layoutDialog(ui=LayerSettingsDialog,parent=self.DeadlineSubmitterWindow,title="Override Layer Job Settings")
		else:
			self.SetupSubmission()
	#----------------------------------------------------------------------
	@property
	def maya_job_type(self):
		""""""
		return self.MayaJobType.getSelect()
	#----------------------------------------------------------------------
	@property
	def is_maya_render_job(self):
		return self.maya_job_type == UI_Globals.MayaRenderJobType
	#----------------------------------------------------------------------
	@property
	def is_mentalRay_Export_Job(self):
		""""""
		return self.maya_job_type == UI_Globals.MentalRayExportJobType
	#----------------------------------------------------------------------
	@property
	def is_vray_export_job(self):
		""""""
		return self.maya_job_type == UI_Globals.VRayExportJobType
	#----------------------------------------------------------------------
	@property
	def is_renderman_export_job(self):
		""""""
		return self.maya_job_type == UI_Globals.RendermanExportJobType
	#----------------------------------------------------------------------
	@property
	def is_arnold_export_Job(self):
		""""""
		return self.maya_job_type == UI_Globals.ArnoldExportJobType
	#----------------------------------------------------------------------
	@property
	def submit_each_render_layer(self):
		""""""
		return self.Job_Submit_Each_Render_Layer.getValue()
	#----------------------------------------------------------------------
	@property
	def override_layer_settings(self):
		""""""
		return self.Job_Override_Layer_Settings.getValue()
	#----------------------------------------------------------------------
	@property
	def is_render_layers_on(self):
		""""""
		return Helpers.Data_Access.IsRenderLayersOn
	#----------------------------------------------------------------------
	@property
	def render_layer_frames_list(self):
		""""""
		fromFrame,toFrame,byFrame = Helpers.Data_Access.frameRange
		if byFrame>1:
			return "%.0f-%.0fx%.0f" % (fromFrame, toFrame, byFrame)
		else:
			return "%.0f-%.0f" % (fromFrame, toFrame)
	#----------------------------------------------------------------------
	@property
	def vray_Scene_File_SubFolders(self):
		""""""
		vrayFilename = self.VRay_File_Name.getText()
		res = []
		for layer in Helpers.Data_Access.valid_Render_Layers:
			file_path = vrayFilename.replace("<Layer>", str(layer.name()))
			directory = os.path.dirname(file_path)
			res.append(directory)
		return res
########################################################################
class UI_Data_Access(object):
	#----------------------------------------------------------------------
	def __init__(self, ui):
		""""""
		self.ui = ui
		isinstance(self.ui, SubmitToDeadLine_UI)
	#----------------------------------------------------------------------
	def get_Image_Output_Path(self):
		return self.ui.ImageOutputPathGrp.getText()
	#----------------------------------------------------------------------
	def set_Image_Output_Path(self, value):
		return self.ui.ImageOutputPathGrp.setText(value)
	#----------------------------------------------------------------------
	Image_Output_Path = property(get_Image_Output_Path, set_Image_Output_Path)
########################################################################
class Persistent_Data_Access(object):
	# Saves the persistent deadline options in the scene.
	def __init__(self, ui):
		self.ui = ui
		self.attr_To_ui_dict = {}
		self.Create_Attributes()
		isinstance(self.ui, SubmitToDeadLine_UI)

	def SavePersistentDeadlineOptions(self, *args):
		if not len(self.attr_To_ui_dict):
			self.attr_To_ui_dict[self.ui.JobNameGrp] = self.deadlineJobName
			self.attr_To_ui_dict[self.ui.Job_Comment_Grp] = self.deadlineJobComment
			self.attr_To_ui_dict[self.ui.Job_Department_Grp] = self.deadlineDepartment
			self.attr_To_ui_dict[self.ui.Job_Goups] = self.deadlineGroup
			self.attr_To_ui_dict[self.ui.Job_Pools] = self.deadlineJobPool
			self.attr_To_ui_dict[self.ui.Secondary_Job_Pools] = self.deadlineJobSecondaryPool
			self.attr_To_ui_dict[self.ui.Job_Priority] = self.deadlineJobPriority
			self.attr_To_ui_dict[self.ui.Job_Limit_Count] = self.deadlineLimitCount
			self.attr_To_ui_dict[self.ui.Job_Concurrent_Tasks] = self.deadlineConcurrentTasks
			self.attr_To_ui_dict[self.ui.Job_On_Complete] = self.deadlineJobOnCompleat
			self.attr_To_ui_dict[self.ui.Job_Render_Camera_List] = self.deadlineRenderCamera
			self.attr_To_ui_dict[self.ui.Job_Slave_Timeout] = self.deadlineSlaveTimeout
			self.attr_To_ui_dict[self.ui.Job_Min_Slave_Timeout] = self.deadlineMinSlaveTimeout
			self.attr_To_ui_dict[self.ui.Job_Limit_Groups] = self.deadlineLimitGroups
			self.attr_To_ui_dict[self.ui.Job_Machines_List] = self.deadlineMachineList
			self.attr_To_ui_dict[self.ui.Job_Dependencies_List] = self.deadlineDependinceList
			self.attr_To_ui_dict[self.ui.Job_Is_Blacklist] = self.deadlineIsBlacklist
			self.attr_To_ui_dict[self.ui.Job_Submit_As_Suspended] = self.deadlineSubmitAsSuspended
			self.attr_To_ui_dict[self.ui.Job_Chunk_Size] = self.deadlineChunkSize
			self.attr_To_ui_dict[self.ui.Job_submit_Maya_Scene] = self.deadlineSubmitMayaScene
			self.attr_To_ui_dict[self.ui.Job_Max_Cpus] = self.deadlineNumCPUs
			self.attr_To_ui_dict[self.ui.Job_Submit_Each_Render_Layer] = self.deadlineSubmitEachRenderLayer
			self.attr_To_ui_dict[self.ui.Job_Override_Layer_Settings] = self.deadlineOverrideLayerSettings
			self.attr_To_ui_dict[self.ui.Job_Submit_Each_Camera] = self.deadlineSubmitEachCamera
			self.attr_To_ui_dict[self.ui.Job_Ignore_Default_Cameras] = self.deadlineIgnoreDefaultCameras
			self.attr_To_ui_dict[self.ui.Job_Use_Maya_Batch_Plugin] = self.deadlineUseMayaBatchPlugin
			self.attr_To_ui_dict[self.ui.Job_Strict_Error_Checking] = self.deadlineStrictErrorChecking
			self.attr_To_ui_dict[self.ui.Job_Local_Rendering] = self.deadlineLocalRendering
			self.attr_To_ui_dict[self.ui.Job_Startup_Script_Path] = self.deadlineStartupScript
			self.attr_To_ui_dict[self.ui.Job_Maya_Command_Line_Args] = self.deadlineMayaArgs
			self.attr_To_ui_dict[self.ui.Job_Tiles_In_X] = self.deadlineTilesInX
			self.attr_To_ui_dict[self.ui.Job_Tiles_In_Y] = self.deadlineTilesInY
			self.attr_To_ui_dict[self.ui.Job_Tile_Single_Frame] = self.deadlineTileSingleJob
			self.attr_To_ui_dict[self.ui.Job_Submit_Tile_Dependent] = self.deadlineTileDependentJob
			self.attr_To_ui_dict[self.ui.Job_Submit_Tile_Cleanup] = self.deadlineTileCleanupJob
			self.attr_To_ui_dict[self.ui.Job_Submit_Tile_Use_Draft] = self.deadlineTileUseDraft
			self.attr_To_ui_dict[self.ui.Job_Submit_Tile_Error_On_Missing] = self.deadlineTileErrorOnMissing
			self.attr_To_ui_dict[self.ui.Job_MentalRay_File_Name] = self.deadlineMentalRayFilename
			self.attr_To_ui_dict[self.ui.Job_Submit_MentalRay_Job] = self.deadlineSubmitMentalRayJob
			self.attr_To_ui_dict[self.ui.Job_MentalRay_Threads] = self.deadlineMentalRayThreads
			self.attr_To_ui_dict[self.ui.Job_MentalRay_Offset] = self.deadlineMentalRayOffset
			self.attr_To_ui_dict[self.ui.MentalRay_Local_Rendering] = self.deadlineMentalRayLocalRendering
			self.attr_To_ui_dict[self.ui.MentalRay_Command_Line_Args] = self.deadlineMentalRayArgs
			self.attr_To_ui_dict[self.ui.VRay_File_Name] = self.deadlineVRayFilename
			self.attr_To_ui_dict[self.ui.Submit_VRay_Job] = self.deadlineSubmitVRayJob
			self.attr_To_ui_dict[self.ui.Job_Vray_Threads] = self.deadlineVRayThreads
			self.attr_To_ui_dict[self.ui.Submit_Vrimg_2_Exr_Job] = self.deadlineSubmitVrimg2ExrJob
			self.attr_To_ui_dict[self.ui.Job_Delete_Vrimg_Files] = self.deadlineDeleteVrimgFiles
			self.attr_To_ui_dict[self.ui.ExportPRManThreads] = self.deadlineExportPRManThreads
			self.attr_To_ui_dict[self.ui.SubmitPRManJob] = self.deadlineSubmitPRManJob
			self.attr_To_ui_dict[self.ui.PrmanThreads] = self.deadlinePRManThreads
			self.attr_To_ui_dict[self.ui.PrmanArgs] = self.deadlinePRManArgs
			self.attr_To_ui_dict[self.ui.SubmitArnoldJob] = self.deadlineSubmitArnoldJob
			self.attr_To_ui_dict[self.ui.ArnoldThreads] = self.deadlineArnoldThreads
			self.attr_To_ui_dict[self.ui.ArnoldArgs] = self.deadlineArnoldArgs
			self.attr_To_ui_dict[self.ui.DraftTemplate] = self.deadlineDraftTemplate
			self.attr_To_ui_dict[self.ui.DraftUser] = self.deadlineDraftUser
			self.attr_To_ui_dict[self.ui.DraftEntity] = self.deadlineDraftEntity
			self.attr_To_ui_dict[self.ui.DraftVersion] = self.deadlineDraftVersion
			self.attr_To_ui_dict[self.ui.DraftExtraArgs] = self.deadlineDraftExtraArgs
			self.attr_To_ui_dict[self.ui.SubmitDraftJob] = self.deadlineUseDraft
			self.attr_To_ui_dict[self.ui.ShotgunVersion] = self.deadlineSGVersionName
			self.attr_To_ui_dict[self.ui.ShotgunResultsBox] = self.deadlineSGDisplayInfo
			self.attr_To_ui_dict[self.ui.UploadDraftToShotgun] = self.deadlineUploadDraftToShotgun
			self.attr_To_ui_dict[self.ui.ShotgunDescription] = self.deadlineSGDescription
			self.attr_To_ui_dict[self.ui.Job_MentalRay_Auto_Memory_Limit] = self.deadlineMentalRayAutoMemoryLimit
			self.attr_To_ui_dict[self.ui.Job_MentalRay_Auto_Memory] = self.deadlineMentalRayMemoryLimit
			self.attr_To_ui_dict[self.ui.Job_Vray_Auto_Memory_Enabled] = self.deadlineVrayAutoMemoryEnabled
			self.attr_To_ui_dict[self.ui.Job_Vray_Auto_Memory_Buffer] = self.deadlineVrayAutoMemoryBuffer

		#if len(args) == 1:
			#if args[0] in self.attr_To_ui_dict:
				#att = self.attr_To_ui_dict[args[0]]
				#try:
					#att.set(args[0].getValue())
				#except:
										#att.set(args[0].gettext())
				#return
		#================================================
		renderLayersEnabled= int(Helpers.Data_Access.IsRenderLayersOn)
		renderer           = str(self.ui.Data_Access.currentRenderer)
		regionRendering    = self.ui.RegionRendering_CheckBox.getValue()
		animationEnabled   = int(Helpers.Data_Access.IsAnimatedOn)

		self.deadlineJobName.set(self.ui.JobNameGrp.getText())
		self.deadlineJobComment.set(self.ui.Job_Comment_Grp.getText())
		self.deadlineDepartment.set(self.ui.Job_Department_Grp.getText())
		self.deadlineGroup.set(self.ui.Job_Goups.getValue())
		self.deadlineRenderCamera.set(self.ui.Job_Render_Camera_List.getValue())
		self.deadlineJobPool.set(self.ui.Job_Pools.getValue())
		self.deadlineJobSecondaryPool.set(self.ui.Secondary_Job_Pools.getValue())
		self.deadlineJobPriority.set(self.ui.Job_Priority.getValue())
		self.deadlineLimitCount.set(self.ui.Job_Limit_Count.getValue())
		self.deadlineConcurrentTasks.set(self.ui.Job_Concurrent_Tasks.getValue())
		self.deadlineSlaveTimeout.set(self.ui.Job_Slave_Timeout.getValue())
		self.deadlineMinSlaveTimeout.set(self.ui.Job_Min_Slave_Timeout.getValue())
		self.deadlineLimitGroups.set(self.ui.Job_Limit_Groups.getText())
		self.deadlineMachineList.set(self.ui.Job_Machines_List.getText())
		self.deadlineIsBlacklist.set(self.ui.Job_Is_Blacklist.getValue())
		self.deadlineSubmitAsSuspended.set(self.ui.Job_Submit_As_Suspended.getValue())
		self.deadlineChunkSize.set(self.ui.Job_Chunk_Size.getValue())
		self.deadlineSubmitMayaScene.set(self.ui.Job_submit_Maya_Scene.getValue())
		self.deadlineFramesList.set(self.ui.FrameListGrp.getText())

		if Helpers.Data_Access.EnableCpuOption:
			self.deadlineNumCPUs.set(self.ui.Job_Max_Cpus.getValue())

		if renderLayersEnabled:
			self.deadlineSubmitEachRenderLayer.set(self.ui.Job_Submit_Each_Render_Layer.getValue())
			self.deadlineOverrideLayerSettings.set(self.ui.Job_Override_Layer_Settings.getValue())

		#================================================


		self.deadlineSubmitEachCamera.set(self.ui.Job_Submit_Each_Camera.getValue())
		self.deadlineIgnoreDefaultCameras.set(self.ui.Job_Ignore_Default_Cameras.getValue())
		self.deadlineUseMayaBatchPlugin.set(self.ui.Job_Use_Maya_Batch_Plugin.getValue())
		self.deadlineStrictErrorChecking.set(self.ui.Job_Strict_Error_Checking.getValue())
		self.deadlineLocalRendering.set(self.ui.Job_Local_Rendering.getValue())
		self.deadlineStartupScript.set(self.ui.Job_Startup_Script_Path.getText())
		self.deadlineMayaArgs.set(self.ui.Job_Maya_Command_Line_Args.getText())
		self.deadlineTilesInX.set(self.ui.Job_Tiles_In_X.getValue())
		self.deadlineTilesInY.set(self.ui.Job_Tiles_In_Y.getValue())
		self.deadlineTileSingleJob.set(self.ui.Submit_Tiles_As_Single_Job_CheckBox.getValue())
		self.deadlineTileDependentJob.set(self.ui.Job_Submit_Tile_Dependent.getValue())
		self.deadlineTileCleanupJob.set(self.ui.Job_Submit_Tile_Cleanup.getValue())
		self.deadlineTileUseDraft.set(self.ui.Job_Submit_Tile_Use_Draft.getValue())
		self.deadlineTileErrorOnMissing.set(self.ui.Job_Submit_Tile_Error_On_Missing.getValue())
		self.deadlineMentalRayFilename.set(self.ui.Job_MentalRay_File_Name.getText())
		self.deadlineSubmitMentalRayJob.set(self.ui.Job_Submit_MentalRay_Job.getValue())
		self.deadlineMentalRayThreads.set(self.ui.Job_MentalRay_Threads.getValue())
		self.deadlineMentalRayOffset.set(self.ui.Job_MentalRay_Offset.getValue())
		self.deadlineMentalRayLocalRendering.set(self.ui.MentalRay_Local_Rendering.getValue())
		self.deadlineMentalRayArgs.set(self.ui.MentalRay_Command_Line_Args.getText())
		self.deadlineVRayFilename.set(self.ui.VRay_File_Name.getText())
		self.deadlineSubmitVRayJob.set(self.ui.Submit_VRay_Job.getValue())
		self.deadlineVRayThreads.set(self.ui.Job_Vray_Threads.getValue())
		self.deadlineSubmitVrimg2ExrJob.set(self.ui.Submit_Vrimg_2_Exr_Job.getValue())
		self.deadlineDeleteVrimgFiles.set(self.ui.Delete_Vrimg_Files.getValue())
		self.deadlineExportPRManThreads.set(self.ui.ExportPRManThreads.getValue())
		self.deadlineSubmitPRManJob.set(self.ui.SubmitPRManJob.getValue())
		self.deadlinePRManThreads.set(self.ui.PrmanThreads.getValue())
		self.deadlinePRManArgs.set(self.ui.PrmanArgs.getText())
		self.deadlineSubmitArnoldJob.set(self.ui.SubmitArnoldJob.getValue())
		self.deadlineArnoldThreads.set(self.ui.ArnoldThreads.getValue())
		self.deadlineArnoldArgs.set(self.ui.ArnoldArgs.getText())
		self.deadlineDraftTemplate.set(self.ui.DraftTemplate.getText())
		self.deadlineDraftUser.set(self.ui.DraftUser.getText())
		self.deadlineDraftEntity.set(self.ui.DraftEntity.getText())
		self.deadlineDraftVersion.set(self.ui.DraftVersion.getText())
		self.deadlineDraftExtraArgs.set(self.ui.DraftExtraArgs.getText())
		self.deadlineUseDraft.set(self.ui.SubmitDraftJob.getValue())
		self.deadlineUploadDraftToShotgun.set(self.ui.UploadDraftToShotgun.getValue())
		self.deadlineSGDisplayInfo.set(self.ui.ShotgunResultsBox.getText())
		self.deadlineSGVersionName.set(self.ui.ShotgunVersion.getText())
		self.deadlineSGDescription.set(self.ui.ShotgunDescription.getText())
		self.deadlineJobOnCompleat.set(self.ui.Job_On_Complete.getValue())
		self.deadlineDependinceList.set(self.ui.Job_Dependencies_List.getText())
		if len(Shotgun_Globals.SGInfoKeys):
			self.deadlineSGInfoKeys.set(Shotgun_Globals.SGInfoKeys)
		if len(Shotgun_Globals.SGInfoValues):
			self.deadlineSGInfoValues.set(Shotgun_Globals.SGInfoValues)


		self.ui.Job_Startup_Script_Path.setEnable(self.ui.Job_Use_Maya_Batch_Plugin.getValue())
		self.ui.IgnoreError211.setEnable(not self.ui.Job_Use_Maya_Batch_Plugin.getValue())
		self.ui.Job_Maya_Command_Line_Args.setEnable(not self.ui.Job_Use_Maya_Batch_Plugin.getValue())

		if renderer == "mentalRay":
			self.deadlineMentalRayAutoMemoryLimit.set(self.ui.Job_MentalRay_Auto_Memory.getValue())
			self.deadlineMentalRayMemoryLimit.set(self.ui.Job_MentalRay_Auto_Memory_Limit.getValue())
			self.ui.Job_MentalRay_Auto_Memory_Limit.setEnable(self.ui.Job_MentalRay_Auto_Memory.getValue())
		if renderer == "vray":
			self.deadlineVrayAutoMemoryEnabled.set(self.ui.Job_Vray_Auto_Memory_Enabled.getValue())
			self.deadlineVrayAutoMemoryBuffer.set(self.ui.Job_Vray_Auto_Memory_Buffer.getValue())
			self.ui.Job_Vray_Auto_Memory_Enabled.setEnable(self.ui.Job_Use_Maya_Batch_Plugin.getValue())
			self.ui.Job_Vray_Auto_Memory_Buffer.setEnable(self.ui.Job_Use_Maya_Batch_Plugin.getValue() and self.ui.Job_Vray_Auto_Memory_Enabled.getValue())

		submitEachRenderLayer = self.ui.Job_Submit_Each_Render_Layer.getValue()
		layerOverride         = self.ui.Job_Override_Layer_Settings.getValue()

		if renderLayersEnabled:
			self.ui.RegionRendering_CheckBox.setEnable(submitEachRenderLayer)
			self.ui.Job_Override_Layer_Settings.setEnable(submitEachRenderLayer)

		if submitEachRenderLayer:
			self.ui.FrameListGrp.setEnable(animationEnabled and layerOverride)
		else:
			self.ui.FrameListGrp.setEnable(animationEnabled)

		if not submitEachRenderLayer and regionRendering:
			regionRendering=False
			self.ui.RegionRendering_CheckBox.setValue(submitEachRenderLayer)
		else:
			self.ui.FrameListGrp.setEnable(animationEnabled)


		#if len(args) == 2:
			#if args[0] == self.ui.RegionRendering_CheckBox:
				#self.Update_On_RegionRendering_CheckBox_Changed()

			#elif args[0] == self.ui.Job_Tile_Render_Single_Job:
				#self.Update_On_Render_Single_Tile_Changed()

			#elif args[0] == self.ui.Job_Submit_Tile_Use_Draft:
				#self.Update_On_Submit_Tile_Use_Draft_Changed()

			#elif args[0] == self.ui.Job_Submit_Tile_Dependent:
				#self.Update_On_Submit_Tile_Dependent_Changed()

		submitEachCamera      = self.ui.Job_Submit_Each_Camera.getValue()
		tileUseDraft          = self.ui.Job_Submit_Tile_Use_Draft.getValue()
		singleRegionRendering = self.ui.Submit_Tiles_As_Single_Job_CheckBox.getValue()
		assemblyRendering     = self.ui.Job_Submit_Tile_Dependent.getValue()

		self.ui.Job_Ignore_Default_Cameras.setEnable(submitEachCamera)

		self.ui.Job_Tiles_In_X.setEnable(regionRendering)
		self.ui.Job_Tiles_In_Y.setEnable(regionRendering)
		self.ui.Submit_Tiles_As_Single_Job_CheckBox.setEnable(regionRendering)
		self.ui.Job_Tile_Single_Frame.setEnable(regionRendering and singleRegionRendering)
		self.ui.Job_Submit_Tile_Dependent.setEnable(regionRendering and singleRegionRendering)
		self.ui.Job_Submit_Tile_Use_Draft.setEnable(regionRendering and singleRegionRendering)
		self.ui.Job_Submit_Tile_Error_On_Missing.setEnable(regionRendering and singleRegionRendering and tileUseDraft)
		self.ui.Job_Submit_Tile_Cleanup.setEnable(regionRendering and singleRegionRendering and assemblyRendering)

	def Update_On_Submit_Tile_Use_Draft_Changed(self):
		self.ui.Job_Submit_Tile_Error_On_Missing.setEnable(self.ui.Job_Submit_Tile_Use_Draft.getValue())

	def Update_On_Submit_Tile_Dependent_Changed(self):
		self.ui.Job_Submit_Tile_Cleanup.setEnable(self.ui.Job_Submit_Tile_Dependent.getValue())

	def Update_On_Render_Single_Tile_Changed(self):
		singleRegionRendering = self.ui.Submit_Tiles_As_Single_Job_CheckBox.getValue()
		self.ui.Job_Submit_Tile_Dependent.setEnable(singleRegionRendering)
		self.ui.Job_Submit_Tile_Use_Draft.setEnable(singleRegionRendering)
		self.Update_On_Submit_Tile_Use_Draft_Changed()
		self.Update_On_Submit_Tile_Dependent_Changed()

	def Update_On_RegionRendering_CheckBox_Changed(self):
		regionRendering = self.ui.RegionRendering_CheckBox.getValue()
		self.ui.Job_Tiles_In_X.setEnable(regionRendering)
		self.ui.Job_Tiles_In_Y.setEnable(regionRendering)
		self.ui.Submit_Tiles_As_Single_Job_CheckBox.setEnable(regionRendering)
		if self.ui.Submit_Tiles_As_Single_Job_CheckBox.getValue():
			self.Update_On_Render_Single_Tile_Changed()
			self.Update_On_Submit_Tile_Use_Draft_Changed()
			self.Update_On_Submit_Tile_Dependent_Changed()


	def Create_Attributes(self):
		self.deadlineStrictErrorChecking      = Helpers.AddBoolAttribute("deadlineStrictErrorChecking", True)
		self.deadlineIsBlacklist              = Helpers.AddBoolAttribute("deadlineIsBlacklist", False)
		self.deadlineSubmitAsSuspended        = Helpers.AddBoolAttribute("deadlineSubmitAsSuspended", False)
		self.deadlineSubmitMayaScene          = Helpers.AddBoolAttribute("deadlineSubmitMayaScene", False)
		self.deadlineSubmitEachRenderLayer    = Helpers.AddBoolAttribute("deadlineSubmitEachRenderLayer", True)
		self.deadlineOverrideLayerSettings    = Helpers.AddBoolAttribute("deadlineOverrideLayerSettings", False)
		self.deadlineSubmitEachCamera         = Helpers.AddBoolAttribute("deadlineSubmitEachCamera", False)
		self.deadlineIgnoreDefaultCameras     = Helpers.AddBoolAttribute("deadlineIgnoreDefaultCameras", False)
		self.deadlineUseMayaBatchPlugin       = Helpers.AddBoolAttribute("deadlineUseMayaBatchPlugin", True)
		self.deadlineLocalRendering           = Helpers.AddBoolAttribute("deadlineLocalRendering", False)
		self.deadlineTileSingleJob            = Helpers.AddBoolAttribute("deadlineTileSingleJob", True)
		self.deadlineTileDependentJob         = Helpers.AddBoolAttribute("deadlineTileDependentJob", True)
		self.deadlineTileCleanupJob           = Helpers.AddBoolAttribute("deadlineTileCleanupJob", False)
		self.deadlineTileUseDraft             = Helpers.AddBoolAttribute("deadlineTileUseDraft", False)
		self.deadlineTileErrorOnMissing       = Helpers.AddBoolAttribute("deadlineTileErrorOnMissing", False)
		self.deadlineSubmitMentalRayJob       = Helpers.AddBoolAttribute("deadlineSubmitMentalRayJob", False)
		self.deadlineMentalRayLocalRendering  = Helpers.AddBoolAttribute("deadlineMentalRayLocalRendering", False)
		self.deadlineSubmitVRayJob            = Helpers.AddBoolAttribute("deadlineSubmitVRayJob", False)
		self.deadlineSubmitVrimg2ExrJob       = Helpers.AddBoolAttribute("deadlineSubmitVrimg2ExrJob", False)
		self.deadlineDeleteVrimgFiles         = Helpers.AddBoolAttribute("deadlineDeleteVrimgFiles", False)
		self.deadlineSubmitPRManJob           = Helpers.AddBoolAttribute("deadlineSubmitPRManJob", False)
		self.deadlineSubmitArnoldJob          = Helpers.AddBoolAttribute("deadlineSubmitArnoldJob", False)
		self.deadlineUseDraft                 = Helpers.AddBoolAttribute("deadlineUseDraft", False)
		self.deadlineMentalRayAutoMemoryLimit = Helpers.AddBoolAttribute("deadlineMentalRayAutoMemoryLimit", True)
		self.deadlineVrayAutoMemoryEnabled    = Helpers.AddBoolAttribute("deadlineVrayAutoMemoryEnabled", False)
		self.deadlineRegionSingleTiles        = Helpers.AddBoolAttribute("deadlineRegionSingleTiles", False)
		
		self.deadlineJobName                  = Helpers.AddStringAttribute("deadlineJobName",Helpers.Data_Access.StrippedSceneFileName)
		self.deadlineJobComment               = Helpers.AddStringAttribute("deadlineJobComment", "")
		self.deadlineDepartment               = Helpers.AddStringAttribute("deadlineDepartment", "")
		self.deadlineGroup                    = Helpers.AddStringAttribute("deadlineGroup", 'none')
		self.deadlineJobPool                  = Helpers.AddStringAttribute("deadlineJobPool", 'none')
		self.deadlineJobSecondaryPool         = Helpers.AddStringAttribute("deadlineJobSecondaryPool", 'none')
		self.deadlineJobPriority              = Helpers.AddLongAttribute("deadlineJobPriority", 50)
		self.deadlineLimitCount               = Helpers.AddLongAttribute("deadlineLimitCount", 50)
		self.deadlineConcurrentTasks          = Helpers.AddLongAttribute("deadlineConcurrentTasks", 1)
		self.deadlineJobOnCompleat            = Helpers.AddStringAttribute("deadlineJobOnCompleat", "Nothing")
		self.deadlineRenderCamera             = Helpers.AddStringAttribute("deadlineRenderCamera", " ")
		self.deadlineSlaveTimeout             = Helpers.AddLongAttribute("deadlineSlaveTimeout", 0)
		self.deadlineMinSlaveTimeout          = Helpers.AddLongAttribute("deadlineMinSlaveTimeout", 0)
		self.deadlineLimitGroups              = Helpers.AddStringAttribute("deadlineLimitGroups", "")
		self.deadlineMachineList              = Helpers.AddStringAttribute("deadlineMachineList", "")
		self.deadlineDependinceList           = Helpers.AddStringAttribute("deadlineDependinceList", "")
		self.deadlineFramesList                = Helpers.AddStringAttribute("deadlineFramesList", Helpers.Frame_Range().frame_expression)
		self.deadlineChunkSize                = Helpers.AddLongAttribute("deadlineChunkSize", 1)
		self.deadlineNumCPUs                  = Helpers.AddLongAttribute("deadlineNumCPUs", 0)
		self.deadlineStartupScript            = Helpers.AddStringAttribute("deadlineStartupScript","")
		self.deadlineMayaArgs                 = Helpers.AddStringAttribute("deadlineMayaArgs", "")
		self.deadlineTilesInX                 = Helpers.AddLongAttribute("deadlineTilesInX", 2)
		self.deadlineTilesInY                 = Helpers.AddLongAttribute("deadlineTilesInY", 2)
		self.deadlineMentalRayFilename        = Helpers.AddStringAttribute("deadlineMentalRayFilename", "")
		self.deadlineMentalRayThreads         = Helpers.AddLongAttribute("deadlineMentalRayThreads", 0)
		self.deadlineMentalRayOffset          = Helpers.AddLongAttribute("deadlineMentalRayOffset", 0)
		self.deadlineMentalRayArgs            = Helpers.AddStringAttribute("deadlineMentalRayArgs", "")
		self.deadlineVRayFilename             = Helpers.AddStringAttribute("deadlineVRayFilename", "")
		self.deadlineVRayThreads              = Helpers.AddLongAttribute("deadlineVRayThreads", 0)
		self.deadlineExportPRManThreads       = Helpers.AddLongAttribute("deadlineExportPRManThreads", 0)
		self.deadlinePRManThreads             = Helpers.AddLongAttribute("deadlinePRManThreads", 0)
		self.deadlinePRManArgs                = Helpers.AddStringAttribute("deadlinePRManArgs", "")
		self.deadlineArnoldThreads            = Helpers.AddLongAttribute("deadlineArnoldThreads", 0)
		self.deadlineArnoldArgs               = Helpers.AddStringAttribute("deadlineArnoldArgs", "")
		self.deadlineDraftTemplate            = Helpers.AddStringAttribute("deadlineDraftTemplate", "")
		self.deadlineDraftUser                = Helpers.AddStringAttribute("deadlineDraftUser")
		self.deadlineDraftEntity              = Helpers.AddStringAttribute("deadlineDraftEntity")
		self.deadlineDraftVersion             = Helpers.AddStringAttribute("deadlineDraftVersion")
		self.deadlineDraftExtraArgs           = Helpers.AddStringAttribute("deadlineDraftExtraArgs")
		self.deadlineSGVersionName            = Helpers.AddStringAttribute("deadlineSGVersionName")
		self.deadlineSGDisplayInfo            = Helpers.AddStringAttribute("deadlineSGDisplayInfo")
		self.deadlineUploadDraftToShotgun     = Helpers.AddLongAttribute("deadlineUploadDraftToShotgun")
		self.deadlineSGDescription            = Helpers.AddStringAttribute("deadlineSGDescription")
		self.deadlineSGInfoKeys               = Helpers.AddStrArrayAttribute("deadlineSGInfoKeys")
		self.deadlineSGInfoValues             = Helpers.AddStrArrayAttribute("deadlineSGInfoValues")
		self.deadlineMentalRayMemoryLimit     = Helpers.AddLongAttribute("deadlineMentalRayMemoryLimit", 0)
		self.deadlineVrayAutoMemoryBuffer     = Helpers.AddLongAttribute("deadlineVrayAutoMemoryBuffer", 500)
		self.deadlineRegionLeft               = Helpers.AddLongAttribute("deadlineRegionLeft", 0)
		self.deadlineRegionTop                = Helpers.AddLongAttribute("deadlineRegionTop", 0)
		self.deadlineRegionRight              = Helpers.AddLongAttribute("deadlineRegionRight", 0)
		self.deadlineRegionBottom             = Helpers.AddLongAttribute("deadlineRegionBottom", 0)
		self.deadlineCurrX                    = Helpers.AddLongAttribute("deadlineCurrX")
		self.deadlineCurrY                    = Helpers.AddLongAttribute("deadlineCurrY")
		self.deadlineCurrTile                 = Helpers.AddLongAttribute("deadlineCurrTile")
		self.deadlineRegionSingleLeft         = Helpers.AddStringAttribute("deadlineRegionSingleLeft")
		self.deadlineRegionSingleTop          = Helpers.AddStringAttribute("deadlineRegionSingleTop")
		self.deadlineRegionSingleRight        = Helpers.AddStringAttribute("deadlineRegionSingleRight")
		self.deadlineRegionSingleBottom       = Helpers.AddStringAttribute("deadlineRegionSingleBottom")
		self.deadlineRegionSinglePrefix       = Helpers.AddStringAttribute("deadlineRegionSinglePrefix")
		
		aw_sg_atts = [["string","AW_SG_ProjectName"], ["string","AW_SG_Description"], ["string","AW_SG_UserName"], ["string","AW_SG_TaskName"], ["string","AW_SG_EntityName"], ["string","AW_SG_EntityType"], ["string","AW_SG_VersionName"],["long","AW_SG_ProjectId"], ["long","AW_SG_TaskId"], ["long","AW_SG_EntityId"], ["string","AW_SG_DraftTemplate"]]
		Helpers.AddCompoundAttribute("AW_Shotgun_Submit_Settings", aw_sg_atts)
		self.AW_SG_ProjectName   = Helpers.AddStringAttribute("AW_SG_ProjectName")
		self.AW_SG_Description   = Helpers.AddStringAttribute("AW_SG_Description")
		self.AW_SG_UserName      = Helpers.AddStringAttribute("AW_SG_UserName")
		self.AW_SG_TaskName      = Helpers.AddStringAttribute("AW_SG_TaskName")
		self.AW_SG_EntityName    = Helpers.AddStringAttribute("AW_SG_EntityName")
		self.AW_SG_EntityType    = Helpers.AddStringAttribute("AW_SG_EntityType")
		self.AW_SG_ProjectId     = Helpers.AddLongAttribute("AW_SG_ProjectId")
		self.AW_SG_TaskId        = Helpers.AddLongAttribute("AW_SG_TaskId")
		self.AW_SG_EntityId      = Helpers.AddLongAttribute("AW_SG_EntityId")
		self.AW_SG_VersionName   = Helpers.AddStringAttribute("AW_SG_VersionName")
		self.AW_SG_DraftTemplate = Helpers.AddStringAttribute("AW_SG_DraftTemplate")