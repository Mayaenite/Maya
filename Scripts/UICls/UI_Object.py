import maya.cmds as cmds
import Scripts.UIFns.Find_UI
import QT
class UI(object):
	"""This Class Is The Base Class That Holds The A Memeory Pointer to a UI Object"""
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		self._isWidgetless = False
		if self.cmd_name in ["hudButton", 'headsUpDisplay', "hudSlider", "hudSliderButton"]:
			self._isWidgetless = True
			self._last_know_name = name
		else:
			self._widget = Scripts.UIFns.Find_UI.toQtObject(name)
			short_name = name.split("|")[-1]
			if self._widget is not None:
				if not short_name == self._widget.objectName():
					for wig in self._widget.children():
						if wig.objectName() == short_name:
							self._widget = wig
							break
				self._last_know_name = self._widget.objectName()
			if self._widget == None:
				raise LookupError("Could Not Find A Valid GUI Object With The Name %s" % name)
			
			if kwargs.has_key("qtParent") and not str(kwargs.get("qt_parent")) == "None":
				qt_parent = kwargs.get("qtParent")
				if isinstance(qt_parent, UI):
					self._widget.setParent(qt_parent._widget)
				elif (qt_parent, QT.QtGui.QWidget):
					self._widget.setParent(qt_parent)

	#----------------------------------------------------------------------
	@property
	def widget(self):
		""""""
		if self._isWidgetless:
			return None
		try:
			return self._widget
		except RuntimeError:
			self._widget = Scripts.UIFns.Find_UI.toQtObject(self._last_know_name)
			return self._widget
	#----------------------------------------------------------------------
	@property
	def widget_children(self):
		""" """
		if not self._isWidgetless:
			return self._widget.children()
		return []
	#----------------------------------------------------------------------
	def get_Parent_Widget(self):
		""" """
		if self._isWidgetless:
			return None
		return self._widget.parentWidget()
	#----------------------------------------------------------------------
	def set_Parent_Widget(self, value):
		"""Set """
		if not self._isWidgetless:
			self._widget.setParent(value)
	#----------------------------------------------------------------------
	parent_widget = property(get_Parent_Widget, set_Parent_Widget)
	#----------------------------------------------------------------------
	def __str__(self):
		return self.name
	#----------------------------------------------------------------------
	def __repr__(self):
		return self.name
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.name)
	#----------------------------------------------------------------------
	def __eq__(self, other):
		return unicode(self.name) == unicode(other)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return unicode(self.name) != unicode(other)
	#----------------------------------------------------------------------
	def _get_name(self):
		if self._isWidgetless:
			return self._last_know_name
		else:
			try:
				return self._widget.objectName()
			except RuntimeError:
				self._widget = Scripts.UIFns.Find_UI.toQtObject(self._last_know_name)
				return self._widget.objectName()
			
	#----------------------------------------------------------------------
	def _set_name(self, value):
		self._last_know_name = value
		if not self._isWidgetless:
			self.widget.setObjectName(value)
	#----------------------------------------------------------------------
	name          = property(_get_name, _set_name)
	
	#----------------------------------------------------------------------
	@property
	def cmd_name(self):
		command_name = self.__class__.__name__
		command_name = command_name[0].lower() + command_name[1:]
		return command_name
	#----------------------------------------------------------------------
	@property
	def cmd(self):
		command_name = self.cmd_name
		return getattr(cmds, command_name)
	
	#----------------------------------------------------------------------
	def query(self, **kwargs):
		kwargs["query"] = True
		return self.cmd(self, **kwargs)
	
	#----------------------------------------------------------------------
	def edit(self, **kwargs):
		kwargs["edit"] = True
		return self.cmd(self, **kwargs)
