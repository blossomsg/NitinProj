from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from vaccum_cleaner import vaccum_cleaner_view_ui
import os
import json
import vaccum_cleaner.techcheck_func

config_path = "E:\\Proj_Codes\\NitinProj\\vaccum_cleaner\\show_configs"
techcheck_path = "E:\\Proj_Codes\\NitinProj\\vaccum_cleaner\\techcheck_func"
config_files = os.listdir(config_path)


with open(os.path.join(techcheck_path, "default_techcheck.json"), "r") as config:
    techcheck_func_dict = json.load(config)
testing = [str(x) for x in techcheck_func_dict.keys()]



class VaccumCleanerDelegate(vaccum_cleaner_view_ui.VaccumCleanerViewUI):
    def __init__(self):
        super(VaccumCleanerDelegate, self).__init__()
        # CAVEAT : Config files adding to the combobox
        self.vacuum_cleaner_combobox.addItems(config_files)

        self.vacuum_cleaner_combobox.activated.connect(self.vaccum_cleaner_combobox_config_func)

        self.vacuum_cleaner_listview_wid.addItems(testing)
        # self.vacuum_cleaner_listview_wid.itemClicked.connect(str(self.vacuum_cleaner_listview_wid.currentItem().text()), "apna time aagaya", techcheck_func_dict.get(self.vacuum_cleaner_listview_wid.currentItem().text()))
        self.vacuum_cleaner_listview_wid.itemClicked.connect(self.print_someting)
        # test_listwid.itemClicked.connect(lambda: text.setText((mydata[list.currentItem().text()])))

        # self.vacuum_cleaner_listview_wid.addItems(['anything_else_besides_polygon_in_the_scene','query_if_the_file_is_coming_from_right_path','name_of_the_camera_for_the_show'])

        # self.model = QtGui.QStringListModel(self.vacuum_cleaner_listview_wid)
        # self.list_of_techcheck = [vaccum_cleaner.techcheck_func.camera_test.query]
        # self.model.setStringList(self.list_of_techcheck)
        # self.item = QtGui.QStandardItem(str(self.list_of_techcheck))
        # self.vacuum_cleaner_listview_wid.setModel(self.model)
        # # print self.model.get(currentIndex)
        # print QtCore.QItemSelectionModel.selectedIndexes(QtCore.QItemSelectionModel(self.model))
        # print QtCore.QItemSelectionModel.currentIndex(QtCore.QItemSelectionModel(self.model))
        # print QtCore.QItemSelectionModel.isSelected()
        # print QtCore.QItemSelectionModel.currentIndex(QtCore.QItemSelectionModel(self.model))
        # print self.vacuum_cleaner_listview_wid.selectedIndexes()


    def vaccum_cleaner_combobox_config_func(self):
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
        print str(self.vacuum_cleaner_listview_wid.currentItem().text()), "apna time aagaya", techcheck_func_dict.get(self.vacuum_cleaner_listview_wid.currentItem().text())
        self.vacuum_cleaner_textedit_wid.setText(str(techcheck_func_dict.get(self.vacuum_cleaner_listview_wid.currentItem().text())))
