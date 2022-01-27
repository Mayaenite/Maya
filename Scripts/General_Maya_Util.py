'''
..
    Red9 Studio Pack: Maya Pipeline Solutions
    Author: Mark Jackson
    email: rednineinfo@gmail.com

    Red9 blog : http://red9-consultancy.blogspot.co.uk/
    MarkJ blog: http://markj3d.blogspot.co.uk


    This is the General library of utils used throughout the modules
    These are abstract general functions

    NOTHING IN THIS MODULE SHOULD REQUIRE RED9

'''
  # required only for Maya2009/8
from functools import wraps
import maya.cmds as cmds
import maya.mel as mel
from . import Singleton
import os
import time
import inspect
import sys
import re
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)



# Generic Utility Functions ---
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
def sortNumerically(data):
	"""
	Sort the given data in the way that humans expect.

	>>> data=['Joint_1','Joint_2','Joint_9','Joint_10','Joint_11','Joint_12']
	>>>
	>>> #standard gives us:
	>>> data.sort()
	>>> ['Joint_1', 'Joint_10', 'Joint_11', 'Joint_12', 'Joint_2', 'Joint_9']
	>>> 
	>>> #sortNumerically gives us:
	>>> sortNumerically(data)
	>>> ['Joint_1', 'Joint_2', 'Joint_9', 'Joint_10', 'Joint_11', 'Joint_12']
	"""
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
	return sorted(data, key=alphanum_key)
#---------------------------------------------------------------------------------
def floatIsEqual(a, b, tolerance=0.01, allowGimbal=True):
	'''
	compare 2 floats with tolerance.

	:param a: value 1 
	:param b: value 2 
	:param tolerance: compare with this tolerance default=0.001 
	:param allowGimbal: allow values differences to be divisible by 180 compensate for gimbal flips 

	'''
	if abs(a - b) < tolerance:
		return True
	else:
		if allowGimbal:
			mod = abs(a - b) % 180.0
			if mod < tolerance:
				log.debug('compare passed with gimbal : %f == %f : diff = %f' % (a, b, mod))
				return True
			elif abs(180.0 - mod) < tolerance:
				log.debug('compare passed with gimbal 180 : %f == %f : diff = %f' % (a, b, abs(180 - mod)))
				return True
			elif abs(90.0 - mod) < tolerance:
				log.debug('compare passed with gimbal 90 : %f == %f diff = %f' % (a, b, abs(90.0 - mod)))
				return True
			log.debug('compare with gimbal failed against mod 180: best diff :%f' % (abs(180.0-mod)))
			log.debug('compare with gimbal failed against mod 90: best diff :%f' % (abs(90.0-mod)))
	log.debug('float is out of tolerance : %f - %f == %f' % (a, b, abs(a - b)))
	return False
#---------------------------------------------------------------------------------
def getCurrentFPS():
	'''
	returns the current frames per second as a number, rather than a useless string
	'''
	fpsDict = {"game":15.0, "film":24.0, "pal":25.0, "ntsc":30.0, "show":48.0, "palf":50.0, "ntscf":60.0}
	return fpsDict[cmds.currentUnit(q=True, fullName=True, time=True)]
#---------------------------------------------------------------------------------
def forceToString(text):
	'''
	simple function to ensure that data can be passed correctly into
	textFields for the UI (ensuring lists are converted)
	'''
	if issubclass(type(text), list):
		return ','.join(text)
	else:
		return text
#---------------------------------------------------------------------------------
def formatPath(path):
	'''
	take a path and format it to forward slashes with catches for the exceptions
	'''
	return os.path.normpath(path).replace('\\','/').replace('\t','/t').replace('\n','/n').replace('\a', '/a')
#---------------------------------------------------------------------------------
def itersubclasses(cls, _seen=None):
	"""
	itersubclasses(cls)
	http://code.activestate.com/recipes/576949-find-all-subclasses-of-a-given-class/
	Iterator to yield full inheritance from a given class, including subclasses. This
	is used in the MetaClass to build the RED9_META_REGISTERY inheritance dict
	"""
	if _seen is None:
		_seen = set()
	try:
		subs = cls.__subclasses__()
	except TypeError:  # fails only when cls is type
		subs = cls.__subclasses__(cls)
	for sub in subs:
		if sub not in _seen:
			_seen.add(sub)
			yield sub
			for sub in itersubclasses(sub, _seen):
				yield sub
