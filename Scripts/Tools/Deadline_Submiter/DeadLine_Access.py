try:
	import subprocess_original as subprocess
except:
	import subprocess
import os
import datetime
def get_DeadLine_Exacutble():
	Bin         = os.environ.get("DEADLINE_PATH")
	exe         = "deadlinecommand.exe"
	path        = os.path.join(Bin,exe)
	exacutble   = '"%s"' % path
	return exacutble

def get_Temp_Result_File():
	temp_folder = os.environ['TEMP']
	temp_file   = "dead_line_output.txt"
	temp_path   = os.path.join(temp_folder,temp_file)
	return temp_path

def CallDeadlineCommand(command):
	if not command.startswith("-"):
		command = "-" + command
	
	exacutble = get_DeadLine_Exacutble()
	command   = exacutble + " " + command
	try:
		submit = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	except:
		temp_file = get_Temp_Result_File()
		with file(temp_file, "w") as f:
			submit = subprocess.Popen(command, stdin=f, stdout=subprocess.PIPE, shell=True)
	out  = submit.communicate()[0]
	return out.splitlines()

def Submit_Deadline_Job(job_info_file, job_settings_file):
	exacutble = get_DeadLine_Exacutble()
	command   = " ".join([exacutble, job_info_file, job_settings_file])
	try:
		submit = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	except:
		temp_file = get_Temp_Result_File()
		with file(temp_file, "w") as f:
			submit = subprocess.Popen(command, stdin=f, stdout=subprocess.PIPE, shell=True)
	out  = submit.communicate()[0]
	lines = out.splitlines()
	Result = False
	jobid  = None
	for line in lines:
		data = line.split("=")
		if len(data) == 2:
			if data[0] == "Result":
				if data[1] == "Success":
					Result = True
				else:
					Result = False
			elif data[0] == "JobID":
				jobid = data[1]
	return Result, jobid, out

def Start_Process(file_name):
	"""Starts the program or program associated with the file"""
	CallDeadlineCommand('StartProcess %s' % file_name)
	
def SlaveNames():
	""" All the slave names"""
	return CallDeadlineCommand("GetSlaveNames")

def GetSlaves(Names):
	""" Display information for the slave
		Names: The slave name, or a list of slave names separated by commas
	"""
	return CallDeadlineCommand('GetSlave %s' % Names)

def SlaveStatistics():
	""" Displays quick summary information of slaves"""
	return CallDeadlineCommand('GetSlaveStatistics')
	
def SlaveSetting(slave, setting):
	""" Gets the value of a setting for the slave
		Names: The slave name, or a list of slave names separated by commas
	"""
	return CallDeadlineCommand('GetSlaveSetting %s %s' % (slave, setting) )

def RepositoryRoot():
	"""Display the repository network root"""
	res = CallDeadlineCommand('GetRepositoryRoot')[0]
	return res

def Root():
	""" Display the repository network root"""
	return CallDeadlineCommand('Root')



def Networks():
	"""Display all repository roots in the Deadline config file"""
	return CallDeadlineCommand('Networks')

def Select_Repository():
	"""Select the repository root from a dialog"""
	return CallDeadlineCommand('SelectRepository')
def Select_Network():
	"""Select the repository root from a dialog"""
	return CallDeadlineCommand('SelectNetwork')
def Select_MachineList(items=None):
	"""Allows you to select a list of machines, then prints them to stdout"""
	cmd = "SelectMachineList"
	if items is not None and not items == "":
		cmd = cmd + ' %s' % items
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
		if res == "Action was cancelled by user":
			res = False
	else:
		res = False
	return res
def Select_LimitGroups(items=None):
	"""Allows you to select a list of limit, then prints them to stdout"""
	cmd = "SelectLimitGroups"
	if items is not None and not items == "":
		cmd = cmd + ' %s' % items
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
		if res == "Action was cancelled by user":
			res = False
	else:
		res = False
	return res

def Select_Directory(path=None):
	"""Opens a folder browser and prints out the result"""
	cmd = "SelectDirectory"
	if path is not None:
		cmd = cmd + ' %s' % path
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
	else:
		res = ''
	res = res.replace("\\", "/")
	return res
