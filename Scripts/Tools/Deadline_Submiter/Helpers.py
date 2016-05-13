
import maya.cmds  as cmds
import pymel.core as pm
import DeadLine_Access
import os
#---------------------------------------------------------
# Functions for saving submission in a compound attribute.
#---------------------------------------------------------
def AddBoolAttribute(attrName, default=True):
	apply_defaut = False
	if not cmds.attributeQuery( attrName,node='defaultRenderGlobals', exists=True ):
		res = pm.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='bool')
		apply_defaut = True
		
	res = pm.PyNode("defaultRenderGlobals."+attrName)
	
	if res.type() != "bool":
		val = res.get()
		res.delete()
		pm.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='bool')
		res = pm.PyNode("defaultRenderGlobals."+attrName)
		try:
			res.set(val)
		except:
			apply_defaut = True
			
	if apply_defaut:
		res.set(default)
		
	isinstance(res, pm.Attribute)
	return res
#---------------------------------------------------------
def AddStringAttribute(attrName, default=""):
	apply_defaut = False
	if not cmds.attributeQuery( attrName,node='defaultRenderGlobals', exists=True ):
		res = pm.addAttr('defaultRenderGlobals',shortName=attrName,dt="string",longName=attrName)
		apply_defaut = True
	res = pm.PyNode("defaultRenderGlobals."+attrName)
	if apply_defaut:
		res.set(default)
	isinstance(res, pm.Attribute)
	return res
#---------------------------------------------------------
def AddEnumAttribute(attrName, default=""):
	apply_defaut = False
	if isinstance(default, str):
		default = default.split(":")
	if not cmds.attributeQuery( attrName,node='defaultRenderGlobals', exists=True ):
		pm.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at="enum",enumName=":".join(default))
	res = pm.PyNode("defaultRenderGlobals."+attrName)
	res.setEnums(default)
	isinstance(res, pm.Attribute)
	return res
#---------------------------------------------------------
def AddLongAttribute(attrName, default=0, minVal=None, maxVal=None):
	apply_defaut = False
	if not cmds.attributeQuery( attrName,node='defaultRenderGlobals', exists=True ):
		res = pm.addAttr('defaultRenderGlobals',shortName=attrName,at='long',longName=attrName)
		apply_defaut = True
	res = pm.PyNode("defaultRenderGlobals."+attrName)
	isinstance(res, pm.Attribute)
	if apply_defaut:
		res.set(default)
		
	if minVal != None:
		res.setMin(minVal)
		
	if maxVal != None:
		res.setMax(maxVal)
	return res
#---------------------------------------------------------
def AddStrArrayAttribute(attrName, default=[]):
	apply_defaut = False
	if not cmds.attributeQuery( attrName,node='defaultRenderGlobals', exists=True ):
		res = pm.addAttr('defaultRenderGlobals',shortName=attrName,dt='stringArray',longName=attrName)
		apply_defaut = True
	res = pm.PyNode("defaultRenderGlobals."+attrName)
	if apply_defaut:
		res.set(default)
	isinstance(res, pm.Attribute)
	return res
#---------------------------------------------------------
def Add_Child_Bool_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='bool', parent=parent)
#---------------------------------------------------------	
def Add_Child_Byte_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='byte', parent=parent)
#---------------------------------------------------------
def Add_Child_Char_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='char', parent=parent)
#---------------------------------------------------------	
def Add_Child_Enum_Attribute(attrName, parent, enumName):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at="enum",enumName=enumName, parent=parent)
#---------------------------------------------------------
def Add_Child_Float_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='float', parent=parent)
#---------------------------------------------------------
def Add_Child_Float2_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='float3', parent=parent)
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"X", longName=attrName+"X", at='float', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Y", longName=attrName+"Y", at='float', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Z", longName=attrName+"Z", at='float', parent=attrName )
#---------------------------------------------------------
def Add_Child_Float2_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='float2', parent=parent)
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"X", longName=attrName+"X", at='float', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Y", longName=attrName+"Y", at='float', parent=attrName )
#---------------------------------------------------------
def Add_Child_Long_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='long', parent=parent)
#---------------------------------------------------------	
def Add_Child_Long2_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='long2', parent=parent)
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"X", longName=attrName+"X", at='long', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Y", longName=attrName+"Y", at='long', parent=attrName )
#---------------------------------------------------------
def Add_Child_Long3_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='long3', parent=parent)
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"X", longName=attrName+"X", at='long', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Y", longName=attrName+"Y", at='long', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Z", longName=attrName+"Z", at='long', parent=attrName )
#---------------------------------------------------------
def Add_Child_Short_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='short', parent=parent)
#---------------------------------------------------------	
def Add_Child_Short2_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='short2', parent=parent)
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"X", longName=attrName+"X", at='short', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Y", longName=attrName+"Y", at='short', parent=attrName )
#---------------------------------------------------------
def Add_Child_Short3_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, at='short3', parent=parent)
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"X", longName=attrName+"X", at='short', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Y", longName=attrName+"Y", at='short', parent=attrName )
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName+"Z", longName=attrName+"Z", at='short', parent=attrName )
#---------------------------------------------------------
def Add_Child_String_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, dt="string", parent=parent)
#---------------------------------------------------------	
def Add_Child_StrArray_Attribute(attrName, parent):
	cmds.addAttr( "defaultRenderGlobals", shortName=attrName, longName=attrName, dt='stringArray', parent=parent)