#---------------------------------------------------------------------------------
def inspectFunctionSource(value):
	'''
	This is a neat little wrapper over the mel "whatIs" and Pythons inspect
	module that finds the given functions source filePath, either Mel or Python
	and opens the original file in the default program.
	Great for developers
	Supports all Mel functions, and Python Class / functions
	'''
	path=None
	#sourceType=None
	#Inspect for MEL
	log.debug('inspecting given command: %s' % value)
	#if issubclass(sourceType(value),str):
	try:
		path=mel.eval('whatIs("%s")' % value)
		if path and not path=="Command":
			path=path.split("in: ")[-1]
			#if path:
				#sourceType='mel'
		elif path=="Command":
			cmds.warning('%s : is a Command not a script' % value)
			return False
	except Exception as error:
		log.info(error)
	#Inspect for Python
	if not path or not os.path.exists(path):
		log.info('This is not a known Mel command, inspecting Python libs for : %s' % value)
		try:
			log.debug('value :  %s' % value)
			log.debug('value isString : ', isinstance(value, str))
			log.debug('value callable: ', callable(value))
			log.debug('value is module : ', inspect.ismodule(value))
			log.debug('value is method : ', inspect.ismethod(value))
			if isinstance(value, str):
			#if not callable(value):
				value=eval(value)
			path=inspect.getsourcefile(value)
			if path:
				#sourceType='python'
				log.info('path : %s' % path)
		except Exception as error:
			log.exception(error)

	#Open the file with the default editor
	#FIXME: If Python and you're a dev then the .py file may be set to open in the default
	#Python runtime/editor and won't open as expected. Need to look at this.
	if path and os.path.exists(path):
		log.debug('NormPath : %s' % os.path.normpath(path))
		os.startfile(os.path.normpath(path))
		return True
	else:
		log.warning('No valid path or functions found matches selection')
		return False
#---------------------------------------------------------------------------------
def getScriptEditorSelection():
	'''
	this is a hack to bypass an issue with getting the data back from the
	ScriptEditorHistory scroll. We need to copy the selected text to the
	clipboard then pull it back afterwards.
	'''
	import Red9.packages.pyperclip as pyperclip
	control=mel.eval("$v=$gLastFocusedCommandControl")
	executer=mel.eval("$v=$gLastFocusedCommandExecuter")
	reporter=mel.eval("$v=$gLastFocusedCommandReporter")
	func=""
	if control==executer:
		func=cmds.cmdScrollFieldExecuter(control, q=True, selectedText=True)
	elif control == reporter:
		cmds.cmdScrollFieldReporter(reporter, e=True, copySelection=True)
		#func=Clipboard.getText()
		#pyperclip.py : IN TESTING : Platform independant clipboard support
		func=pyperclip.paste()
	log.info('command caught: %s ' % func)
	return func

# Context Managers and Decorators ---
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
def Timer(func):
	'''
	Simple timer decorator
	'''
	@wraps(func)
	def wrapper(*args, **kws):
		t1 = time.time()
		res=func(*args, **kws)
		t2 = time.time()

		functionTrace=''
		try:
			#module if found
			mod = inspect.getmodule(args[0])
			functionTrace+='%s >>' % mod.__name__.split('.')[-1]
		except:
			log.debug('function module inspect failure')
		try:
			#class function is part of, if found
			cls = args[0].__class__
			functionTrace+='%s.' % args[0].__class__.__name__
		except:
			log.debug('function class inspect failure')
		functionTrace += func.__name__
		log.debug('TIMER : %s: took %0.3f ms' % (functionTrace, (t2 - t1) * 1000.0))
		#log.info('%s: took %0.3f ms' % (func.func_name, (t2-t1)*1000.0))
		return res
	return wrapper
#---------------------------------------------------------------------------------
def runProfile(func):
	'''
	run the profiler - only ever used when debugging /optimizing function call speeds.
	visualize the data using 'runsnakerun' to view the profiles and debug
	'''
	import cProfile
	from time import gmtime, strftime

	@wraps(func)
	def wrapper(*args, **kwargs):
		currentTime = strftime("%d-%m-%H.%M.%S", gmtime())
		dumpFileName = 'c:/%s(%s).profile' % (func.__name__, currentTime)
		def command():
			func(*args, **kwargs)
		profile = cProfile.runctx("command()", globals(), locals(), dumpFileName)
		return profile
	return wrapper

