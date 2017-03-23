'''
Light Manager
Version 1.0: 10-03-2017
Select and edit lights and their attributes from the window
'''

import maya.cmds as cmds
from functools import partial
from PySide import QtGui, QtCore
import maya.OpenMayaUI as mui
import shiboken


#Populating the Maya Lights
def getMayaLights():
    mayaLights = cmds.ls(lights = True)
    return mayaLights


#Populating the Arnold Lights    
def getArnoldLights():
    #Checking if the arnold plugin is installed
    if 'mtoa' in cmds.moduleInfo(listModules = True):
        #Checking if the plugin is loaded
        if cmds.pluginInfo('mtoa',query = True , settings = True)[0]:
            arnoldLights = cmds.ls(exactType = ("aiAreaLight","aiPhotometricLight","aiSkyDomeLight"))
            return arnoldLights
            
    return none
     
     
#Creating a Maya Window to Append our Gui
def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer),QtGui.QWidget)
    
    
# Setting Attributes

def setIntensity(light, val):
    cmds.setAttr(light+".intensity",val)
    
def setColor(light,colorPicker,NPI):
    colorVal = cmds.colorSliderGrp(colorPicker,q= True, rgb = True)
	cmds.setAttr(light+".colorR",colorVal[0])
	cmds.setAttr(light+".colorG",colorVal[1])
	cmds.setAttr(light+".colorB",colorVal[2])
	
def setExposure(light,val):
    cmds.setAttr(light+".aiexposure",val)
    
def changeTemp(light, val):
    cmds.setAttr(light+".aiColorTemperature",val)


# Create a template attributes for each light


    