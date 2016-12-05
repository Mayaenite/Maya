import inspect, types, operator, sys, warnings
import itertools
class Singleton(type):
	""" Metaclass for Singleton classes.

	    >>> class DictSingleton(dict) :
	    ...    __metaclass__ = Singleton
	    ...
	    >>> DictSingleton({'A':1})
	    {'A': 1}
	    >>> a = DictSingleton()
	    >>> a
	    {'A': 1}
	    >>> b = DictSingleton({'B':2})
	    >>> a, b, DictSingleton()
	    ({'B': 2}, {'B': 2}, {'B': 2})
	    >>> a is b and a is DictSingleton()
	    True

	    >>> class StringSingleton(str) :
	    ...    __metaclass__ = Singleton
	    ...
	    >>> StringSingleton("first")
	    'first'
	    >>> a = StringSingleton()
	    >>> a
	    'first'
	    >>> b = StringSingleton("changed")
	    >>> a, b, StringSingleton()
	    ('first', 'first', 'first')
	    >>> a is b and a is StringSingleton()
	    True

	    >>> class DictSingleton2(DictSingleton):
	    ...     pass
	    ...
	    >>> DictSingleton2({'A':1})
	    {'A': 1}
	    >>> a = DictSingleton2()
	    >>> a
	    {'A': 1}
	    >>> b = DictSingleton2({'B':2})
	    >>> a, b, DictSingleton2()
	    ({'B': 2}, {'B': 2}, {'B': 2})
	    >>> a is b and a is DictSingleton2()
	    True

	"""
	def __new__(mcl, classname, bases, classdict):

		# newcls =  super(Singleton, mcl).__new__(mcl, classname, bases, classdict)

		# redefine __new__
		def __new__(cls, *p, **k):
			if '_the_instance' not in cls.__dict__:
				cls._the_instance = super(newcls, cls).__new__(cls, *p, **k)
			return cls._the_instance
		newdict = { '__new__': __new__}
		# define __init__ if it has not been defined in the class being created
		def __init__(self, *p, **k):
			cls = self.__class__
			if p :
				if hasattr(self, 'clear') :
					self.clear()
				else :
					super(newcls, self).__init__()
				super(newcls, self).__init__(*p, **k)
		if '__init__' not in classdict :
			newdict['__init__'] = __init__
		# Note: could have defined the __new__ method like it is done in Singleton but it's as easy to derive from it
		for k in classdict :
			if k in newdict :
				warnings.warn("Attribute %r is predefined in class %r of type %r and can't be overriden" % (k, classname, mcl.__name__))
			else :
				newdict[k] = classdict[k]

		newcls =  super(Singleton, mcl).__new__(mcl, classname, bases, newdict)

		return newcls


class Item_IDs_Singleton(dict):
	__metaclass__ = Singleton
	id_generator  = itertools.count(0)
	def add_item(self,name):
		idNumber = self.id_generator.new()
		item     = ID_Data(name, idNumber)
		self[idNumber]=item
		return item
	
ID_Tracker = Item_IDs_Singleton()
########################################################################
class ID_Data(object):
	""""""
	_Tracker = ID_Tracker
	def __init__(self,name,idNumber):
		self.name       = name
		self.idNumber   = idNumber
		self.references = []