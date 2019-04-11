from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(long(ptr), QtWidgets.QWidget)


class VacuumCleanerViewUI(QtWidgets.QWidget):
    def __init__(self):
        super(VacuumCleanerViewUI, self).__init__()
        # CAVEAT : Parent the UI to the application Maya
        self.setParent(ptr_instance)
        self.setWindowFlags(QtCore.Qt.Window)

        # CAVEAT : Children wid's of Vacuum Cleaner, to list the techcheck names and the result
        self.vacuum_cleaner_combobox_label = QtWidgets.QLabel("Project Name")
        self.vacuum_cleaner_combobox_label.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.vacuum_cleaner_combobox_label.setAlignment(QtCore.Qt.AlignRight)
        self.vacuum_cleaner_combobox = QtWidgets.QComboBox()
        self.vacuum_cleaner_combobox.setMaximumSize(165, 30)
        self.vacuum_cleaner_listwid = QtWidgets.QListWidget()
        self.vacuum_cleaner_textedit_wid = QtWidgets.QTextEdit()
        self.vacuum_cleaner_progressbar = QtWidgets.QProgressBar()
        self.vacuum_cleaner_pushbutton = QtWidgets.QPushButton("Run Vacuum")
        self.vacuum_cleaner_publish_pushbutton = QtWidgets.QPushButton("Publish")
        self.vacuum_cleaner_publish_pushbutton.setEnabled(False)
        # CAVEAT : Layout the children to keep them organized vertically
        self.vacuum_cleaner_parent_vertical_lay = QtWidgets.QVBoxLayout()

        # CAVEAT : Layout to keep list and textedit horizontally organized
        self.vacuum_cleaner_list_textedit_horizontal_lay = QtWidgets.QHBoxLayout()
        self.vacuum_cleaner_combobox_label_horizontal_lay = QtWidgets.QHBoxLayout()

        # CAVEAT : Adding widgets to Vacuum Cleaner/ Connections
        self.vacuum_cleaner_combobox_label_horizontal_lay.addWidget(self.vacuum_cleaner_combobox_label)
        self.vacuum_cleaner_combobox_label_horizontal_lay.addWidget(self.vacuum_cleaner_combobox)
        self.vacuum_cleaner_list_textedit_horizontal_lay.addWidget(self.vacuum_cleaner_listwid)
        self.vacuum_cleaner_list_textedit_horizontal_lay.addWidget(self.vacuum_cleaner_textedit_wid)
        self.vacuum_cleaner_parent_vertical_lay.addLayout(self.vacuum_cleaner_combobox_label_horizontal_lay)
        self.vacuum_cleaner_parent_vertical_lay.addLayout(self.vacuum_cleaner_list_textedit_horizontal_lay)
        self.vacuum_cleaner_parent_vertical_lay.addWidget(self.vacuum_cleaner_progressbar)
        self.vacuum_cleaner_parent_vertical_lay.addWidget(self.vacuum_cleaner_pushbutton)
        self.vacuum_cleaner_parent_vertical_lay.addWidget(self.vacuum_cleaner_publish_pushbutton)

        self.setLayout(self.vacuum_cleaner_parent_vertical_lay)

        self.setWindowTitle("vacuum cleaner v1.0")
        # self.setWindowIcon("E:\\Proj_Codes\\NitinProj\\icons\\anim_conglomeration\\tool_logo\\molecule.png")
        # self.windowIcon("E:\\Proj_Codes\\NitinProj\\icons\\anim_conglomeration\\tool_logo\\molecule.png")
        # self.setFixedSize(250, 230)


if __name__ == "__main__":
    print "This is Main FertilizerViewUI"
else:
    print "This is FertilizerViewUI"
    # window = FertilizerViewUI()
    # window.show()
