from . import Helpers
import os
from . import DeadLine_Access
import pymel.core as pm

class Base_Info_File(object):
	Renderer = ""
	counter = 1
	#----------------------------------------------------------------------
	def Write_File(self):
		# Get the deadline temp directory.
		submitFilename = Helpers.Data_Access.User_Temp_Directory + "/maya_deadline_" + self.Renderer + str(self.__class__.counter) + "_Plugin_info.job"
		self.__class__.counter += 1
		lines = self.create_job_string()
		# Create the job info file.
		with file(submitFilename,"w") as fileId:
			fileId.write(lines)
		return submitFilename

class Maya_Batch_Vray_Export_Info_File(Base_Info_File):
	Renderer             = "vrayExport"
	defaultRenderGlobals = pm.PyNode("defaultRenderGlobals")
	def __init__(self):
		self.Animation        = Helpers.Data_Access.IsAnimatedOn
		self.VRayExportFile   = self.defaultRenderGlobals.deadlineVRayFilename.get()
		self.Version          = Helpers.Data_Access.mayaVersion
		self.Build            = "64bit"
		self.ProjectPath      = Helpers.Data_Access.project_workspace
		self.StartupScript    = self.defaultRenderGlobals.deadlineStartupScript.get()
		self.ImageWidth       = Helpers.Data_Access.globalsResolution[0]
		self.ImageHeight      = Helpers.Data_Access.globalsResolution[1]
		self.OutputFilePath   = os.path.dirname(self.VRayExportFile.replace("<Layer>", Helpers.Data_Access.currentRenderLayer))
		self.OutputFilePrefix = ""
		self.Camera           = self.defaultRenderGlobals.deadlineRenderCamera.get()
		self.All_Cameras      = Helpers.Data_Access.all_Renderable_Cameras
		self.SceneFile        = Helpers.Data_Access.scene_File_Path
		self.IgnoreError211   = False
		
		
	def create_job_string(self):
		lines = []
		lines.append("Animation=%i" % self.Animation)
		lines.append("Renderer=%s" % self.Renderer)
		lines.append("VRayExportFile=%s" % self.VRayExportFile)
		lines.append("Version=%i" % self.Version)
		lines.append("Build=%s" % self.Build)
		lines.append("ProjectPath=%s" % self.ProjectPath)
		lines.append("StartupScript=%s" % self.StartupScript)
		lines.append("ImageWidth=%i" % self.ImageWidth)
		lines.append("ImageHeight=%i" % self.ImageHeight)
		lines.append("OutputFilePath=%s" % self.OutputFilePath)
		lines.append("SceneFile=%s" % self.SceneFile)
		lines.append("OutputFilePrefix=%s" % self.OutputFilePrefix)
		lines.append("IgnoreError211=%i" % self.IgnoreError211)
		lines.append("Camera=%s" % self.Camera)
		for index, cam in enumerate(self.All_Cameras):
			lines.append( "Camera%i=%s" % (index, cam.name() ))
		
		res = "\n".join(lines)
		return res

class Vray_Standalone_Info_File(Base_Info_File):
	def __init__(self, InputFilename="", OutputFilename="", Threads=0, CommandLineOptions=""):
		self.InputFilename         = InputFilename
		self.Width                 = Helpers.Data_Access.globalsResolution[0]
		self.Height                = Helpers.Data_Access.globalsResolution[1]
		self.Threads               = Threads
		self.OutputFilename        = OutputFilename
		self.SeparateFilesPerFrame = False
		self.CommandLineOptions    = CommandLineOptions

		
	def create_job_string(self):
		lines = []
		lines.append("InputFilename=%s" % self.InputFilename)
		lines.append("OutputFilename=%s" % self.OutputFilename)
		lines.append("Width=%i" % self.Width)
		lines.append("Height=%i" % self.Height)
		lines.append("Threads=%i" % self.Threads)
		lines.append("SeparateFilesPerFrame=%r" % self.SeparateFilesPerFrame)
		lines.append("CommandLineOptions=%s" % self.CommandLineOptions)
		
		res = "\n".join(lines)
		return res
	
	
