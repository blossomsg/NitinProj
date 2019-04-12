from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from vacuum_cleaner import vacuum_cleaner_view_ui
import os
import json
import shutil
import vacuum_cleaner.techcheck_func

config_path = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\show_configs"
techcheck_path = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func"
config_files = os.listdir(config_path)


with open(os.path.join(techcheck_path, "default_techcheck.json"), "r") as config:
    techcheck_func_dict = json.load(config)


class VacuumCleanerDelegate(vacuum_cleaner_view_ui.VacuumCleanerViewUI):
    def __init__(self):
        super(VacuumCleanerDelegate, self).__init__()
        # CAVEAT : Config files adding to the combobox and selection
        self.vacuum_cleaner_combobox.addItems(config_files)
        self.vacuum_cleaner_combobox.activated.connect(self.vacuum_cleaner_combobox_config_func)

        # CAVEAT : Loading all the techcheck list(from a json file) in the listview and selection of techcheck in the view
        self.vacuum_cleaner_listwid.addItems(techcheck_func_dict.keys())
        self.vacuum_cleaner_listwid.currentItemChanged.connect(self.print_someting)
        # test_listwid.itemClicked.connect(lambda: text.setText((mydata[list.currentItem().text()])))

        # CAVEAT : Progress bar already 100% (assuming as the scene is filled with dirt)
        self.vacuum_cleaner_progressbar.setValue(100)
        self.vacuum_cleaner_pushbutton.clicked.connect(self.vacuum_cleaner_progress_bar_process)

        # self.vacuum_cleaner_listview_wid.addItems(['anything_else_besides_polygon_in_the_scene','query_if_the_file_is_coming_from_right_path','name_of_the_camera_for_the_show'])

        # self.model = QtGui.QStringListModel(self.vacuum_cleaner_listview_wid)
        # self.list_of_techcheck = [vacuum_cleaner.techcheck_func.camera_test.query]
        # self.model.setStringList(self.list_of_techcheck)
        # self.item = QtGui.QStandardItem(str(self.list_of_techcheck))
        # self.vacuum_cleaner_listview_wid.setModel(self.model)
        # # print self.model.get(currentIndex)
        # print QtCore.QItemSelectionModel.selectedIndexes(QtCore.QItemSelectionModel(self.model))
        # print QtCore.QItemSelectionModel.currentIndex(QtCore.QItemSelectionModel(self.model))
        # print QtCore.QItemSelectionModel.isSelected()
        # print QtCore.QItemSelectionModel.currentIndex(QtCore.QItemSelectionModel(self.model))
        # print self.vacuum_cleaner_listview_wid.selectedIndexes()


    def vacuum_cleaner_combobox_config_func(self):
        with open(os.path.join(config_path, self.vacuum_cleaner_combobox.currentText()), "r") as config:
            config_var_dict = json.load(config)
        # print dict.keys(config_var_dict)

    # def load_techcheck_func(self):
    #     with open(os.path.join(techcheck_path, "default_techcheck.json"), "r") as config:
    #         techcheck_func_dict = json.load(config)
    #     # listing = ['anything_else_besides_polygon_in_the_scene','query_if_the_file_is_coming_from_right_path','name_of_the_camera_for_the_show']
    #     #     return techcheck_func_dict.keys()
    #     testing = [str(x) for x in techcheck_func_dict.keys()]
    #     return testing

    def print_someting(self):
        print str(self.vacuum_cleaner_listwid.currentItem().text()), "apna time aagaya", techcheck_func_dict.get(self.vacuum_cleaner_listwid.currentItem().text())
        self.vacuum_cleaner_textedit_wid.setText(str(techcheck_func_dict.get(self.vacuum_cleaner_listwid.currentItem().text())))


    def vacuum_cleaner_progress_bar_process(self):
        self.vacuum_cleaner_progressbar.setValue(0)
        self.vacuum_cleaner_publish_pushbutton.setEnabled(True)
        src = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck.json"
        dst = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck_updated.json"
        shutil.copy(src, dst)
        print "created an updated techcheck", dst


    def closeEvent(self, event):
        if os.path.isfile("E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck_updated.json"):
            os.remove("E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck_updated.json")
        else:
            print "no updated techcheck file was created"







# this the setup to write the update updated_techcheck.json
# import maya.cmds as cmds
# import json
#
# config_path = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\show_configs"
# config_files = os.listdir(config_path)
# techcheck_path = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func"
#
#
#
# with open(os.path.join(config_path, "dumplings.json"), "r") as config:
#     techcheck_func_dict = json.load(config)
# testing = [str(x) for x in techcheck_func_dict.keys()]
#
# with open(os.path.join(techcheck_path, "default_techcheck.json"), "r") as config:
#     listview_update = json.load(config)
#
#
# def camera_exits(config_file_camera_attribute):
#     camera_list = cmds.ls(type="camera")
#     if config_file_camera_attribute in camera_list:
#         return "Camera exists in the scene with the right name - renderCamShape"
#     else:
#         return "Camera does not exists in the scene or the name of the camera is improper kindly rectify name with renderCamShape(name the transform node to camRender automatically will rename the shapenode)"
#
# #camera_exits(techcheck_func_dict["camera_name"])
#
# listview_update["Camera exists"] = "Camera exits in the scene with the right name - renderCamShape"
#
# with open(os.path.join(techcheck_path, "default_techcheck.json"), 'w') as f:
#     f.write(json.dumps(listview_update))
