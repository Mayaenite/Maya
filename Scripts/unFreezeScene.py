#!/usr/bin/env python
from maya import cmds
from itertools import count
import Scripts.OpenMaya_Util_API
MNODE = Scripts.OpenMaya_Util_API.Maya_Node
Maya_Node = Scripts.OpenMaya_Util_API.Maya_Node
strings_to_MNODES = Scripts.OpenMaya_Util_API.strings_to_Maya_Nodes
strings_to_Maya_Nodes = Scripts.OpenMaya_Util_API.strings_to_Maya_Nodes
import Scripts.General_Maya_Util
import time
import logging
import os
_LOG_FILE   = "Custom_Log"
_LOG_FOLDER = os.path.join(os.path.dirname(__file__),"Custom_Logs")
_LOG_NUMBER = count(0)

########################################################################
class Custom_Formatter(logging.Formatter):
	def __init__(self, fmt=None, datefmt=None):
		logging.Formatter.__init__(self,fmt=fmt, datefmt=datefmt)
		self._fmt_v1  = str("%(message)s")
		
	def post_formate(self,record):
		message = record.getMessage()
		self._fmt = self._fmt_v1
		
	def format(self, record):
		self.post_formate(record)
		return logging.Formatter.format(self,record)

########################################################################
class Custom_Logger(logging.Logger):
	""""""
	def __init__(self,name=None,level=logging.DEBUG,log_file=None,file_mode="w"):
		if name == None:
			name = "%s_%i" % (_LOG_FILE,_LOG_NUMBER.next())
		logging.Logger.__init__(self,name)
		self.setLevel(level)

		if log_file == None:
			
			if not os.path.exists(_LOG_FOLDER):
				os.makedirs(_LOG_FOLDER)
				print _LOG_FOLDER
			file_name = "%s.text" % name
			
			log_file = os.path.join(_LOG_FOLDER,file_name)
		
		# create formatter
		self._yaml_formatter = Custom_Formatter()
		
		# create file handler
		self._yaml_stream_handler = logging.StreamHandler()
		self._yaml_file_handler = logging.FileHandler(log_file,mode=file_mode)
		#self._yaml_buffer_handler = logging.handlers.BufferingHandler(5)
		self._yaml_file_handler.setLevel(level)
		self._yaml_stream_handler.setLevel(level)
		#self._yaml_buffer_handler.setLevel(level)
	
		# add formatter to file_handler
		self._yaml_file_handler.setFormatter(self._yaml_formatter)
		self._yaml_stream_handler.setFormatter(self._yaml_formatter)
		#self._yaml_buffer_handler.setFormatter(self._yaml_formatter)

		# add file_handler to logger
		self.addHandler(self._yaml_file_handler)
		self.addHandler(self._yaml_stream_handler)
		#self.addHandler(self._yaml_buffer_handler)
	@property
	def baseFileName(self):
		return self._yaml_file_handler.baseFilename

log = Custom_Logger()



def get_TopLevel_PolyTransforms():
	selList =  cmds.selectedNodes()

	cmds.select( cmds.ls(cmds.ls(assemblies=True,long=True),v=True,long=True) )
	cams = cmds.listRelatives(cmds.ls( ca=True,long=True), parent=True, fullPath=True, type="transform")
	cmds.select( cams, deselect=True)

	assemblies =  strings_to_Maya_Nodes(cmds.selectedNodes())

	for item in assemblies:
		if item.numberOfChildern:
			firstChild = item.children[0]
			if not firstChild.objectType in ['transform'] and not item.get_parent() == False:
				cmds.select(item,deselect=True)
	res = strings_to_Maya_Nodes(cmds.selectedNodes())

	if selList:
		cmds.select(selList)
	else:
		cmds.select(clear=True)

	return res

def correct_mirros_and_Flips(node):

	x = node.Make_Plug("scaleX")
	y = node.Make_Plug("scaleY")
	z = node.Make_Plug("scaleZ")
	if z.value<0:
		cmds.xform(node,cp=True)

		cmds.scale(1,1,-1,node.name+".vtx[*]",ls=True,r=True,ocp=True)
		z.value = 1
		cmds.makeIdentity(node,apply=True,t=True,r=True,s=True,n=False)

		cmds.scale(-1,1,1,node.name+".vtx[*]",ls=True,r=True,ocp=True)
		x.value = -1
		cmds.makeIdentity(node,apply=True,t=True,r=True,s=True,n=False)

		cmds.scale(1,-1,1,node.name+".vtx[*]",ls=True,r=True,ocp=True)
		y.value = -1
		cmds.makeIdentity(node,apply=True,t=True,r=False,s=False,n=False)

		cmds.polyNormal(node,constructionHistory=False,normalMode=04)