class Vray_Image_To_Exr_Info_File(Base_Info_File):
	def __init__(self, InputFile="", OutputFile="", DataWindow=True, sRGB=False, Half=False, SetGamma=False, Gamma=1.8,SetChannel=True, Channel="RGB", SetCompression=True, Compression="zip", SetBufferSize=True, BufferSize=10, DeleteInputFiles=False):
		self.InputFile=InputFile
		self.OutputFile=OutputFile
		self.Half=Half
		self.sRGB=sRGB
		self.DataWindow=DataWindow
		self.SetGamma=SetGamma
		self.Gamma=Gamma
		self.SetChannel=SetChannel
		self.Channel=Channel
		self.SetCompression=SetCompression
		self.Compression=Compression
		self.SetBufferSize=SetBufferSize
		self.BufferSize=BufferSize
		self.DeleteInputFiles=DeleteInputFiles

		
	def create_job_string(self):
		lines = []
		lines.append("InputFile=%s" % self.InputFile)
		lines.append("OutputFile=%s" % self.OutputFile)
		lines.append("Half=%r" % self.Half)
		lines.append("sRGB=%r" % self.sRGB)
		lines.append("DataWindow=%r" % self.DataWindow)
		lines.append("SetGamma=%r" % self.SetGamma)
		lines.append("Gamma=%r" % self.Gamma)
		lines.append("SetChannel=%r" % self.SetChannel)
		lines.append("Channel=%s" % self.Channel)
		lines.append("SetCompression=%r" % self.SetCompression)
		lines.append("Compression=%s" % self.Compression)
		lines.append("SetBufferSize=%r" % self.SetBufferSize)
		lines.append("BufferSize=%r" % self.BufferSize)
		lines.append("DeleteInputFiles=%r" % self.DeleteInputFiles)
		res = "\n".join(lines)
		return res
	
Active = "Active"
Suspended = "Suspended"
class ScheduledTypes():
	none  = "None"
	once  = "Once"
	daily = "Daily"
	


