__all__ = ['AttrColorSliderGrp'     , 'AttrControlGrp'          , 'AttrFieldGrp',
           'AttrFieldSliderGrp'     , 'AttrNavigationControlGrp', 'TreeView'    , 
           'Button'                 , 'Canvas'                  , 'ChannelBox'  ,
           'CheckBox'               , 'CheckBoxGrp'             , 'CmdScrollFieldExecuter',
           'CmdScrollFieldReporter' , 'CmdShell'                , 'ColorIndexSliderGrp',
           'ColorSliderButtonGrp'   , 'ColorSliderGrp'          , 'CommandLine',
           'ComponentBox'           , 'Control'                 , 'FloatField',
           'FloatFieldGrp'          , 'FloatScrollBar'          , 'FloatSlider',
           'FloatSlider2'           , 'FloatSliderButtonGrp'    , 'FloatSliderGrp',
           'GradientControl'        , 'GradientControlNoAttr'   , 'HelpLine',
           'HudButton'              , 'HudSlider'               , 'HudSliderButton',
           'IconTextButton'         , 'IconTextCheckBox'        , 'IconTextRadioButton',
           'IconTextRadioCollection', 'IconTextScrollList'      , 'IconTextStaticLabel',
           'Image'                  , 'IntField'                , 'IntFieldGrp',
           'IntScrollBar'           , 'IntSlider'               , 'IntSliderGrp',
           'LayerButton'            , 'MessageLine'             , 'NameField',
           'NodeTreeLister'         , 'PalettePort'             , 'Picture',
           'ProgressBar'            , 'RadioButton'             , 'RadioButtonGrp',
           'RadioCollection'        , 'RangeControl'            , 'ScriptTable',
           'ScrollField'            , 'Separator'               , 'ShelfButton',
           'SoundControl'           , 'SwatchDisplayPort'       , 'SwitchTable',
           'SymbolButton'           , 'SymbolCheckBox'          , 'Text',
           'TextField'              , 'TextFieldButtonGrp'      , 'TextFieldGrp',
           'TextScrollList'         , 'TimeControl'             , 'TimePort',
           'ToolButton'             , 'ToolCollection'          , 'TreeLister']
import maya.cmds as cmds
import UI_Object
reload(UI_Object)

