import anim_conglomeration_ui
import maya.cmds as cmds
import maya.mel as mel


class MassPlayblastLayFunc(anim_conglomeration_ui.AnimConglomerationUI):
    def __init__(self):
        super(MassPlayblastLayFunc, self).__init__()

        # CAVEAT : AnimConglomerationUI connections with functions
        self.animcog_mpb_browse_qpushbutton.clicked.connect(self.animcog_mpb_browse_button_func)
        self.animcog_mpb_usealllights_qpushbutton.clicked.connect(self.animcog_mpb_usealllights_toggle_button_func)
        self.animcog_mpb_shadows_qpushbutton.clicked.connect(self.animcog_mpb_shadows_toggle_button_func)
        self.animcog_mpb_ambocclusion_qpushbutton.clicked.connect(self.animcog_mpb_ambocclusion_toggle_button_func)
        self.animcog_mpb_antialiasing_qpushbutton.clicked.connect(self.animcog_mpb_antialiasing_toggle_button_func)
        self.animcog_mpb_vp_combobox.activated.connect(self.animcog_mpb_vp_mode_func)
        self.animcog_mpb_playblast_qpushbutton.clicked.connect(self.animcog_mpb_playblast_button)
        self.animcog_mpb_default_settings()

    # CAVEAT : AnimConglomerationUI mass_playblast vp default settings
    def animcog_mpb_default_settings(self):
        cmds.modelEditor("modelPanel4", edit=True, rendererName="vp2Renderer")
        cmds.modelEditor("modelPanel4", edit=True, displayLights="none")
        cmds.modelEditor("modelPanel4", edit=True, shadows=False)
        cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 0)
        cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 0)

    # CAVEAT : AnimConglomerationUI browse func
    def animcog_mpb_browse_button_func(self):
        self.browse_path = cmds.fileDialog2(fileFilter="Movie Files(*.mov)", dialogStyle=2)
        print "Playblast Saving Path --> %s" % self.browse_path[0]
        self.animcog_mpb_path_qlineedit.setText(self.browse_path[0])

    # CAVEAT : AnimConglomerationUI all_lights func
    def animcog_mpb_usealllights_toggle_button_func(self):
        if self.animcog_mpb_usealllights_qpushbutton.isChecked():
            cmds.modelEditor("modelPanel4", edit=True, displayLights="all")
        else:
            cmds.modelEditor("modelPanel4", edit=True, displayLights="none")

    # CAVEAT : AnimConglomerationUI shadows func
    def animcog_mpb_shadows_toggle_button_func(self):
        if self.animcog_mpb_shadows_qpushbutton.isChecked():
            cmds.modelEditor("modelPanel4", edit=True, shadows=True)
        else:
            cmds.modelEditor("modelPanel4", edit=True, shadows=False)

    # CAVEAT : AnimConglomerationUI ambient occlusion func
    def animcog_mpb_ambocclusion_toggle_button_func(self):
        if self.animcog_mpb_ambocclusion_qpushbutton.isChecked():
            cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 1)
        else:
            cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 0)

    # CAVEAT : AnimConglomerationUI antialiasing func
    def animcog_mpb_antialiasing_toggle_button_func(self):
        if self.animcog_mpb_antialiasing_qpushbutton.isChecked():
            cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
        else:
            cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 0)

    # CAVEAT : AnimConglomerationUI viewport mode func
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

    # CAVEAT : AnimConglomerationUI playblast func
    def animcog_mpb_playblast_button(self):
        self.time_slider = mel.eval("$gPlayBackSlider = $gPlayBackSlider")
        self.soundtrack_name = cmds.timeControl(self.time_slider, query=True, sound=True)
        self.default_width = cmds.getAttr("defaultResolution.width")
        self.default_height = cmds.getAttr("defaultResolution.height")
        cmds.playblast(format="qt", offScreen=True, percent=100, quality=100, filename="%s" % self.browse_path[0],
                       forceOverwrite=True, clearCache=True, viewer=True, showOrnaments=False, compression="PNG",
                       sequenceTime=False, sound=self.soundtrack_name,
                       widthHeight=[self.default_width, self.default_height])


if __name__ == "__main__":
    print "This is my Main MassPlayblastLayFunc"
else:
    print "This is MassPlayblastLayFunc"


# import anim_conglomeration.mass_playblast_lay_func
# test = mass_playblast_lay_func.MassPlayblastLayFunc()
# test.show()