# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\drew.loveridge\Documents\maya\scripts\AW_Systems_Code\Software\Maya\Scripts\Tools\Vray_Scene_States_Manager/UI\Warning_Message.ui'
#
# Created: Fri Mar 29 11:07:41 2019
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(1198, 820)
		self.verticalLayout = QtGui.QVBoxLayout(Dialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtGui.QLabel(Dialog)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		self.label.setMinimumSize(QtCore.QSize(521, 771))
		self.label.setMaximumSize(QtCore.QSize(521, 771))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("//isln-smb/aw_config/Git_Live_Code/Software/Maya/icons/Smokey_Bear.jpg"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.textEdit = QtGui.QTextEdit(Dialog)
		self.textEdit.setEnabled(True)
		self.textEdit.setMinimumSize(QtCore.QSize(651, 751))
		self.textEdit.setMaximumSize(QtCore.QSize(651, 751))
		self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.textEdit.setReadOnly(True)
		self.textEdit.setObjectName("textEdit")
		self.horizontalLayout.addWidget(self.textEdit)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setCenterButtons(True)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#ff0000;\">WARNING: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#00ff00;\">AFTER SYSTEM TRANSFER</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#00ff00;\">YOU WILL HAVE TO CHECK EACH RENDER LAYER</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#00ff00;\">FOR INCORRECT STATE ASSIGNMENT</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())

