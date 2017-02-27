# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dloveridge\Documents\AW_Git_Repo\Maya\Scripts\Tools\Vray_Scene_States_Manager\Split_Frames.ui'
#
# Created: Wed Jun 15 12:53:55 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(400, 467)
		self.verticalLayout = QtGui.QVBoxLayout(Form)
		self.verticalLayout.setObjectName("verticalLayout")
		self.splitter = QtGui.QSplitter(Form)
		self.splitter.setOrientation(QtCore.Qt.Vertical)
		self.splitter.setObjectName("splitter")
		self.treeWidget = QtGui.QTreeWidget(self.splitter)
		self.treeWidget.setObjectName("treeWidget")
		self.treeWidget.headerItem().setText(0, "1")
		self.graphicsView = QtGui.QGraphicsView(self.splitter)
		self.graphicsView.setObjectName("graphicsView")
		self.verticalLayout.addWidget(self.splitter)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