#---------------------------------------------------------
def AddCompoundAttribute(attrName, child_attribs):
	if not cmds.attributeQuery( attrName,node='defaultRenderGlobals', exists=True ):
		child_count = len(child_attribs)
		cmds.addAttr('defaultRenderGlobals', shortName=attrName, longName=attrName, numberOfChildren=child_count, attributeType='compound' )
		for typ, name in child_attribs:
			if typ == "bool":
				Add_Child_Bool_Attribute(name,attrName)
			elif typ == "byte":
				Add_Child_Byte_Attribute(name,attrName)
			elif typ == "char":
				Add_Child_Char_Attribute(name,attrName)
			elif typ == "enum":
				Add_Child_Enum_Attribute(name,attrName,"Green:Blue:")
			elif typ == "long":
				Add_Child_Long_Attribute(name, attrName)
			elif typ == "long2":
				Add_Child_Long2_Attribute(name, attrName)
			elif typ == "long3":
				Add_Child_Long3_Attribute(name, attrName)
			elif typ == "short":
				Add_Child_Short_Attribute(name, attrName)
			elif typ == "short2":
				Add_Child_Short2_Attribute(name, attrName)
			elif typ == "short3":
				Add_Child_Short3_Attribute(name, attrName)
			elif typ == "float":
				Add_Child_Float_Attribute(name, attrName)
			elif typ == "float2":
				Add_Child_Float2_Attribute(name, attrName)
			elif typ == "float3":
				Add_Child_Float3_Attribute(name, attrName)
			elif typ == "string":
				Add_Child_String_Attribute(name, attrName)
			elif typ == "stringArray":
				Add_Child_StrArray_Attribute(name, attrName)

#=================================================================
#---------------------------------------------------------
# Maya Helper Functions
#---------------------------------------------------------

