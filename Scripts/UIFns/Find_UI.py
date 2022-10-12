
import QT
import maya.OpenMayaUI as apiUI

def getMayaWindow():
	"""
	Get the main Maya window as a QT.QMainWindow instance
	@return: QT.QMainWindow instance of the top level Maya windows
	"""
	ptr = apiUI.MQtUtil.mainWindow()
	if ptr is not None:
		try:
			return QT.wraperfn(long(ptr), QT.QWidget)
		except:
			return QT.wraperfn(int(ptr), QT.QWidget)

def toQtObject(mayaName):
	"""
	Convert a Maya ui path to a Qt object
	@param mayaName: Maya UI Path to convert (Ex: "scriptEditorPanel1Window|TearOffPane|scriptEditorPanel1|testButton" )
	@return: PyQt representation of that object
	"""
	res = None
	ptr = apiUI.MQtUtil.findControl(mayaName)
	if ptr is None:
		ptr = apiUI.MQtUtil.findLayout(mayaName)
	if ptr is None:
		ptr = apiUI.MQtUtil.findMenuItem(mayaName)
	if ptr is not None:
		try:
			res = QT.wraperfn(long(ptr), QT.QWidget)
		except:
			res = QT.wraperfn(int(ptr), QT.QWidget)
	isinstance(res, QT.QWidget)
	return res