########################################################################
class Job_Info_File(object):
	_counter = 1
	#----------------------------------------------------------------------
	def __init__(self,
	             Plugin="",
	             Frames="",
	             Name="Untitled",
	             Department="",
	             Comment="",
	             Group="none",
	             Pool="none",
	             SecondaryPool="",
	             Priority=50,
	             ChunkSize=1,
	             ForceReloadPlugin=False,
	             SynchronizeAllAuxiliaryFiles=False,
	             InitialStatus="Active",
	             LimitGroups="",
	             MachineLimit=0,
	             MachineLimitProgress=-1.0,
	             Machinelist="",
	             DeleteOnComplete=False,
	             ArchiveOnComplete=False,
	             OnJobComplete="Nothing",
	             ConcurrentTasks=1,
	             LimitTasksToNumberOfCpus=True,
	             Sequential=False,
	             Interruptible=False,
	             SuppressEvents=False,
	             MinRenderTimeSeconds=0,
	             MinRenderTimeMinutes=0,
	             TaskTimeoutSeconds=0,
	             TaskTimeoutMinutes=0,
	             OnTaskTimeout="Error",
	             EnableAutoTimeout=False,
	             EnableTimeoutsForScriptTasks=False,
	             JobDependencies='',
	             JobDependencyPercentage=-1,
	             IsFrameDependent=False,
	             FrameDependencyOffsetStart=0,
	             FrameDependencyOffsetEnd=0,
	             ResumeOnCompleteDependencies=True,
	             ResumeOnDeletedDependencies=False,
	             ResumeOnFailedDependencies=False,
	             RequiredAssets='',
	             ScriptDependencies="",
	             ScheduledType=None,
	             ScheduledStartDateTime="dd/MM/yyyy HH:mm",
	             ScheduledDays=1,
	             OutputFilenames=[],
	             OutputDirectorys=[],
	             NotificationTargets="",
	             ClearNotificationTargets=False,
	             NotificationEmails="",
	             OverrideNotificationMethod=False,
	             EmailNotification=False,
	             PopupNotification=False,
	             NotificationNote="",
	             PreJobScript="",
	             PostJobScript="",
	             PreTaskScript="",
	             PostTaskScript="",
	             TileJob=False,
	             TileJobFrame=0,
	             TileJobTilesInX=0,
	             TileJobTilesInY=0,
	             TileJobTileCount=0,
	             OverrideJobFailureDetection=False,
	             FailureDetectionJobErrors=0,
	             OverrideTaskFailureDetection=False,
	             FailureDetectionTaskErrors=0,
	             IgnoreBadJobDetection=False,
	             SendJobErrorWarning=False,
	             ExtraInfo = [],
	             ExtraInfoKeyValues={},
	             IncludeEnvironment=False,
	             UseJobEnvironmentOnly=False,
	             CustomPluginDirectory=False,
	             EnvironmentKeyValue={},
	             useScheduling=False,
	             useNotifications=False,
	             useScripts=False, 
	             IsBlacklist=False,
	             Submit_To_ShotGun=False,
	             SG_TaskName="", 
	             SG_ProjectName="", 
	             SG_EntityName="", 
	             SG_VersionName="", 
	             SG_Description="", 
	             SG_UserName="", 
	             SG_Path_To_Frames="",
	             SG_Path_To_File="",
	             SG_TaskId=0, 
	             SG_ProjectId=0, 
	             SG_EntityId=0, 
	             SG_EntityType=""):
		
		"""
			General
			
				--Plugin
					| Specifies the plugin to use.
					| Must match an existing plugin in the repository.
					|
				--Frames
					| Specifies the frame range of the render job
					| 
				--Name
					| Specifies the name of the job
					| (default = Untitled).
					| 
				--Department
					| Specifies the department that the job belongs to.
					| This is simply a way to group jobs together,
					| and does not affect rendering in any way
					| (default = blank).
					| 
				--Comment
					| Specifies a comment for the job
					| (default = blank).
					| 
				--Group
					| Specifies the group that the job is being submitted to
					| (default = none).
					| 
				--Pool
					| Specifies the pool that the job is being submitted to
					| (default = none).
					| 
				--SecondaryPool
					| Specifies the secondary pool that the job can spread to
					| if machines are available.
					| If not specified, the job will not use a secondary pool.
					| (default = none).
					| 
				--Priority
					| Specifies the priority of a job with 0 being the lowest
					| The maximum priority can be configured in the Job Settings
					| of the Repository Options,
					| and defaults to 100.
					| (default = 50). 
					| 
				--ChunkSize
					| Specifies how many frames to render per task
					| (default = 1).
					| 
				--ForceReloadPlugin
					| Specifies whether or not to reload the plugin between subsequent frames of a job
					| This deals with memory leaks or applications that do not unload all job aspects properly.
					| (default = false). 
					| 
				--SynchronizeAllAuxiliaryFiles
					| If enabled, all job files (as opposed to just the job info and plugin info files) 
					| will be synchronized by the Slave between tasks for this job
					| Note that this can add significant network overhead, 
					| and should only be used if you plan on manually editing any of the files that are being submitted with the job.
					| (default = false). 
					| 
				--InitialStatus
					| Specifies what status the job should be in immediately after submission
					| (default = Active).
					| 
				--LimitGroups
					| Specifies the limit groups that this job is a member of
					| (default = blank).
					| 
				--MachineLimit
					| Specifies the maximum number of machines this job can be rendered on at the same time
					| (default = 0, which means unlimited).
					| 
				--MachineLimitProgress
					| If set, the slave rendering the job will give up its current machine limit lock 
					| when the current task reaches the specified progress.
					| If negative, this feature is disabled
					| The usefulness of this feature is directly related to the progress reporting capabilities of the individual plugins.
					| (default = -1.0). 
					| 
				--Whitelist
					| Specifies which slaves are on the job's whitelist
					| If both a whitelist and a blacklist are specified, only the whitelist is used.
					| (default = blank).
					| 
				--Blacklist
					| Specifies which slaves are on the job's blacklist
					| If both a whitelist and a blacklist are specified, only the whitelist is used.
					| (default = blank). 
					| 
				--DeleteOnComplete
					| Specifies whether or not the job should be automatically deleted after it completes
					| (default = false).
					| 
				--ArchiveOnComplete
					| Specifies whether or not the job should be automatically archived after it completes 
					| (default = false).
					| 
				--OnJobComplete
					| Specifies what should happen to a job after it completes 
					| (default = Nothing).
					| 
				--ConcurrentTasks
					| Specifies the maximum number of tasks that a slave can render at a time
					| This is useful for script plugins that support multithreading.
					| (default = 1). 
					| 
				--LimitTasksToNumberOfCpus
					| If ConcurrentTasks is greater than 1, 
					| setting this to true will ensure that a slave will not dequeue more tasks than it has processors 
					| (default = true).
					| 
				--Sequential
					| Sequential rendering forces a slave to render the tasks of a job in order. 
					| If an earlier task is ever requeued, 
					| the slave won't go back to that task until it has finished the remaining tasks in order 
					| (default = false).
					| 
				--Interruptible
					| Specifies if tasks for a job can be interrupted by a higher priority job during rendering
					| (default = false).
					| 
				--SuppressEvents
					| If true, the job will not trigger any event plugins while in the queue
					| (default = false).
					|

Timeout Options
				--MinRenderTimeSeconds
					| Specifies the minimum time, in seconds, a slave should render a task for, otherwise an error will be reported
					| Note that if MinRenderTimeSeconds and MinRenderTimeMinutes are both specified, MinRenderTimeSeconds will be ignored.
					| (default = 0, which means no minimum).
					| 
				--MinRenderTimeMinutes
					| Specifies the minimum time, in minutes, a slave should render a task for, otherwise an error will be reported
					| Note that if MinRenderTimeSeconds and MinRenderTimeMinare both specified, MinRenderTimeSeconds will be ignored.
					| (default = 0, which means no minimum). 
					| 
				--TaskTimeoutSeconds
					| Specifies the time, in seconds, a slave has to render a task before it times out
					| Note that if TaskTimeoutSeconds and TaskTimeoutMinutes are both specified, TaskTimeoutSeconds will be ignored.: 
					| (default = 0, which means unlimited).
					| 
				--TaskTimeoutMinutes
					| Specifies the time, in minutes, a slave has to render a task before it times out
					| Note that if TaskTimeoutSeconds and TaskTimeoutMinutes are both specified, TaskTimeoutSeconds will be ignored.
					| (default = 0, which means unlimited).
					| 
				--OnTaskTimeout
					| Specifies what should occur if a task times out
					| (default = Error).
					| 
				--EnableAutoTimeout
					| If true, a slave will automatically figure out if it has been rendering too long
					| based on some Repository Configuration settings and the render times of previously completed tasks
					| (default = false).
					| 
				--EnableTimeoutsForScriptTasks
					| If true, then the timeouts for this job will also affect its pre/post job scripts,
					| if any are defined
					| (default = false).
			
			- Dependency Options
			
				--JobDependencies
					| Specifies what jobs must finish before this job will resume 
					| These dependency jobs must be identified using their unique job ID, 
					| which is outputted after the job is submitted, 
					| and can be found in the Monitor in the "Job ID" column.
					| (default = blank).
					| 
				--JobDependencyPercentage
					| If between 0 and 100, 
					| this job will resume when all of its job dependencies have completed the specified percentage number of tasks. 
					| If -1, this feature will be disabled 
					| (default = -1).
					| 
				--IsFrameDependent
					| Specifies whether or not the job is frame dependent.0 to 100> :
					| (default = false)
					| 
				--FrameDependencyOffsetStart
					| If the job is frame dependent, this is the start frame offset 
					| (default = 0).
					| 
				--FrameDependencyOffsetEnd
					| If the job is frame dependent, this is the end frame offset 
					| (default = 0).: 
					| 
				--ResumeOnCompleteDependencies
					| Specifies whether or not the dependent job should resume when its dependencies are complete 
					| (default = true)
					| 
				--ResumeOnDeletedDependencies
					| Specifies whether or not the dependent job should resume when its dependencies have been deleted 
					| (default = false).	
					| 
				--ResumeOnFailedDependencies
					| Specifies whether or not the dependent job should resume when its dependencies have failed 
					| (default = false).	
					| 
				--RequiredAssets
					| Specifies what asset files must exist before this job will resume. 
					| These asset paths must be identified using full paths, 
					| and multiple paths can be separated with commas. 
					| If using frame dependencies, you can replace padding in a sequence with the '' characters, 
					| and a task for the job will only be resumed when the required assets for the task's frame) exist.
					| (default = blank)
					| 
				--ScriptDependencies
					| Specifies what Python script files will be executed to determine if a job can resume 
					| These script paths must be identified using full paths, 
					| and multiple paths can be separated with commas. 
					| See the Scripting section of the documentation for more information on script dependencies.
					| (default = blank).
					|
					
			- Scheduling Options
			
				--ScheduledType
					| Specifies whether or not you want to schedule the job 
					| (default = None).
					| 
				--ScheduledStartDateTime
					| The date/time at which the job will run. The start date/time must match the specified format. Here'sxplanation:
					| dd: The day of the month. Single-digit days must have a leading zero.
					| MM: The numeric month. Single-digit months must have a leading zero.
					| yyyy: The year in four digits, including the century.
					| HH: The hour in a 24-hour clock. Single-digit hours must have a leading zero.
					| mm: The minute. Single-digit minutes must have a leading zero.
					| 
				--ScheduledDays
					| If scheduling a Daily job, this is the day interval for when the job runs
					| (default = 1).
					|
					
			- Output Options
			
				--OutputFilename0
					| Specifies the output image filenames for each frame. 
					| This allows the Monitor to display the "View Output Image" context menu option in the task list. 
					| There is no minimum or maximum limit to padding length supported. 
					| A padding of 4 x  is very common in many applications. 
					| If the filename is a full path, then the OutputDirectory option is not needed. 
					| This option is numbered, starting with 0 (OutputFilename0), to handle multiple output file names per frame. 
					| For each additional file name, just increase the number (OutputFilename1, OutputFilename2, etc).
					| (default = blank)
					| 
				--OutputDirectory0
					| Specifies the output image directory for the job. 
					| This allows the Monitor to display the "Explore Output" context menu option in the job list. 
					| This option is numbered, starting with 0 (OutputDirectory0), to handle multiple output directories per frame. 
					| For each additional directory, just increase the number (OutputDirectory1, OutputDirectory2, etc).
					| (default = blank)
					|
					
					
			- Notification Options
			
				--NotificationTargets
					| A list of users, separated by commas, who should be notified when the job is completed
					| (default = blank).
					| 
				--ClearNotificationTargets
					| If enabled, all of the job's notification targets will be removed
					| (default = false)
					| 
				--NotificationEmails
					| A list of additional email addresses, separated by commas, to send job notifications to
					| (default = blank).
					| 
				--OverrideNotificationMethod
					| If the job user's notification method should be ignored
					| (default = false).
					| 
				--EmailNotification
					| If overriding the job user's notification method, whether to use email notification
					| (default = false).
					| 
				--PopupNotification
					| If overriding the job user's notification method, whether to use popup notification
					| (default = false).
					| 
				--NotificationNote
					| A note to append to the notification email sent out when the job is complete
					| (default = blank).
					| Separate multiple lines with [EOL] 
					|
					
			- Script Options
			
				--PreJobScript
					| Specifies a full path to a python script to execute when the job initially starts rendering
					| (default = blank).
					| 
				--PostJobScript
					| Specifies a full path to a python script to execute when the job completes
					| (default = blank).
					| 
				--PreTaskScript
					| Specifies a full path to a python script to execute before each task starts rendering
					| (default = blank).
					| 
				--PostTaskScript
					| Specifies a full path to a python script to execute after each task completes
					| (default = blank).
					|
					
			Tile Job Options
			
				--TileJob
					| If this job is a tile job
					| (default = false).
					| 
				--TileJobFrame
					| The frame that the tile job is rendering
					| (default = 0).
					| 
				--TileJobTilesInX
					| The number of tiles in X for a tile job
					| (default = 0).
					| This should be specified with the TileJobTilesInY option below.: 
					| 
				--TileJobTilesInY
					| The number of tiles in Y for a tile job
					| (default = 0).
					| This should be specified with the TileJobTilesInX option above.
					| 
				--TileJobTileCount
					| The number of tiles for a tile job
					| (default = 0).
					| This is an alternative to specifying the TileJobTilesInX and TileJobTilesInY options above.
					| 
		"""
		
		self.Plugin                       = Plugin
		self.Frames                       = Frames
		self.Name                         = Name
		self.Department                   = Department
		self.Comment                      = Comment
		self.Group                        = Group
		self.Pool                         = Pool
		self.SecondaryPool                = SecondaryPool
		self.Priority                     = Priority
		self.ChunkSize                    = ChunkSize
		self.ForceReloadPlugin            = ForceReloadPlugin
		self.SynchronizeAllAuxiliaryFiles = SynchronizeAllAuxiliaryFiles
		self.InitialStatus                = InitialStatus
		self.LimitGroups                  = LimitGroups
		self.MachineLimit                 = MachineLimit
		self.MachineLimitProgress         = MachineLimitProgress
		self.Machinelist                  = Machinelist
		self.DeleteOnComplete             = DeleteOnComplete
		self.ArchiveOnComplete            = ArchiveOnComplete
		self.OnJobComplete                = OnJobComplete
		self.ConcurrentTasks              = ConcurrentTasks
		self.LimitTasksToNumberOfCpus     = LimitTasksToNumberOfCpus
		self.Sequential                   = Sequential
		self.Interruptible                = Interruptible
		self.SuppressEvents               = SuppressEvents
		self.MinRenderTimeSeconds         = MinRenderTimeSeconds
		self.MinRenderTimeMinutes         = MinRenderTimeMinutes
		self.TaskTimeoutSeconds           = TaskTimeoutSeconds
		self.TaskTimeoutMinutes           = TaskTimeoutMinutes
		self.OnTaskTimeout                = OnTaskTimeout
		self.EnableAutoTimeout            = EnableAutoTimeout
		self.EnableTimeoutsForScriptTasks = EnableTimeoutsForScriptTasks
		self.JobDependencies              = JobDependencies
		self.JobDependencyPercentage      = JobDependencyPercentage
		self.IsFrameDependent             = IsFrameDependent
		self.FrameDependencyOffsetStart   = FrameDependencyOffsetStart
		self.FrameDependencyOffsetEnd     = FrameDependencyOffsetEnd
		self.ResumeOnCompleteDependencies = ResumeOnCompleteDependencies
		self.ResumeOnDeletedDependencies  = ResumeOnDeletedDependencies
		self.ResumeOnFailedDependencies   = ResumeOnFailedDependencies
		self.RequiredAssets               = RequiredAssets
		self.ScriptDependencies           = ScriptDependencies
		self.ScheduledType                = ScheduledType
		self.ScheduledStartDateTime       = ScheduledStartDateTime
		self.ScheduledDays                = ScheduledDays
		self.OutputFilenames              = OutputFilenames
		self.OutputDirectorys             = OutputDirectorys
		self.NotificationTargets          = NotificationTargets
		self.ClearNotificationTargets     = ClearNotificationTargets
		self.NotificationEmails           = NotificationEmails
		self.OverrideNotificationMethod   = OverrideNotificationMethod
		self.EmailNotification            = EmailNotification
		self.PopupNotification            = PopupNotification
		self.NotificationNote             = NotificationNote
		self.PreJobScript                 = PreJobScript
		self.PostJobScript                = PostJobScript
		self.PreTaskScript                = PreTaskScript
		self.PostTaskScript               = PostTaskScript
		self.TileJob                      = TileJob
		self.TileJobFrame                 = TileJobFrame
		self.TileJobTilesInX              = TileJobTilesInX
		self.TileJobTilesInY              = TileJobTilesInY
		self.TileJobTileCount             = TileJobTileCount
		self.IsBlacklist                  = IsBlacklist
		self.ExtraInfo                    = ExtraInfo
		self.ExtraInfoKeyValues           = ExtraInfoKeyValues
		self.IncludeEnvironment           = IncludeEnvironment
		self.UseJobEnvironmentOnly        = UseJobEnvironmentOnly
		self.EnvironmentKeyValue          = EnvironmentKeyValue
		self.CustomPluginDirectory        = CustomPluginDirectory
		self.OverrideJobFailureDetection  = OverrideJobFailureDetection
		self.FailureDetectionJobErrors    = FailureDetectionJobErrors
		self.OverrideTaskFailureDetection = OverrideTaskFailureDetection
		self.FailureDetectionTaskErrors   = FailureDetectionTaskErrors
		self.IgnoreBadJobDetection        = IgnoreBadJobDetection
		self.SendJobErrorWarning          = SendJobErrorWarning
		self.Submit_To_ShotGun            = Submit_To_ShotGun
		self.SG_TaskName                  = SG_TaskName
		self.SG_ProjectName               = SG_ProjectName
		self.SG_EntityName                = SG_EntityName 
		self.SG_VersionName               = SG_VersionName 
		self.SG_Description               = SG_Description 
		self.SG_UserName                  = SG_UserName 
		self.SG_Path_To_Frames            = SG_Path_To_Frames
		self.SG_Path_To_File              = SG_Path_To_File
		self.SG_TaskId                    = SG_TaskId
		self.SG_ProjectId                 = SG_ProjectId 
		self.SG_EntityId                  = SG_EntityId 
		self.SG_EntityType                = SG_EntityType

	def create_job_string(self):
		lines = []
		lines.append("Plugin=%s" % self.Plugin)
		lines.append("Frames=%s" % self.Frames)
		lines.append("Name=%s" % self.Name)
		lines.append("Department=%s" % self.Department)
		lines.append("Comment=%s" % self.Comment)
		lines.append("Group=%s" % self.Group)
		lines.append("Pool=%s" % self.Pool)
		lines.append("SecondaryPool=%s" % self.SecondaryPool)
		lines.append("Priority=%s" % str(self.Priority))
		lines.append("InitialStatus=%s" % self.InitialStatus)
		lines.append("OnJobComplete=%s" % self.OnJobComplete)
		
		if self.ChunkSize > 1:
			lines.append("ChunkSize=%s" % str(self.ChunkSize))
				
		if self.ConcurrentTasks > 1:
			lines.append("ConcurrentTasks=%s" % str(self.ConcurrentTasks))
			lines.append("LimitTasksToNumberOfCpus=%s" % str(self.LimitTasksToNumberOfCpus).lower())
			
		if self.ForceReloadPlugin:
			lines.append("ForceReloadPlugin=true")
			
		if self.SynchronizeAllAuxiliaryFiles:
			lines.append("SynchronizeAllAuxiliaryFiles=true")
			
		if len(self.LimitGroups):
			lines.append("LimitGroups=%s" % self.LimitGroups)
			
		if self.MachineLimit:
			lines.append("MachineLimit=%s" % str(self.MachineLimit))
			
		if self.MachineLimitProgress:
			lines.append("MachineLimitProgress=%s" % str(self.MachineLimitProgress))
			
		if self.Machinelist:
			if self.IsBlacklist:
				lines.append("Blacklist=%s" % str(self.Machinelist))
			else:
				lines.append("Whitelist=%s" % str(self.Machinelist))
				
		if self.DeleteOnComplete:
			lines.append("DeleteOnComplete=true")
			
		if self.ArchiveOnComplete:
			lines.append("ArchiveOnComplete=true")
		
		if self.Sequential:
			lines.append("Sequential=true")
		
		if self.Interruptible:
			lines.append("Interruptible=true")
		
		if self.SuppressEvents:
			lines.append("SuppressEvents=true")
					
		if len(self.EnvironmentKeyValue):
			for index, item in enumerate(self.EnvironmentKeyValue.items()):
				lines.append("EnvironmentKeyValue%i=%s=%s" % (index, item[0], str(item[1]) ) )
				
		if self.IncludeEnvironment:
			lines.append("IncludeEnvironment=true")
			
		if self.UseJobEnvironmentOnly:
			lines.append("UseJobEnvironmentOnly=true")
			
		if self.OverrideJobFailureDetection and self.FailureDetectionJobErrors > 0:
			lines.append("OverrideJobFailureDetection=true")
			lines.append("FailureDetectionJobErrors=%s" % str(self.FailureDetectionJobErrors))
			
		if self.OverrideTaskFailureDetection and self.FailureDetectionTaskErrors > 0:
			lines.append("OverrideTaskFailureDetection=true")
			lines.append("FailureDetectionTaskErrors=%s" % str(self.FailureDetectionTaskErrors))
			
		if self.IgnoreBadJobDetection:
			lines.append("IgnoreBadJobDetection=true")
		
		if self.SendJobErrorWarning:
			lines.append("SendJobErrorWarning=true")
			
		if self.MinRenderTimeMinutes:
			lines.append("MinRenderTimeMinutes=%s" % str(self.MinRenderTimeMinutes))
		if self.MinRenderTimeSeconds and not self.MinRenderTimeMinutes:
			lines.append("MinRenderTimeSeconds=%s" % str(self.MinRenderTimeSeconds))
		
		if self.TaskTimeoutMinutes:
			lines.append("TaskTimeoutMinutes=%s" % str(self.TaskTimeoutMinutes))
		if self.TaskTimeoutSeconds and not self.TaskTimeoutMinutes:
			lines.append("TaskTimeoutSeconds=%s" % str(self.TaskTimeoutSeconds))
		
		if self.TaskTimeoutSeconds or self.TaskTimeoutMinutes:
			lines.append("OnTaskTimeout=%s" % str(self.OnTaskTimeout))
			
		if self.EnableAutoTimeout:
			lines.append("EnableAutoTimeout=true")
		
		if self.EnableTimeoutsForScriptTasks:
			lines.append("EnableTimeoutsForScriptTasks=true")
			
		if len(self.JobDependencies):
			lines.append("JobDependencies=%s" % self.JobDependencies)
			
			if self.JobDependencyPercentage:
				lines.append("JobDependencyPercentage=%s" % str(self.JobDependencyPercentage))
		
		if self.IsFrameDependent:
			lines.append("IsFrameDependent=true")
			lines.append("FrameDependencyOffsetStart=%s" % str(self.FrameDependencyOffsetStart))
			lines.append("FrameDependencyOffsetEnd=%s" % str(self.FrameDependencyOffsetEnd))
			
		if not self.ResumeOnCompleteDependencies:
			lines.append("ResumeOnCompleteDependencies=false")
		
		if self.ResumeOnDeletedDependencies:
			lines.append("ResumeOnDeletedDependencies=true")
			
		if self.ResumeOnFailedDependencies:
			lines.append("ResumeOnDeletedDependencies=true")
			
		if len(self.RequiredAssets):
			lines.append("RequiredAssets=%s" % str(self.RequiredAssets))
		if len(self.ScriptDependencies):
			lines.append("ScriptDependencies=%s" % str(self.ScriptDependencies))
		
		#ScheduledType=None
		#ScheduledStartDateTime="dd/MM/yyyy HH:mm"
		#ScheduledDays=1
		if len(self.OutputFilenames):
			for index, name in  enumerate(self.OutputFilenames):
				lines.append("OutputFilename%i=%s" % (index, name) )
		if len(self.OutputDirectorys):
			for index, name in  enumerate(self.OutputDirectorys):
				lines.append("OutputDirectory%i=%s" % (index, name) )
		
		#if len(self.NotificationTargets):
			#lines.append("NotificationTargets=%s" % self.NotificationTargets )
		
		#ClearNotificationTargets=False
		#NotificationEmails=""
		#OverrideNotificationMethod=False
		#EmailNotification=False
		#PopupNotification=False
		#NotificationNote=""
		if len(self.PreJobScript):
			lines.append("PreJobScript=%s" % str(self.PreJobScript))
		if len(self.PostJobScript):
			lines.append("PostJobScript=%s" % str(self.PostJobScript))
		if len(self.PreTaskScript):
			lines.append("PreTaskScript=%s" % str(self.PreTaskScript))
		if len(self.PostTaskScript):
			lines.append("PostTaskScript=%s" % str(self.PostTaskScript))
		#TileJob=False
		#TileJobFrame=0
		#TileJobTilesInX=0
		#TileJobTilesInY=0
		#TileJobTileCount=0
		
		
		if self.Submit_To_ShotGun:
			lines.append("ExtraInfo0=%s" % self.SG_TaskName)
			lines.append("ExtraInfo1=%s" % self.SG_ProjectName)
			lines.append("ExtraInfo2=%s" % self.SG_EntityName)
			lines.append("ExtraInfo3=%s" % self.SG_VersionName)
			lines.append("ExtraInfo4=%s" % self.SG_Description)
			lines.append("ExtraInfo5=%s" % self.SG_UserName)
			lines.append("ExtraInfo6=%s" % self.SG_Path_To_File)
			lines.append("ExtraInfoKeyValue0=VersionName=%s" % self.SG_VersionName)
			lines.append("ExtraInfoKeyValue1=Description=%s" % self.SG_Description)
			lines.append("ExtraInfoKeyValue2=TaskId=%i"      % self.SG_TaskId)
			lines.append("ExtraInfoKeyValue3=ProjectId=%i"   % self.SG_ProjectId)
			lines.append("ExtraInfoKeyValue4=EntityId=%i"    % self.SG_EntityId)
			lines.append("ExtraInfoKeyValue5=EntityType=%s"  % self.SG_EntityType)
			lines.append("ExtraInfoKeyValue6=PathToFile=%s"  % self.SG_Path_To_File)
		else:
			if len(self.ExtraInfo):
				for index, info in enumerate(self.ExtraInfo):
					lines.append("ExtraInfo%i=%s" % (index, str(info)) )
			if len(self.ExtraInfoKeyValues):
				for index, item in enumerate(self.ExtraInfoKeyValues.items()):
					lines.append("ExtraInfoKeyValue%i=%s=%s" % (index, item[0], str(item[1]) ) )
				
		res = "\n".join(lines)
		return res

	#----------------------------------------------------------------------
	def Write_File(self):
		# Get the deadline temp directory.
		submitFilename = Helpers.Data_Access.User_Temp_Directory + "/maya_deadline_info_" + str(self.__class__._counter) + ".job"
		self.__class__._counter += 1
		lines = self.create_job_string()
		# Create the job info file.
		with file(submitFilename,"w") as fileId:
			fileId.write(lines)
		return submitFilename

