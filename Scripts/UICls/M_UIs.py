import maya.cmds as cmds
from functools import  partial
import Scripts.UIFns.Find_UI
import Scripts.UICls.UI_Object


########################################################################
class Window(Scripts.UICls.UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None):
		run_command = True
		if not name == None:
			if cmds.window(name, exists=True):
				run_command = False
		if run_command:
			if not name == None:
				name = cmds.window(name)
			else:
				name = cmds.window()
		super(Window, self).__init__(name)
	
	#----------------------------------------------------------------------
	def get_title(self):
		""""""
		return self.query(title=True)
	#----------------------------------------------------------------------
	def set_title(self, value):
		""""""
		self.edit(title=value)
	#----------------------------------------------------------------------
	title = property(get_title, set_title)
	#----------------------------------------------------------------------
	def get_iconName(self):
		""""""
		return self.query(iconName=True)
	#----------------------------------------------------------------------
	def set_iconName(self, value):
		""""""
		self.edit(iconName=value)
	#----------------------------------------------------------------------
	iconName = property(get_iconName, set_iconName)
	#----------------------------------------------------------------------
	def get_sizeable(self):
		""""""
		return self.query(sizeable=True)
	#----------------------------------------------------------------------
	def set_sizeable(self, value):
		""""""
		self.edit(sizeable=value)
	#----------------------------------------------------------------------
	sizeable = property(get_sizeable, set_sizeable)
	#----------------------------------------------------------------------
	def get_titleBar(self):
		""""""
		return self.query(titleBar=True)
	#----------------------------------------------------------------------
	def set_titleBar(self, value):
		""""""
		self.edit(titleBar=value)
	#----------------------------------------------------------------------
	titleBar = property(get_titleBar, set_titleBar)
	#----------------------------------------------------------------------
	def get_minimizeButton(self):
		""""""
		return self.query(minimizeButton=True)
	#----------------------------------------------------------------------
	def set_minimizeButton(self, value):
		""""""
		self.edit(minimizeButton=value)
	#----------------------------------------------------------------------
	minimizeButton = property(get_minimizeButton, set_minimizeButton)
	#----------------------------------------------------------------------
	def get_maximizeButton(self):
		""""""
		return self.query(maximizeButton=True)
	#----------------------------------------------------------------------
	def set_maximizeButton(self, value):
		""""""
		self.edit(maximizeButton=value)
	#----------------------------------------------------------------------
	maximizeButton = property(get_maximizeButton, set_maximizeButton)
	#----------------------------------------------------------------------
	@property
	def menuBar(self):
		""""""
		return self.query(menuBar=True)
	#----------------------------------------------------------------------
	def get_toolbox(self):
		""""""
		return self.query(toolbox=True)
	#----------------------------------------------------------------------
	def set_toolbox(self, value):
		""""""
		self.edit(toolbox=value)
	#----------------------------------------------------------------------
	toolbox = property(get_toolbox, set_toolbox)
	#----------------------------------------------------------------------
	def get_titleBarMenu(self):
		""""""
		return self.query(titleBarMenu=True)
	#----------------------------------------------------------------------
	def set_titleBarMenu(self, value):
		""""""
		self.edit(titleBarMenu=value)
	#----------------------------------------------------------------------
	titleBarMenu = property(get_titleBarMenu, set_titleBarMenu)
	#----------------------------------------------------------------------
	def get_menuBarVisible(self):
		""""""
		return self.query(menuBarVisible=True)
	#----------------------------------------------------------------------
	def set_menuBarVisible(self, value):
		""""""
		self.edit(menuBarVisible=value)
	#----------------------------------------------------------------------
	menuBarVisible = property(get_menuBarVisible, set_menuBarVisible)
	#----------------------------------------------------------------------
	def get_topEdge(self):
		""""""
		return self.query(topEdge=True)
	#----------------------------------------------------------------------
	def set_topEdge(self, value):
		""""""
		self.edit(topEdge=value)
	#----------------------------------------------------------------------
	topEdge = property(get_topEdge, set_topEdge)
	#----------------------------------------------------------------------
	def get_leftEdge(self):
		""""""
		return self.query(leftEdge=True)
	#----------------------------------------------------------------------
	def set_leftEdge(self, value):
		""""""
		self.edit(leftEdge=value)
	#----------------------------------------------------------------------
	leftEdge = property(get_leftEdge, set_leftEdge)
	#----------------------------------------------------------------------
	def get_topLeftCorner(self):
		""""""
		return self.query(topLeftCorner=True)
	#----------------------------------------------------------------------
	def set_topLeftCorner(self, value):
		""""""
		self.edit(topLeftCorner=value)
	#----------------------------------------------------------------------
	topLeftCorner = property(get_topLeftCorner, set_topLeftCorner)
	#----------------------------------------------------------------------
	def get_width(self):
		""""""
		return self.query(width=True)
	#----------------------------------------------------------------------
	def set_width(self, value):
		""""""
		self.edit(width=value)
	#----------------------------------------------------------------------
	width = property(get_width, set_width)
	#----------------------------------------------------------------------
	def get_height(self):
		""""""
		return self.query(height=True)
	#----------------------------------------------------------------------
	def set_height(self, value):
		""""""
		self.edit(height=value)
	#----------------------------------------------------------------------
	height = property(get_height, set_height)
	#----------------------------------------------------------------------
	def get_widthHeight(self):
		""""""
		return self.query(widthHeight=True)
	#----------------------------------------------------------------------
	def set_widthHeight(self, value):
		""""""
		self.edit(widthHeight=value)
	#----------------------------------------------------------------------
	widthHeight = property(get_widthHeight, set_widthHeight)

	#----------------------------------------------------------------------
	def get_visible(self):
		""""""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	def set_visible(self, value):
		""""""
		self.edit(visible=value)
	#----------------------------------------------------------------------
	visible = property(get_visible, set_visible)
	#----------------------------------------------------------------------
	def get_iconify(self):
		""""""
		return self.query(iconify=True)
	#----------------------------------------------------------------------
	def set_iconify(self, value):
		""""""
		self.edit(iconify=value)
	#----------------------------------------------------------------------
	iconify = property(get_iconify, set_iconify)
	#----------------------------------------------------------------------
	def get_mainWindow(self):
		""""""
		return self.query(mainWindow=True)
	#----------------------------------------------------------------------
	def set_mainWindow(self, value):
		""""""
		self.edit(mainWindow=value)
	#----------------------------------------------------------------------
	mainWindow = property(get_mainWindow, set_mainWindow)
	#----------------------------------------------------------------------
	def backgroundColor(self,value):
		""""""
		self.edig(backgroundColor=value)
	#----------------------------------------------------------------------
	def get_resizeToFitChildren(self):
		""""""
		return self.query(resizeToFitChildren=True)
	#----------------------------------------------------------------------
	def set_resizeToFitChildren(self, value):
		""""""
		self.edit(resizeToFitChildren=value)
	#----------------------------------------------------------------------
	resizeToFitChildren = property(get_resizeToFitChildren, set_resizeToFitChildren)

	#----------------------------------------------------------------------
	def minimizeCommand(self,value):
		""""""
		self.edig(minimizeCommand=value)
	#----------------------------------------------------------------------
	def restoreCommand(self,value):
		""""""
		self.edig(restoreCommand=value)
	#----------------------------------------------------------------------
	@property
	def numberOfMenus(self):
		""""""
		return self.query(numberOfMenus=True)
	#----------------------------------------------------------------------
	@property
	def menuArray(self):
		""""""
		return self.query(menuArray=True)
	#----------------------------------------------------------------------
	def menuIndex(self,value):
		""""""
		self.edig(menuIndex=value)
	#----------------------------------------------------------------------
	def get_docTag(self):
		""""""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		""""""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	@property
	def frontWindow(self):
		""""""
		return self.query(frontWindow=True)
			
		
