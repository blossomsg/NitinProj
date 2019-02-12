from PySide2 import QtWidgets
from PySide2 import QtGui


class MassPlayblastLay(QtWidgets.QWidget):
    """animcog_mpb is abbreviation for animconglomeration_massplayblast

	"""

    def __init__(self):
        super(MassPlayblastLay, self).__init__()
        # CAVEAT : Playblast Toolbox layout
        self.animcog_mpb_toolbox_palyblast_column = QtWidgets.QWidget()
        self.animcog_mpb_toolbox_palyblast_column.setStyleSheet("QWidget {background-color:#95c7db;}")

        # CAVEAT : Default Vp settings buttons in toolbox layout- lights
        self.animcog_mpb_usealllights_qpushbutton = QtWidgets.QPushButton()
        self.animcog_mpb_usealllights_qpushbutton.setIcon(
            QtGui.QIcon("E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_lights.png"))
        self.animcog_mpb_usealllights_qpushbutton.setFlat(True)
        self.animcog_mpb_usealllights_qpushbutton.setCheckable(True)
        self.animcog_mpb_usealllights_qpushbutton.setFixedSize(20, 20)
        self.animcog_mpb_usealllights_qpushbutton.setStyleSheet("QPushButton:pressed{background:#054f6d; border:none} "
                                                                "QPushButton:checked{background:#054f6d; border:none} "
                                                                "QPushButton:hover:checked{image:url(E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_lights.png); border:none}"
                                                                "QPushButton:hover{image: url(E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_lights.png); border:none}")

        # CAVEAT : Default Vp settings buttons in toolbox layout- shadows
        self.animcog_mpb_shadows_qpushbutton = QtWidgets.QPushButton()
        self.animcog_mpb_shadows_qpushbutton.setIcon(
            QtGui.QIcon("E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_shadows.png"))
        self.animcog_mpb_shadows_qpushbutton.setFlat(True)
        self.animcog_mpb_shadows_qpushbutton.setCheckable(True)
        self.animcog_mpb_shadows_qpushbutton.setFixedSize(20, 20)
        self.animcog_mpb_shadows_qpushbutton.setStyleSheet("QPushButton:pressed{background:#054f6d; border:none} "
                                                           "QPushButton:checked{background:#054f6d; border:none} "
                                                           "QPushButton:hover:checked{image: url(E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_shadows.png); border:none}"
                                                           "QPushButton:hover{E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_shadows.png); border:none}")

        # CAVEAT : Default Vp settings buttons in toolbox layout- ambient occlusion
        self.animcog_mpb_ambocclusion_qpushbutton = QtWidgets.QPushButton()
        self.animcog_mpb_ambocclusion_qpushbutton.setIcon(
            QtGui.QIcon(
                "E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_ambient_occlusion.png"))
        self.animcog_mpb_ambocclusion_qpushbutton.setFlat(True)
        self.animcog_mpb_ambocclusion_qpushbutton.setCheckable(True)
        self.animcog_mpb_ambocclusion_qpushbutton.setFixedSize(20, 20)
        self.animcog_mpb_ambocclusion_qpushbutton.setStyleSheet("QPushButton:pressed{background:#054f6d; border:none} "
                                                                "QPushButton:checked{background:#054f6d; border:none} "
                                                                "QPushButton:hover:checked{image: url(E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_ambient_occlusion.png); border:none}"
                                                                "QPushButton:hover{E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_ambient_occlusion.png); border:none}")

        # CAVEAT : Default Vp settings buttons in toolbox layout- anti-aliasing
        self.animcog_mpb_antialiasing_qpushbutton = QtWidgets.QPushButton()
        self.animcog_mpb_antialiasing_qpushbutton.setIcon(
            QtGui.QIcon(
                "E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_anti_aliasing.png"))
        self.animcog_mpb_antialiasing_qpushbutton.setFlat(True)
        self.animcog_mpb_antialiasing_qpushbutton.setCheckable(True)
        self.animcog_mpb_antialiasing_qpushbutton.setFixedSize(20, 20)
        self.animcog_mpb_antialiasing_qpushbutton.setStyleSheet(
            "QPushButton:pressed{background:#054f6d; border:none} "
            "QPushButton:checked{background:#054f6d; border:none} "
            "QPushButton:hover:checked{image: url(E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_anti_aliasing.png); border:none}"
            "QPushButton:hover{E:\\Proj_Codes\\NitinProj\icons\\anim_conglomeration\\viewport_modes\\vp_icon_anti_aliasing.png); border:none}")

        # CAVEAT : Playblast browse button in toolbox layout
        self.animcog_mpb_path_qlineedit = QtWidgets.QLineEdit()
        self.animcog_mpb_path_qlineedit.setStyleSheet(
            "QLineEdit {background-color:#054f6d; color:#81d0ef; border: 1px solid #054f6d;}")
        self.animcog_mpb_browse_qpushbutton = QtWidgets.QPushButton("Browse")
        self.animcog_mpb_browse_qpushbutton.setStyleSheet("QPushButton {background-color:#054f6d; color:#81d0ef; }")

        # CAVEAT : Viewport Mode List in toolbox layout
        self.animcog_mpb_vp_combobox = QtWidgets.QComboBox()
        self.animcog_mpb_vp_combobox.setStyleSheet(
            "QComboBox {background-color:#054f6d; color:#81d0ef; background:#054f6d} QComboBox QAbstractItemView {"
            "background-color:#054f6d; color:#81d0ef; background:#054f6d}")
        self.animcog_mpb_vp_2_combobox = self.animcog_mpb_vp_combobox.addItem(
            "Viewport 2.0")
        self.animcog_mpb_ldvp_combobox = self.animcog_mpb_vp_combobox.addItem(
            "Legacy Default Viewport")
        self.animcog_mpb_lhqvp_combobox = self.animcog_mpb_vp_combobox.addItem(
            "Legacy High Quality Viewport")
        self.animcog_mpb_playblast_qpushbutton = QtWidgets.QPushButton("Playblast")
        self.animcog_mpb_playblast_qpushbutton.setStyleSheet("QPushButton {background-color:#054f6d; color:#81d0ef; }")

        # CAVEAT : Layouts for the multiple widgets
        self.animcog_mpb_parent_vertical_layout = QtWidgets.QVBoxLayout(
            self.animcog_mpb_toolbox_palyblast_column)
        self.animcog_mpb_browser_horizontal_layout = QtWidgets.QHBoxLayout()
        self.animcog_mpb_vp_buttons = QtWidgets.QHBoxLayout()

        # CAVEAT : Adding widget to Layouts/Connections
        # CAVEAT : Adding widget anim line_edit and browse button to horizontal layout
        self.animcog_mpb_browser_horizontal_layout.addWidget(self.animcog_mpb_path_qlineedit)
        self.animcog_mpb_browser_horizontal_layout.addWidget(self.animcog_mpb_browse_qpushbutton)
        # CAVEAT : Adding widget vp buttons in horizontal layout so that visually they are in one line
        self.animcog_mpb_vp_buttons.addWidget(self.animcog_mpb_usealllights_qpushbutton)
        self.animcog_mpb_vp_buttons.addWidget(self.animcog_mpb_shadows_qpushbutton)
        self.animcog_mpb_vp_buttons.addWidget(self.animcog_mpb_ambocclusion_qpushbutton)
        self.animcog_mpb_vp_buttons.addWidget(self.animcog_mpb_antialiasing_qpushbutton)
        # CAVEAT : Adding layouts in the playblast stack in vertical manner
        self.animcog_mpb_parent_vertical_layout.addLayout(self.animcog_mpb_browser_horizontal_layout)
        self.animcog_mpb_parent_vertical_layout.addLayout(self.animcog_mpb_vp_buttons)
        self.animcog_mpb_parent_vertical_layout.addWidget(self.animcog_mpb_vp_combobox)
        self.animcog_mpb_parent_vertical_layout.addWidget(self.animcog_mpb_playblast_qpushbutton)


if __name__ == "__main__":
    print "This is my Main MassPlayblastLay"
else:
    print "This is MassPlayblastLay"