########################################################################
class AnimationContext(object):
	"""
	Simple Context Manager for restoring Animation settings
	"""
	def __init__(self):
		self.autoKeyState=None
		self.timeStore=None

	def __enter__(self):
		self.autoKeyState=cmds.autoKeyframe(query=True, state=True)
		self.timeStore=cmds.currentTime(q=True)
		cmds.undoInfo(openChunk=True)

	def __exit__(self, exc_type, exc_value, traceback):
		# Close the undo chunk, warn if any exceptions were caught:
		cmds.autoKeyframe(state=self.autoKeyState)
		cmds.currentTime(self.timeStore)
		log.info('autoKeyState restored: %s' % self.autoKeyState)
		log.info('currentTime restored: %f' % self.timeStore)
		cmds.undoInfo(closeChunk=True)
		if exc_type:
			log.exception('%s : %s'%(exc_type, exc_value))
		# If this was false, it would re-raise the exception when complete
		return True
########################################################################
class undoContext(object):
	"""
	Simple Context Manager for chunking the undoState
	"""
	def __enter__(self):
		cmds.undoInfo(openChunk=True)

	def __exit__(self, exc_type, exc_value, traceback):
		cmds.undoInfo(closeChunk=True)
		if exc_type:
			log.exception('%s : %s'%(exc_type, exc_value))
		# If this was false, it would re-raise the exception when complete
		return True
########################################################################
class ProgressBarContext(object):
	'''
	Context manager to make it easier to wrap progressBars

	>>> #Example of using this in code
	>>> 
	>>> step=5
	>>> progressBar=r9General.ProgressBarContext(1000)
	>>> progressBar.setStep(step)
	>>> count=0
	>>> 
	>>> #now do your code but increment and check the progress state
	>>> with progressBar:
	>>>     for i in range(1:1000):
	>>>        if progressBar.isCanceled():
	>>>             print 'process cancelled'
	>>>             return
	>>>         progressBar.setProgress(count)
	>>>         count+=step

	'''
	def __init__(self, maxValue=100, step=1, interruptable=True):
		if maxValue <= 0:
			raise ValueError("Max has to be greater than 0")
		self._step = step
		self.setStep(step)
		self._maxValue = maxValue
		self._interruptable = interruptable
		self._gMainProgressBar = mel.eval('$tmp = $gMainProgressBar')

	def isCanceled(self):
		#print 'cancelled check : ', cmds.progressBar(self._gMainProgressBar, query=True, isCancelled=True)
		return cmds.progressBar(self._gMainProgressBar, query=True, isCancelled=True)

	def setText(self, text):
		cmds.progressBar(self._gMainProgressBar, edit=True, status=text)

	def setMaxValue(self, value):
		cmds.progressBar(self._gMainProgressBar, edit=True, maxValue=int(value))
		
	def getMaxValue(self, value):
		return cmds.progressBar(self._gMainProgressBar, query=True, maxValue=True)
	
	MaxValue = property(getMaxValue, setMaxValue)

	def setStep(self, value):
		self._step = value
		
	def getStep(self):
		return self._step
	
	steps = property(getStep, setStep)

	def setProgress(self, value):
		cmds.progressBar(self._gMainProgressBar, edit=True, progress=int(value))
		
	def getProgress(self):
		return cmds.progressBar(self._gMainProgressBar, query=True, progress=True)
	
	progress = property(getProgress, setProgress)
		
	def increment(self):
		cmds.progressBar(self._gMainProgressBar, edit=True, step=int(self._step))
		
	def reset(self):
		self.setMaxValue(self._maxValue)
		
	def __enter__(self):
		cmds.progressBar(self._gMainProgressBar,
				         edit=True,
				         beginProgress=True,
				         isInterruptable=self._interruptable,
				         maxValue=self._maxValue)

	def __exit__(self, exc_type, exc_value, traceback):
		cmds.progressBar(self._gMainProgressBar, edit=True, endProgress=True)
		if exc_type:
			log.exception('%s : %s'%(exc_type, exc_value))
		del(self)
		return False  # False so that the exceptiopn gets re-raised
