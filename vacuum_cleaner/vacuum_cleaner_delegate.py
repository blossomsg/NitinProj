from PySide2 import QtGui
from vacuum_cleaner import vacuum_cleaner_view_ui
import os
import json
import shutil
import maya.cmds as cmds



class VacuumCleanerDelegate(vacuum_cleaner_view_ui.VacuumCleanerViewUI):
    def __init__(self):
        super(VacuumCleanerDelegate, self).__init__()
        # CAVEAT : Config files adding to the combobox and selection
        config_path = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\show_configs"
        config_files = os.listdir(config_path)
        self.vacuum_cleaner_combobox.addItems(config_files)
        self.vacuum_cleaner_combobox.activated.connect(self.vacuum_cleaner_combobox_config_func)

        # CAVEAT : Loading all the techcheck list(from default json file) in the listview and selection of techcheck in the editview
        self.vacuum_cleaner_listwid.addItems(self.vacuum_cleaner_load_techcheck_json("default_techcheck.json").keys())
        self.vacuum_cleaner_listwid.currentItemChanged.connect(self.vacuum_cleaner_textedit_values)

        # CAVEAT : Progress bar already 100% (assuming as the scene is filled with dirt)
        self.vacuum_cleaner_progressbar.setValue(100)
        self.vacuum_cleaner_pushbutton.clicked.connect(self.vacuum_cleaner_setup)

    # FIXME: Combobox is only for project purpose to choose which proj is being used
    def vacuum_cleaner_combobox_config_func(self):
        with open(os.path.join(config_path, self.vacuum_cleaner_combobox.currentText()), "r") as config:
            config_var_dict = json.load(config)
        # print dict.keys(config_var_dict)
        return dict.keys(config_var_dict)

    # CAVEAT: Loads the techcheck(json) that you, and with the help of arg loads specific json
    def vacuum_cleaner_load_techcheck_json(self, techcheck_json_file):
        techcheck_path = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func"
        with open(os.path.join(techcheck_path, techcheck_json_file), "r") as config:
            techcheck_func_dict = json.load(config)
            # print techcheck_func_dict
            return techcheck_func_dict

    # FIXME: Default techcheck(json) values in textedit, need to make it dynamic and even prompts an error
    def vacuum_cleaner_textedit_values(self):
        # print self.vacuum_cleaner_listwid.currentItem().text(), "---->", self.vacuum_cleaner_load_techcheck_json("default_techcheck.json").get(self.vacuum_cleaner_listwid.currentItem().text())
        self.vacuum_cleaner_textedit_wid.setText(str(
            self.vacuum_cleaner_load_techcheck_json("default_techcheck.json").get(
                self.vacuum_cleaner_listwid.currentItem().text())))

    # CAVEAT: Run vacuum cleaner button sets pregress bar value, enables publish, creates updated techcheck, clears default techcheck from the listwid, queries whole scene, and updates with new values
    def vacuum_cleaner_setup(self):
        self.vacuum_cleaner_progressbar.setValue(0)
        self.vacuum_cleaner_publish_pushbutton.setEnabled(True)
        src = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_fun" \
              "c\\default_techcheck.json"
        dst = "E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck_updated.json"
        shutil.copy(src, dst)
        self.camera_exists(self.vacuum_cleaner_confirm_key_in_techcheck("Camera exists"))
        self.vacuum_cleaner_listwid.clear()
        self.vacuum_cleaner_listwid.addItems(
            self.vacuum_cleaner_load_techcheck_json("default_techcheck_updated.json").keys())
        self.vacuum_cleaner_listwid.currentItemChanged.connect(self.vacuum_cleaner_textedit_values_updated)

    # FIXME: Default techcheck(json) updated values in textedit, need to make it dynamic is a boilerplate
    def vacuum_cleaner_textedit_values_updated(self):
        # print self.vacuum_cleaner_listwid.currentItem().text(), "---->", self.vacuum_cleaner_load_techcheck_json("default_techcheck.json").get(self.vacuum_cleaner_listwid.currentItem().text())
        self.vacuum_cleaner_textedit_wid.setText(str(
            self.vacuum_cleaner_load_techcheck_json("default_techcheck_updated.json").get(
                self.vacuum_cleaner_listwid.currentItem().text())))

    # CAVEAT: Cross check provided arg(key name in the json for the exact key name) and returns the key
    def vacuum_cleaner_confirm_key_in_techcheck(self, select_techcheck_attr):
        listview_update = self.vacuum_cleaner_load_techcheck_json("default_techcheck_updated.json")
        if select_techcheck_attr in listview_update:
            # print "yes it exits"
            return select_techcheck_attr

    # CAVEAT: Dumps the values in the json, need to provide a var for specific key value update
    def write_updated_techcheck_josn(self, var_name_with_new_values):
        with open(os.path.join("E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\",
                               "default_techcheck_updated.json"), 'w') as techcheck_func_dic:
            techcheck_func_dic.write(json.dumps(var_name_with_new_values))

    # CAVEAT: techcheck camera query in the scene
    def camera_exists(self, updated_techcheck_attr):
        listview_update_attr = self.vacuum_cleaner_load_techcheck_json("default_techcheck_updated.json")
        camera_list = cmds.ls(type="camera")
        print camera_list
        if "renderCamShape" in camera_list:
            listview_update_attr[
                updated_techcheck_attr] = "Camera exists in the scene with the right name - renderCamShape"
            self.write_updated_techcheck_josn(listview_update_attr)
            print "Camera exists in the scene with the right name - renderCamShape"
            # self.vacuum_cleaner_listwid.item(3)
            self.QListWidgetItem.setText("Camera exists").setForeground(QtGui.QBrush.setColor(QtGui.QColor.colorNames(red)))

            # QtGui.QColor.colorNames()
        else:
            listview_update_attr[
                updated_techcheck_attr] = "Camera does not exists in the scene or the name of the camera is improper kindly rectify name with renderCamShape(name the transform node to camRender automatically will rename the shapenode)"
            self.write_updated_techcheck_josn(listview_update_attr)
            print "Camera does not exists in the scene or the name of the camera is improper kindly rectify name with renderCamShape(name the transform node to camRender automatically will rename the shapenode)"

    # CAVEAT : When the window is closed(X-cross red button) it will return certain values
    def closeEvent(self, event):
        if os.path.isfile("E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck_updated.json"):
            os.remove("E:\\Proj_Codes\\NitinProj\\vacuum_cleaner\\techcheck_func\\default_techcheck_updated.json")
            print "deleted updated techcheck file"
        else:
            print "no updated techcheck file was created"


# import sys
# path = "E:\Proj_Codes\NitinProj\vacuum_cleaner"
# sys.path.append(path)
# if path in sys.path:
#     print "path exits"
# from vacuum_cleaner.vacuum_cleaner_delegate import VacuumCleanerDelegate
# delegate = VacuumCleanerDelegate()
# delegate.show()