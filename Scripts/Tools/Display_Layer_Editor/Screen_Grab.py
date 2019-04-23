
import maya.OpenMayaUI as OpenMayaUI

#---------------------------------------------------------------------------------
def thumbnailApiFromView(filename, width, height, compression='jpg', modelPanel='modelPanel4'):
	'''
	grab the thumbnail direct from the buffer?
	TODO: not yet figured out how you crop the data here?
	'''
	#Grab the last active 3d viewport
	view = None
	if modelPanel is None:
		view = OpenMayaUI.M3dView.active3dView()
	else:
		try:
			view = OpenMayaUI.M3dView()
			OpenMayaUI.M3dView.getM3dViewFromModelEditor(modelPanel, view)
		except:
			#in case the given modelPanel doesn't exist!!
			view = OpenMayaUI.M3dView.active3dView()

	#read the color buffer from the view, and save the MImage to disk
	image = OpenMaya.MImage()
	view.readColorBuffer(image, True)
	image.resize(width, height, True)
	image.writeToFile(filename, compression)