def Select_Dependencies(items=None):
	"""Allows you to select a list of dependencies,then prints them to stdout"""
	cmd = "SelectDependencies"
	if items is not None and not items == "":
		cmd = cmd + ' %s' % items
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
		if  res == "Action was cancelled by user":
			res = False
	else:
		res = False
	return res
def Select_FilenameLoad(path=None, filters=None):
	"""Opens a file load dialog and prints out the result"""
	cmd = "SelectFilenameLoad"
	if path is not None:
		cmd = cmd + ' %s' % path
	else:
		cmd = cmd + ' ""' % path
	if filters is not None:
		cmd = cmd + ' %s' % filters
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
	else:
		res = ''
	res = res.replace("\\", "/")
	return res

def Select_FilenameSave(path=None, filters=None):
	"""Opens a file save dialog and prints out the result"""
	cmd = "SelectFilenameSave"
	if path is not None:
		cmd = cmd + ' %s' % path
	else:
		cmd = cmd + ' ""' % path
	if filters is not None:
		cmd = cmd + ' %s' % filters
	res = CallDeadlineCommand(cmd)
	if len(res):
		res = res[0]
	else:
		res = ''
	res = res.replace("\\", "/")
	return res
def Get_LimitGroupNames():
	"""Display all limit names"""
	return CallDeadlineCommand('GetLimitGroupNames')

def Get_LimitGroups():
	"""Displays information for all limits"""
	return CallDeadlineCommand('GetLimitGroups')

def Get_LimitGroup(name):
	"""Displays information for The limitGroup name, or a list of names separated by commas"""
	return CallDeadlineCommand('GetLimitGroup '+name)

def Get_UserNames():
	""" Display all the user names"""
	return CallDeadlineCommand('GetUserNames')

def Get_Users():
	""" Displays information for all users"""
	return CallDeadlineCommand('GetUsers')

def Get_User(name):
	"""Displays information for the user or a list of names separated by commas"""
	return CallDeadlineCommand('GetUser ' + name)

def Get_CurrentUserName():
	"""Display the current Deadline user"""
	return CallDeadlineCommand('GetCurrentUserName')

def Get_PluginNames():
	"""Displays all plugin names"""
	return CallDeadlineCommand('GetPluginNames')

def Get_MaximumPriority():
	"""Displays the maximum priority value for jobs"""
	return int(CallDeadlineCommand('GetMaximumPriority')[0])

def Get_PoolNames():
	"""Displays all pool names"""
	return CallDeadlineCommand('GetPoolNames')

def Get_GroupNames():
	"""Displays all groups"""
	return CallDeadlineCommand('GetGroupNames')

def Get_JobErrorReportFilenames(Job_ID):
	"""Gets the error report filenames for the job"""
	return CallDeadlineCommand('GetJobErrorReportFilenames '+str(Job_ID))

def Get_JobLogReportFilenames(Job_ID):
	"""Gets the log report filenames for the job"""
	return CallDeadlineCommand('GetJobLogReportFilenames '+str(Job_ID))

def Get_SlaveErrorReportFilenames(slave):
	"""Gets the error report filenames for the slave"""
	return CallDeadlineCommand('GetSlaveErrorReportFilenames '+str(slave))

def Get_FarmStatistics():
	"""Displays quick summary information of jobs and slaves"""
	return CallDeadlineCommand('GetFarmStatistics')

def Get_FarmStatisticsEx():
	"""Displays quick summary information of jobs and slave"""
	return CallDeadlineCommand('GetFarmStatisticsEx')

def Get_CurrentUserHomeDirectory():
	"""Displays the current user home directory of the Deadline Client software"""
	return CallDeadlineCommand("GetCurrentUserHomeDirectory")[0]

def ChangeUser():
	"""Changes the current Deadline user on this machine"""
	return CallDeadlineCommand("ChangeUser")

def ShowMessageBox(title="Message", message="This is The Message", buttons=[]):
	"""Displays a simple dialog box and prints out the button selected"""
	command = 'ShowMessageBox -title "%s" -message "%s"' % (title, message)
	if len(buttons):
		buttons = ",".join([str(bnt) for bnt in buttons])
		command += ' -buttons %s' % buttons
	return CallDeadlineCommand(command)

