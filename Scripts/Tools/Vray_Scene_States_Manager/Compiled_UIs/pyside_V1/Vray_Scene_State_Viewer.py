# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dloveridge\Documents\AW_Git_Repo\Maya\Scripts\Tools\Vray_Scene_States_Manager\Vray_Scene_State_Viewer.ui'
#
# Created: Wed Jun 15 12:53:57 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Vray_Scene_States_Viewer(object):
	def setupUi(self, Vray_Scene_States_Viewer):
		Vray_Scene_States_Viewer.setObjectName("Vray_Scene_States_Viewer")
		Vray_Scene_States_Viewer.resize(504, 646)
		self.centralwidget = QtGui.QWidget(Vray_Scene_States_Viewer)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.Update_Button = QtGui.QPushButton(self.centralwidget)
		self.Update_Button.setObjectName("Update_Button")
		self.verticalLayout_3.addWidget(self.Update_Button)
		self.rebuild_Render_layer_states_button = QtGui.QPushButton(self.centralwidget)
		self.rebuild_Render_layer_states_button.setObjectName("rebuild_Render_layer_states_button")
		self.verticalLayout_3.addWidget(self.rebuild_Render_layer_states_button)
		self.Asset_Grid_groupBox = QtGui.QGroupBox(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Asset_Grid_groupBox.sizePolicy().hasHeightForWidth())
		self.Asset_Grid_groupBox.setSizePolicy(sizePolicy)
		self.Asset_Grid_groupBox.setMinimumSize(QtCore.QSize(0, 100))
		self.Asset_Grid_groupBox.setObjectName("Asset_Grid_groupBox")
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.Asset_Grid_groupBox)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.Asset_Grid_widget = Asset_Grid(self.Asset_Grid_groupBox)
		self.Asset_Grid_widget.setBaseSize(QtCore.QSize(0, 100))
		self.Asset_Grid_widget.setObjectName("Asset_Grid_widget")
		self.verticalLayout_2.addWidget(self.Asset_Grid_widget)
		self.verticalLayout_3.addWidget(self.Asset_Grid_groupBox)
		self.entity_tree_view = Asset_Tree_View(self.centralwidget)
		self.entity_tree_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.entity_tree_view.setObjectName("entity_tree_view")
		self.verticalLayout_3.addWidget(self.entity_tree_view)
		Vray_Scene_States_Viewer.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(Vray_Scene_States_Viewer)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 26))
		self.menubar.setObjectName("menubar")
		Vray_Scene_States_Viewer.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(Vray_Scene_States_Viewer)
		self.statusbar.setObjectName("statusbar")
		Vray_Scene_States_Viewer.setStatusBar(self.statusbar)

		self.retranslateUi(Vray_Scene_States_Viewer)
		QtCore.QMetaObject.connectSlotsByName(Vray_Scene_States_Viewer)

	def retranslateUi(self, Vray_Scene_States_Viewer):
		Vray_Scene_States_Viewer.setWindowTitle(QtGui.QApplication.translate("Vray_Scene_States_Viewer", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
		self.Update_Button.setText(QtGui.QApplication.translate("Vray_Scene_States_Viewer", "Update To Version 2", None, QtGui.QApplication.UnicodeUTF8))
		self.rebuild_Render_layer_states_button.setText(QtGui.QApplication.translate("Vray_Scene_States_Viewer", "Rebuild Render Layer States", None, QtGui.QApplication.UnicodeUTF8))
		self.Asset_Grid_groupBox.setTitle(QtGui.QApplication.translate("Vray_Scene_States_Viewer", "Asset Grid", None, QtGui.QApplication.UnicodeUTF8))

from Scripts.Tools.Vray_Scene_States_Manager.Custom_Widgets import Asset_Grid, Asset_Tree_View

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Vray_Scene_States_Viewer = QtGui.QMainWindow()
	ui = Ui_Vray_Scene_States_Viewer()
	ui.setupUi(Vray_Scene_States_Viewer)
	Vray_Scene_States_Viewer.show()
	sys.exit(app.exec_())

