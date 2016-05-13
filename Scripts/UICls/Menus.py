__all__ = ['ArtBuildPaintMenu', 'AttrEnumOptionMenu', 'AttrEnumOptionMenuGrp', 'AttributeMenu', 'HotBox', 'Menu', 'MenuEditor', 'MenuItem', 'MenuSet', 'MenuSetPref', 'OptionMenu', 'OptionMenuGrp', 'PopupMenu', 'RadioMenuItemCollection', 'SaveMenu',]
import maya.cmds as cmds
import UI_Object


########################################################################
class ArtBuildPaintMenu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.artBuildPaintMenu(**kwargs)
			super(ArtBuildPaintMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.artBuildPaintMenu(name, exists=True):
				super(ArtBuildPaintMenu, self).__init__(name)
			else:
				name = cmds.artBuildPaintMenu(name, **kwargs)
				super(ArtBuildPaintMenu, self).__init__(name, **dict(qtParent=parent))
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
########################################################################
class AttrEnumOptionMenu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrEnumOptionMenu(**kwargs)
			super(AttrEnumOptionMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrEnumOptionMenu(name, exists=True):
				super(AttrEnumOptionMenu, self).__init__(name)
			else:
				name = cmds.attrEnumOptionMenu(name, **kwargs)
				super(AttrEnumOptionMenu, self).__init__(name, **dict(qtParent=parent))
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
	def attribute(self,value):
		""""""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
########################################################################
class AttrEnumOptionMenuGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrEnumOptionMenuGrp(**kwargs)
			super(AttrEnumOptionMenuGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrEnumOptionMenuGrp(name, exists=True):
				super(AttrEnumOptionMenuGrp, self).__init__(name)
			else:
				name = cmds.attrEnumOptionMenuGrp(name, **kwargs)
				super(AttrEnumOptionMenuGrp, self).__init__(name, **dict(qtParent=parent))
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
	def columnWidth(self,value):
		""""""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	def columnWidth1(self,value):
		""""""
		self.edit(columnWidth1=value)
	#----------------------------------------------------------------------
	def columnWidth2(self,value):
		""""""
		self.edit(columnWidth2=value)
	#----------------------------------------------------------------------
	def columnWidth3(self,value):
		""""""
		self.edit(columnWidth3=value)
	#----------------------------------------------------------------------
	def columnWidth4(self,value):
		""""""
		self.edit(columnWidth4=value)
	#----------------------------------------------------------------------
	def columnWidth5(self,value):
		""""""
		self.edit(columnWidth5=value)
	#----------------------------------------------------------------------
	def columnWidth6(self,value):
		""""""
		self.edit(columnWidth6=value)
	#----------------------------------------------------------------------
	def columnAttach(self,value):
		""""""
		self.edit(columnAttach=value)
	#----------------------------------------------------------------------
	def columnAttach2(self,value):
		""""""
		self.edit(columnAttach2=value)
	#----------------------------------------------------------------------
	def columnAttach3(self,value):
		""""""
		self.edit(columnAttach3=value)
	#----------------------------------------------------------------------
	def columnAttach4(self,value):
		""""""
		self.edit(columnAttach4=value)
	#----------------------------------------------------------------------
	def columnAttach5(self,value):
		""""""
		self.edit(columnAttach5=value)
	#----------------------------------------------------------------------
	def columnAttach6(self,value):
		""""""
		self.edit(columnAttach6=value)
	#----------------------------------------------------------------------
	def columnOffset2(self,value):
		""""""
		self.edit(columnOffset2=value)
	#----------------------------------------------------------------------
	def columnOffset3(self,value):
		""""""
		self.edit(columnOffset3=value)
	#----------------------------------------------------------------------
	def columnOffset4(self,value):
		""""""
		self.edit(columnOffset4=value)
	#----------------------------------------------------------------------
	def columnOffset5(self,value):
		""""""
		self.edit(columnOffset5=value)
	#----------------------------------------------------------------------
	def columnOffset6(self,value):
		""""""
		self.edit(columnOffset6=value)
	#----------------------------------------------------------------------
	def rowAttach(self,value):
		""""""
		self.edit(rowAttach=value)
	#----------------------------------------------------------------------
	def columnAlign(self,value):
		""""""
		self.edit(columnAlign=value)
	#----------------------------------------------------------------------
	def columnAlign2(self,value):
		""""""
		self.edit(columnAlign2=value)
	#----------------------------------------------------------------------
	def columnAlign3(self,value):
		""""""
		self.edit(columnAlign3=value)
	#----------------------------------------------------------------------
	def columnAlign4(self,value):
		""""""
		self.edit(columnAlign4=value)
	#----------------------------------------------------------------------
	def columnAlign5(self,value):
		""""""
		self.edit(columnAlign5=value)
	#----------------------------------------------------------------------
	def columnAlign6(self,value):
		""""""
		self.edit(columnAlign6=value)
	#----------------------------------------------------------------------
	def adjustableColumn(self,value):
		""""""
		self.edit(adjustableColumn=value)
	#----------------------------------------------------------------------
	def adjustableColumn2(self,value):
		""""""
		self.edit(adjustableColumn2=value)
	#----------------------------------------------------------------------
	def adjustableColumn3(self,value):
		""""""
		self.edit(adjustableColumn3=value)
	#----------------------------------------------------------------------
	def adjustableColumn4(self,value):
		""""""
		self.edit(adjustableColumn4=value)
	#----------------------------------------------------------------------
	def adjustableColumn5(self,value):
		""""""
		self.edit(adjustableColumn5=value)
	#----------------------------------------------------------------------
	def adjustableColumn6(self,value):
		""""""
		self.edit(adjustableColumn6=value)
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
	def attribute(self,value):
		""""""
		self.edit(attribute=value)
########################################################################
class AttributeMenu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attributeMenu(**kwargs)
			super(AttributeMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attributeMenu(name, exists=True):
				super(AttributeMenu, self).__init__(name)
			else:
				name = cmds.attributeMenu(name, **kwargs)
				super(AttributeMenu, self).__init__(name, **dict(qtParent=parent))
########################################################################
class HotBox(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotBox(**kwargs)
			super(HotBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotBox(name, exists=True):
				super(HotBox, self).__init__(name)
			else:
				name = cmds.hotBox(name, **kwargs)
				super(HotBox, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def transparenyLevel(self):
		""""""
		return self.query(transparenyLevel=True)
	#----------------------------------------------------------------------
	@property
	def showAllToggleMenus(self):
		""""""
		return self.query(showAllToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def polygonsToggleMenus(self):
		""""""
		return self.query(polygonsToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def surfacesToggleMenus(self):
		""""""
		return self.query(surfacesToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def animationToggleMenus(self):
		""""""
		return self.query(animationToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def dynamicsToggleMenus(self):
		""""""
		return self.query(dynamicsToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def renderingToggleMenus(self):
		""""""
		return self.query(renderingToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def clothToggleMenus(self):
		""""""
		return self.query(clothToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def liveToggleMenus(self):
		""""""
		return self.query(liveToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def commonToggleMenus(self):
		""""""
		return self.query(commonToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def customMenuSetsToggleMenus(self):
		""""""
		return self.query(customMenuSetsToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def PaneToggleMenus(self):
		""""""
		return self.query(PaneToggleMenus=True)
	#----------------------------------------------------------------------
	@property
	def rmbPopups(self):
		""""""
		return self.query(rmbPopups=True)
	#----------------------------------------------------------------------
	@property
	def polygonsOnlyMenus(self):
		""""""
		return self.query(polygonsOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def surfacesOnlyMenus(self):
		""""""
		return self.query(surfacesOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def animationOnlyMenus(self):
		""""""
		return self.query(animationOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def dynamicsOnlyMenus(self):
		""""""
		return self.query(dynamicsOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def renderingOnlyMenus(self):
		""""""
		return self.query(renderingOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def clothOnlyMenus(self):
		""""""
		return self.query(clothOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def liveOnlyMenus(self):
		""""""
		return self.query(liveOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def commonOnlyMenus(self):
		""""""
		return self.query(commonOnlyMenus=True)
	#----------------------------------------------------------------------
	@property
	def displayHotbox(self):
		""""""
		return self.query(displayHotbox=True)
	#----------------------------------------------------------------------
	@property
	def displayZonesOnly(self):
		""""""
		return self.query(displayZonesOnly=True)
	#----------------------------------------------------------------------
	@property
	def displayStyle(self):
		""""""
		return self.query(displayStyle=True)
	#----------------------------------------------------------------------
	@property
	def release(self):
		""""""
		return self.query(release=True)
	#----------------------------------------------------------------------
	@property
	def noKeyPress(self):
		""""""
		return self.query(noKeyPress=True)
########################################################################
class Menu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menu(**kwargs)
			super(Menu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menu(name, exists=True):
				super(Menu, self).__init__(name)
			else:
				name = cmds.menu(name, **kwargs)
				super(Menu, self).__init__(name, **dict(qtParent=parent))
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
	def get_helpMenu(self):
		""""""
		return self.query(helpMenu=True)
	#----------------------------------------------------------------------
	def set_helpMenu(self, value):
		""""""
		self.edit(helpMenu=value)
	#----------------------------------------------------------------------
	helpMenu = property(get_helpMenu, set_helpMenu)
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
	def get_mnemonic(self):
		""""""
		return self.query(mnemonic=True)
	#----------------------------------------------------------------------
	def set_mnemonic(self, value):
		""""""
		self.edit(mnemonic=value)
	#----------------------------------------------------------------------
	mnemonic = property(get_mnemonic, set_mnemonic)
	#----------------------------------------------------------------------
	@property
	def allowOptionBoxes(self):
		""""""
		return self.query(allowOptionBoxes=True)
	#----------------------------------------------------------------------
	@property
	def numberOfItems(self):
		""""""
		return self.query(numberOfItems=True)
	#----------------------------------------------------------------------
	@property
	def itemArray(self):
		""""""
		return self.query(itemArray=True)
	#----------------------------------------------------------------------
	def postMenuCommand(self,value):
		""""""
		self.edit(postMenuCommand=value)
	#----------------------------------------------------------------------
	def get_postMenuCommandOnce(self):
		""""""
		return self.query(postMenuCommandOnce=True)
	#----------------------------------------------------------------------
	def set_postMenuCommandOnce(self, value):
		""""""
		self.edit(postMenuCommandOnce=value)
	#----------------------------------------------------------------------
	postMenuCommandOnce = property(get_postMenuCommandOnce, set_postMenuCommandOnce)
	#----------------------------------------------------------------------
	def deleteAllItems(self,value):
		""""""
		self.edit(deleteAllItems=value)
	#----------------------------------------------------------------------
	def get_familyImage(self):
		""""""
		return self.query(familyImage=True)
	#----------------------------------------------------------------------
	def set_familyImage(self, value):
		""""""
		self.edit(familyImage=value)
	#----------------------------------------------------------------------
	familyImage = property(get_familyImage, set_familyImage)
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
class MenuEditor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuEditor(**kwargs)
			super(MenuEditor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuEditor(name, exists=True):
				super(MenuEditor, self).__init__(name)
			else:
				name = cmds.menuEditor(name, **kwargs)
				super(MenuEditor, self).__init__(name, **dict(qtParent=parent))
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
	def cellWidthHeight(self,value):
		""""""
		self.edit(cellWidthHeight=value)
	#----------------------------------------------------------------------
	def get_topLevelMenu(self):
		""""""
		return self.query(topLevelMenu=True)
	#----------------------------------------------------------------------
	def set_topLevelMenu(self, value):
		""""""
		self.edit(topLevelMenu=value)
	#----------------------------------------------------------------------
	topLevelMenu = property(get_topLevelMenu, set_topLevelMenu)
	#----------------------------------------------------------------------
	def subMenuAt(self,value):
		""""""
		self.edit(subMenuAt=value)
	#----------------------------------------------------------------------
	def get_separator(self):
		""""""
		return self.query(separator=True)
	#----------------------------------------------------------------------
	def set_separator(self, value):
		""""""
		self.edit(separator=value)
	#----------------------------------------------------------------------
	separator = property(get_separator, set_separator)
	#----------------------------------------------------------------------
	def delete(self,value):
		""""""
		self.edit(delete=value)
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
	def get_command(self):
		""""""
		return self.query(command=True)
	#----------------------------------------------------------------------
	def set_command(self, value):
		""""""
		self.edit(command=value)
	#----------------------------------------------------------------------
	command = property(get_command, set_command)
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
	def get_checkBoxPresent(self):
		""""""
		return self.query(checkBoxPresent=True)
	#----------------------------------------------------------------------
	def set_checkBoxPresent(self, value):
		""""""
		self.edit(checkBoxPresent=value)
	#----------------------------------------------------------------------
	checkBoxPresent = property(get_checkBoxPresent, set_checkBoxPresent)
	#----------------------------------------------------------------------
	def get_checkBoxState(self):
		""""""
		return self.query(checkBoxState=True)
	#----------------------------------------------------------------------
	def set_checkBoxState(self, value):
		""""""
		self.edit(checkBoxState=value)
	#----------------------------------------------------------------------
	checkBoxState = property(get_checkBoxState, set_checkBoxState)
	#----------------------------------------------------------------------
	def get_radioButtonPresent(self):
		""""""
		return self.query(radioButtonPresent=True)
	#----------------------------------------------------------------------
	def set_radioButtonPresent(self, value):
		""""""
		self.edit(radioButtonPresent=value)
	#----------------------------------------------------------------------
	radioButtonPresent = property(get_radioButtonPresent, set_radioButtonPresent)
	#----------------------------------------------------------------------
	def get_radioButtonState(self):
		""""""
		return self.query(radioButtonState=True)
	#----------------------------------------------------------------------
	def set_radioButtonState(self, value):
		""""""
		self.edit(radioButtonState=value)
	#----------------------------------------------------------------------
	radioButtonState = property(get_radioButtonState, set_radioButtonState)
	#----------------------------------------------------------------------
	def get_optionBoxPresent(self):
		""""""
		return self.query(optionBoxPresent=True)
	#----------------------------------------------------------------------
	def set_optionBoxPresent(self, value):
		""""""
		self.edit(optionBoxPresent=value)
	#----------------------------------------------------------------------
	optionBoxPresent = property(get_optionBoxPresent, set_optionBoxPresent)
	#----------------------------------------------------------------------
	def get_optionBoxCommand(self):
		""""""
		return self.query(optionBoxCommand=True)
	#----------------------------------------------------------------------
	def set_optionBoxCommand(self, value):
		""""""
		self.edit(optionBoxCommand=value)
	#----------------------------------------------------------------------
	optionBoxCommand = property(get_optionBoxCommand, set_optionBoxCommand)
	#----------------------------------------------------------------------
	@property
	def menuItemTypes(self):
		""""""
		return self.query(menuItemTypes=True)
	#----------------------------------------------------------------------
	@property
	def subMenuEditorsOpen(self):
		""""""
		return self.query(subMenuEditorsOpen=True)
########################################################################
class MenuItem(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuItem(**kwargs)
			super(MenuItem, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuItem(name, exists=True):
				super(MenuItem, self).__init__(name)
			else:
				name = cmds.menuItem(name, **kwargs)
				super(MenuItem, self).__init__(name, **dict(qtParent=parent))
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
	def divider(self):
		""""""
		return self.query(divider=True)
	#----------------------------------------------------------------------
	def get_checkBox(self):
		""""""
		return self.query(checkBox=True)
	#----------------------------------------------------------------------
	def set_checkBox(self, value):
		""""""
		self.edit(checkBox=value)
	#----------------------------------------------------------------------
	checkBox = property(get_checkBox, set_checkBox)
	#----------------------------------------------------------------------
	@property
	def isCheckBox(self):
		""""""
		return self.query(isCheckBox=True)
	#----------------------------------------------------------------------
	def get_radioButton(self):
		""""""
		return self.query(radioButton=True)
	#----------------------------------------------------------------------
	def set_radioButton(self, value):
		""""""
		self.edit(radioButton=value)
	#----------------------------------------------------------------------
	radioButton = property(get_radioButton, set_radioButton)
	#----------------------------------------------------------------------
	@property
	def isRadioButton(self):
		""""""
		return self.query(isRadioButton=True)
	#----------------------------------------------------------------------
	@property
	def optionBox(self):
		""""""
		return self.query(optionBox=True)
	#----------------------------------------------------------------------
	@property
	def isOptionBox(self):
		""""""
		return self.query(isOptionBox=True)
	#----------------------------------------------------------------------
	def get_optionBoxIcon(self):
		""""""
		return self.query(optionBoxIcon=True)
	#----------------------------------------------------------------------
	def set_optionBoxIcon(self, value):
		""""""
		self.edit(optionBoxIcon=value)
	#----------------------------------------------------------------------
	optionBoxIcon = property(get_optionBoxIcon, set_optionBoxIcon)
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
	@property
	def collection(self):
		""""""
		return self.query(collection=True)
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
	def get_imageOverlayLabel(self):
		""""""
		return self.query(imageOverlayLabel=True)
	#----------------------------------------------------------------------
	def set_imageOverlayLabel(self, value):
		""""""
		self.edit(imageOverlayLabel=value)
	#----------------------------------------------------------------------
	imageOverlayLabel = property(get_imageOverlayLabel, set_imageOverlayLabel)
	#----------------------------------------------------------------------
	@property
	def familyImage(self):
		""""""
		return self.query(familyImage=True)
	#----------------------------------------------------------------------
	@property
	def allowOptionBoxes(self):
		""""""
		return self.query(allowOptionBoxes=True)
	#----------------------------------------------------------------------
	@property
	def subMenu(self):
		""""""
		return self.query(subMenu=True)
	#----------------------------------------------------------------------
	@property
	def tearOff(self):
		""""""
		return self.query(tearOff=True)
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
	def get_data(self):
		""""""
		return self.query(data=True)
	#----------------------------------------------------------------------
	def set_data(self, value):
		""""""
		self.edit(data=value)
	#----------------------------------------------------------------------
	data = property(get_data, set_data)
	#----------------------------------------------------------------------
	def get_radialPosition(self):
		""""""
		return self.query(radialPosition=True)
	#----------------------------------------------------------------------
	def set_radialPosition(self, value):
		""""""
		self.edit(radialPosition=value)
	#----------------------------------------------------------------------
	radialPosition = property(get_radialPosition, set_radialPosition)
	#----------------------------------------------------------------------
	def get_command(self):
		""""""
		return self.query(command=True)
	#----------------------------------------------------------------------
	def set_command(self, value):
		""""""
		self.edit(command=value)
	#----------------------------------------------------------------------
	command = property(get_command, set_command)
	#----------------------------------------------------------------------
	def get_dragMenuCommand(self):
		""""""
		return self.query(dragMenuCommand=True)
	#----------------------------------------------------------------------
	def set_dragMenuCommand(self, value):
		""""""
		self.edit(dragMenuCommand=value)
	#----------------------------------------------------------------------
	dragMenuCommand = property(get_dragMenuCommand, set_dragMenuCommand)
	#----------------------------------------------------------------------
	def get_dragDoubleClickCommand(self):
		""""""
		return self.query(dragDoubleClickCommand=True)
	#----------------------------------------------------------------------
	def set_dragDoubleClickCommand(self, value):
		""""""
		self.edit(dragDoubleClickCommand=value)
	#----------------------------------------------------------------------
	dragDoubleClickCommand = property(get_dragDoubleClickCommand, set_dragDoubleClickCommand)
	#----------------------------------------------------------------------
	def get_postMenuCommand(self):
		""""""
		return self.query(postMenuCommand=True)
	#----------------------------------------------------------------------
	def set_postMenuCommand(self, value):
		""""""
		self.edit(postMenuCommand=value)
	#----------------------------------------------------------------------
	postMenuCommand = property(get_postMenuCommand, set_postMenuCommand)
	#----------------------------------------------------------------------
	def get_postMenuCommandOnce(self):
		""""""
		return self.query(postMenuCommandOnce=True)
	#----------------------------------------------------------------------
	def set_postMenuCommandOnce(self, value):
		""""""
		self.edit(postMenuCommandOnce=value)
	#----------------------------------------------------------------------
	postMenuCommandOnce = property(get_postMenuCommandOnce, set_postMenuCommandOnce)
	#----------------------------------------------------------------------
	def get_sourceType(self):
		""""""
		return self.query(sourceType=True)
	#----------------------------------------------------------------------
	def set_sourceType(self, value):
		""""""
		self.edit(sourceType=value)
	#----------------------------------------------------------------------
	sourceType = property(get_sourceType, set_sourceType)
	#----------------------------------------------------------------------
	def get_keyEquivalent(self):
		""""""
		return self.query(keyEquivalent=True)
	#----------------------------------------------------------------------
	def set_keyEquivalent(self, value):
		""""""
		self.edit(keyEquivalent=value)
	#----------------------------------------------------------------------
	keyEquivalent = property(get_keyEquivalent, set_keyEquivalent)
	#----------------------------------------------------------------------
	def get_altModifier(self):
		""""""
		return self.query(altModifier=True)
	#----------------------------------------------------------------------
	def set_altModifier(self, value):
		""""""
		self.edit(altModifier=value)
	#----------------------------------------------------------------------
	altModifier = property(get_altModifier, set_altModifier)
	#----------------------------------------------------------------------
	def get_optionModifier(self):
		""""""
		return self.query(optionModifier=True)
	#----------------------------------------------------------------------
	def set_optionModifier(self, value):
		""""""
		self.edit(optionModifier=value)
	#----------------------------------------------------------------------
	optionModifier = property(get_optionModifier, set_optionModifier)
	#----------------------------------------------------------------------
	def get_ctrlModifier(self):
		""""""
		return self.query(ctrlModifier=True)
	#----------------------------------------------------------------------
	def set_ctrlModifier(self, value):
		""""""
		self.edit(ctrlModifier=value)
	#----------------------------------------------------------------------
	ctrlModifier = property(get_ctrlModifier, set_ctrlModifier)
	#----------------------------------------------------------------------
	def get_commandModifier(self):
		""""""
		return self.query(commandModifier=True)
	#----------------------------------------------------------------------
	def set_commandModifier(self, value):
		""""""
		self.edit(commandModifier=value)
	#----------------------------------------------------------------------
	commandModifier = property(get_commandModifier, set_commandModifier)
	#----------------------------------------------------------------------
	def get_shiftModifier(self):
		""""""
		return self.query(shiftModifier=True)
	#----------------------------------------------------------------------
	def set_shiftModifier(self, value):
		""""""
		self.edit(shiftModifier=value)
	#----------------------------------------------------------------------
	shiftModifier = property(get_shiftModifier, set_shiftModifier)
	#----------------------------------------------------------------------
	def get_enableCommandRepeat(self):
		""""""
		return self.query(enableCommandRepeat=True)
	#----------------------------------------------------------------------
	def set_enableCommandRepeat(self, value):
		""""""
		self.edit(enableCommandRepeat=value)
	#----------------------------------------------------------------------
	enableCommandRepeat = property(get_enableCommandRepeat, set_enableCommandRepeat)
	#----------------------------------------------------------------------
	def get_echoCommand(self):
		""""""
		return self.query(echoCommand=True)
	#----------------------------------------------------------------------
	def set_echoCommand(self, value):
		""""""
		self.edit(echoCommand=value)
	#----------------------------------------------------------------------
	echoCommand = property(get_echoCommand, set_echoCommand)
	#----------------------------------------------------------------------
	@property
	def italicized(self):
		""""""
		return self.query(italicized=True)
	#----------------------------------------------------------------------
	@property
	def boldFont(self):
		""""""
		return self.query(boldFont=True)
	#----------------------------------------------------------------------
	def get_version(self):
		""""""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		""""""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
########################################################################
class MenuSet(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuSet(**kwargs)
			super(MenuSet, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuSet(name, exists=True):
				super(MenuSet, self).__init__(name)
			else:
				name = cmds.menuSet(name, **kwargs)
				super(MenuSet, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def exists(self):
		""""""
		return self.query(exists=True)
	#----------------------------------------------------------------------
	@property
	def label(self):
		""""""
		return self.query(label=True)
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
	@property
	def currentMenuSet(self):
		""""""
		return self.query(currentMenuSet=True)
	#----------------------------------------------------------------------
	@property
	def numberOfMenuSets(self):
		""""""
		return self.query(numberOfMenuSets=True)
	#----------------------------------------------------------------------
	@property
	def allMenuSets(self):
		""""""
		return self.query(allMenuSets=True)
	#----------------------------------------------------------------------
	def get_hotBoxVisible(self):
		""""""
		return self.query(hotBoxVisible=True)
	#----------------------------------------------------------------------
	def set_hotBoxVisible(self, value):
		""""""
		self.edit(hotBoxVisible=value)
	#----------------------------------------------------------------------
	hotBoxVisible = property(get_hotBoxVisible, set_hotBoxVisible)
	#----------------------------------------------------------------------
	def get_permanent(self):
		""""""
		return self.query(permanent=True)
	#----------------------------------------------------------------------
	def set_permanent(self, value):
		""""""
		self.edit(permanent=value)
	#----------------------------------------------------------------------
	permanent = property(get_permanent, set_permanent)
########################################################################
class MenuSetPref(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.menuSetPref(**kwargs)
			super(MenuSetPref, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.menuSetPref(name, exists=True):
				super(MenuSetPref, self).__init__(name)
			else:
				name = cmds.menuSetPref(name, **kwargs)
				super(MenuSetPref, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def force(self,value):
		""""""
		self.edit(force=value)
	#----------------------------------------------------------------------
	@property
	def exists(self):
		""""""
		return self.query(exists=True)
	#----------------------------------------------------------------------
	@property
	def version(self):
		""""""
		return self.query(version=True)
########################################################################
class OptionMenu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.optionMenu(**kwargs)
			super(OptionMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.optionMenu(name, exists=True):
				super(OptionMenu, self).__init__(name)
			else:
				name = cmds.optionMenu(name, **kwargs)
				super(OptionMenu, self).__init__(name, **dict(qtParent=parent))
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
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	@property
	def itemListShort(self):
		""""""
		return self.query(itemListShort=True)
	#----------------------------------------------------------------------
	@property
	def itemListLong(self):
		""""""
		return self.query(itemListLong=True)
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
	def numberOfItems(self):
		""""""
		return self.query(numberOfItems=True)
	#----------------------------------------------------------------------
	def get_select(self):
		""""""
		return self.query(select=True)
	#----------------------------------------------------------------------
	def set_select(self, value):
		""""""
		self.edit(select=value)
	#----------------------------------------------------------------------
	select = property(get_select, set_select)
	#----------------------------------------------------------------------
	def get_value(self):
		""""""
		return self.query(value=True)
	#----------------------------------------------------------------------
	def set_value(self, value):
		""""""
		self.edit(value=value)
	#----------------------------------------------------------------------
	value = property(get_value, set_value)
########################################################################
class OptionMenuGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.optionMenuGrp(**kwargs)
			super(OptionMenuGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.optionMenuGrp(name, exists=True):
				super(OptionMenuGrp, self).__init__(name)
			else:
				name = cmds.optionMenuGrp(name, **kwargs)
				super(OptionMenuGrp, self).__init__(name, **dict(qtParent=parent))
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
	def columnWidth(self,value):
		""""""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	def columnWidth1(self,value):
		""""""
		self.edit(columnWidth1=value)
	#----------------------------------------------------------------------
	def columnWidth2(self,value):
		""""""
		self.edit(columnWidth2=value)
	#----------------------------------------------------------------------
	def columnWidth3(self,value):
		""""""
		self.edit(columnWidth3=value)
	#----------------------------------------------------------------------
	def columnWidth4(self,value):
		""""""
		self.edit(columnWidth4=value)
	#----------------------------------------------------------------------
	def columnWidth5(self,value):
		""""""
		self.edit(columnWidth5=value)
	#----------------------------------------------------------------------
	def columnWidth6(self,value):
		""""""
		self.edit(columnWidth6=value)
	#----------------------------------------------------------------------
	def columnAttach(self,value):
		""""""
		self.edit(columnAttach=value)
	#----------------------------------------------------------------------
	def columnAttach2(self,value):
		""""""
		self.edit(columnAttach2=value)
	#----------------------------------------------------------------------
	def columnAttach3(self,value):
		""""""
		self.edit(columnAttach3=value)
	#----------------------------------------------------------------------
	def columnAttach4(self,value):
		""""""
		self.edit(columnAttach4=value)
	#----------------------------------------------------------------------
	def columnAttach5(self,value):
		""""""
		self.edit(columnAttach5=value)
	#----------------------------------------------------------------------
	def columnAttach6(self,value):
		""""""
		self.edit(columnAttach6=value)
	#----------------------------------------------------------------------
	def columnOffset2(self,value):
		""""""
		self.edit(columnOffset2=value)
	#----------------------------------------------------------------------
	def columnOffset3(self,value):
		""""""
		self.edit(columnOffset3=value)
	#----------------------------------------------------------------------
	def columnOffset4(self,value):
		""""""
		self.edit(columnOffset4=value)
	#----------------------------------------------------------------------
	def columnOffset5(self,value):
		""""""
		self.edit(columnOffset5=value)
	#----------------------------------------------------------------------
	def columnOffset6(self,value):
		""""""
		self.edit(columnOffset6=value)
	#----------------------------------------------------------------------
	def rowAttach(self,value):
		""""""
		self.edit(rowAttach=value)
	#----------------------------------------------------------------------
	def columnAlign(self,value):
		""""""
		self.edit(columnAlign=value)
	#----------------------------------------------------------------------
	def columnAlign2(self,value):
		""""""
		self.edit(columnAlign2=value)
	#----------------------------------------------------------------------
	def columnAlign3(self,value):
		""""""
		self.edit(columnAlign3=value)
	#----------------------------------------------------------------------
	def columnAlign4(self,value):
		""""""
		self.edit(columnAlign4=value)
	#----------------------------------------------------------------------
	def columnAlign5(self,value):
		""""""
		self.edit(columnAlign5=value)
	#----------------------------------------------------------------------
	def columnAlign6(self,value):
		""""""
		self.edit(columnAlign6=value)
	#----------------------------------------------------------------------
	def adjustableColumn(self,value):
		""""""
		self.edit(adjustableColumn=value)
	#----------------------------------------------------------------------
	def adjustableColumn2(self,value):
		""""""
		self.edit(adjustableColumn2=value)
	#----------------------------------------------------------------------
	def adjustableColumn3(self,value):
		""""""
		self.edit(adjustableColumn3=value)
	#----------------------------------------------------------------------
	def adjustableColumn4(self,value):
		""""""
		self.edit(adjustableColumn4=value)
	#----------------------------------------------------------------------
	def adjustableColumn5(self,value):
		""""""
		self.edit(adjustableColumn5=value)
	#----------------------------------------------------------------------
	def adjustableColumn6(self,value):
		""""""
		self.edit(adjustableColumn6=value)
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
	def get_extraLabel(self):
		""""""
		return self.query(extraLabel=True)
	#----------------------------------------------------------------------
	def set_extraLabel(self, value):
		""""""
		self.edit(extraLabel=value)
	#----------------------------------------------------------------------
	extraLabel = property(get_extraLabel, set_extraLabel)
	#----------------------------------------------------------------------
	@property
	def itemListShort(self):
		""""""
		return self.query(itemListShort=True)
	#----------------------------------------------------------------------
	@property
	def itemListLong(self):
		""""""
		return self.query(itemListLong=True)
	#----------------------------------------------------------------------
	@property
	def numberOfItems(self):
		""""""
		return self.query(numberOfItems=True)
	#----------------------------------------------------------------------
	def get_select(self):
		""""""
		return self.query(select=True)
	#----------------------------------------------------------------------
	def set_select(self, value):
		""""""
		self.edit(select=value)
	#----------------------------------------------------------------------
	select = property(get_select, set_select)
	#----------------------------------------------------------------------
	def get_value(self):
		""""""
		return self.query(value=True)
	#----------------------------------------------------------------------
	def set_value(self, value):
		""""""
		self.edit(value=value)
	#----------------------------------------------------------------------
	value = property(get_value, set_value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
########################################################################
class PopupMenu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.popupMenu(**kwargs)
			super(PopupMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.popupMenu(name, exists=True):
				super(PopupMenu, self).__init__(name)
			else:
				name = cmds.popupMenu(name, **kwargs)
				super(PopupMenu, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_altModifier(self):
		""""""
		return self.query(altModifier=True)
	#----------------------------------------------------------------------
	def set_altModifier(self, value):
		""""""
		self.edit(altModifier=value)
	#----------------------------------------------------------------------
	altModifier = property(get_altModifier, set_altModifier)
	#----------------------------------------------------------------------
	def get_ctrlModifier(self):
		""""""
		return self.query(ctrlModifier=True)
	#----------------------------------------------------------------------
	def set_ctrlModifier(self, value):
		""""""
		self.edit(ctrlModifier=value)
	#----------------------------------------------------------------------
	ctrlModifier = property(get_ctrlModifier, set_ctrlModifier)
	#----------------------------------------------------------------------
	def get_shiftModifier(self):
		""""""
		return self.query(shiftModifier=True)
	#----------------------------------------------------------------------
	def set_shiftModifier(self, value):
		""""""
		self.edit(shiftModifier=value)
	#----------------------------------------------------------------------
	shiftModifier = property(get_shiftModifier, set_shiftModifier)
	#----------------------------------------------------------------------
	def get_button(self):
		""""""
		return self.query(button=True)
	#----------------------------------------------------------------------
	def set_button(self, value):
		""""""
		self.edit(button=value)
	#----------------------------------------------------------------------
	button = property(get_button, set_button)
	#----------------------------------------------------------------------
	@property
	def allowOptionBoxes(self):
		""""""
		return self.query(allowOptionBoxes=True)
	#----------------------------------------------------------------------
	def get_markingMenu(self):
		""""""
		return self.query(markingMenu=True)
	#----------------------------------------------------------------------
	def set_markingMenu(self, value):
		""""""
		self.edit(markingMenu=value)
	#----------------------------------------------------------------------
	markingMenu = property(get_markingMenu, set_markingMenu)
	#----------------------------------------------------------------------
	def postMenuCommand(self,value):
		""""""
		self.edit(postMenuCommand=value)
	#----------------------------------------------------------------------
	def get_postMenuCommandOnce(self):
		""""""
		return self.query(postMenuCommandOnce=True)
	#----------------------------------------------------------------------
	def set_postMenuCommandOnce(self, value):
		""""""
		self.edit(postMenuCommandOnce=value)
	#----------------------------------------------------------------------
	postMenuCommandOnce = property(get_postMenuCommandOnce, set_postMenuCommandOnce)
	#----------------------------------------------------------------------
	@property
	def numberOfItems(self):
		""""""
		return self.query(numberOfItems=True)
	#----------------------------------------------------------------------
	@property
	def itemArray(self):
		""""""
		return self.query(itemArray=True)
	#----------------------------------------------------------------------
	def deleteAllItems(self,value):
		""""""
		self.edit(deleteAllItems=value)
########################################################################
class RadioMenuItemCollection(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.radioMenuItemCollection(**kwargs)
			super(RadioMenuItemCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.radioMenuItemCollection(name, exists=True):
				super(RadioMenuItemCollection, self).__init__(name)
			else:
				name = cmds.radioMenuItemCollection(name, **kwargs)
				super(RadioMenuItemCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gl(self):
		""""""
		return self.query(gl=True)
########################################################################
class SaveMenu(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveMenu(**kwargs)
			super(SaveMenu, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveMenu(name, exists=True):
				super(SaveMenu, self).__init__(name)
			else:
				name = cmds.saveMenu(name, **kwargs)
				super(SaveMenu, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gl(self):
		""""""
		return self.query(gl=True)