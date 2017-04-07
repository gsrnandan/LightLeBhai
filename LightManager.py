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


#Create a model class for the TableView
class myModel(QtCore.QAbstractTableModel):
    
    def __init__(self,parent,lightType,header,*args):
        QtCore.QAbstractTableModel.__init__(self,parent,*args)
        self.lightType = lightType
        self.param = header
    
    def rowCount(self,parent):
        if ( self.lightType == "Maya"):
            return len(getMayaLights())
        elif (self.lightType == "Arnold"):
            return len(getArnoldLights())
        else:
            return 0
        
    def columnCount(self,parent):
        return len(getHeader())
        
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
            
        if (self.lightType == "Maya"):
            lights = getMayaLights()
        elif (self.lightType == "Arnold"):
            lights = getArnoldLights()
        return lights[index.row()]
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.param[col]
        return None
        
    
    


#Create Main Window for Maya
class MainControlWindow(QtGui.QDialog):
     
     def __init__(self, parent=None):
         
         super(MainControlWindow, self).__init__(parent)
         self.setWindowFlags(QtCore.Qt.Tool)
         self.setWindowTitle("LightLeBhai")
         self.ui =  customUI.Ui_Form()
         self.ui.setupUi(self)
         # set the maya table
         tableModelMaya = myModel(self, "Maya", header)
         self.ui.tableView.setModel(tableModelMaya)
         font = QFont("Calibri", 12)
         self.ui.tableView.setFont(font)
         # set Arnold table
         tableModelArnold = myModel(self, "Arnold", header)
         self.ui.tableView_2.setModel(tableModelArnold)
         font = QFont("Calibri", 12)
         self.ui.tableView_2.setFont(font)
         # set column width to fit contents (set font first!)
         self.ui.tableView.resizeColumnsToContents()
         self.ui.tableView_2.resizeColumnsToContents()
         # set the pushButton Functionality   
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
             cmds.confirmDialog( title='Error', message='Please select one light', button=['Ok'], defaultButton='Ok', cancelButton='Ok', dismissString='Ok' )
             print "Please select One Light"
             pass
         else:
             return lightName 
         
     def showLinkedObjects(self):
         lightName = self.getSelected()
         print lightName
         if len(lightName) < 1:
             cmds.confirmDialog( title='Error', message='Please select a light', button=['Ok'], defaultButton='Ok', cancelButton='Ok', dismissString='Ok' )
             print "Please select a light"
             pass
         else:
             objectsLinked = cmds.lightlink(q = True, light = lightName , sets = False)
             if objectsLinked:
                 cmds.select(objectsLinked,replace = True )
    
     def setLinkedObjects(self):
        lightName = self.getSelected()
        objectsLinked = cmds.lightlink( q = True, light=lightName, sets= False)
        cmds.lightlink( b=True, light=lightName, object = objectsLinked )
        objectsLinked = cmds.ls( selection = True, type = ('transform','shape') )
        cmds.lightlink( light=lightName, object = objectsLinked)
         
           
#Define the parameters
def getHeader():
    header = ['Lights','Enable','Isolate','Color','Intensity', 'Decay Rate','Shadows','Shadow Rays','Exposure','Samples','Diffuse','Specular','SSS','Indirect','Volume']
    return header        

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

# Getting Attributes 'Enable','Isolate','Color','Intensity', 'Decay Rate','Shadows','Shadow Rays','Exposure','Samples','Diffuse','Specular','SSS','Indirect','Volume'
    
    
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


    
