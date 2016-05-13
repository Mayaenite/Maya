from Scripts.NodeCls import OpenMaya_Objects
from Singleton import Singleton
from Scripts.UIFns import Find_UI
from PyQt4 import QtCore

class Display_Layer_Manager(QtCore.QObject):
	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		super(Display_Layer_Manager,self).__init__(parent=None)
		self."layerManager.currentDisplayLayer"
		self.QtSingles = Display_Layer_Singles()
		self.message = self.Make_Plug("message")
		self.currentDisplayLayer = self.Make_Plug("currentDisplayLayer")
		self.displayLayerId = self.Make_Plug("displayLayerId")



class Render_Layer_Manager(OpenMaya_Objects.MNODE):
	__metaclass__ = Singleton

	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		super(Render_Layer_Manager,self).__init__("renderLayerManager")
		self.message = self.plug_access.message
		self.isHistoricallyInteresting
		self.nodeState
		self.binMembership
		self.currentDisplayLayer = self.plug_access.currentDisplayLayer
		self.displayLayerId = self.plug_access.currentDisplayLayer
