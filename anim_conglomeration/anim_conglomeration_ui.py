from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

import sys

path_anim_tools = "D:\\All_Projs\\NitinProj\\anim_conglomeration\\"
if not path_anim_tools in sys.path:
	sys.path.append(path_anim_tools)
import mass_playblast_lay

reload(mass_playblast_lay)

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(long(ptr), QtWidgets.QWidget)


class AnimConglomerationUI(mass_playblast_lay.MassPlayblastLay):
	def __init__(self):
		super(AnimConglomerationUI, self).__init__()
		# CAVEAT : Parent ui to the application through which the ui is being created
		self.setParent(ptr_instance)
		self.setWindowFlags(QtCore.Qt.Window)

		# CAVEAT : Playblast Toolbox
		self.animcomp_toolbox = QtWidgets.QToolBox()
		self.animcomp_toolbox_comingsoon_column = QtWidgets.QWidget()

		# CAVEAT : Layout for the Toolbox widgets
		self.animcomp_grid_layout = QtWidgets.QGridLayout()

		# CAVEAT : Adding widget to MassLayouts/ Connections
		self.animcomp_toolbox.addItem(self.animcomp_toolbox_palyblast_column, "Playblast")
		self.animcomp_toolbox.addItem(self.animcomp_toolbox_comingsoon_column, "ComingSoon")
		self.animcomp_grid_layout.addWidget(self.animcomp_toolbox)
		self.setLayout(self.animcomp_grid_layout)

		self.setWindowTitle("AnimCompact")
		# self.setFixedSize(300, 130)


if __name__ == "__main__":
	print "This is my main function"
	window = AnimConglomerationUI()
	window.show()