class Maya_Job_Info_File(Job_Info_File):
	def __init__(self, OutputDirectorys=[]):
		super(Maya_Job_Info_File, self).__init__()
		self.DRG = pm.PyNode("defaultRenderGlobals")
		isinstance(self.DRG, pm.nodetypes.DependNode)
		
		camera = self.DRG.deadlineRenderCamera.get()
		self.Plugin               = "MayaBatch"
		
		if self.DRG.deadlineRenderCamera.get() != "":
			self.Name             = self.DRG.deadlineJobName.get() + " - " + self.DRG.deadlineRenderCamera.get()
		else:
			self.Name             = self.DRG.deadlineJobName.get()
			
		self.Comment              = self.DRG.deadlineJobComment.get("")
		self.Pool                 = self.DRG.deadlineJobPool.get("none")
		self.MachineLimit         = self.DRG.deadlineLimitCount.get(0)
		self.Priority             = self.DRG.deadlineJobPriority.get(50)
		self.OnJobComplete        = self.DRG.deadlineJobOnCompleat.get()
		self.TaskTimeoutMinutes   = self.DRG.deadlineSlaveTimeout.get(0)
		self.MinRenderTimeMinutes = self.DRG.deadlineMinSlaveTimeout.get(0)
		self.ConcurrentTasks      = self.DRG.deadlineConcurrentTasks.get(1)
		self.Department           = self.DRG.deadlineDepartment.get("")
		self.Group                = self.DRG.deadlineGroup.get("none")
		self.LimitGroups          = self.DRG.deadlineLimitGroups.get("")
		self.JobDependencies      = self.DRG.deadlineDependinceList.get("")
		self.MachineList          = self.DRG.deadlineMachineList.get("")
		self.IsBlacklist          = self.DRG.deadlineIsBlacklist.get(False)
		self.Frames               = self.DRG.deadlineFramesList.get("")
		self.ChunkSize            = self.DRG.deadlineChunkSize.get(1)
		
		if self.DRG.deadlineSubmitAsSuspended.get(False):
			self.InitialStatus = "Suspended"
		self.OutputDirectorys = OutputDirectorys
########################################################################
class Job_Submitter(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, job, plugin):
		"""Constructor"""
		self.plugin = plugin
		self.job    = job
		
	def Submit_the_job_to_Deadline(self):
		jobFilename = self.job.Write_File()
		plugin_file_name = self.plugin.Write_File()
		Result, jobId , submitResults = DeadLine_Access.Submit_Deadline_Job(jobFilename, plugin_file_name)
		self.Result        = Result
		self.jobId         = jobId
		self.submitResults = submitResults
		
    
	