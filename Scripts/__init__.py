import sys
import os

def reload_Tools(nameSpace = "", moduleList = None):
	for mod in [m for m in sys.modules.keys() if m.startswith("Scripts")]:
		m = sys.modules[mod]
		if str(type(m)) == "<type 'module'>":
			if not "Script_Jobs" in m.__name__ or "QT_Tools" in  m.__name__:
				mod = str(reload(m))
				path= mod.split()[3][1:-2]
				name= mod.split()[1]
				if name is None:
					print "could not reload %s" % m.__name__
				elif not path.endswith("c"):
					print "reloaded %s" % name
