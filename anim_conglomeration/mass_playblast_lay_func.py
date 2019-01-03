from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

import sys

path_anim_tools = "E:\\Proj_Codes\\NitinProj\\anim_conglomeration\\"
if not path_anim_tools in sys.path:
    sys.path.append(path_anim_tools)
import anim_conglomeration_ui

class MassPlayblastLayFunc(anim_conglomeration_ui.AnimConglomerationUI):
    def __init__(self):
        super(MassPlayblastLayFunc, self).__init__()

        self.animcog_mpb_browse_qpushbutton.clicked.connect(self.animcog_mpb_browse_button_func)

    def animcog_mpb_browse_button_func(self):
        cmds.fileDialog2(dialogStyle=2)
#
# if __name__ == "__main__":
#     print "This is my Main Class"
# else:
#     print "This is MassPlayblastLayFunc"


# import sys
# path_anim_tools = "E:\\Proj_Codes\\NitinProj\\anim_conglomeration\\"
# if not path_anim_tools in sys.path:
# 	sys.path.append(path_anim_tools)
# import mass_playblast_lay_func
# reload(mass_playblast_lay_func)
# anicog_win = mass_playblast_lay_func.MassPlayblastLayFunc()
# anicog_win.show()