def PopupMessage(message, del_message=False):
	""" Displays a popup message"""
	command = 'PopupMessage "%s" ' % message
	if del_message:
		command += ' true'
	else:
		command += ' false'
	return CallDeadlineCommand(command)

def ExecuteScript(script):
	"""Executes the script"""
	command = 'ExecuteScript %s' % script
	return CallDeadlineCommand(command)

def ConnectToSlaveLog(SlaveName, window=True):
	"""Connect to a remote slave to watch its log in real time. Press Enter at any time to disconnect from the slave."""
	command = 'ConnectToSlaveLog %s' % SlaveName
	if window:
		command += " true"
	else:
		command += " false"
	return CallDeadlineCommand(command)

def Get_JobIds():
	""" Displays all the job IDs"""
	return CallDeadlineCommand("GetJobIds")

def Get_Jobs():
	"""Displays information for all the jobs"""
	return CallDeadlineCommand("GetJobs")

def Get_Job(ID):
	"""Display information for the job(s)"""
	command = 'GetJob %r' % ID
	return CallDeadlineCommand(command)

def Get_TaskProgress(ID):
	"""Display progress information about the job's tasks"""
	command = 'GetTaskProgress %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTaskTotalTime(ID):
	"""Display total task render time for the job"""
	command = 'GetJobTaskTotalTime %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTaskAverageTime(ID):
	"""Display average task render time for the job"""
	command = 'GetJobTaskAverageTime %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTaskTotalTimeNorm(ID):
	"""Display total task normalized render time for the job"""
	command = 'GetJobTaskTotalTimeNorm %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTaskAverageTimeNorm(ID):
	"""Display average task normalized render time for the job"""
	command = 'GetJobTaskAverageTimeNorm %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTaskIds(ID):
	""" Display the task IDs for the job"""
	command = 'GetJobTaskIds %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTasks(ID):
	"""Display the tasks for the job"""
	command = 'GetJobTasks %r' % ID
	return CallDeadlineCommand(command)

def Get_JobTask(job_ID, task_ID):
	"""Display the specified task for the job"""
	command = 'GetJobTask %r %r' % (job_ID, task_ID)
	return CallDeadlineCommand(command)

def Get_SlavesRenderingJob(job_ID):
	"""Display the slaves that are rendering the job. If the second parameter is 'true', the slave IP addresses will be shown instead."""
	command = 'GetSlavesRenderingJob %r' % (job_ID)
	return CallDeadlineCommand(command)

def Get_JobSetting(job_ID, setting):
	""" Gets the value of a setting for the job"""
	command = 'GetJobSetting %s %s' % (job_ID, setting)
	return CallDeadlineCommand(command)

def Get_JobStatistics():
	""" Archives the job"""
	command = 'GetJobStatistics'
	return CallDeadlineCommand(command)
def SuspendJob(job_IDs):
	""" Suspends the job"""
	command = 'SuspendJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def CompleteJob(job_IDs):
	""" Completes a job"""
	command = 'CompleteJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def FailJob(job_IDs):
	"""Fails a job"""
	command = 'FailJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def PendJob(job_IDs):
	"""Marks the job as pending (if it has job dependencies, required assets, or scheduling settings)"""
	command = 'PendJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def ReleasePendingJob(job_IDs):
	"""Releases the pending job"""
	command = 'ReleasePendingJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def ResumeJob(job_IDs):
	"""Resumes the job"""
	command = 'ResumeJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def ResumeFailedJob(job_IDs):
	"""Resumes the failed job"""
	command = 'ResumeFailedJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def DeleteJob(job_IDs):
	""" Deletes the job(s)"""
	command = 'DeleteJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def RequeueJob(job_IDs):
	""" Requeues the job"""
	command = 'RequeueJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

def ArchiveJob(job_IDs):
	""" Archives the job"""
	command = 'ArchiveJob %s' % (job_IDs)
	return CallDeadlineCommand(command)