########################################################################
class SceneRestoreContext(object):
	"""
	Simple Context Manager for restoring Scene Global settings

	Basically we store the state of all the modelPanels and timeLine
	setups. Think of it like this, you export a scene, file -new, then re-import it
	but you've now lost all the scenes UI and setups. This is capable of returning 
	the UI to the previous state. Maybe this could be a tool in it's own write?

	Things stored:
	    * All UI viewport states, display and settings
	    * currentTime, timeRanges, timeUnits, sceneUnits, upAxis
	    * Main cameras and transforms for the 4 main modelPanels
	    * active sound and sound displays

	>>> from Red9.core.Red9_General import SceneRestoreContext as sceneStore
	>>> with sceneStore:    
	>>>     #do something to modify the scene setup
	>>>     cmds.currentTime(100)
	>>> 
	>>> #out of the context manager the scene will be restored as it was 
	>>> #before the code entered the context. (with sceneStore:)
	"""
	def __init__(self):
		self.gPlayBackSlider=mel.eval("string $temp=$gPlayBackSlider")
		self.dataStore={}

	def __enter__(self):
		self.storeSettings()

	def __exit__(self, exc_type, exc_value, traceback):
		self.restoreSettings()
		if exc_type:
			log.exception('%s : %s'%(exc_type, exc_value))
		return True

	def storeSettings(self):
		'''
		main work function, store all UI settings
		'''
		self.dataStore['autoKey'] = cmds.autoKeyframe(query=True, state=True)

		# timeline management
		self.dataStore['currentTime'] = cmds.currentTime(q=True)
		self.dataStore['minTime'] = cmds.playbackOptions(q=True, min=True)
		self.dataStore['maxTime'] = cmds.playbackOptions(q=True, max=True)
		self.dataStore['startTime'] = cmds.playbackOptions(q=True, ast=True)
		self.dataStore['endTime'] = cmds.playbackOptions(q=True, aet=True)
		self.dataStore['playSpeed'] = cmds.playbackOptions(query=True, playbackSpeed=True)

		# unit management
		self.dataStore['timeUnit'] = cmds.currentUnit(q=True, fullName=True, time=True)
		self.dataStore['sceneUnits'] = cmds.currentUnit(q=True, fullName=True, linear=True)
		self.dataStore['upAxis'] = cmds.upAxis(q=True, axis=True)

		#panel management
		self.dataStore['panelStore'] = {}
		for panel in ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']:
			if not cmds.modelPanel(panel, q=True, exists=True):
				continue
			self.dataStore['panelStore'][panel] = {}
			self.dataStore['panelStore'][panel]['settings'] = cmds.modelEditor(panel, q=True, sts=True)
			activeCam = cmds.modelPanel(panel, q=True, camera=True)
			if not cmds.nodeType(activeCam) == 'camera':
				activeCam = cmds.listRelatives(activeCam)[0]
			self.dataStore['panelStore'][panel]['activeCam'] = activeCam

		#camera management
		#TODO : store the camera field of view etc also
		self.dataStore['cameraTransforms']={}
		for cam in ['persp', 'top', 'side', 'front']:
			self.dataStore['cameraTransforms'][cam] = [cmds.getAttr('%s.translate' % cam),
						                               cmds.getAttr('%s.rotate' % cam),
						                               cmds.getAttr('%s.scale' % cam)]

		#sound management
		self.dataStore['activeSound'] = cmds.timeControl(self.gPlayBackSlider, q=True, s=1)
		self.dataStore['displaySound'] = cmds.timeControl(self.gPlayBackSlider, q=True, ds=1)

	def restoreSettings(self):
		'''
		restore all UI settings
		'''
		cmds.autoKeyframe(state=self.dataStore['autoKey'])

		#timeline management
		cmds.currentTime(self.dataStore['currentTime'])
		cmds.playbackOptions(min=self.dataStore['minTime'])
		cmds.playbackOptions(max=self.dataStore['maxTime'])
		cmds.playbackOptions(ast=self.dataStore['startTime'])
		cmds.playbackOptions(aet=self.dataStore['endTime'])
		cmds.playbackOptions(ps=self.dataStore['playSpeed'])

		#unit management
		cmds.currentUnit(time=self.dataStore['timeUnit'])
		cmds.currentUnit(linear=self.dataStore['sceneUnits'])
		cmds.upAxis(axis=self.dataStore['upAxis'])

		log.info('Restored PlayBack / Timeline setup')

		#panel management
		for panel, data in list(self.dataStore['panelStore'].items()):
			cmdString = data['settings'].replace('$editorName', panel)
			mel.eval(cmdString)
			log.info("Restored Panel Settings Data >> %s" % panel)
			mel.eval('lookThroughModelPanel("%s","%s")' % (data['activeCam'], panel))
			log.info("Restored Panel Active Camera Data >> %s >> cam : %s" % (panel, data['activeCam']))

		# camera management
		for cam, settings in list(self.dataStore['cameraTransforms'].items()):
			cmds.setAttr('%s.translate' % cam, settings[0][0][0], settings[0][0][1], settings[0][0][2])
			cmds.setAttr('%s.rotate' % cam, settings[1][0][0], settings[1][0][1], settings[1][0][2])
			cmds.setAttr('%s.scale' % cam, settings[2][0][0], settings[2][0][1], settings[2][0][2])
			log.info('Restored Default Camera Transform Data : % s' % cam)

		#sound management
		if self.dataStore['displaySound']:
			cmds.timeControl(self.gPlayBackSlider, e=True, ds=1, sound=self.dataStore['activeSound'])
			log.info('Restored Audio setup')
		else:
			cmds.timeControl(self.gPlayBackSlider, e=True, ds=0)
		return True
