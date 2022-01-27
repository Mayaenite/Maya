#from exceptions import Exception

#--------------------------
# PyNode Exceptions
#--------------------------
########################################################################
class MayaObjectError(TypeError):
    _objectDescription = 'Object'
    def __init__(self, node=None):
        self.node = str(node)
    def __str__(self):
        msg = "Maya %s does not exist (or is not unique):" % (self._objectDescription)
        if self.node:
            msg += ": %r" % (self.node)
        return msg
########################################################################
class MayaNodeError(MayaObjectError):
    _objectDescription = 'Node'
########################################################################
class MayaAttributeError(MayaObjectError, AttributeError):
    _objectDescription = 'Attribute'
########################################################################
class MayaAttributeEnumError(MayaAttributeError):
    _objectDescription = 'Attribute Enum'
    def __init__(self, node=None, enum=None):
        super(MayaAttributeEnumError, self).__init__(node)
        self.enum = enum
    def __str__(self):
        msg = super(MayaAttributeEnumError, self).__str__()
        if self.enum:
            msg += " - %r" % (self.enum)
        return msg
########################################################################
class MayaComponentError(MayaAttributeError):
    _objectDescription = 'Component'
########################################################################
class MayaParticleAttributeError(MayaComponentError):
    _objectDescription = 'Per-Particle Attribute'
#----------------------------------------------------------------------
def _objectError(objectName):
    # TODO: better name parsing
    if '.' in objectName:
        return MayaAttributeError(objectName)
    return MayaNodeError(objectName)

########################################################################
class Error(Exception):
    """Base class for exceptions in this Package."""
    #----------------------------------------------------------------------
    def __str__(self):
        args    = ",".join([repr(arg) for arg in self.args])
        message = repr(self.message)
        return message + " :: " + args
    
########################################################################
class No_Input_Nothing_Selected_Error(Error):
    """Exception raised when an input node is not given and there is nothing selected."""
    #----------------------------------------------------------------------
    def __init__(self, function):
        fn_name = function.__name__
        self.message = fn_name + " was not giving an input node and there was nothing currently selected"
        
########################################################################
class Object_Does_Not_Exist_Error(Error):
    """Exception raised when an input node Does Not Exist Within The Maya Scene."""
    #----------------------------------------------------------------------
    def __init__(self, name):
        self.message = "the input node %r Does not Exist" % name