"""
PrettyJson                    Turn on output as PrettyJson. Then run the next command if given.

AddGroup                      Adds the group
  [Group Name]                The group name


DeleteGroup                   Deletes the group
  [Group Name]                The group name


PurgeObsoleteGroups           Purges groups that are no longer in use
  [Group Name]                The replacement group for jobs that are using
                              obsolete groups (optional)

AddPool                       Adds the pool
  [Pool Name(s)]              The pool name, or a list of names separated by
                              commas


DeletePool                    Deletes the pool
  [Pool Name]                 The pool name


PurgeObsoletePools            Purges pools that are no longer in use
  [Pool Name]                 The replacement pool for jobs that are using
                              obsolete pools (optional)

UpgradePluginSettings         Used by installer to upgrade the plugins without
                              overriding user configured settings
  [Repository Root]           The repository root
SetUser                       Modifies or creates the user.
  [User Name]                 The user name
  [Email]                     Their email address
  [Machine Name]              Their machine name
  [Notify By Email]           If they want email notifications (true/false)
  [Notify By Popup Message]   If they want popup notifications (true/false)
  [User Group]                Optional. The user group (or list of groups
                              separated by commas) to add the user to. By
                              default, the user is already part of the
                              Everyone group.


DeleteUser                    Deletes the user
  [User Name(s)]              The user name, or a list of names separated by
                              commas


AddUserToUserGroup            Adds a user to the user group
  [User Name(s)]              The user name, or a list of user names separated
                              by commas
  [User Group Name(s)]        The user group name, or a list of user group
                              names separated by commas


RemoveUserFromUserGroup       Removes a user from the user group
  [User Name(s)]              The user name, or a list of user names separated
                              by commas
  [User Group Name(s)]        The user group name, or a list of user group
                              names separated by commas


SetUserForUserGroup           Removes a user from the user group
  [User Name(s)]              The user name, or a list of user names separated
                              by commas
  [User Group Name(s)]        The user group name, or a list of user group
                              names separated by commas


SetLimitGroup                 Modifies or creates the limit
  [Limit Name]                The limit name
  [Limit]                     The new limit
  [Listed Slaves]             The listed slaves
  [Whilelist Flag]            true/false
  [Limit Progress]            The limit progress (optional)
  [Excluded Slaves]           The excluded slaves (optional)


DeleteLimitGroup              Deletes the limit
  [Limit Name(s)]             The limit name, or a list of names separated by
                              commas
							  
GetSlaveNamesInPool           Displays the slave names that have been assigned
                              to the specified pool
  [Pool Name(s)]              The pool name, or a list of pool names separated
                              by commas


GetSlaveNamesInGroup          Displays the slave names that have been assigned
                              to the specified group
  [Group Name(s)]             The group name, or a list of group names
                              separated by commas

SetPoolsForSlave              Sets the pools for a slave
  [Slave Name(s)]             The slave name, or a list of slave names
                              separated by commas
  [Pool Name(s)]              The pool name, or a list of pool names separated
                              by commas


SetGroupsForSlave             Sets the groups for a slave
  [Slave Name(s)]             The slave name, or a list of slave names
                              separated by commas
  [Group Name(s)]             The group name, or a list of group names
                              separated by commas


AddPoolToSlave                Adds a pool to the slave
  [Slave Name(s)]             The slave name, or a list of slave names
                              separated by commas
  [Pool Name(s)]              The pool name, or a list of pool names separated
                              by commas


AddGroupToSlave               Adds a group to the slave
  [Slave Name(s)]             The slave name, or a list of slave names
                              separated by commas
  [Group Name(s)]             The group name, or a list of group names
                              separated by commas


RemovePoolFromSlave           Removes a pool from the slave
  [Slave Name(s)]             The slave name, or a list of slave names
                              separated by commas
  [Pool Name(s)]              The pool name, or a list of pool names separated
                              by commas


RemoveGroupFromSlave          Removes a group from the slave
  [Slave Name(s)]             The slave name, or a list of slave names
                              separated by commas
  [Group Name(s)]             The group name, or a list of group names
                              separated by commas
							  
"""


