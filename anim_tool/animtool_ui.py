from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(long(ptr), QtWidgets.QWidget)


class AnimToolsUI(QtWidgets.QWidget):
	def __init__(self):
		super(AnimToolsUI, self).__init__()
		# CAVEAT : Parent ui to the application through which the ui is being created
		self.setParent(ptr_instance)
		self.setWindowFlags(QtCore.Qt.Window)

		# CAVEAT : Playblast group_box
		self.animtool_playblast_groupbox = QtWidgets.QGroupBox("Playblast")

		# CAVEAT : Browser
		self.animtool_playblast_groupbox_path_qlineedit = QtWidgets.QLineEdit()
		self.animtool_playblast_groupbox_browse_qpushbutton = QtWidgets.QPushButton("Browse")

		# CAVEAT : Viewport Mode List
		self.animtool_playblast_groupbox_vp_combobox = QtWidgets.QComboBox()
		self.animtool_playblast_groupbox_vp_2_combobox = self.animtool_playblast_groupbox_vp_combobox.addItem(
			"Viewport 2.0")
		self.animtool_playblast_groupbox_vp_2_combobox = self.animtool_playblast_groupbox_vp_combobox.addItem(
			"Legacy Default Viewport")
		self.animtool_playblast_groupbox_vp_2_combobox = self.animtool_playblast_groupbox_vp_combobox.addItem(
			"Legacy High Quality Viewport")
		self.animtool_playblast_groupbox_playblast_qpushbutton = QtWidgets.QPushButton("Playblast")

		# CAVEAT : Layout for the multiple widgets
		self.animtool_grid_layout = QtWidgets.QGridLayout()
		self.animtool_playblast_groupbox_horizontal_layout = QtWidgets.QHBoxLayout()
		self.animtool_playblast_groupbox_box_layout = QtWidgets.QBoxLayout(
			QtWidgets.QBoxLayout.Direction(QtWidgets.QBoxLayout.TopToBottom))

		# CAVEAT : Adding widget to layouts
		self.animtool_grid_layout.addWidget(self.animtool_playblast_groupbox)
		self.animtool_playblast_groupbox.setLayout(self.animtool_playblast_groupbox_box_layout)

		self.animtool_playblast_groupbox_horizontal_layout.addWidget(self.animtool_playblast_groupbox_path_qlineedit)
		self.animtool_playblast_groupbox_horizontal_layout.addWidget(
			self.animtool_playblast_groupbox_browse_qpushbutton)

		self.animtool_playblast_groupbox_box_layout.addLayout(self.animtool_playblast_groupbox_horizontal_layout)
		self.animtool_playblast_groupbox_box_layout.addWidget(self.animtool_playblast_groupbox_vp_combobox)
		self.animtool_playblast_groupbox_box_layout.addWidget(self.animtool_playblast_groupbox_playblast_qpushbutton)

		self.animtool_grid_layout.addLayout(self.animtool_playblast_groupbox_box_layout, 1, 1)
		self.setLayout(self.animtool_grid_layout)

		self.setWindowTitle("AnimTools")
		self.setFixedSize(300, 130)


if __name__ == "__main__":
	print "This is my main function"
	window = AnimToolsUI()
	window.show()
