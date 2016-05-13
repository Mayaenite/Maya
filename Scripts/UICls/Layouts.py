__all__ = ["ColumnLayout", "DockControl", "FlowLayout", "FormLayout", "FrameLayout", "GridLayout", "Layout", "MenuBarLayout", "PaneLayout", "RowColumnLayout", "RowLayout", "ScrollLayout", "ShelfLayout", "ShelfTabLayout", "TabLayout", "ToolBar"]
import maya.cmds as cmds
import UI_Object


########################################################################
class ColumnLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.columnLayout(**kwargs)
			super(ColumnLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.columnLayout(name, exists=True):
				super(ColumnLayout, self).__init__(name)
			else:
				name = cmds.columnLayout(name, **kwargs)
				super(ColumnLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def adjustableColumn(self,value):
		""""""
		self.edit(adjustableColumn=value)
	#----------------------------------------------------------------------
	def columnAlign(self,value):
		""""""
		self.edit(columnAlign=value)
	#----------------------------------------------------------------------
	def columnAttach(self,value):
		""""""
		self.edit(columnAttach=value)
	#----------------------------------------------------------------------
	def columnOffset(self,value):
		""""""
		self.edit(columnOffset=value)
	#----------------------------------------------------------------------
	def get_columnWidth(self):
		""""""
		return self.query(columnWidth=True)
	#----------------------------------------------------------------------
	def set_columnWidth(self, value):
		""""""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	columnWidth = property(get_columnWidth, set_columnWidth)
	#----------------------------------------------------------------------
	def get_rowSpacing(self):
		""""""
		return self.query(rowSpacing=True)
	#----------------------------------------------------------------------
	def set_rowSpacing(self, value):
		""""""
		self.edit(rowSpacing=value)
	#----------------------------------------------------------------------
	rowSpacing = property(get_rowSpacing, set_rowSpacing)
########################################################################
class DockControl(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.dockControl(**kwargs)
			super(DockControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.dockControl(name, exists=True):
				super(DockControl, self).__init__(name)
			else:
				name = cmds.dockControl(name, **kwargs)
				super(DockControl, self).__init__(name, **dict(qtParent=parent))
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
	def get_allowedArea(self):
		""""""
		return self.query(allowedArea=True)
	#----------------------------------------------------------------------
	def set_allowedArea(self, value):
		""""""
		self.edit(allowedArea=value)
	#----------------------------------------------------------------------
	allowedArea = property(get_allowedArea, set_allowedArea)
	#----------------------------------------------------------------------
	def get_floating(self):
		""""""
		return self.query(floating=True)
	#----------------------------------------------------------------------
	def set_floating(self, value):
		""""""
		self.edit(floating=value)
	#----------------------------------------------------------------------
	floating = property(get_floating, set_floating)
	#----------------------------------------------------------------------
	def floatChangeCommand(self,value):
		""""""
		self.edit(floatChangeCommand=value)
	#----------------------------------------------------------------------
	def get_area(self):
		""""""
		return self.query(area=True)
	#----------------------------------------------------------------------
	def set_area(self, value):
		""""""
		self.edit(area=value)
	#----------------------------------------------------------------------
	area = property(get_area, set_area)
	#----------------------------------------------------------------------
	@property
	def content(self):
		""""""
		return self.query(content=True)
	#----------------------------------------------------------------------
	def get_enablePopupOption(self):
		""""""
		return self.query(enablePopupOption=True)
	#----------------------------------------------------------------------
	def set_enablePopupOption(self, value):
		""""""
		self.edit(enablePopupOption=value)
	#----------------------------------------------------------------------
	enablePopupOption = property(get_enablePopupOption, set_enablePopupOption)
	#----------------------------------------------------------------------
	def get_r(self):
		""""""
		return self.query(r=True)
	#----------------------------------------------------------------------
	def set_r(self, value):
		""""""
		self.edit(r=value)
	#----------------------------------------------------------------------
	r = property(get_r, set_r)
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
########################################################################
class FlowLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.flowLayout(**kwargs)
			super(FlowLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.flowLayout(name, exists=True):
				super(FlowLayout, self).__init__(name)
			else:
				name = cmds.flowLayout(name, **kwargs)
				super(FlowLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_columnSpacing(self):
		""""""
		return self.query(columnSpacing=True)
	#----------------------------------------------------------------------
	def set_columnSpacing(self, value):
		""""""
		self.edit(columnSpacing=value)
	#----------------------------------------------------------------------
	columnSpacing = property(get_columnSpacing, set_columnSpacing)
	#----------------------------------------------------------------------
	@property
	def vertical(self):
		""""""
		return self.query(vertical=True)
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
########################################################################
class FormLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.formLayout(**kwargs)
			super(FormLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.formLayout(name, exists=True):
				super(FormLayout, self).__init__(name)
			else:
				name = cmds.formLayout(name, **kwargs)
				super(FormLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_numberOfDivisions(self):
		""""""
		return self.query(numberOfDivisions=True)
	#----------------------------------------------------------------------
	def set_numberOfDivisions(self, value):
		""""""
		self.edit(numberOfDivisions=value)
	#----------------------------------------------------------------------
	numberOfDivisions = property(get_numberOfDivisions, set_numberOfDivisions)
	#----------------------------------------------------------------------
	def attachForm(self,value):
		""""""
		self.edit(attachForm=value)
	#----------------------------------------------------------------------
	def attachOppositeForm(self,value):
		""""""
		self.edit(attachOppositeForm=value)
	#----------------------------------------------------------------------
	def attachControl(self,value):
		""""""
		self.edit(attachControl=value)
	#----------------------------------------------------------------------
	def attachOppositeControl(self,value):
		""""""
		self.edit(attachOppositeControl=value)
	#----------------------------------------------------------------------
	def attachPosition(self,value):
		""""""
		self.edit(attachPosition=value)
	#----------------------------------------------------------------------
	def attachNone(self,value):
		""""""
		self.edit(attachNone=value)
########################################################################
class FrameLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.frameLayout(**kwargs)
			super(FrameLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.frameLayout(name, exists=True):
				super(FrameLayout, self).__init__(name)
			else:
				name = cmds.frameLayout(name, **kwargs)
				super(FrameLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_borderVisible(self):
		""""""
		return self.query(borderVisible=True)
	#----------------------------------------------------------------------
	def set_borderVisible(self, value):
		""""""
		self.edit(borderVisible=value)
	#----------------------------------------------------------------------
	borderVisible = property(get_borderVisible, set_borderVisible)
	#----------------------------------------------------------------------
	def get_borderStyle(self):
		""""""
		return self.query(borderStyle=True)
	#----------------------------------------------------------------------
	def set_borderStyle(self, value):
		""""""
		self.edit(borderStyle=value)
	#----------------------------------------------------------------------
	borderStyle = property(get_borderStyle, set_borderStyle)
	#----------------------------------------------------------------------
	def get_collapse(self):
		""""""
		return self.query(collapse=True)
	#----------------------------------------------------------------------
	def set_collapse(self, value):
		""""""
		self.edit(collapse=value)
	#----------------------------------------------------------------------
	collapse = property(get_collapse, set_collapse)
	#----------------------------------------------------------------------
	def get_collapsable(self):
		""""""
		return self.query(collapsable=True)
	#----------------------------------------------------------------------
	def set_collapsable(self, value):
		""""""
		self.edit(collapsable=value)
	#----------------------------------------------------------------------
	collapsable = property(get_collapsable, set_collapsable)
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
	def get_labelVisible(self):
		""""""
		return self.query(labelVisible=True)
	#----------------------------------------------------------------------
	def set_labelVisible(self, value):
		""""""
		self.edit(labelVisible=value)
	#----------------------------------------------------------------------
	labelVisible = property(get_labelVisible, set_labelVisible)
	#----------------------------------------------------------------------
	def get_labelIndent(self):
		""""""
		return self.query(labelIndent=True)
	#----------------------------------------------------------------------
	def set_labelIndent(self, value):
		""""""
		self.edit(labelIndent=value)
	#----------------------------------------------------------------------
	labelIndent = property(get_labelIndent, set_labelIndent)
	#----------------------------------------------------------------------
	def get_font(self):
		""""""
		return self.query(font=True)
	#----------------------------------------------------------------------
	def set_font(self, value):
		""""""
		self.edit(font=value)
	#----------------------------------------------------------------------
	font = property(get_font, set_font)
	#----------------------------------------------------------------------
	def get_marginHeight(self):
		""""""
		return self.query(marginHeight=True)
	#----------------------------------------------------------------------
	def set_marginHeight(self, value):
		""""""
		self.edit(marginHeight=value)
	#----------------------------------------------------------------------
	marginHeight = property(get_marginHeight, set_marginHeight)
	#----------------------------------------------------------------------
	def get_marginWidth(self):
		""""""
		return self.query(marginWidth=True)
	#----------------------------------------------------------------------
	def set_marginWidth(self, value):
		""""""
		self.edit(marginWidth=value)
	#----------------------------------------------------------------------
	marginWidth = property(get_marginWidth, set_marginWidth)
	#----------------------------------------------------------------------
	def collapseCommand(self,value):
		""""""
		self.edit(collapseCommand=value)
	#----------------------------------------------------------------------
	def expandCommand(self,value):
		""""""
		self.edit(expandCommand=value)
	#----------------------------------------------------------------------
	def preCollapseCommand(self,value):
		""""""
		self.edit(preCollapseCommand=value)
	#----------------------------------------------------------------------
	def preExpandCommand(self,value):
		""""""
		self.edit(preExpandCommand=value)
########################################################################
class GridLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.gridLayout(**kwargs)
			super(GridLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.gridLayout(name, exists=True):
				super(GridLayout, self).__init__(name)
			else:
				name = cmds.gridLayout(name, **kwargs)
				super(GridLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	@property
	def columnsResizable(self):
		""""""
		return self.query(columnsResizable=True)
	#----------------------------------------------------------------------
	@property
	def allowEmptyCells(self):
		""""""
		return self.query(allowEmptyCells=True)
	#----------------------------------------------------------------------
	@property
	def autoGrow(self):
		""""""
		return self.query(autoGrow=True)
	#----------------------------------------------------------------------
	def numberOfRowsColumns(self,value):
		""""""
		self.edit(numberOfRowsColumns=value)
	#----------------------------------------------------------------------
	def get_numberOfRows(self):
		""""""
		return self.query(numberOfRows=True)
	#----------------------------------------------------------------------
	def set_numberOfRows(self, value):
		""""""
		self.edit(numberOfRows=value)
	#----------------------------------------------------------------------
	numberOfRows = property(get_numberOfRows, set_numberOfRows)
	#----------------------------------------------------------------------
	def get_numberOfColumns(self):
		""""""
		return self.query(numberOfColumns=True)
	#----------------------------------------------------------------------
	def set_numberOfColumns(self, value):
		""""""
		self.edit(numberOfColumns=value)
	#----------------------------------------------------------------------
	numberOfColumns = property(get_numberOfColumns, set_numberOfColumns)
	#----------------------------------------------------------------------
	def cellWidthHeight(self,value):
		""""""
		self.edit(cellWidthHeight=value)
	#----------------------------------------------------------------------
	def get_cellWidth(self):
		""""""
		return self.query(cellWidth=True)
	#----------------------------------------------------------------------
	def set_cellWidth(self, value):
		""""""
		self.edit(cellWidth=value)
	#----------------------------------------------------------------------
	cellWidth = property(get_cellWidth, set_cellWidth)
	#----------------------------------------------------------------------
	def get_cellHeight(self):
		""""""
		return self.query(cellHeight=True)
	#----------------------------------------------------------------------
	def set_cellHeight(self, value):
		""""""
		self.edit(cellHeight=value)
	#----------------------------------------------------------------------
	cellHeight = property(get_cellHeight, set_cellHeight)
	#----------------------------------------------------------------------
	@property
	def gridOrder(self):
		""""""
		return self.query(gridOrder=True)
	#----------------------------------------------------------------------
	def position(self,value):
		""""""
		self.edit(position=value)
########################################################################
class Layout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.layout(**kwargs)
			super(Layout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.layout(name, exists=True):
				super(Layout, self).__init__(name)
			else:
				name = cmds.layout(name, **kwargs)
				super(Layout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
########################################################################
class MenuBarLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuBarLayout(**kwargs)
			super(MenuBarLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuBarLayout(name, exists=True):
				super(MenuBarLayout, self).__init__(name)
			else:
				name = cmds.menuBarLayout(name, **kwargs)
				super(MenuBarLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
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
########################################################################
class PaneLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.paneLayout(**kwargs)
			super(PaneLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.paneLayout(name, exists=True):
				super(PaneLayout, self).__init__(name)
			else:
				name = cmds.paneLayout(name, **kwargs)
				super(PaneLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_configuration(self):
		""""""
		return self.query(configuration=True)
	#----------------------------------------------------------------------
	def set_configuration(self, value):
		""""""
		self.edit(configuration=value)
	#----------------------------------------------------------------------
	configuration = property(get_configuration, set_configuration)
	#----------------------------------------------------------------------
	def setPane(self,value):
		""""""
		self.edit(setPane=value)
	#----------------------------------------------------------------------
	def get_activePane(self):
		""""""
		return self.query(activePane=True)
	#----------------------------------------------------------------------
	def set_activePane(self, value):
		""""""
		self.edit(activePane=value)
	#----------------------------------------------------------------------
	activePane = property(get_activePane, set_activePane)
	#----------------------------------------------------------------------
	def get_activePaneIndex(self):
		""""""
		return self.query(activePaneIndex=True)
	#----------------------------------------------------------------------
	def set_activePaneIndex(self, value):
		""""""
		self.edit(activePaneIndex=value)
	#----------------------------------------------------------------------
	activePaneIndex = property(get_activePaneIndex, set_activePaneIndex)
	#----------------------------------------------------------------------
	def get_activeFrameThickness(self):
		""""""
		return self.query(activeFrameThickness=True)
	#----------------------------------------------------------------------
	def set_activeFrameThickness(self, value):
		""""""
		self.edit(activeFrameThickness=value)
	#----------------------------------------------------------------------
	activeFrameThickness = property(get_activeFrameThickness, set_activeFrameThickness)
	#----------------------------------------------------------------------
	def get_separatorThickness(self):
		""""""
		return self.query(separatorThickness=True)
	#----------------------------------------------------------------------
	def set_separatorThickness(self, value):
		""""""
		self.edit(separatorThickness=value)
	#----------------------------------------------------------------------
	separatorThickness = property(get_separatorThickness, set_separatorThickness)
	#----------------------------------------------------------------------
	def get_paneSize(self):
		""""""
		return self.query(paneSize=True)
	#----------------------------------------------------------------------
	def set_paneSize(self, value):
		""""""
		self.edit(paneSize=value)
	#----------------------------------------------------------------------
	paneSize = property(get_paneSize, set_paneSize)
	#----------------------------------------------------------------------
	@property
	def pane1(self):
		""""""
		return self.query(pane1=True)
	#----------------------------------------------------------------------
	@property
	def pane2(self):
		""""""
		return self.query(pane2=True)
	#----------------------------------------------------------------------
	@property
	def pane3(self):
		""""""
		return self.query(pane3=True)
	#----------------------------------------------------------------------
	@property
	def pane4(self):
		""""""
		return self.query(pane4=True)
	#----------------------------------------------------------------------
	@property
	def paneUnderPointer(self):
		""""""
		return self.query(paneUnderPointer=True)
	#----------------------------------------------------------------------
	def staticWidthPane(self,value):
		""""""
		self.edit(staticWidthPane=value)
	#----------------------------------------------------------------------
	def staticHeightPane(self,value):
		""""""
		self.edit(staticHeightPane=value)
	#----------------------------------------------------------------------
	@property
	def numberOfVisiblePanes(self):
		""""""
		return self.query(numberOfVisiblePanes=True)
	#----------------------------------------------------------------------
	def separatorMovedCommand(self,value):
		""""""
		self.edit(separatorMovedCommand=value)
########################################################################
class RowColumnLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.rowColumnLayout(**kwargs)
			super(RowColumnLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.rowColumnLayout(name, exists=True):
				super(RowColumnLayout, self).__init__(name)
			else:
				name = cmds.rowColumnLayout(name, **kwargs)
				super(RowColumnLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	@property
	def numberOfColumns(self):
		""""""
		return self.query(numberOfColumns=True)
	#----------------------------------------------------------------------
	@property
	def numberOfRows(self):
		""""""
		return self.query(numberOfRows=True)
	#----------------------------------------------------------------------
	def columnWidth(self,value):
		""""""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	def rowHeight(self,value):
		""""""
		self.edit(rowHeight=value)
	#----------------------------------------------------------------------
	def columnAlign(self,value):
		""""""
		self.edit(columnAlign=value)
	#----------------------------------------------------------------------
	def rowAlign(self,value):
		""""""
		self.edit(rowAlign=value)
	#----------------------------------------------------------------------
	def columnAttach(self,value):
		""""""
		self.edit(columnAttach=value)
	#----------------------------------------------------------------------
	def rowAttach(self,value):
		""""""
		self.edit(rowAttach=value)
	#----------------------------------------------------------------------
	def columnOffset(self,value):
		""""""
		self.edit(columnOffset=value)
	#----------------------------------------------------------------------
	def rowOffset(self,value):
		""""""
		self.edit(rowOffset=value)
	#----------------------------------------------------------------------
	def columnSpacing(self,value):
		""""""
		self.edit(columnSpacing=value)
	#----------------------------------------------------------------------
	def rowSpacing(self,value):
		""""""
		self.edit(rowSpacing=value)
########################################################################
class RowLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.rowLayout(**kwargs)
			super(RowLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.rowLayout(name, exists=True):
				super(RowLayout, self).__init__(name)
			else:
				name = cmds.rowLayout(name, **kwargs)
				super(RowLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	@property
	def numberOfColumns(self):
		""""""
		return self.query(numberOfColumns=True)
	#----------------------------------------------------------------------
	def columnWidth(self,value):
		""""""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	def columnAttach(self,value):
		""""""
		self.edit(columnAttach=value)
	#----------------------------------------------------------------------
	def rowAttach(self,value):
		""""""
		self.edit(rowAttach=value)
	#----------------------------------------------------------------------
	def columnAlign(self,value):
		""""""
		self.edit(columnAlign=value)
	#----------------------------------------------------------------------
	def adjustableColumn(self,value):
		""""""
		self.edit(adjustableColumn=value)
########################################################################
class ScrollLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scrollLayout(**kwargs)
			super(ScrollLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scrollLayout(name, exists=True):
				super(ScrollLayout, self).__init__(name)
			else:
				name = cmds.scrollLayout(name, **kwargs)
				super(ScrollLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def horizontalScrollBarThickness(self,value):
		""""""
		self.edit(horizontalScrollBarThickness=value)
	#----------------------------------------------------------------------
	def verticalScrollBarThickness(self,value):
		""""""
		self.edit(verticalScrollBarThickness=value)
	#----------------------------------------------------------------------
	@property
	def childResizable(self):
		""""""
		return self.query(childResizable=True)
	#----------------------------------------------------------------------
	@property
	def scrollAreaWidth(self):
		""""""
		return self.query(scrollAreaWidth=True)
	#----------------------------------------------------------------------
	@property
	def scrollAreaHeight(self):
		""""""
		return self.query(scrollAreaHeight=True)
	#----------------------------------------------------------------------
	@property
	def scrollAreaValue(self):
		""""""
		return self.query(scrollAreaValue=True)
	#----------------------------------------------------------------------
	@property
	def minChildWidth(self):
		""""""
		return self.query(minChildWidth=True)
	#----------------------------------------------------------------------
	def resizeCommand(self,value):
		""""""
		self.edit(resizeCommand=value)
	#----------------------------------------------------------------------
	def scrollPage(self,value):
		""""""
		self.edit(scrollPage=value)
	#----------------------------------------------------------------------
	def scrollByPixel(self,value):
		""""""
		self.edit(scrollByPixel=value)
########################################################################
class ShelfLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.shelfLayout(**kwargs)
			super(ShelfLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.shelfLayout(name, exists=True):
				super(ShelfLayout, self).__init__(name)
			else:
				name = cmds.shelfLayout(name, **kwargs)
				super(ShelfLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_style(self):
		""""""
		return self.query(style=True)
	#----------------------------------------------------------------------
	def set_style(self, value):
		""""""
		self.edit(style=value)
	#----------------------------------------------------------------------
	style = property(get_style, set_style)
	#----------------------------------------------------------------------
	def get_cellWidth(self):
		""""""
		return self.query(cellWidth=True)
	#----------------------------------------------------------------------
	def set_cellWidth(self, value):
		""""""
		self.edit(cellWidth=value)
	#----------------------------------------------------------------------
	cellWidth = property(get_cellWidth, set_cellWidth)
	#----------------------------------------------------------------------
	def get_cellHeight(self):
		""""""
		return self.query(cellHeight=True)
	#----------------------------------------------------------------------
	def set_cellHeight(self, value):
		""""""
		self.edit(cellHeight=value)
	#----------------------------------------------------------------------
	cellHeight = property(get_cellHeight, set_cellHeight)
	#----------------------------------------------------------------------
	def get_cellWidthHeight(self):
		""""""
		return self.query(cellWidthHeight=True)
	#----------------------------------------------------------------------
	def set_cellWidthHeight(self, value):
		""""""
		self.edit(cellWidthHeight=value)
	#----------------------------------------------------------------------
	cellWidthHeight = property(get_cellWidthHeight, set_cellWidthHeight)
	#----------------------------------------------------------------------
	def position(self,value):
		""""""
		self.edit(position=value)
########################################################################
class ShelfTabLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.shelfTabLayout(**kwargs)
			super(ShelfTabLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.shelfTabLayout(name, exists=True):
				super(ShelfTabLayout, self).__init__(name)
			else:
				name = cmds.shelfTabLayout(name, **kwargs)
				super(ShelfTabLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_tabsVisible(self):
		""""""
		return self.query(tabsVisible=True)
	#----------------------------------------------------------------------
	def set_tabsVisible(self, value):
		""""""
		self.edit(tabsVisible=value)
	#----------------------------------------------------------------------
	tabsVisible = property(get_tabsVisible, set_tabsVisible)
	#----------------------------------------------------------------------
	def get_selectTab(self):
		""""""
		return self.query(selectTab=True)
	#----------------------------------------------------------------------
	def set_selectTab(self, value):
		""""""
		self.edit(selectTab=value)
	#----------------------------------------------------------------------
	selectTab = property(get_selectTab, set_selectTab)
	#----------------------------------------------------------------------
	def get_selectTabIndex(self):
		""""""
		return self.query(selectTabIndex=True)
	#----------------------------------------------------------------------
	def set_selectTabIndex(self, value):
		""""""
		self.edit(selectTabIndex=value)
	#----------------------------------------------------------------------
	selectTabIndex = property(get_selectTabIndex, set_selectTabIndex)
	#----------------------------------------------------------------------
	def get_tabLabel(self):
		""""""
		return self.query(tabLabel=True)
	#----------------------------------------------------------------------
	def set_tabLabel(self, value):
		""""""
		self.edit(tabLabel=value)
	#----------------------------------------------------------------------
	tabLabel = property(get_tabLabel, set_tabLabel)
	#----------------------------------------------------------------------
	def get_tabLabelIndex(self):
		""""""
		return self.query(tabLabelIndex=True)
	#----------------------------------------------------------------------
	def set_tabLabelIndex(self, value):
		""""""
		self.edit(tabLabelIndex=value)
	#----------------------------------------------------------------------
	tabLabelIndex = property(get_tabLabelIndex, set_tabLabelIndex)
	#----------------------------------------------------------------------
	@property
	def scrollable(self):
		""""""
		return self.query(scrollable=True)
	#----------------------------------------------------------------------
	def horizontalScrollBarThickness(self,value):
		""""""
		self.edit(horizontalScrollBarThickness=value)
	#----------------------------------------------------------------------
	def verticalScrollBarThickness(self,value):
		""""""
		self.edit(verticalScrollBarThickness=value)
	#----------------------------------------------------------------------
	@property
	def innerMarginWidth(self):
		""""""
		return self.query(innerMarginWidth=True)
	#----------------------------------------------------------------------
	@property
	def innerMarginHeight(self):
		""""""
		return self.query(innerMarginHeight=True)
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
	def get_imageVisible(self):
		""""""
		return self.query(imageVisible=True)
	#----------------------------------------------------------------------
	def set_imageVisible(self, value):
		""""""
		self.edit(imageVisible=value)
	#----------------------------------------------------------------------
	imageVisible = property(get_imageVisible, set_imageVisible)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
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
	def preSelectCommand(self,value):
		""""""
		self.edit(preSelectCommand=value)
	#----------------------------------------------------------------------
	def doubleClickCommand(self,value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	@property
	def childResizable(self):
		""""""
		return self.query(childResizable=True)
	#----------------------------------------------------------------------
	@property
	def minChildWidth(self):
		""""""
		return self.query(minChildWidth=True)
	#----------------------------------------------------------------------
	def moveTab(self,value):
		""""""
		self.edit(moveTab=value)
########################################################################
class TabLayout(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.tabLayout(**kwargs)
			super(TabLayout, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.tabLayout(name, exists=True):
				super(TabLayout, self).__init__(name)
			else:
				name = cmds.tabLayout(name, **kwargs)
				super(TabLayout, self).__init__(name, **dict(qtParent=parent))
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
	#----------------------------------------------------------------------
	@property
	def numberOfChildren(self):
		""""""
		return self.query(numberOfChildren=True)
	#----------------------------------------------------------------------
	@property
	def childArray(self):
		""""""
		return self.query(childArray=True)
	#----------------------------------------------------------------------
	def get_tabsVisible(self):
		""""""
		return self.query(tabsVisible=True)
	#----------------------------------------------------------------------
	def set_tabsVisible(self, value):
		""""""
		self.edit(tabsVisible=value)
	#----------------------------------------------------------------------
	tabsVisible = property(get_tabsVisible, set_tabsVisible)
	#----------------------------------------------------------------------
	def get_selectTab(self):
		""""""
		return self.query(selectTab=True)
	#----------------------------------------------------------------------
	def set_selectTab(self, value):
		""""""
		self.edit(selectTab=value)
	#----------------------------------------------------------------------
	selectTab = property(get_selectTab, set_selectTab)
	#----------------------------------------------------------------------
	def get_selectTabIndex(self):
		""""""
		return self.query(selectTabIndex=True)
	#----------------------------------------------------------------------
	def set_selectTabIndex(self, value):
		""""""
		self.edit(selectTabIndex=value)
	#----------------------------------------------------------------------
	selectTabIndex = property(get_selectTabIndex, set_selectTabIndex)
	#----------------------------------------------------------------------
	def get_tabLabel(self):
		""""""
		return self.query(tabLabel=True)
	#----------------------------------------------------------------------
	def set_tabLabel(self, value):
		""""""
		self.edit(tabLabel=value)
	#----------------------------------------------------------------------
	tabLabel = property(get_tabLabel, set_tabLabel)
	#----------------------------------------------------------------------
	def get_tabLabelIndex(self):
		""""""
		return self.query(tabLabelIndex=True)
	#----------------------------------------------------------------------
	def set_tabLabelIndex(self, value):
		""""""
		self.edit(tabLabelIndex=value)
	#----------------------------------------------------------------------
	tabLabelIndex = property(get_tabLabelIndex, set_tabLabelIndex)
	#----------------------------------------------------------------------
	@property
	def scrollable(self):
		""""""
		return self.query(scrollable=True)
	#----------------------------------------------------------------------
	def horizontalScrollBarThickness(self,value):
		""""""
		self.edit(horizontalScrollBarThickness=value)
	#----------------------------------------------------------------------
	def verticalScrollBarThickness(self,value):
		""""""
		self.edit(verticalScrollBarThickness=value)
	#----------------------------------------------------------------------
	@property
	def innerMarginWidth(self):
		""""""
		return self.query(innerMarginWidth=True)
	#----------------------------------------------------------------------
	@property
	def innerMarginHeight(self):
		""""""
		return self.query(innerMarginHeight=True)
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
	def get_imageVisible(self):
		""""""
		return self.query(imageVisible=True)
	#----------------------------------------------------------------------
	def set_imageVisible(self, value):
		""""""
		self.edit(imageVisible=value)
	#----------------------------------------------------------------------
	imageVisible = property(get_imageVisible, set_imageVisible)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
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
	def preSelectCommand(self,value):
		""""""
		self.edit(preSelectCommand=value)
	#----------------------------------------------------------------------
	def doubleClickCommand(self,value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	@property
	def childResizable(self):
		""""""
		return self.query(childResizable=True)
	#----------------------------------------------------------------------
	@property
	def minChildWidth(self):
		""""""
		return self.query(minChildWidth=True)
	#----------------------------------------------------------------------
	def moveTab(self,value):
		""""""
		self.edit(moveTab=value)
########################################################################
class ToolBar(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toolBar(**kwargs)
			super(ToolBar, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toolBar(name, exists=True):
				super(ToolBar, self).__init__(name)
			else:
				name = cmds.toolBar(name, **kwargs)
				super(ToolBar, self).__init__(name, **dict(qtParent=parent))
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
	def get_allowedArea(self):
		""""""
		return self.query(allowedArea=True)
	#----------------------------------------------------------------------
	def set_allowedArea(self, value):
		""""""
		self.edit(allowedArea=value)
	#----------------------------------------------------------------------
	allowedArea = property(get_allowedArea, set_allowedArea)
	#----------------------------------------------------------------------
	def get_area(self):
		""""""
		return self.query(area=True)
	#----------------------------------------------------------------------
	def set_area(self, value):
		""""""
		self.edit(area=value)
	#----------------------------------------------------------------------
	area = property(get_area, set_area)
	#----------------------------------------------------------------------
	@property
	def content(self):
		""""""
		return self.query(content=True)