'''
Light Manager - LightLeBhai
Version 1.0: 10-03-2017
Select and edit lights and their attributes from the window
'''

import maya.cmds as cmds
from functools import partial
from PySide import QtGui, QtCore
import maya.OpenMayaUI as mui
import shiboken
import sys, pprint
from pysideuic import compileUi
pyfile = open("/homes/govindaluris/maya/scripts/lightLeBhai.py", 'w')
compileUi("/homes/govindaluris/maya/scripts/lightLeBhai.ui", pyfile, False, 4,False)
pyfile.close()
import lightLeBhai as customUI


#Create a window for Maya
def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer),QtGui.QWidget)


#Create Main Window for Maya
class MainControlWindow(QtGui.QDialog):
     
     def __init__(self, parent=None):
         
         super(MainControlWindow, self).__init__(parent)
         self.setWindowFlags(QtCore.Qt.Tool)
         
         self.setWindowTitle("LightLeBhai")
         self.ui =  customUI.Ui_Form()
         self.ui.setupUi(self)    
         self.ui.pushButton.clicked.connect(self.reloadLights)
         self.ui.pushButton_2.clicked.connect(self.refreshLights)
         self.ui.pushButton_3.clicked.connect(self.showLinkedObjects)
         self.ui.pushButton_4.clicked.connect(self.setLinkedObjects)


    
     def reloadLights(self):
            self.deleteLater()
            lightListPanel()
            
     def refreshLights(self):
         print "Hi"
         
         
     def getSelected(self):
         lightName = cmds.ls( selection=True)
         print lightName
         if len(lightName) > 1:
             print "Please select One Light"
             pass
         else:
             return lightName 
         
     def showLinkedObjects(self):
         lightName = self.getSelected()
         print lightName
         if len(lightName) < 1:
             print "Please select a light"
             pass
         else:
             objectsLinked = cmds.lightlink(q = True, light = lightName , sets = False)
             if objectsLinked:
                 cmds.select(objectsLinked,replace = True )   
                 
     def setLinkedObjects(self):
         	# get all linked objects (transforms and shapes, only. Not shadingEngines or sets. we will keep them)
	objectsRelated = cmds.lightlink( q = True, light=lightName, sets= False)
	
	# break links with those objects
	cmds.lightlink( b=True, light=lightName, object = objectsRelated )

	# get selected shapes and transforms with selected objects
	objectsRelated = cmds.ls( selection = True, type = ('transform','shape') )

	# make new links
	cmds.lightlink( light=lightName, object = objectsRelated )
         
           
          

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
        else:
            print "Arnold not loaded"
            
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

#Create a Window
def lightListPanel():
	win = MainControlWindow(parent = getMayaWindow())
	win.setWindowTitle("LightLeBhai")	
	win.show()
   
lightListPanel()    
getMayaLights()
getArnoldLights()


# Create a template attributes for each light


    
