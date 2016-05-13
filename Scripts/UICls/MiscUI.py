import maya.cmds as cmds
import UI_Object


########################################################################
class Annotate(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.annotate(**kwargs)
			super(Annotate, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.annotate(name, exists=True):
				super(Annotate, self).__init__(name)
			else:
				name = cmds.annotate(name, **kwargs)
				super(Annotate, self).__init__(name, **dict(qtParent=parent))
########################################################################
class AutoPlace(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.autoPlace(**kwargs)
			super(AutoPlace, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.autoPlace(name, exists=True):
				super(AutoPlace, self).__init__(name)
			else:
				name = cmds.autoPlace(name, **kwargs)
				super(AutoPlace, self).__init__(name, **dict(qtParent=parent))
########################################################################
class ButtonManip(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.buttonManip(**kwargs)
			super(ButtonManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.buttonManip(name, exists=True):
				super(ButtonManip, self).__init__(name)
			else:
				name = cmds.buttonManip(name, **kwargs)
				super(ButtonManip, self).__init__(name, **dict(qtParent=parent))
########################################################################
class Callbacks(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.callbacks(**kwargs)
			super(Callbacks, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.callbacks(name, exists=True):
				super(Callbacks, self).__init__(name)
			else:
				name = cmds.callbacks(name, **kwargs)
				super(Callbacks, self).__init__(name, **dict(qtParent=parent))
########################################################################
class GrabColor(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.grabColor(**kwargs)
			super(GrabColor, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.grabColor(name, exists=True):
				super(GrabColor, self).__init__(name)
			else:
				name = cmds.grabColor(name, **kwargs)
				super(GrabColor, self).__init__(name, **dict(qtParent=parent))
########################################################################
class HeadsUpDisplay(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
		if cmds.headsUpDisplay(name, exists=True):
			self._id = name
			super(HeadsUpDisplay, self).__init__(name)
		else:
			self._id = cmds.headsUpDisplay(name, **kwargs)
			super(HeadsUpDisplay, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def name(self,value):
		""""""
		self.edit(name=value)
	#----------------------------------------------------------------------
	@property
	def exists(self):
		""""""
		return self.query(exists=True)
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
	def get_layoutVisibility(self):
		""""""
		return self.query(layoutVisibility=True)
	#----------------------------------------------------------------------
	def set_layoutVisibility(self, value):
		""""""
		self.edit(layoutVisibility=value)
	#----------------------------------------------------------------------
	layoutVisibility = property(get_layoutVisibility, set_layoutVisibility)
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
	def get_allowOverlap(self):
		""""""
		return self.query(allowOverlap=True)
	#----------------------------------------------------------------------
	def set_allowOverlap(self, value):
		""""""
		self.edit(allowOverlap=value)
	#----------------------------------------------------------------------
	allowOverlap = property(get_allowOverlap, set_allowOverlap)
	#----------------------------------------------------------------------
	def get_section(self):
		""""""
		return self.query(section=True)
	#----------------------------------------------------------------------
	def set_section(self, value):
		""""""
		self.edit(section=value)
	#----------------------------------------------------------------------
	section = property(get_section, set_section)
	#----------------------------------------------------------------------
	def get_block(self):
		""""""
		return self.query(block=True)
	#----------------------------------------------------------------------
	def set_block(self, value):
		""""""
		self.edit(block=value)
	#----------------------------------------------------------------------
	block = property(get_block, set_block)
	#----------------------------------------------------------------------
	def get_blockSize(self):
		""""""
		return self.query(blockSize=True)
	#----------------------------------------------------------------------
	def set_blockSize(self, value):
		""""""
		self.edit(blockSize=value)
	#----------------------------------------------------------------------
	blockSize = property(get_blockSize, set_blockSize)
	#----------------------------------------------------------------------
	def get_padding(self):
		""""""
		return self.query(padding=True)
	#----------------------------------------------------------------------
	def set_padding(self, value):
		""""""
		self.edit(padding=value)
	#----------------------------------------------------------------------
	padding = property(get_padding, set_padding)
	#----------------------------------------------------------------------
	def get_blockAlignment(self):
		""""""
		return self.query(blockAlignment=True)
	#----------------------------------------------------------------------
	def set_blockAlignment(self, value):
		""""""
		self.edit(blockAlignment=value)
	#----------------------------------------------------------------------
	blockAlignment = property(get_blockAlignment, set_blockAlignment)
	#----------------------------------------------------------------------
	def get_labelFontSize(self):
		""""""
		return self.query(labelFontSize=True)
	#----------------------------------------------------------------------
	def set_labelFontSize(self, value):
		""""""
		self.edit(labelFontSize=value)
	#----------------------------------------------------------------------
	labelFontSize = property(get_labelFontSize, set_labelFontSize)
	#----------------------------------------------------------------------
	def get_dataFontSize(self):
		""""""
		return self.query(dataFontSize=True)
	#----------------------------------------------------------------------
	def set_dataFontSize(self, value):
		""""""
		self.edit(dataFontSize=value)
	#----------------------------------------------------------------------
	dataFontSize = property(get_dataFontSize, set_dataFontSize)
	#----------------------------------------------------------------------
	def get_dataAlignment(self):
		""""""
		return self.query(dataAlignment=True)
	#----------------------------------------------------------------------
	def set_dataAlignment(self, value):
		""""""
		self.edit(dataAlignment=value)
	#----------------------------------------------------------------------
	dataAlignment = property(get_dataAlignment, set_dataAlignment)
	#----------------------------------------------------------------------
	def get_labelWidth(self):
		""""""
		return self.query(labelWidth=True)
	#----------------------------------------------------------------------
	def set_labelWidth(self, value):
		""""""
		self.edit(labelWidth=value)
	#----------------------------------------------------------------------
	labelWidth = property(get_labelWidth, set_labelWidth)
	#----------------------------------------------------------------------
	def get_dataWidth(self):
		""""""
		return self.query(dataWidth=True)
	#----------------------------------------------------------------------
	def set_dataWidth(self, value):
		""""""
		self.edit(dataWidth=value)
	#----------------------------------------------------------------------
	dataWidth = property(get_dataWidth, set_dataWidth)
	#----------------------------------------------------------------------
	def get_decimalPrecision(self):
		""""""
		return self.query(decimalPrecision=True)
	#----------------------------------------------------------------------
	def set_decimalPrecision(self, value):
		""""""
		self.edit(decimalPrecision=value)
	#----------------------------------------------------------------------
	decimalPrecision = property(get_decimalPrecision, set_decimalPrecision)
	#----------------------------------------------------------------------
	def get_showGrid(self):
		""""""
		return self.query(showGrid=True)
	#----------------------------------------------------------------------
	def set_showGrid(self, value):
		""""""
		self.edit(showGrid=value)
	#----------------------------------------------------------------------
	showGrid = property(get_showGrid, set_showGrid)
	#----------------------------------------------------------------------
	def get_gridColor(self):
		""""""
		return self.query(gridColor=True)
	#----------------------------------------------------------------------
	def set_gridColor(self, value):
		""""""
		self.edit(gridColor=value)
	#----------------------------------------------------------------------
	gridColor = property(get_gridColor, set_gridColor)
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
	def get_nodeChanges(self):
		""""""
		return self.query(nodeChanges=True)
	#----------------------------------------------------------------------
	def set_nodeChanges(self, value):
		""""""
		self.edit(nodeChanges=value)
	#----------------------------------------------------------------------
	nodeChanges = property(get_nodeChanges, set_nodeChanges)
	#----------------------------------------------------------------------
	def resetNodeChanges(self,value):
		""""""
		self.edit(resetNodeChanges=value)
	#----------------------------------------------------------------------
	def get_attachToRefresh(self):
		""""""
		return self.query(attachToRefresh=True)
	#----------------------------------------------------------------------
	def set_attachToRefresh(self, value):
		""""""
		self.edit(attachToRefresh=value)
	#----------------------------------------------------------------------
	attachToRefresh = property(get_attachToRefresh, set_attachToRefresh)
	#----------------------------------------------------------------------
	def conditionTrue(self,value):
		""""""
		self.edit(conditionTrue=value)
	#----------------------------------------------------------------------
	def conditionFalse(self,value):
		""""""
		self.edit(conditionFalse=value)
	#----------------------------------------------------------------------
	def conditionChange(self,value):
		""""""
		self.edit(conditionChange=value)
	#----------------------------------------------------------------------
	def event(self,value):
		""""""
		self.edit(event=value)
	#----------------------------------------------------------------------
	def attributeChange(self,value):
		""""""
		self.edit(attributeChange=value)
	#----------------------------------------------------------------------
	def connectionChange(self,value):
		""""""
		self.edit(connectionChange=value)
	#----------------------------------------------------------------------
	def disregardIndex(self,value):
		""""""
		self.edit(disregardIndex=value)
	#----------------------------------------------------------------------
	def allDescendants(self,value):
		""""""
		self.edit(allDescendants=value)
	#----------------------------------------------------------------------
	def get_preset(self):
		""""""
		return self.query(preset=True)
	#----------------------------------------------------------------------
	def set_preset(self, value):
		""""""
		self.edit(preset=value)
	#----------------------------------------------------------------------
	preset = property(get_preset, set_preset)
	#----------------------------------------------------------------------
	@property
	def listConditions(self):
		""""""
		return self.query(listConditions=True)
	#----------------------------------------------------------------------
	@property
	def listEvents(self):
		""""""
		return self.query(listEvents=True)
	#----------------------------------------------------------------------
	@property
	def listHeadsUpDisplays(self):
		""""""
		return self.query(listHeadsUpDisplays=True)
	#----------------------------------------------------------------------
	@property
	def listNodeChanges(self):
		""""""
		return self.query(listNodeChanges=True)
	#----------------------------------------------------------------------
	@property
	def listPresets(self):
		""""""
		return self.query(listPresets=True)
	#----------------------------------------------------------------------
	@property
	def scriptResult(self):
		""""""
		return self.query(scriptResult=True)
	#----------------------------------------------------------------------
	def remove(self,value):
		""""""
		self.edit(remove=value)
	#----------------------------------------------------------------------
	def removeID(self,value):
		""""""
		self.edit(removeID=value)
	#----------------------------------------------------------------------
	def removePosition(self,value):
		""""""
		self.edit(removePosition=value)
	#----------------------------------------------------------------------
	def setOption(self,value):
		""""""
		self.edit(setOption=value)
	#----------------------------------------------------------------------
	@property
	def getOption(self):
		""""""
		return self.query(getOption=True)
########################################################################
class HeadsUpMessage(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.headsUpMessage(**kwargs)
			super(HeadsUpMessage, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.headsUpMessage(name, exists=True):
				super(HeadsUpMessage, self).__init__(name)
			else:
				name = cmds.headsUpMessage(name, **kwargs)
				super(HeadsUpMessage, self).__init__(name, **dict(qtParent=parent))
########################################################################
class Hotkey(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotkey(**kwargs)
			super(Hotkey, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotkey(name, exists=True):
				super(Hotkey, self).__init__(name)
			else:
				name = cmds.hotkey(name, **kwargs)
				super(Hotkey, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def altModifier(self):
		""""""
		return self.query(altModifier=True)
	#----------------------------------------------------------------------
	@property
	def ctrlModifier(self):
		""""""
		return self.query(ctrlModifier=True)
	#----------------------------------------------------------------------
	@property
	def name(self):
		""""""
		return self.query(name=True)
	#----------------------------------------------------------------------
	@property
	def releaseName(self):
		""""""
		return self.query(releaseName=True)
########################################################################
class HotkeyCheck(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.hotkeyCheck(**kwargs)
			super(HotkeyCheck, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.hotkeyCheck(name, exists=True):
				super(HotkeyCheck, self).__init__(name)
			else:
				name = cmds.hotkeyCheck(name, **kwargs)
				super(HotkeyCheck, self).__init__(name, **dict(qtParent=parent))
########################################################################
class InViewMessage(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.inViewMessage(**kwargs)
			super(InViewMessage, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.inViewMessage(name, exists=True):
				super(InViewMessage, self).__init__(name)
			else:
				name = cmds.inViewMessage(name, **kwargs)
				super(InViewMessage, self).__init__(name, **dict(qtParent=parent))
########################################################################
class LinearPrecision(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.linearPrecision(**kwargs)
			super(LinearPrecision, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.linearPrecision(name, exists=True):
				super(LinearPrecision, self).__init__(name)
			else:
				name = cmds.linearPrecision(name, **kwargs)
				super(LinearPrecision, self).__init__(name, **dict(qtParent=parent))
########################################################################
class LoadPrefObjects(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.loadPrefObjects(**kwargs)
			super(LoadPrefObjects, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.loadPrefObjects(name, exists=True):
				super(LoadPrefObjects, self).__init__(name)
			else:
				name = cmds.loadPrefObjects(name, **kwargs)
				super(LoadPrefObjects, self).__init__(name, **dict(qtParent=parent))
########################################################################
class LoadUI(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.loadUI(**kwargs)
			super(LoadUI, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.loadUI(name, exists=True):
				super(LoadUI, self).__init__(name)
			else:
				name = cmds.loadUI(name, **kwargs)
				super(LoadUI, self).__init__(name, **dict(qtParent=parent))
########################################################################
class NameCommand(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nameCommand(**kwargs)
			super(NameCommand, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nameCommand(name, exists=True):
				super(NameCommand, self).__init__(name)
			else:
				name = cmds.nameCommand(name, **kwargs)
				super(NameCommand, self).__init__(name, **dict(qtParent=parent))
########################################################################
class OverrideModifier(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.overrideModifier(**kwargs)
			super(OverrideModifier, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.overrideModifier(name, exists=True):
				super(OverrideModifier, self).__init__(name)
			else:
				name = cmds.overrideModifier(name, **kwargs)
				super(OverrideModifier, self).__init__(name, **dict(qtParent=parent))
########################################################################
class SaveAllShelves(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveAllShelves(**kwargs)
			super(SaveAllShelves, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveAllShelves(name, exists=True):
				super(SaveAllShelves, self).__init__(name)
			else:
				name = cmds.saveAllShelves(name, **kwargs)
				super(SaveAllShelves, self).__init__(name, **dict(qtParent=parent))
########################################################################
class SavePrefObjects(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.savePrefObjects(**kwargs)
			super(SavePrefObjects, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.savePrefObjects(name, exists=True):
				super(SavePrefObjects, self).__init__(name)
			else:
				name = cmds.savePrefObjects(name, **kwargs)
				super(SavePrefObjects, self).__init__(name, **dict(qtParent=parent))
########################################################################
class SavePrefs(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.savePrefs(**kwargs)
			super(SavePrefs, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.savePrefs(name, exists=True):
				super(SavePrefs, self).__init__(name)
			else:
				name = cmds.savePrefs(name, **kwargs)
				super(SavePrefs, self).__init__(name, **dict(qtParent=parent))
########################################################################
class SaveShelf(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.saveShelf(**kwargs)
			super(SaveShelf, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.saveShelf(name, exists=True):
				super(SaveShelf, self).__init__(name)
			else:
				name = cmds.saveShelf(name, **kwargs)
				super(SaveShelf, self).__init__(name, **dict(qtParent=parent))
########################################################################
class Scmh(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scmh(**kwargs)
			super(Scmh, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scmh(name, exists=True):
				super(Scmh, self).__init__(name)
			else:
				name = cmds.scmh(name, **kwargs)
				super(Scmh, self).__init__(name, **dict(qtParent=parent))
########################################################################
class SetMenuMode(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setMenuMode(**kwargs)
			super(SetMenuMode, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setMenuMode(name, exists=True):
				super(SetMenuMode, self).__init__(name)
			else:
				name = cmds.setMenuMode(name, **kwargs)
				super(SetMenuMode, self).__init__(name, **dict(qtParent=parent))
########################################################################
class SetNodeTypeFlag(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setNodeTypeFlag(**kwargs)
			super(SetNodeTypeFlag, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setNodeTypeFlag(name, exists=True):
				super(SetNodeTypeFlag, self).__init__(name)
			else:
				name = cmds.setNodeTypeFlag(name, **kwargs)
				super(SetNodeTypeFlag, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def threadSafe(self):
		""""""
		return self.query(threadSafe=True)
########################################################################
class SetStartupMessage(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.setStartupMessage(**kwargs)
			super(SetStartupMessage, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.setStartupMessage(name, exists=True):
				super(SetStartupMessage, self).__init__(name)
			else:
				name = cmds.setStartupMessage(name, **kwargs)
				super(SetStartupMessage, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def threadSafe(self):
		""""""
		return self.query(threadSafe=True)
########################################################################
class TextManip(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textManip(**kwargs)
			super(TextManip, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textManip(name, exists=True):
				super(TextManip, self).__init__(name)
			else:
				name = cmds.textManip(name, **kwargs)
				super(TextManip, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def visible(self):
		""""""
		return self.query(visible=True)