########################################################################
class ModelEditor(Scripts.UICls.UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None):
		run_command = True
		if not name == None:
			if cmds.modelEditor(name, exists=True):
				run_command = False
		if run_command:
			if not name == None:
				name = cmds.modelEditor(name)
			else:
				name = cmds.modelEditor()
		super(ModelEditor, self).__init__(name)



	#----------------------------------------------------------------------
	@property
	def panel(self):
		""""""
		return self.query(panel=True)
	#----------------------------------------------------------------------
	def get_parent(self):
		""""""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	def set_parent(self, value):
		""""""
		self.edit(parent=value)
	#----------------------------------------------------------------------
	parent = property(get_parent, set_parent)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edig(unParent=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	def get_mainListConnection(self):
		""""""
		return self.query(mainListConnection=True)
	#----------------------------------------------------------------------
	def set_mainListConnection(self, value):
		""""""
		self.edit(mainListConnection=value)
	#----------------------------------------------------------------------
	mainListConnection = property(get_mainListConnection, set_mainListConnection)
	#----------------------------------------------------------------------
	def get_forceMainConnection(self):
		""""""
		return self.query(forceMainConnection=True)
	#----------------------------------------------------------------------
	def set_forceMainConnection(self, value):
		""""""
		self.edit(forceMainConnection=value)
	#----------------------------------------------------------------------
	forceMainConnection = property(get_forceMainConnection, set_forceMainConnection)
	#----------------------------------------------------------------------
	def get_selectionConnection(self):
		""""""
		return self.query(selectionConnection=True)
	#----------------------------------------------------------------------
	def set_selectionConnection(self, value):
		""""""
		self.edit(selectionConnection=value)
	#----------------------------------------------------------------------
	selectionConnection = property(get_selectionConnection, set_selectionConnection)
	#----------------------------------------------------------------------
	def get_highlightConnection(self):
		""""""
		return self.query(highlightConnection=True)
	#----------------------------------------------------------------------
	def set_highlightConnection(self, value):
		""""""
		self.edit(highlightConnection=value)
	#----------------------------------------------------------------------
	highlightConnection = property(get_highlightConnection, set_highlightConnection)
	#----------------------------------------------------------------------
	def get_filter(self):
		""""""
		return self.query(filter=True)
	#----------------------------------------------------------------------
	def set_filter(self, value):
		""""""
		self.edit(filter=value)
	#----------------------------------------------------------------------
	filter = property(get_filter, set_filter)
	#----------------------------------------------------------------------
	def lockMainConnection(self,value):
		""""""
		self.edig(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edig(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edig(updateMainConnection=value)
	#----------------------------------------------------------------------
	def get_docTag(self):
		""""""
		return self.query(docTag=True)
	#----------------------------------------------------------------------
	def set_docTag(self, value):
		""""""
		self.edit(docTag=value)
	#----------------------------------------------------------------------
	docTag = property(get_docTag, set_docTag)
	#----------------------------------------------------------------------
	def get_camera(self):
		""""""
		return self.query(camera=True)
	#----------------------------------------------------------------------
	def set_camera(self, value):
		""""""
		self.edit(camera=value)
	#----------------------------------------------------------------------
	camera = property(get_camera, set_camera)
	#----------------------------------------------------------------------
	def cameraName(self,value):
		""""""
		self.edig(cameraName=value)
	#----------------------------------------------------------------------
	def get_displayLights(self):
		""""""
		return self.query(displayLights=True)
	#----------------------------------------------------------------------
	def set_displayLights(self, value):
		""""""
		self.edit(displayLights=value)
	#----------------------------------------------------------------------
	displayLights = property(get_displayLights, set_displayLights)
	#----------------------------------------------------------------------
	def get_bufferMode(self):
		""""""
		return self.query(bufferMode=True)
	#----------------------------------------------------------------------
	def set_bufferMode(self, value):
		""""""
		self.edit(bufferMode=value)
	#----------------------------------------------------------------------
	bufferMode = property(get_bufferMode, set_bufferMode)
	#----------------------------------------------------------------------
	def get_activeOnly(self):
		""""""
		return self.query(activeOnly=True)
	#----------------------------------------------------------------------
	def set_activeOnly(self, value):
		""""""
		self.edit(activeOnly=value)
	#----------------------------------------------------------------------
	activeOnly = property(get_activeOnly, set_activeOnly)
	#----------------------------------------------------------------------
	def get_interactive(self):
		""""""
		return self.query(interactive=True)
	#----------------------------------------------------------------------
	def set_interactive(self, value):
		""""""
		self.edit(interactive=value)
	#----------------------------------------------------------------------
	interactive = property(get_interactive, set_interactive)
	#----------------------------------------------------------------------
	def get_default(self):
		""""""
		return self.query(default=True)
	#----------------------------------------------------------------------
	def set_default(self, value):
		""""""
		self.edit(default=value)
	#----------------------------------------------------------------------
	default = property(get_default, set_default)
	#----------------------------------------------------------------------
	def get_ignorePanZoom(self):
		""""""
		return self.query(ignorePanZoom=True)
	#----------------------------------------------------------------------
	def set_ignorePanZoom(self, value):
		""""""
		self.edit(ignorePanZoom=value)
	#----------------------------------------------------------------------
	ignorePanZoom = property(get_ignorePanZoom, set_ignorePanZoom)
	#----------------------------------------------------------------------
	def get_twoSidedLighting(self):
		""""""
		return self.query(twoSidedLighting=True)
	#----------------------------------------------------------------------
	def set_twoSidedLighting(self, value):
		""""""
		self.edit(twoSidedLighting=value)
	#----------------------------------------------------------------------
	twoSidedLighting = property(get_twoSidedLighting, set_twoSidedLighting)
	#----------------------------------------------------------------------
	def get_displayAppearance(self):
		""""""
		return self.query(displayAppearance=True)
	#----------------------------------------------------------------------
	def set_displayAppearance(self, value):
		""""""
		self.edit(displayAppearance=value)
	#----------------------------------------------------------------------
	displayAppearance = property(get_displayAppearance, set_displayAppearance)
	#----------------------------------------------------------------------
	def get_wireframeOnShaded(self):
		""""""
		return self.query(wireframeOnShaded=True)
	#----------------------------------------------------------------------
	def set_wireframeOnShaded(self, value):
		""""""
		self.edit(wireframeOnShaded=value)
	#----------------------------------------------------------------------
	wireframeOnShaded = property(get_wireframeOnShaded, set_wireframeOnShaded)
	#----------------------------------------------------------------------
	def get_headsUpDisplay(self):
		""""""
		return self.query(headsUpDisplay=True)
	#----------------------------------------------------------------------
	def set_headsUpDisplay(self, value):
		""""""
		self.edit(headsUpDisplay=value)
	#----------------------------------------------------------------------
	headsUpDisplay = property(get_headsUpDisplay, set_headsUpDisplay)
	#----------------------------------------------------------------------
	def get_selectionHiliteDisplay(self):
		""""""
		return self.query(selectionHiliteDisplay=True)
	#----------------------------------------------------------------------
	def set_selectionHiliteDisplay(self, value):
		""""""
		self.edit(selectionHiliteDisplay=value)
	#----------------------------------------------------------------------
	selectionHiliteDisplay = property(get_selectionHiliteDisplay, set_selectionHiliteDisplay)
	#----------------------------------------------------------------------
	def get_useDefaultMaterial(self):
		""""""
		return self.query(useDefaultMaterial=True)
	#----------------------------------------------------------------------
	def set_useDefaultMaterial(self, value):
		""""""
		self.edit(useDefaultMaterial=value)
	#----------------------------------------------------------------------
	useDefaultMaterial = property(get_useDefaultMaterial, set_useDefaultMaterial)
	#----------------------------------------------------------------------
	def get_useColorIndex(self):
		""""""
		return self.query(useColorIndex=True)
	#----------------------------------------------------------------------
	def set_useColorIndex(self, value):
		""""""
		self.edit(useColorIndex=value)
	#----------------------------------------------------------------------
	useColorIndex = property(get_useColorIndex, set_useColorIndex)
	#----------------------------------------------------------------------
	def get_userNode(self):
		""""""
		return self.query(userNode=True)
	#----------------------------------------------------------------------
	def set_userNode(self, value):
		""""""
		self.edit(userNode=value)
	#----------------------------------------------------------------------
	userNode = property(get_userNode, set_userNode)
	#----------------------------------------------------------------------
	def get_wireframeBackingStore(self):
		""""""
		return self.query(wireframeBackingStore=True)
	#----------------------------------------------------------------------
	def set_wireframeBackingStore(self, value):
		""""""
		self.edit(wireframeBackingStore=value)
	#----------------------------------------------------------------------
	wireframeBackingStore = property(get_wireframeBackingStore, set_wireframeBackingStore)
	#----------------------------------------------------------------------
	def get_useRGBImagePlane(self):
		""""""
		return self.query(useRGBImagePlane=True)
	#----------------------------------------------------------------------
	def set_useRGBImagePlane(self, value):
		""""""
		self.edit(useRGBImagePlane=value)
	#----------------------------------------------------------------------
	useRGBImagePlane = property(get_useRGBImagePlane, set_useRGBImagePlane)
	#----------------------------------------------------------------------
	def get_imagePlane(self):
		""""""
		return self.query(imagePlane=True)
	#----------------------------------------------------------------------
	def set_imagePlane(self, value):
		""""""
		self.edit(imagePlane=value)
	#----------------------------------------------------------------------
	imagePlane = property(get_imagePlane, set_imagePlane)
	#----------------------------------------------------------------------
	def updateColorMode(self,value):
		""""""
		self.edig(updateColorMode=value)
	#----------------------------------------------------------------------
	@property
	def colorMap(self):
		""""""
		return self.query(colorMap=True)
	#----------------------------------------------------------------------
	def get_backfaceCulling(self):
		""""""
		return self.query(backfaceCulling=True)
	#----------------------------------------------------------------------
	def set_backfaceCulling(self, value):
		""""""
		self.edit(backfaceCulling=value)
	#----------------------------------------------------------------------
	backfaceCulling = property(get_backfaceCulling, set_backfaceCulling)
	#----------------------------------------------------------------------
	def get_xray(self):
		""""""
		return self.query(xray=True)
	#----------------------------------------------------------------------
	def set_xray(self, value):
		""""""
		self.edit(xray=value)
	#----------------------------------------------------------------------
	xray = property(get_xray, set_xray)
	#----------------------------------------------------------------------
	def get_jointXray(self):
		""""""
		return self.query(jointXray=True)
	#----------------------------------------------------------------------
	def set_jointXray(self, value):
		""""""
		self.edit(jointXray=value)
	#----------------------------------------------------------------------
	jointXray = property(get_jointXray, set_jointXray)
	#----------------------------------------------------------------------
	def get_activeComponentsXray(self):
		""""""
		return self.query(activeComponentsXray=True)
	#----------------------------------------------------------------------
	def set_activeComponentsXray(self, value):
		""""""
		self.edit(activeComponentsXray=value)
	#----------------------------------------------------------------------
	activeComponentsXray = property(get_activeComponentsXray, set_activeComponentsXray)
	#----------------------------------------------------------------------
	def get_maxConstantTransparency(self):
		""""""
		return self.query(maxConstantTransparency=True)
	#----------------------------------------------------------------------
	def set_maxConstantTransparency(self, value):
		""""""
		self.edit(maxConstantTransparency=value)
	#----------------------------------------------------------------------
	maxConstantTransparency = property(get_maxConstantTransparency, set_maxConstantTransparency)
	#----------------------------------------------------------------------
	def get_displayTextures(self):
		""""""
		return self.query(displayTextures=True)
	#----------------------------------------------------------------------
	def set_displayTextures(self, value):
		""""""
		self.edit(displayTextures=value)
	#----------------------------------------------------------------------
	displayTextures = property(get_displayTextures, set_displayTextures)
	#----------------------------------------------------------------------
	def get_smoothWireframe(self):
		""""""
		return self.query(smoothWireframe=True)
	#----------------------------------------------------------------------
	def set_smoothWireframe(self, value):
		""""""
		self.edit(smoothWireframe=value)
	#----------------------------------------------------------------------
	smoothWireframe = property(get_smoothWireframe, set_smoothWireframe)
	#----------------------------------------------------------------------
	def get_lineWidth(self):
		""""""
		return self.query(lineWidth=True)
	#----------------------------------------------------------------------
	def set_lineWidth(self, value):
		""""""
		self.edit(lineWidth=value)
	#----------------------------------------------------------------------
	lineWidth = property(get_lineWidth, set_lineWidth)
	#----------------------------------------------------------------------
	def get_textureMaxSize(self):
		""""""
		return self.query(textureMaxSize=True)
	#----------------------------------------------------------------------
	def set_textureMaxSize(self, value):
		""""""
		self.edit(textureMaxSize=value)
	#----------------------------------------------------------------------
	textureMaxSize = property(get_textureMaxSize, set_textureMaxSize)
	#----------------------------------------------------------------------
	@property
	def textureMemoryUsed(self):
		""""""
		return self.query(textureMemoryUsed=True)
	#----------------------------------------------------------------------
	def get_textureAnisotropic(self):
		""""""
		return self.query(textureAnisotropic=True)
	#----------------------------------------------------------------------
	def set_textureAnisotropic(self, value):
		""""""
		self.edit(textureAnisotropic=value)
	#----------------------------------------------------------------------
	textureAnisotropic = property(get_textureAnisotropic, set_textureAnisotropic)
	#----------------------------------------------------------------------
	def get_textureSampling(self):
		""""""
		return self.query(textureSampling=True)
	#----------------------------------------------------------------------
	def set_textureSampling(self, value):
		""""""
		self.edit(textureSampling=value)
	#----------------------------------------------------------------------
	textureSampling = property(get_textureSampling, set_textureSampling)
	#----------------------------------------------------------------------
	def get_textureDisplay(self):
		""""""
		return self.query(textureDisplay=True)
	#----------------------------------------------------------------------
	def set_textureDisplay(self, value):
		""""""
		self.edit(textureDisplay=value)
	#----------------------------------------------------------------------
	textureDisplay = property(get_textureDisplay, set_textureDisplay)
	#----------------------------------------------------------------------
	def get_textureHilight(self):
		""""""
		return self.query(textureHilight=True)
	#----------------------------------------------------------------------
	def set_textureHilight(self, value):
		""""""
		self.edit(textureHilight=value)
	#----------------------------------------------------------------------
	textureHilight = property(get_textureHilight, set_textureHilight)
	#----------------------------------------------------------------------
	def get_fogging(self):
		""""""
		return self.query(fogging=True)
	#----------------------------------------------------------------------
	def set_fogging(self, value):
		""""""
		self.edit(fogging=value)
	#----------------------------------------------------------------------
	fogging = property(get_fogging, set_fogging)
	#----------------------------------------------------------------------
	def get_fogSource(self):
		""""""
		return self.query(fogSource=True)
	#----------------------------------------------------------------------
	def set_fogSource(self, value):
		""""""
		self.edit(fogSource=value)
	#----------------------------------------------------------------------
	fogSource = property(get_fogSource, set_fogSource)
	#----------------------------------------------------------------------
	def get_fogMode(self):
		""""""
		return self.query(fogMode=True)
	#----------------------------------------------------------------------
	def set_fogMode(self, value):
		""""""
		self.edit(fogMode=value)
	#----------------------------------------------------------------------
	fogMode = property(get_fogMode, set_fogMode)
	#----------------------------------------------------------------------
	def get_fogDensity(self):
		""""""
		return self.query(fogDensity=True)
	#----------------------------------------------------------------------
	def set_fogDensity(self, value):
		""""""
		self.edit(fogDensity=value)
	#----------------------------------------------------------------------
	fogDensity = property(get_fogDensity, set_fogDensity)
	#----------------------------------------------------------------------
	def get_fogEnd(self):
		""""""
		return self.query(fogEnd=True)
	#----------------------------------------------------------------------
	def set_fogEnd(self, value):
		""""""
		self.edit(fogEnd=value)
	#----------------------------------------------------------------------
	fogEnd = property(get_fogEnd, set_fogEnd)
	#----------------------------------------------------------------------
	def get_fogStart(self):
		""""""
		return self.query(fogStart=True)
	#----------------------------------------------------------------------
	def set_fogStart(self, value):
		""""""
		self.edit(fogStart=value)
	#----------------------------------------------------------------------
	fogStart = property(get_fogStart, set_fogStart)
	#----------------------------------------------------------------------
	def get_fogColor(self):
		""""""
		return self.query(fogColor=True)
	#----------------------------------------------------------------------
	def set_fogColor(self, value):
		""""""
		self.edit(fogColor=value)
	#----------------------------------------------------------------------
	fogColor = property(get_fogColor, set_fogColor)
	#----------------------------------------------------------------------
	def get_shadows(self):
		""""""
		return self.query(shadows=True)
	#----------------------------------------------------------------------
	def set_shadows(self, value):
		""""""
		self.edit(shadows=value)
	#----------------------------------------------------------------------
	shadows = property(get_shadows, set_shadows)
	#----------------------------------------------------------------------
	def get_rendererName(self):
		""""""
		return self.query(rendererName=True)
	#----------------------------------------------------------------------
	def set_rendererName(self, value):
		""""""
		self.edit(rendererName=value)
	#----------------------------------------------------------------------
	rendererName = property(get_rendererName, set_rendererName)
	#----------------------------------------------------------------------
	@property
	def rendererDeviceName(self):
		""""""
		return self.query(rendererDeviceName=True)
	#----------------------------------------------------------------------
	@property
	def rendererList(self):
		""""""
		return self.query(rendererList=True)
	#----------------------------------------------------------------------
	@property
	def rendererListUI(self):
		""""""
		return self.query(rendererListUI=True)
	#----------------------------------------------------------------------
	def get_rendererOverrideName(self):
		""""""
		return self.query(rendererOverrideName=True)
	#----------------------------------------------------------------------
	def set_rendererOverrideName(self, value):
		""""""
		self.edit(rendererOverrideName=value)
	#----------------------------------------------------------------------
	rendererOverrideName = property(get_rendererOverrideName, set_rendererOverrideName)
	#----------------------------------------------------------------------
	@property
	def rendererOverrideList(self):
		""""""
		return self.query(rendererOverrideList=True)
	#----------------------------------------------------------------------
	@property
	def rendererOverrideListUI(self):
		""""""
		return self.query(rendererOverrideListUI=True)
	#----------------------------------------------------------------------
	def get_colorResolution(self):
		""""""
		return self.query(colorResolution=True)
	#----------------------------------------------------------------------
	def set_colorResolution(self, value):
		""""""
		self.edit(colorResolution=value)
	#----------------------------------------------------------------------
	colorResolution = property(get_colorResolution, set_colorResolution)
	#----------------------------------------------------------------------
	def get_bumpResolution(self):
		""""""
		return self.query(bumpResolution=True)
	#----------------------------------------------------------------------
	def set_bumpResolution(self, value):
		""""""
		self.edit(bumpResolution=value)
	#----------------------------------------------------------------------
	bumpResolution = property(get_bumpResolution, set_bumpResolution)
	#----------------------------------------------------------------------
	def get_transparencyAlgorithm(self):
		""""""
		return self.query(transparencyAlgorithm=True)
	#----------------------------------------------------------------------
	def set_transparencyAlgorithm(self, value):
		""""""
		self.edit(transparencyAlgorithm=value)
	#----------------------------------------------------------------------
	transparencyAlgorithm = property(get_transparencyAlgorithm, set_transparencyAlgorithm)
	#----------------------------------------------------------------------
	def get_transpInShadows(self):
		""""""
		return self.query(transpInShadows=True)
	#----------------------------------------------------------------------
	def set_transpInShadows(self, value):
		""""""
		self.edit(transpInShadows=value)
	#----------------------------------------------------------------------
	transpInShadows = property(get_transpInShadows, set_transpInShadows)
	#----------------------------------------------------------------------
	def get_cullingOverride(self):
		""""""
		return self.query(cullingOverride=True)
	#----------------------------------------------------------------------
	def set_cullingOverride(self, value):
		""""""
		self.edit(cullingOverride=value)
	#----------------------------------------------------------------------
	cullingOverride = property(get_cullingOverride, set_cullingOverride)
	#----------------------------------------------------------------------
	def get_lowQualityLighting(self):
		""""""
		return self.query(lowQualityLighting=True)
	#----------------------------------------------------------------------
	def set_lowQualityLighting(self, value):
		""""""
		self.edit(lowQualityLighting=value)
	#----------------------------------------------------------------------
	lowQualityLighting = property(get_lowQualityLighting, set_lowQualityLighting)
	#----------------------------------------------------------------------
	def get_occlusionCulling(self):
		""""""
		return self.query(occlusionCulling=True)
	#----------------------------------------------------------------------
	def set_occlusionCulling(self, value):
		""""""
		self.edit(occlusionCulling=value)
	#----------------------------------------------------------------------
	occlusionCulling = property(get_occlusionCulling, set_occlusionCulling)
	#----------------------------------------------------------------------
	def get_useBaseRenderer(self):
		""""""
		return self.query(useBaseRenderer=True)
	#----------------------------------------------------------------------
	def set_useBaseRenderer(self, value):
		""""""
		self.edit(useBaseRenderer=value)
	#----------------------------------------------------------------------
	useBaseRenderer = property(get_useBaseRenderer, set_useBaseRenderer)
	#----------------------------------------------------------------------
	def get_nurbsCurves(self):
		""""""
		return self.query(nurbsCurves=True)
	#----------------------------------------------------------------------
	def set_nurbsCurves(self, value):
		""""""
		self.edit(nurbsCurves=value)
	#----------------------------------------------------------------------
	nurbsCurves = property(get_nurbsCurves, set_nurbsCurves)
	#----------------------------------------------------------------------
	def get_nurbsSurfaces(self):
		""""""
		return self.query(nurbsSurfaces=True)
	#----------------------------------------------------------------------
	def set_nurbsSurfaces(self, value):
		""""""
		self.edit(nurbsSurfaces=value)
	#----------------------------------------------------------------------
	nurbsSurfaces = property(get_nurbsSurfaces, set_nurbsSurfaces)
	#----------------------------------------------------------------------
	def get_polymeshes(self):
		""""""
		return self.query(polymeshes=True)
	#----------------------------------------------------------------------
	def set_polymeshes(self, value):
		""""""
		self.edit(polymeshes=value)
	#----------------------------------------------------------------------
	polymeshes = property(get_polymeshes, set_polymeshes)
	#----------------------------------------------------------------------
	def get_subdivSurfaces(self):
		""""""
		return self.query(subdivSurfaces=True)
	#----------------------------------------------------------------------
	def set_subdivSurfaces(self, value):
		""""""
		self.edit(subdivSurfaces=value)
	#----------------------------------------------------------------------
	subdivSurfaces = property(get_subdivSurfaces, set_subdivSurfaces)
	#----------------------------------------------------------------------
	def get_planes(self):
		""""""
		return self.query(planes=True)
	#----------------------------------------------------------------------
	def set_planes(self, value):
		""""""
		self.edit(planes=value)
	#----------------------------------------------------------------------
	planes = property(get_planes, set_planes)
	#----------------------------------------------------------------------
	def get_lights(self):
		""""""
		return self.query(lights=True)
	#----------------------------------------------------------------------
	def set_lights(self, value):
		""""""
		self.edit(lights=value)
	#----------------------------------------------------------------------
	lights = property(get_lights, set_lights)
	#----------------------------------------------------------------------
	def get_cameras(self):
		""""""
		return self.query(cameras=True)
	#----------------------------------------------------------------------
	def set_cameras(self, value):
		""""""
		self.edit(cameras=value)
	#----------------------------------------------------------------------
	cameras = property(get_cameras, set_cameras)
	#----------------------------------------------------------------------
	def get_controlVertices(self):
		""""""
		return self.query(controlVertices=True)
	#----------------------------------------------------------------------
	def set_controlVertices(self, value):
		""""""
		self.edit(controlVertices=value)
	#----------------------------------------------------------------------
	controlVertices = property(get_controlVertices, set_controlVertices)
	#----------------------------------------------------------------------
	def get_grid(self):
		""""""
		return self.query(grid=True)
	#----------------------------------------------------------------------
	def set_grid(self, value):
		""""""
		self.edit(grid=value)
	#----------------------------------------------------------------------
	grid = property(get_grid, set_grid)
	#----------------------------------------------------------------------
	def get_hulls(self):
		""""""
		return self.query(hulls=True)
	#----------------------------------------------------------------------
	def set_hulls(self, value):
		""""""
		self.edit(hulls=value)
	#----------------------------------------------------------------------
	hulls = property(get_hulls, set_hulls)
	#----------------------------------------------------------------------
	def get_joints(self):
		""""""
		return self.query(joints=True)
	#----------------------------------------------------------------------
	def set_joints(self, value):
		""""""
		self.edit(joints=value)
	#----------------------------------------------------------------------
	joints = property(get_joints, set_joints)
	#----------------------------------------------------------------------
	def get_ikHandles(self):
		""""""
		return self.query(ikHandles=True)
	#----------------------------------------------------------------------
	def set_ikHandles(self, value):
		""""""
		self.edit(ikHandles=value)
	#----------------------------------------------------------------------
	ikHandles = property(get_ikHandles, set_ikHandles)
	#----------------------------------------------------------------------
	def get_deformers(self):
		""""""
		return self.query(deformers=True)
	#----------------------------------------------------------------------
	def set_deformers(self, value):
		""""""
		self.edit(deformers=value)
	#----------------------------------------------------------------------
	deformers = property(get_deformers, set_deformers)
	#----------------------------------------------------------------------
	def get_dynamics(self):
		""""""
		return self.query(dynamics=True)
	#----------------------------------------------------------------------
	def set_dynamics(self, value):
		""""""
		self.edit(dynamics=value)
	#----------------------------------------------------------------------
	dynamics = property(get_dynamics, set_dynamics)
	#----------------------------------------------------------------------
	def get_fluids(self):
		""""""
		return self.query(fluids=True)
	#----------------------------------------------------------------------
	def set_fluids(self, value):
		""""""
		self.edit(fluids=value)
	#----------------------------------------------------------------------
	fluids = property(get_fluids, set_fluids)
	#----------------------------------------------------------------------
	def get_hairSystems(self):
		""""""
		return self.query(hairSystems=True)
	#----------------------------------------------------------------------
	def set_hairSystems(self, value):
		""""""
		self.edit(hairSystems=value)
	#----------------------------------------------------------------------
	hairSystems = property(get_hairSystems, set_hairSystems)
	#----------------------------------------------------------------------
	def get_follicles(self):
		""""""
		return self.query(follicles=True)
	#----------------------------------------------------------------------
	def set_follicles(self, value):
		""""""
		self.edit(follicles=value)
	#----------------------------------------------------------------------
	follicles = property(get_follicles, set_follicles)
	#----------------------------------------------------------------------
	def get_nCloths(self):
		""""""
		return self.query(nCloths=True)
	#----------------------------------------------------------------------
	def set_nCloths(self, value):
		""""""
		self.edit(nCloths=value)
	#----------------------------------------------------------------------
	nCloths = property(get_nCloths, set_nCloths)
	#----------------------------------------------------------------------
	def get_nParticles(self):
		""""""
		return self.query(nParticles=True)
	#----------------------------------------------------------------------
	def set_nParticles(self, value):
		""""""
		self.edit(nParticles=value)
	#----------------------------------------------------------------------
	nParticles = property(get_nParticles, set_nParticles)
	#----------------------------------------------------------------------
	def get_nRigids(self):
		""""""
		return self.query(nRigids=True)
	#----------------------------------------------------------------------
	def set_nRigids(self, value):
		""""""
		self.edit(nRigids=value)
	#----------------------------------------------------------------------
	nRigids = property(get_nRigids, set_nRigids)
	#----------------------------------------------------------------------
	def get_dynamicConstraints(self):
		""""""
		return self.query(dynamicConstraints=True)
	#----------------------------------------------------------------------
	def set_dynamicConstraints(self, value):
		""""""
		self.edit(dynamicConstraints=value)
	#----------------------------------------------------------------------
	dynamicConstraints = property(get_dynamicConstraints, set_dynamicConstraints)
	#----------------------------------------------------------------------
	def get_locators(self):
		""""""
		return self.query(locators=True)
	#----------------------------------------------------------------------
	def set_locators(self, value):
		""""""
		self.edit(locators=value)
	#----------------------------------------------------------------------
	locators = property(get_locators, set_locators)
	#----------------------------------------------------------------------
	def get_manipulators(self):
		""""""
		return self.query(manipulators=True)
	#----------------------------------------------------------------------
	def set_manipulators(self, value):
		""""""
		self.edit(manipulators=value)
	#----------------------------------------------------------------------
	manipulators = property(get_manipulators, set_manipulators)
	#----------------------------------------------------------------------
	def get_dimensions(self):
		""""""
		return self.query(dimensions=True)
	#----------------------------------------------------------------------
	def set_dimensions(self, value):
		""""""
		self.edit(dimensions=value)
	#----------------------------------------------------------------------
	dimensions = property(get_dimensions, set_dimensions)
	#----------------------------------------------------------------------
	def get_handles(self):
		""""""
		return self.query(handles=True)
	#----------------------------------------------------------------------
	def set_handles(self, value):
		""""""
		self.edit(handles=value)
	#----------------------------------------------------------------------
	handles = property(get_handles, set_handles)
	#----------------------------------------------------------------------
	def get_pivots(self):
		""""""
		return self.query(pivots=True)
	#----------------------------------------------------------------------
	def set_pivots(self, value):
		""""""
		self.edit(pivots=value)
	#----------------------------------------------------------------------
	pivots = property(get_pivots, set_pivots)
	#----------------------------------------------------------------------
	def get_textures(self):
		""""""
		return self.query(textures=True)
	#----------------------------------------------------------------------
	def set_textures(self, value):
		""""""
		self.edit(textures=value)
	#----------------------------------------------------------------------
	textures = property(get_textures, set_textures)
	#----------------------------------------------------------------------
	def get_strokes(self):
		""""""
		return self.query(strokes=True)
	#----------------------------------------------------------------------
	def set_strokes(self, value):
		""""""
		self.edit(strokes=value)
	#----------------------------------------------------------------------
	strokes = property(get_strokes, set_strokes)
	#----------------------------------------------------------------------
	def pluginObjects(self,value):
		""""""
		self.edig(pluginObjects=value)
	#----------------------------------------------------------------------
	@property
	def queryPluginObjects(self):
		""""""
		return self.query(queryPluginObjects=True)
	#----------------------------------------------------------------------
	def get_allObjects(self):
		""""""
		return self.query(allObjects=True)
	#----------------------------------------------------------------------
	def set_allObjects(self, value):
		""""""
		self.edit(allObjects=value)
	#----------------------------------------------------------------------
	allObjects = property(get_allObjects, set_allObjects)
	#----------------------------------------------------------------------
	def get_useInteractiveMode(self):
		""""""
		return self.query(useInteractiveMode=True)
	#----------------------------------------------------------------------
	def set_useInteractiveMode(self, value):
		""""""
		self.edit(useInteractiveMode=value)
	#----------------------------------------------------------------------
	useInteractiveMode = property(get_useInteractiveMode, set_useInteractiveMode)
	#----------------------------------------------------------------------
	def get_activeView(self):
		""""""
		return self.query(activeView=True)
	#----------------------------------------------------------------------
	def set_activeView(self, value):
		""""""
		self.edit(activeView=value)
	#----------------------------------------------------------------------
	activeView = property(get_activeView, set_activeView)
	#----------------------------------------------------------------------
	def get_sortTransparent(self):
		""""""
		return self.query(sortTransparent=True)
	#----------------------------------------------------------------------
	def set_sortTransparent(self, value):
		""""""
		self.edit(sortTransparent=value)
	#----------------------------------------------------------------------
	sortTransparent = property(get_sortTransparent, set_sortTransparent)
	#----------------------------------------------------------------------
	def get_viewSelected(self):
		""""""
		return self.query(viewSelected=True)
	#----------------------------------------------------------------------
	def set_viewSelected(self, value):
		""""""
		self.edit(viewSelected=value)
	#----------------------------------------------------------------------
	viewSelected = property(get_viewSelected, set_viewSelected)
	#----------------------------------------------------------------------
	def setSelected(self,value):
		""""""
		self.edig(setSelected=value)
	#----------------------------------------------------------------------
	def addSelected(self,value):
		""""""
		self.edig(addSelected=value)
	#----------------------------------------------------------------------
	def removeSelected(self,value):
		""""""
		self.edig(removeSelected=value)
	#----------------------------------------------------------------------
	def addObjects(self,value):
		""""""
		self.edig(addObjects=value)
	#----------------------------------------------------------------------
	@property
	def viewObjects(self):
		""""""
		return self.query(viewObjects=True)
	#----------------------------------------------------------------------
	def noUndo(self,value):
		""""""
		self.edig(noUndo=value)
	#----------------------------------------------------------------------
	@property
	def cameraSetup(self):
		""""""
		return self.query(cameraSetup=True)
	#----------------------------------------------------------------------
	def get_editorChanged(self):
		""""""
		return self.query(editorChanged=True)
	#----------------------------------------------------------------------
	def set_editorChanged(self, value):
		""""""
		self.edit(editorChanged=value)
	#----------------------------------------------------------------------
	editorChanged = property(get_editorChanged, set_editorChanged)
	#----------------------------------------------------------------------
	def get_objectFilter(self):
		""""""
		return self.query(objectFilter=True)
	#----------------------------------------------------------------------
	def set_objectFilter(self, value):
		""""""
		self.edit(objectFilter=value)
	#----------------------------------------------------------------------
	objectFilter = property(get_objectFilter, set_objectFilter)
	#----------------------------------------------------------------------
	@property
	def objectFilterUI(self):
		""""""
		return self.query(objectFilterUI=True)
	#----------------------------------------------------------------------
	@property
	def objectFilterList(self):
		""""""
		return self.query(objectFilterList=True)
	#----------------------------------------------------------------------
	@property
	def objectFilterListUI(self):
		""""""
		return self.query(objectFilterListUI=True)
	#----------------------------------------------------------------------
	def get_objectFilterShowInHUD(self):
		""""""
		return self.query(objectFilterShowInHUD=True)
	#----------------------------------------------------------------------
	def set_objectFilterShowInHUD(self, value):
		""""""
		self.edit(objectFilterShowInHUD=value)
	#----------------------------------------------------------------------
	objectFilterShowInHUD = property(get_objectFilterShowInHUD, set_objectFilterShowInHUD)
	#----------------------------------------------------------------------
	@property
	def isFiltered(self):
		""""""
		return self.query(isFiltered=True)
	#----------------------------------------------------------------------
	@property
	def filteredObjectList(self):
		""""""
		return self.query(filteredObjectList=True)

	#----------------------------------------------------------------------
	@property
	def viewType(self):
		""""""
		return self.query(viewType=True)
