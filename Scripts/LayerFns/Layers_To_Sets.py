__all__ = ["Display_Layers_To_Selection_Sets"]

import maya.cmds as cmds
import Scripts.NodeCls.M_Nodes

def Display_Layers_To_Selection_Sets(flatten_to_Shapes=False):
	current_selection = cmds.ls(sl=True)
	master_set = Scripts.NodeCls.M_Nodes.SelectionSet("Display_Layers_To_Selection_Sets")
	res = []
	# GET A LIST OF ALL THE DISPLAY LAYER NAMES
	display_layer_list = cmds.ls(type="displayLayer")
	# REMOVE THE DEFAULT LAYER
	display_layer_list.remove('defaultLayer')

	# ITERATE THROUGH EACH LAYER SELECT THE CONTENTS AND MAKE A SELECTION SET
	for item in display_layer_list:
		item = Scripts.NodeCls.M_Nodes.DisplayLayer(item)
		if item.members:
			cmds.select(item.members)
			cmds.select(cmds.listRelatives(allDescendents=True,type="mesh",path=True))
			cmds.select(cmds.listRelatives(parent=True,type="transform",path=True))
		part_layer_set = Scripts.NodeCls.M_Nodes.SelectionSet(item.name+"_DL")
		master_set >> part_layer_set
		res.append(part_layer_set)
	if current_selection:
		cmds.select(current_selection,replace=True)
	return res