#---------------------------------------------------------
def GetOutputPrefix(replaceFrameNumber,newFrameNumber,layerName,cameraName):
	"""
	Returns the output prefix as is shown in the Render Globals, except that the frame
	number is replaced with '?' padding.
	global proc string GetOutputPrefix( int $replaceFrameNumber, int $newFrameNumber )
	"""
	outputPrefix=""
	paddingString=""
	renderer= Data_Access.currentRenderer
	if renderer == "vray":
		pm.melGlobals.initVar( 'string[]', 'g_vrayImgExt' )
		# Need to special case vray, because they like to do things differently.
		ext=""
		if pm.optionMenuGrp("vrayImageFormatMenu", exists=True):
			ext=str(pm.optionMenuGrp("vrayImageFormatMenu",q=1,v=1))
		else:
			ext=pm.getAttr('vraySettings.imageFormatStr')
			# VRay can append this to the end of the render settings display, but we don't want it in the file name.

		isMultichannelExr=False
		multichannel=" (multichannel)"
		if ext.endswith(multichannel):
			ext=ext[0:-len(multichannel)]
			isMultichannelExr=True

		prefix=str(pm.getAttr('vraySettings.fileNamePrefix'))
		# We need to use eval because the definition of vrayTransformFilename is different for
		# different versions of vray, and this is the only way to get around the "incorrect
		# number of arguments" error.
		# Don't transform if the prefix is blank, so we can just default to the scene file name.
		if prefix != "":
			if not pm.catch( lambda: pm.mel.eval("vrayTransformFilename( \"\", \"\", \"\", 0 )") ):
				sceneName=Data_Access.StrippedSceneFileName
				prefix=str(pm.mel.eval("vrayTransformFilename( \"" + prefix + "\", \"" + cameraName + "\", \"" + sceneName + "\", 0 )"))
			elif not pm.catch( lambda: pm.mel.eval("vrayTransformFilename( \"\", \"\", \"\" )") ):
				prefix=str(pm.mel.eval("vrayTransformFilename( \"" + prefix + "\", \"\", \"\" )"))
			elif not pm.catch( lambda: pm.mel.eval("vrayTransformFilename( \"\", \"\" )") ):
				prefix=str(pm.mel.eval("vrayTransformFilename( \"" + prefix + "\", \"\" )"))
		if prefix == "":
			prefix=str(Data_Access.StrippedSceneFileName)
		if Data_Access.IsAnimatedOn:
			padding=4
			# Seems to be a bug where no matter what, VRay will use 4 digits for padding.
			# If ever fixed, try using the value from the vray settings.
			#int $padding = `getAttr vraySettings.fileNamePadding`;
			for i in range(0,padding):
				paddingString=paddingString + "#"
				# When rendering to a non-raw format, vray places a period before the padding, even though it
				# doesn't show up in the render globals filename.

			if ext == "vrimg" or isMultichannelExr:
				outputPrefix=prefix + paddingString + "." + ext
			else:
				outputPrefix=prefix + "." + paddingString + "." + ext
		elif ext == "vrimg" or isMultichannelExr:
			outputPrefix=prefix + "." + ext
			# When rendering to a non-raw format, vray places a period before the padding, even though it
			# doesn't show up in the render globals filename.
		else:
			outputPrefix=prefix + "." + ext
	else:
		paddingFound=0
		# Get the first output prefix.
		prefixString=""
		if renderer == "renderMan":
			prefixString=str(pm.mel.rmanGetImageName(1))


		elif renderer == "MayaKrakatoa":
			prefixes=pm.renderSettings(fin=1,cam=cameraName,lyr=layerName)
			#string $prefixes[] = `renderSettings -fin`;
			prefixString=prefixes[0]
			forceEXROutput=int(pm.getAttr("MayaKrakatoaRenderSettings.forceEXROutput"))
			if forceEXROutput == 1:
				tokens=[]
				tokens=prefixString.split(".")
				result=""
				i=0
				for i in range(0,len(tokens) - 1):
					result+=tokens[i] + "."

				prefixString=result + "exr"



		else:
			prefixes=pm.renderSettings(fin=1,cam=cameraName,lyr=layerName)
			#string $prefixes[] = `renderSettings -fin`;
			prefixString=prefixes[0]

		prefixWithColons=""
		# Go through each letter of the prefix and create a new prefix with each letter
		# separated by colons, ie: f:i:l:e:n:a:m:e:.:e:x:t:
		for i in range(1,len(prefixString)+1):
			prefixWithColons+=prefixString[i-1:i] + ":"
			# Now split up the new prefix into an array, which removes all the colons and
			# places one letter in each index. Then count backwards and replace the first
			# group of numbers with the padding characters.

		prefix=prefixWithColons.split(":")
		if Data_Access.IsAnimatedOn:
			for i in range(len(prefix),0,-1):
				if pm.mel.match("[0-9]", prefix[i]) != "":
					prefix[i]="#"
					paddingString=paddingString + "#"
					paddingFound=1


				elif paddingFound:
					break



		outputPrefix="".join(prefix)
		# Finally, convert the prefix array back to a string.

	if Data_Access.IsAnimatedOn and replaceFrameNumber:
		paddedFrame="" + str(newFrameNumber)
		while len(paddedFrame)<len(paddingString):
			paddedFrame="0" + paddedFrame


		outputPrefix=str(pm.mel.substituteAllString(outputPrefix, paddingString, paddedFrame))

	return outputPrefix

