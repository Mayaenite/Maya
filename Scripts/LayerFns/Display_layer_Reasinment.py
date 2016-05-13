import Scripts.NodeCls.M_Nodes
DisplayLayer = Scripts.NodeCls.M_Nodes.DisplayLayer
MNODE =  Scripts.NodeCls.M_Nodes.MNODE
strings_to_MNODES =  Scripts.NodeCls.M_Nodes.strings_to_MNODES
import Scripts.Global_Constants as GCNT
from maya import cmds


def Assine_Tranforms_To_Closet_Group_Display_Layer():
	# Scan Through All Root Level Tranform Nodes
	for root in GCNT.Nodes.assemblies():
		for item in root.allDescendents:
			if (item.transfromType!="group") and (item.objectType=="transform") and (item.assinedDisplayLayer=="defaultLayer"):
				for parent in item.allParents:
					if not parent.assinedDisplayLayer == "defaultLayer":
						dl = DisplayLayer(parent.assinedDisplayLayer)
						dl.addMembers(item, noRecurse=True)
						break

def Assine_Group_Tranforms_To_Default_Display_Layer():
	# Scan Through All Root Level Tranform Nodes
	items = []
	for root in GCNT.Nodes.assemblies():
		if (root.transfromType=="group") & (root.objectType == "transform") & (root.assinedDisplayLayer != "defaultLayer"):
			items.append(root)
		for item in root.allDescendents:
			if (item.transfromType=="group") & (item.objectType == "transform") & (item.assinedDisplayLayer != "defaultLayer"):
				items.append(item)
	DisplayLayer("defaultLayer").addMembers(items, noRecurse=True)
