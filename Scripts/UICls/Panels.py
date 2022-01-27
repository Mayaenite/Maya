__all__ = ["Panel", "ComponentEditor", "HardwareRenderPanel", "HyperGraph", "HyperPanel", "HyperShade", "ModelEditor", "ModelPanel", "NodeEditor", "OutlinerEditor", "PanelConfiguration", "PanelHistory", "ScriptedPanel", "Visor"]
import maya.cmds as cmds
from . import UI_Object

########################################################################
class ComponentEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.componentEditor(**kwargs)
			super(ComponentEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.componentEditor(name, exists=True):
				super(ComponentEditor, self).__init__(name)
			else:
				name = cmds.componentEditor(name, **kwargs)
				super(ComponentEditor, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(unParent=value)
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
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edit(updateMainConnection=value)
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
	def get_lockInput(self):
		""""""
		return self.query(lockInput=True)
	#----------------------------------------------------------------------
	def set_lockInput(self, value):
		""""""
		self.edit(lockInput=value)
	#----------------------------------------------------------------------
	lockInput = property(get_lockInput, set_lockInput)
	#----------------------------------------------------------------------
	def get_precision(self):
		""""""
		return self.query(precision=True)
	#----------------------------------------------------------------------
	def set_precision(self, value):
		""""""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	precision = property(get_precision, set_precision)
	#----------------------------------------------------------------------
	def setOperationLabel(self,value):
		""""""
		self.edit(setOperationLabel=value)
	#----------------------------------------------------------------------
	@property
	def operationLabels(self):
		""""""
		return self.query(operationLabels=True)
	#----------------------------------------------------------------------
	@property
	def operationCount(self):
		""""""
		return self.query(operationCount=True)
	#----------------------------------------------------------------------
	def get_operationType(self):
		""""""
		return self.query(operationType=True)
	#----------------------------------------------------------------------
	def set_operationType(self, value):
		""""""
		self.edit(operationType=value)
	#----------------------------------------------------------------------
	operationType = property(get_operationType, set_operationType)
	#----------------------------------------------------------------------
	def get_hideZeroColumns(self):
		""""""
		return self.query(hideZeroColumns=True)
	#----------------------------------------------------------------------
	def set_hideZeroColumns(self, value):
		""""""
		self.edit(hideZeroColumns=value)
	#----------------------------------------------------------------------
	hideZeroColumns = property(get_hideZeroColumns, set_hideZeroColumns)
	#----------------------------------------------------------------------
	def get_sortAlpha(self):
		""""""
		return self.query(sortAlpha=True)
	#----------------------------------------------------------------------
	def set_sortAlpha(self, value):
		""""""
		self.edit(sortAlpha=value)
	#----------------------------------------------------------------------
	sortAlpha = property(get_sortAlpha, set_sortAlpha)
	#----------------------------------------------------------------------
	def showSelected(self,value):
		""""""
		self.edit(showSelected=value)
	#----------------------------------------------------------------------
	def get_floatSlider(self):
		""""""
		return self.query(floatSlider=True)
	#----------------------------------------------------------------------
	def set_floatSlider(self, value):
		""""""
		self.edit(floatSlider=value)
	#----------------------------------------------------------------------
	floatSlider = property(get_floatSlider, set_floatSlider)
	#----------------------------------------------------------------------
	def get_floatField(self):
		""""""
		return self.query(floatField=True)
	#----------------------------------------------------------------------
	def set_floatField(self, value):
		""""""
		self.edit(floatField=value)
	#----------------------------------------------------------------------
	floatField = property(get_floatField, set_floatField)
	#----------------------------------------------------------------------
	def get_hidePathName(self):
		""""""
		return self.query(hidePathName=True)
	#----------------------------------------------------------------------
	def set_hidePathName(self, value):
		""""""
		self.edit(hidePathName=value)
	#----------------------------------------------------------------------
	hidePathName = property(get_hidePathName, set_hidePathName)
	#----------------------------------------------------------------------
	def newTab(self,value):
		""""""
		self.edit(newTab=value)
	#----------------------------------------------------------------------
	def removeTab(self,value):
		""""""
		self.edit(removeTab=value)
	#----------------------------------------------------------------------
	@property
	def selected(self):
		""""""
		return self.query(selected=True)
########################################################################
class GetPanel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.getPanel(**kwargs)
			super(GetPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.getPanel(name, exists=True):
				super(GetPanel, self).__init__(name)
			else:
				name = cmds.getPanel(name, **kwargs)
				super(GetPanel, self).__init__(name, **dict(qtParent=parent))
########################################################################
class HardwareRenderPanel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hardwareRenderPanel(**kwargs)
			super(HardwareRenderPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hardwareRenderPanel(name, exists=True):
				super(HardwareRenderPanel, self).__init__(name)
			else:
				name = cmds.hardwareRenderPanel(name, **kwargs)
				super(HardwareRenderPanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def init(self,value):
		""""""
		self.edit(init=value)
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def copy(self,value):
		""""""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		""""""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		""""""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		""""""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		""""""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		""""""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
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
	def get_needsInit(self):
		""""""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		""""""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
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
	def glRenderEditor(self):
		""""""
		return self.query(glRenderEditor=True)
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
########################################################################
class HyperGraph(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hyperGraph(**kwargs)
			super(HyperGraph, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hyperGraph(name, exists=True):
				super(HyperGraph, self).__init__(name)
			else:
				name = cmds.hyperGraph(name, **kwargs)
				super(HyperGraph, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(unParent=value)
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
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edit(updateMainConnection=value)
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
	def addBookmark(self,value):
		""""""
		self.edit(addBookmark=value)
	#----------------------------------------------------------------------
	def addDependNode(self,value):
		""""""
		self.edit(addDependNode=value)
	#----------------------------------------------------------------------
	def addDependGraph(self,value):
		""""""
		self.edit(addDependGraph=value)
	#----------------------------------------------------------------------
	def get_animateTransition(self):
		""""""
		return self.query(animateTransition=True)
	#----------------------------------------------------------------------
	def set_animateTransition(self, value):
		""""""
		self.edit(animateTransition=value)
	#----------------------------------------------------------------------
	animateTransition = property(get_animateTransition, set_animateTransition)
	#----------------------------------------------------------------------
	def attributeEditor(self,value):
		""""""
		self.edit(attributeEditor=value)
	#----------------------------------------------------------------------
	@property
	def bookmarkName(self):
		""""""
		return self.query(bookmarkName=True)
	#----------------------------------------------------------------------
	def connectionDrawStyle(self,value):
		""""""
		self.edit(connectionDrawStyle=value)
	#----------------------------------------------------------------------
	def clear(self,value):
		""""""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def collapseContainer(self,value):
		""""""
		self.edit(collapseContainer=value)
	#----------------------------------------------------------------------
	def deleteBookmark(self,value):
		""""""
		self.edit(deleteBookmark=value)
	#----------------------------------------------------------------------
	def dependGraph(self,value):
		""""""
		self.edit(dependGraph=value)
	#----------------------------------------------------------------------
	def dependNode(self,value):
		""""""
		self.edit(dependNode=value)
	#----------------------------------------------------------------------
	@property
	def dropNode(self):
		""""""
		return self.query(dropNode=True)
	#----------------------------------------------------------------------
	@property
	def dropTargetNode(self):
		""""""
		return self.query(dropTargetNode=True)
	#----------------------------------------------------------------------
	def dragAndDropBehaviorCommand(self,value):
		""""""
		self.edit(dragAndDropBehaviorCommand=value)
	#----------------------------------------------------------------------
	def edgeDblClickCommand(self,value):
		""""""
		self.edit(edgeDblClickCommand=value)
	#----------------------------------------------------------------------
	def edgeDimmedDblClickCommand(self,value):
		""""""
		self.edit(edgeDimmedDblClickCommand=value)
	#----------------------------------------------------------------------
	def enableAutomaticLayout(self,value):
		""""""
		self.edit(enableAutomaticLayout=value)
	#----------------------------------------------------------------------
	def expandContainer(self,value):
		""""""
		self.edit(expandContainer=value)
	#----------------------------------------------------------------------
	@property
	def fromAttr(self):
		""""""
		return self.query(fromAttr=True)
	#----------------------------------------------------------------------
	@property
	def feedbackGadget(self):
		""""""
		return self.query(feedbackGadget=True)
	#----------------------------------------------------------------------
	@property
	def feedbackNode(self):
		""""""
		return self.query(feedbackNode=True)
	#----------------------------------------------------------------------
	def focusCommand(self,value):
		""""""
		self.edit(focusCommand=value)
	#----------------------------------------------------------------------
	def filterDetail(self,value):
		""""""
		self.edit(filterDetail=value)
	#----------------------------------------------------------------------
	def fold(self,value):
		""""""
		self.edit(fold=value)
	#----------------------------------------------------------------------
	def forceRefresh(self,value):
		""""""
		self.edit(forceRefresh=value)
	#----------------------------------------------------------------------
	def frame(self,value):
		""""""
		self.edit(frame=value)
	#----------------------------------------------------------------------
	def frameBranch(self,value):
		""""""
		self.edit(frameBranch=value)
	#----------------------------------------------------------------------
	def frameGraph(self,value):
		""""""
		self.edit(frameGraph=value)
	#----------------------------------------------------------------------
	def frameHierarchy(self,value):
		""""""
		self.edit(frameHierarchy=value)
	#----------------------------------------------------------------------
	def get_graphLayoutStyle(self):
		""""""
		return self.query(graphLayoutStyle=True)
	#----------------------------------------------------------------------
	def set_graphLayoutStyle(self, value):
		""""""
		self.edit(graphLayoutStyle=value)
	#----------------------------------------------------------------------
	graphLayoutStyle = property(get_graphLayoutStyle, set_graphLayoutStyle)
	#----------------------------------------------------------------------
	@property
	def getNodeList(self):
		""""""
		return self.query(getNodeList=True)
	#----------------------------------------------------------------------
	@property
	def getNodePosition(self):
		""""""
		return self.query(getNodePosition=True)
	#----------------------------------------------------------------------
	@property
	def graphType(self):
		""""""
		return self.query(graphType=True)
	#----------------------------------------------------------------------
	def get_iconSize(self):
		""""""
		return self.query(iconSize=True)
	#----------------------------------------------------------------------
	def set_iconSize(self, value):
		""""""
		self.edit(iconSize=value)
	#----------------------------------------------------------------------
	iconSize = property(get_iconSize, set_iconSize)
	#----------------------------------------------------------------------
	def get_viewOption(self):
		""""""
		return self.query(viewOption=True)
	#----------------------------------------------------------------------
	def set_viewOption(self, value):
		""""""
		self.edit(viewOption=value)
	#----------------------------------------------------------------------
	viewOption = property(get_viewOption, set_viewOption)
	#----------------------------------------------------------------------
	@property
	def isHotkeyTarget(self):
		""""""
		return self.query(isHotkeyTarget=True)
	#----------------------------------------------------------------------
	def get_image(self):
		""""""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		""""""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	def get_imageEnabled(self):
		""""""
		return self.query(imageEnabled=True)
	#----------------------------------------------------------------------
	def set_imageEnabled(self, value):
		""""""
		self.edit(imageEnabled=value)
	#----------------------------------------------------------------------
	imageEnabled = property(get_imageEnabled, set_imageEnabled)
	#----------------------------------------------------------------------
	def get_imagePosition(self):
		""""""
		return self.query(imagePosition=True)
	#----------------------------------------------------------------------
	def set_imagePosition(self, value):
		""""""
		self.edit(imagePosition=value)
	#----------------------------------------------------------------------
	imagePosition = property(get_imagePosition, set_imagePosition)
	#----------------------------------------------------------------------
	def get_imageScale(self):
		""""""
		return self.query(imageScale=True)
	#----------------------------------------------------------------------
	def set_imageScale(self, value):
		""""""
		self.edit(imageScale=value)
	#----------------------------------------------------------------------
	imageScale = property(get_imageScale, set_imageScale)
	#----------------------------------------------------------------------
	def get_imageForContainer(self):
		""""""
		return self.query(imageForContainer=True)
	#----------------------------------------------------------------------
	def set_imageForContainer(self, value):
		""""""
		self.edit(imageForContainer=value)
	#----------------------------------------------------------------------
	imageForContainer = property(get_imageForContainer, set_imageForContainer)
	#----------------------------------------------------------------------
	def layout(self,value):
		""""""
		self.edit(layout=value)
	#----------------------------------------------------------------------
	def layoutSelected(self,value):
		""""""
		self.edit(layoutSelected=value)
	#----------------------------------------------------------------------
	def look(self,value):
		""""""
		self.edit(look=value)
	#----------------------------------------------------------------------
	def down(self,value):
		""""""
		self.edit(down=value)
	#----------------------------------------------------------------------
	def get_mergeConnections(self):
		""""""
		return self.query(mergeConnections=True)
	#----------------------------------------------------------------------
	def set_mergeConnections(self, value):
		""""""
		self.edit(mergeConnections=value)
	#----------------------------------------------------------------------
	mergeConnections = property(get_mergeConnections, set_mergeConnections)
	#----------------------------------------------------------------------
	def navigateHome(self,value):
		""""""
		self.edit(navigateHome=value)
	#----------------------------------------------------------------------
	def nodeDropCommand(self,value):
		""""""
		self.edit(nodeDropCommand=value)
	#----------------------------------------------------------------------
	def nodePressCommand(self,value):
		""""""
		self.edit(nodePressCommand=value)
	#----------------------------------------------------------------------
	def nodeReleaseCommand(self,value):
		""""""
		self.edit(nodeReleaseCommand=value)
	#----------------------------------------------------------------------
	def nextView(self,value):
		""""""
		self.edit(nextView=value)
	#----------------------------------------------------------------------
	def get_opaqueContainers(self):
		""""""
		return self.query(opaqueContainers=True)
	#----------------------------------------------------------------------
	def set_opaqueContainers(self, value):
		""""""
		self.edit(opaqueContainers=value)
	#----------------------------------------------------------------------
	opaqueContainers = property(get_opaqueContainers, set_opaqueContainers)
	#----------------------------------------------------------------------
	def get_orientation(self):
		""""""
		return self.query(orientation=True)
	#----------------------------------------------------------------------
	def set_orientation(self, value):
		""""""
		self.edit(orientation=value)
	#----------------------------------------------------------------------
	orientation = property(get_orientation, set_orientation)
	#----------------------------------------------------------------------
	def previousView(self,value):
		""""""
		self.edit(previousView=value)
	#----------------------------------------------------------------------
	def popupMenuScript(self,value):
		""""""
		self.edit(popupMenuScript=value)
	#----------------------------------------------------------------------
	def get_range(self):
		""""""
		return self.query(range=True)
	#----------------------------------------------------------------------
	def set_range(self, value):
		""""""
		self.edit(range=value)
	#----------------------------------------------------------------------
	range = property(get_range, set_range)
	#----------------------------------------------------------------------
	def rebuild(self,value):
		""""""
		self.edit(rebuild=value)
	#----------------------------------------------------------------------
	def rename(self,value):
		""""""
		self.edit(rename=value)
	#----------------------------------------------------------------------
	def resetFreeform(self,value):
		""""""
		self.edit(resetFreeform=value)
	#----------------------------------------------------------------------
	def get_freeform(self):
		""""""
		return self.query(freeform=True)
	#----------------------------------------------------------------------
	def set_freeform(self, value):
		""""""
		self.edit(freeform=value)
	#----------------------------------------------------------------------
	freeform = property(get_freeform, set_freeform)
	#----------------------------------------------------------------------
	def restoreBookmark(self,value):
		""""""
		self.edit(restoreBookmark=value)
	#----------------------------------------------------------------------
	def removeNode(self,value):
		""""""
		self.edit(removeNode=value)
	#----------------------------------------------------------------------
	def scrollUpDownNoZoom(self,value):
		""""""
		self.edit(scrollUpDownNoZoom=value)
	#----------------------------------------------------------------------
	def get_showConstraints(self):
		""""""
		return self.query(showConstraints=True)
	#----------------------------------------------------------------------
	def set_showConstraints(self, value):
		""""""
		self.edit(showConstraints=value)
	#----------------------------------------------------------------------
	showConstraints = property(get_showConstraints, set_showConstraints)
	#----------------------------------------------------------------------
	def get_showExpressions(self):
		""""""
		return self.query(showExpressions=True)
	#----------------------------------------------------------------------
	def set_showExpressions(self, value):
		""""""
		self.edit(showExpressions=value)
	#----------------------------------------------------------------------
	showExpressions = property(get_showExpressions, set_showExpressions)
	#----------------------------------------------------------------------
	def get_showDeformers(self):
		""""""
		return self.query(showDeformers=True)
	#----------------------------------------------------------------------
	def set_showDeformers(self, value):
		""""""
		self.edit(showDeformers=value)
	#----------------------------------------------------------------------
	showDeformers = property(get_showDeformers, set_showDeformers)
	#----------------------------------------------------------------------
	def get_showInvisible(self):
		""""""
		return self.query(showInvisible=True)
	#----------------------------------------------------------------------
	def set_showInvisible(self, value):
		""""""
		self.edit(showInvisible=value)
	#----------------------------------------------------------------------
	showInvisible = property(get_showInvisible, set_showInvisible)
	#----------------------------------------------------------------------
	def get_showConnectionFromSelected(self):
		""""""
		return self.query(showConnectionFromSelected=True)
	#----------------------------------------------------------------------
	def set_showConnectionFromSelected(self, value):
		""""""
		self.edit(showConnectionFromSelected=value)
	#----------------------------------------------------------------------
	showConnectionFromSelected = property(get_showConnectionFromSelected, set_showConnectionFromSelected)
	#----------------------------------------------------------------------
	def get_showConnectionToSelected(self):
		""""""
		return self.query(showConnectionToSelected=True)
	#----------------------------------------------------------------------
	def set_showConnectionToSelected(self, value):
		""""""
		self.edit(showConnectionToSelected=value)
	#----------------------------------------------------------------------
	showConnectionToSelected = property(get_showConnectionToSelected, set_showConnectionToSelected)
	#----------------------------------------------------------------------
	def get_showRelationships(self):
		""""""
		return self.query(showRelationships=True)
	#----------------------------------------------------------------------
	def set_showRelationships(self, value):
		""""""
		self.edit(showRelationships=value)
	#----------------------------------------------------------------------
	showRelationships = property(get_showRelationships, set_showRelationships)
	#----------------------------------------------------------------------
	def get_showShapes(self):
		""""""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		""""""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_showUnderworld(self):
		""""""
		return self.query(showUnderworld=True)
	#----------------------------------------------------------------------
	def set_showUnderworld(self, value):
		""""""
		self.edit(showUnderworld=value)
	#----------------------------------------------------------------------
	showUnderworld = property(get_showUnderworld, set_showUnderworld)
	#----------------------------------------------------------------------
	def setNodePosition(self,value):
		""""""
		self.edit(setNodePosition=value)
	#----------------------------------------------------------------------
	def get_transitionFrames(self):
		""""""
		return self.query(transitionFrames=True)
	#----------------------------------------------------------------------
	def set_transitionFrames(self, value):
		""""""
		self.edit(transitionFrames=value)
	#----------------------------------------------------------------------
	transitionFrames = property(get_transitionFrames, set_transitionFrames)
	#----------------------------------------------------------------------
	def unfold(self,value):
		""""""
		self.edit(unfold=value)
	#----------------------------------------------------------------------
	def unfoldAll(self,value):
		""""""
		self.edit(unfoldAll=value)
	#----------------------------------------------------------------------
	def get_updateNodeAdded(self):
		""""""
		return self.query(updateNodeAdded=True)
	#----------------------------------------------------------------------
	def set_updateNodeAdded(self, value):
		""""""
		self.edit(updateNodeAdded=value)
	#----------------------------------------------------------------------
	updateNodeAdded = property(get_updateNodeAdded, set_updateNodeAdded)
	#----------------------------------------------------------------------
	def get_updateSelection(self):
		""""""
		return self.query(updateSelection=True)
	#----------------------------------------------------------------------
	def set_updateSelection(self, value):
		""""""
		self.edit(updateSelection=value)
	#----------------------------------------------------------------------
	updateSelection = property(get_updateSelection, set_updateSelection)
	#----------------------------------------------------------------------
	def upstream(self,value):
		""""""
		self.edit(upstream=value)
	#----------------------------------------------------------------------
	def downstream(self,value):
		""""""
		self.edit(downstream=value)
	#----------------------------------------------------------------------
	def get_useFeedbackList(self):
		""""""
		return self.query(useFeedbackList=True)
	#----------------------------------------------------------------------
	def set_useFeedbackList(self, value):
		""""""
		self.edit(useFeedbackList=value)
	#----------------------------------------------------------------------
	useFeedbackList = property(get_useFeedbackList, set_useFeedbackList)
	#----------------------------------------------------------------------
	def visibility(self,value):
		""""""
		self.edit(visibility=value)
	#----------------------------------------------------------------------
	def zoom(self,value):
		""""""
		self.edit(zoom=value)
########################################################################
class HyperPanel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hyperPanel(**kwargs)
			super(HyperPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hyperPanel(name, exists=True):
				super(HyperPanel, self).__init__(name)
			else:
				name = cmds.hyperPanel(name, **kwargs)
				super(HyperPanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def init(self,value):
		""""""
		self.edit(init=value)
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def copy(self,value):
		""""""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		""""""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		""""""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		""""""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		""""""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		""""""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
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
	def get_needsInit(self):
		""""""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		""""""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
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
	def hyperEditor(self):
		""""""
		return self.query(hyperEditor=True)
########################################################################
class HyperShade(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hyperShade(**kwargs)
			super(HyperShade, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hyperShade(name, exists=True):
				super(HyperShade, self).__init__(name)
			else:
				name = cmds.hyperShade(name, **kwargs)
				super(HyperShade, self).__init__(name, **dict(qtParent=parent))
########################################################################
class ModelEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.modelEditor(**kwargs)
			super(ModelEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.modelEditor(name, exists=True):
				super(ModelEditor, self).__init__(name)
			else:
				name = cmds.modelEditor(name, **kwargs)
				super(ModelEditor, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(unParent=value)
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
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edit(updateMainConnection=value)
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
		self.edit(cameraName=value)
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
		self.edit(updateColorMode=value)
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
		self.edit(pluginObjects=value)
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
		self.edit(setSelected=value)
	#----------------------------------------------------------------------
	def addSelected(self,value):
		""""""
		self.edit(addSelected=value)
	#----------------------------------------------------------------------
	def removeSelected(self,value):
		""""""
		self.edit(removeSelected=value)
	#----------------------------------------------------------------------
	def addObjects(self,value):
		""""""
		self.edit(addObjects=value)
	#----------------------------------------------------------------------
	@property
	def viewObjects(self):
		""""""
		return self.query(viewObjects=True)
	#----------------------------------------------------------------------
	def noUndo(self,value):
		""""""
		self.edit(noUndo=value)
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
########################################################################
class ModelPanel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.modelPanel(**kwargs)
			super(ModelPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.modelPanel(name, exists=True):
				super(ModelPanel, self).__init__(name)
			else:
				name = cmds.modelPanel(name, **kwargs)
				super(ModelPanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def init(self,value):
		""""""
		self.edit(init=value)
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def copy(self,value):
		""""""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		""""""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		""""""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		""""""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		""""""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		""""""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
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
	def get_needsInit(self):
		""""""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		""""""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
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
	def modelEditor(self):
		""""""
		return self.query(modelEditor=True)
	#----------------------------------------------------------------------
	@property
	def barLayout(self):
		""""""
		return self.query(barLayout=True)
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
########################################################################
class NodeEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nodeEditor(**kwargs)
			super(NodeEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nodeEditor(name, exists=True):
				super(NodeEditor, self).__init__(name)
			else:
				name = cmds.nodeEditor(name, **kwargs)
				super(NodeEditor, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(unParent=value)
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
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edit(updateMainConnection=value)
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
	def get_addNewNodes(self):
		""""""
		return self.query(addNewNodes=True)
	#----------------------------------------------------------------------
	def set_addNewNodes(self, value):
		""""""
		self.edit(addNewNodes=value)
	#----------------------------------------------------------------------
	addNewNodes = property(get_addNewNodes, set_addNewNodes)
	#----------------------------------------------------------------------
	def addNode(self,value):
		""""""
		self.edit(addNode=value)
	#----------------------------------------------------------------------
	def get_allAttributes(self):
		""""""
		return self.query(allAttributes=True)
	#----------------------------------------------------------------------
	def set_allAttributes(self, value):
		""""""
		self.edit(allAttributes=value)
	#----------------------------------------------------------------------
	allAttributes = property(get_allAttributes, set_allAttributes)
	#----------------------------------------------------------------------
	def get_allNodes(self):
		""""""
		return self.query(allNodes=True)
	#----------------------------------------------------------------------
	def set_allNodes(self, value):
		""""""
		self.edit(allNodes=value)
	#----------------------------------------------------------------------
	allNodes = property(get_allNodes, set_allNodes)
	#----------------------------------------------------------------------
	def get_autoSizeNodes(self):
		""""""
		return self.query(autoSizeNodes=True)
	#----------------------------------------------------------------------
	def set_autoSizeNodes(self, value):
		""""""
		self.edit(autoSizeNodes=value)
	#----------------------------------------------------------------------
	autoSizeNodes = property(get_autoSizeNodes, set_autoSizeNodes)
	#----------------------------------------------------------------------
	def beginNewConnection(self,value):
		""""""
		self.edit(beginNewConnection=value)
	#----------------------------------------------------------------------
	def beginCreateNode(self,value):
		""""""
		self.edit(beginCreateNode=value)
	#----------------------------------------------------------------------
	def get_createNodeCommand(self):
		""""""
		return self.query(createNodeCommand=True)
	#----------------------------------------------------------------------
	def set_createNodeCommand(self, value):
		""""""
		self.edit(createNodeCommand=value)
	#----------------------------------------------------------------------
	createNodeCommand = property(get_createNodeCommand, set_createNodeCommand)
	#----------------------------------------------------------------------
	def cycleHUD(self,value):
		""""""
		self.edit(cycleHUD=value)
	#----------------------------------------------------------------------
	def get_dotFormat(self):
		""""""
		return self.query(dotFormat=True)
	#----------------------------------------------------------------------
	def set_dotFormat(self, value):
		""""""
		self.edit(dotFormat=value)
	#----------------------------------------------------------------------
	dotFormat = property(get_dotFormat, set_dotFormat)
	#----------------------------------------------------------------------
	def get_downstream(self):
		""""""
		return self.query(downstream=True)
	#----------------------------------------------------------------------
	def set_downstream(self, value):
		""""""
		self.edit(downstream=value)
	#----------------------------------------------------------------------
	downstream = property(get_downstream, set_downstream)
	#----------------------------------------------------------------------
	def get_filterCreateNodeTypes(self):
		""""""
		return self.query(filterCreateNodeTypes=True)
	#----------------------------------------------------------------------
	def set_filterCreateNodeTypes(self, value):
		""""""
		self.edit(filterCreateNodeTypes=value)
	#----------------------------------------------------------------------
	filterCreateNodeTypes = property(get_filterCreateNodeTypes, set_filterCreateNodeTypes)
	#----------------------------------------------------------------------
	def get_ignoreAssets(self):
		""""""
		return self.query(ignoreAssets=True)
	#----------------------------------------------------------------------
	def set_ignoreAssets(self, value):
		""""""
		self.edit(ignoreAssets=value)
	#----------------------------------------------------------------------
	ignoreAssets = property(get_ignoreAssets, set_ignoreAssets)
	#----------------------------------------------------------------------
	def get_upstream(self):
		""""""
		return self.query(upstream=True)
	#----------------------------------------------------------------------
	def set_upstream(self, value):
		""""""
		self.edit(upstream=value)
	#----------------------------------------------------------------------
	upstream = property(get_upstream, set_upstream)
	#----------------------------------------------------------------------
	def get_rootNode(self):
		""""""
		return self.query(rootNode=True)
	#----------------------------------------------------------------------
	def set_rootNode(self, value):
		""""""
		self.edit(rootNode=value)
	#----------------------------------------------------------------------
	rootNode = property(get_rootNode, set_rootNode)
	#----------------------------------------------------------------------
	def rootsFromSelection(self,value):
		""""""
		self.edit(rootsFromSelection=value)
	#----------------------------------------------------------------------
	def selectAll(self,value):
		""""""
		self.edit(selectAll=value)
	#----------------------------------------------------------------------
	def selectUpstream(self,value):
		""""""
		self.edit(selectUpstream=value)
	#----------------------------------------------------------------------
	def selectDownstream(self,value):
		""""""
		self.edit(selectDownstream=value)
	#----------------------------------------------------------------------
	def get_selectNode(self):
		""""""
		return self.query(selectNode=True)
	#----------------------------------------------------------------------
	def set_selectNode(self, value):
		""""""
		self.edit(selectNode=value)
	#----------------------------------------------------------------------
	selectNode = property(get_selectNode, set_selectNode)
	#----------------------------------------------------------------------
	def get_syncedSelection(self):
		""""""
		return self.query(syncedSelection=True)
	#----------------------------------------------------------------------
	def set_syncedSelection(self, value):
		""""""
		self.edit(syncedSelection=value)
	#----------------------------------------------------------------------
	syncedSelection = property(get_syncedSelection, set_syncedSelection)
	#----------------------------------------------------------------------
	def get_toolTipCommand(self):
		""""""
		return self.query(toolTipCommand=True)
	#----------------------------------------------------------------------
	def set_toolTipCommand(self, value):
		""""""
		self.edit(toolTipCommand=value)
	#----------------------------------------------------------------------
	toolTipCommand = property(get_toolTipCommand, set_toolTipCommand)
	#----------------------------------------------------------------------
	def get_traversalDepthLimit(self):
		""""""
		return self.query(traversalDepthLimit=True)
	#----------------------------------------------------------------------
	def set_traversalDepthLimit(self, value):
		""""""
		self.edit(traversalDepthLimit=value)
	#----------------------------------------------------------------------
	traversalDepthLimit = property(get_traversalDepthLimit, set_traversalDepthLimit)
	#----------------------------------------------------------------------
	def layout(self,value):
		""""""
		self.edit(layout=value)
	#----------------------------------------------------------------------
	def get_layoutCommand(self):
		""""""
		return self.query(layoutCommand=True)
	#----------------------------------------------------------------------
	def set_layoutCommand(self, value):
		""""""
		self.edit(layoutCommand=value)
	#----------------------------------------------------------------------
	layoutCommand = property(get_layoutCommand, set_layoutCommand)
	#----------------------------------------------------------------------
	def frameAll(self,value):
		""""""
		self.edit(frameAll=value)
	#----------------------------------------------------------------------
	def frameModelSelection(self,value):
		""""""
		self.edit(frameModelSelection=value)
	#----------------------------------------------------------------------
	def frameSelected(self,value):
		""""""
		self.edit(frameSelected=value)
	#----------------------------------------------------------------------
	def get_island(self):
		""""""
		return self.query(island=True)
	#----------------------------------------------------------------------
	def set_island(self, value):
		""""""
		self.edit(island=value)
	#----------------------------------------------------------------------
	island = property(get_island, set_island)
	#----------------------------------------------------------------------
	def get_popupMenuScript(self):
		""""""
		return self.query(popupMenuScript=True)
	#----------------------------------------------------------------------
	def set_popupMenuScript(self, value):
		""""""
		self.edit(popupMenuScript=value)
	#----------------------------------------------------------------------
	popupMenuScript = property(get_popupMenuScript, set_popupMenuScript)
	#----------------------------------------------------------------------
	def scaleView(self,value):
		""""""
		self.edit(scaleView=value)
	#----------------------------------------------------------------------
	def showAllNodeAttributes(self,value):
		""""""
		self.edit(showAllNodeAttributes=value)
	#----------------------------------------------------------------------
	def get_showNamespace(self):
		""""""
		return self.query(showNamespace=True)
	#----------------------------------------------------------------------
	def set_showNamespace(self, value):
		""""""
		self.edit(showNamespace=value)
	#----------------------------------------------------------------------
	showNamespace = property(get_showNamespace, set_showNamespace)
	#----------------------------------------------------------------------
	def get_showShapes(self):
		""""""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		""""""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_showSGShapes(self):
		""""""
		return self.query(showSGShapes=True)
	#----------------------------------------------------------------------
	def set_showSGShapes(self, value):
		""""""
		self.edit(showSGShapes=value)
	#----------------------------------------------------------------------
	showSGShapes = property(get_showSGShapes, set_showSGShapes)
	#----------------------------------------------------------------------
	def get_showTransforms(self):
		""""""
		return self.query(showTransforms=True)
	#----------------------------------------------------------------------
	def set_showTransforms(self, value):
		""""""
		self.edit(showTransforms=value)
	#----------------------------------------------------------------------
	showTransforms = property(get_showTransforms, set_showTransforms)
	#----------------------------------------------------------------------
	def get_extendToShapes(self):
		""""""
		return self.query(extendToShapes=True)
	#----------------------------------------------------------------------
	def set_extendToShapes(self, value):
		""""""
		self.edit(extendToShapes=value)
	#----------------------------------------------------------------------
	extendToShapes = property(get_extendToShapes, set_extendToShapes)
	#----------------------------------------------------------------------
	@property
	def feedbackConnection(self):
		""""""
		return self.query(feedbackConnection=True)
	#----------------------------------------------------------------------
	@property
	def feedbackNode(self):
		""""""
		return self.query(feedbackNode=True)
	#----------------------------------------------------------------------
	@property
	def feedbackPlug(self):
		""""""
		return self.query(feedbackPlug=True)
	#----------------------------------------------------------------------
	@property
	def feedbackType(self):
		""""""
		return self.query(feedbackType=True)
	#----------------------------------------------------------------------
	def hudMessage(self,value):
		""""""
		self.edit(hudMessage=value)
	#----------------------------------------------------------------------
	def removeNode(self,value):
		""""""
		self.edit(removeNode=value)
	#----------------------------------------------------------------------
	def removeUnselected(self,value):
		""""""
		self.edit(removeUnselected=value)
	#----------------------------------------------------------------------
	def removeUpstream(self,value):
		""""""
		self.edit(removeUpstream=value)
	#----------------------------------------------------------------------
	def removeDownstream(self,value):
		""""""
		self.edit(removeDownstream=value)
	#----------------------------------------------------------------------
	def renameNode(self,value):
		""""""
		self.edit(renameNode=value)
	#----------------------------------------------------------------------
	def restoreInfo(self,value):
		""""""
		self.edit(restoreInfo=value)
	#----------------------------------------------------------------------
	def createInfo(self,value):
		""""""
		self.edit(createInfo=value)
	#----------------------------------------------------------------------
	def deleteSelected(self,value):
		""""""
		self.edit(deleteSelected=value)
	#----------------------------------------------------------------------
	def get_keyPressCommand(self):
		""""""
		return self.query(keyPressCommand=True)
	#----------------------------------------------------------------------
	def set_keyPressCommand(self, value):
		""""""
		self.edit(keyPressCommand=value)
	#----------------------------------------------------------------------
	keyPressCommand = property(get_keyPressCommand, set_keyPressCommand)
	#----------------------------------------------------------------------
	def get_keyReleaseCommand(self):
		""""""
		return self.query(keyReleaseCommand=True)
	#----------------------------------------------------------------------
	def set_keyReleaseCommand(self, value):
		""""""
		self.edit(keyReleaseCommand=value)
	#----------------------------------------------------------------------
	keyReleaseCommand = property(get_keyReleaseCommand, set_keyReleaseCommand)
	#----------------------------------------------------------------------
	def nodeViewMode(self,value):
		""""""
		self.edit(nodeViewMode=value)
	#----------------------------------------------------------------------
	def get_nodeTitleMode(self):
		""""""
		return self.query(nodeTitleMode=True)
	#----------------------------------------------------------------------
	def set_nodeTitleMode(self, value):
		""""""
		self.edit(nodeTitleMode=value)
	#----------------------------------------------------------------------
	nodeTitleMode = property(get_nodeTitleMode, set_nodeTitleMode)
	#----------------------------------------------------------------------
	def panView(self,value):
		""""""
		self.edit(panView=value)
	#----------------------------------------------------------------------
	def get_settingsChangedCallback(self):
		""""""
		return self.query(settingsChangedCallback=True)
	#----------------------------------------------------------------------
	def set_settingsChangedCallback(self, value):
		""""""
		self.edit(settingsChangedCallback=value)
	#----------------------------------------------------------------------
	settingsChangedCallback = property(get_settingsChangedCallback, set_settingsChangedCallback)
	#----------------------------------------------------------------------
	def toggleSwatchSize(self,value):
		""""""
		self.edit(toggleSwatchSize=value)
	#----------------------------------------------------------------------
	def pinSelectedNodes(self,value):
		""""""
		self.edit(pinSelectedNodes=value)
	#----------------------------------------------------------------------
	def toggleSelectedPins(self,value):
		""""""
		self.edit(toggleSelectedPins=value)
	#----------------------------------------------------------------------
	def shaderNetworks(self,value):
		""""""
		self.edit(shaderNetworks=value)
	#----------------------------------------------------------------------
	def breakSelectedConnections(self,value):
		""""""
		self.edit(breakSelectedConnections=value)
	#----------------------------------------------------------------------
	def graphSelectedConnections(self,value):
		""""""
		self.edit(graphSelectedConnections=value)
	#----------------------------------------------------------------------
	def selectConnectionNodes(self,value):
		""""""
		self.edit(selectConnectionNodes=value)
	#----------------------------------------------------------------------
	def selectFeedbackConnection(self,value):
		""""""
		self.edit(selectFeedbackConnection=value)
	#----------------------------------------------------------------------
	def get_additiveGraphingMode(self):
		""""""
		return self.query(additiveGraphingMode=True)
	#----------------------------------------------------------------------
	def set_additiveGraphingMode(self, value):
		""""""
		self.edit(additiveGraphingMode=value)
	#----------------------------------------------------------------------
	additiveGraphingMode = property(get_additiveGraphingMode, set_additiveGraphingMode)
	#----------------------------------------------------------------------
	def get_defaultPinnedState(self):
		""""""
		return self.query(defaultPinnedState=True)
	#----------------------------------------------------------------------
	def set_defaultPinnedState(self, value):
		""""""
		self.edit(defaultPinnedState=value)
	#----------------------------------------------------------------------
	defaultPinnedState = property(get_defaultPinnedState, set_defaultPinnedState)
	#----------------------------------------------------------------------
	@property
	def getNodeList(self):
		""""""
		return self.query(getNodeList=True)
	#----------------------------------------------------------------------
	def get_gridVisibility(self):
		""""""
		return self.query(gridVisibility=True)
	#----------------------------------------------------------------------
	def set_gridVisibility(self, value):
		""""""
		self.edit(gridVisibility=value)
	#----------------------------------------------------------------------
	gridVisibility = property(get_gridVisibility, set_gridVisibility)
	#----------------------------------------------------------------------
	def get_gridSnap(self):
		""""""
		return self.query(gridSnap=True)
	#----------------------------------------------------------------------
	def set_gridSnap(self, value):
		""""""
		self.edit(gridSnap=value)
	#----------------------------------------------------------------------
	gridSnap = property(get_gridSnap, set_gridSnap)
########################################################################
class NodeOutliner(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nodeOutliner(**kwargs)
			super(NodeOutliner, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nodeOutliner(name, exists=True):
				super(NodeOutliner, self).__init__(name)
			else:
				name = cmds.nodeOutliner(name, **kwargs)
				super(NodeOutliner, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_addCommand(self):
		""""""
		return self.query(addCommand=True)
	#----------------------------------------------------------------------
	def set_addCommand(self, value):
		""""""
		self.edit(addCommand=value)
	#----------------------------------------------------------------------
	addCommand = property(get_addCommand, set_addCommand)
	#----------------------------------------------------------------------
	def addObject(self,value):
		""""""
		self.edit(addObject=value)
	#----------------------------------------------------------------------
	def remove(self,value):
		""""""
		self.edit(remove=value)
	#----------------------------------------------------------------------
	def removeAll(self,value):
		""""""
		self.edit(removeAll=value)
	#----------------------------------------------------------------------
	def get_replace(self):
		""""""
		return self.query(replace=True)
	#----------------------------------------------------------------------
	def set_replace(self, value):
		""""""
		self.edit(replace=value)
	#----------------------------------------------------------------------
	replace = property(get_replace, set_replace)
	#----------------------------------------------------------------------
	def get_showInputs(self):
		""""""
		return self.query(showInputs=True)
	#----------------------------------------------------------------------
	def set_showInputs(self, value):
		""""""
		self.edit(showInputs=value)
	#----------------------------------------------------------------------
	showInputs = property(get_showInputs, set_showInputs)
	#----------------------------------------------------------------------
	def get_showOutputs(self):
		""""""
		return self.query(showOutputs=True)
	#----------------------------------------------------------------------
	def set_showOutputs(self, value):
		""""""
		self.edit(showOutputs=value)
	#----------------------------------------------------------------------
	showOutputs = property(get_showOutputs, set_showOutputs)
	#----------------------------------------------------------------------
	def get_showPublished(self):
		""""""
		return self.query(showPublished=True)
	#----------------------------------------------------------------------
	def set_showPublished(self, value):
		""""""
		self.edit(showPublished=value)
	#----------------------------------------------------------------------
	showPublished = property(get_showPublished, set_showPublished)
	#----------------------------------------------------------------------
	def get_showReadOnly(self):
		""""""
		return self.query(showReadOnly=True)
	#----------------------------------------------------------------------
	def set_showReadOnly(self, value):
		""""""
		self.edit(showReadOnly=value)
	#----------------------------------------------------------------------
	showReadOnly = property(get_showReadOnly, set_showReadOnly)
	#----------------------------------------------------------------------
	def get_showHidden(self):
		""""""
		return self.query(showHidden=True)
	#----------------------------------------------------------------------
	def set_showHidden(self, value):
		""""""
		self.edit(showHidden=value)
	#----------------------------------------------------------------------
	showHidden = property(get_showHidden, set_showHidden)
	#----------------------------------------------------------------------
	def get_showNonKeyable(self):
		""""""
		return self.query(showNonKeyable=True)
	#----------------------------------------------------------------------
	def set_showNonKeyable(self, value):
		""""""
		self.edit(showNonKeyable=value)
	#----------------------------------------------------------------------
	showNonKeyable = property(get_showNonKeyable, set_showNonKeyable)
	#----------------------------------------------------------------------
	def get_showNonConnectable(self):
		""""""
		return self.query(showNonConnectable=True)
	#----------------------------------------------------------------------
	def set_showNonConnectable(self, value):
		""""""
		self.edit(showNonConnectable=value)
	#----------------------------------------------------------------------
	showNonConnectable = property(get_showNonConnectable, set_showNonConnectable)
	#----------------------------------------------------------------------
	def get_showConnectedOnly(self):
		""""""
		return self.query(showConnectedOnly=True)
	#----------------------------------------------------------------------
	def set_showConnectedOnly(self, value):
		""""""
		self.edit(showConnectedOnly=value)
	#----------------------------------------------------------------------
	showConnectedOnly = property(get_showConnectedOnly, set_showConnectedOnly)
	#----------------------------------------------------------------------
	def get_connectivity(self):
		""""""
		return self.query(connectivity=True)
	#----------------------------------------------------------------------
	def set_connectivity(self, value):
		""""""
		self.edit(connectivity=value)
	#----------------------------------------------------------------------
	connectivity = property(get_connectivity, set_connectivity)
	#----------------------------------------------------------------------
	def noConnectivity(self,value):
		""""""
		self.edit(noConnectivity=value)
	#----------------------------------------------------------------------
	def get_multiSelect(self):
		""""""
		return self.query(multiSelect=True)
	#----------------------------------------------------------------------
	def set_multiSelect(self, value):
		""""""
		self.edit(multiSelect=value)
	#----------------------------------------------------------------------
	multiSelect = property(get_multiSelect, set_multiSelect)
	#----------------------------------------------------------------------
	def get_selectCommand(self):
		""""""
		return self.query(selectCommand=True)
	#----------------------------------------------------------------------
	def set_selectCommand(self, value):
		""""""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	selectCommand = property(get_selectCommand, set_selectCommand)
	#----------------------------------------------------------------------
	@property
	def currentSelection(self):
		""""""
		return self.query(currentSelection=True)
	#----------------------------------------------------------------------
	@property
	def nodesDisplayed(self):
		""""""
		return self.query(nodesDisplayed=True)
	#----------------------------------------------------------------------
	def menuCommand(self,value):
		""""""
		self.edit(menuCommand=value)
	#----------------------------------------------------------------------
	@property
	def lastMenuChoice(self):
		""""""
		return self.query(lastMenuChoice=True)
	#----------------------------------------------------------------------
	def get_menuMultiOption(self):
		""""""
		return self.query(menuMultiOption=True)
	#----------------------------------------------------------------------
	def set_menuMultiOption(self, value):
		""""""
		self.edit(menuMultiOption=value)
	#----------------------------------------------------------------------
	menuMultiOption = property(get_menuMultiOption, set_menuMultiOption)
	#----------------------------------------------------------------------
	def get_pressHighlightsUnconnected(self):
		""""""
		return self.query(pressHighlightsUnconnected=True)
	#----------------------------------------------------------------------
	def set_pressHighlightsUnconnected(self, value):
		""""""
		self.edit(pressHighlightsUnconnected=value)
	#----------------------------------------------------------------------
	pressHighlightsUnconnected = property(get_pressHighlightsUnconnected, set_pressHighlightsUnconnected)
	#----------------------------------------------------------------------
	def get_longNames(self):
		""""""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		""""""
		self.edit(longNames=value)
	#----------------------------------------------------------------------
	longNames = property(get_longNames, set_longNames)
	#----------------------------------------------------------------------
	def get_niceNames(self):
		""""""
		return self.query(niceNames=True)
	#----------------------------------------------------------------------
	def set_niceNames(self, value):
		""""""
		self.edit(niceNames=value)
	#----------------------------------------------------------------------
	niceNames = property(get_niceNames, set_niceNames)
	#----------------------------------------------------------------------
	def get_attrAlphaOrder(self):
		""""""
		return self.query(attrAlphaOrder=True)
	#----------------------------------------------------------------------
	def set_attrAlphaOrder(self, value):
		""""""
		self.edit(attrAlphaOrder=value)
	#----------------------------------------------------------------------
	attrAlphaOrder = property(get_attrAlphaOrder, set_attrAlphaOrder)
########################################################################
class OutlinerEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.outlinerEditor(**kwargs)
			super(OutlinerEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.outlinerEditor(name, exists=True):
				super(OutlinerEditor, self).__init__(name)
			else:
				name = cmds.outlinerEditor(name, **kwargs)
				super(OutlinerEditor, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(unParent=value)
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
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edit(updateMainConnection=value)
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
	def get_showShapes(self):
		""""""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		""""""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_showReferenceNodes(self):
		""""""
		return self.query(showReferenceNodes=True)
	#----------------------------------------------------------------------
	def set_showReferenceNodes(self, value):
		""""""
		self.edit(showReferenceNodes=value)
	#----------------------------------------------------------------------
	showReferenceNodes = property(get_showReferenceNodes, set_showReferenceNodes)
	#----------------------------------------------------------------------
	def get_showReferenceMembers(self):
		""""""
		return self.query(showReferenceMembers=True)
	#----------------------------------------------------------------------
	def set_showReferenceMembers(self, value):
		""""""
		self.edit(showReferenceMembers=value)
	#----------------------------------------------------------------------
	showReferenceMembers = property(get_showReferenceMembers, set_showReferenceMembers)
	#----------------------------------------------------------------------
	def get_attrFilter(self):
		""""""
		return self.query(attrFilter=True)
	#----------------------------------------------------------------------
	def set_attrFilter(self, value):
		""""""
		self.edit(attrFilter=value)
	#----------------------------------------------------------------------
	attrFilter = property(get_attrFilter, set_attrFilter)
	#----------------------------------------------------------------------
	def get_showAttributes(self):
		""""""
		return self.query(showAttributes=True)
	#----------------------------------------------------------------------
	def set_showAttributes(self, value):
		""""""
		self.edit(showAttributes=value)
	#----------------------------------------------------------------------
	showAttributes = property(get_showAttributes, set_showAttributes)
	#----------------------------------------------------------------------
	def get_showConnected(self):
		""""""
		return self.query(showConnected=True)
	#----------------------------------------------------------------------
	def set_showConnected(self, value):
		""""""
		self.edit(showConnected=value)
	#----------------------------------------------------------------------
	showConnected = property(get_showConnected, set_showConnected)
	#----------------------------------------------------------------------
	def get_showAnimCurvesOnly(self):
		""""""
		return self.query(showAnimCurvesOnly=True)
	#----------------------------------------------------------------------
	def set_showAnimCurvesOnly(self, value):
		""""""
		self.edit(showAnimCurvesOnly=value)
	#----------------------------------------------------------------------
	showAnimCurvesOnly = property(get_showAnimCurvesOnly, set_showAnimCurvesOnly)
	#----------------------------------------------------------------------
	def get_showTextureNodesOnly(self):
		""""""
		return self.query(showTextureNodesOnly=True)
	#----------------------------------------------------------------------
	def set_showTextureNodesOnly(self, value):
		""""""
		self.edit(showTextureNodesOnly=value)
	#----------------------------------------------------------------------
	showTextureNodesOnly = property(get_showTextureNodesOnly, set_showTextureNodesOnly)
	#----------------------------------------------------------------------
	def get_showDagOnly(self):
		""""""
		return self.query(showDagOnly=True)
	#----------------------------------------------------------------------
	def set_showDagOnly(self, value):
		""""""
		self.edit(showDagOnly=value)
	#----------------------------------------------------------------------
	showDagOnly = property(get_showDagOnly, set_showDagOnly)
	#----------------------------------------------------------------------
	def get_showAssets(self):
		""""""
		return self.query(showAssets=True)
	#----------------------------------------------------------------------
	def set_showAssets(self, value):
		""""""
		self.edit(showAssets=value)
	#----------------------------------------------------------------------
	showAssets = property(get_showAssets, set_showAssets)
	#----------------------------------------------------------------------
	def get_showContainerContents(self):
		""""""
		return self.query(showContainerContents=True)
	#----------------------------------------------------------------------
	def set_showContainerContents(self, value):
		""""""
		self.edit(showContainerContents=value)
	#----------------------------------------------------------------------
	showContainerContents = property(get_showContainerContents, set_showContainerContents)
	#----------------------------------------------------------------------
	def get_showContainedOnly(self):
		""""""
		return self.query(showContainedOnly=True)
	#----------------------------------------------------------------------
	def set_showContainedOnly(self, value):
		""""""
		self.edit(showContainedOnly=value)
	#----------------------------------------------------------------------
	showContainedOnly = property(get_showContainedOnly, set_showContainedOnly)
	#----------------------------------------------------------------------
	def get_showPublishedAsConnected(self):
		""""""
		return self.query(showPublishedAsConnected=True)
	#----------------------------------------------------------------------
	def set_showPublishedAsConnected(self, value):
		""""""
		self.edit(showPublishedAsConnected=value)
	#----------------------------------------------------------------------
	showPublishedAsConnected = property(get_showPublishedAsConnected, set_showPublishedAsConnected)
	#----------------------------------------------------------------------
	def get_ignoreDagHierarchy(self):
		""""""
		return self.query(ignoreDagHierarchy=True)
	#----------------------------------------------------------------------
	def set_ignoreDagHierarchy(self, value):
		""""""
		self.edit(ignoreDagHierarchy=value)
	#----------------------------------------------------------------------
	ignoreDagHierarchy = property(get_ignoreDagHierarchy, set_ignoreDagHierarchy)
	#----------------------------------------------------------------------
	def get_autoExpand(self):
		""""""
		return self.query(autoExpand=True)
	#----------------------------------------------------------------------
	def set_autoExpand(self, value):
		""""""
		self.edit(autoExpand=value)
	#----------------------------------------------------------------------
	autoExpand = property(get_autoExpand, set_autoExpand)
	#----------------------------------------------------------------------
	def get_expandConnections(self):
		""""""
		return self.query(expandConnections=True)
	#----------------------------------------------------------------------
	def set_expandConnections(self, value):
		""""""
		self.edit(expandConnections=value)
	#----------------------------------------------------------------------
	expandConnections = property(get_expandConnections, set_expandConnections)
	#----------------------------------------------------------------------
	def get_showUpstreamCurves(self):
		""""""
		return self.query(showUpstreamCurves=True)
	#----------------------------------------------------------------------
	def set_showUpstreamCurves(self, value):
		""""""
		self.edit(showUpstreamCurves=value)
	#----------------------------------------------------------------------
	showUpstreamCurves = property(get_showUpstreamCurves, set_showUpstreamCurves)
	#----------------------------------------------------------------------
	def get_showUnitlessCurves(self):
		""""""
		return self.query(showUnitlessCurves=True)
	#----------------------------------------------------------------------
	def set_showUnitlessCurves(self, value):
		""""""
		self.edit(showUnitlessCurves=value)
	#----------------------------------------------------------------------
	showUnitlessCurves = property(get_showUnitlessCurves, set_showUnitlessCurves)
	#----------------------------------------------------------------------
	def get_showCompounds(self):
		""""""
		return self.query(showCompounds=True)
	#----------------------------------------------------------------------
	def set_showCompounds(self, value):
		""""""
		self.edit(showCompounds=value)
	#----------------------------------------------------------------------
	showCompounds = property(get_showCompounds, set_showCompounds)
	#----------------------------------------------------------------------
	def get_showLeafs(self):
		""""""
		return self.query(showLeafs=True)
	#----------------------------------------------------------------------
	def set_showLeafs(self, value):
		""""""
		self.edit(showLeafs=value)
	#----------------------------------------------------------------------
	showLeafs = property(get_showLeafs, set_showLeafs)
	#----------------------------------------------------------------------
	def get_showNumericAttrsOnly(self):
		""""""
		return self.query(showNumericAttrsOnly=True)
	#----------------------------------------------------------------------
	def set_showNumericAttrsOnly(self, value):
		""""""
		self.edit(showNumericAttrsOnly=value)
	#----------------------------------------------------------------------
	showNumericAttrsOnly = property(get_showNumericAttrsOnly, set_showNumericAttrsOnly)
	#----------------------------------------------------------------------
	def get_editAttrName(self):
		""""""
		return self.query(editAttrName=True)
	#----------------------------------------------------------------------
	def set_editAttrName(self, value):
		""""""
		self.edit(editAttrName=value)
	#----------------------------------------------------------------------
	editAttrName = property(get_editAttrName, set_editAttrName)
	#----------------------------------------------------------------------
	def get_showUVAttrsOnly(self):
		""""""
		return self.query(showUVAttrsOnly=True)
	#----------------------------------------------------------------------
	def set_showUVAttrsOnly(self, value):
		""""""
		self.edit(showUVAttrsOnly=value)
	#----------------------------------------------------------------------
	showUVAttrsOnly = property(get_showUVAttrsOnly, set_showUVAttrsOnly)
	#----------------------------------------------------------------------
	def get_highlightActive(self):
		""""""
		return self.query(highlightActive=True)
	#----------------------------------------------------------------------
	def set_highlightActive(self, value):
		""""""
		self.edit(highlightActive=value)
	#----------------------------------------------------------------------
	highlightActive = property(get_highlightActive, set_highlightActive)
	#----------------------------------------------------------------------
	def get_highlightSecondary(self):
		""""""
		return self.query(highlightSecondary=True)
	#----------------------------------------------------------------------
	def set_highlightSecondary(self, value):
		""""""
		self.edit(highlightSecondary=value)
	#----------------------------------------------------------------------
	highlightSecondary = property(get_highlightSecondary, set_highlightSecondary)
	#----------------------------------------------------------------------
	def get_autoSelectNewObjects(self):
		""""""
		return self.query(autoSelectNewObjects=True)
	#----------------------------------------------------------------------
	def set_autoSelectNewObjects(self, value):
		""""""
		self.edit(autoSelectNewObjects=value)
	#----------------------------------------------------------------------
	autoSelectNewObjects = property(get_autoSelectNewObjects, set_autoSelectNewObjects)
	#----------------------------------------------------------------------
	def get_doNotSelectNewObjects(self):
		""""""
		return self.query(doNotSelectNewObjects=True)
	#----------------------------------------------------------------------
	def set_doNotSelectNewObjects(self, value):
		""""""
		self.edit(doNotSelectNewObjects=value)
	#----------------------------------------------------------------------
	doNotSelectNewObjects = property(get_doNotSelectNewObjects, set_doNotSelectNewObjects)
	#----------------------------------------------------------------------
	def get_dropIsParent(self):
		""""""
		return self.query(dropIsParent=True)
	#----------------------------------------------------------------------
	def set_dropIsParent(self, value):
		""""""
		self.edit(dropIsParent=value)
	#----------------------------------------------------------------------
	dropIsParent = property(get_dropIsParent, set_dropIsParent)
	#----------------------------------------------------------------------
	def get_transmitFilters(self):
		""""""
		return self.query(transmitFilters=True)
	#----------------------------------------------------------------------
	def set_transmitFilters(self, value):
		""""""
		self.edit(transmitFilters=value)
	#----------------------------------------------------------------------
	transmitFilters = property(get_transmitFilters, set_transmitFilters)
	#----------------------------------------------------------------------
	def showSelected(self,value):
		""""""
		self.edit(showSelected=value)
	#----------------------------------------------------------------------
	def get_setFilter(self):
		""""""
		return self.query(setFilter=True)
	#----------------------------------------------------------------------
	def set_setFilter(self, value):
		""""""
		self.edit(setFilter=value)
	#----------------------------------------------------------------------
	setFilter = property(get_setFilter, set_setFilter)
	#----------------------------------------------------------------------
	def get_showSetMembers(self):
		""""""
		return self.query(showSetMembers=True)
	#----------------------------------------------------------------------
	def set_showSetMembers(self, value):
		""""""
		self.edit(showSetMembers=value)
	#----------------------------------------------------------------------
	showSetMembers = property(get_showSetMembers, set_showSetMembers)
	#----------------------------------------------------------------------
	def get_organizeByLayer(self):
		""""""
		return self.query(organizeByLayer=True)
	#----------------------------------------------------------------------
	def set_organizeByLayer(self, value):
		""""""
		self.edit(organizeByLayer=value)
	#----------------------------------------------------------------------
	organizeByLayer = property(get_organizeByLayer, set_organizeByLayer)
	#----------------------------------------------------------------------
	def get_showAnimLayerWeight(self):
		""""""
		return self.query(showAnimLayerWeight=True)
	#----------------------------------------------------------------------
	def set_showAnimLayerWeight(self, value):
		""""""
		self.edit(showAnimLayerWeight=value)
	#----------------------------------------------------------------------
	showAnimLayerWeight = property(get_showAnimLayerWeight, set_showAnimLayerWeight)
	#----------------------------------------------------------------------
	def get_autoExpandLayers(self):
		""""""
		return self.query(autoExpandLayers=True)
	#----------------------------------------------------------------------
	def set_autoExpandLayers(self, value):
		""""""
		self.edit(autoExpandLayers=value)
	#----------------------------------------------------------------------
	autoExpandLayers = property(get_autoExpandLayers, set_autoExpandLayers)
	#----------------------------------------------------------------------
	def allowMultiSelection(self,value):
		""""""
		self.edit(allowMultiSelection=value)
	#----------------------------------------------------------------------
	def alwaysToggleSelect(self,value):
		""""""
		self.edit(alwaysToggleSelect=value)
	#----------------------------------------------------------------------
	def directSelect(self,value):
		""""""
		self.edit(directSelect=value)
	#----------------------------------------------------------------------
	@property
	def parentObject(self):
		""""""
		return self.query(parentObject=True)
	#----------------------------------------------------------------------
	@property
	def object(self):
		""""""
		return self.query(object=True)
	#----------------------------------------------------------------------
	def get_displayMode(self):
		""""""
		return self.query(displayMode=True)
	#----------------------------------------------------------------------
	def set_displayMode(self, value):
		""""""
		self.edit(displayMode=value)
	#----------------------------------------------------------------------
	displayMode = property(get_displayMode, set_displayMode)
	#----------------------------------------------------------------------
	def get_expandObjects(self):
		""""""
		return self.query(expandObjects=True)
	#----------------------------------------------------------------------
	def set_expandObjects(self, value):
		""""""
		self.edit(expandObjects=value)
	#----------------------------------------------------------------------
	expandObjects = property(get_expandObjects, set_expandObjects)
	#----------------------------------------------------------------------
	def get_setsIgnoreFilters(self):
		""""""
		return self.query(setsIgnoreFilters=True)
	#----------------------------------------------------------------------
	def set_setsIgnoreFilters(self, value):
		""""""
		self.edit(setsIgnoreFilters=value)
	#----------------------------------------------------------------------
	setsIgnoreFilters = property(get_setsIgnoreFilters, set_setsIgnoreFilters)
	#----------------------------------------------------------------------
	def get_containersIgnoreFilters(self):
		""""""
		return self.query(containersIgnoreFilters=True)
	#----------------------------------------------------------------------
	def set_containersIgnoreFilters(self, value):
		""""""
		self.edit(containersIgnoreFilters=value)
	#----------------------------------------------------------------------
	containersIgnoreFilters = property(get_containersIgnoreFilters, set_containersIgnoreFilters)
	#----------------------------------------------------------------------
	def get_showAttrValues(self):
		""""""
		return self.query(showAttrValues=True)
	#----------------------------------------------------------------------
	def set_showAttrValues(self, value):
		""""""
		self.edit(showAttrValues=value)
	#----------------------------------------------------------------------
	showAttrValues = property(get_showAttrValues, set_showAttrValues)
	#----------------------------------------------------------------------
	def get_masterOutliner(self):
		""""""
		return self.query(masterOutliner=True)
	#----------------------------------------------------------------------
	def set_masterOutliner(self, value):
		""""""
		self.edit(masterOutliner=value)
	#----------------------------------------------------------------------
	masterOutliner = property(get_masterOutliner, set_masterOutliner)
	#----------------------------------------------------------------------
	@property
	def isChildSelected(self):
		""""""
		return self.query(isChildSelected=True)
	#----------------------------------------------------------------------
	def get_attrAlphaOrder(self):
		""""""
		return self.query(attrAlphaOrder=True)
	#----------------------------------------------------------------------
	def set_attrAlphaOrder(self, value):
		""""""
		self.edit(attrAlphaOrder=value)
	#----------------------------------------------------------------------
	attrAlphaOrder = property(get_attrAlphaOrder, set_attrAlphaOrder)
	#----------------------------------------------------------------------
	def get_animLayerFilterOptions(self):
		""""""
		return self.query(animLayerFilterOptions=True)
	#----------------------------------------------------------------------
	def set_animLayerFilterOptions(self, value):
		""""""
		self.edit(animLayerFilterOptions=value)
	#----------------------------------------------------------------------
	animLayerFilterOptions = property(get_animLayerFilterOptions, set_animLayerFilterOptions)
	#----------------------------------------------------------------------
	def get_sortOrder(self):
		""""""
		return self.query(sortOrder=True)
	#----------------------------------------------------------------------
	def set_sortOrder(self, value):
		""""""
		self.edit(sortOrder=value)
	#----------------------------------------------------------------------
	sortOrder = property(get_sortOrder, set_sortOrder)
	#----------------------------------------------------------------------
	def get_longNames(self):
		""""""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		""""""
		self.edit(longNames=value)
	#----------------------------------------------------------------------
	longNames = property(get_longNames, set_longNames)
	#----------------------------------------------------------------------
	def get_niceNames(self):
		""""""
		return self.query(niceNames=True)
	#----------------------------------------------------------------------
	def set_niceNames(self, value):
		""""""
		self.edit(niceNames=value)
	#----------------------------------------------------------------------
	niceNames = property(get_niceNames, set_niceNames)
	#----------------------------------------------------------------------
	def get_selectCommand(self):
		""""""
		return self.query(selectCommand=True)
	#----------------------------------------------------------------------
	def set_selectCommand(self, value):
		""""""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	selectCommand = property(get_selectCommand, set_selectCommand)
	#----------------------------------------------------------------------
	def get_showNamespace(self):
		""""""
		return self.query(showNamespace=True)
	#----------------------------------------------------------------------
	def set_showNamespace(self, value):
		""""""
		self.edit(showNamespace=value)
	#----------------------------------------------------------------------
	showNamespace = property(get_showNamespace, set_showNamespace)
	#----------------------------------------------------------------------
	def get_pinPlug(self):
		""""""
		return self.query(pinPlug=True)
	#----------------------------------------------------------------------
	def set_pinPlug(self, value):
		""""""
		self.edit(pinPlug=value)
	#----------------------------------------------------------------------
	pinPlug = property(get_pinPlug, set_pinPlug)
	#----------------------------------------------------------------------
	def unpinPlug(self,value):
		""""""
		self.edit(unpinPlug=value)
	#----------------------------------------------------------------------
	def get_showPinIcons(self):
		""""""
		return self.query(showPinIcons=True)
	#----------------------------------------------------------------------
	def set_showPinIcons(self, value):
		""""""
		self.edit(showPinIcons=value)
	#----------------------------------------------------------------------
	showPinIcons = property(get_showPinIcons, set_showPinIcons)
	#----------------------------------------------------------------------
	def get_mapMotionTrails(self):
		""""""
		return self.query(mapMotionTrails=True)
	#----------------------------------------------------------------------
	def set_mapMotionTrails(self, value):
		""""""
		self.edit(mapMotionTrails=value)
	#----------------------------------------------------------------------
	mapMotionTrails = property(get_mapMotionTrails, set_mapMotionTrails)
########################################################################
class OutlinerPanel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.outlinerPanel(**kwargs)
			super(OutlinerPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.outlinerPanel(name, exists=True):
				super(OutlinerPanel, self).__init__(name)
			else:
				name = cmds.outlinerPanel(name, **kwargs)
				super(OutlinerPanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def init(self,value):
		""""""
		self.edit(init=value)
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def copy(self,value):
		""""""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		""""""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		""""""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		""""""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		""""""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		""""""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
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
	def get_needsInit(self):
		""""""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		""""""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
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
	def outlinerEditor(self):
		""""""
		return self.query(outlinerEditor=True)
########################################################################
class Panel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.panel(**kwargs)
			super(Panel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.panel(name, exists=True):
				super(Panel, self).__init__(name)
			else:
				name = cmds.panel(name, **kwargs)
				super(Panel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def init(self,value):
		""""""
		self.edit(init=value)
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def copy(self,value):
		""""""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		""""""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		""""""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		""""""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		""""""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		""""""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
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
	def get_needsInit(self):
		""""""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		""""""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
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
########################################################################
class PanelConfiguration(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.panelConfiguration(**kwargs)
			super(PanelConfiguration, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.panelConfiguration(name, exists=True):
				super(PanelConfiguration, self).__init__(name)
			else:
				name = cmds.panelConfiguration(name, **kwargs)
				super(PanelConfiguration, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	@property
	def defaultImage(self):
		""""""
		return self.query(defaultImage=True)
	#----------------------------------------------------------------------
	def get_image(self):
		""""""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		""""""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
	#----------------------------------------------------------------------
	def get_sceneConfig(self):
		""""""
		return self.query(sceneConfig=True)
	#----------------------------------------------------------------------
	def set_sceneConfig(self, value):
		""""""
		self.edit(sceneConfig=value)
	#----------------------------------------------------------------------
	sceneConfig = property(get_sceneConfig, set_sceneConfig)
	#----------------------------------------------------------------------
	def get_configString(self):
		""""""
		return self.query(configString=True)
	#----------------------------------------------------------------------
	def set_configString(self, value):
		""""""
		self.edit(configString=value)
	#----------------------------------------------------------------------
	configString = property(get_configString, set_configString)
	#----------------------------------------------------------------------
	@property
	def numberOfPanels(self):
		""""""
		return self.query(numberOfPanels=True)
	#----------------------------------------------------------------------
	def addPanel(self,value):
		""""""
		self.edit(addPanel=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def replaceLabel(self,value):
		""""""
		self.edit(replaceLabel=value)
	#----------------------------------------------------------------------
	def replaceEditString(self,value):
		""""""
		self.edit(replaceEditString=value)
	#----------------------------------------------------------------------
	def replaceCreateString(self,value):
		""""""
		self.edit(replaceCreateString=value)
	#----------------------------------------------------------------------
	def replaceFixedState(self,value):
		""""""
		self.edit(replaceFixedState=value)
	#----------------------------------------------------------------------
	def replaceTypeString(self,value):
		""""""
		self.edit(replaceTypeString=value)
	#----------------------------------------------------------------------
	def removeLastPanel(self,value):
		""""""
		self.edit(removeLastPanel=value)
	#----------------------------------------------------------------------
	def removeAllPanels(self,value):
		""""""
		self.edit(removeAllPanels=value)
	#----------------------------------------------------------------------
	@property
	def isFixedState(self):
		""""""
		return self.query(isFixedState=True)
	#----------------------------------------------------------------------
	@property
	def labelStrings(self):
		""""""
		return self.query(labelStrings=True)
	#----------------------------------------------------------------------
	@property
	def typeStrings(self):
		""""""
		return self.query(typeStrings=True)
	#----------------------------------------------------------------------
	@property
	def createStrings(self):
		""""""
		return self.query(createStrings=True)
	#----------------------------------------------------------------------
	@property
	def editStrings(self):
		""""""
		return self.query(editStrings=True)
########################################################################
class PanelHistory(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.panelHistory(**kwargs)
			super(PanelHistory, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.panelHistory(name, exists=True):
				super(PanelHistory, self).__init__(name)
			else:
				name = cmds.panelHistory(name, **kwargs)
				super(PanelHistory, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def targetPane(self):
		""""""
		return self.query(targetPane=True)
	#----------------------------------------------------------------------
	def back(self,value):
		""""""
		self.edit(back=value)
	#----------------------------------------------------------------------
	def forward(self,value):
		""""""
		self.edit(forward=value)
	#----------------------------------------------------------------------
	def clear(self,value):
		""""""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def get_historyDepth(self):
		""""""
		return self.query(historyDepth=True)
	#----------------------------------------------------------------------
	def set_historyDepth(self, value):
		""""""
		self.edit(historyDepth=value)
	#----------------------------------------------------------------------
	historyDepth = property(get_historyDepth, set_historyDepth)
	#----------------------------------------------------------------------
	def suspend(self,value):
		""""""
		self.edit(suspend=value)
	#----------------------------------------------------------------------
	def get_wrap(self):
		""""""
		return self.query(wrap=True)
	#----------------------------------------------------------------------
	def set_wrap(self, value):
		""""""
		self.edit(wrap=value)
	#----------------------------------------------------------------------
	wrap = property(get_wrap, set_wrap)
	#----------------------------------------------------------------------
	@property
	def isEmpty(self):
		""""""
		return self.query(isEmpty=True)
########################################################################
class SaveViewportSettings(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveViewportSettings(**kwargs)
			super(SaveViewportSettings, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveViewportSettings(name, exists=True):
				super(SaveViewportSettings, self).__init__(name)
			else:
				name = cmds.saveViewportSettings(name, **kwargs)
				super(SaveViewportSettings, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def targetPane(self):
		""""""
		return self.query(targetPane=True)
	#----------------------------------------------------------------------
	def back(self,value):
		""""""
		self.edit(back=value)
	#----------------------------------------------------------------------
	def forward(self,value):
		""""""
		self.edit(forward=value)
	#----------------------------------------------------------------------
	def clear(self,value):
		""""""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def get_historyDepth(self):
		""""""
		return self.query(historyDepth=True)
	#----------------------------------------------------------------------
	def set_historyDepth(self, value):
		""""""
		self.edit(historyDepth=value)
	#----------------------------------------------------------------------
	historyDepth = property(get_historyDepth, set_historyDepth)
	#----------------------------------------------------------------------
	def suspend(self,value):
		""""""
		self.edit(suspend=value)
	#----------------------------------------------------------------------
	def get_wrap(self):
		""""""
		return self.query(wrap=True)
	#----------------------------------------------------------------------
	def set_wrap(self, value):
		""""""
		self.edit(wrap=value)
	#----------------------------------------------------------------------
	wrap = property(get_wrap, set_wrap)
	#----------------------------------------------------------------------
	@property
	def isEmpty(self):
		""""""
		return self.query(isEmpty=True)
########################################################################
class ScriptedPanel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scriptedPanel(**kwargs)
			super(ScriptedPanel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scriptedPanel(name, exists=True):
				super(ScriptedPanel, self).__init__(name)
			else:
				name = cmds.scriptedPanel(name, **kwargs)
				super(ScriptedPanel, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def init(self,value):
		""""""
		self.edit(init=value)
	#----------------------------------------------------------------------
	def get_label(self):
		""""""
		return self.query(label=True)
	#----------------------------------------------------------------------
	def set_label(self, value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	label = property(get_label, set_label)
	#----------------------------------------------------------------------
	def copy(self,value):
		""""""
		self.edit(copy=value)
	#----------------------------------------------------------------------
	@property
	def control(self):
		""""""
		return self.query(control=True)
	#----------------------------------------------------------------------
	@property
	def isUnique(self):
		""""""
		return self.query(isUnique=True)
	#----------------------------------------------------------------------
	def get_popupMenuProcedure(self):
		""""""
		return self.query(popupMenuProcedure=True)
	#----------------------------------------------------------------------
	def set_popupMenuProcedure(self, value):
		""""""
		self.edit(popupMenuProcedure=value)
	#----------------------------------------------------------------------
	popupMenuProcedure = property(get_popupMenuProcedure, set_popupMenuProcedure)
	#----------------------------------------------------------------------
	def unParent(self,value):
		""""""
		self.edit(unParent=value)
	#----------------------------------------------------------------------
	def replacePanel(self,value):
		""""""
		self.edit(replacePanel=value)
	#----------------------------------------------------------------------
	def get_tearOff(self):
		""""""
		return self.query(tearOff=True)
	#----------------------------------------------------------------------
	def set_tearOff(self, value):
		""""""
		self.edit(tearOff=value)
	#----------------------------------------------------------------------
	tearOff = property(get_tearOff, set_tearOff)
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
	def get_needsInit(self):
		""""""
		return self.query(needsInit=True)
	#----------------------------------------------------------------------
	def set_needsInit(self, value):
		""""""
		self.edit(needsInit=value)
	#----------------------------------------------------------------------
	needsInit = property(get_needsInit, set_needsInit)
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
	def type(self):
		""""""
		return self.query(type=True)
########################################################################
class ScriptedPanelType(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scriptedPanelType(**kwargs)
			super(ScriptedPanelType, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scriptedPanelType(name, exists=True):
				super(ScriptedPanelType, self).__init__(name)
			else:
				name = cmds.scriptedPanelType(name, **kwargs)
				super(ScriptedPanelType, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_createCallback(self):
		""""""
		return self.query(createCallback=True)
	#----------------------------------------------------------------------
	def set_createCallback(self, value):
		""""""
		self.edit(createCallback=value)
	#----------------------------------------------------------------------
	createCallback = property(get_createCallback, set_createCallback)
	#----------------------------------------------------------------------
	def get_initCallback(self):
		""""""
		return self.query(initCallback=True)
	#----------------------------------------------------------------------
	def set_initCallback(self, value):
		""""""
		self.edit(initCallback=value)
	#----------------------------------------------------------------------
	initCallback = property(get_initCallback, set_initCallback)
	#----------------------------------------------------------------------
	def get_addCallback(self):
		""""""
		return self.query(addCallback=True)
	#----------------------------------------------------------------------
	def set_addCallback(self, value):
		""""""
		self.edit(addCallback=value)
	#----------------------------------------------------------------------
	addCallback = property(get_addCallback, set_addCallback)
	#----------------------------------------------------------------------
	def get_removeCallback(self):
		""""""
		return self.query(removeCallback=True)
	#----------------------------------------------------------------------
	def set_removeCallback(self, value):
		""""""
		self.edit(removeCallback=value)
	#----------------------------------------------------------------------
	removeCallback = property(get_removeCallback, set_removeCallback)
	#----------------------------------------------------------------------
	def get_deleteCallback(self):
		""""""
		return self.query(deleteCallback=True)
	#----------------------------------------------------------------------
	def set_deleteCallback(self, value):
		""""""
		self.edit(deleteCallback=value)
	#----------------------------------------------------------------------
	deleteCallback = property(get_deleteCallback, set_deleteCallback)
	#----------------------------------------------------------------------
	def get_saveStateCallback(self):
		""""""
		return self.query(saveStateCallback=True)
	#----------------------------------------------------------------------
	def set_saveStateCallback(self, value):
		""""""
		self.edit(saveStateCallback=value)
	#----------------------------------------------------------------------
	saveStateCallback = property(get_saveStateCallback, set_saveStateCallback)
	#----------------------------------------------------------------------
	def get_copyStateCallback(self):
		""""""
		return self.query(copyStateCallback=True)
	#----------------------------------------------------------------------
	def set_copyStateCallback(self, value):
		""""""
		self.edit(copyStateCallback=value)
	#----------------------------------------------------------------------
	copyStateCallback = property(get_copyStateCallback, set_copyStateCallback)
	#----------------------------------------------------------------------
	def get_unique(self):
		""""""
		return self.query(unique=True)
	#----------------------------------------------------------------------
	def set_unique(self, value):
		""""""
		self.edit(unique=value)
	#----------------------------------------------------------------------
	unique = property(get_unique, set_unique)
	#----------------------------------------------------------------------
	def get_obsolete(self):
		""""""
		return self.query(obsolete=True)
	#----------------------------------------------------------------------
	def set_obsolete(self, value):
		""""""
		self.edit(obsolete=value)
	#----------------------------------------------------------------------
	obsolete = property(get_obsolete, set_obsolete)
	#----------------------------------------------------------------------
	def get_retainOnFileOpen(self):
		""""""
		return self.query(retainOnFileOpen=True)
	#----------------------------------------------------------------------
	def set_retainOnFileOpen(self, value):
		""""""
		self.edit(retainOnFileOpen=value)
	#----------------------------------------------------------------------
	retainOnFileOpen = property(get_retainOnFileOpen, set_retainOnFileOpen)
	#----------------------------------------------------------------------
	def get_customView(self):
		""""""
		return self.query(customView=True)
	#----------------------------------------------------------------------
	def set_customView(self, value):
		""""""
		self.edit(customView=value)
	#----------------------------------------------------------------------
	customView = property(get_customView, set_customView)
########################################################################
class SetFocus(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setFocus(**kwargs)
			super(SetFocus, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setFocus(name, exists=True):
				super(SetFocus, self).__init__(name)
			else:
				name = cmds.setFocus(name, **kwargs)
				super(SetFocus, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_createCallback(self):
		""""""
		return self.query(createCallback=True)
	#----------------------------------------------------------------------
	def set_createCallback(self, value):
		""""""
		self.edit(createCallback=value)
	#----------------------------------------------------------------------
	createCallback = property(get_createCallback, set_createCallback)
	#----------------------------------------------------------------------
	def get_initCallback(self):
		""""""
		return self.query(initCallback=True)
	#----------------------------------------------------------------------
	def set_initCallback(self, value):
		""""""
		self.edit(initCallback=value)
	#----------------------------------------------------------------------
	initCallback = property(get_initCallback, set_initCallback)
	#----------------------------------------------------------------------
	def get_addCallback(self):
		""""""
		return self.query(addCallback=True)
	#----------------------------------------------------------------------
	def set_addCallback(self, value):
		""""""
		self.edit(addCallback=value)
	#----------------------------------------------------------------------
	addCallback = property(get_addCallback, set_addCallback)
	#----------------------------------------------------------------------
	def get_removeCallback(self):
		""""""
		return self.query(removeCallback=True)
	#----------------------------------------------------------------------
	def set_removeCallback(self, value):
		""""""
		self.edit(removeCallback=value)
	#----------------------------------------------------------------------
	removeCallback = property(get_removeCallback, set_removeCallback)
	#----------------------------------------------------------------------
	def get_deleteCallback(self):
		""""""
		return self.query(deleteCallback=True)
	#----------------------------------------------------------------------
	def set_deleteCallback(self, value):
		""""""
		self.edit(deleteCallback=value)
	#----------------------------------------------------------------------
	deleteCallback = property(get_deleteCallback, set_deleteCallback)
	#----------------------------------------------------------------------
	def get_saveStateCallback(self):
		""""""
		return self.query(saveStateCallback=True)
	#----------------------------------------------------------------------
	def set_saveStateCallback(self, value):
		""""""
		self.edit(saveStateCallback=value)
	#----------------------------------------------------------------------
	saveStateCallback = property(get_saveStateCallback, set_saveStateCallback)
	#----------------------------------------------------------------------
	def get_copyStateCallback(self):
		""""""
		return self.query(copyStateCallback=True)
	#----------------------------------------------------------------------
	def set_copyStateCallback(self, value):
		""""""
		self.edit(copyStateCallback=value)
	#----------------------------------------------------------------------
	copyStateCallback = property(get_copyStateCallback, set_copyStateCallback)
	#----------------------------------------------------------------------
	def get_unique(self):
		""""""
		return self.query(unique=True)
	#----------------------------------------------------------------------
	def set_unique(self, value):
		""""""
		self.edit(unique=value)
	#----------------------------------------------------------------------
	unique = property(get_unique, set_unique)
	#----------------------------------------------------------------------
	def get_obsolete(self):
		""""""
		return self.query(obsolete=True)
	#----------------------------------------------------------------------
	def set_obsolete(self, value):
		""""""
		self.edit(obsolete=value)
	#----------------------------------------------------------------------
	obsolete = property(get_obsolete, set_obsolete)
	#----------------------------------------------------------------------
	def get_retainOnFileOpen(self):
		""""""
		return self.query(retainOnFileOpen=True)
	#----------------------------------------------------------------------
	def set_retainOnFileOpen(self, value):
		""""""
		self.edit(retainOnFileOpen=value)
	#----------------------------------------------------------------------
	retainOnFileOpen = property(get_retainOnFileOpen, set_retainOnFileOpen)
	#----------------------------------------------------------------------
	def get_customView(self):
		""""""
		return self.query(customView=True)
	#----------------------------------------------------------------------
	def set_customView(self, value):
		""""""
		self.edit(customView=value)
	#----------------------------------------------------------------------
	customView = property(get_customView, set_customView)
########################################################################
class SpreadSheetEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.spreadSheetEditor(**kwargs)
			super(SpreadSheetEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.spreadSheetEditor(name, exists=True):
				super(SpreadSheetEditor, self).__init__(name)
			else:
				name = cmds.spreadSheetEditor(name, **kwargs)
				super(SpreadSheetEditor, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(unParent=value)
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
		self.edit(lockMainConnection=value)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	def unlockMainConnection(self,value):
		""""""
		self.edit(unlockMainConnection=value)
	#----------------------------------------------------------------------
	def updateMainConnection(self,value):
		""""""
		self.edit(updateMainConnection=value)
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
	def get_niceNames(self):
		""""""
		return self.query(niceNames=True)
	#----------------------------------------------------------------------
	def set_niceNames(self, value):
		""""""
		self.edit(niceNames=value)
	#----------------------------------------------------------------------
	niceNames = property(get_niceNames, set_niceNames)
	#----------------------------------------------------------------------
	def get_longNames(self):
		""""""
		return self.query(longNames=True)
	#----------------------------------------------------------------------
	def set_longNames(self, value):
		""""""
		self.edit(longNames=value)
	#----------------------------------------------------------------------
	longNames = property(get_longNames, set_longNames)
	#----------------------------------------------------------------------
	def get_precision(self):
		""""""
		return self.query(precision=True)
	#----------------------------------------------------------------------
	def set_precision(self, value):
		""""""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	precision = property(get_precision, set_precision)
	#----------------------------------------------------------------------
	def get_keyableOnly(self):
		""""""
		return self.query(keyableOnly=True)
	#----------------------------------------------------------------------
	def set_keyableOnly(self, value):
		""""""
		self.edit(keyableOnly=value)
	#----------------------------------------------------------------------
	keyableOnly = property(get_keyableOnly, set_keyableOnly)
	#----------------------------------------------------------------------
	def get_showShapes(self):
		""""""
		return self.query(showShapes=True)
	#----------------------------------------------------------------------
	def set_showShapes(self, value):
		""""""
		self.edit(showShapes=value)
	#----------------------------------------------------------------------
	showShapes = property(get_showShapes, set_showShapes)
	#----------------------------------------------------------------------
	def get_fixedAttrList(self):
		""""""
		return self.query(fixedAttrList=True)
	#----------------------------------------------------------------------
	def set_fixedAttrList(self, value):
		""""""
		self.edit(fixedAttrList=value)
	#----------------------------------------------------------------------
	fixedAttrList = property(get_fixedAttrList, set_fixedAttrList)
	#----------------------------------------------------------------------
	@property
	def selectedAttr(self):
		""""""
		return self.query(selectedAttr=True)
	#----------------------------------------------------------------------
	@property
	def allAttr(self):
		""""""
		return self.query(allAttr=True)
	#----------------------------------------------------------------------
	def get_attrRegExp(self):
		""""""
		return self.query(attrRegExp=True)
	#----------------------------------------------------------------------
	def set_attrRegExp(self, value):
		""""""
		self.edit(attrRegExp=value)
	#----------------------------------------------------------------------
	attrRegExp = property(get_attrRegExp, set_attrRegExp)
	#----------------------------------------------------------------------
	def execute(self,value):
		""""""
		self.edit(execute=value)
########################################################################
class ViewManip(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.viewManip(**kwargs)
			super(ViewManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.viewManip(name, exists=True):
				super(ViewManip, self).__init__(name)
			else:
				name = cmds.viewManip(name, **kwargs)
				super(ViewManip, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def visible(self):
		""""""
		return self.query(visible=True)
	#----------------------------------------------------------------------
	@property
	def topRight(self):
		""""""
		return self.query(topRight=True)
	#----------------------------------------------------------------------
	@property
	def bottomRight(self):
		""""""
		return self.query(bottomRight=True)
	#----------------------------------------------------------------------
	@property
	def topLeft(self):
		""""""
		return self.query(topLeft=True)
	#----------------------------------------------------------------------
	@property
	def bottomLeft(self):
		""""""
		return self.query(bottomLeft=True)
	#----------------------------------------------------------------------
	@property
	def size(self):
		""""""
		return self.query(size=True)
	#----------------------------------------------------------------------
	@property
	def minOpacity(self):
		""""""
		return self.query(minOpacity=True)
	#----------------------------------------------------------------------
	@property
	def dragSnap(self):
		""""""
		return self.query(dragSnap=True)
	#----------------------------------------------------------------------
	@property
	def zoomToFitScene(self):
		""""""
		return self.query(zoomToFitScene=True)
	#----------------------------------------------------------------------
	@property
	def drawCompass(self):
		""""""
		return self.query(drawCompass=True)
	#----------------------------------------------------------------------
	@property
	def compassAngle(self):
		""""""
		return self.query(compassAngle=True)
########################################################################
class Visor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.visor(**kwargs)
			super(Visor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.visor(name, exists=True):
				super(Visor, self).__init__(name)
			else:
				name = cmds.visor(name, **kwargs)
				super(Visor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def reset(self):
		""""""
		return self.query(reset=True)
	#----------------------------------------------------------------------
	@property
	def addFolder(self):
		""""""
		return self.query(addFolder=True)
	#----------------------------------------------------------------------
	@property
	def deleteFolder(self):
		""""""
		return self.query(deleteFolder=True)
	#----------------------------------------------------------------------
	@property
	def addNodes(self):
		""""""
		return self.query(addNodes=True)
	#----------------------------------------------------------------------
	@property
	def openFolder(self):
		""""""
		return self.query(openFolder=True)
	#----------------------------------------------------------------------
	@property
	def openDirectories(self):
		""""""
		return self.query(openDirectories=True)
	#----------------------------------------------------------------------
	@property
	def editFolder(self):
		""""""
		return self.query(editFolder=True)
	#----------------------------------------------------------------------
	@property
	def name(self):
		""""""
		return self.query(name=True)
	#----------------------------------------------------------------------
	@property
	def parent(self):
		""""""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	@property
	def command(self):
		""""""
		return self.query(command=True)
	#----------------------------------------------------------------------
	@property
	def transform(self):
		""""""
		return self.query(transform=True)
	#----------------------------------------------------------------------
	@property
	def nodeType(self):
		""""""
		return self.query(nodeType=True)
	#----------------------------------------------------------------------
	@property
	def path(self):
		""""""
		return self.query(path=True)
	#----------------------------------------------------------------------
	@property
	def rebuild(self):
		""""""
		return self.query(rebuild=True)
	#----------------------------------------------------------------------
	@property
	def scrollBar(self):
		""""""
		return self.query(scrollBar=True)
	#----------------------------------------------------------------------
	@property
	def stateString(self):
		""""""
		return self.query(stateString=True)
	#----------------------------------------------------------------------
	@property
	def scrollPercent(self):
		""""""
		return self.query(scrollPercent=True)
	#----------------------------------------------------------------------
	@property
	def type(self):
		""""""
		return self.query(type=True)
	#----------------------------------------------------------------------
	@property
	def menu(self):
		""""""
		return self.query(menu=True)
	#----------------------------------------------------------------------
	@property
	def style(self):
		""""""
		return self.query(style=True)
	#----------------------------------------------------------------------
	@property
	def allowZooming(self):
		""""""
		return self.query(allowZooming=True)
	#----------------------------------------------------------------------
	@property
	def allowPanningInX(self):
		""""""
		return self.query(allowPanningInX=True)
	#----------------------------------------------------------------------
	@property
	def allowPanningInY(self):
		""""""
		return self.query(allowPanningInY=True)
	#----------------------------------------------------------------------
	@property
	def showFolders(self):
		""""""
		return self.query(showFolders=True)
	#----------------------------------------------------------------------
	@property
	def showNodes(self):
		""""""
		return self.query(showNodes=True)
	#----------------------------------------------------------------------
	@property
	def showFiles(self):
		""""""
		return self.query(showFiles=True)
	#----------------------------------------------------------------------
	@property
	def showDividers(self):
		""""""
		return self.query(showDividers=True)
	#----------------------------------------------------------------------
	@property
	def popupMenuScript(self):
		""""""
		return self.query(popupMenuScript=True)
	#----------------------------------------------------------------------
	@property
	def selectedGadgets(self):
		""""""
		return self.query(selectedGadgets=True)
	#----------------------------------------------------------------------
	@property
	def folderList(self):
		""""""
		return self.query(folderList=True)
	#----------------------------------------------------------------------
	@property
	def restrictPanAndZoom(self):
		""""""
		return self.query(restrictPanAndZoom=True)
	#----------------------------------------------------------------------
	@property
	def saveSwatches(self):
		""""""
		return self.query(saveSwatches=True)
	#----------------------------------------------------------------------
	@property
	def refreshAllSwatches(self):
		""""""
		return self.query(refreshAllSwatches=True)
	#----------------------------------------------------------------------
	@property
	def refreshSelectedSwatches(self):
		""""""
		return self.query(refreshSelectedSwatches=True)
	#----------------------------------------------------------------------
	@property
	def refreshSwatch(self):
		""""""
		return self.query(refreshSwatch=True)
########################################################################
class WebBrowser(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if "qtParent" in kwargs:
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.webBrowser(**kwargs)
			super(WebBrowser, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.webBrowser(name, exists=True):
				super(WebBrowser, self).__init__(name)
			else:
				name = cmds.webBrowser(name, **kwargs)
				super(WebBrowser, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def parent(self):
		""""""
		return self.query(parent=True)
	#----------------------------------------------------------------------
	def get_enable(self):
		""""""
		return self.query(enable=True)
	#----------------------------------------------------------------------
	def set_enable(self, value):
		""""""
		self.edit(enable=value)
	#----------------------------------------------------------------------
	enable = property(get_enable, set_enable)
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
	def get_visibleChangeCommand(self):
		""""""
		return self.query(visibleChangeCommand=True)
	#----------------------------------------------------------------------
	def set_visibleChangeCommand(self, value):
		""""""
		self.edit(visibleChangeCommand=value)
	#----------------------------------------------------------------------
	visibleChangeCommand = property(get_visibleChangeCommand, set_visibleChangeCommand)
	#----------------------------------------------------------------------
	@property
	def isObscured(self):
		""""""
		return self.query(isObscured=True)
	#----------------------------------------------------------------------
	def get_manage(self):
		""""""
		return self.query(manage=True)
	#----------------------------------------------------------------------
	def set_manage(self, value):
		""""""
		self.edit(manage=value)
	#----------------------------------------------------------------------
	manage = property(get_manage, set_manage)
	#----------------------------------------------------------------------
	@property
	def numberOfPopupMenus(self):
		""""""
		return self.query(numberOfPopupMenus=True)
	#----------------------------------------------------------------------
	@property
	def popupMenuArray(self):
		""""""
		return self.query(popupMenuArray=True)
	#----------------------------------------------------------------------
	def get_preventOverride(self):
		""""""
		return self.query(preventOverride=True)
	#----------------------------------------------------------------------
	def set_preventOverride(self, value):
		""""""
		self.edit(preventOverride=value)
	#----------------------------------------------------------------------
	preventOverride = property(get_preventOverride, set_preventOverride)
	#----------------------------------------------------------------------
	def get_annotation(self):
		""""""
		return self.query(annotation=True)
	#----------------------------------------------------------------------
	def set_annotation(self, value):
		""""""
		self.edit(annotation=value)
	#----------------------------------------------------------------------
	annotation = property(get_annotation, set_annotation)
	#----------------------------------------------------------------------
	def get_backgroundColor(self):
		""""""
		return self.query(backgroundColor=True)
	#----------------------------------------------------------------------
	def set_backgroundColor(self, value):
		""""""
		self.edit(backgroundColor=value)
	#----------------------------------------------------------------------
	backgroundColor = property(get_backgroundColor, set_backgroundColor)
	#----------------------------------------------------------------------
	def noBackground(self,value):
		""""""
		self.edit(noBackground=value)
	#----------------------------------------------------------------------
	def get_enableBackground(self):
		""""""
		return self.query(enableBackground=True)
	#----------------------------------------------------------------------
	def set_enableBackground(self, value):
		""""""
		self.edit(enableBackground=value)
	#----------------------------------------------------------------------
	enableBackground = property(get_enableBackground, set_enableBackground)
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
	def dragCallback(self,value):
		""""""
		self.edit(dragCallback=value)
	#----------------------------------------------------------------------
	def dropCallback(self,value):
		""""""
		self.edit(dropCallback=value)
	#----------------------------------------------------------------------
	@property
	def fullPathName(self):
		""""""
		return self.query(fullPathName=True)