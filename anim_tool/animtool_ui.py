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
        self.animtool_playblast_groupbox_qlineedit = QtWidgets.QLineEdit()
        self.animtool_playblast_groupbox_qpushbutton = QtWidgets.QPushButton("Browser")

        # CAVEAT : Viewport Mode List
        self.animtool_playblast_groupbox_combobox = QtWidgets.QComboBox()
        self.combobox_list_test = self.animtool_playblast_groupbox_combobox.addItem("test")

        # CAVEAT : Layout for the multiple widgets
        self.animtool_grid_layout = QtWidgets.QGridLayout()
        self.animtool_playblast_groupbox_horizontal_layout = QtWidgets.QHBoxLayout()
        self.animtool_playblast_groupbox_vertical_layout = QtWidgets.QVBoxLayout()
        self.animtool_playblast_groupbox_box_layout = QtWidgets.QBoxLayout()

        #CAVEAT : Adding widget to layouts
        self.animtool_grid_layout.addWidget(self.animtool_playblast_groupbox)

        self.animtool_playblast_groupbox_horizontal_layout.addWidget(self.animtool_playblast_groupbox_qlineedit)
        self.animtool_playblast_groupbox_horizontal_layout.addWidget(self.animtool_playblast_groupbox_qpushbutton)

        self.animtool_playblast_groupbox_vertical_layout.addWidget(self.animtool_playblast_groupbox_combobox)

        self.animtool_playblast_groupbox.setLayout(self.animtool_playblast_groupbox_box_layout.addLayout(self.animtool_playblast_groupbox_vertical_layout))
        self.animtool_playblast_groupbox.setLayout(self.animtool_playblast_groupbox_box_layout.addLayout(self.animtool_playblast_groupbox_horizontal_layout))
        self.setLayout(self.animtool_grid_layout)

        self.setWindowTitle("AnimTools")
        self.setFixedSize(300, 100)


if __name__ == "__main__":
    print "This is my main function"
    window = AnimToolsUI()
    window.show()





# from PySide2 import QtCore, QtWidgets, QtGui
#
# animtool_grid_layout = QtWidgets.QGridLayout()
# animtool_h_layout = QtWidgets.QHBoxLayout()
# animtool_b_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction(QtWidgets.QBoxLayout.TopToBottom))
# #animtool_b_layout = QtWidgets.QBoxLayout.Direction(QtCore.Qt.Orientation(QtWidgets.QBoxLayout.TopToBottom))
# animtool_playblast_groupbox = QtWidgets.QGroupBox("Playblast")
# animtool_playblast_groupbox_qlineedit = QtWidgets.QLineEdit()
# animtool_playblast_groupbox_qpushbutton = QtWidgets.QPushButton("Browser")
# animtool_playblast_groupbox_combobox = QtWidgets.QComboBox()
# animtool_playblast_groupbox_qpushbutton_test = QtWidgets.QPushButton("TEST")
# animtool_h_layout.addWidget(animtool_playblast_groupbox_qlineedit)
# animtool_h_layout.addWidget(animtool_playblast_groupbox_qpushbutton)
# animtool_b_layout.addLayout(animtool_h_layout)
# animtool_b_layout.addWidget(animtool_playblast_groupbox_combobox)
# animtool_b_layout.addWidget(animtool_playblast_groupbox_qpushbutton_test)
# animtool_grid_layout.addLayout(animtool_b_layout, 1,1)
#
#
# animtool_playblast_groupbox.setLayout(animtool_grid_layout)
# window = animtool_playblast_groupbox
# window.show()
