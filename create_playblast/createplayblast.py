
import maya.cmds as cmds

panel = mc.getPanel(withFocus=True)
mc.modelEditor(panel, edit=True, displayTextures=True)
mc.modelEditor(panel, edit=True, displayLights='all')
mc.modelEditor(panel, edit=True, shadows=True)