########################################################################
class AttrColorSliderGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrColorSliderGrp(**kwargs)
			super(AttrColorSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrColorSliderGrp(name, exists=True):
				super(AttrColorSliderGrp, self).__init__(name)
			else:
				name = cmds.attrColorSliderGrp(name, **kwargs)
				super(AttrColorSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_attribute(self):
		""""""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		""""""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
	#----------------------------------------------------------------------
	def get_attrNavDecision(self):
		""""""
		return self.query(attrNavDecision=True)
	#----------------------------------------------------------------------
	def set_attrNavDecision(self, value):
		""""""
		self.edit(attrNavDecision=value)
	#----------------------------------------------------------------------
	attrNavDecision = property(get_attrNavDecision, set_attrNavDecision)
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
	def get_rgbValue(self):
		""""""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	def set_rgbValue(self, value):
		""""""
		self.edit(rgbValue=value)
	#----------------------------------------------------------------------
	rgbValue = property(get_rgbValue, set_rgbValue)
	#----------------------------------------------------------------------
	def get_hsvValue(self):
		""""""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	def set_hsvValue(self, value):
		""""""
		self.edit(hsvValue=value)
	#----------------------------------------------------------------------
	hsvValue = property(get_hsvValue, set_hsvValue)
	#----------------------------------------------------------------------
	def get_showButton(self):
		""""""
		return self.query(showButton=True)
	#----------------------------------------------------------------------
	def set_showButton(self, value):
		""""""
		self.edit(showButton=value)
	#----------------------------------------------------------------------
	showButton = property(get_showButton, set_showButton)
########################################################################
class AttrControlGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrControlGrp(**kwargs)
			super(AttrControlGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrControlGrp(name, exists=True):
				super(AttrControlGrp, self).__init__(name)
			else:
				name = cmds.attrControlGrp(name, **kwargs)
				super(AttrControlGrp, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_attribute(self):
		""""""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		""""""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
	#----------------------------------------------------------------------
	def get_changeCommand(self):
		""""""
		return self.query(changeCommand=True)
	#----------------------------------------------------------------------
	def set_changeCommand(self, value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	changeCommand = property(get_changeCommand, set_changeCommand)
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
	def get_hideMapButton(self):
		""""""
		return self.query(hideMapButton=True)
	#----------------------------------------------------------------------
	def set_hideMapButton(self, value):
		""""""
		self.edit(hideMapButton=value)
	#----------------------------------------------------------------------
	hideMapButton = property(get_hideMapButton, set_hideMapButton)
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
	def get_handlesAttribute(self):
		""""""
		return self.query(handlesAttribute=True)
	#----------------------------------------------------------------------
	def set_handlesAttribute(self, value):
		""""""
		self.edit(handlesAttribute=value)
	#----------------------------------------------------------------------
	handlesAttribute = property(get_handlesAttribute, set_handlesAttribute)
########################################################################
class AttrFieldGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrFieldGrp(**kwargs)
			super(AttrFieldGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrFieldGrp(name, exists=True):
				super(AttrFieldGrp, self).__init__(name)
			else:
				name = cmds.attrFieldGrp(name, **kwargs)
				super(AttrFieldGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_attribute(self):
		""""""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		""""""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
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
	def precision(self,value):
		""""""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
########################################################################
class AttrFieldSliderGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrFieldSliderGrp(**kwargs)
			super(AttrFieldSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrFieldSliderGrp(name, exists=True):
				super(AttrFieldSliderGrp, self).__init__(name)
			else:
				name = cmds.attrFieldSliderGrp(name, **kwargs)
				super(AttrFieldSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_attribute(self):
		""""""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		""""""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
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
	def get_fieldMinValue(self):
		""""""
		return self.query(fieldMinValue=True)
	#----------------------------------------------------------------------
	def set_fieldMinValue(self, value):
		""""""
		self.edit(fieldMinValue=value)
	#----------------------------------------------------------------------
	fieldMinValue = property(get_fieldMinValue, set_fieldMinValue)
	#----------------------------------------------------------------------
	def get_fieldMaxValue(self):
		""""""
		return self.query(fieldMaxValue=True)
	#----------------------------------------------------------------------
	def set_fieldMaxValue(self, value):
		""""""
		self.edit(fieldMaxValue=value)
	#----------------------------------------------------------------------
	fieldMaxValue = property(get_fieldMaxValue, set_fieldMaxValue)
	#----------------------------------------------------------------------
	def get_sliderMinValue(self):
		""""""
		return self.query(sliderMinValue=True)
	#----------------------------------------------------------------------
	def set_sliderMinValue(self, value):
		""""""
		self.edit(sliderMinValue=value)
	#----------------------------------------------------------------------
	sliderMinValue = property(get_sliderMinValue, set_sliderMinValue)
	#----------------------------------------------------------------------
	def get_sliderMaxValue(self):
		""""""
		return self.query(sliderMaxValue=True)
	#----------------------------------------------------------------------
	def set_sliderMaxValue(self, value):
		""""""
		self.edit(sliderMaxValue=value)
	#----------------------------------------------------------------------
	sliderMaxValue = property(get_sliderMaxValue, set_sliderMaxValue)
	#----------------------------------------------------------------------
	def precision(self,value):
		""""""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_fieldStep(self):
		""""""
		return self.query(fieldStep=True)
	#----------------------------------------------------------------------
	def set_fieldStep(self, value):
		""""""
		self.edit(fieldStep=value)
	#----------------------------------------------------------------------
	fieldStep = property(get_fieldStep, set_fieldStep)
	#----------------------------------------------------------------------
	def get_sliderStep(self):
		""""""
		return self.query(sliderStep=True)
	#----------------------------------------------------------------------
	def set_sliderStep(self, value):
		""""""
		self.edit(sliderStep=value)
	#----------------------------------------------------------------------
	sliderStep = property(get_sliderStep, set_sliderStep)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	@property
	def vertical(self):
		""""""
		return self.query(vertical=True)
########################################################################
class AttrNavigationControlGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.attrNavigationControlGrp(**kwargs)
			super(AttrNavigationControlGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.attrNavigationControlGrp(name, exists=True):
				super(AttrNavigationControlGrp, self).__init__(name)
			else:
				name = cmds.attrNavigationControlGrp(name, **kwargs)
				super(AttrNavigationControlGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_attribute(self):
		""""""
		return self.query(attribute=True)
	#----------------------------------------------------------------------
	def set_attribute(self, value):
		""""""
		self.edit(attribute=value)
	#----------------------------------------------------------------------
	attribute = property(get_attribute, set_attribute)
	#----------------------------------------------------------------------
	def get_attrNavDecision(self):
		""""""
		return self.query(attrNavDecision=True)
	#----------------------------------------------------------------------
	def set_attrNavDecision(self, value):
		""""""
		self.edit(attrNavDecision=value)
	#----------------------------------------------------------------------
	attrNavDecision = property(get_attrNavDecision, set_attrNavDecision)
	#----------------------------------------------------------------------
	def get_createNew(self):
		""""""
		return self.query(createNew=True)
	#----------------------------------------------------------------------
	def set_createNew(self, value):
		""""""
		self.edit(createNew=value)
	#----------------------------------------------------------------------
	createNew = property(get_createNew, set_createNew)
	#----------------------------------------------------------------------
	def get_connectToExisting(self):
		""""""
		return self.query(connectToExisting=True)
	#----------------------------------------------------------------------
	def set_connectToExisting(self, value):
		""""""
		self.edit(connectToExisting=value)
	#----------------------------------------------------------------------
	connectToExisting = property(get_connectToExisting, set_connectToExisting)
	#----------------------------------------------------------------------
	def get_connectNodeToDropped(self):
		""""""
		return self.query(connectNodeToDropped=True)
	#----------------------------------------------------------------------
	def set_connectNodeToDropped(self, value):
		""""""
		self.edit(connectNodeToDropped=value)
	#----------------------------------------------------------------------
	connectNodeToDropped = property(get_connectNodeToDropped, set_connectNodeToDropped)
	#----------------------------------------------------------------------
	def get_connectAttrToDropped(self):
		""""""
		return self.query(connectAttrToDropped=True)
	#----------------------------------------------------------------------
	def set_connectAttrToDropped(self, value):
		""""""
		self.edit(connectAttrToDropped=value)
	#----------------------------------------------------------------------
	connectAttrToDropped = property(get_connectAttrToDropped, set_connectAttrToDropped)
	#----------------------------------------------------------------------
	def get_disconnect(self):
		""""""
		return self.query(disconnect=True)
	#----------------------------------------------------------------------
	def set_disconnect(self, value):
		""""""
		self.edit(disconnect=value)
	#----------------------------------------------------------------------
	disconnect = property(get_disconnect, set_disconnect)
	#----------------------------------------------------------------------
	def get_ignore(self):
		""""""
		return self.query(ignore=True)
	#----------------------------------------------------------------------
	def set_ignore(self, value):
		""""""
		self.edit(ignore=value)
	#----------------------------------------------------------------------
	ignore = property(get_ignore, set_ignore)
	#----------------------------------------------------------------------
	def get_unignore(self):
		""""""
		return self.query(unignore=True)
	#----------------------------------------------------------------------
	def set_unignore(self, value):
		""""""
		self.edit(unignore=value)
	#----------------------------------------------------------------------
	unignore = property(get_unignore, set_unignore)
	#----------------------------------------------------------------------
	def get_delete(self):
		""""""
		return self.query(delete=True)
	#----------------------------------------------------------------------
	def set_delete(self, value):
		""""""
		self.edit(delete=value)
	#----------------------------------------------------------------------
	delete = property(get_delete, set_delete)
	#----------------------------------------------------------------------
	def get_relatedNodes(self):
		""""""
		return self.query(relatedNodes=True)
	#----------------------------------------------------------------------
	def set_relatedNodes(self, value):
		""""""
		self.edit(relatedNodes=value)
	#----------------------------------------------------------------------
	relatedNodes = property(get_relatedNodes, set_relatedNodes)
	#----------------------------------------------------------------------
	def get_defaultTraversal(self):
		""""""
		return self.query(defaultTraversal=True)
	#----------------------------------------------------------------------
	def set_defaultTraversal(self, value):
		""""""
		self.edit(defaultTraversal=value)
	#----------------------------------------------------------------------
	defaultTraversal = property(get_defaultTraversal, set_defaultTraversal)
########################################################################
class Button(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.button(**kwargs)
			super(Button, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.button(name, exists=True):
				super(Button, self).__init__(name)
			else:
				name = cmds.button(name, **kwargs)
				super(Button, self).__init__(name, **dict(qtParent=parent))
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_recomputeSize(self):
		""""""
		return self.query(recomputeSize=True)
	#----------------------------------------------------------------------
	def set_recomputeSize(self, value):
		""""""
		self.edit(recomputeSize=value)
	#----------------------------------------------------------------------
	recomputeSize = property(get_recomputeSize, set_recomputeSize)
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
	def get_actOnPress(self):
		""""""
		return self.query(actOnPress=True)
	#----------------------------------------------------------------------
	def set_actOnPress(self, value):
		""""""
		self.edit(actOnPress=value)
	#----------------------------------------------------------------------
	actOnPress = property(get_actOnPress, set_actOnPress)
	#----------------------------------------------------------------------
	def get_actionIsSubstitute(self):
		""""""
		return self.query(actionIsSubstitute=True)
	#----------------------------------------------------------------------
	def set_actionIsSubstitute(self, value):
		""""""
		self.edit(actionIsSubstitute=value)
	#----------------------------------------------------------------------
	actionIsSubstitute = property(get_actionIsSubstitute, set_actionIsSubstitute)
########################################################################
class Canvas(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.canvas(**kwargs)
			super(Canvas, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.canvas(name, exists=True):
				super(Canvas, self).__init__(name)
			else:
				name = cmds.canvas(name, **kwargs)
				super(Canvas, self).__init__(name, **dict(qtParent=parent))
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
	def get_rgbValue(self):
		""""""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	def set_rgbValue(self, value):
		""""""
		self.edit(rgbValue=value)
	#----------------------------------------------------------------------
	rgbValue = property(get_rgbValue, set_rgbValue)
	#----------------------------------------------------------------------
	def get_hsvValue(self):
		""""""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	def set_hsvValue(self, value):
		""""""
		self.edit(hsvValue=value)
	#----------------------------------------------------------------------
	hsvValue = property(get_hsvValue, set_hsvValue)
	#----------------------------------------------------------------------
	def pressCommand(self,value):
		""""""
		self.edit(pressCommand=value)
########################################################################
class ChannelBox(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.channelBox(**kwargs)
			super(ChannelBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.channelBox(name, exists=True):
				super(ChannelBox, self).__init__(name)
			else:
				name = cmds.channelBox(name, **kwargs)
				super(ChannelBox, self).__init__(name, **dict(qtParent=parent))
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
	def get_attributeEditorMode(self):
		""""""
		return self.query(attributeEditorMode=True)
	#----------------------------------------------------------------------
	def set_attributeEditorMode(self, value):
		""""""
		self.edit(attributeEditorMode=value)
	#----------------------------------------------------------------------
	attributeEditorMode = property(get_attributeEditorMode, set_attributeEditorMode)
	#----------------------------------------------------------------------
	def get_enableLabelSelection(self):
		""""""
		return self.query(enableLabelSelection=True)
	#----------------------------------------------------------------------
	def set_enableLabelSelection(self, value):
		""""""
		self.edit(enableLabelSelection=value)
	#----------------------------------------------------------------------
	enableLabelSelection = property(get_enableLabelSelection, set_enableLabelSelection)
	#----------------------------------------------------------------------
	def get_maxWidth(self):
		""""""
		return self.query(maxWidth=True)
	#----------------------------------------------------------------------
	def set_maxWidth(self, value):
		""""""
		self.edit(maxWidth=value)
	#----------------------------------------------------------------------
	maxWidth = property(get_maxWidth, set_maxWidth)
	#----------------------------------------------------------------------
	def get_maxHeight(self):
		""""""
		return self.query(maxHeight=True)
	#----------------------------------------------------------------------
	def set_maxHeight(self, value):
		""""""
		self.edit(maxHeight=value)
	#----------------------------------------------------------------------
	maxHeight = property(get_maxHeight, set_maxHeight)
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
	def get_fieldWidth(self):
		""""""
		return self.query(fieldWidth=True)
	#----------------------------------------------------------------------
	def set_fieldWidth(self, value):
		""""""
		self.edit(fieldWidth=value)
	#----------------------------------------------------------------------
	fieldWidth = property(get_fieldWidth, set_fieldWidth)
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
	@property
	def mainObjectList(self):
		""""""
		return self.query(mainObjectList=True)
	#----------------------------------------------------------------------
	@property
	def shapeObjectList(self):
		""""""
		return self.query(shapeObjectList=True)
	#----------------------------------------------------------------------
	@property
	def historyObjectList(self):
		""""""
		return self.query(historyObjectList=True)
	#----------------------------------------------------------------------
	@property
	def outputObjectList(self):
		""""""
		return self.query(outputObjectList=True)
	#----------------------------------------------------------------------
	@property
	def selectedMainAttributes(self):
		""""""
		return self.query(selectedMainAttributes=True)
	#----------------------------------------------------------------------
	@property
	def selectedShapeAttributes(self):
		""""""
		return self.query(selectedShapeAttributes=True)
	#----------------------------------------------------------------------
	@property
	def selectedHistoryAttributes(self):
		""""""
		return self.query(selectedHistoryAttributes=True)
	#----------------------------------------------------------------------
	@property
	def selectedOutputAttributes(self):
		""""""
		return self.query(selectedOutputAttributes=True)
	#----------------------------------------------------------------------
	def execute(self,value):
		""""""
		self.edit(execute=value)
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
	def get_useManips(self):
		""""""
		return self.query(useManips=True)
	#----------------------------------------------------------------------
	def set_useManips(self, value):
		""""""
		self.edit(useManips=value)
	#----------------------------------------------------------------------
	useManips = property(get_useManips, set_useManips)
	#----------------------------------------------------------------------
	def takeFocus(self,value):
		""""""
		self.edit(takeFocus=value)
	#----------------------------------------------------------------------
	def get_hyperbolic(self):
		""""""
		return self.query(hyperbolic=True)
	#----------------------------------------------------------------------
	def set_hyperbolic(self, value):
		""""""
		self.edit(hyperbolic=value)
	#----------------------------------------------------------------------
	hyperbolic = property(get_hyperbolic, set_hyperbolic)
	#----------------------------------------------------------------------
	def get_speed(self):
		""""""
		return self.query(speed=True)
	#----------------------------------------------------------------------
	def set_speed(self, value):
		""""""
		self.edit(speed=value)
	#----------------------------------------------------------------------
	speed = property(get_speed, set_speed)
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
	def get_attrColor(self):
		""""""
		return self.query(attrColor=True)
	#----------------------------------------------------------------------
	def set_attrColor(self, value):
		""""""
		self.edit(attrColor=value)
	#----------------------------------------------------------------------
	attrColor = property(get_attrColor, set_attrColor)
	#----------------------------------------------------------------------
	def get_attrBgColor(self):
		""""""
		return self.query(attrBgColor=True)
	#----------------------------------------------------------------------
	def set_attrBgColor(self, value):
		""""""
		self.edit(attrBgColor=value)
	#----------------------------------------------------------------------
	attrBgColor = property(get_attrBgColor, set_attrBgColor)
	#----------------------------------------------------------------------
	def get_nodeRegex(self):
		""""""
		return self.query(nodeRegex=True)
	#----------------------------------------------------------------------
	def set_nodeRegex(self, value):
		""""""
		self.edit(nodeRegex=value)
	#----------------------------------------------------------------------
	nodeRegex = property(get_nodeRegex, set_nodeRegex)
	#----------------------------------------------------------------------
	def get_attrRegex(self):
		""""""
		return self.query(attrRegex=True)
	#----------------------------------------------------------------------
	def set_attrRegex(self, value):
		""""""
		self.edit(attrRegex=value)
	#----------------------------------------------------------------------
	attrRegex = property(get_attrRegex, set_attrRegex)
	#----------------------------------------------------------------------
	def update(self,value):
		""""""
		self.edit(update=value)
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
	def get_containerAtTop(self):
		""""""
		return self.query(containerAtTop=True)
	#----------------------------------------------------------------------
	def set_containerAtTop(self, value):
		""""""
		self.edit(containerAtTop=value)
	#----------------------------------------------------------------------
	containerAtTop = property(get_containerAtTop, set_containerAtTop)
########################################################################
class CheckBox(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.checkBox(**kwargs)
			super(CheckBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.checkBox(name, exists=True):
				super(CheckBox, self).__init__(name)
			else:
				name = cmds.checkBox(name, **kwargs)
				super(CheckBox, self).__init__(name, **dict(qtParent=parent))
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def get_recomputeSize(self):
		""""""
		return self.query(recomputeSize=True)
	#----------------------------------------------------------------------
	def set_recomputeSize(self, value):
		""""""
		self.edit(recomputeSize=value)
	#----------------------------------------------------------------------
	recomputeSize = property(get_recomputeSize, set_recomputeSize)
	#----------------------------------------------------------------------
	def onCommand(self,value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
########################################################################
class CheckBoxGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.checkBoxGrp(**kwargs)
			super(CheckBoxGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.checkBoxGrp(name, exists=True):
				super(CheckBoxGrp, self).__init__(name)
			else:
				name = cmds.checkBoxGrp(name, **kwargs)
				super(CheckBoxGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_label1(self):
		""""""
		return self.query(label1=True)
	#----------------------------------------------------------------------
	def set_label1(self, value):
		""""""
		self.edit(label1=value)
	#----------------------------------------------------------------------
	label1 = property(get_label1, set_label1)
	#----------------------------------------------------------------------
	def get_label2(self):
		""""""
		return self.query(label2=True)
	#----------------------------------------------------------------------
	def set_label2(self, value):
		""""""
		self.edit(label2=value)
	#----------------------------------------------------------------------
	label2 = property(get_label2, set_label2)
	#----------------------------------------------------------------------
	def get_label3(self):
		""""""
		return self.query(label3=True)
	#----------------------------------------------------------------------
	def set_label3(self, value):
		""""""
		self.edit(label3=value)
	#----------------------------------------------------------------------
	label3 = property(get_label3, set_label3)
	#----------------------------------------------------------------------
	def get_label4(self):
		""""""
		return self.query(label4=True)
	#----------------------------------------------------------------------
	def set_label4(self, value):
		""""""
		self.edit(label4=value)
	#----------------------------------------------------------------------
	label4 = property(get_label4, set_label4)
	#----------------------------------------------------------------------
	def get_labelArray2(self):
		""""""
		return self.query(labelArray2=True)
	#----------------------------------------------------------------------
	def set_labelArray2(self, value):
		""""""
		self.edit(labelArray2=value)
	#----------------------------------------------------------------------
	labelArray2 = property(get_labelArray2, set_labelArray2)
	#----------------------------------------------------------------------
	def get_labelArray3(self):
		""""""
		return self.query(labelArray3=True)
	#----------------------------------------------------------------------
	def set_labelArray3(self, value):
		""""""
		self.edit(labelArray3=value)
	#----------------------------------------------------------------------
	labelArray3 = property(get_labelArray3, set_labelArray3)
	#----------------------------------------------------------------------
	def labelArray4(self,value):
		""""""
		self.edit(labelArray4=value)
	#----------------------------------------------------------------------
	def get_value1(self):
		""""""
		return self.query(value1=True)
	#----------------------------------------------------------------------
	def set_value1(self, value):
		""""""
		self.edit(value1=value)
	#----------------------------------------------------------------------
	value1 = property(get_value1, set_value1)
	#----------------------------------------------------------------------
	def get_value2(self):
		""""""
		return self.query(value2=True)
	#----------------------------------------------------------------------
	def set_value2(self, value):
		""""""
		self.edit(value2=value)
	#----------------------------------------------------------------------
	value2 = property(get_value2, set_value2)
	#----------------------------------------------------------------------
	def get_value3(self):
		""""""
		return self.query(value3=True)
	#----------------------------------------------------------------------
	def set_value3(self, value):
		""""""
		self.edit(value3=value)
	#----------------------------------------------------------------------
	value3 = property(get_value3, set_value3)
	#----------------------------------------------------------------------
	def get_value4(self):
		""""""
		return self.query(value4=True)
	#----------------------------------------------------------------------
	def set_value4(self, value):
		""""""
		self.edit(value4=value)
	#----------------------------------------------------------------------
	value4 = property(get_value4, set_value4)
	#----------------------------------------------------------------------
	def get_valueArray2(self):
		""""""
		return self.query(valueArray2=True)
	#----------------------------------------------------------------------
	def set_valueArray2(self, value):
		""""""
		self.edit(valueArray2=value)
	#----------------------------------------------------------------------
	valueArray2 = property(get_valueArray2, set_valueArray2)
	#----------------------------------------------------------------------
	def get_valueArray3(self):
		""""""
		return self.query(valueArray3=True)
	#----------------------------------------------------------------------
	def set_valueArray3(self, value):
		""""""
		self.edit(valueArray3=value)
	#----------------------------------------------------------------------
	valueArray3 = property(get_valueArray3, set_valueArray3)
	#----------------------------------------------------------------------
	def valueArray4(self,value):
		""""""
		self.edit(valueArray4=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def changeCommand1(self,value):
		""""""
		self.edit(changeCommand1=value)
	#----------------------------------------------------------------------
	def changeCommand2(self,value):
		""""""
		self.edit(changeCommand2=value)
	#----------------------------------------------------------------------
	def changeCommand3(self,value):
		""""""
		self.edit(changeCommand3=value)
	#----------------------------------------------------------------------
	def changeCommand4(self,value):
		""""""
		self.edit(changeCommand4=value)
	#----------------------------------------------------------------------
	def onCommand(self,value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	def onCommand1(self,value):
		""""""
		self.edit(onCommand1=value)
	#----------------------------------------------------------------------
	def onCommand2(self,value):
		""""""
		self.edit(onCommand2=value)
	#----------------------------------------------------------------------
	def onCommand3(self,value):
		""""""
		self.edit(onCommand3=value)
	#----------------------------------------------------------------------
	def onCommand4(self,value):
		""""""
		self.edit(onCommand4=value)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def offCommand1(self,value):
		""""""
		self.edit(offCommand1=value)
	#----------------------------------------------------------------------
	def offCommand2(self,value):
		""""""
		self.edit(offCommand2=value)
	#----------------------------------------------------------------------
	def offCommand3(self,value):
		""""""
		self.edit(offCommand3=value)
	#----------------------------------------------------------------------
	def offCommand4(self,value):
		""""""
		self.edit(offCommand4=value)
	#----------------------------------------------------------------------
	def get_enable1(self):
		""""""
		return self.query(enable1=True)
	#----------------------------------------------------------------------
	def set_enable1(self, value):
		""""""
		self.edit(enable1=value)
	#----------------------------------------------------------------------
	enable1 = property(get_enable1, set_enable1)
	#----------------------------------------------------------------------
	def get_enable2(self):
		""""""
		return self.query(enable2=True)
	#----------------------------------------------------------------------
	def set_enable2(self, value):
		""""""
		self.edit(enable2=value)
	#----------------------------------------------------------------------
	enable2 = property(get_enable2, set_enable2)
	#----------------------------------------------------------------------
	def get_enable3(self):
		""""""
		return self.query(enable3=True)
	#----------------------------------------------------------------------
	def set_enable3(self, value):
		""""""
		self.edit(enable3=value)
	#----------------------------------------------------------------------
	enable3 = property(get_enable3, set_enable3)
	#----------------------------------------------------------------------
	def get_enable4(self):
		""""""
		return self.query(enable4=True)
	#----------------------------------------------------------------------
	def set_enable4(self, value):
		""""""
		self.edit(enable4=value)
	#----------------------------------------------------------------------
	enable4 = property(get_enable4, set_enable4)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	@property
	def vertical(self):
		""""""
		return self.query(vertical=True)
########################################################################
class CmdScrollFieldExecuter(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.cmdScrollFieldExecuter(**kwargs)
			super(CmdScrollFieldExecuter, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.cmdScrollFieldExecuter(name, exists=True):
				super(CmdScrollFieldExecuter, self).__init__(name)
			else:
				name = cmds.cmdScrollFieldExecuter(name, **kwargs)
				super(CmdScrollFieldExecuter, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def load(self,value):
		""""""
		self.edit(load=value)
	#----------------------------------------------------------------------
	def source(self,value):
		""""""
		self.edit(source=value)
	#----------------------------------------------------------------------
	def saveSelection(self,value):
		""""""
		self.edit(saveSelection=value)
	#----------------------------------------------------------------------
	def saveSelectionToShelf(self,value):
		""""""
		self.edit(saveSelectionToShelf=value)
	#----------------------------------------------------------------------
	def selectAll(self,value):
		""""""
		self.edit(selectAll=value)
	#----------------------------------------------------------------------
	def select(self,value):
		""""""
		self.edit(select=value)
	#----------------------------------------------------------------------
	@property
	def hasSelection(self):
		""""""
		return self.query(hasSelection=True)
	#----------------------------------------------------------------------
	@property
	def selectedText(self):
		""""""
		return self.query(selectedText=True)
	#----------------------------------------------------------------------
	def clear(self,value):
		""""""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def get_text(self):
		""""""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		""""""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	@property
	def textLength(self):
		""""""
		return self.query(textLength=True)
	#----------------------------------------------------------------------
	def cutSelection(self,value):
		""""""
		self.edit(cutSelection=value)
	#----------------------------------------------------------------------
	def copySelection(self,value):
		""""""
		self.edit(copySelection=value)
	#----------------------------------------------------------------------
	def pasteSelection(self,value):
		""""""
		self.edit(pasteSelection=value)
	#----------------------------------------------------------------------
	@property
	def hasFocus(self):
		""""""
		return self.query(hasFocus=True)
	#----------------------------------------------------------------------
	def undo(self,value):
		""""""
		self.edit(undo=value)
	#----------------------------------------------------------------------
	def redo(self,value):
		""""""
		self.edit(redo=value)
	#----------------------------------------------------------------------
	def execute(self,value):
		""""""
		self.edit(execute=value)
	#----------------------------------------------------------------------
	def executeAll(self,value):
		""""""
		self.edit(executeAll=value)
	#----------------------------------------------------------------------
	def storeContents(self,value):
		""""""
		self.edit(storeContents=value)
	#----------------------------------------------------------------------
	def loadContents(self,value):
		""""""
		self.edit(loadContents=value)
	#----------------------------------------------------------------------
	def removeStoredContents(self,value):
		""""""
		self.edit(removeStoredContents=value)
	#----------------------------------------------------------------------
	def appendText(self,value):
		""""""
		self.edit(appendText=value)
	#----------------------------------------------------------------------
	def insertText(self,value):
		""""""
		self.edit(insertText=value)
	#----------------------------------------------------------------------
	@property
	def sourceType(self):
		""""""
		return self.query(sourceType=True)
	#----------------------------------------------------------------------
	def get_showLineNumbers(self):
		""""""
		return self.query(showLineNumbers=True)
	#----------------------------------------------------------------------
	def set_showLineNumbers(self, value):
		""""""
		self.edit(showLineNumbers=value)
	#----------------------------------------------------------------------
	showLineNumbers = property(get_showLineNumbers, set_showLineNumbers)
	#----------------------------------------------------------------------
	def get_commandCompletion(self):
		""""""
		return self.query(commandCompletion=True)
	#----------------------------------------------------------------------
	def set_commandCompletion(self, value):
		""""""
		self.edit(commandCompletion=value)
	#----------------------------------------------------------------------
	commandCompletion = property(get_commandCompletion, set_commandCompletion)
	#----------------------------------------------------------------------
	def get_objectPathCompletion(self):
		""""""
		return self.query(objectPathCompletion=True)
	#----------------------------------------------------------------------
	def set_objectPathCompletion(self, value):
		""""""
		self.edit(objectPathCompletion=value)
	#----------------------------------------------------------------------
	objectPathCompletion = property(get_objectPathCompletion, set_objectPathCompletion)
	#----------------------------------------------------------------------
	def get_showTooltipHelp(self):
		""""""
		return self.query(showTooltipHelp=True)
	#----------------------------------------------------------------------
	def set_showTooltipHelp(self, value):
		""""""
		self.edit(showTooltipHelp=value)
	#----------------------------------------------------------------------
	showTooltipHelp = property(get_showTooltipHelp, set_showTooltipHelp)
	#----------------------------------------------------------------------
	def get_searchDown(self):
		""""""
		return self.query(searchDown=True)
	#----------------------------------------------------------------------
	def set_searchDown(self, value):
		""""""
		self.edit(searchDown=value)
	#----------------------------------------------------------------------
	searchDown = property(get_searchDown, set_searchDown)
	#----------------------------------------------------------------------
	def get_searchMatchCase(self):
		""""""
		return self.query(searchMatchCase=True)
	#----------------------------------------------------------------------
	def set_searchMatchCase(self, value):
		""""""
		self.edit(searchMatchCase=value)
	#----------------------------------------------------------------------
	searchMatchCase = property(get_searchMatchCase, set_searchMatchCase)
	#----------------------------------------------------------------------
	def get_searchWraps(self):
		""""""
		return self.query(searchWraps=True)
	#----------------------------------------------------------------------
	def set_searchWraps(self, value):
		""""""
		self.edit(searchWraps=value)
	#----------------------------------------------------------------------
	searchWraps = property(get_searchWraps, set_searchWraps)
	#----------------------------------------------------------------------
	def get_searchString(self):
		""""""
		return self.query(searchString=True)
	#----------------------------------------------------------------------
	def set_searchString(self, value):
		""""""
		self.edit(searchString=value)
	#----------------------------------------------------------------------
	searchString = property(get_searchString, set_searchString)
	#----------------------------------------------------------------------
	@property
	def searchAndSelect(self):
		""""""
		return self.query(searchAndSelect=True)
	#----------------------------------------------------------------------
	def replaceAll(self,value):
		""""""
		self.edit(replaceAll=value)
	#----------------------------------------------------------------------
	def get_currentLine(self):
		""""""
		return self.query(currentLine=True)
	#----------------------------------------------------------------------
	def set_currentLine(self, value):
		""""""
		self.edit(currentLine=value)
	#----------------------------------------------------------------------
	currentLine = property(get_currentLine, set_currentLine)
	#----------------------------------------------------------------------
	@property
	def numberOfLines(self):
		""""""
		return self.query(numberOfLines=True)
	#----------------------------------------------------------------------
	def get_spacesPerTab(self):
		""""""
		return self.query(spacesPerTab=True)
	#----------------------------------------------------------------------
	def set_spacesPerTab(self, value):
		""""""
		self.edit(spacesPerTab=value)
	#----------------------------------------------------------------------
	spacesPerTab = property(get_spacesPerTab, set_spacesPerTab)
	#----------------------------------------------------------------------
	def get_filterKeyPress(self):
		""""""
		return self.query(filterKeyPress=True)
	#----------------------------------------------------------------------
	def set_filterKeyPress(self, value):
		""""""
		self.edit(filterKeyPress=value)
	#----------------------------------------------------------------------
	filterKeyPress = property(get_filterKeyPress, set_filterKeyPress)
	#----------------------------------------------------------------------
	def get_tabsForIndent(self):
		""""""
		return self.query(tabsForIndent=True)
	#----------------------------------------------------------------------
	def set_tabsForIndent(self, value):
		""""""
		self.edit(tabsForIndent=value)
	#----------------------------------------------------------------------
	tabsForIndent = property(get_tabsForIndent, set_tabsForIndent)
	#----------------------------------------------------------------------
	def get_autoCloseBraces(self):
		""""""
		return self.query(autoCloseBraces=True)
	#----------------------------------------------------------------------
	def set_autoCloseBraces(self, value):
		""""""
		self.edit(autoCloseBraces=value)
	#----------------------------------------------------------------------
	autoCloseBraces = property(get_autoCloseBraces, set_autoCloseBraces)
########################################################################
class CmdScrollFieldReporter(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.cmdScrollFieldReporter(**kwargs)
			super(CmdScrollFieldReporter, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.cmdScrollFieldReporter(name, exists=True):
				super(CmdScrollFieldReporter, self).__init__(name)
			else:
				name = cmds.cmdScrollFieldReporter(name, **kwargs)
				super(CmdScrollFieldReporter, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_filterSourceType(self):
		""""""
		return self.query(filterSourceType=True)
	#----------------------------------------------------------------------
	def set_filterSourceType(self, value):
		""""""
		self.edit(filterSourceType=value)
	#----------------------------------------------------------------------
	filterSourceType = property(get_filterSourceType, set_filterSourceType)
	#----------------------------------------------------------------------
	def saveSelection(self,value):
		""""""
		self.edit(saveSelection=value)
	#----------------------------------------------------------------------
	def saveSelectionToShelf(self,value):
		""""""
		self.edit(saveSelectionToShelf=value)
	#----------------------------------------------------------------------
	def selectAll(self,value):
		""""""
		self.edit(selectAll=value)
	#----------------------------------------------------------------------
	def select(self,value):
		""""""
		self.edit(select=value)
	#----------------------------------------------------------------------
	def clear(self,value):
		""""""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def get_text(self):
		""""""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		""""""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	@property
	def textLength(self):
		""""""
		return self.query(textLength=True)
	#----------------------------------------------------------------------
	def cutSelection(self,value):
		""""""
		self.edit(cutSelection=value)
	#----------------------------------------------------------------------
	def copySelection(self,value):
		""""""
		self.edit(copySelection=value)
	#----------------------------------------------------------------------
	def pasteSelection(self,value):
		""""""
		self.edit(pasteSelection=value)
	#----------------------------------------------------------------------
	@property
	def hasFocus(self):
		""""""
		return self.query(hasFocus=True)
	#----------------------------------------------------------------------
	def receiveFocusCommand(self,value):
		""""""
		self.edit(receiveFocusCommand=value)
	#----------------------------------------------------------------------
	def get_echoAllCommands(self):
		""""""
		return self.query(echoAllCommands=True)
	#----------------------------------------------------------------------
	def set_echoAllCommands(self, value):
		""""""
		self.edit(echoAllCommands=value)
	#----------------------------------------------------------------------
	echoAllCommands = property(get_echoAllCommands, set_echoAllCommands)
	#----------------------------------------------------------------------
	def get_lineNumbers(self):
		""""""
		return self.query(lineNumbers=True)
	#----------------------------------------------------------------------
	def set_lineNumbers(self, value):
		""""""
		self.edit(lineNumbers=value)
	#----------------------------------------------------------------------
	lineNumbers = property(get_lineNumbers, set_lineNumbers)
	#----------------------------------------------------------------------
	def get_stackTrace(self):
		""""""
		return self.query(stackTrace=True)
	#----------------------------------------------------------------------
	def set_stackTrace(self, value):
		""""""
		self.edit(stackTrace=value)
	#----------------------------------------------------------------------
	stackTrace = property(get_stackTrace, set_stackTrace)
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
	def get_suppressStackTrace(self):
		""""""
		return self.query(suppressStackTrace=True)
	#----------------------------------------------------------------------
	def set_suppressStackTrace(self, value):
		""""""
		self.edit(suppressStackTrace=value)
	#----------------------------------------------------------------------
	suppressStackTrace = property(get_suppressStackTrace, set_suppressStackTrace)
########################################################################
class CmdShell(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.cmdShell(**kwargs)
			super(CmdShell, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.cmdShell(name, exists=True):
				super(CmdShell, self).__init__(name)
			else:
				name = cmds.cmdShell(name, **kwargs)
				super(CmdShell, self).__init__(name, **dict(qtParent=parent))
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
	def get_prompt(self):
		""""""
		return self.query(prompt=True)
	#----------------------------------------------------------------------
	def set_prompt(self, value):
		""""""
		self.edit(prompt=value)
	#----------------------------------------------------------------------
	prompt = property(get_prompt, set_prompt)
	#----------------------------------------------------------------------
	def get_numberOfSavedLines(self):
		""""""
		return self.query(numberOfSavedLines=True)
	#----------------------------------------------------------------------
	def set_numberOfSavedLines(self, value):
		""""""
		self.edit(numberOfSavedLines=value)
	#----------------------------------------------------------------------
	numberOfSavedLines = property(get_numberOfSavedLines, set_numberOfSavedLines)
	#----------------------------------------------------------------------
	def get_numberOfHistoryLines(self):
		""""""
		return self.query(numberOfHistoryLines=True)
	#----------------------------------------------------------------------
	def set_numberOfHistoryLines(self, value):
		""""""
		self.edit(numberOfHistoryLines=value)
	#----------------------------------------------------------------------
	numberOfHistoryLines = property(get_numberOfHistoryLines, set_numberOfHistoryLines)
########################################################################
class ColorIndexSliderGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.colorIndexSliderGrp(**kwargs)
			super(ColorIndexSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.colorIndexSliderGrp(name, exists=True):
				super(ColorIndexSliderGrp, self).__init__(name)
			else:
				name = cmds.colorIndexSliderGrp(name, **kwargs)
				super(ColorIndexSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_invisible(self):
		""""""
		return self.query(invisible=True)
	#----------------------------------------------------------------------
	def set_invisible(self, value):
		""""""
		self.edit(invisible=value)
	#----------------------------------------------------------------------
	invisible = property(get_invisible, set_invisible)
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
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class ColorSliderButtonGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.colorSliderButtonGrp(**kwargs)
			super(ColorSliderButtonGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.colorSliderButtonGrp(name, exists=True):
				super(ColorSliderButtonGrp, self).__init__(name)
			else:
				name = cmds.colorSliderButtonGrp(name, **kwargs)
				super(ColorSliderButtonGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_rgbValue(self):
		""""""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	def set_rgbValue(self, value):
		""""""
		self.edit(rgbValue=value)
	#----------------------------------------------------------------------
	rgbValue = property(get_rgbValue, set_rgbValue)
	#----------------------------------------------------------------------
	def get_hsvValue(self):
		""""""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	def set_hsvValue(self, value):
		""""""
		self.edit(hsvValue=value)
	#----------------------------------------------------------------------
	hsvValue = property(get_hsvValue, set_hsvValue)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
	#----------------------------------------------------------------------
	def get_buttonLabel(self):
		""""""
		return self.query(buttonLabel=True)
	#----------------------------------------------------------------------
	def set_buttonLabel(self, value):
		""""""
		self.edit(buttonLabel=value)
	#----------------------------------------------------------------------
	buttonLabel = property(get_buttonLabel, set_buttonLabel)
	#----------------------------------------------------------------------
	def buttonCommand(self,value):
		""""""
		self.edit(buttonCommand=value)
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
	def symbolButtonCommand(self,value):
		""""""
		self.edit(symbolButtonCommand=value)
	#----------------------------------------------------------------------
	def get_symbolButtonDisplay(self):
		""""""
		return self.query(symbolButtonDisplay=True)
	#----------------------------------------------------------------------
	def set_symbolButtonDisplay(self, value):
		""""""
		self.edit(symbolButtonDisplay=value)
	#----------------------------------------------------------------------
	symbolButtonDisplay = property(get_symbolButtonDisplay, set_symbolButtonDisplay)
########################################################################
class ColorSliderGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.colorSliderGrp(**kwargs)
			super(ColorSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.colorSliderGrp(name, exists=True):
				super(ColorSliderGrp, self).__init__(name)
			else:
				name = cmds.colorSliderGrp(name, **kwargs)
				super(ColorSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_rgbValue(self):
		""""""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	def set_rgbValue(self, value):
		""""""
		self.edit(rgbValue=value)
	#----------------------------------------------------------------------
	rgbValue = property(get_rgbValue, set_rgbValue)
	#----------------------------------------------------------------------
	def get_hsvValue(self):
		""""""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	def set_hsvValue(self, value):
		""""""
		self.edit(hsvValue=value)
	#----------------------------------------------------------------------
	hsvValue = property(get_hsvValue, set_hsvValue)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class CommandLine(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.commandLine(**kwargs)
			super(CommandLine, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.commandLine(name, exists=True):
				super(CommandLine, self).__init__(name)
			else:
				name = cmds.commandLine(name, **kwargs)
				super(CommandLine, self).__init__(name, **dict(qtParent=parent))
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
	def command(self,value):
		""""""
		self.edit(command=value)
	#----------------------------------------------------------------------
	def enterCommand(self,value):
		""""""
		self.edit(enterCommand=value)
	#----------------------------------------------------------------------
	def get_inputAnnotation(self):
		""""""
		return self.query(inputAnnotation=True)
	#----------------------------------------------------------------------
	def set_inputAnnotation(self, value):
		""""""
		self.edit(inputAnnotation=value)
	#----------------------------------------------------------------------
	inputAnnotation = property(get_inputAnnotation, set_inputAnnotation)
	#----------------------------------------------------------------------
	def get_outputAnnotation(self):
		""""""
		return self.query(outputAnnotation=True)
	#----------------------------------------------------------------------
	def set_outputAnnotation(self, value):
		""""""
		self.edit(outputAnnotation=value)
	#----------------------------------------------------------------------
	outputAnnotation = property(get_outputAnnotation, set_outputAnnotation)
	#----------------------------------------------------------------------
	def get_numberOfHistoryLines(self):
		""""""
		return self.query(numberOfHistoryLines=True)
	#----------------------------------------------------------------------
	def set_numberOfHistoryLines(self, value):
		""""""
		self.edit(numberOfHistoryLines=value)
	#----------------------------------------------------------------------
	numberOfHistoryLines = property(get_numberOfHistoryLines, set_numberOfHistoryLines)
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
	def get_holdFocus(self):
		""""""
		return self.query(holdFocus=True)
	#----------------------------------------------------------------------
	def set_holdFocus(self, value):
		""""""
		self.edit(holdFocus=value)
	#----------------------------------------------------------------------
	holdFocus = property(get_holdFocus, set_holdFocus)
########################################################################
class ComponentBox(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.componentBox(**kwargs)
			super(ComponentBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.componentBox(name, exists=True):
				super(ComponentBox, self).__init__(name)
			else:
				name = cmds.componentBox(name, **kwargs)
				super(ComponentBox, self).__init__(name, **dict(qtParent=parent))
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
	def get_maxWidth(self):
		""""""
		return self.query(maxWidth=True)
	#----------------------------------------------------------------------
	def set_maxWidth(self, value):
		""""""
		self.edit(maxWidth=value)
	#----------------------------------------------------------------------
	maxWidth = property(get_maxWidth, set_maxWidth)
	#----------------------------------------------------------------------
	def get_maxHeight(self):
		""""""
		return self.query(maxHeight=True)
	#----------------------------------------------------------------------
	def set_maxHeight(self, value):
		""""""
		self.edit(maxHeight=value)
	#----------------------------------------------------------------------
	maxHeight = property(get_maxHeight, set_maxHeight)
	#----------------------------------------------------------------------
	def rowHeight(self,value):
		""""""
		self.edit(rowHeight=value)
	#----------------------------------------------------------------------
	@property
	def selectedAttr(self):
		""""""
		return self.query(selectedAttr=True)
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
	def execute(self,value):
		""""""
		self.edit(execute=value)
########################################################################
class Control(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.control(**kwargs)
			super(Control, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.control(name, exists=True):
				super(Control, self).__init__(name)
			else:
				name = cmds.control(name, **kwargs)
				super(Control, self).__init__(name, **dict(qtParent=parent))
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
########################################################################
class FloatField(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatField(**kwargs)
			super(FloatField, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatField(name, exists=True):
				super(FloatField, self).__init__(name)
			else:
				name = cmds.floatField(name, **kwargs)
				super(FloatField, self).__init__(name, **dict(qtParent=parent))
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def enterCommand(self,value):
		""""""
		self.edit(enterCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
	#----------------------------------------------------------------------
	def receiveFocusCommand(self,value):
		""""""
		self.edit(receiveFocusCommand=value)
########################################################################
class FloatFieldGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatFieldGrp(**kwargs)
			super(FloatFieldGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatFieldGrp(name, exists=True):
				super(FloatFieldGrp, self).__init__(name)
			else:
				name = cmds.floatFieldGrp(name, **kwargs)
				super(FloatFieldGrp, self).__init__(name, **dict(qtParent=parent))
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
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
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
	def precision(self,value):
		""""""
		self.edit(precision=value)
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_value1(self):
		""""""
		return self.query(value1=True)
	#----------------------------------------------------------------------
	def set_value1(self, value):
		""""""
		self.edit(value1=value)
	#----------------------------------------------------------------------
	value1 = property(get_value1, set_value1)
	#----------------------------------------------------------------------
	def get_value2(self):
		""""""
		return self.query(value2=True)
	#----------------------------------------------------------------------
	def set_value2(self, value):
		""""""
		self.edit(value2=value)
	#----------------------------------------------------------------------
	value2 = property(get_value2, set_value2)
	#----------------------------------------------------------------------
	def get_value3(self):
		""""""
		return self.query(value3=True)
	#----------------------------------------------------------------------
	def set_value3(self, value):
		""""""
		self.edit(value3=value)
	#----------------------------------------------------------------------
	value3 = property(get_value3, set_value3)
	#----------------------------------------------------------------------
	def get_value4(self):
		""""""
		return self.query(value4=True)
	#----------------------------------------------------------------------
	def set_value4(self, value):
		""""""
		self.edit(value4=value)
	#----------------------------------------------------------------------
	value4 = property(get_value4, set_value4)
	#----------------------------------------------------------------------
	def get_enable1(self):
		""""""
		return self.query(enable1=True)
	#----------------------------------------------------------------------
	def set_enable1(self, value):
		""""""
		self.edit(enable1=value)
	#----------------------------------------------------------------------
	enable1 = property(get_enable1, set_enable1)
	#----------------------------------------------------------------------
	def get_enable2(self):
		""""""
		return self.query(enable2=True)
	#----------------------------------------------------------------------
	def set_enable2(self, value):
		""""""
		self.edit(enable2=value)
	#----------------------------------------------------------------------
	enable2 = property(get_enable2, set_enable2)
	#----------------------------------------------------------------------
	def get_enable3(self):
		""""""
		return self.query(enable3=True)
	#----------------------------------------------------------------------
	def set_enable3(self, value):
		""""""
		self.edit(enable3=value)
	#----------------------------------------------------------------------
	enable3 = property(get_enable3, set_enable3)
	#----------------------------------------------------------------------
	def get_enable4(self):
		""""""
		return self.query(enable4=True)
	#----------------------------------------------------------------------
	def set_enable4(self, value):
		""""""
		self.edit(enable4=value)
	#----------------------------------------------------------------------
	enable4 = property(get_enable4, set_enable4)
########################################################################
class FloatScrollBar(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatScrollBar(**kwargs)
			super(FloatScrollBar, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatScrollBar(name, exists=True):
				super(FloatScrollBar, self).__init__(name)
			else:
				name = cmds.floatScrollBar(name, **kwargs)
				super(FloatScrollBar, self).__init__(name, **dict(qtParent=parent))
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	@property
	def horizontal(self):
		""""""
		return self.query(horizontal=True)
	#----------------------------------------------------------------------
	def get_largeStep(self):
		""""""
		return self.query(largeStep=True)
	#----------------------------------------------------------------------
	def set_largeStep(self, value):
		""""""
		self.edit(largeStep=value)
	#----------------------------------------------------------------------
	largeStep = property(get_largeStep, set_largeStep)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class FloatSlider(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatSlider(**kwargs)
			super(FloatSlider, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatSlider(name, exists=True):
				super(FloatSlider, self).__init__(name)
			else:
				name = cmds.floatSlider(name, **kwargs)
				super(FloatSlider, self).__init__(name, **dict(qtParent=parent))
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	@property
	def horizontal(self):
		""""""
		return self.query(horizontal=True)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class FloatSlider2(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatSlider2(**kwargs)
			super(FloatSlider2, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatSlider2(name, exists=True):
				super(FloatSlider2, self).__init__(name)
			else:
				name = cmds.floatSlider2(name, **kwargs)
				super(FloatSlider2, self).__init__(name, **dict(qtParent=parent))
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
	def get_minimum(self):
		""""""
		return self.query(minimum=True)
	#----------------------------------------------------------------------
	def set_minimum(self, value):
		""""""
		self.edit(minimum=value)
	#----------------------------------------------------------------------
	minimum = property(get_minimum, set_minimum)
	#----------------------------------------------------------------------
	def get_maximum(self):
		""""""
		return self.query(maximum=True)
	#----------------------------------------------------------------------
	def set_maximum(self, value):
		""""""
		self.edit(maximum=value)
	#----------------------------------------------------------------------
	maximum = property(get_maximum, set_maximum)
	#----------------------------------------------------------------------
	def get_polarity(self):
		""""""
		return self.query(polarity=True)
	#----------------------------------------------------------------------
	def set_polarity(self, value):
		""""""
		self.edit(polarity=value)
	#----------------------------------------------------------------------
	polarity = property(get_polarity, set_polarity)
	#----------------------------------------------------------------------
	def get_value1(self):
		""""""
		return self.query(value1=True)
	#----------------------------------------------------------------------
	def set_value1(self, value):
		""""""
		self.edit(value1=value)
	#----------------------------------------------------------------------
	value1 = property(get_value1, set_value1)
	#----------------------------------------------------------------------
	def get_value2(self):
		""""""
		return self.query(value2=True)
	#----------------------------------------------------------------------
	def set_value2(self, value):
		""""""
		self.edit(value2=value)
	#----------------------------------------------------------------------
	value2 = property(get_value2, set_value2)
	#----------------------------------------------------------------------
	def values(self,value):
		""""""
		self.edit(values=value)
	#----------------------------------------------------------------------
	def changeCommand1(self,value):
		""""""
		self.edit(changeCommand1=value)
	#----------------------------------------------------------------------
	def changeCommand2(self,value):
		""""""
		self.edit(changeCommand2=value)
	#----------------------------------------------------------------------
	def positionControl1(self,value):
		""""""
		self.edit(positionControl1=value)
	#----------------------------------------------------------------------
	def positionControl2(self,value):
		""""""
		self.edit(positionControl2=value)
########################################################################
class FloatSliderButtonGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatSliderButtonGrp(**kwargs)
			super(FloatSliderButtonGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatSliderButtonGrp(name, exists=True):
				super(FloatSliderButtonGrp, self).__init__(name)
			else:
				name = cmds.floatSliderButtonGrp(name, **kwargs)
				super(FloatSliderButtonGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_fieldMinValue(self):
		""""""
		return self.query(fieldMinValue=True)
	#----------------------------------------------------------------------
	def set_fieldMinValue(self, value):
		""""""
		self.edit(fieldMinValue=value)
	#----------------------------------------------------------------------
	fieldMinValue = property(get_fieldMinValue, set_fieldMinValue)
	#----------------------------------------------------------------------
	def get_fieldMaxValue(self):
		""""""
		return self.query(fieldMaxValue=True)
	#----------------------------------------------------------------------
	def set_fieldMaxValue(self, value):
		""""""
		self.edit(fieldMaxValue=value)
	#----------------------------------------------------------------------
	fieldMaxValue = property(get_fieldMaxValue, set_fieldMaxValue)
	#----------------------------------------------------------------------
	def precision(self,value):
		""""""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_fieldStep(self):
		""""""
		return self.query(fieldStep=True)
	#----------------------------------------------------------------------
	def set_fieldStep(self, value):
		""""""
		self.edit(fieldStep=value)
	#----------------------------------------------------------------------
	fieldStep = property(get_fieldStep, set_fieldStep)
	#----------------------------------------------------------------------
	def get_sliderStep(self):
		""""""
		return self.query(sliderStep=True)
	#----------------------------------------------------------------------
	def set_sliderStep(self, value):
		""""""
		self.edit(sliderStep=value)
	#----------------------------------------------------------------------
	sliderStep = property(get_sliderStep, set_sliderStep)
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
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
	#----------------------------------------------------------------------
	def get_buttonLabel(self):
		""""""
		return self.query(buttonLabel=True)
	#----------------------------------------------------------------------
	def set_buttonLabel(self, value):
		""""""
		self.edit(buttonLabel=value)
	#----------------------------------------------------------------------
	buttonLabel = property(get_buttonLabel, set_buttonLabel)
	#----------------------------------------------------------------------
	def buttonCommand(self,value):
		""""""
		self.edit(buttonCommand=value)
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
	def symbolButtonCommand(self,value):
		""""""
		self.edit(symbolButtonCommand=value)
	#----------------------------------------------------------------------
	def get_symbolButtonDisplay(self):
		""""""
		return self.query(symbolButtonDisplay=True)
	#----------------------------------------------------------------------
	def set_symbolButtonDisplay(self, value):
		""""""
		self.edit(symbolButtonDisplay=value)
	#----------------------------------------------------------------------
	symbolButtonDisplay = property(get_symbolButtonDisplay, set_symbolButtonDisplay)
########################################################################
class FloatSliderGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.floatSliderGrp(**kwargs)
			super(FloatSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.floatSliderGrp(name, exists=True):
				super(FloatSliderGrp, self).__init__(name)
			else:
				name = cmds.floatSliderGrp(name, **kwargs)
				super(FloatSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_fieldMinValue(self):
		""""""
		return self.query(fieldMinValue=True)
	#----------------------------------------------------------------------
	def set_fieldMinValue(self, value):
		""""""
		self.edit(fieldMinValue=value)
	#----------------------------------------------------------------------
	fieldMinValue = property(get_fieldMinValue, set_fieldMinValue)
	#----------------------------------------------------------------------
	def get_fieldMaxValue(self):
		""""""
		return self.query(fieldMaxValue=True)
	#----------------------------------------------------------------------
	def set_fieldMaxValue(self, value):
		""""""
		self.edit(fieldMaxValue=value)
	#----------------------------------------------------------------------
	fieldMaxValue = property(get_fieldMaxValue, set_fieldMaxValue)
	#----------------------------------------------------------------------
	def precision(self,value):
		""""""
		self.edit(precision=value)
	#----------------------------------------------------------------------
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_fieldStep(self):
		""""""
		return self.query(fieldStep=True)
	#----------------------------------------------------------------------
	def set_fieldStep(self, value):
		""""""
		self.edit(fieldStep=value)
	#----------------------------------------------------------------------
	fieldStep = property(get_fieldStep, set_fieldStep)
	#----------------------------------------------------------------------
	def get_sliderStep(self):
		""""""
		return self.query(sliderStep=True)
	#----------------------------------------------------------------------
	def set_sliderStep(self, value):
		""""""
		self.edit(sliderStep=value)
	#----------------------------------------------------------------------
	sliderStep = property(get_sliderStep, set_sliderStep)
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
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class GradientControl(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.gradientControl(**kwargs)
			super(GradientControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.gradientControl(name, exists=True):
				super(GradientControl, self).__init__(name)
			else:
				name = cmds.gradientControl(name, **kwargs)
				super(GradientControl, self).__init__(name, **dict(qtParent=parent))
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
	def get_adaptiveScaling(self):
		""""""
		return self.query(adaptiveScaling=True)
	#----------------------------------------------------------------------
	def set_adaptiveScaling(self, value):
		""""""
		self.edit(adaptiveScaling=value)
	#----------------------------------------------------------------------
	adaptiveScaling = property(get_adaptiveScaling, set_adaptiveScaling)
	#----------------------------------------------------------------------
	def get_refreshOnRelease(self):
		""""""
		return self.query(refreshOnRelease=True)
	#----------------------------------------------------------------------
	def set_refreshOnRelease(self, value):
		""""""
		self.edit(refreshOnRelease=value)
	#----------------------------------------------------------------------
	refreshOnRelease = property(get_refreshOnRelease, set_refreshOnRelease)
	#----------------------------------------------------------------------
	def get_upperLimitControl(self):
		""""""
		return self.query(upperLimitControl=True)
	#----------------------------------------------------------------------
	def set_upperLimitControl(self, value):
		""""""
		self.edit(upperLimitControl=value)
	#----------------------------------------------------------------------
	upperLimitControl = property(get_upperLimitControl, set_upperLimitControl)
	#----------------------------------------------------------------------
	def selectedColorControl(self,value):
		""""""
		self.edit(selectedColorControl=value)
	#----------------------------------------------------------------------
	def selectedPositionControl(self,value):
		""""""
		self.edit(selectedPositionControl=value)
	#----------------------------------------------------------------------
	def selectedInterpControl(self,value):
		""""""
		self.edit(selectedInterpControl=value)
	#----------------------------------------------------------------------
	@property
	def numberOfControls(self):
		""""""
		return self.query(numberOfControls=True)
	#----------------------------------------------------------------------
	def get_staticNumberOfControls(self):
		""""""
		return self.query(staticNumberOfControls=True)
	#----------------------------------------------------------------------
	def set_staticNumberOfControls(self, value):
		""""""
		self.edit(staticNumberOfControls=value)
	#----------------------------------------------------------------------
	staticNumberOfControls = property(get_staticNumberOfControls, set_staticNumberOfControls)
	#----------------------------------------------------------------------
	def get_staticPositions(self):
		""""""
		return self.query(staticPositions=True)
	#----------------------------------------------------------------------
	def set_staticPositions(self, value):
		""""""
		self.edit(staticPositions=value)
	#----------------------------------------------------------------------
	staticPositions = property(get_staticPositions, set_staticPositions)
	#----------------------------------------------------------------------
	def get_verticalLayout(self):
		""""""
		return self.query(verticalLayout=True)
	#----------------------------------------------------------------------
	def set_verticalLayout(self, value):
		""""""
		self.edit(verticalLayout=value)
	#----------------------------------------------------------------------
	verticalLayout = property(get_verticalLayout, set_verticalLayout)
########################################################################
class GradientControlNoAttr(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.gradientControlNoAttr(**kwargs)
			super(GradientControlNoAttr, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.gradientControlNoAttr(name, exists=True):
				super(GradientControlNoAttr, self).__init__(name)
			else:
				name = cmds.gradientControlNoAttr(name, **kwargs)
				super(GradientControlNoAttr, self).__init__(name, **dict(qtParent=parent))
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
	def get_optionVar(self):
		""""""
		return self.query(optionVar=True)
	#----------------------------------------------------------------------
	def set_optionVar(self, value):
		""""""
		self.edit(optionVar=value)
	#----------------------------------------------------------------------
	optionVar = property(get_optionVar, set_optionVar)
	#----------------------------------------------------------------------
	@property
	def valueAtPoint(self):
		""""""
		return self.query(valueAtPoint=True)
	#----------------------------------------------------------------------
	def get_currentKeyColorValue(self):
		""""""
		return self.query(currentKeyColorValue=True)
	#----------------------------------------------------------------------
	def set_currentKeyColorValue(self, value):
		""""""
		self.edit(currentKeyColorValue=value)
	#----------------------------------------------------------------------
	currentKeyColorValue = property(get_currentKeyColorValue, set_currentKeyColorValue)
	#----------------------------------------------------------------------
	def get_currentKeyCurveValue(self):
		""""""
		return self.query(currentKeyCurveValue=True)
	#----------------------------------------------------------------------
	def set_currentKeyCurveValue(self, value):
		""""""
		self.edit(currentKeyCurveValue=value)
	#----------------------------------------------------------------------
	currentKeyCurveValue = property(get_currentKeyCurveValue, set_currentKeyCurveValue)
	#----------------------------------------------------------------------
	def get_currentKeyInterpValue(self):
		""""""
		return self.query(currentKeyInterpValue=True)
	#----------------------------------------------------------------------
	def set_currentKeyInterpValue(self, value):
		""""""
		self.edit(currentKeyInterpValue=value)
	#----------------------------------------------------------------------
	currentKeyInterpValue = property(get_currentKeyInterpValue, set_currentKeyInterpValue)
	#----------------------------------------------------------------------
	def get_asString(self):
		""""""
		return self.query(asString=True)
	#----------------------------------------------------------------------
	def set_asString(self, value):
		""""""
		self.edit(asString=value)
	#----------------------------------------------------------------------
	asString = property(get_asString, set_asString)
	#----------------------------------------------------------------------
	def get_rampAsColor(self):
		""""""
		return self.query(rampAsColor=True)
	#----------------------------------------------------------------------
	def set_rampAsColor(self, value):
		""""""
		self.edit(rampAsColor=value)
	#----------------------------------------------------------------------
	rampAsColor = property(get_rampAsColor, set_rampAsColor)
	#----------------------------------------------------------------------
	def get_currentKey(self):
		""""""
		return self.query(currentKey=True)
	#----------------------------------------------------------------------
	def set_currentKey(self, value):
		""""""
		self.edit(currentKey=value)
	#----------------------------------------------------------------------
	currentKey = property(get_currentKey, set_currentKey)
	#----------------------------------------------------------------------
	def currentKeyChanged(self,value):
		""""""
		self.edit(currentKeyChanged=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class HelpLine(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.helpLine(**kwargs)
			super(HelpLine, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.helpLine(name, exists=True):
				super(HelpLine, self).__init__(name)
			else:
				name = cmds.helpLine(name, **kwargs)
				super(HelpLine, self).__init__(name, **dict(qtParent=parent))
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
########################################################################
class HudButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		parent = None
		if cmds.headsUpDisplay(name,exists=True):
			self._id = name
			super(HudButton, self).__init__(name)
		else:
			self._id = cmds.hudButton(name, **kwargs)
			super(HudButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_buttonWidth(self):
		""""""
		return self.query(buttonWidth=True)
	#----------------------------------------------------------------------
	def set_buttonWidth(self, value):
		""""""
		self.edit(buttonWidth=value)
	#----------------------------------------------------------------------
	buttonWidth = property(get_buttonWidth, set_buttonWidth)
	#----------------------------------------------------------------------
	def get_buttonShape(self):
		""""""
		return self.query(buttonShape=True)
	#----------------------------------------------------------------------
	def set_buttonShape(self, value):
		""""""
		self.edit(buttonShape=value)
	#----------------------------------------------------------------------
	buttonShape = property(get_buttonShape, set_buttonShape)
	#----------------------------------------------------------------------
	def get_pressCommand(self):
		""""""
		return self.query(pressCommand=True)
	#----------------------------------------------------------------------
	def set_pressCommand(self, value):
		""""""
		self.edit(pressCommand=value)
	#----------------------------------------------------------------------
	pressCommand = property(get_pressCommand, set_pressCommand)
	#----------------------------------------------------------------------
	def get_releaseCommand(self):
		""""""
		return self.query(releaseCommand=True)
	#----------------------------------------------------------------------
	def set_releaseCommand(self, value):
		""""""
		self.edit(releaseCommand=value)
	#----------------------------------------------------------------------
	releaseCommand = property(get_releaseCommand, set_releaseCommand)
########################################################################
class HudSlider(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		parent = None
			
		if cmds.headsUpDisplay(name, exists=True):
			self._id = name
			super(HudSlider, self).__init__(name)
		else:
			self._id = cmds.hudSlider(name, **kwargs)
			super(HudSlider, self).__init__(name, **dict(qtParent=parent))
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
	def get_internalPadding(self):
		""""""
		return self.query(internalPadding=True)
	#----------------------------------------------------------------------
	def set_internalPadding(self, value):
		""""""
		self.edit(internalPadding=value)
	#----------------------------------------------------------------------
	internalPadding = property(get_internalPadding, set_internalPadding)
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
	def get_type(self):
		""""""
		return self.query(type=True)
	#----------------------------------------------------------------------
	def set_type(self, value):
		""""""
		self.edit(type=value)
	#----------------------------------------------------------------------
	type = property(get_type, set_type)
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
	def get_valueFontSize(self):
		""""""
		return self.query(valueFontSize=True)
	#----------------------------------------------------------------------
	def set_valueFontSize(self, value):
		""""""
		self.edit(valueFontSize=value)
	#----------------------------------------------------------------------
	valueFontSize = property(get_valueFontSize, set_valueFontSize)
	#----------------------------------------------------------------------
	def get_valueAlignment(self):
		""""""
		return self.query(valueAlignment=True)
	#----------------------------------------------------------------------
	def set_valueAlignment(self, value):
		""""""
		self.edit(valueAlignment=value)
	#----------------------------------------------------------------------
	valueAlignment = property(get_valueAlignment, set_valueAlignment)
	#----------------------------------------------------------------------
	def get_valueWidth(self):
		""""""
		return self.query(valueWidth=True)
	#----------------------------------------------------------------------
	def set_valueWidth(self, value):
		""""""
		self.edit(valueWidth=value)
	#----------------------------------------------------------------------
	valueWidth = property(get_valueWidth, set_valueWidth)
	#----------------------------------------------------------------------
	def get_sliderLength(self):
		""""""
		return self.query(sliderLength=True)
	#----------------------------------------------------------------------
	def set_sliderLength(self, value):
		""""""
		self.edit(sliderLength=value)
	#----------------------------------------------------------------------
	sliderLength = property(get_sliderLength, set_sliderLength)
	#----------------------------------------------------------------------
	def get_sliderIncrement(self):
		""""""
		return self.query(sliderIncrement=True)
	#----------------------------------------------------------------------
	def set_sliderIncrement(self, value):
		""""""
		self.edit(sliderIncrement=value)
	#----------------------------------------------------------------------
	sliderIncrement = property(get_sliderIncrement, set_sliderIncrement)
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
	def get_pressCommand(self):
		""""""
		return self.query(pressCommand=True)
	#----------------------------------------------------------------------
	def set_pressCommand(self, value):
		""""""
		self.edit(pressCommand=value)
	#----------------------------------------------------------------------
	pressCommand = property(get_pressCommand, set_pressCommand)
	#----------------------------------------------------------------------
	def get_dragCommand(self):
		""""""
		return self.query(dragCommand=True)
	#----------------------------------------------------------------------
	def set_dragCommand(self, value):
		""""""
		self.edit(dragCommand=value)
	#----------------------------------------------------------------------
	dragCommand = property(get_dragCommand, set_dragCommand)
	#----------------------------------------------------------------------
	def get_releaseCommand(self):
		""""""
		return self.query(releaseCommand=True)
	#----------------------------------------------------------------------
	def set_releaseCommand(self, value):
		""""""
		self.edit(releaseCommand=value)
	#----------------------------------------------------------------------
	releaseCommand = property(get_releaseCommand, set_releaseCommand)
########################################################################
class HudSliderButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
		if cmds.headsUpDisplay(name, exists=True):
			self._id = name
			super(HudSliderButton, self).__init__(name)
		else:
			self._id = cmds.hudSliderButton(name, **kwargs)
			super(HudSliderButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_internalPadding(self):
		""""""
		return self.query(internalPadding=True)
	#----------------------------------------------------------------------
	def set_internalPadding(self, value):
		""""""
		self.edit(internalPadding=value)
	#----------------------------------------------------------------------
	internalPadding = property(get_internalPadding, set_internalPadding)
	#----------------------------------------------------------------------
	def get_sliderLabel(self):
		""""""
		return self.query(sliderLabel=True)
	#----------------------------------------------------------------------
	def set_sliderLabel(self, value):
		""""""
		self.edit(sliderLabel=value)
	#----------------------------------------------------------------------
	sliderLabel = property(get_sliderLabel, set_sliderLabel)
	#----------------------------------------------------------------------
	def get_sliderLabelFontSize(self):
		""""""
		return self.query(sliderLabelFontSize=True)
	#----------------------------------------------------------------------
	def set_sliderLabelFontSize(self, value):
		""""""
		self.edit(sliderLabelFontSize=value)
	#----------------------------------------------------------------------
	sliderLabelFontSize = property(get_sliderLabelFontSize, set_sliderLabelFontSize)
	#----------------------------------------------------------------------
	def get_sliderLabelWidth(self):
		""""""
		return self.query(sliderLabelWidth=True)
	#----------------------------------------------------------------------
	def set_sliderLabelWidth(self, value):
		""""""
		self.edit(sliderLabelWidth=value)
	#----------------------------------------------------------------------
	sliderLabelWidth = property(get_sliderLabelWidth, set_sliderLabelWidth)
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
	def get_type(self):
		""""""
		return self.query(type=True)
	#----------------------------------------------------------------------
	def set_type(self, value):
		""""""
		self.edit(type=value)
	#----------------------------------------------------------------------
	type = property(get_type, set_type)
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
	def get_valueFontSize(self):
		""""""
		return self.query(valueFontSize=True)
	#----------------------------------------------------------------------
	def set_valueFontSize(self, value):
		""""""
		self.edit(valueFontSize=value)
	#----------------------------------------------------------------------
	valueFontSize = property(get_valueFontSize, set_valueFontSize)
	#----------------------------------------------------------------------
	def get_valueAlignment(self):
		""""""
		return self.query(valueAlignment=True)
	#----------------------------------------------------------------------
	def set_valueAlignment(self, value):
		""""""
		self.edit(valueAlignment=value)
	#----------------------------------------------------------------------
	valueAlignment = property(get_valueAlignment, set_valueAlignment)
	#----------------------------------------------------------------------
	def get_valueWidth(self):
		""""""
		return self.query(valueWidth=True)
	#----------------------------------------------------------------------
	def set_valueWidth(self, value):
		""""""
		self.edit(valueWidth=value)
	#----------------------------------------------------------------------
	valueWidth = property(get_valueWidth, set_valueWidth)
	#----------------------------------------------------------------------
	def get_sliderLength(self):
		""""""
		return self.query(sliderLength=True)
	#----------------------------------------------------------------------
	def set_sliderLength(self, value):
		""""""
		self.edit(sliderLength=value)
	#----------------------------------------------------------------------
	sliderLength = property(get_sliderLength, set_sliderLength)
	#----------------------------------------------------------------------
	def get_sliderIncrement(self):
		""""""
		return self.query(sliderIncrement=True)
	#----------------------------------------------------------------------
	def set_sliderIncrement(self, value):
		""""""
		self.edit(sliderIncrement=value)
	#----------------------------------------------------------------------
	sliderIncrement = property(get_sliderIncrement, set_sliderIncrement)
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
	def get_sliderPressCommand(self):
		""""""
		return self.query(sliderPressCommand=True)
	#----------------------------------------------------------------------
	def set_sliderPressCommand(self, value):
		""""""
		self.edit(sliderPressCommand=value)
	#----------------------------------------------------------------------
	sliderPressCommand = property(get_sliderPressCommand, set_sliderPressCommand)
	#----------------------------------------------------------------------
	def get_sliderDragCommand(self):
		""""""
		return self.query(sliderDragCommand=True)
	#----------------------------------------------------------------------
	def set_sliderDragCommand(self, value):
		""""""
		self.edit(sliderDragCommand=value)
	#----------------------------------------------------------------------
	sliderDragCommand = property(get_sliderDragCommand, set_sliderDragCommand)
	#----------------------------------------------------------------------
	def get_sliderReleaseCommand(self):
		""""""
		return self.query(sliderReleaseCommand=True)
	#----------------------------------------------------------------------
	def set_sliderReleaseCommand(self, value):
		""""""
		self.edit(sliderReleaseCommand=value)
	#----------------------------------------------------------------------
	sliderReleaseCommand = property(get_sliderReleaseCommand, set_sliderReleaseCommand)
	#----------------------------------------------------------------------
	def get_buttonLabel(self):
		""""""
		return self.query(buttonLabel=True)
	#----------------------------------------------------------------------
	def set_buttonLabel(self, value):
		""""""
		self.edit(buttonLabel=value)
	#----------------------------------------------------------------------
	buttonLabel = property(get_buttonLabel, set_buttonLabel)
	#----------------------------------------------------------------------
	def get_buttonLabelFontSize(self):
		""""""
		return self.query(buttonLabelFontSize=True)
	#----------------------------------------------------------------------
	def set_buttonLabelFontSize(self, value):
		""""""
		self.edit(buttonLabelFontSize=value)
	#----------------------------------------------------------------------
	buttonLabelFontSize = property(get_buttonLabelFontSize, set_buttonLabelFontSize)
	#----------------------------------------------------------------------
	def get_buttonWidth(self):
		""""""
		return self.query(buttonWidth=True)
	#----------------------------------------------------------------------
	def set_buttonWidth(self, value):
		""""""
		self.edit(buttonWidth=value)
	#----------------------------------------------------------------------
	buttonWidth = property(get_buttonWidth, set_buttonWidth)
	#----------------------------------------------------------------------
	def get_buttonShape(self):
		""""""
		return self.query(buttonShape=True)
	#----------------------------------------------------------------------
	def set_buttonShape(self, value):
		""""""
		self.edit(buttonShape=value)
	#----------------------------------------------------------------------
	buttonShape = property(get_buttonShape, set_buttonShape)
	#----------------------------------------------------------------------
	def get_buttonPressCommand(self):
		""""""
		return self.query(buttonPressCommand=True)
	#----------------------------------------------------------------------
	def set_buttonPressCommand(self, value):
		""""""
		self.edit(buttonPressCommand=value)
	#----------------------------------------------------------------------
	buttonPressCommand = property(get_buttonPressCommand, set_buttonPressCommand)
	#----------------------------------------------------------------------
	def get_buttonReleaseCommand(self):
		""""""
		return self.query(buttonReleaseCommand=True)
	#----------------------------------------------------------------------
	def set_buttonReleaseCommand(self, value):
		""""""
		self.edit(buttonReleaseCommand=value)
	#----------------------------------------------------------------------
	buttonReleaseCommand = property(get_buttonReleaseCommand, set_buttonReleaseCommand)
########################################################################
class IconTextButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextButton(**kwargs)
			super(IconTextButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextButton(name, exists=True):
				super(IconTextButton, self).__init__(name)
			else:
				name = cmds.iconTextButton(name, **kwargs)
				super(IconTextButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		""""""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		""""""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
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
	def get_disabledImage(self):
		""""""
		return self.query(disabledImage=True)
	#----------------------------------------------------------------------
	def set_disabledImage(self, value):
		""""""
		self.edit(disabledImage=value)
	#----------------------------------------------------------------------
	disabledImage = property(get_disabledImage, set_disabledImage)
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
	def get_overlayLabelColor(self):
		""""""
		return self.query(overlayLabelColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelColor(self, value):
		""""""
		self.edit(overlayLabelColor=value)
	#----------------------------------------------------------------------
	overlayLabelColor = property(get_overlayLabelColor, set_overlayLabelColor)
	#----------------------------------------------------------------------
	def get_overlayLabelBackColor(self):
		""""""
		return self.query(overlayLabelBackColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelBackColor(self, value):
		""""""
		self.edit(overlayLabelBackColor=value)
	#----------------------------------------------------------------------
	overlayLabelBackColor = property(get_overlayLabelBackColor, set_overlayLabelBackColor)
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_labelOffset(self):
		""""""
		return self.query(labelOffset=True)
	#----------------------------------------------------------------------
	def set_labelOffset(self, value):
		""""""
		self.edit(labelOffset=value)
	#----------------------------------------------------------------------
	labelOffset = property(get_labelOffset, set_labelOffset)
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
	def get_version(self):
		""""""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		""""""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
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
	def get_doubleClickCommand(self):
		""""""
		return self.query(doubleClickCommand=True)
	#----------------------------------------------------------------------
	def set_doubleClickCommand(self, value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	doubleClickCommand = property(get_doubleClickCommand, set_doubleClickCommand)
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
	def get_selectionImage(self):
		""""""
		return self.query(selectionImage=True)
	#----------------------------------------------------------------------
	def set_selectionImage(self, value):
		""""""
		self.edit(selectionImage=value)
	#----------------------------------------------------------------------
	selectionImage = property(get_selectionImage, set_selectionImage)
	#----------------------------------------------------------------------
	def get_highlightImage(self):
		""""""
		return self.query(highlightImage=True)
	#----------------------------------------------------------------------
	def set_highlightImage(self, value):
		""""""
		self.edit(highlightImage=value)
	#----------------------------------------------------------------------
	highlightImage = property(get_highlightImage, set_highlightImage)
	#----------------------------------------------------------------------
	def handleNodeDropCallback(self,value):
		""""""
		self.edit(handleNodeDropCallback=value)
	#----------------------------------------------------------------------
	def labelEditingCallback(self,value):
		""""""
		self.edit(labelEditingCallback=value)
	#----------------------------------------------------------------------
	def get_commandRepeatable(self):
		""""""
		return self.query(commandRepeatable=True)
	#----------------------------------------------------------------------
	def set_commandRepeatable(self, value):
		""""""
		self.edit(commandRepeatable=value)
	#----------------------------------------------------------------------
	commandRepeatable = property(get_commandRepeatable, set_commandRepeatable)
	#----------------------------------------------------------------------
	def get_flat(self):
		""""""
		return self.query(flat=True)
	#----------------------------------------------------------------------
	def set_flat(self, value):
		""""""
		self.edit(flat=value)
	#----------------------------------------------------------------------
	flat = property(get_flat, set_flat)
########################################################################
class IconTextCheckBox(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextCheckBox(**kwargs)
			super(IconTextCheckBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextCheckBox(name, exists=True):
				super(IconTextCheckBox, self).__init__(name)
			else:
				name = cmds.iconTextCheckBox(name, **kwargs)
				super(IconTextCheckBox, self).__init__(name, **dict(qtParent=parent))
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		""""""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		""""""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
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
	def get_disabledImage(self):
		""""""
		return self.query(disabledImage=True)
	#----------------------------------------------------------------------
	def set_disabledImage(self, value):
		""""""
		self.edit(disabledImage=value)
	#----------------------------------------------------------------------
	disabledImage = property(get_disabledImage, set_disabledImage)
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
	def get_overlayLabelColor(self):
		""""""
		return self.query(overlayLabelColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelColor(self, value):
		""""""
		self.edit(overlayLabelColor=value)
	#----------------------------------------------------------------------
	overlayLabelColor = property(get_overlayLabelColor, set_overlayLabelColor)
	#----------------------------------------------------------------------
	def get_overlayLabelBackColor(self):
		""""""
		return self.query(overlayLabelBackColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelBackColor(self, value):
		""""""
		self.edit(overlayLabelBackColor=value)
	#----------------------------------------------------------------------
	overlayLabelBackColor = property(get_overlayLabelBackColor, set_overlayLabelBackColor)
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_labelOffset(self):
		""""""
		return self.query(labelOffset=True)
	#----------------------------------------------------------------------
	def set_labelOffset(self, value):
		""""""
		self.edit(labelOffset=value)
	#----------------------------------------------------------------------
	labelOffset = property(get_labelOffset, set_labelOffset)
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
	def get_version(self):
		""""""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		""""""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
	#----------------------------------------------------------------------
	def get_onCommand(self):
		""""""
		return self.query(onCommand=True)
	#----------------------------------------------------------------------
	def set_onCommand(self, value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	onCommand = property(get_onCommand, set_onCommand)
	#----------------------------------------------------------------------
	def get_offCommand(self):
		""""""
		return self.query(offCommand=True)
	#----------------------------------------------------------------------
	def set_offCommand(self, value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	offCommand = property(get_offCommand, set_offCommand)
	#----------------------------------------------------------------------
	def get_changeCommand(self):
		""""""
		return self.query(changeCommand=True)
	#----------------------------------------------------------------------
	def set_changeCommand(self, value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	changeCommand = property(get_changeCommand, set_changeCommand)
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
	def get_selectionImage(self):
		""""""
		return self.query(selectionImage=True)
	#----------------------------------------------------------------------
	def set_selectionImage(self, value):
		""""""
		self.edit(selectionImage=value)
	#----------------------------------------------------------------------
	selectionImage = property(get_selectionImage, set_selectionImage)
	#----------------------------------------------------------------------
	def get_highlightImage(self):
		""""""
		return self.query(highlightImage=True)
	#----------------------------------------------------------------------
	def set_highlightImage(self, value):
		""""""
		self.edit(highlightImage=value)
	#----------------------------------------------------------------------
	highlightImage = property(get_highlightImage, set_highlightImage)
	#----------------------------------------------------------------------
	def get_selectionHighlightImage(self):
		""""""
		return self.query(selectionHighlightImage=True)
	#----------------------------------------------------------------------
	def set_selectionHighlightImage(self, value):
		""""""
		self.edit(selectionHighlightImage=value)
	#----------------------------------------------------------------------
	selectionHighlightImage = property(get_selectionHighlightImage, set_selectionHighlightImage)
	#----------------------------------------------------------------------
	def get_flat(self):
		""""""
		return self.query(flat=True)
	#----------------------------------------------------------------------
	def set_flat(self, value):
		""""""
		self.edit(flat=value)
	#----------------------------------------------------------------------
	flat = property(get_flat, set_flat)
########################################################################
class IconTextRadioButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextRadioButton(**kwargs)
			super(IconTextRadioButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextRadioButton(name, exists=True):
				super(IconTextRadioButton, self).__init__(name)
			else:
				name = cmds.iconTextRadioButton(name, **kwargs)
				super(IconTextRadioButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		""""""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		""""""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
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
	def get_disabledImage(self):
		""""""
		return self.query(disabledImage=True)
	#----------------------------------------------------------------------
	def set_disabledImage(self, value):
		""""""
		self.edit(disabledImage=value)
	#----------------------------------------------------------------------
	disabledImage = property(get_disabledImage, set_disabledImage)
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
	def get_overlayLabelColor(self):
		""""""
		return self.query(overlayLabelColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelColor(self, value):
		""""""
		self.edit(overlayLabelColor=value)
	#----------------------------------------------------------------------
	overlayLabelColor = property(get_overlayLabelColor, set_overlayLabelColor)
	#----------------------------------------------------------------------
	def get_overlayLabelBackColor(self):
		""""""
		return self.query(overlayLabelBackColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelBackColor(self, value):
		""""""
		self.edit(overlayLabelBackColor=value)
	#----------------------------------------------------------------------
	overlayLabelBackColor = property(get_overlayLabelBackColor, set_overlayLabelBackColor)
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_labelOffset(self):
		""""""
		return self.query(labelOffset=True)
	#----------------------------------------------------------------------
	def set_labelOffset(self, value):
		""""""
		self.edit(labelOffset=value)
	#----------------------------------------------------------------------
	labelOffset = property(get_labelOffset, set_labelOffset)
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
	def get_version(self):
		""""""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		""""""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
	#----------------------------------------------------------------------
	def get_onCommand(self):
		""""""
		return self.query(onCommand=True)
	#----------------------------------------------------------------------
	def set_onCommand(self, value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	onCommand = property(get_onCommand, set_onCommand)
	#----------------------------------------------------------------------
	def get_offCommand(self):
		""""""
		return self.query(offCommand=True)
	#----------------------------------------------------------------------
	def set_offCommand(self, value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	offCommand = property(get_offCommand, set_offCommand)
	#----------------------------------------------------------------------
	def get_changeCommand(self):
		""""""
		return self.query(changeCommand=True)
	#----------------------------------------------------------------------
	def set_changeCommand(self, value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	changeCommand = property(get_changeCommand, set_changeCommand)
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
	def get_selectionImage(self):
		""""""
		return self.query(selectionImage=True)
	#----------------------------------------------------------------------
	def set_selectionImage(self, value):
		""""""
		self.edit(selectionImage=value)
	#----------------------------------------------------------------------
	selectionImage = property(get_selectionImage, set_selectionImage)
	#----------------------------------------------------------------------
	def get_highlightImage(self):
		""""""
		return self.query(highlightImage=True)
	#----------------------------------------------------------------------
	def set_highlightImage(self, value):
		""""""
		self.edit(highlightImage=value)
	#----------------------------------------------------------------------
	highlightImage = property(get_highlightImage, set_highlightImage)
	#----------------------------------------------------------------------
	def get_selectionHighlightImage(self):
		""""""
		return self.query(selectionHighlightImage=True)
	#----------------------------------------------------------------------
	def set_selectionHighlightImage(self, value):
		""""""
		self.edit(selectionHighlightImage=value)
	#----------------------------------------------------------------------
	selectionHighlightImage = property(get_selectionHighlightImage, set_selectionHighlightImage)
	#----------------------------------------------------------------------
	def get_flat(self):
		""""""
		return self.query(flat=True)
	#----------------------------------------------------------------------
	def set_flat(self, value):
		""""""
		self.edit(flat=value)
	#----------------------------------------------------------------------
	flat = property(get_flat, set_flat)
########################################################################
class IconTextRadioCollection(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextRadioCollection(**kwargs)
			super(IconTextRadioCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextRadioCollection(name, exists=True):
				super(IconTextRadioCollection, self).__init__(name)
			else:
				name = cmds.iconTextRadioCollection(name, **kwargs)
				super(IconTextRadioCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gl(self):
		""""""
		return self.query(gl=True)
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
	def disableCommands(self,value):
		""""""
		self.edit(disableCommands=value)
	#----------------------------------------------------------------------
	@property
	def numberOfCollectionItems(self):
		""""""
		return self.query(numberOfCollectionItems=True)
	#----------------------------------------------------------------------
	@property
	def collectionItemArray(self):
		""""""
		return self.query(collectionItemArray=True)
########################################################################
class IconTextScrollList(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextScrollList(**kwargs)
			super(IconTextScrollList, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextScrollList(name, exists=True):
				super(IconTextScrollList, self).__init__(name)
			else:
				name = cmds.iconTextScrollList(name, **kwargs)
				super(IconTextScrollList, self).__init__(name, **dict(qtParent=parent))
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
	def append(self,value):
		""""""
		self.edit(append=value)
	#----------------------------------------------------------------------
	def removeAll(self,value):
		""""""
		self.edit(removeAll=value)
	#----------------------------------------------------------------------
	def get_allowMultiSelection(self):
		""""""
		return self.query(allowMultiSelection=True)
	#----------------------------------------------------------------------
	def set_allowMultiSelection(self, value):
		""""""
		self.edit(allowMultiSelection=value)
	#----------------------------------------------------------------------
	allowMultiSelection = property(get_allowMultiSelection, set_allowMultiSelection)
	#----------------------------------------------------------------------
	def selectCommand(self,value):
		""""""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	def get_selectItem(self):
		""""""
		return self.query(selectItem=True)
	#----------------------------------------------------------------------
	def set_selectItem(self, value):
		""""""
		self.edit(selectItem=value)
	#----------------------------------------------------------------------
	selectItem = property(get_selectItem, set_selectItem)
	#----------------------------------------------------------------------
	def get_selectIndexedItem(self):
		""""""
		return self.query(selectIndexedItem=True)
	#----------------------------------------------------------------------
	def set_selectIndexedItem(self, value):
		""""""
		self.edit(selectIndexedItem=value)
	#----------------------------------------------------------------------
	selectIndexedItem = property(get_selectIndexedItem, set_selectIndexedItem)
	#----------------------------------------------------------------------
	def deselectAll(self,value):
		""""""
		self.edit(deselectAll=value)
	#----------------------------------------------------------------------
	def itemTextColor(self,value):
		""""""
		self.edit(itemTextColor=value)
	#----------------------------------------------------------------------
	@property
	def itemAt(self):
		""""""
		return self.query(itemAt=True)
	#----------------------------------------------------------------------
	@property
	def visualRectAt(self):
		""""""
		return self.query(visualRectAt=True)
	#----------------------------------------------------------------------
	def doubleClickCommand(self,value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	@property
	def numberOfRows(self):
		""""""
		return self.query(numberOfRows=True)
	#----------------------------------------------------------------------
	def dropRectCallback(self,value):
		""""""
		self.edit(dropRectCallback=value)
########################################################################
class IconTextStaticLabel(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.iconTextStaticLabel(**kwargs)
			super(IconTextStaticLabel, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.iconTextStaticLabel(name, exists=True):
				super(IconTextStaticLabel, self).__init__(name)
			else:
				name = cmds.iconTextStaticLabel(name, **kwargs)
				super(IconTextStaticLabel, self).__init__(name, **dict(qtParent=parent))
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		""""""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		""""""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
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
	def get_disabledImage(self):
		""""""
		return self.query(disabledImage=True)
	#----------------------------------------------------------------------
	def set_disabledImage(self, value):
		""""""
		self.edit(disabledImage=value)
	#----------------------------------------------------------------------
	disabledImage = property(get_disabledImage, set_disabledImage)
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
	def get_overlayLabelColor(self):
		""""""
		return self.query(overlayLabelColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelColor(self, value):
		""""""
		self.edit(overlayLabelColor=value)
	#----------------------------------------------------------------------
	overlayLabelColor = property(get_overlayLabelColor, set_overlayLabelColor)
	#----------------------------------------------------------------------
	def get_overlayLabelBackColor(self):
		""""""
		return self.query(overlayLabelBackColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelBackColor(self, value):
		""""""
		self.edit(overlayLabelBackColor=value)
	#----------------------------------------------------------------------
	overlayLabelBackColor = property(get_overlayLabelBackColor, set_overlayLabelBackColor)
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_labelOffset(self):
		""""""
		return self.query(labelOffset=True)
	#----------------------------------------------------------------------
	def set_labelOffset(self, value):
		""""""
		self.edit(labelOffset=value)
	#----------------------------------------------------------------------
	labelOffset = property(get_labelOffset, set_labelOffset)
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
class Image(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.image(**kwargs)
			super(Image, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.image(name, exists=True):
				super(Image, self).__init__(name)
			else:
				name = cmds.image(name, **kwargs)
				super(Image, self).__init__(name, **dict(qtParent=parent))
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
	def get_image(self):
		""""""
		return self.query(image=True)
	#----------------------------------------------------------------------
	def set_image(self, value):
		""""""
		self.edit(image=value)
	#----------------------------------------------------------------------
	image = property(get_image, set_image)
########################################################################
class IntField(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.intField(**kwargs)
			super(IntField, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.intField(name, exists=True):
				super(IntField, self).__init__(name)
			else:
				name = cmds.intField(name, **kwargs)
				super(IntField, self).__init__(name, **dict(qtParent=parent))
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def enterCommand(self,value):
		""""""
		self.edit(enterCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
	#----------------------------------------------------------------------
	def receiveFocusCommand(self,value):
		""""""
		self.edit(receiveFocusCommand=value)
########################################################################
class IntFieldGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.intFieldGrp(**kwargs)
			super(IntFieldGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.intFieldGrp(name, exists=True):
				super(IntFieldGrp, self).__init__(name)
			else:
				name = cmds.intFieldGrp(name, **kwargs)
				super(IntFieldGrp, self).__init__(name, **dict(qtParent=parent))
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
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
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
	def get_value1(self):
		""""""
		return self.query(value1=True)
	#----------------------------------------------------------------------
	def set_value1(self, value):
		""""""
		self.edit(value1=value)
	#----------------------------------------------------------------------
	value1 = property(get_value1, set_value1)
	#----------------------------------------------------------------------
	def get_value2(self):
		""""""
		return self.query(value2=True)
	#----------------------------------------------------------------------
	def set_value2(self, value):
		""""""
		self.edit(value2=value)
	#----------------------------------------------------------------------
	value2 = property(get_value2, set_value2)
	#----------------------------------------------------------------------
	def get_value3(self):
		""""""
		return self.query(value3=True)
	#----------------------------------------------------------------------
	def set_value3(self, value):
		""""""
		self.edit(value3=value)
	#----------------------------------------------------------------------
	value3 = property(get_value3, set_value3)
	#----------------------------------------------------------------------
	def get_value4(self):
		""""""
		return self.query(value4=True)
	#----------------------------------------------------------------------
	def set_value4(self, value):
		""""""
		self.edit(value4=value)
	#----------------------------------------------------------------------
	value4 = property(get_value4, set_value4)
	#----------------------------------------------------------------------
	def get_enable1(self):
		""""""
		return self.query(enable1=True)
	#----------------------------------------------------------------------
	def set_enable1(self, value):
		""""""
		self.edit(enable1=value)
	#----------------------------------------------------------------------
	enable1 = property(get_enable1, set_enable1)
	#----------------------------------------------------------------------
	def get_enable2(self):
		""""""
		return self.query(enable2=True)
	#----------------------------------------------------------------------
	def set_enable2(self, value):
		""""""
		self.edit(enable2=value)
	#----------------------------------------------------------------------
	enable2 = property(get_enable2, set_enable2)
	#----------------------------------------------------------------------
	def get_enable3(self):
		""""""
		return self.query(enable3=True)
	#----------------------------------------------------------------------
	def set_enable3(self, value):
		""""""
		self.edit(enable3=value)
	#----------------------------------------------------------------------
	enable3 = property(get_enable3, set_enable3)
	#----------------------------------------------------------------------
	def get_enable4(self):
		""""""
		return self.query(enable4=True)
	#----------------------------------------------------------------------
	def set_enable4(self, value):
		""""""
		self.edit(enable4=value)
	#----------------------------------------------------------------------
	enable4 = property(get_enable4, set_enable4)
########################################################################
class IntScrollBar(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.intScrollBar(**kwargs)
			super(IntScrollBar, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.intScrollBar(name, exists=True):
				super(IntScrollBar, self).__init__(name)
			else:
				name = cmds.intScrollBar(name, **kwargs)
				super(IntScrollBar, self).__init__(name, **dict(qtParent=parent))
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	@property
	def horizontal(self):
		""""""
		return self.query(horizontal=True)
	#----------------------------------------------------------------------
	def get_largeStep(self):
		""""""
		return self.query(largeStep=True)
	#----------------------------------------------------------------------
	def set_largeStep(self, value):
		""""""
		self.edit(largeStep=value)
	#----------------------------------------------------------------------
	largeStep = property(get_largeStep, set_largeStep)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class IntSlider(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.intSlider(**kwargs)
			super(IntSlider, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.intSlider(name, exists=True):
				super(IntSlider, self).__init__(name)
			else:
				name = cmds.intSlider(name, **kwargs)
				super(IntSlider, self).__init__(name, **dict(qtParent=parent))
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
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	@property
	def horizontal(self):
		""""""
		return self.query(horizontal=True)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
########################################################################
class IntSliderGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.intSliderGrp(**kwargs)
			super(IntSliderGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.intSliderGrp(name, exists=True):
				super(IntSliderGrp, self).__init__(name)
			else:
				name = cmds.intSliderGrp(name, **kwargs)
				super(IntSliderGrp, self).__init__(name, **dict(qtParent=parent))
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
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def dragCommand(self,value):
		""""""
		self.edit(dragCommand=value)
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
	def get_fieldMinValue(self):
		""""""
		return self.query(fieldMinValue=True)
	#----------------------------------------------------------------------
	def set_fieldMinValue(self, value):
		""""""
		self.edit(fieldMinValue=value)
	#----------------------------------------------------------------------
	fieldMinValue = property(get_fieldMinValue, set_fieldMinValue)
	#----------------------------------------------------------------------
	def get_fieldMaxValue(self):
		""""""
		return self.query(fieldMaxValue=True)
	#----------------------------------------------------------------------
	def set_fieldMaxValue(self, value):
		""""""
		self.edit(fieldMaxValue=value)
	#----------------------------------------------------------------------
	fieldMaxValue = property(get_fieldMaxValue, set_fieldMaxValue)
	#----------------------------------------------------------------------
	def get_step(self):
		""""""
		return self.query(step=True)
	#----------------------------------------------------------------------
	def set_step(self, value):
		""""""
		self.edit(step=value)
	#----------------------------------------------------------------------
	step = property(get_step, set_step)
	#----------------------------------------------------------------------
	def get_fieldStep(self):
		""""""
		return self.query(fieldStep=True)
	#----------------------------------------------------------------------
	def set_fieldStep(self, value):
		""""""
		self.edit(fieldStep=value)
	#----------------------------------------------------------------------
	fieldStep = property(get_fieldStep, set_fieldStep)
	#----------------------------------------------------------------------
	def get_sliderStep(self):
		""""""
		return self.query(sliderStep=True)
	#----------------------------------------------------------------------
	def set_sliderStep(self, value):
		""""""
		self.edit(sliderStep=value)
	#----------------------------------------------------------------------
	sliderStep = property(get_sliderStep, set_sliderStep)
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
class LayerButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.layerButton(**kwargs)
			super(LayerButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.layerButton(name, exists=True):
				super(LayerButton, self).__init__(name)
			else:
				name = cmds.layerButton(name, **kwargs)
				super(LayerButton, self).__init__(name, **dict(qtParent=parent))
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
	def color(self,value):
		""""""
		self.edit(color=value)
	#----------------------------------------------------------------------
	def get_transparent(self):
		""""""
		return self.query(transparent=True)
	#----------------------------------------------------------------------
	def set_transparent(self, value):
		""""""
		self.edit(transparent=value)
	#----------------------------------------------------------------------
	transparent = property(get_transparent, set_transparent)
	#----------------------------------------------------------------------
	def get_layerState(self):
		""""""
		return self.query(layerState=True)
	#----------------------------------------------------------------------
	def set_layerState(self, value):
		""""""
		self.edit(layerState=value)
	#----------------------------------------------------------------------
	layerState = property(get_layerState, set_layerState)
	#----------------------------------------------------------------------
	def get_layerVisible(self):
		""""""
		return self.query(layerVisible=True)
	#----------------------------------------------------------------------
	def set_layerVisible(self, value):
		""""""
		self.edit(layerVisible=value)
	#----------------------------------------------------------------------
	layerVisible = property(get_layerVisible, set_layerVisible)
	#----------------------------------------------------------------------
	@property
	def name(self):
		""""""
		return self.query(name=True)
	#----------------------------------------------------------------------
	def get_identification(self):
		""""""
		return self.query(identification=True)
	#----------------------------------------------------------------------
	def set_identification(self, value):
		""""""
		self.edit(identification=value)
	#----------------------------------------------------------------------
	identification = property(get_identification, set_identification)
	#----------------------------------------------------------------------
	def command(self,value):
		""""""
		self.edit(command=value)
	#----------------------------------------------------------------------
	def doubleClickCommand(self,value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	def renameCommand(self,value):
		""""""
		self.edit(renameCommand=value)
	#----------------------------------------------------------------------
	def current(self,value):
		""""""
		self.edit(current=value)
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
	@property
	def labelWidth(self):
		""""""
		return self.query(labelWidth=True)
	#----------------------------------------------------------------------
	def visibleCommand(self,value):
		""""""
		self.edit(visibleCommand=value)
	#----------------------------------------------------------------------
	def typeCommand(self,value):
		""""""
		self.edit(typeCommand=value)
########################################################################
class MessageLine(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.messageLine(**kwargs)
			super(MessageLine, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.messageLine(name, exists=True):
				super(MessageLine, self).__init__(name)
			else:
				name = cmds.messageLine(name, **kwargs)
				super(MessageLine, self).__init__(name, **dict(qtParent=parent))
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
########################################################################
class NameField(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nameField(**kwargs)
			super(NameField, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nameField(name, exists=True):
				super(NameField, self).__init__(name)
			else:
				name = cmds.nameField(name, **kwargs)
				super(NameField, self).__init__(name, **dict(qtParent=parent))
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
	def get_object(self):
		""""""
		return self.query(object=True)
	#----------------------------------------------------------------------
	def set_object(self, value):
		""""""
		self.edit(object=value)
	#----------------------------------------------------------------------
	object = property(get_object, set_object)
	#----------------------------------------------------------------------
	def get_nameChangeCommand(self):
		""""""
		return self.query(nameChangeCommand=True)
	#----------------------------------------------------------------------
	def set_nameChangeCommand(self, value):
		""""""
		self.edit(nameChangeCommand=value)
	#----------------------------------------------------------------------
	nameChangeCommand = property(get_nameChangeCommand, set_nameChangeCommand)
	#----------------------------------------------------------------------
	def get_changeCommand(self):
		""""""
		return self.query(changeCommand=True)
	#----------------------------------------------------------------------
	def set_changeCommand(self, value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	changeCommand = property(get_changeCommand, set_changeCommand)
	#----------------------------------------------------------------------
	def get_receiveFocusCommand(self):
		""""""
		return self.query(receiveFocusCommand=True)
	#----------------------------------------------------------------------
	def set_receiveFocusCommand(self, value):
		""""""
		self.edit(receiveFocusCommand=value)
	#----------------------------------------------------------------------
	receiveFocusCommand = property(get_receiveFocusCommand, set_receiveFocusCommand)
########################################################################
class NodeTreeLister(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.nodeTreeLister(**kwargs)
			super(NodeTreeLister, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.nodeTreeLister(name, exists=True):
				super(NodeTreeLister, self).__init__(name)
			else:
				name = cmds.nodeTreeLister(name, **kwargs)
				super(NodeTreeLister, self).__init__(name, **dict(qtParent=parent))
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
	def addItem(self,value):
		""""""
		self.edit(addItem=value)
	#----------------------------------------------------------------------
	def addFavorite(self,value):
		""""""
		self.edit(addFavorite=value)
	#----------------------------------------------------------------------
	def clearContents(self,value):
		""""""
		self.edit(clearContents=value)
	#----------------------------------------------------------------------
	def executeItem(self,value):
		""""""
		self.edit(executeItem=value)
	#----------------------------------------------------------------------
	@property
	def favoritesList(self):
		""""""
		return self.query(favoritesList=True)
	#----------------------------------------------------------------------
	def removeFavorite(self,value):
		""""""
		self.edit(removeFavorite=value)
	#----------------------------------------------------------------------
	def removeItem(self,value):
		""""""
		self.edit(removeItem=value)
	#----------------------------------------------------------------------
	@property
	def resultsPathUnderCursor(self):
		""""""
		return self.query(resultsPathUnderCursor=True)
	#----------------------------------------------------------------------
	def collapsePath(self,value):
		""""""
		self.edit(collapsePath=value)
	#----------------------------------------------------------------------
	def expandPath(self,value):
		""""""
		self.edit(expandPath=value)
	#----------------------------------------------------------------------
	def expandToDepth(self,value):
		""""""
		self.edit(expandToDepth=value)
	#----------------------------------------------------------------------
	def favoritesCallback(self,value):
		""""""
		self.edit(favoritesCallback=value)
	#----------------------------------------------------------------------
	@property
	def itemScript(self):
		""""""
		return self.query(itemScript=True)
	#----------------------------------------------------------------------
	def selectPath(self,value):
		""""""
		self.edit(selectPath=value)
########################################################################
class PalettePort(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.palettePort(**kwargs)
			super(PalettePort, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.palettePort(name, exists=True):
				super(PalettePort, self).__init__(name)
			else:
				name = cmds.palettePort(name, **kwargs)
				super(PalettePort, self).__init__(name, **dict(qtParent=parent))
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
	def dimensions(self):
		""""""
		return self.query(dimensions=True)
	#----------------------------------------------------------------------
	@property
	def actualTotal(self):
		""""""
		return self.query(actualTotal=True)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def get_colorEditable(self):
		""""""
		return self.query(colorEditable=True)
	#----------------------------------------------------------------------
	def set_colorEditable(self, value):
		""""""
		self.edit(colorEditable=value)
	#----------------------------------------------------------------------
	colorEditable = property(get_colorEditable, set_colorEditable)
	#----------------------------------------------------------------------
	def redraw(self,value):
		""""""
		self.edit(redraw=value)
	#----------------------------------------------------------------------
	def get_rgbValue(self):
		""""""
		return self.query(rgbValue=True)
	#----------------------------------------------------------------------
	def set_rgbValue(self, value):
		""""""
		self.edit(rgbValue=value)
	#----------------------------------------------------------------------
	rgbValue = property(get_rgbValue, set_rgbValue)
	#----------------------------------------------------------------------
	def get_hsvValue(self):
		""""""
		return self.query(hsvValue=True)
	#----------------------------------------------------------------------
	def set_hsvValue(self, value):
		""""""
		self.edit(hsvValue=value)
	#----------------------------------------------------------------------
	hsvValue = property(get_hsvValue, set_hsvValue)
	#----------------------------------------------------------------------
	def get_transparent(self):
		""""""
		return self.query(transparent=True)
	#----------------------------------------------------------------------
	def set_transparent(self, value):
		""""""
		self.edit(transparent=value)
	#----------------------------------------------------------------------
	transparent = property(get_transparent, set_transparent)
	#----------------------------------------------------------------------
	def get_setCurCell(self):
		""""""
		return self.query(setCurCell=True)
	#----------------------------------------------------------------------
	def set_setCurCell(self, value):
		""""""
		self.edit(setCurCell=value)
	#----------------------------------------------------------------------
	setCurCell = property(get_setCurCell, set_setCurCell)
	#----------------------------------------------------------------------
	def colorEdited(self,value):
		""""""
		self.edit(colorEdited=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
########################################################################
class Picture(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.picture(**kwargs)
			super(Picture, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.picture(name, exists=True):
				super(Picture, self).__init__(name)
			else:
				name = cmds.picture(name, **kwargs)
				super(Picture, self).__init__(name, **dict(qtParent=parent))
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
	def get_tile(self):
		""""""
		return self.query(tile=True)
	#----------------------------------------------------------------------
	def set_tile(self, value):
		""""""
		self.edit(tile=value)
	#----------------------------------------------------------------------
	tile = property(get_tile, set_tile)
########################################################################
class ProgressBar(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.progressBar(**kwargs)
			super(ProgressBar, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.progressBar(name, exists=True):
				super(ProgressBar, self).__init__(name)
			else:
				name = cmds.progressBar(name, **kwargs)
				super(ProgressBar, self).__init__(name, **dict(qtParent=parent))
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
	def get_isMainProgressBar(self):
		""""""
		return self.query(isMainProgressBar=True)
	#----------------------------------------------------------------------
	def set_isMainProgressBar(self, value):
		""""""
		self.edit(isMainProgressBar=value)
	#----------------------------------------------------------------------
	isMainProgressBar = property(get_isMainProgressBar, set_isMainProgressBar)
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
	#----------------------------------------------------------------------
	def beginProgress(self,value):
		""""""
		self.edit(beginProgress=value)
	#----------------------------------------------------------------------
	def endProgress(self,value):
		""""""
		self.edit(endProgress=value)
########################################################################
class RadioButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.radioButton(**kwargs)
			super(RadioButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.radioButton(name, exists=True):
				super(RadioButton, self).__init__(name)
			else:
				name = cmds.radioButton(name, **kwargs)
				super(RadioButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def get_recomputeSize(self):
		""""""
		return self.query(recomputeSize=True)
	#----------------------------------------------------------------------
	def set_recomputeSize(self, value):
		""""""
		self.edit(recomputeSize=value)
	#----------------------------------------------------------------------
	recomputeSize = property(get_recomputeSize, set_recomputeSize)
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
	def onCommand(self,value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
########################################################################
class RadioButtonGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.radioButtonGrp(**kwargs)
			super(RadioButtonGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.radioButtonGrp(name, exists=True):
				super(RadioButtonGrp, self).__init__(name)
			else:
				name = cmds.radioButtonGrp(name, **kwargs)
				super(RadioButtonGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_label1(self):
		""""""
		return self.query(label1=True)
	#----------------------------------------------------------------------
	def set_label1(self, value):
		""""""
		self.edit(label1=value)
	#----------------------------------------------------------------------
	label1 = property(get_label1, set_label1)
	#----------------------------------------------------------------------
	def get_label2(self):
		""""""
		return self.query(label2=True)
	#----------------------------------------------------------------------
	def set_label2(self, value):
		""""""
		self.edit(label2=value)
	#----------------------------------------------------------------------
	label2 = property(get_label2, set_label2)
	#----------------------------------------------------------------------
	def get_label3(self):
		""""""
		return self.query(label3=True)
	#----------------------------------------------------------------------
	def set_label3(self, value):
		""""""
		self.edit(label3=value)
	#----------------------------------------------------------------------
	label3 = property(get_label3, set_label3)
	#----------------------------------------------------------------------
	def get_label4(self):
		""""""
		return self.query(label4=True)
	#----------------------------------------------------------------------
	def set_label4(self, value):
		""""""
		self.edit(label4=value)
	#----------------------------------------------------------------------
	label4 = property(get_label4, set_label4)
	#----------------------------------------------------------------------
	def get_labelAnnotation(self):
		""""""
		return self.query(labelAnnotation=True)
	#----------------------------------------------------------------------
	def set_labelAnnotation(self, value):
		""""""
		self.edit(labelAnnotation=value)
	#----------------------------------------------------------------------
	labelAnnotation = property(get_labelAnnotation, set_labelAnnotation)
	#----------------------------------------------------------------------
	def get_annotation1(self):
		""""""
		return self.query(annotation1=True)
	#----------------------------------------------------------------------
	def set_annotation1(self, value):
		""""""
		self.edit(annotation1=value)
	#----------------------------------------------------------------------
	annotation1 = property(get_annotation1, set_annotation1)
	#----------------------------------------------------------------------
	def get_annotation2(self):
		""""""
		return self.query(annotation2=True)
	#----------------------------------------------------------------------
	def set_annotation2(self, value):
		""""""
		self.edit(annotation2=value)
	#----------------------------------------------------------------------
	annotation2 = property(get_annotation2, set_annotation2)
	#----------------------------------------------------------------------
	def get_annotation3(self):
		""""""
		return self.query(annotation3=True)
	#----------------------------------------------------------------------
	def set_annotation3(self, value):
		""""""
		self.edit(annotation3=value)
	#----------------------------------------------------------------------
	annotation3 = property(get_annotation3, set_annotation3)
	#----------------------------------------------------------------------
	def get_annotation4(self):
		""""""
		return self.query(annotation4=True)
	#----------------------------------------------------------------------
	def set_annotation4(self, value):
		""""""
		self.edit(annotation4=value)
	#----------------------------------------------------------------------
	annotation4 = property(get_annotation4, set_annotation4)
	#----------------------------------------------------------------------
	def get_labelArray2(self):
		""""""
		return self.query(labelArray2=True)
	#----------------------------------------------------------------------
	def set_labelArray2(self, value):
		""""""
		self.edit(labelArray2=value)
	#----------------------------------------------------------------------
	labelArray2 = property(get_labelArray2, set_labelArray2)
	#----------------------------------------------------------------------
	def get_labelArray3(self):
		""""""
		return self.query(labelArray3=True)
	#----------------------------------------------------------------------
	def set_labelArray3(self, value):
		""""""
		self.edit(labelArray3=value)
	#----------------------------------------------------------------------
	labelArray3 = property(get_labelArray3, set_labelArray3)
	#----------------------------------------------------------------------
	def get_labelArray4(self):
		""""""
		return self.query(labelArray4=True)
	#----------------------------------------------------------------------
	def set_labelArray4(self, value):
		""""""
		self.edit(labelArray4=value)
	#----------------------------------------------------------------------
	labelArray4 = property(get_labelArray4, set_labelArray4)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def changeCommand1(self,value):
		""""""
		self.edit(changeCommand1=value)
	#----------------------------------------------------------------------
	def changeCommand2(self,value):
		""""""
		self.edit(changeCommand2=value)
	#----------------------------------------------------------------------
	def changeCommand3(self,value):
		""""""
		self.edit(changeCommand3=value)
	#----------------------------------------------------------------------
	def changeCommand4(self,value):
		""""""
		self.edit(changeCommand4=value)
	#----------------------------------------------------------------------
	def onCommand(self,value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	def onCommand1(self,value):
		""""""
		self.edit(onCommand1=value)
	#----------------------------------------------------------------------
	def onCommand2(self,value):
		""""""
		self.edit(onCommand2=value)
	#----------------------------------------------------------------------
	def onCommand3(self,value):
		""""""
		self.edit(onCommand3=value)
	#----------------------------------------------------------------------
	def onCommand4(self,value):
		""""""
		self.edit(onCommand4=value)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def offCommand1(self,value):
		""""""
		self.edit(offCommand1=value)
	#----------------------------------------------------------------------
	def offCommand2(self,value):
		""""""
		self.edit(offCommand2=value)
	#----------------------------------------------------------------------
	def offCommand3(self,value):
		""""""
		self.edit(offCommand3=value)
	#----------------------------------------------------------------------
	def offCommand4(self,value):
		""""""
		self.edit(offCommand4=value)
	#----------------------------------------------------------------------
	def get_enable1(self):
		""""""
		return self.query(enable1=True)
	#----------------------------------------------------------------------
	def set_enable1(self, value):
		""""""
		self.edit(enable1=value)
	#----------------------------------------------------------------------
	enable1 = property(get_enable1, set_enable1)
	#----------------------------------------------------------------------
	def get_enable2(self):
		""""""
		return self.query(enable2=True)
	#----------------------------------------------------------------------
	def set_enable2(self, value):
		""""""
		self.edit(enable2=value)
	#----------------------------------------------------------------------
	enable2 = property(get_enable2, set_enable2)
	#----------------------------------------------------------------------
	def get_enable3(self):
		""""""
		return self.query(enable3=True)
	#----------------------------------------------------------------------
	def set_enable3(self, value):
		""""""
		self.edit(enable3=value)
	#----------------------------------------------------------------------
	enable3 = property(get_enable3, set_enable3)
	#----------------------------------------------------------------------
	def get_enable4(self):
		""""""
		return self.query(enable4=True)
	#----------------------------------------------------------------------
	def set_enable4(self, value):
		""""""
		self.edit(enable4=value)
	#----------------------------------------------------------------------
	enable4 = property(get_enable4, set_enable4)
	#----------------------------------------------------------------------
	def get_data1(self):
		""""""
		return self.query(data1=True)
	#----------------------------------------------------------------------
	def set_data1(self, value):
		""""""
		self.edit(data1=value)
	#----------------------------------------------------------------------
	data1 = property(get_data1, set_data1)
	#----------------------------------------------------------------------
	def get_data2(self):
		""""""
		return self.query(data2=True)
	#----------------------------------------------------------------------
	def set_data2(self, value):
		""""""
		self.edit(data2=value)
	#----------------------------------------------------------------------
	data2 = property(get_data2, set_data2)
	#----------------------------------------------------------------------
	def get_data3(self):
		""""""
		return self.query(data3=True)
	#----------------------------------------------------------------------
	def set_data3(self, value):
		""""""
		self.edit(data3=value)
	#----------------------------------------------------------------------
	data3 = property(get_data3, set_data3)
	#----------------------------------------------------------------------
	def get_data4(self):
		""""""
		return self.query(data4=True)
	#----------------------------------------------------------------------
	def set_data4(self, value):
		""""""
		self.edit(data4=value)
	#----------------------------------------------------------------------
	data4 = property(get_data4, set_data4)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	@property
	def vertical(self):
		""""""
		return self.query(vertical=True)
########################################################################
class RadioCollection(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.radioCollection(**kwargs)
			super(RadioCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.radioCollection(name, exists=True):
				super(RadioCollection, self).__init__(name)
			else:
				name = cmds.radioCollection(name, **kwargs)
				super(RadioCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gl(self):
		""""""
		return self.query(gl=True)
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
	@property
	def numberOfCollectionItems(self):
		""""""
		return self.query(numberOfCollectionItems=True)
	#----------------------------------------------------------------------
	@property
	def collectionItemArray(self):
		""""""
		return self.query(collectionItemArray=True)
########################################################################
class RangeControl(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.rangeControl(**kwargs)
			super(RangeControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.rangeControl(name, exists=True):
				super(RangeControl, self).__init__(name)
			else:
				name = cmds.rangeControl(name, **kwargs)
				super(RangeControl, self).__init__(name, **dict(qtParent=parent))
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
	def changedCommand(self,value):
		""""""
		self.edit(changedCommand=value)
	#----------------------------------------------------------------------
	def widthHeight(self,value):
		""""""
		self.edit(widthHeight=value)
	#----------------------------------------------------------------------
	def get_minRange(self):
		""""""
		return self.query(minRange=True)
	#----------------------------------------------------------------------
	def set_minRange(self, value):
		""""""
		self.edit(minRange=value)
	#----------------------------------------------------------------------
	minRange = property(get_minRange, set_minRange)
	#----------------------------------------------------------------------
	def get_maxRange(self):
		""""""
		return self.query(maxRange=True)
	#----------------------------------------------------------------------
	def set_maxRange(self, value):
		""""""
		self.edit(maxRange=value)
	#----------------------------------------------------------------------
	maxRange = property(get_maxRange, set_maxRange)
########################################################################
class ScriptTable(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scriptTable(**kwargs)
			super(ScriptTable, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scriptTable(name, exists=True):
				super(ScriptTable, self).__init__(name)
			else:
				name = cmds.scriptTable(name, **kwargs)
				super(ScriptTable, self).__init__(name, **dict(qtParent=parent))
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
	def label(self,value):
		""""""
		self.edit(label=value)
	#----------------------------------------------------------------------
	def columnWidth(self,value):
		""""""
		self.edit(columnWidth=value)
	#----------------------------------------------------------------------
	@property
	def selectedRow(self):
		""""""
		return self.query(selectedRow=True)
	#----------------------------------------------------------------------
	def get_selectedCells(self):
		""""""
		return self.query(selectedCells=True)
	#----------------------------------------------------------------------
	def set_selectedCells(self, value):
		""""""
		self.edit(selectedCells=value)
	#----------------------------------------------------------------------
	selectedCells = property(get_selectedCells, set_selectedCells)
	#----------------------------------------------------------------------
	def get_selectedRows(self):
		""""""
		return self.query(selectedRows=True)
	#----------------------------------------------------------------------
	def set_selectedRows(self, value):
		""""""
		self.edit(selectedRows=value)
	#----------------------------------------------------------------------
	selectedRows = property(get_selectedRows, set_selectedRows)
	#----------------------------------------------------------------------
	def get_selectedColumns(self):
		""""""
		return self.query(selectedColumns=True)
	#----------------------------------------------------------------------
	def set_selectedColumns(self, value):
		""""""
		self.edit(selectedColumns=value)
	#----------------------------------------------------------------------
	selectedColumns = property(get_selectedColumns, set_selectedColumns)
	#----------------------------------------------------------------------
	def get_rowHeight(self):
		""""""
		return self.query(rowHeight=True)
	#----------------------------------------------------------------------
	def set_rowHeight(self, value):
		""""""
		self.edit(rowHeight=value)
	#----------------------------------------------------------------------
	rowHeight = property(get_rowHeight, set_rowHeight)
	#----------------------------------------------------------------------
	def get_multiEditEnabled(self):
		""""""
		return self.query(multiEditEnabled=True)
	#----------------------------------------------------------------------
	def set_multiEditEnabled(self, value):
		""""""
		self.edit(multiEditEnabled=value)
	#----------------------------------------------------------------------
	multiEditEnabled = property(get_multiEditEnabled, set_multiEditEnabled)
	#----------------------------------------------------------------------
	def get_useDoubleClickEdit(self):
		""""""
		return self.query(useDoubleClickEdit=True)
	#----------------------------------------------------------------------
	def set_useDoubleClickEdit(self, value):
		""""""
		self.edit(useDoubleClickEdit=value)
	#----------------------------------------------------------------------
	useDoubleClickEdit = property(get_useDoubleClickEdit, set_useDoubleClickEdit)
	#----------------------------------------------------------------------
	@property
	def underPointerRow(self):
		""""""
		return self.query(underPointerRow=True)
	#----------------------------------------------------------------------
	@property
	def underPointerColumn(self):
		""""""
		return self.query(underPointerColumn=True)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def getCellCmd(self,value):
		""""""
		self.edit(getCellCmd=value)
	#----------------------------------------------------------------------
	def cellBackgroundColorCommand(self,value):
		""""""
		self.edit(cellBackgroundColorCommand=value)
	#----------------------------------------------------------------------
	def cellForegroundColorCommand(self,value):
		""""""
		self.edit(cellForegroundColorCommand=value)
	#----------------------------------------------------------------------
	def cellChangedCmd(self,value):
		""""""
		self.edit(cellChangedCmd=value)
	#----------------------------------------------------------------------
	def get_selectionBehavior(self):
		""""""
		return self.query(selectionBehavior=True)
	#----------------------------------------------------------------------
	def set_selectionBehavior(self, value):
		""""""
		self.edit(selectionBehavior=value)
	#----------------------------------------------------------------------
	selectionBehavior = property(get_selectionBehavior, set_selectionBehavior)
	#----------------------------------------------------------------------
	def get_selectionMode(self):
		""""""
		return self.query(selectionMode=True)
	#----------------------------------------------------------------------
	def set_selectionMode(self, value):
		""""""
		self.edit(selectionMode=value)
	#----------------------------------------------------------------------
	selectionMode = property(get_selectionMode, set_selectionMode)
	#----------------------------------------------------------------------
	def get_rows(self):
		""""""
		return self.query(rows=True)
	#----------------------------------------------------------------------
	def set_rows(self, value):
		""""""
		self.edit(rows=value)
	#----------------------------------------------------------------------
	rows = property(get_rows, set_rows)
	#----------------------------------------------------------------------
	def get_columns(self):
		""""""
		return self.query(columns=True)
	#----------------------------------------------------------------------
	def set_columns(self, value):
		""""""
		self.edit(columns=value)
	#----------------------------------------------------------------------
	columns = property(get_columns, set_columns)
	#----------------------------------------------------------------------
	def get_sortEnabled(self):
		""""""
		return self.query(sortEnabled=True)
	#----------------------------------------------------------------------
	def set_sortEnabled(self, value):
		""""""
		self.edit(sortEnabled=value)
	#----------------------------------------------------------------------
	sortEnabled = property(get_sortEnabled, set_sortEnabled)
	#----------------------------------------------------------------------
	@property
	def excludingHeaders(self):
		""""""
		return self.query(excludingHeaders=True)
	#----------------------------------------------------------------------
	def insertRow(self,value):
		""""""
		self.edit(insertRow=value)
	#----------------------------------------------------------------------
	def deleteRow(self,value):
		""""""
		self.edit(deleteRow=value)
	#----------------------------------------------------------------------
	def clearRow(self,value):
		""""""
		self.edit(clearRow=value)
	#----------------------------------------------------------------------
	def clearTable(self,value):
		""""""
		self.edit(clearTable=value)
	#----------------------------------------------------------------------
	def get_cellIndex(self):
		""""""
		return self.query(cellIndex=True)
	#----------------------------------------------------------------------
	def set_cellIndex(self, value):
		""""""
		self.edit(cellIndex=value)
	#----------------------------------------------------------------------
	cellIndex = property(get_cellIndex, set_cellIndex)
	#----------------------------------------------------------------------
	def get_cellValue(self):
		""""""
		return self.query(cellValue=True)
	#----------------------------------------------------------------------
	def set_cellValue(self, value):
		""""""
		self.edit(cellValue=value)
	#----------------------------------------------------------------------
	cellValue = property(get_cellValue, set_cellValue)
	#----------------------------------------------------------------------
	def columnFilter(self,value):
		""""""
		self.edit(columnFilter=value)
########################################################################
class ScrollField(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.scrollField(**kwargs)
			super(ScrollField, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.scrollField(name, exists=True):
				super(ScrollField, self).__init__(name)
			else:
				name = cmds.scrollField(name, **kwargs)
				super(ScrollField, self).__init__(name, **dict(qtParent=parent))
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
	def enterCommand(self,value):
		""""""
		self.edit(enterCommand=value)
	#----------------------------------------------------------------------
	def keyPressCommand(self,value):
		""""""
		self.edit(keyPressCommand=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
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
	def get_text(self):
		""""""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		""""""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	def insertText(self,value):
		""""""
		self.edit(insertText=value)
	#----------------------------------------------------------------------
	def get_insertionPosition(self):
		""""""
		return self.query(insertionPosition=True)
	#----------------------------------------------------------------------
	def set_insertionPosition(self, value):
		""""""
		self.edit(insertionPosition=value)
	#----------------------------------------------------------------------
	insertionPosition = property(get_insertionPosition, set_insertionPosition)
	#----------------------------------------------------------------------
	@property
	def selection(self):
		""""""
		return self.query(selection=True)
	#----------------------------------------------------------------------
	def clear(self,value):
		""""""
		self.edit(clear=value)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	@property
	def numberOfLines(self):
		""""""
		return self.query(numberOfLines=True)
########################################################################
class Separator(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.separator(**kwargs)
			super(Separator, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.separator(name, exists=True):
				super(Separator, self).__init__(name)
			else:
				name = cmds.separator(name, **kwargs)
				super(Separator, self).__init__(name, **dict(qtParent=parent))
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
	@property
	def horizontal(self):
		""""""
		return self.query(horizontal=True)
########################################################################
class ShelfButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.shelfButton(**kwargs)
			super(ShelfButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.shelfButton(name, exists=True):
				super(ShelfButton, self).__init__(name)
			else:
				name = cmds.shelfButton(name, **kwargs)
				super(ShelfButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		""""""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		""""""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
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
	def get_disabledImage(self):
		""""""
		return self.query(disabledImage=True)
	#----------------------------------------------------------------------
	def set_disabledImage(self, value):
		""""""
		self.edit(disabledImage=value)
	#----------------------------------------------------------------------
	disabledImage = property(get_disabledImage, set_disabledImage)
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
	def get_overlayLabelColor(self):
		""""""
		return self.query(overlayLabelColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelColor(self, value):
		""""""
		self.edit(overlayLabelColor=value)
	#----------------------------------------------------------------------
	overlayLabelColor = property(get_overlayLabelColor, set_overlayLabelColor)
	#----------------------------------------------------------------------
	def get_overlayLabelBackColor(self):
		""""""
		return self.query(overlayLabelBackColor=True)
	#----------------------------------------------------------------------
	def set_overlayLabelBackColor(self, value):
		""""""
		self.edit(overlayLabelBackColor=value)
	#----------------------------------------------------------------------
	overlayLabelBackColor = property(get_overlayLabelBackColor, set_overlayLabelBackColor)
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
	#----------------------------------------------------------------------
	def get_labelOffset(self):
		""""""
		return self.query(labelOffset=True)
	#----------------------------------------------------------------------
	def set_labelOffset(self, value):
		""""""
		self.edit(labelOffset=value)
	#----------------------------------------------------------------------
	labelOffset = property(get_labelOffset, set_labelOffset)
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
	def get_version(self):
		""""""
		return self.query(version=True)
	#----------------------------------------------------------------------
	def set_version(self, value):
		""""""
		self.edit(version=value)
	#----------------------------------------------------------------------
	version = property(get_version, set_version)
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
	def get_doubleClickCommand(self):
		""""""
		return self.query(doubleClickCommand=True)
	#----------------------------------------------------------------------
	def set_doubleClickCommand(self, value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	doubleClickCommand = property(get_doubleClickCommand, set_doubleClickCommand)
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
	def get_selectionImage(self):
		""""""
		return self.query(selectionImage=True)
	#----------------------------------------------------------------------
	def set_selectionImage(self, value):
		""""""
		self.edit(selectionImage=value)
	#----------------------------------------------------------------------
	selectionImage = property(get_selectionImage, set_selectionImage)
	#----------------------------------------------------------------------
	def get_highlightImage(self):
		""""""
		return self.query(highlightImage=True)
	#----------------------------------------------------------------------
	def set_highlightImage(self, value):
		""""""
		self.edit(highlightImage=value)
	#----------------------------------------------------------------------
	highlightImage = property(get_highlightImage, set_highlightImage)
	#----------------------------------------------------------------------
	def handleNodeDropCallback(self,value):
		""""""
		self.edit(handleNodeDropCallback=value)
	#----------------------------------------------------------------------
	def labelEditingCallback(self,value):
		""""""
		self.edit(labelEditingCallback=value)
	#----------------------------------------------------------------------
	def get_commandRepeatable(self):
		""""""
		return self.query(commandRepeatable=True)
	#----------------------------------------------------------------------
	def set_commandRepeatable(self, value):
		""""""
		self.edit(commandRepeatable=value)
	#----------------------------------------------------------------------
	commandRepeatable = property(get_commandRepeatable, set_commandRepeatable)
	#----------------------------------------------------------------------
	def get_flat(self):
		""""""
		return self.query(flat=True)
	#----------------------------------------------------------------------
	def set_flat(self, value):
		""""""
		self.edit(flat=value)
	#----------------------------------------------------------------------
	flat = property(get_flat, set_flat)
########################################################################
class SoundControl(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.soundControl(**kwargs)
			super(SoundControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.soundControl(name, exists=True):
				super(SoundControl, self).__init__(name)
			else:
				name = cmds.soundControl(name, **kwargs)
				super(SoundControl, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	def get_sound(self):
		""""""
		return self.query(sound=True)
	#----------------------------------------------------------------------
	def set_sound(self, value):
		""""""
		self.edit(sound=value)
	#----------------------------------------------------------------------
	sound = property(get_sound, set_sound)
	#----------------------------------------------------------------------
	def get_displaySound(self):
		""""""
		return self.query(displaySound=True)
	#----------------------------------------------------------------------
	def set_displaySound(self, value):
		""""""
		self.edit(displaySound=value)
	#----------------------------------------------------------------------
	displaySound = property(get_displaySound, set_displaySound)
	#----------------------------------------------------------------------
	def get_waveform(self):
		""""""
		return self.query(waveform=True)
	#----------------------------------------------------------------------
	def set_waveform(self, value):
		""""""
		self.edit(waveform=value)
	#----------------------------------------------------------------------
	waveform = property(get_waveform, set_waveform)
	#----------------------------------------------------------------------
	def resample(self,value):
		""""""
		self.edit(resample=value)
	#----------------------------------------------------------------------
	def get_repeatOnHold(self):
		""""""
		return self.query(repeatOnHold=True)
	#----------------------------------------------------------------------
	def set_repeatOnHold(self, value):
		""""""
		self.edit(repeatOnHold=value)
	#----------------------------------------------------------------------
	repeatOnHold = property(get_repeatOnHold, set_repeatOnHold)
	#----------------------------------------------------------------------
	def get_repeatChunkSize(self):
		""""""
		return self.query(repeatChunkSize=True)
	#----------------------------------------------------------------------
	def set_repeatChunkSize(self, value):
		""""""
		self.edit(repeatChunkSize=value)
	#----------------------------------------------------------------------
	repeatChunkSize = property(get_repeatChunkSize, set_repeatChunkSize)
	#----------------------------------------------------------------------
	def beginScrub(self,value):
		""""""
		self.edit(beginScrub=value)
	#----------------------------------------------------------------------
	def endScrub(self,value):
		""""""
		self.edit(endScrub=value)
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
	def get_minTime(self):
		""""""
		return self.query(minTime=True)
	#----------------------------------------------------------------------
	def set_minTime(self, value):
		""""""
		self.edit(minTime=value)
	#----------------------------------------------------------------------
	minTime = property(get_minTime, set_minTime)
	#----------------------------------------------------------------------
	def get_maxTime(self):
		""""""
		return self.query(maxTime=True)
	#----------------------------------------------------------------------
	def set_maxTime(self, value):
		""""""
		self.edit(maxTime=value)
	#----------------------------------------------------------------------
	maxTime = property(get_maxTime, set_maxTime)
	#----------------------------------------------------------------------
	def pressCommand(self,value):
		""""""
		self.edit(pressCommand=value)
	#----------------------------------------------------------------------
	def releaseCommand(self,value):
		""""""
		self.edit(releaseCommand=value)
########################################################################
class SwatchDisplayPort(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.swatchDisplayPort(**kwargs)
			super(SwatchDisplayPort, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.swatchDisplayPort(name, exists=True):
				super(SwatchDisplayPort, self).__init__(name)
			else:
				name = cmds.swatchDisplayPort(name, **kwargs)
				super(SwatchDisplayPort, self).__init__(name, **dict(qtParent=parent))
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
	def get_shadingNode(self):
		""""""
		return self.query(shadingNode=True)
	#----------------------------------------------------------------------
	def set_shadingNode(self, value):
		""""""
		self.edit(shadingNode=value)
	#----------------------------------------------------------------------
	shadingNode = property(get_shadingNode, set_shadingNode)
	#----------------------------------------------------------------------
	def widthHeight(self,value):
		""""""
		self.edit(widthHeight=value)
	#----------------------------------------------------------------------
	def get_renderSize(self):
		""""""
		return self.query(renderSize=True)
	#----------------------------------------------------------------------
	def set_renderSize(self, value):
		""""""
		self.edit(renderSize=value)
	#----------------------------------------------------------------------
	renderSize = property(get_renderSize, set_renderSize)
	#----------------------------------------------------------------------
	def get_borderWidth(self):
		""""""
		return self.query(borderWidth=True)
	#----------------------------------------------------------------------
	def set_borderWidth(self, value):
		""""""
		self.edit(borderWidth=value)
	#----------------------------------------------------------------------
	borderWidth = property(get_borderWidth, set_borderWidth)
	#----------------------------------------------------------------------
	def get_borderColor(self):
		""""""
		return self.query(borderColor=True)
	#----------------------------------------------------------------------
	def set_borderColor(self, value):
		""""""
		self.edit(borderColor=value)
	#----------------------------------------------------------------------
	borderColor = property(get_borderColor, set_borderColor)
	#----------------------------------------------------------------------
	def pressCommand(self,value):
		""""""
		self.edit(pressCommand=value)
########################################################################
class SwitchTable(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.switchTable(**kwargs)
			super(SwitchTable, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.switchTable(name, exists=True):
				super(SwitchTable, self).__init__(name)
			else:
				name = cmds.switchTable(name, **kwargs)
				super(SwitchTable, self).__init__(name, **dict(qtParent=parent))
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
	def label1(self,value):
		""""""
		self.edit(label1=value)
	#----------------------------------------------------------------------
	def label2(self,value):
		""""""
		self.edit(label2=value)
	#----------------------------------------------------------------------
	def get_switchNode(self):
		""""""
		return self.query(switchNode=True)
	#----------------------------------------------------------------------
	def set_switchNode(self, value):
		""""""
		self.edit(switchNode=value)
	#----------------------------------------------------------------------
	switchNode = property(get_switchNode, set_switchNode)
	#----------------------------------------------------------------------
	@property
	def selectedRow(self):
		""""""
		return self.query(selectedRow=True)
	#----------------------------------------------------------------------
	@property
	def underPointerRow(self):
		""""""
		return self.query(underPointerRow=True)
########################################################################
class SymbolButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.symbolButton(**kwargs)
			super(SymbolButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.symbolButton(name, exists=True):
				super(SymbolButton, self).__init__(name)
			else:
				name = cmds.symbolButton(name, **kwargs)
				super(SymbolButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_command(self):
		""""""
		return self.query(command=True)
	#----------------------------------------------------------------------
	def set_command(self, value):
		""""""
		self.edit(command=value)
	#----------------------------------------------------------------------
	command = property(get_command, set_command)
########################################################################
class SymbolCheckBox(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.symbolCheckBox(**kwargs)
			super(SymbolCheckBox, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.symbolCheckBox(name, exists=True):
				super(SymbolCheckBox, self).__init__(name)
			else:
				name = cmds.symbolCheckBox(name, **kwargs)
				super(SymbolCheckBox, self).__init__(name, **dict(qtParent=parent))
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
	def get_offImage(self):
		""""""
		return self.query(offImage=True)
	#----------------------------------------------------------------------
	def set_offImage(self, value):
		""""""
		self.edit(offImage=value)
	#----------------------------------------------------------------------
	offImage = property(get_offImage, set_offImage)
	#----------------------------------------------------------------------
	def get_onImage(self):
		""""""
		return self.query(onImage=True)
	#----------------------------------------------------------------------
	def set_onImage(self, value):
		""""""
		self.edit(onImage=value)
	#----------------------------------------------------------------------
	onImage = property(get_onImage, set_onImage)
	#----------------------------------------------------------------------
	def get_disableOffImage(self):
		""""""
		return self.query(disableOffImage=True)
	#----------------------------------------------------------------------
	def set_disableOffImage(self, value):
		""""""
		self.edit(disableOffImage=value)
	#----------------------------------------------------------------------
	disableOffImage = property(get_disableOffImage, set_disableOffImage)
	#----------------------------------------------------------------------
	def get_disableOnImage(self):
		""""""
		return self.query(disableOnImage=True)
	#----------------------------------------------------------------------
	def set_disableOnImage(self, value):
		""""""
		self.edit(disableOnImage=value)
	#----------------------------------------------------------------------
	disableOnImage = property(get_disableOnImage, set_disableOnImage)
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
	def onCommand(self,value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def get_innerMargin(self):
		""""""
		return self.query(innerMargin=True)
	#----------------------------------------------------------------------
	def set_innerMargin(self, value):
		""""""
		self.edit(innerMargin=value)
	#----------------------------------------------------------------------
	innerMargin = property(get_innerMargin, set_innerMargin)
########################################################################
class Text(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.text(**kwargs)
			super(Text, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.text(name, exists=True):
				super(Text, self).__init__(name)
			else:
				name = cmds.text(name, **kwargs)
				super(Text, self).__init__(name, **dict(qtParent=parent))
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
	def get_align(self):
		""""""
		return self.query(align=True)
	#----------------------------------------------------------------------
	def set_align(self, value):
		""""""
		self.edit(align=value)
	#----------------------------------------------------------------------
	align = property(get_align, set_align)
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
	def get_recomputeSize(self):
		""""""
		return self.query(recomputeSize=True)
	#----------------------------------------------------------------------
	def set_recomputeSize(self, value):
		""""""
		self.edit(recomputeSize=value)
	#----------------------------------------------------------------------
	recomputeSize = property(get_recomputeSize, set_recomputeSize)
	#----------------------------------------------------------------------
	@property
	def wordWrap(self):
		""""""
		return self.query(wordWrap=True)
	#----------------------------------------------------------------------
	def dropRectCallback(self,value):
		""""""
		self.edit(dropRectCallback=value)
	#----------------------------------------------------------------------
	def get_hyperlink(self):
		""""""
		return self.query(hyperlink=True)
	#----------------------------------------------------------------------
	def set_hyperlink(self, value):
		""""""
		self.edit(hyperlink=value)
	#----------------------------------------------------------------------
	hyperlink = property(get_hyperlink, set_hyperlink)
########################################################################
class TextField(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textField(**kwargs)
			super(TextField, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textField(name, exists=True):
				super(TextField, self).__init__(name)
			else:
				name = cmds.textField(name, **kwargs)
				super(TextField, self).__init__(name, **dict(qtParent=parent))
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
	def get_text(self):
		""""""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		""""""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	def get_placeholderText(self):
		""""""
		return self.query(placeholderText=True)
	#----------------------------------------------------------------------
	def set_placeholderText(self, value):
		""""""
		self.edit(placeholderText=value)
	#----------------------------------------------------------------------
	placeholderText = property(get_placeholderText, set_placeholderText)
	#----------------------------------------------------------------------
	def get_fileName(self):
		""""""
		return self.query(fileName=True)
	#----------------------------------------------------------------------
	def set_fileName(self, value):
		""""""
		self.edit(fileName=value)
	#----------------------------------------------------------------------
	fileName = property(get_fileName, set_fileName)
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
	def insertText(self,value):
		""""""
		self.edit(insertText=value)
	#----------------------------------------------------------------------
	def get_insertionPosition(self):
		""""""
		return self.query(insertionPosition=True)
	#----------------------------------------------------------------------
	def set_insertionPosition(self, value):
		""""""
		self.edit(insertionPosition=value)
	#----------------------------------------------------------------------
	insertionPosition = property(get_insertionPosition, set_insertionPosition)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def enterCommand(self,value):
		""""""
		self.edit(enterCommand=value)
	#----------------------------------------------------------------------
	def receiveFocusCommand(self,value):
		""""""
		self.edit(receiveFocusCommand=value)
	#----------------------------------------------------------------------
	def get_alwaysInvokeEnterCommandOnReturn(self):
		""""""
		return self.query(alwaysInvokeEnterCommandOnReturn=True)
	#----------------------------------------------------------------------
	def set_alwaysInvokeEnterCommandOnReturn(self, value):
		""""""
		self.edit(alwaysInvokeEnterCommandOnReturn=value)
	#----------------------------------------------------------------------
	alwaysInvokeEnterCommandOnReturn = property(get_alwaysInvokeEnterCommandOnReturn, set_alwaysInvokeEnterCommandOnReturn)
########################################################################
class TextFieldButtonGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textFieldButtonGrp(**kwargs)
			super(TextFieldButtonGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textFieldButtonGrp(name, exists=True):
				super(TextFieldButtonGrp, self).__init__(name)
			else:
				name = cmds.textFieldButtonGrp(name, **kwargs)
				super(TextFieldButtonGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_text(self):
		""""""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		""""""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	def get_placeholderText(self):
		""""""
		return self.query(placeholderText=True)
	#----------------------------------------------------------------------
	def set_placeholderText(self, value):
		""""""
		self.edit(placeholderText=value)
	#----------------------------------------------------------------------
	placeholderText = property(get_placeholderText, set_placeholderText)
	#----------------------------------------------------------------------
	def get_fileName(self):
		""""""
		return self.query(fileName=True)
	#----------------------------------------------------------------------
	def set_fileName(self, value):
		""""""
		self.edit(fileName=value)
	#----------------------------------------------------------------------
	fileName = property(get_fileName, set_fileName)
	#----------------------------------------------------------------------
	def insertText(self,value):
		""""""
		self.edit(insertText=value)
	#----------------------------------------------------------------------
	def get_insertionPosition(self):
		""""""
		return self.query(insertionPosition=True)
	#----------------------------------------------------------------------
	def set_insertionPosition(self, value):
		""""""
		self.edit(insertionPosition=value)
	#----------------------------------------------------------------------
	insertionPosition = property(get_insertionPosition, set_insertionPosition)
	#----------------------------------------------------------------------
	def forceChangeCommand(self,value):
		""""""
		self.edit(forceChangeCommand=value)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def textChangedCommand(self,value):
		""""""
		self.edit(textChangedCommand=value)
	#----------------------------------------------------------------------
	def get_buttonLabel(self):
		""""""
		return self.query(buttonLabel=True)
	#----------------------------------------------------------------------
	def set_buttonLabel(self, value):
		""""""
		self.edit(buttonLabel=value)
	#----------------------------------------------------------------------
	buttonLabel = property(get_buttonLabel, set_buttonLabel)
	#----------------------------------------------------------------------
	def buttonCommand(self,value):
		""""""
		self.edit(buttonCommand=value)
	#----------------------------------------------------------------------
	def get_enableButton(self):
		""""""
		return self.query(enableButton=True)
	#----------------------------------------------------------------------
	def set_enableButton(self, value):
		""""""
		self.edit(enableButton=value)
	#----------------------------------------------------------------------
	enableButton = property(get_enableButton, set_enableButton)
########################################################################
class TextFieldGrp(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textFieldGrp(**kwargs)
			super(TextFieldGrp, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textFieldGrp(name, exists=True):
				super(TextFieldGrp, self).__init__(name)
			else:
				name = cmds.textFieldGrp(name, **kwargs)
				super(TextFieldGrp, self).__init__(name, **dict(qtParent=parent))
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
	def get_text(self):
		""""""
		return self.query(text=True)
	#----------------------------------------------------------------------
	def set_text(self, value):
		""""""
		self.edit(text=value)
	#----------------------------------------------------------------------
	text = property(get_text, set_text)
	#----------------------------------------------------------------------
	def get_placeholderText(self):
		""""""
		return self.query(placeholderText=True)
	#----------------------------------------------------------------------
	def set_placeholderText(self, value):
		""""""
		self.edit(placeholderText=value)
	#----------------------------------------------------------------------
	placeholderText = property(get_placeholderText, set_placeholderText)
	#----------------------------------------------------------------------
	def get_fileName(self):
		""""""
		return self.query(fileName=True)
	#----------------------------------------------------------------------
	def set_fileName(self, value):
		""""""
		self.edit(fileName=value)
	#----------------------------------------------------------------------
	fileName = property(get_fileName, set_fileName)
	#----------------------------------------------------------------------
	def insertText(self,value):
		""""""
		self.edit(insertText=value)
	#----------------------------------------------------------------------
	def get_insertionPosition(self):
		""""""
		return self.query(insertionPosition=True)
	#----------------------------------------------------------------------
	def set_insertionPosition(self, value):
		""""""
		self.edit(insertionPosition=value)
	#----------------------------------------------------------------------
	insertionPosition = property(get_insertionPosition, set_insertionPosition)
	#----------------------------------------------------------------------
	def forceChangeCommand(self,value):
		""""""
		self.edit(forceChangeCommand=value)
	#----------------------------------------------------------------------
	def get_editable(self):
		""""""
		return self.query(editable=True)
	#----------------------------------------------------------------------
	def set_editable(self, value):
		""""""
		self.edit(editable=value)
	#----------------------------------------------------------------------
	editable = property(get_editable, set_editable)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def textChangedCommand(self,value):
		""""""
		self.edit(textChangedCommand=value)
########################################################################
class TextScrollList(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.textScrollList(**kwargs)
			super(TextScrollList, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.textScrollList(name, exists=True):
				super(TextScrollList, self).__init__(name)
			else:
				name = cmds.textScrollList(name, **kwargs)
				super(TextScrollList, self).__init__(name, **dict(qtParent=parent))
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
	def append(self,value):
		""""""
		self.edit(append=value)
	#----------------------------------------------------------------------
	def appendPosition(self,value):
		""""""
		self.edit(appendPosition=value)
	#----------------------------------------------------------------------
	@property
	def allItems(self):
		""""""
		return self.query(allItems=True)
	#----------------------------------------------------------------------
	def get_allowAutomaticSelection(self):
		""""""
		return self.query(allowAutomaticSelection=True)
	#----------------------------------------------------------------------
	def set_allowAutomaticSelection(self, value):
		""""""
		self.edit(allowAutomaticSelection=value)
	#----------------------------------------------------------------------
	allowAutomaticSelection = property(get_allowAutomaticSelection, set_allowAutomaticSelection)
	#----------------------------------------------------------------------
	def get_allowMultiSelection(self):
		""""""
		return self.query(allowMultiSelection=True)
	#----------------------------------------------------------------------
	def set_allowMultiSelection(self, value):
		""""""
		self.edit(allowMultiSelection=value)
	#----------------------------------------------------------------------
	allowMultiSelection = property(get_allowMultiSelection, set_allowMultiSelection)
	#----------------------------------------------------------------------
	def doubleClickCommand(self,value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	def deleteKeyCommand(self,value):
		""""""
		self.edit(deleteKeyCommand=value)
	#----------------------------------------------------------------------
	def lineFont(self,value):
		""""""
		self.edit(lineFont=value)
	#----------------------------------------------------------------------
	@property
	def numberOfItems(self):
		""""""
		return self.query(numberOfItems=True)
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
	@property
	def numberOfSelectedItems(self):
		""""""
		return self.query(numberOfSelectedItems=True)
	#----------------------------------------------------------------------
	def removeAll(self,value):
		""""""
		self.edit(removeAll=value)
	#----------------------------------------------------------------------
	def removeItem(self,value):
		""""""
		self.edit(removeItem=value)
	#----------------------------------------------------------------------
	def removeIndexedItem(self,value):
		""""""
		self.edit(removeIndexedItem=value)
	#----------------------------------------------------------------------
	def selectCommand(self,value):
		""""""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	def get_selectItem(self):
		""""""
		return self.query(selectItem=True)
	#----------------------------------------------------------------------
	def set_selectItem(self, value):
		""""""
		self.edit(selectItem=value)
	#----------------------------------------------------------------------
	selectItem = property(get_selectItem, set_selectItem)
	#----------------------------------------------------------------------
	def get_selectIndexedItem(self):
		""""""
		return self.query(selectIndexedItem=True)
	#----------------------------------------------------------------------
	def set_selectIndexedItem(self, value):
		""""""
		self.edit(selectIndexedItem=value)
	#----------------------------------------------------------------------
	selectIndexedItem = property(get_selectIndexedItem, set_selectIndexedItem)
	#----------------------------------------------------------------------
	def deselectAll(self,value):
		""""""
		self.edit(deselectAll=value)
	#----------------------------------------------------------------------
	def deselectItem(self,value):
		""""""
		self.edit(deselectItem=value)
	#----------------------------------------------------------------------
	def deselectIndexedItem(self,value):
		""""""
		self.edit(deselectIndexedItem=value)
	#----------------------------------------------------------------------
	def showIndexedItem(self,value):
		""""""
		self.edit(showIndexedItem=value)
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
	def uniqueTag(self,value):
		""""""
		self.edit(uniqueTag=value)
	#----------------------------------------------------------------------
	def get_selectUniqueTagItem(self):
		""""""
		return self.query(selectUniqueTagItem=True)
	#----------------------------------------------------------------------
	def set_selectUniqueTagItem(self, value):
		""""""
		self.edit(selectUniqueTagItem=value)
	#----------------------------------------------------------------------
	selectUniqueTagItem = property(get_selectUniqueTagItem, set_selectUniqueTagItem)
########################################################################
class TimeControl(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.timeControl(**kwargs)
			super(TimeControl, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.timeControl(name, exists=True):
				super(TimeControl, self).__init__(name)
			else:
				name = cmds.timeControl(name, **kwargs)
				super(TimeControl, self).__init__(name, **dict(qtParent=parent))
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
	def get_globalTime(self):
		""""""
		return self.query(globalTime=True)
	#----------------------------------------------------------------------
	def set_globalTime(self, value):
		""""""
		self.edit(globalTime=value)
	#----------------------------------------------------------------------
	globalTime = property(get_globalTime, set_globalTime)
	#----------------------------------------------------------------------
	def get_snap(self):
		""""""
		return self.query(snap=True)
	#----------------------------------------------------------------------
	def set_snap(self, value):
		""""""
		self.edit(snap=value)
	#----------------------------------------------------------------------
	snap = property(get_snap, set_snap)
	#----------------------------------------------------------------------
	def get_sound(self):
		""""""
		return self.query(sound=True)
	#----------------------------------------------------------------------
	def set_sound(self, value):
		""""""
		self.edit(sound=value)
	#----------------------------------------------------------------------
	sound = property(get_sound, set_sound)
	#----------------------------------------------------------------------
	def get_displaySound(self):
		""""""
		return self.query(displaySound=True)
	#----------------------------------------------------------------------
	def set_displaySound(self, value):
		""""""
		self.edit(displaySound=value)
	#----------------------------------------------------------------------
	displaySound = property(get_displaySound, set_displaySound)
	#----------------------------------------------------------------------
	def get_waveform(self):
		""""""
		return self.query(waveform=True)
	#----------------------------------------------------------------------
	def set_waveform(self, value):
		""""""
		self.edit(waveform=value)
	#----------------------------------------------------------------------
	waveform = property(get_waveform, set_waveform)
	#----------------------------------------------------------------------
	def resample(self,value):
		""""""
		self.edit(resample=value)
	#----------------------------------------------------------------------
	def get_repeatOnHold(self):
		""""""
		return self.query(repeatOnHold=True)
	#----------------------------------------------------------------------
	def set_repeatOnHold(self, value):
		""""""
		self.edit(repeatOnHold=value)
	#----------------------------------------------------------------------
	repeatOnHold = property(get_repeatOnHold, set_repeatOnHold)
	#----------------------------------------------------------------------
	def get_repeatChunkSize(self):
		""""""
		return self.query(repeatChunkSize=True)
	#----------------------------------------------------------------------
	def set_repeatChunkSize(self, value):
		""""""
		self.edit(repeatChunkSize=value)
	#----------------------------------------------------------------------
	repeatChunkSize = property(get_repeatChunkSize, set_repeatChunkSize)
	#----------------------------------------------------------------------
	def beginScrub(self,value):
		""""""
		self.edit(beginScrub=value)
	#----------------------------------------------------------------------
	def endScrub(self,value):
		""""""
		self.edit(endScrub=value)
	#----------------------------------------------------------------------
	def get_showKeys(self):
		""""""
		return self.query(showKeys=True)
	#----------------------------------------------------------------------
	def set_showKeys(self, value):
		""""""
		self.edit(showKeys=value)
	#----------------------------------------------------------------------
	showKeys = property(get_showKeys, set_showKeys)
	#----------------------------------------------------------------------
	def get_showGreaseFrames(self):
		""""""
		return self.query(showGreaseFrames=True)
	#----------------------------------------------------------------------
	def set_showGreaseFrames(self, value):
		""""""
		self.edit(showGreaseFrames=value)
	#----------------------------------------------------------------------
	showGreaseFrames = property(get_showGreaseFrames, set_showGreaseFrames)
	#----------------------------------------------------------------------
	def get_showKeysCombined(self):
		""""""
		return self.query(showKeysCombined=True)
	#----------------------------------------------------------------------
	def set_showKeysCombined(self, value):
		""""""
		self.edit(showKeysCombined=value)
	#----------------------------------------------------------------------
	showKeysCombined = property(get_showKeysCombined, set_showKeysCombined)
	#----------------------------------------------------------------------
	@property
	def animCurveNames(self):
		""""""
		return self.query(animCurveNames=True)
	#----------------------------------------------------------------------
	@property
	def greasePencilSequenceNames(self):
		""""""
		return self.query(greasePencilSequenceNames=True)
	#----------------------------------------------------------------------
	@property
	def range(self):
		""""""
		return self.query(range=True)
	#----------------------------------------------------------------------
	@property
	def rangeArray(self):
		""""""
		return self.query(rangeArray=True)
	#----------------------------------------------------------------------
	@property
	def rangeVisible(self):
		""""""
		return self.query(rangeVisible=True)
	#----------------------------------------------------------------------
	def pressCommand(self,value):
		""""""
		self.edit(pressCommand=value)
	#----------------------------------------------------------------------
	def releaseCommand(self,value):
		""""""
		self.edit(releaseCommand=value)
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
	def get_tickSize(self):
		""""""
		return self.query(tickSize=True)
	#----------------------------------------------------------------------
	def set_tickSize(self, value):
		""""""
		self.edit(tickSize=value)
	#----------------------------------------------------------------------
	tickSize = property(get_tickSize, set_tickSize)
	#----------------------------------------------------------------------
	def get_tickSpan(self):
		""""""
		return self.query(tickSpan=True)
	#----------------------------------------------------------------------
	def set_tickSpan(self, value):
		""""""
		self.edit(tickSpan=value)
	#----------------------------------------------------------------------
	tickSpan = property(get_tickSpan, set_tickSpan)
	#----------------------------------------------------------------------
	def forceRefresh(self,value):
		""""""
		self.edit(forceRefresh=value)
########################################################################
class TimePort(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.timePort(**kwargs)
			super(TimePort, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.timePort(name, exists=True):
				super(TimePort, self).__init__(name)
			else:
				name = cmds.timePort(name, **kwargs)
				super(TimePort, self).__init__(name, **dict(qtParent=parent))
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
	def get_globalTime(self):
		""""""
		return self.query(globalTime=True)
	#----------------------------------------------------------------------
	def set_globalTime(self, value):
		""""""
		self.edit(globalTime=value)
	#----------------------------------------------------------------------
	globalTime = property(get_globalTime, set_globalTime)
	#----------------------------------------------------------------------
	def get_snap(self):
		""""""
		return self.query(snap=True)
	#----------------------------------------------------------------------
	def set_snap(self, value):
		""""""
		self.edit(snap=value)
	#----------------------------------------------------------------------
	snap = property(get_snap, set_snap)
########################################################################
class ToolButton(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toolButton(**kwargs)
			super(ToolButton, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toolButton(name, exists=True):
				super(ToolButton, self).__init__(name)
			else:
				name = cmds.toolButton(name, **kwargs)
				super(ToolButton, self).__init__(name, **dict(qtParent=parent))
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
	def get_image1(self):
		""""""
		return self.query(image1=True)
	#----------------------------------------------------------------------
	def set_image1(self, value):
		""""""
		self.edit(image1=value)
	#----------------------------------------------------------------------
	image1 = property(get_image1, set_image1)
	#----------------------------------------------------------------------
	def get_image2(self):
		""""""
		return self.query(image2=True)
	#----------------------------------------------------------------------
	def set_image2(self, value):
		""""""
		self.edit(image2=value)
	#----------------------------------------------------------------------
	image2 = property(get_image2, set_image2)
	#----------------------------------------------------------------------
	def get_image3(self):
		""""""
		return self.query(image3=True)
	#----------------------------------------------------------------------
	def set_image3(self, value):
		""""""
		self.edit(image3=value)
	#----------------------------------------------------------------------
	image3 = property(get_image3, set_image3)
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
	def get_toolImage1(self):
		""""""
		return self.query(toolImage1=True)
	#----------------------------------------------------------------------
	def set_toolImage1(self, value):
		""""""
		self.edit(toolImage1=value)
	#----------------------------------------------------------------------
	toolImage1 = property(get_toolImage1, set_toolImage1)
	#----------------------------------------------------------------------
	def get_toolImage2(self):
		""""""
		return self.query(toolImage2=True)
	#----------------------------------------------------------------------
	def set_toolImage2(self, value):
		""""""
		self.edit(toolImage2=value)
	#----------------------------------------------------------------------
	toolImage2 = property(get_toolImage2, set_toolImage2)
	#----------------------------------------------------------------------
	def get_toolImage3(self):
		""""""
		return self.query(toolImage3=True)
	#----------------------------------------------------------------------
	def set_toolImage3(self, value):
		""""""
		self.edit(toolImage3=value)
	#----------------------------------------------------------------------
	toolImage3 = property(get_toolImage3, set_toolImage3)
	#----------------------------------------------------------------------
	def style(self,value):
		""""""
		self.edit(style=value)
	#----------------------------------------------------------------------
	def onCommand(self,value):
		""""""
		self.edit(onCommand=value)
	#----------------------------------------------------------------------
	def offCommand(self,value):
		""""""
		self.edit(offCommand=value)
	#----------------------------------------------------------------------
	def changeCommand(self,value):
		""""""
		self.edit(changeCommand=value)
	#----------------------------------------------------------------------
	def collection(self,value):
		""""""
		self.edit(collection=value)
	#----------------------------------------------------------------------
	def doubleClickCommand(self,value):
		""""""
		self.edit(doubleClickCommand=value)
	#----------------------------------------------------------------------
	def select(self,value):
		""""""
		self.edit(select=value)
	#----------------------------------------------------------------------
	def get_tool(self):
		""""""
		return self.query(tool=True)
	#----------------------------------------------------------------------
	def set_tool(self, value):
		""""""
		self.edit(tool=value)
	#----------------------------------------------------------------------
	tool = property(get_tool, set_tool)
	#----------------------------------------------------------------------
	@property
	def allowMultipleTools(self):
		""""""
		return self.query(allowMultipleTools=True)
	#----------------------------------------------------------------------
	@property
	def toolCount(self):
		""""""
		return self.query(toolCount=True)
	#----------------------------------------------------------------------
	@property
	def toolArray(self):
		""""""
		return self.query(toolArray=True)
	#----------------------------------------------------------------------
	def get_popupIndicatorVisible(self):
		""""""
		return self.query(popupIndicatorVisible=True)
	#----------------------------------------------------------------------
	def set_popupIndicatorVisible(self, value):
		""""""
		self.edit(popupIndicatorVisible=value)
	#----------------------------------------------------------------------
	popupIndicatorVisible = property(get_popupIndicatorVisible, set_popupIndicatorVisible)
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
class ToolCollection(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.toolCollection(**kwargs)
			super(ToolCollection, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.toolCollection(name, exists=True):
				super(ToolCollection, self).__init__(name)
			else:
				name = cmds.toolCollection(name, **kwargs)
				super(ToolCollection, self).__init__(name, **dict(qtParent=parent))
	#----------------------------------------------------------------------
	@property
	def gl(self):
		""""""
		return self.query(gl=True)
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
	@property
	def numberOfCollectionItems(self):
		""""""
		return self.query(numberOfCollectionItems=True)
	#----------------------------------------------------------------------
	@property
	def collectionItemArray(self):
		""""""
		return self.query(collectionItemArray=True)
########################################################################
class TreeLister(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.treeLister(**kwargs)
			super(TreeLister, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.treeLister(name, exists=True):
				super(TreeLister, self).__init__(name)
			else:
				name = cmds.treeLister(name, **kwargs)
				super(TreeLister, self).__init__(name, **dict(qtParent=parent))
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
	def addItem(self,value):
		""""""
		self.edit(addItem=value)
	#----------------------------------------------------------------------
	def addFavorite(self,value):
		""""""
		self.edit(addFavorite=value)
	#----------------------------------------------------------------------
	def clearContents(self,value):
		""""""
		self.edit(clearContents=value)
	#----------------------------------------------------------------------
	def executeItem(self,value):
		""""""
		self.edit(executeItem=value)
	#----------------------------------------------------------------------
	@property
	def favoritesList(self):
		""""""
		return self.query(favoritesList=True)
	#----------------------------------------------------------------------
	def removeFavorite(self,value):
		""""""
		self.edit(removeFavorite=value)
	#----------------------------------------------------------------------
	def removeItem(self,value):
		""""""
		self.edit(removeItem=value)
	#----------------------------------------------------------------------
	@property
	def resultsPathUnderCursor(self):
		""""""
		return self.query(resultsPathUnderCursor=True)
	#----------------------------------------------------------------------
	def collapsePath(self,value):
		""""""
		self.edit(collapsePath=value)
	#----------------------------------------------------------------------
	def expandPath(self,value):
		""""""
		self.edit(expandPath=value)
	#----------------------------------------------------------------------
	def expandToDepth(self,value):
		""""""
		self.edit(expandToDepth=value)
	#----------------------------------------------------------------------
	def favoritesCallback(self,value):
		""""""
		self.edit(favoritesCallback=value)
	#----------------------------------------------------------------------
	@property
	def itemScript(self):
		""""""
		return self.query(itemScript=True)
	#----------------------------------------------------------------------
	def selectPath(self,value):
		""""""
		self.edit(selectPath=value)
########################################################################
class TreeView(UI_Object.UI):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, name=None, **kwargs):
		parent = None
		if kwargs.has_key("qtParent"):
			parent = kwargs.pop("qtParent")
			
		if name == None:
			name = cmds.treeView(**kwargs)
			super(TreeView, self).__init__(name, **dict(qtParent=parent))
			
		else:
			if cmds.treeView(name, exists=True):
				super(TreeView, self).__init__(name)
			else:
				name = cmds.treeView(name, **kwargs)
				super(TreeView, self).__init__(name, **dict(qtParent=parent))
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
	def labelBackgroundColor(self,value):
		""""""
		self.edit(labelBackgroundColor=value)
	#----------------------------------------------------------------------
	def get_allowDragAndDrop(self):
		""""""
		return self.query(allowDragAndDrop=True)
	#----------------------------------------------------------------------
	def set_allowDragAndDrop(self, value):
		""""""
		self.edit(allowDragAndDrop=value)
	#----------------------------------------------------------------------
	allowDragAndDrop = property(get_allowDragAndDrop, set_allowDragAndDrop)
	#----------------------------------------------------------------------
	def get_allowMultiSelection(self):
		""""""
		return self.query(allowMultiSelection=True)
	#----------------------------------------------------------------------
	def set_allowMultiSelection(self, value):
		""""""
		self.edit(allowMultiSelection=value)
	#----------------------------------------------------------------------
	allowMultiSelection = property(get_allowMultiSelection, set_allowMultiSelection)
	#----------------------------------------------------------------------
	def get_allowReparenting(self):
		""""""
		return self.query(allowReparenting=True)
	#----------------------------------------------------------------------
	def set_allowReparenting(self, value):
		""""""
		self.edit(allowReparenting=value)
	#----------------------------------------------------------------------
	allowReparenting = property(get_allowReparenting, set_allowReparenting)
	#----------------------------------------------------------------------
	def displayLabel(self,value):
		""""""
		self.edit(displayLabel=value)
	#----------------------------------------------------------------------
	def displayLabelSuffix(self,value):
		""""""
		self.edit(displayLabelSuffix=value)
	#----------------------------------------------------------------------
	def hideButtons(self,value):
		""""""
		self.edit(hideButtons=value)
	#----------------------------------------------------------------------
	def editLabelCommand(self,value):
		""""""
		self.edit(editLabelCommand=value)
	#----------------------------------------------------------------------
	def itemRenamedCommand(self,value):
		""""""
		self.edit(itemRenamedCommand=value)
	#----------------------------------------------------------------------
	def itemDblClickCommand(self,value):
		""""""
		self.edit(itemDblClickCommand=value)
	#----------------------------------------------------------------------
	def selectCommand(self,value):
		""""""
		self.edit(selectCommand=value)
	#----------------------------------------------------------------------
	def selectionChangedCommand(self,value):
		""""""
		self.edit(selectionChangedCommand=value)
	#----------------------------------------------------------------------
	def contextMenuCommand(self,value):
		""""""
		self.edit(contextMenuCommand=value)
	#----------------------------------------------------------------------
	@property
	def isItemExpanded(self):
		""""""
		return self.query(isItemExpanded=True)
	#----------------------------------------------------------------------
	def numberOfButtons(self,value):
		""""""
		self.edit(numberOfButtons=value)
	#----------------------------------------------------------------------
	def enableLabel(self,value):
		""""""
		self.edit(enableLabel=value)
	#----------------------------------------------------------------------
	def enableKeys(self,value):
		""""""
		self.edit(enableKeys=value)
	#----------------------------------------------------------------------
	@property
	def itemExists(self):
		""""""
		return self.query(itemExists=True)
	#----------------------------------------------------------------------
	@property
	def itemSelected(self):
		""""""
		return self.query(itemSelected=True)
	#----------------------------------------------------------------------
	@property
	def itemIndex(self):
		""""""
		return self.query(itemIndex=True)
	#----------------------------------------------------------------------
	@property
	def itemParent(self):
		""""""
		return self.query(itemParent=True)
	#----------------------------------------------------------------------
	def get_itemAnnotation(self):
		""""""
		return self.query(itemAnnotation=True)
	#----------------------------------------------------------------------
	def set_itemAnnotation(self, value):
		""""""
		self.edit(itemAnnotation=value)
	#----------------------------------------------------------------------
	itemAnnotation = property(get_itemAnnotation, set_itemAnnotation)
	#----------------------------------------------------------------------
	def enableButton(self,value):
		""""""
		self.edit(enableButton=value)
	#----------------------------------------------------------------------
	def ignoreButtonClick(self,value):
		""""""
		self.edit(ignoreButtonClick=value)
	#----------------------------------------------------------------------
	def buttonTooltip(self,value):
		""""""
		self.edit(buttonTooltip=value)
	#----------------------------------------------------------------------
	def buttonTextIcon(self,value):
		""""""
		self.edit(buttonTextIcon=value)
	#----------------------------------------------------------------------
	def image(self,value):
		""""""
		self.edit(image=value)
	#----------------------------------------------------------------------
	def buttonStyle(self,value):
		""""""
		self.edit(buttonStyle=value)
	#----------------------------------------------------------------------
	def buttonState(self,value):
		""""""
		self.edit(buttonState=value)
	#----------------------------------------------------------------------
	def attachButtonRight(self,value):
		""""""
		self.edit(attachButtonRight=value)
	#----------------------------------------------------------------------
	def expandCollapseCommand(self,value):
		""""""
		self.edit(expandCollapseCommand=value)
	#----------------------------------------------------------------------
	def dragAndDropCommand(self,value):
		""""""
		self.edit(dragAndDropCommand=value)
	#----------------------------------------------------------------------
	def textColor(self,value):
		""""""
		self.edit(textColor=value)
	#----------------------------------------------------------------------
	def get_selectItem(self):
		""""""
		return self.query(selectItem=True)
	#----------------------------------------------------------------------
	def set_selectItem(self, value):
		""""""
		self.edit(selectItem=value)
	#----------------------------------------------------------------------
	selectItem = property(get_selectItem, set_selectItem)
	#----------------------------------------------------------------------
	def clearSelection(self,value):
		""""""
		self.edit(clearSelection=value)
	#----------------------------------------------------------------------
	def get_selectionColor(self):
		""""""
		return self.query(selectionColor=True)
	#----------------------------------------------------------------------
	def set_selectionColor(self, value):
		""""""
		self.edit(selectionColor=value)
	#----------------------------------------------------------------------
	selectionColor = property(get_selectionColor, set_selectionColor)
	#----------------------------------------------------------------------
	@property
	def item(self):
		""""""
		return self.query(item=True)
	#----------------------------------------------------------------------
	def highlite(self,value):
		""""""
		self.edit(highlite=value)
	#----------------------------------------------------------------------
	def highliteColor(self,value):
		""""""
		self.edit(highliteColor=value)
	#----------------------------------------------------------------------
	def addItem(self,value):
		""""""
		self.edit(addItem=value)
	#----------------------------------------------------------------------
	def removeAll(self,value):
		""""""
		self.edit(removeAll=value)
	#----------------------------------------------------------------------
	def expandItem(self,value):
		""""""
		self.edit(expandItem=value)
	#----------------------------------------------------------------------
	def borderHighlite(self,value):
		""""""
		self.edit(borderHighlite=value)
	#----------------------------------------------------------------------
	def borderHighliteColor(self,value):
		""""""
		self.edit(borderHighliteColor=value)
	#----------------------------------------------------------------------
	def ornament(self,value):
		""""""
		self.edit(ornament=value)
	#----------------------------------------------------------------------
	def ornamentColor(self,value):
		""""""
		self.edit(ornamentColor=value)
	#----------------------------------------------------------------------
	def reverseTreeOrder(self,value):
		""""""
		self.edit(reverseTreeOrder=value)
	#----------------------------------------------------------------------
	def fontFace(self,value):
		""""""
		self.edit(fontFace=value)
	#----------------------------------------------------------------------
	def get_itemVisible(self):
		""""""
		return self.query(itemVisible=True)
	#----------------------------------------------------------------------
	def set_itemVisible(self, value):
		""""""
		self.edit(itemVisible=value)
	#----------------------------------------------------------------------
	itemVisible = property(get_itemVisible, set_itemVisible)
	#----------------------------------------------------------------------
	def buttonTransparencyOverride(self,value):
		""""""
		self.edit(buttonTransparencyOverride=value)
	#----------------------------------------------------------------------
	def buttonTransparencyColor(self,value):
		""""""
		self.edit(buttonTransparencyColor=value)
	#----------------------------------------------------------------------
	def pressCommand(self,value):
		""""""
		self.edit(pressCommand=value)
	#----------------------------------------------------------------------
	def rightPressCommand(self,value):
		""""""
		self.edit(rightPressCommand=value)
	#----------------------------------------------------------------------
	@property
	def children(self):
		""""""
		return self.query(children=True)
	#----------------------------------------------------------------------
	@property
	def isLeaf(self):
		""""""
		return self.query(isLeaf=True)
	#----------------------------------------------------------------------
	def showItem(self,value):
		""""""
		self.edit(showItem=value)
	#----------------------------------------------------------------------
	def get_allowHiddenParents(self):
		""""""
		return self.query(allowHiddenParents=True)
	#----------------------------------------------------------------------
	def set_allowHiddenParents(self, value):
		""""""
		self.edit(allowHiddenParents=value)
	#----------------------------------------------------------------------
	allowHiddenParents = property(get_allowHiddenParents, set_allowHiddenParents)
	#----------------------------------------------------------------------
	def get_buttonErase(self):
		""""""
		return self.query(buttonErase=True)
	#----------------------------------------------------------------------
	def set_buttonErase(self, value):
		""""""
		self.edit(buttonErase=value)
	#----------------------------------------------------------------------
	buttonErase = property(get_buttonErase, set_buttonErase)