def unfreezeTransform(node):
	isinstance(node,MNODE)
	pivs = cmds.xform(node,q=True,rp=True)
	org_tr_pos = node.create_Float3("Original_Translate_Pos")
	org_tr_pos.value = pivs
	unlock_and_break_Attr_connections(node)
	childern, Parent = Extract_Node_From_Hiarkey(node)
	cmds.xform(node,cp=True)
	cmds.makeIdentity(node,apply=True,t=True,r=False,s=False,n=False)
	cmds.move(0.0,0.0,0.0,node,rpr=True)
	cmds.refresh(f=True)

	Translate = [x * -1 for x in cmds.xform(node,q=True,ws=True,t=True)]
	cmds.refresh(f=True)
	cmds.makeIdentity(node,apply=True,t=True,r=False,s=False,n=False)
	cmds.xform(node,ws=True,t=(Translate[0], Translate[1], Translate[2]))
	cmds.refresh(f=True)
	Insert_Back_Into_Hiarkey(Parent, node, childern)
	cmds.xform(node,pivots=pivs)

def freezeTransform(node):
	unlock_and_break_Attr_connections(node)
	childern, Parent = Extract_Node_From_Hiarkey(node)
	cmds.makeIdentity(node,apply=True,t=True,r=True,s=False,n=False)
	Insert_Back_Into_Hiarkey(Parent, node, childern)


########################################################################
class Node_Freezer_Context(object):
	"""
	Context Manager for Unparenting And Reparenting Nodes
	"""
	_Tab_count = 0
	_created_items = []
	_hide_it_count = 0
	def __init__(self,node, progressBar):
		self.node     = node
		self.progressBar = progressBar
		self.PlaceHolders = Maya_Node("PlaceHolders_Container")
		isinstance(self.node, Maya_Node)
		isinstance(self.progressBar, Scripts.General_Maya_Util.ProgressBarContext)
		self.childern = self.node.child_transforms
		self.Parent   = self.node.get_parent()
		Node_Freezer_Context._created_items.append(self)
		
	def __enter__(self):
		#log.debug(str("\t"*self._Tab_count)+ "Entered %r Context" % self.node.nice_name)
		cmds.refresh(cv=True, force=True)
		Node_Freezer_Context._Tab_count += 1
		self.unlock_and_break_Attr_connections()
		self.spaceLocator = self.create_locator_Place_Holder()
		#if Node_Freezer_Context._Tab_count <= 3:
			##self.node.plug_access.visibility.value = True
			#self.node.select_hierarchy()
			#cmds.refresh(cv=True, force=True)
			#cmds.viewFit( 'persp', f=1, animate=1 )
			#cmds.select(clear=True)
			#cmds.refresh(cv=True, force=True)
		self.node.plug_access.visibility.value = False
		self.Extract_Node_From_Hiarkey()
		self.Scan_Children()
		
	def __exit__(self, exc_type, exc_value, traceback):
		self.node.plug_access.visibility.value = True
		cmds.refresh(cv=True, force=True)
		self.unfreezeTransform()
		cmds.refresh(cv=True, force=True)
		self.Insert_Back_Into_Hiarkey()
		cmds.refresh(cv=True, force=True)
		self.spaceLocator.delete()
		Node_Freezer_Context._Tab_count -= 1
		#log.debug(str("\t"*self._Tab_count) + "Exiting %r Context" % self.node.nice_name)
		if exc_type:
			log.exception('%s : %s'%(exc_type, exc_value))
		# If this was false, it would re-raise the exception when complete
		return True
	#----------------------------------------------------------------------
	def iter_Children(self):
		for child in self.childern:
			yield child
	
	#----------------------------------------------------------------------
	def Insert_Back_Into_Hiarkey(self):
		if self.Parent:
			#log.debug(str("\t"*self._Tab_count)+ "Reparenting '%s' To '%s'" % (self.node.nice_name, self.Parent.nice_name))
			cmds.parent(self.node,self.Parent)
			
		if self.childern:
			for child in self.childern:
				#log.debug(str("\t"*self._Tab_count)+ "Reparenting Child '%s' To '%s'" % (child.nice_name, self.node.nice_name))
				cmds.parent(child,self.node)
	
	#----------------------------------------------------------------------
	def Extract_Node_From_Hiarkey(self):
		if self.childern:
			for child in self.childern:
				child.plug_access.visibility.value = False
				#log.debug(str("\t"*self._Tab_count)+ "Un-parenting Child '%s' From '%s'" % (child.nice_name, self.node.nice_name))
			cmds.parent(self.childern,w=True)
	
		if self.Parent:
			#log.debug(str("\t"*self._Tab_count)+ "Un-Parenting '%s' From '%s'" % (self.node.nice_name, self.Parent.nice_name))
			cmds.parent(self.node,w=True)
			
	#----------------------------------------------------------------------
	def unlock_and_break_Attr_connections(self):
		for att in ["tx","ty","tz","rx","ry","rz","sx","sy","sz"]:
			plg = self.node.Make_Plug(att)
			plg.unlock
			plg.Disconnect_All_Inputs()
	#----------------------------------------------------------------------
	def makeIdentity_True(self):
		#log.debug(str("\t"*self._Tab_count)+ "Setting '%s' Identity True" % self.node.nice_name)
		cmds.makeIdentity(self.node,apply=True,t=True,r=True,s=True,n=False, pn=True)
	#----------------------------------------------------------------------
	def centerPivot(self):
		#log.debug(str("\t"*self._Tab_count)+ "Centering Pivot Of '%s'" % self.node.nice_name)
		cmds.xform(self.node,cp=True)
	
	#----------------------------------------------------------------------
	def create_locator_Place_Holder(self):
		#log.debug(str("\t"*self._Tab_count)+ "creating locator Place Holder for '%s'" % self.node.nice_name)
		loc  = cmds.createNode("transform",name=self.node.nice_name+"_PlaceHolder", parent=self.PlaceHolders)
		shp  = cmds.createNode("locator",parent=loc)
		cmds.delete(cmds.pointConstraint(self.node,loc,offset=[0,0,0],weight=1))
		cmds.setAttr(shp+".localScale",10,10,10)
		return Maya_Node(loc)
	
	#----------------------------------------------------------------------
	def unfreezeTransform(self):
		self.centerPivot()
		pivs = cmds.xform(self.node,q=True,rp=True)
		self.makeIdentity_True()
		cmds.move(0.0,0.0,0.0,self.node,rpr=True)
		cmds.refresh(cv=True, force=True)
		self.makeIdentity_True()
		self.Reposition_To_Locator()
	#----------------------------------------------------------------------
	def Reposition_To_Locator(self):
		Translate = self.spaceLocator.plug_access.translate.value
		cmds.xform(self.node,ws=True,t=(Translate[0], Translate[1], Translate[2]))
		cmds.refresh(cv=True, force=True)
	#----------------------------------------------------------------------
	def Scan_Children(self):
		if self.progressBar.isCanceled():
			print "task stoped"
			return
		else:
			progress = self.progressBar.getProgress()
			progress += 1
			self.progressBar.setProgress(progress)
		if not self.progressBar.isCanceled():
			for child in self.childern:
				if not self.progressBar.isCanceled():
					freezer = Node_Freezer_Context(child, self.progressBar)
					if not self.progressBar.isCanceled():
						with freezer:
							pass
						if Node_Freezer_Context._Tab_count <= 1:
							freezer.node.plug_access.visibility.value = False
							
