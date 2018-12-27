from PySide2 import QtWidgets
from PySide2 import QtGui


class MassPlayblastLay(QtWidgets.QWidget):
	def __init__(self):
		super(MassPlayblastLay, self).__init__()
		# CAVEAT : Playblast Toolbox Layout
		self.animcog_toolbox_palyblast_column = QtWidgets.QWidget()

		# CAVEAT : Default Vp settings
		self.animcog_textured_qpushbutton = QtWidgets.QToolButton.setIcon(QtGui.QIcon("D:\\All_Projs\\NitinProj\\anim_conglomeration\\chess.png"))

		# CAVEAT : Browser
		self.animcog_path_qlineedit = QtWidgets.QLineEdit()
		self.animcog_browse_qpushbutton = QtWidgets.QPushButton("Browse")

		# CAVEAT : Viewport Mode List
		self.animcog_vp_combobox = QtWidgets.QComboBox()
		self.animcog_vp_2_combobox = self.animcog_vp_combobox.addItem(
			"Viewport 2.0")
		self.animcog_ldvp_combobox = self.animcog_vp_combobox.addItem(
			"Legacy Default Viewport")
		self.animcog_lhqvp_combobox = self.animcog_vp_combobox.addItem(
			"Legacy High Quality Viewport")
		self.animcog_playblast_qpushbutton = QtWidgets.QPushButton("Playblast")

		# CAVEAT : Layout for the multiple widgets
		self.animcog_parenthorizontal_vertical_layout = QtWidgets.QVBoxLayout(self.animcog_toolbox_palyblast_column)
		self.animcog_browser_horizontal_layout = QtWidgets.QHBoxLayout()
		self.animcog_switches_buttons_horizontal_layout = QtWidgets.QHBoxLayout()

		# CAVEAT : Adding widget to Layouts/Connections
		self.animcog_browser_horizontal_layout.addWidget(self.animcog_path_qlineedit)
		self.animcog_browser_horizontal_layout.addWidget(self.animcog_browse_qpushbutton)
		self.animcog_switches_buttons_horizontal_layout.addWidget(self.animcog_textured_qpushbutton)
		self.animcog_parenthorizontal_vertical_layout.addLayout(self.animcog_browser_horizontal_layout)
		self.animcog_parenthorizontal_vertical_layout.addLayout(self.animcog_switches_buttons_horizontal_layout)
		self.animcog_parenthorizontal_vertical_layout.addWidget(self.animcog_vp_combobox)
		self.animcog_parenthorizontal_vertical_layout.addWidget(self.animcog_playblast_qpushbutton)



if __name__ == "__main__":
	print "This is my Main Class"
else:
	print "This is MassPlayblastLay"