# Built In Maya Data Functions And Class Access---
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
def get_Mel_Variable(name):
	if not name.startswith("$"):
		name = "$"+name

	typ = mel.eval('whatIs "%s"' % name)
	if not typ == 'Unknown':

		typ = typ.split()[0]

		if typ.startswith("string"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_SA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_S_Var = %s;' % name)
		elif typ.startswith("int"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_IA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_I_Var = %s;' % name)
		elif typ.startswith("float"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_FA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_F_Var = %s;' % name)
		elif typ.startswith("vector"):
			if typ.endswith("[]"):
				res = mel.eval('$AW_G_VA_Var = %s;' % name)
			else:
				res = mel.eval('$AW_G_V_Var = %s;' % name)
		elif typ.startswith("matrix"):
			res = mel.eval('$AW_G_MX_Var = %s;' % name)
		return res
	else:
		return None
########################################################################
class Mel_Variable(object):
	def __init__(self,name):
		self._name = name

	def get_value(self):
		return get_Mel_Variable(self._name)

	value = property(get_value)
########################################################################
class Mel_Global_Variables(object, metaclass=Singleton.Singleton):
	def __init__(self):
		""""""
		self.rebuild()

	def rebuild(self):
		for name in mel.eval("env"):
			var = Mel_Variable(name)
			setattr(self, name[1:], var)

	#----------------------------------------------------------------------
	def __getattribute__(self,name):
		obj = object.__getattribute__(self,name)
		if hasattr(obj,"value"):
			return obj.value
		return obj
########################################################################
class OptionVar(object):
	#----------------------------------------------------------------------
	def __init__(self,name,val=None):
		self._name = name
		if not self.exists:
			if val == None:
				self.set_value("")
			else:
				self.set_value(val)
	#----------------------------------------------------------------------
	@property
	def name(self):
		return self._name
	#----------------------------------------------------------------------
	def get_value(self):
		if self.exists:
			return cmds.optionVar( query=self.name)
		else:
			return None
	#----------------------------------------------------------------------
	def set_value(self,val):
		typ = type(val)
		if typ == int:
			cmds.optionVar(intValue=[self._name, val])
		elif typ == bool:
			cmds.optionVar(intValue=[self._name, 1 if val else 0])
		elif typ == str:
			cmds.optionVar(stringValue=[self._name, val])
		elif typ == float:
			cmds.optionVar(floatValue=[self._name, val])
	#----------------------------------------------------------------------
	@property
	def varType(self):
		"""returns the type of the val"""
		if self.exists:
			val = self.get_value()
			typ = type(val)
			if typ == list:
				val = val[0]
			return type(val)
		else:
			return None
	#----------------------------------------------------------------------
	@property
	def exists(self):
		"""returns True if a exists, False otherwise."""
		return cmds.optionVar(exists=self._name) == True
	#----------------------------------------------------------------------
	def append(self,val):
		"""adds this value to the end of the array"""
		typ = self.varType
		if typ == int:
			cmds.optionVar(intValueAppend=[self._name, int(val)])
		elif typ == str:
			cmds.optionVar(stringValueAppend=[self._name, str(val)])
		elif typ == float:
			cmds.optionVar(floatValueAppend=[self._name, float(val)])
	#----------------------------------------------------------------------
	def __getitem__(self,index):
		if self.__len__() == 1:
			return self.get_value()
		else:
			return self.get_value()[index]
	#----------------------------------------------------------------------
	def __len__(self):
		return cmds.optionVar(arraySize=self._name)
	#----------------------------------------------------------------------
	value = property(fget=get_value, fset=set_value)
	#----------------------------------------------------------------------
	def __str__(self):
		return repr(self.get_value())
	#----------------------------------------------------------------------
	def __repr__(self):
		return repr(self.get_value())
########################################################################
class OptionVariables(object, metaclass=Singleton.Singleton):
	def __init__(self):
		""""""
		for name in cmds.optionVar( list=True ):
			var = OptionVar(name)
			self.__dict__[name] = var
	#----------------------------------------------------------------------
	def create_Var(self, name, value=None):
		if not hasattr(self, name):
			var = OptionVar(name, value)
			self.__dict__[name] = var
		else:
			var = getattr(self, name)
		return var
	#----------------------------------------------------------------------
	def remove_Var(self, name):
		if hasattr(self, name):
			cmds.optionVar( remove=name )
			del self.__dict__[name]
#---------------------------------------------------------------------------------
# General ---
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
def thumbNailScreen(filepath, width, height, mode='api'):
	path='%s.bmp' % os.path.splitext(filepath)[0]
	if mode=='api':
		thumbnailApiFromView(path, width, height)
		log.debug('API Thumb > path : %s' % path)
	else:
		thumbnailFromPlayBlast(path, width, height)
		log.debug('Playblast Thumb > path : %s' % path)
#---------------------------------------------------------------------------------
def thumbnailFromPlayBlast(filepath, width, height):
	'''
	Generate a ThumbNail of the screen
	Note: 'cf' flag is broken in 2012
	:param filepath: path to Thumbnail
	:param width: width of capture
	:param height: height of capture
	'''
	filepath=os.path.splitext(filepath)[0]
	filename=os.path.basename(filepath)
	filedir=os.path.dirname(filepath)

	#get modelPanel and camera
	win = cmds.playblast(activeEditor=True).split('|')[-1]
	cam = cmds.modelPanel(win, q=True, camera=True)
	if not cmds.nodeType(cam) == 'camera':
		cam = cmds.listRelatives(cam)[0]

	storedformat = cmds.getAttr('defaultRenderGlobals.imageFormat')
	storedResolutionGate = cmds.getAttr('%s.filmFit' % cam)

	cmds.setAttr('defaultRenderGlobals.imageFormat', 20)
	cmds.setAttr('%s.filmFit' % cam, 2)  # set to Vertical so we don't get so much overscan

	cmds.playblast(frame=cmds.currentTime(q=True),  # startTime=cmds.currentTime(q=True),
		           # endTime=cmds.currentTime(q=True),
		           format="image",
		           filename=filepath,
		           width=width,
		           height=height,
		           percent=100,
		           quality=90,
		           forceOverwrite=True,
		           framePadding=0,
		           showOrnaments=False,
		           compression="BMP",
		           viewer=False)
	cmds.setAttr('defaultRenderGlobals.imageFormat', storedformat)
	cmds.setAttr('%s.filmFit' % cam, storedResolutionGate)
	#Why do this rename? In Maya2012 the 'cf' flag fails which means you have to use
	#the 'f' flag and that adds framePadding, crap I know! So we strip it and rename
	#the file after it's made.
	try:
		newfile=[f for f in os.listdir(filedir)
				 if f.split('.bmp')[0].split('.')[0] == filename and not
				 '.pose' in f]
		log.debug('Original Playblast file : %s' % newfile)
		os.rename(os.path.join(filedir, newfile[0]), '%s.bmp' % filepath)
		log.debug('Thumbnail Renamed : %s' % ('%s.bmp' % filepath))
		return '%s.bmp' % filepath
	except:
		pass
#---------------------------------------------------------------------------------
def thumbnailApiFromView(filename, width, height, compression='bmp', modelPanel='modelPanel4'):
	'''
	grab the thumbnail direct from the buffer?
	TODO: not yet figured out how you crop the data here?
	'''
	import maya.OpenMaya as OpenMaya
	import maya.OpenMayaUI as OpenMayaUI

	#Grab the last active 3d viewport
	view = None
	if modelPanel is None:
		view = OpenMayaUI.M3dView.active3dView()
	else:
		try:
			view = OpenMayaUI.M3dView()
			OpenMayaUI.M3dView.getM3dViewFromModelEditor(modelPanel, view)
		except:
			#in case the given modelPanel doesn't exist!!
			view = OpenMayaUI.M3dView.active3dView()

	#read the color buffer from the view, and save the MImage to disk
	image = OpenMaya.MImage()
	view.readColorBuffer(image, True)
	image.resize(width, height, True)
	image.writeToFile(filename, compression)
	log.info('API Thumbname call path : %s' % filename)
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
def getModifier():
	'''
	return the modifier key pressed
	'''
	mods = cmds.getModifiers()
	if mods == 1:
		return 'Shift'
	if mods == 4:
		return 'Ctrl'
	if mods == 8:
		return 'Alt'
	if mods == 5:
		return 'Ctrl+Shift'
	if mods == 9:
		return 'Alt+Shift'
	if mods == 12:
		return 'Ctrl+Alt'
	if mods == 13:
		return 'Ctrl+Alt+Shift'
	else:
		return None


# OS functions ---
#---------------------------------------------------------------------------------
########################################################################
class Clipboard:
	'''
	Get or Set data to the Windows clipboard...Used in the inspect code to grab the
	ScriptEditor's selected history
	CURRENTLY NOT BEING CALLED - switched to pyperclip.py module
	'''

	@staticmethod
	def getText():
		'''
		Get clipboard text if available
		'''
		import ctypes

		# declare win32 API
		user32 = ctypes.windll.user32
		kernel32 = ctypes.windll.kernel32

		if not user32.OpenClipboard(0):
			return ''

		CF_TEXT = 1
		hClipMem = user32.GetClipboardData(CF_TEXT)
		kernel32.GlobalLock.restype = ctypes.c_char_p
		value = kernel32.GlobalLock(hClipMem)
		kernel32.GlobalUnlock(hClipMem)
		user32.CloseClipboard()

		if isinstance(value, str):
			return value
		elif hasattr(value, 'decode'):
			return value.decode(sys.getfilesystemencoding())
		else:
			return ''

	@staticmethod
	def setText(value):
		'''
		Set clipbard text
		'''
		import ctypes

		if not isinstance(value, str):
			raise TypeError('value should be of str type')

		# declare win32 API
		user32 = ctypes.windll.user32
		kernel32 = ctypes.windll.kernel32

		GlobalLock = kernel32.GlobalLock
		memcpy = ctypes.cdll.msvcrt.memcpy

		CF_TEXT = 1
		GHND = 66

		buf = ctypes.c_buffer(value.encode(sys.getfilesystemencoding()))
		bufferSize = ctypes.sizeof(buf)
		hGlobalMem = kernel32.GlobalAlloc(GHND, bufferSize)
		GlobalLock.restype = ctypes.c_void_p
		lpGlobalMem = GlobalLock(hGlobalMem)
		memcpy(lpGlobalMem, ctypes.addressof(buf), bufferSize)
		kernel32.GlobalUnlock(hGlobalMem)

		if user32.OpenClipboard(0):
			user32.EmptyClipboard()
			user32.SetClipboardData(CF_TEXT, hGlobalMem)
			user32.CloseClipboard()
			return True


#---------------------------------------------------------------------------------
def os_OpenFileDirectory(path):
	'''
	open the given folder in the default OS browser
	'''
	import subprocess
	path=os.path.abspath(path)
	if sys.platform == 'win32':
		subprocess.Popen('explorer /select, "%s"' % path)
	elif sys.platform == 'darwin':  # macOS
		subprocess.Popen(['open', path])
	else:  # linux
		try:
			subprocess.Popen(['xdg-open', path])
		except OSError:
			raise OSError('unsupported xdg-open call??')

#---------------------------------------------------------------------------------
def os_OpenFile(filePath):
	'''
	open the given file in the default program for this OS
	'''
	import subprocess
	#log.debug('filePath : %s' % filePath)
	#filePath=os.path.abspath(filePath)
	#log.debug('abspath : %s' % filePath)
	if sys.platform == 'win32':
		os.startfile(filePath)
	elif sys.platform == 'darwin':  # macOS
		subprocess.Popen(['open', filePath])
	else:  # linux
		try:
			subprocess.Popen(['xdg-open', filePath])
		except OSError:
			raise OSError('unsupported xdg-open call??')
