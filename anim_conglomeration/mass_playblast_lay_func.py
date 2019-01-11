from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

import sys

path_anim_tools = "E:\\Proj_Codes\\NitinProj\\anim_conglomeration\\"
if not path_anim_tools in sys.path:
    sys.path.append(path_anim_tools)
import anim_conglomeration_ui

class MassPlayblastLayFunc(anim_conglomeration_ui.AnimConglomerationUI):
    def __init__(self):
        super(MassPlayblastLayFunc, self).__init__()

        self.animcog_mpb_browse_qpushbutton.clicked.connect(self.animcog_mpb_browse_button_func)
        self.animcog_mpb_usealllights_qpushbutton.clicked.connect(self.animcog_mpb_usealllights_toggle_button_func)
        self.animcog_mpb_shadows_qpushbutton.clicked.connect(self.animcog_mpb_shadows_toggle_button_func)
        self.animcog_mpb_ambocclusion_qpushbutton.clicked.connect(self.animcog_mpb_ambocclusion_toggle_button_func)
        self.animcog_mpb_antialiasing_qpushbutton.clicked.connect(self.animcog_mpb_antialiasing_toggle_button_func)
        self.animcog_mpb_vp_combobox.activated.connect(self.animcog_mpb_vp_mode_func)
        self.animcog_mpb_playblast_qpushbutton.clicked.connect(self.animcog_mpb_playblast_button)
        self.animcog_mpb_default_settings()

    def animcog_mpb_default_settings(self):
        cmds.modelEditor("modelPanel4", edit=True, rendererName="vp2Renderer")
        cmds.modelEditor("modelPanel4", edit=True, displayLights="none")
        cmds.modelEditor("modelPanel4", edit=True, shadows=False)
        cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 0)
        cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 0)

    def animcog_mpb_browse_button_func(self):
        self.browse_path = cmds.fileDialog2(fileFilter="Movie Files(*.mov)", dialogStyle=2)
        print "Playblast Saving Path --> %s" %self.browse_path[0]
        self.animcog_mpb_path_qlineedit.setText(self.browse_path[0])

    def animcog_mpb_usealllights_toggle_button_func(self):
        if self.animcog_mpb_usealllights_qpushbutton.isChecked():
            cmds.modelEditor("modelPanel4", edit=True, displayLights="all")
        else:
            cmds.modelEditor("modelPanel4", edit=True, displayLights="none")

    def animcog_mpb_shadows_toggle_button_func(self):
        if self.animcog_mpb_shadows_qpushbutton.isChecked():
            cmds.modelEditor("modelPanel4", edit=True, shadows=True)
        else:
            cmds.modelEditor("modelPanel4", edit=True, shadows=False)

    def animcog_mpb_ambocclusion_toggle_button_func(self):
        if self.animcog_mpb_ambocclusion_qpushbutton.isChecked():
            cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 1)
        else:
            cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 0)

    def animcog_mpb_antialiasing_toggle_button_func(self):
        if self.animcog_mpb_antialiasing_qpushbutton.isChecked():
            cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
        else:
            cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 0)

    def animcog_mpb_vp_mode_func(self):
        if self.animcog_mpb_vp_combobox.currentText() == "Viewport 2.0":
            print self.animcog_mpb_vp_combobox.currentText()
            cmds.modelEditor("modelPanel4", edit=True, rendererName="vp2Renderer")
        elif self.animcog_mpb_vp_combobox.currentText() == "Legacy Default Viewport":
            print self.animcog_mpb_vp_combobox.currentText()
            cmds.modelEditor("modelPanel4", edit=True, rendererName="base_OpenGL_Renderer")
        elif self.animcog_mpb_vp_combobox.currentText() == "Legacy High Quality Viewport":
            print self.animcog_mpb_vp_combobox.currentText()
            cmds.modelEditor("modelPanel4", edit=True, rendererName="hwRender_OpenGL_Renderer")

    def animcog_mpb_playblast_button(self):
        self.time_slider = mel.eval("$gPlayBackSlider = $gPlayBackSlider")
        self.soundtrack_name = cmds.timeControl(self.time_slider, query=True, sound=True)
        self.default_width = cmds.getAttr ("defaultResolution.width")
        self.default_height = cmds.getAttr("defaultResolution.height")
        cmds.playblast(format="qt", offScreen=True, percent=100, quality=100, filename="%s"%self.browse_path[0],
                       forceOverwrite=True, clearCache=True, viewer=True, showOrnaments=False, compression="PNG",
                       sequenceTime=False, sound=self.soundtrack_name, widthHeight=[self.default_width, self.default_height])


if __name__ == "__main__":
    print "This is my Main MassPlayblastLayFunc"
else:
    print "This is MassPlayblastLayFunc"


# import sys
# path_anim_tools = "E:\\Proj_Codes\\NitinProj\\anim_conglomeration\\"
# if not path_anim_tools in sys.path:
# 	sys.path.append(path_anim_tools)
# import mass_playblast_lay_func
# reload(mass_playblast_lay_func)
# anicog_win = mass_playblast_lay_func.MassPlayblastLayFunc()
# anicog_win.show()


# import maya.cmds as cmds
# cmds.fileDialog2(dialogStyle=2)
# cmds.modelEditor( 'modelPanel4', q=True, rls=True )
# cmds.getPanel (wf=1)
# cmds.modelEditor("modelPanel4", edit=True, displayLights="all")
# cmds.modelEditor("modelPanel4", edit=True, shadows=True)
# cmds.setAttr ("hardwareRenderingGlobals.ssaoEnable", 1)
# cmds.setAttr ("hardwareRenderingGlobals.multiSampleEnable", 1)
# cmds.modelEditor("modelPanel4", query=True, rendererList=True)
# cmds.modelEditor("modelPanel4", edit=True, rendererName="vp2Renderer")
# cmds.modelEditor("modelPanel4", edit=True, rendererName="hwRender_OpenGL_Renderer")
# cmds.modelEditor("modelPanel4", edit=True, rendererName="base_OpenGL_Renderer")
# browse_path = cmds.fileDialog2(fileFilter="Movie Files(*.mov)", dialogStyle=2)
# time_control = mel.eval("$gPlayBackSlider = $gPlayBackSlider")
# sound_name = cmds.timeControl(time_control, query=True, sound=True)
# cmds.playblast( format="qt", offScreen=True, percent=100, quality=100, filename="E:\\Proj_References\\test.mov", forceOverwrite=True, clearCache=True, viewer=True, showOrnaments=False, compression="PNG", sequenceTime=False, sound=sound_name )
# default_width = cmds.getAttr ("defaultResolution.width")
# default_height = cmds.getAttr("defaultResolution.height")
# # Result: [u'vp2Renderer',u'base_OpenGL_Renderer',u'hwRender_OpenGL_Renderer',u'stub_Renderer'] #