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
		self.animcomp_toolbox = QtWidgets.QToolBox()
		self.animcomp_toolbox_palyblast_column = QtWidgets.QWidget()
		self.animcomp_toolbox_comingsoon_column = QtWidgets.QWidget()

		# CAVEAT : Default Vp settings

		# CAVEAT : Browser
		self.animcomp_path_qlineedit = QtWidgets.QLineEdit()
		self.animcomp_browse_qpushbutton = QtWidgets.QPushButton("Browse")

		# CAVEAT : Viewport Mode List
		self.animcomp_vp_combobox = QtWidgets.QComboBox()
		self.animcomp_vp_2_combobox = self.animcomp_vp_combobox.addItem(
			"Viewport 2.0")
		self.animcomp_ldvp_combobox = self.animcomp_vp_combobox.addItem(
			"Legacy Default Viewport")
		self.animcomp_lhqvp_combobox = self.animcomp_vp_combobox.addItem(
			"Legacy High Quality Viewport")
		self.animcomp_playblast_qpushbutton = QtWidgets.QPushButton("Playblast")

		# CAVEAT : Layout for the multiple widgets
		self.animcomp_grid_layout = QtWidgets.QGridLayout()
		self.animcomp_parenthorizontal_vertical_layout = QtWidgets.QVBoxLayout(self.animcomp_toolbox_palyblast_column)
		self.animcomp_browser_horizontal_layout = QtWidgets.QHBoxLayout()


		# CAVEAT : Adding widget to layouts/ Connections
		self.animcomp_toolbox.addItem(self.animcomp_toolbox_palyblast_column, "Playblast")
		self.animcomp_toolbox.addItem(self.animcomp_toolbox_comingsoon_column, "ComingSoon")
		self.animcomp_browser_horizontal_layout.addWidget(self.animcomp_path_qlineedit)
		self.animcomp_browser_horizontal_layout.addWidget(self.animcomp_browse_qpushbutton)
		self.animcomp_parenthorizontal_vertical_layout.addLayout(self.animcomp_browser_horizontal_layout)
		self.animcomp_grid_layout.addWidget(self.animcomp_toolbox)
		self.setLayout(self.animcomp_grid_layout)

		self.setWindowTitle("AnimCompact")
		# self.setFixedSize(300, 130)


if __name__ == "__main__":
	print "This is my main function"
	window = AnimCompactUI()
	window.show()
