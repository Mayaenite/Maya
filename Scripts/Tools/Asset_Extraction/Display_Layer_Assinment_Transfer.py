from maya import cmds
from Scripts.NodeCls.DisplayLayer import DisplayLayer
import pymel.core as pm
import os,sys,pickle


class Display_Layer_Assinment_Transfer(object):
	def __init__(self):
		self.dl_name_dict   = {}
		self.dl_obj_id_dict = {}
		self._assinment_logs = []
		self._skiped_assinment_logs = []

	def dump_data(self):
		pkl_file_name = os.path.join(os.environ["TMPDIR"],"dl_assinments.pkl")
		with file(pkl_file_name,"w") as f:
			pickle.dump(self.dl_name_dict,f)
			pickle.dump(self.dl_obj_id_dict,f)

	def load_data(self):
		pkl_file_name = os.path.join(os.environ["TMPDIR"],"dl_assinments.pkl")
		with file(pkl_file_name,"r") as f:
			self.dl_name_dict   = pickle.load(f)
			self.dl_obj_id_dict = pickle.load(f)

	def assine_display_layers(self):
		for item in pm.ls(type="displayLayer"):
			#if not str(item) == 'defaultLayer':
			if 'layerManager' in [str(in_put_node) for in_put_node in item.inputs()]:
				dl = DisplayLayer(str(item))
				self.dl_name_dict[dl.nice_name]=dl.member_names
				self.dl_obj_id_dict[dl.nice_name]=[]
				for member in dl.members:
					if member.attributeExists("objectID"):
						idnum = cmds.getAttr(member.name+".objectID")
						self.dl_obj_id_dict[dl.nice_name].append(idnum)
		self.dump_data()
	def reassine_display_layers(self):
		self._assinment_logs = []
		self._skiped_assinment_logs = []
		self.load_data()
		for layer in self.dl_name_dict.keys():
			if not cmds.objExists(layer):
				print layer
			else:
				dl = DisplayLayer(layer)
				for obj in self.dl_name_dict[layer]:
					if not cmds.objExists(obj):
						log =  "skipping '%s' because it does not exist and " % obj.split("|")[-1]
						self._skiped_assinment_logs.append(log)

					else:
						dl.addMembers(obj, noRecurse=True)
						log = "Assined '%s' To Display Layer '%s' " % (obj.split("|")[-1],layer)
						self._assinment_logs.append(log)
