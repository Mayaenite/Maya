import maya.cmds as cmds
import Scripts.GeneralCls
Named_Object = Scripts.GeneralCls.Named_Object

class SelectionConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		if not cmds.selectionConnection(name,exists=True):
			name = cmds.selectionConnection(name, **kwargs)
		super(SelectionConnection, self).__init__(name)

	def __lshift__(self, other):
		cmds.selectionConnection(self.name,e=True,select=other)

	def __rshift__(self, other):
		cmds.selectionConnection(self.name,e=True,deselect=other)

	def get_objects(self):
		"""will return all the members of the selection connection (if the connection wraps a set, the set members will be returned)"""
		return cmds.selectionConnection(self.name,q=True,object=True)

	def select_objects(self):
		cmds.select(self.name)

	def clear(self):
		cmds.selectionConnection(self.name,e=True,clear=True)

	def add_connection(self,name):
		cmds.selectionConnection(name,e=True,addto=self.name)

	def remove_connection(self,name):
		cmds.selectionConnection(self.name,e=True,remove=name)

	def addScript(self,fn):
		cmds.selectionConnection(self.name,e=True,addScript=fn)

	def removeScript(self,fn):
		cmds.selectionConnection(self.name,e=True,removeScript=fn)

	def identify(self):
		return cmds.selectionConnection(self.name,q=True,identify=True)

	def add_objects(self,*objects):
		try:
			for item in objects:
				if isinstance(item,(list,tuple)):
					for obj in item:
						cmds.selectionConnection(self.name,e=True,select=obj)
				else:
					cmds.selectionConnection(self.name,e=True,select=item)
		except:
			cmds.selectionConnection(self.name,e=True,select=objects)

	def remove_objects(self,*objects):
		try:
			for item in objects:
				if isinstance(item,(list,tuple)):
					for obj in item:
						cmds.selectionConnection(self.name,e=True,deselect=obj)
				else:
					cmds.selectionConnection(self.name,e=True,deselect=item)
		except:
			cmds.selectionConnection(self.name,e=True,deselect=objects)

	def connect_to_editor_MainList(self,editor):
		cmds.editor( str(editor), edit=True, mainListConnection=self)
		
	def connect_to_editor_Selection(self,editor):
		cmds.editor( str(editor), edit=True, selectionConnection=self)
		
	def connect_to_editor_Highlight(self,editor):
		cmds.editor( str(editor), edit=True, highlightConnection=self)
		
	def delete(self):
		if cmds.selectionConnection(self._name,exists=True):
			cmds.deleteUI(self._name)
			
	def __delete__(self):
		self.delete()
		super(SelectionConnection,self).__delete__()


class ActiveListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["activeList"]=True
		super(ActiveListConnection, self).__init__(name,**kwargs)

class ModelListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["modelList"]=True
		super(ModelListConnection, self).__init__(name,**kwargs)

class KeyframeListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["keyframeList"]=True
		super(KeyframeListConnection, self).__init__(name,**kwargs)

class WorldListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["worldList"]=True
		super(WorldListConnection, self).__init__(name,**kwargs)

class ObjectListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["objectList"]=True
		super(ObjectListConnection, self).__init__(name,**kwargs)

class ListListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["listList"]=True
		super(ListListConnection, self).__init__(name,**kwargs)

class EditorListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["editorList"]=True
		super(EditorListConnection, self).__init__(name,**kwargs)

class SetListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["setList"]=True
		super(SetListConnection, self).__init__(name,**kwargs)

class CharacterListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["characterList"]=True
		super(CharacterListConnection, self).__init__(name,**kwargs)

class HighlightListConnection(Named_Object):
	#----------------------------------------------------------------------
	def __init__(self,name, **kwargs):
		kwargs["highlightList"]=True
		super(HighlightListConnection, self).__init__(name,**kwargs)