#=================================================================
class Frame_Range(object):
	defaultRenderGlobals = pm.PyNode("defaultRenderGlobals")
	@property
	#----------------------------------------------------------------------
	def startFrame(self):
		""""""
		if self.defaultRenderGlobals.animation.get():
			return self.defaultRenderGlobals.startFrame.get()
		else:
			return pm.currentTime(q=1)
	@property
	#----------------------------------------------------------------------
	def endFrame(self):
		""""""
		if self.defaultRenderGlobals.animation.get():
			return self.defaultRenderGlobals.endFrame.get()
		else:
			return pm.currentTime(q=1)
	@property
	#----------------------------------------------------------------------
	def frameStep(self):
		""""""
		if self.defaultRenderGlobals.animation.get():
			return self.defaultRenderGlobals.byFrameStep.get()
		else:
			return 1
	@property
	#----------------------------------------------------------------------
	def frame_expression(self):
		""""""
		if self.frameStep>1:
			return "%.0f-%.0fx%.0f" % (self.startFrame, self.endFrame, self.frameStep)
		else:
			return "%.0f-%.0f" % (self.startFrame, self.endFrame)
	@property
	#----------------------------------------------------------------------
	def frame_count(self):
		return self.endFrame - self.startFrame
#=================================================================
class Data_Access_Uitls(object):
	""""""
	defaultRenderGlobals = pm.PyNode("defaultRenderGlobals")
	_deadline_pools      = []
	_deadline_groups     = []
	frameRange           = Frame_Range()
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
	# Returns the current renderer.
	@property
	def currentRenderer(self):
		renderer = self.defaultRenderGlobals.currentRenderer.get()
		if renderer == "_3delight":
			renderer="3delight"
		return renderer
	# Returns the cpu count selected for the current render (if any).
	@property
	def cpuSetting(self):
		renderer = self.currentRenderer
		if renderer == "mayaSoftware":
			cpus= cmds.getAttr("defaultRenderGlobals.numCpusToUse")
			if cpus>0:
				return cpus
		elif renderer == "maxwell":
			cpus= cmds.getAttr("maxwellRenderOptions.numThreads")
			if cpus>0:
				return cpus
		elif renderer == "vray":
			cpus= cmds.getAttr("vraySettings.sys_max_threads")
			if cpus>0:
				return cpus
		return 0
	# Returns the current version of Maya as an integer.
	@property
	def mayaVersion(self):
		return int(cmds.about(version=True)[:4])
	# Gets the image directory for Maya.
	@property
	def imageDirectory(self):
		imageDir=""
		path = os.path.join(pm.workspace(q=1,fullName=1),pm.workspace("images",q=1,fileRuleEntry=1)).replace("\\","/")
		## The -renderType flag is obsolete in 2013 and later.
		#if self.mayaVersion<=2012:
			#fileRules=pm.workspace(q=1,renderType=1)
			## Relative path, get the project's image directory.
			#for i in range(0,len(fileRules),2):
				#if fileRules[i] == "images":
					#imageDir=fileRules[i + 1]
					#break
		#else:
			#imageDir=str(pm.workspace("images",q=1,fileRuleEntry=1))
			## Relative path, get the project's image directory.

		#path = pm.workspace(q=1,fullName=1)
		#if path[:] != "\\" and path[:] != "/":
			#path=path + "/"

		#if imageDir == "":
			#return path

		#if imageDir[:] != "\\" and imageDir[:] != "/":
			#imageDir=imageDir + "/"
			## Check for an absolute path in the image directory.

		#if imageDir[0:1] == "/" or imageDir[0:1] == "\\" or imageDir[1:2] == ":":
			#path=imageDir
		#else:
			#path=path + imageDir

		return path
	# Returns if animation is enabled.
	@property
	def IsAnimatedOn(self):
		return self.defaultRenderGlobals.animation.get()
	# Returns if motion blur is enabled.
	@property
	def IsMotionBlur(self):
		renderer= self.currentRenderer
		if renderer == "mentalRay":
			return int(pm.getAttr('miDefaultOptions.motionBlur'))
		elif renderer == "mayaHardware":
			return int(pm.getAttr('hardwareRenderGlobals.enableMotionBlur'))
		elif renderer == "mayaVector":
			return int(False)
		elif renderer == "turtle":
			return (pm.getAttr('TurtleRenderOptions.motionBlur'))
		elif renderer == "renderMan":
			return int(pm.getAttr('renderManGlobals.rman__torattr___motionBlur'))
		elif renderer == "finalRender":
			return int(pm.getAttr('defaultFinalRenderSettings.motionBlur'))
		elif renderer == "vray":
			return int(pm.getAttr('vraySettings.cam_mbOn'))
		else:
			return int(self.defaultRenderGlobals.motionBlur.get())
	# Returns global resolution.
	@property
	def globalsResolution(self):
		res = [320,240]
		renderer=self.currentRenderer
		if renderer != "vray":
			res[0]=self.defaultResolution.width.get()
			res[1]=self.defaultResolution.height.get()
		else:
			res[0]=cmds.getAttr('vraySettings.width')
			res[1]=cmds.getAttr('vraySettings.height')
		return res
	# Returns if render layers is on.
	@property
	def IsRenderLayersOn(self):
		layers=int(False)
		goodRLCounter=0
		for item in pm.ls(exactType="renderLayer"):
			if not item.isReferenced():
				if str(item) == "defaultRenderLayer":
					# This is THE defaultRenderLayer, so count it.
					goodRLCounter+=1
				elif str(item) != "defaultRenderLayer":
					# This is a user render layer, count it.
					goodRLCounter+=1
		if goodRLCounter>1:
			layers=int(True)		
		return layers
	# Returns if the renderer supports region rendering.
	@property
	def SupportsRegionRendering(self):
		renderer = self.currentRenderer
		if renderer == "arnold" or renderer == "mayaSoftware" or renderer == "mentalRay" or renderer == "renderMan" or renderer == "finalRender" or renderer == "turtle" or renderer == "vray":
			return True
		return False
	# Returns if the renderer supports the CPU option.
	@property
	def EnableCpuOption(self):
		renderer = self.currentRenderer
		if self.IsRenderLayersOn:
			return True
		elif renderer == "mayaSoftware" or renderer == "mentalRay" or renderer == "renderMan" or renderer == "finalRender" or renderer == "gelato" or renderer == "maxwell" or renderer == "vray":
			return True
		return False
	# Returns if the renderer supports half frame rendering.
	@property
	def ShowHalfFramesOption(self):
		if not self.IsRenderLayersOn:
			if self.currentRenderer == "renderman" or self.currentRenderer == "vray":
				return False
		return True
	#----------------------------------------------------------------------
	@property
	def StrippedSceneFileName(self):
		fileName = os.path.basename(cmds.file(q=1,sceneName=1))
		fileName = os.path.splitext(fileName)[0]
		return fileName
	#----------------------------------------------------------------------
	@property
	def scene_File_Path(self):
		""""""
		return pm.cmds.file(q=1,sceneName=1)
	#----------------------------------------------------------------------
	@property
	def all_Cameras(self):
		return list(set([cam.getParent() for cam in pm.ls(exactType="camera")]))
	#----------------------------------------------------------------------
	@property
	def all_Renderable_Cameras(self):
		""""""
		return list(set([cam.getParent() for cam in pm.ls(exactType="camera") if cam.renderable.get()]))
	@property
	def all_Renderable_Camera_Names(self):
		""""""
		return [cam.name() for cam in self.all_Renderable_Cameras]
	#----------------------------------------------------------------------
	@property
	def User_Temp_Directory(self):
		""""""
		tempDir = DeadLine_Access.Get_CurrentUserHomeDirectory() + "/temp"
		return tempDir.replace("\\", "/")
	#----------------------------------------------------------------------
	@property
	def currentRenderLayer(self):
		return pm.editRenderLayerGlobals(currentRenderLayer=1,query=1)
	#----------------------------------------------------------------------
	@property
	def valid_Render_Layers(self):
		res = []
		if self.IsRenderLayersOn:
			for layer in pm.ls(exactType="renderLayer"):
				if not layer.isReferenced() and layer.renderable.get():
					res.append(layer)
		else:
			if not self.currentRenderLayer.isReferenced() and self.currentRenderLayer.renderable.get():
				res.append(self.currentRenderLayer)
		return res	
	#----------------------------------------------------------------------
	@property
	def project_workspace(self):
		return str(pm.workspace(q=1,fullName=1))
	
	#----------------------------------------------------------------------
	@property
	def deadline_pools(self):
		""""""
		if not len(self.__class__._deadline_pools):
			pools = DeadLine_Access.Get_PoolNames()
			self.__class__._deadline_pools = pools
		return self.__class__._deadline_pools
	
	#----------------------------------------------------------------------
	@property
	def deadline_groups(self):
		""""""
		if not len(self.__class__._deadline_groups):
			groups = DeadLine_Access.Get_GroupNames()
			self.__class__._deadline_groups = groups
		return self.__class__._deadline_groups

Data_Access = Data_Access_Uitls()

# Creates a tile prefix from the given prefix by placing the tile part at the
# beginning of the filename. It's placed at the beginning to try and avoid as
# many conflicts as possible with Maya's prefix shortcuts.


