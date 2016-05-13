__all__ = ["Window", "Editor", "ProgressWindow", "PromptDialog"]
import maya.cmds as cmds
import UI_Object


########################################################################
class ColorEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.colorEditor(**kwargs)
			super(ColorEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.colorEditor(name, exists=True):
				super(ColorEditor, self).__init__(name)
			else:
				name = cmds.colorEditor(name, **kwargs)
				super(ColorEditor, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def rgbValue(self):
		""""""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	@property
	def hsvValue(self):
		""""""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	@property
	def result(self):
		""""""
		return self.query(result=True)
########################################################################
class ConfirmDialog(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.confirmDialog(**kwargs)
			super(ConfirmDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.confirmDialog(name, exists=True):
				super(ConfirmDialog, self).__init__(name)
			else:
				name = cmds.confirmDialog(name, **kwargs)
				super(ConfirmDialog, self).__init__(name, **dict(qtParent=parent))
########################################################################
class CreateEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.createEditor(**kwargs)
			super(CreateEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.createEditor(name, exists=True):
				super(CreateEditor, self).__init__(name)
			else:
				name = cmds.createEditor(name, **kwargs)
				super(CreateEditor, self).__init__(name, **dict(qtParent=parent))
########################################################################
class DefaultNavigation(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.defaultNavigation(**kwargs)
			super(DefaultNavigation, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.defaultNavigation(name, exists=True):
				super(DefaultNavigation, self).__init__(name)
			else:
				name = cmds.defaultNavigation(name, **kwargs)
				super(DefaultNavigation, self).__init__(name, **dict(qtParent=parent))
########################################################################
class Editor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.editor(**kwargs)
			super(Editor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.editor(name, exists=True):
				super(Editor, self).__init__(name)
			else:
				name = cmds.editor(name, **kwargs)
				super(Editor, self).__init__(name, **dict(qtParent=parent))
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
########################################################################
class EditorTemplate(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.editorTemplate(**kwargs)
			super(EditorTemplate, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.editorTemplate(name, exists=True):
				super(EditorTemplate, self).__init__(name)
			else:
				name = cmds.editorTemplate(name, **kwargs)
				super(EditorTemplate, self).__init__(name, **dict(qtParent=parent))
########################################################################
class FontDialog(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.fontDialog(**kwargs)
			super(FontDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.fontDialog(name, exists=True):
				super(FontDialog, self).__init__(name)
			else:
				name = cmds.fontDialog(name, **kwargs)
				super(FontDialog, self).__init__(name, **dict(qtParent=parent))
########################################################################
class LayoutDialog(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.layoutDialog(**kwargs)
			super(LayoutDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.layoutDialog(name, exists=True):
				super(LayoutDialog, self).__init__(name)
			else:
				name = cmds.layoutDialog(name, **kwargs)
				super(LayoutDialog, self).__init__(name, **dict(qtParent=parent))
########################################################################
class MinimizeApp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.minimizeApp(**kwargs)
			super(MinimizeApp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.minimizeApp(name, exists=True):
				super(MinimizeApp, self).__init__(name)
			else:
				name = cmds.minimizeApp(name, **kwargs)
				super(MinimizeApp, self).__init__(name, **dict(qtParent=parent))
########################################################################
class ProgressWindow(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.progressWindow(**kwargs)
			super(ProgressWindow, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.progressWindow(name, exists=True):
				super(ProgressWindow, self).__init__(name)
			else:
				name = cmds.progressWindow(name, **kwargs)
				super(ProgressWindow, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def isCancelled(self):
		""""""
		return self.query(isCancelled=True)
	#----------------------------------------------------------------------
	def get_progress(self):
		""""""
		return self.query(progress=True)
	#----------------------------------------------------------------------
	def set_progress(self, value):
		""""""
		self.edit(progress=value)
	#----------------------------------------------------------------------
	progress = property(get_progress, set_progress)
	#----------------------------------------------------------------------
	def step(self,value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	def get_minValue(self):
		""""""
		return self.query(minValue=True)
	#----------------------------------------------------------------------
	def set_minValue(self, value):
		""""""
		self.edit(minValue=value)
	#----------------------------------------------------------------------
	minValue = property(get_minValue, set_minValue)
	#----------------------------------------------------------------------
	def get_maxValue(self):
		""""""
		return self.query(maxValue=True)
	#----------------------------------------------------------------------
	def set_maxValue(self, value):
		""""""
		self.edit(maxValue=value)
	#----------------------------------------------------------------------
	maxValue = property(get_maxValue, set_maxValue)
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
	def get_status(self):
		""""""
		return self.query(status=True)
	#----------------------------------------------------------------------
	def set_status(self, value):
		""""""
		self.edit(status=value)
	#----------------------------------------------------------------------
	status = property(get_status, set_status)
	#----------------------------------------------------------------------
	def get_isInterruptable(self):
		""""""
		return self.query(isInterruptable=True)
	#----------------------------------------------------------------------
	def set_isInterruptable(self, value):
		""""""
		self.edit(isInterruptable=value)
	#----------------------------------------------------------------------
	isInterruptable = property(get_isInterruptable, set_isInterruptable)
########################################################################
class PromptDialog(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.promptDialog(**kwargs)
			super(PromptDialog, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.promptDialog(name, exists=True):
				super(PromptDialog, self).__init__(name)
			else:
				name = cmds.promptDialog(name, **kwargs)
				super(PromptDialog, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def text(self):
		""""""
		return self.query(text=True)
########################################################################
class RefreshEditorTemplates(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.refreshEditorTemplates(**kwargs)
			super(RefreshEditorTemplates, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.refreshEditorTemplates(name, exists=True):
				super(RefreshEditorTemplates, self).__init__(name)
			else:
				name = cmds.refreshEditorTemplates(name, **kwargs)
				super(RefreshEditorTemplates, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def text(self):
		""""""
		return self.query(text=True)
########################################################################
class ScriptEditorInfo(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scriptEditorInfo(**kwargs)
			super(ScriptEditorInfo, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scriptEditorInfo(name, exists=True):
				super(ScriptEditorInfo, self).__init__(name)
			else:
				name = cmds.scriptEditorInfo(name, **kwargs)
				super(ScriptEditorInfo, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def clearHistory(self,value):
		""""""
		self.edit(clearHistory=value)
	#----------------------------------------------------------------------
	def input(self,value):
		""""""
		self.edit(input=value)
	#----------------------------------------------------------------------
	def get_historyFilename(self):
		""""""
		return self.query(historyFilename=True)
	#----------------------------------------------------------------------
	def set_historyFilename(self, value):
		""""""
		self.edit(historyFilename=value)
	#----------------------------------------------------------------------
	historyFilename = property(get_historyFilename, set_historyFilename)
	#----------------------------------------------------------------------
	def get_writeHistory(self):
		""""""
		return self.query(writeHistory=True)
	#----------------------------------------------------------------------
	def set_writeHistory(self, value):
		""""""
		self.edit(writeHistory=value)
	#----------------------------------------------------------------------
	writeHistory = property(get_writeHistory, set_writeHistory)
	#----------------------------------------------------------------------
	def clearHistoryFile(self,value):
		""""""
		self.edit(clearHistoryFile=value)
	#----------------------------------------------------------------------
	def get_suppressErrors(self):
		""""""
		return self.query(suppressErrors=True)
	#----------------------------------------------------------------------
	def set_suppressErrors(self, value):
		""""""
		self.edit(suppressErrors=value)
	#----------------------------------------------------------------------
	suppressErrors = property(get_suppressErrors, set_suppressErrors)
	#----------------------------------------------------------------------
	def get_suppressWarnings(self):
		""""""
		return self.query(suppressWarnings=True)
	#----------------------------------------------------------------------
	def set_suppressWarnings(self, value):
		""""""
		self.edit(suppressWarnings=value)
	#----------------------------------------------------------------------
	suppressWarnings = property(get_suppressWarnings, set_suppressWarnings)
	#----------------------------------------------------------------------
	def get_suppressInfo(self):
		""""""
		return self.query(suppressInfo=True)
	#----------------------------------------------------------------------
	def set_suppressInfo(self, value):
		""""""
		self.edit(suppressInfo=value)
	#----------------------------------------------------------------------
	suppressInfo = property(get_suppressInfo, set_suppressInfo)
	#----------------------------------------------------------------------
	def get_suppressResults(self):
		""""""
		return self.query(suppressResults=True)
	#----------------------------------------------------------------------
	def set_suppressResults(self, value):
		""""""
		self.edit(suppressResults=value)
	#----------------------------------------------------------------------
	suppressResults = property(get_suppressResults, set_suppressResults)
	#----------------------------------------------------------------------
	def get_suppressStackWindow(self):
		""""""
		return self.query(suppressStackWindow=True)
	#----------------------------------------------------------------------
	def set_suppressStackWindow(self, value):
		""""""
		self.edit(suppressStackWindow=value)
	#----------------------------------------------------------------------
	suppressStackWindow = property(get_suppressStackWindow, set_suppressStackWindow)
########################################################################
class ShowSelectionInTitle(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.showSelectionInTitle(**kwargs)
			super(ShowSelectionInTitle, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.showSelectionInTitle(name, exists=True):
				super(ShowSelectionInTitle, self).__init__(name)
			else:
				name = cmds.showSelectionInTitle(name, **kwargs)
				super(ShowSelectionInTitle, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def clearHistory(self,value):
		""""""
		self.edit(clearHistory=value)
	#----------------------------------------------------------------------
	def input(self,value):
		""""""
		self.edit(input=value)
	#----------------------------------------------------------------------
	def get_historyFilename(self):
		""""""
		return self.query(historyFilename=True)
	#----------------------------------------------------------------------
	def set_historyFilename(self, value):
		""""""
		self.edit(historyFilename=value)
	#----------------------------------------------------------------------
	historyFilename = property(get_historyFilename, set_historyFilename)
	#----------------------------------------------------------------------
	def get_writeHistory(self):
		""""""
		return self.query(writeHistory=True)
	#----------------------------------------------------------------------
	def set_writeHistory(self, value):
		""""""
		self.edit(writeHistory=value)
	#----------------------------------------------------------------------
	writeHistory = property(get_writeHistory, set_writeHistory)
	#----------------------------------------------------------------------
	def clearHistoryFile(self,value):
		""""""
		self.edit(clearHistoryFile=value)
	#----------------------------------------------------------------------
	def get_suppressErrors(self):
		""""""
		return self.query(suppressErrors=True)
	#----------------------------------------------------------------------
	def set_suppressErrors(self, value):
		""""""
		self.edit(suppressErrors=value)
	#----------------------------------------------------------------------
	suppressErrors = property(get_suppressErrors, set_suppressErrors)
	#----------------------------------------------------------------------
	def get_suppressWarnings(self):
		""""""
		return self.query(suppressWarnings=True)
	#----------------------------------------------------------------------
	def set_suppressWarnings(self, value):
		""""""
		self.edit(suppressWarnings=value)
	#----------------------------------------------------------------------
	suppressWarnings = property(get_suppressWarnings, set_suppressWarnings)
	#----------------------------------------------------------------------
	def get_suppressInfo(self):
		""""""
		return self.query(suppressInfo=True)
	#----------------------------------------------------------------------
	def set_suppressInfo(self, value):
		""""""
		self.edit(suppressInfo=value)
	#----------------------------------------------------------------------
	suppressInfo = property(get_suppressInfo, set_suppressInfo)
	#----------------------------------------------------------------------
	def get_suppressResults(self):
		""""""
		return self.query(suppressResults=True)
	#----------------------------------------------------------------------
	def set_suppressResults(self, value):
		""""""
		self.edit(suppressResults=value)
	#----------------------------------------------------------------------
	suppressResults = property(get_suppressResults, set_suppressResults)
	#----------------------------------------------------------------------
	def get_suppressStackWindow(self):
		""""""
		return self.query(suppressStackWindow=True)
	#----------------------------------------------------------------------
	def set_suppressStackWindow(self, value):
		""""""
		self.edit(suppressStackWindow=value)
	#----------------------------------------------------------------------
	suppressStackWindow = property(get_suppressStackWindow, set_suppressStackWindow)
########################################################################
class ShowWindow(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.showWindow(**kwargs)
			super(ShowWindow, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.showWindow(name, exists=True):
				super(ShowWindow, self).__init__(name)
			else:
				name = cmds.showWindow(name, **kwargs)
				super(ShowWindow, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def clearHistory(self,value):
		""""""
		self.edit(clearHistory=value)
	#----------------------------------------------------------------------
	def input(self,value):
		""""""
		self.edit(input=value)
	#----------------------------------------------------------------------
	def get_historyFilename(self):
		""""""
		return self.query(historyFilename=True)
	#----------------------------------------------------------------------
	def set_historyFilename(self, value):
		""""""
		self.edit(historyFilename=value)
	#----------------------------------------------------------------------
	historyFilename = property(get_historyFilename, set_historyFilename)
	#----------------------------------------------------------------------
	def get_writeHistory(self):
		""""""
		return self.query(writeHistory=True)
	#----------------------------------------------------------------------
	def set_writeHistory(self, value):
		""""""
		self.edit(writeHistory=value)
	#----------------------------------------------------------------------
	writeHistory = property(get_writeHistory, set_writeHistory)
	#----------------------------------------------------------------------
	def clearHistoryFile(self,value):
		""""""
		self.edit(clearHistoryFile=value)
	#----------------------------------------------------------------------
	def get_suppressErrors(self):
		""""""
		return self.query(suppressErrors=True)
	#----------------------------------------------------------------------
	def set_suppressErrors(self, value):
		""""""
		self.edit(suppressErrors=value)
	#----------------------------------------------------------------------
	suppressErrors = property(get_suppressErrors, set_suppressErrors)
	#----------------------------------------------------------------------
	def get_suppressWarnings(self):
		""""""
		return self.query(suppressWarnings=True)
	#----------------------------------------------------------------------
	def set_suppressWarnings(self, value):
		""""""
		self.edit(suppressWarnings=value)
	#----------------------------------------------------------------------
	suppressWarnings = property(get_suppressWarnings, set_suppressWarnings)
	#----------------------------------------------------------------------
	def get_suppressInfo(self):
		""""""
		return self.query(suppressInfo=True)
	#----------------------------------------------------------------------
	def set_suppressInfo(self, value):
		""""""
		self.edit(suppressInfo=value)
	#----------------------------------------------------------------------
	suppressInfo = property(get_suppressInfo, set_suppressInfo)
	#----------------------------------------------------------------------
	def get_suppressResults(self):
		""""""
		return self.query(suppressResults=True)
	#----------------------------------------------------------------------
	def set_suppressResults(self, value):
		""""""
		self.edit(suppressResults=value)
	#----------------------------------------------------------------------
	suppressResults = property(get_suppressResults, set_suppressResults)
	#----------------------------------------------------------------------
	def get_suppressStackWindow(self):
		""""""
		return self.query(suppressStackWindow=True)
	#----------------------------------------------------------------------
	def set_suppressStackWindow(self, value):
		""""""
		self.edit(suppressStackWindow=value)
	#----------------------------------------------------------------------
	suppressStackWindow = property(get_suppressStackWindow, set_suppressStackWindow)
########################################################################
class ToggleWindowVisibility(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toggleWindowVisibility(**kwargs)
			super(ToggleWindowVisibility, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toggleWindowVisibility(name, exists=True):
				super(ToggleWindowVisibility, self).__init__(name)
			else:
				name = cmds.toggleWindowVisibility(name, **kwargs)
				super(ToggleWindowVisibility, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def clearHistory(self,value):
		""""""
		self.edit(clearHistory=value)
	#----------------------------------------------------------------------
	def input(self,value):
		""""""
		self.edit(input=value)
	#----------------------------------------------------------------------
	def get_historyFilename(self):
		""""""
		return self.query(historyFilename=True)
	#----------------------------------------------------------------------
	def set_historyFilename(self, value):
		""""""
		self.edit(historyFilename=value)
	#----------------------------------------------------------------------
	historyFilename = property(get_historyFilename, set_historyFilename)
	#----------------------------------------------------------------------
	def get_writeHistory(self):
		""""""
		return self.query(writeHistory=True)
	#----------------------------------------------------------------------
	def set_writeHistory(self, value):
		""""""
		self.edit(writeHistory=value)
	#----------------------------------------------------------------------
	writeHistory = property(get_writeHistory, set_writeHistory)
	#----------------------------------------------------------------------
	def clearHistoryFile(self,value):
		""""""
		self.edit(clearHistoryFile=value)
	#----------------------------------------------------------------------
	def get_suppressErrors(self):
		""""""
		return self.query(suppressErrors=True)
	#----------------------------------------------------------------------
	def set_suppressErrors(self, value):
		""""""
		self.edit(suppressErrors=value)
	#----------------------------------------------------------------------
	suppressErrors = property(get_suppressErrors, set_suppressErrors)
	#----------------------------------------------------------------------
	def get_suppressWarnings(self):
		""""""
		return self.query(suppressWarnings=True)
	#----------------------------------------------------------------------
	def set_suppressWarnings(self, value):
		""""""
		self.edit(suppressWarnings=value)
	#----------------------------------------------------------------------
	suppressWarnings = property(get_suppressWarnings, set_suppressWarnings)
	#----------------------------------------------------------------------
	def get_suppressInfo(self):
		""""""
		return self.query(suppressInfo=True)
	#----------------------------------------------------------------------
	def set_suppressInfo(self, value):
		""""""
		self.edit(suppressInfo=value)
	#----------------------------------------------------------------------
	suppressInfo = property(get_suppressInfo, set_suppressInfo)
	#----------------------------------------------------------------------
	def get_suppressResults(self):
		""""""
		return self.query(suppressResults=True)
	#----------------------------------------------------------------------
	def set_suppressResults(self, value):
		""""""
		self.edit(suppressResults=value)
	#----------------------------------------------------------------------
	suppressResults = property(get_suppressResults, set_suppressResults)
	#----------------------------------------------------------------------
	def get_suppressStackWindow(self):
		""""""
		return self.query(suppressStackWindow=True)
	#----------------------------------------------------------------------
	def set_suppressStackWindow(self, value):
		""""""
		self.edit(suppressStackWindow=value)
	#----------------------------------------------------------------------
	suppressStackWindow = property(get_suppressStackWindow, set_suppressStackWindow)
########################################################################
class Window(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.window(**kwargs)
			super(Window, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.window(name, exists=True):
				super(Window, self).__init__(name)
			else:
				name = cmds.window(name, **kwargs)
				super(Window, self).__init__(name, **dict(qtParent=parent))
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
		self.edit(backgroundColor=value)
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
		self.edit(minimizeCommand=value)
	#----------------------------------------------------------------------
	def restoreCommand(self,value):
		""""""
		self.edit(restoreCommand=value)
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
		self.edit(menuIndex=value)
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
class WindowPref(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.windowPref(**kwargs)
			super(WindowPref, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.windowPref(name, exists=True):
				super(WindowPref, self).__init__(name)
			else:
				name = cmds.windowPref(name, **kwargs)
				super(WindowPref, self).__init__(name, **dict(qtParent=parent))
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
	def get_maximized(self):
		""""""
		return self.query(maximized=True)
	#----------------------------------------------------------------------
	def set_maximized(self, value):
		""""""
		self.edit(maximized=value)
	#----------------------------------------------------------------------
	maximized = property(get_maximized, set_maximized)
	#----------------------------------------------------------------------
	@property
	def parentMain(self):
		""""""
		return self.query(parentMain=True)
	#----------------------------------------------------------------------
	@property
	def enableAll(self):
		""""""
		return self.query(enableAll=True)