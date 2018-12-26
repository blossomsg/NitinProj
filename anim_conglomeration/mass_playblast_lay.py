from PySide2 import QtWidgets


class MassPlayblastLay(QtWidgets.QWidget):
	def __init__(self):
		super(MassPlayblastLay, self).__init__()
		# CAVEAT : Playblast Toolbox Layout
		self.animcomp_toolbox_palyblast_column = QtWidgets.QWidget()

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
		self.animcomp_parenthorizontal_vertical_layout = QtWidgets.QVBoxLayout(self.animcomp_toolbox_palyblast_column)
		self.animcomp_browser_horizontal_layout = QtWidgets.QHBoxLayout()

		# CAVEAT : Adding widget to Layouts/Connections
		self.animcomp_browser_horizontal_layout.addWidget(self.animcomp_path_qlineedit)
		self.animcomp_browser_horizontal_layout.addWidget(self.animcomp_browse_qpushbutton)
		self.animcomp_parenthorizontal_vertical_layout.addLayout(self.animcomp_browser_horizontal_layout)
		self.animcomp_parenthorizontal_vertical_layout.addWidget(self.animcomp_vp_combobox)
		self.animcomp_parenthorizontal_vertical_layout.addWidget(self.animcomp_playblast_qpushbutton)


if __name__ == "__main__":
	print "This is my Main Class"
else:
	print "This is MassPlayblastLay"
