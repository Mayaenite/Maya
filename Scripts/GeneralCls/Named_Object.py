class Named_Object(object):
	"""This Class Is A Base Class That Holds The A Memeory Pointer to a node
	it can be sent to maya.cmds as itself and acts like a string useing the pointers name to repesent itself
	"""
	#----------------------------------------------------------------------
	def __init__(self,name):
		self._name = name
	#----------------------------------------------------------------------
	def __str__(self):
		return self.name
	#----------------------------------------------------------------------
	def __repr__(self):
		return self.name
	#----------------------------------------------------------------------
	def __hash__(self):
		return hash(self.name)
	#----------------------------------------------------------------------
	def __eq__(self, other):
		return str(self.name) == str(other)
	#----------------------------------------------------------------------
	def __ne__(self, other):
		return str(self.name) != str(other)
	#----------------------------------------------------------------------
	def __get_name(self):
		return str(self._name)
	#----------------------------------------------------------------------
	name          = property(fget=__get_name)