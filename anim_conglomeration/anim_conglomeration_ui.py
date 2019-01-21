import mass_playblast_lay
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(long(ptr), QtWidgets.QWidget)


class AnimConglomerationUI(mass_playblast_lay.MassPlayblastLay):
    def __init__(self):
        super(AnimConglomerationUI, self).__init__()
        # CAVEAT : Parent ui to the application through which the ui is being created
        self.setParent(ptr_instance)
        self.setWindowFlags(QtCore.Qt.Window)

        # CAVEAT : Playblast Toolbox
        self.animcog_toolbox = QtWidgets.QToolBox()
        self.animcog_toolbox_comingsoon_column = QtWidgets.QWidget()

        # CAVEAT : Layout for the Toolbox widgets
        self.animcog_grid_layout = QtWidgets.QGridLayout()

        # CAVEAT : Adding widget to MassLayouts/ Connections
        self.animcog_toolbox.addItem(self.animcog_mpb_toolbox_palyblast_column, "Playblast")
        self.animcog_toolbox.addItem(self.animcog_toolbox_comingsoon_column, "ComingSoon")
        self.animcog_grid_layout.addWidget(self.animcog_toolbox)
        self.setLayout(self.animcog_grid_layout)

        self.setWindowTitle("animcog v1.0")
        self.setWindowIcon("E:\\Proj_Codes\\NitinProj\\icons\\anim_conglomeration\\tool_logo\\molecule.png")
        # self.windowIcon("E:\\Proj_Codes\\NitinProj\\icons\\anim_conglomeration\\tool_logo\\molecule.png")
        self.setFixedSize(250, 230)


if __name__ == "__main__":
    print "This is Main AnimConglomerationUI"
else:
    print "This is AnimConglomerationUI"
    # window = AnimConglomerationUI()
    # window.show()