def dagGraphScanner_Counter(node=None):
	isinstance(node, Maya_Node)
	count = 0
	if node is None:
		nodelist = get_TopLevel_PolyTransforms()
		for node in nodelist:
			items = cmds.listRelatives(node, allDescendents=True, path=True, type='transform')
			if not items == None:
				count += len(items)
			else:
				count += 1
	else:
		items = cmds.listRelatives(node, allDescendents=True, path=True, type='transform')
		if not items == None:
			count += len(items)
		else:
			count += 1
	return count

def dagGraphScanner(progressBar, node=None,inishalize=True,freezType=0):

	if node == None and inishalize:
		nodelist = get_TopLevel_PolyTransforms()
		for node in nodelist:
			dagGraphScanner(progressBar, node, False, freezType=freezType)

	else:
		if progressBar.isCanceled():
			print "task stoped"
			return
		else:
			progress = progressBar.getProgress()
			progress += 1
			progressBar.setProgress(progress)
		if not progressBar.isCanceled():
			progressBar.setText(node.nice_name)
			#cmds.cameraView(node.nice_name+"1",animate=5,e=True,camera="persp",setCamera=True)
			with Node_Freezer_Context(node) as freezer:
				for child in freezer.iter_Children():
					dagGraphScanner(progressBar, child, False, freezType=freezType)

def UnFreezeScene(start_object=None,freezType=1):
	if cmds.objExists("PlaceHolders_Container"):
		cmds.delete("PlaceHolders_Container")
	step  = 1
	count = dagGraphScanner_Counter(start_object)
	progressBar = Scripts.General_Maya_Util.ProgressBarContext(count)
	progressBar.setStep(1)
	if not cmds.objExists("PlaceHolders_Container"):
		cmds.select(clear=True)
		cmds.createNode("transform",name="PlaceHolders_Container")
		
	Node_Freezer_Context._created_items = []
	
	with progressBar:
		if start_object == None:
			nodelist = get_TopLevel_PolyTransforms()
			for node in nodelist:
				progress = progressBar.getProgress()
				progress += 1
				progressBar.setProgress(progress)
				freezer = Node_Freezer_Context(node, progressBar)
				with freezer:
					pass
		else:
			start_object = Maya_Node(start_object)
			progress = progressBar.getProgress()
			progress += 1
			progressBar.setProgress(progress)
			freezer = Node_Freezer_Context(start_object, progressBar)
			with freezer:
				pass
		if progressBar.isCanceled():
			cmds.undo()
		else:
			for context_node in Node_Freezer_Context._created_items:
				context_node.node.plug_access.visibility.value = True
			Node_Freezer_Context._created_items = []
			cmds.delete("PlaceHolders_Container")
#import Scripts.NodeTreeFns.unFreezeScene
#reload(Scripts.NodeTreeFns.unFreezeScene)
#Scripts.NodeTreeFns.unFreezeScene.UnFreezeScene()
