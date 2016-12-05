import os
import QT.UI.UI_Compiler
import  wingdbstub
QT.UI.UI_Compiler.build_ui_files(os.path.dirname(__file__), os.path.join(os.path.dirname(__file__),"Compiled_UIs"))
