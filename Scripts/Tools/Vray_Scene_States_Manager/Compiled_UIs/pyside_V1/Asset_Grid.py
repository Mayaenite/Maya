# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dloveridge\Documents\AW_Git_Repo\Maya\Scripts\Tools\Vray_Scene_States_Manager\Asset_Grid.ui'
#
# Created: Wed Jun 15 12:53:55 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(399, 77)
		self.gridLayout = QtGui.QGridLayout(Form)
		self.gridLayout.setObjectName("gridLayout")
		self.frame = QtGui.QFrame(Form)
		self.frame.setFrameShape(QtGui.QFrame.Box)
		self.frame.setFrameShadow(QtGui.QFrame.Plain)
		self.frame.setObjectName("frame")
		self.verticalLayout = QtGui.QVBoxLayout(self.frame)
		self.verticalLayout.setObjectName("verticalLayout")
		self.asset_name_label = QtGui.QLabel(self.frame)
		self.asset_name_label.setAlignment(QtCore.Qt.AlignCenter)
		self.asset_name_label.setObjectName("asset_name_label")
		self.verticalLayout.addWidget(self.asset_name_label)
		self.asset_states_comboBox = QtGui.QComboBox(self.frame)
		self.asset_states_comboBox.setObjectName("asset_states_comboBox")
		self.verticalLayout.addWidget(self.asset_states_comboBox)
		self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
		self.frame_2 = QtGui.QFrame(Form)
		self.frame_2.setFrameShape(QtGui.QFrame.Box)
		self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
		self.frame_2.setObjectName("frame_2")
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.asset_name_label_2 = QtGui.QLabel(self.frame_2)
		self.asset_name_label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.asset_name_label_2.setObjectName("asset_name_label_2")
		self.verticalLayout_2.addWidget(self.asset_name_label_2)
		self.asset_states_comboBox_2 = QtGui.QComboBox(self.frame_2)
		self.asset_states_comboBox_2.setObjectName("asset_states_comboBox_2")
		self.verticalLayout_2.addWidget(self.asset_states_comboBox_2)
		self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.asset_name_label.setText(QtGui.QApplication.translate("Form", "Asset Name", None, QtGui.QApplication.UnicodeUTF8))
		self.asset_name_label_2.setText(QtGui.QApplication.translate("Form", "Asset Name", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

