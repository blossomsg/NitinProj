from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(long(ptr), QtWidgets.QWidget)


class AnimCompactUI(QtWidgets.QWidget):
	def __init__(self):
		super(AnimCompactUI, self).__init__()
		# CAVEAT : Parent ui to the application through which the ui is being created
		self.setParent(ptr_instance)
		self.setWindowFlags(QtCore.Qt.Window)

		# CAVEAT : Playblast Toolbox
		self.animcomp_toolbox = QtWidgets.QToolBox("Anim_Compact")
		self.animcomp_toolbox_palyblast_column = QtWidgets.QWidget("PlayblastWid")
		self.animcomp_toolbox_comingsoon_column = QtWidgets.QWidget("ComingSoonWid")

		# CAVEAT : Default Vp settings

		# CAVEAT : Browser
		self.animcomp_toolbox_path_qlineedit = QtWidgets.QLineEdit()
		self.animcomp_toolbox_browse_qpushbutton = QtWidgets.QPushButton("Browse")

		# CAVEAT : Viewport Mode List
		self.animcomp_compactbox_vp_combobox = QtWidgets.QComboBox()
		self.animcomp_toolbox_vp_2_combobox = self.animcomp_toolbox_vp_combobox.addItem(
			"Viewport 2.0")
		self.animcomp_toolbox_ldvp_combobox = self.animcomp_toolbox_vp_combobox.addItem(
			"Legacy Default Viewport")
		self.animcomp_toolbox_lhqvp_combobox = self.animcomp_toolbox_vp_combobox.addItem(
			"Legacy High Quality Viewport")
		self.animcomp_toolbox_playblast_qpushbutton = QtWidgets.QPushButton("Playblast")

		# CAVEAT : Layout for the multiple widgets
		self.animcomp_grid_layout = QtWidgets.QGridLayout()
		self.animcomp_toolbox_horizontal_layout = QtWidgets.QHBoxLayout()
		# self.animcomp_playblast_toolbox_box_layout = QtWidgets.QBoxLayout(
		# 	QtWidgets.QBoxLayout.Direction(QtWidgets.QBoxLayout.TopToBottom))

		# CAVEAT : Adding widget to layouts/ Connections
		self.animcomp_toolbox.addItem(self.animcomp_toolbox_palyblast_column, "Playblast")
		self.animcomp_toolbox.addItem(self.animcomp_toolbox_comingsoon_column, "ComingSoon")

		self.animcomp_grid_layout.addWidget(self.animcomp_toolbox)
		# self.animcomp_playblast_toolbox.setLayout(self.animcomp_playblast_toolbox_box_layout)
		#
		# self.animcomp_playblast_toolbox_horizontal_layout.addWidget(self.animcomp_playblast_toolbox_path_qlineedit)
		# self.animcomp_playblast_toolbox_horizontal_layout.addWidget(
		# 	self.animcomp_playblast_toolbox_browse_qpushbutton)
		#
		# self.animcomp_playblast_toolbox_box_layout.addLayout(self.animcomp_playblast_toolbox_horizontal_layout)
		# self.animcomp_playblast_toolbox_box_layout.addWidget(self.animcomp_playblast_toolbox_vp_combobox)
		# self.animcomp_playblast_toolbox_box_layout.addWidget(self.animcomp_playblast_toolbox_playblast_qpushbutton)
		#
		# self.animcomp_grid_layout.addLayout(self.animcomp_playblast_toolbox_box_layout, 1, 1)
		self.setLayout(self.animcomp_grid_layout)

		self.setWindowTitle("AnimCompact")
		self.setFixedSize(300, 130)


if __name__ == "__main__":
	print "This is my main function"
	window = AnimCompactUI()
	window.show()




# from PySide2 import QtWidgets
# from PySide2 import QtGui
# from PySide2 import QtCore
#
# lay = QtWidgets.QVBoxLayout()
# wind_for_lay = QtWidgets.QWidget()
# toolbox_wid = QtWidgets.QToolBox()
# tile_tab_01 = QtWidgets.QWidget()
# tile_tab_02 = QtWidgets.QWidget()
#
#
# test_tile_01 = toolbox_wid.addItem(tile_tab_01, "this is a test")
# test_tile_02 = toolbox_wid.addItem(tile_tab_02, "this is second test")
# lay.addWidget(toolbox_wid)
# wind_for_lay.setLayout(lay)
#
# win = wind_for_lay
# win.show()