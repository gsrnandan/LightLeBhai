'''
Light Manager - LightLeBhai
Version 1.0: 10-03-2017
Select and edit lights and their attributes from the window
'''

import maya.cmds as cmds
from functools import partial
import operator
from PySide.QtCore import *
from PySide.QtGui import *
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

#Create a Class for the light objects

class mayaLightNodes():
    
    def __init__(self,lightType,header,lightName):
        self.lightType = lightType
        self.lightName = lightName

#Light Intensity     
    def setIntensity(val):
        cmds.setAttr(self.lightName+".intensity",val)
    def getIntensity():
        return cmds.setAttr(self.lightName+".intensity")
        
#Color Value of the Light'''    
    def setColor(light,colorPicker,NPI):
        colorVal = cmds.colorSliderGrp(colorPicker,q= True, rgb = True)
        cmds.setAttr(light+".colorR",colorVal[0])
        cmds.setAttr(light+".colorG",colorVal[1])
        cmds.setAttr(light+".colorB",colorVal[2])    
    def getColor(light):
        lightColor = []
        lightColor[0] = cmds.getAttr(light+".colorR")
        lightColor[1] = cmds.getAttr(light+".colorG")
        lightColor[2] = cmds.getAttr(light+".colorB")
        return lightColor
        
#Enable and Disable Lights'''    
    def enableLight():
        pass        
    def disableLight():
        pass

#Isolate and integrate Lights'''        
    def isolateLight():
        pass        
    def integrateLight():
        pass
    
#Decay Rate for Lights'''    
    def setDecayRate(val):
        cmds.setAttr(self.lightName+".decayRate",val)        
    def getDecayRate():
        return cmds.getAttr(self.lightName+".decayRate")
        
#Use Ray Trace Shadows for Lights'''
    def setRayTraceShadow():
        cmds.setAttr(self.lightName+".useRayTraceShadows",1)
    def unsetRayTraceShadows():
        cmds.setAttr(self.lightName+".useRayTraceShadows",0)
        
#Setting the number of Shadow Rays'''
    def setShadowRays(val):
        cmds.setAttr(self.lightName+".shadowRays",val)
    def getShadowRays():
        return cmds.getAttr(self.lightName+".shadowRays")
        
#Setting the Exposure of the lights'''
    def setExposure(val):
        cmds.setAttr(self.lightName+".exposure",val)
    def getExposure():
        return cmds.getAttr(self.lightName+".exposure")
        
#Setting the aiSamples'''
    def setAiSamples(val):
        cmds.setAttr(self.lightName+".aiSamples",val)
    def getAiSamples():
        cmds.getAttr(self.lightName+".aiSamples")
        
#Getting and Setting the Diffuse,Specular,SSS,Indirect and Volume Samples'''

    def setDiffuseSamples(val):
        cmds.setAttr(self.lightName+".aiDiffuse",val)
    def setSpecularSamples(val):
        cmds.setAttr(self.lightName+".aiSpecular",val)
    def setSSSSamples(val):
        cmds.setAttr(self.lightName+".aiSss",val)
    def setIndirectSamples(val):
        cmds.setAttr(self.lightName+".aiIndirect",val)
    def setVolumeSamples(val):
        cmds.setAttr(self.lightName+".aiVolume",val)
        
    def getDiffuseSamples():
        return cmds.getAttr(self.lightName+".aiDiffuse")
    def getSpecularSamples():
        return cmds.getAttr(self.lightName+".aiSpecular")
    def getSSSSamples(val):
        return cmds.getAttr(self.lightName+".aiSss")
    def getIndirectSamples(val):
        return cmds.getAttr(self.lightName+".aiIndirect")
    def getVolumeSamples(val):
        return cmds.getAttr(self.lightName+".aiVolume")
            
                     
#Create a class for Arnold Lights
class arnoldLightNodes():
    
    def __init__(self,lightType,header,lightName):
        self.lightType = lightType
        self.lightName = lightName

#Light Intensity'''
    def setIntensity(val):
        cmds.setAttr(self.lightName+".intensity",val)    
    def getIntensity():
        return cmds.setAttr(self.lightName+".intensity")
        
#Color Value of the Light'''    
    def setColor(light,colorPicker,NPI):
        colorVal = cmds.colorSliderGrp(colorPicker,q= True, rgb = True)
        cmds.setAttr(light+".colorR",colorVal[0])
        cmds.setAttr(light+".colorG",colorVal[1])
        cmds.setAttr(light+".colorB",colorVal[2])    
    def getColor(light):
        lightColor = []
        lightColor[0] = cmds.getAttr(light+".colorR")
        lightColor[1] = cmds.getAttr(light+".colorG")
        lightColor[2] = cmds.getAttr(light+".colorB")
        return lightColor
        
#Enable and Disable Lights'''    
    def enableLight():
        cmds.setAttr(self.lightName+".visibility",1)       
    def disableLight():
        cmds.setAttr(self.lightName+".visibility",0)

#Isolate and integrate Lights'''        
    def isolateLight():
        cmds.setAttr(self.lightName+".visibility",1)       
    def integrateLight():
        cmds.setAttr(self.lightName+".visibility",0)
    
#Decay Type for aiLights'''    
    def setDecayRate(val):
        cmds.setAttr(self.lightName+".aiDecayType",val)        
    def getDecayRate():
        return cmds.getAttr(self.lightName+".aiDecayType")
        
#Use Cast Shadows for Lights'''
    def setCastShadows():
        cmds.setAttr(self.lightName+".aiCastShadows",1)
    def unsetCastShadows():
        cmds.setAttr(self.lightName+".aiCastShadows",0)

#Affect Volumetrics for aiLights'''
    def setAffectVolumetrics():
        cmds.setAttr(self.lightName+".aiAffectVolumetrics",1)
    def unsetAffectVolumetrics():
        cmds.setAttr(self.lightName+".aiAffectVolumetrics",0)        

#Affect Cast Volumetric Shadows'''
    def setVolumetricCastShadows():
        cmds.setAttr(self.lightName+".aiCastVolumetricShadows",1)
    def unsetVolumetricCastShadows():
        cmds.setAttr(self.lightName+".aiCastVolumetricShadows",0)
        
#Setting the Exposure of the lights'''
    def setExposure(val):
        cmds.setAttr(self.lightName+".aiExposure",val)
    def getExposure():
        return cmds.getAttr(self.lightName+".aiExposure")
        
#Setting the aiSamples'''
    def setAiSamples(val):
        cmds.setAttr(self.lightName+".aiSamples",val)
    def getAiSamples():
        cmds.getAttr(self.lightName+".aiSamples")
        
#Getting and Setting the Diffuse,Specular,SSS,Indirect and Volume Samples'''

    def setDiffuseSamples(val):
        cmds.setAttr(self.lightName+".aiDiffuse",val)
    def setSpecularSamples(val):
        cmds.setAttr(self.lightName+".aiSpecular",val)
    def setSSSSamples(val):
        cmds.setAttr(self.lightName+".aiSss",val)
    def setIndirectSamples(val):
        cmds.setAttr(self.lightName+".aiIndirect",val)
    def setVolumeSamples(val):
        cmds.setAttr(self.lightName+".aiVolume",val)
        
    def getDiffuseSamples():
        return cmds.getAttr(self.lightName+".aiDiffuse")
    def getSpecularSamples():
        return cmds.getAttr(self.lightName+".aiSpecular")
    def getSSSSamples(val):
        return cmds.getAttr(self.lightName+".aiSss")
    def getIndirectSamples(val):
        return cmds.getAttr(self.lightName+".aiIndirect")
    def getVolumeSamples(val):
        return cmds.getAttr(self.lightName+".aiVolume")
            

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
        return len(self.param)
        
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
        
    
#Create different Widgets for each attribute
'''CheckBoxes for Isolate and Enable'''



#Create Main Window for Maya
class MainControlWindow(QtGui.QDialog):
     
     def __init__(self, parent=None):
         
         super(MainControlWindow, self).__init__(parent)
         self.setWindowFlags(QtCore.Qt.Tool)
         self.setWindowTitle("LightLeBhai")
         self.ui =  customUI.Ui_Form()
         self.ui.setupUi(self)
         # set the maya table
         mayaHeader = getMayaHeader()
         tableModelMaya = myModel(self, "Maya", mayaHeader)
         self.ui.tableView.setModel(tableModelMaya)
         font = QtGui.QFont("Calibri", 12)
         self.ui.tableView.setFont(font)
         # set Arnold table
         arnoldHeader = getArnoldHeader()
         tableModelArnold = myModel(self, "Arnold", arnoldHeader)
         self.ui.tableView_2.setModel(tableModelArnold)
         font = QtGui.QFont("Calibri", 12)
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
def getMayaHeader():
    mayaHeader = ['Lights','Enable','Isolate','Color','Intensity', 'Decay Rate','Shadows','Shadow Rays','Exposure','Samples','Diffuse','Specular','SSS','Indirect','Volume']
    return mayaHeader
    
def getArnoldHeader():
    arnoldHeader = ['Lights','Enable','Isolate','Color','Intensity', 'Decay Rate','Cast Shadows','Affect Volumetrics','Cast Volumetric Shadows', 'Exposure','Samples','Diffuse','Specular','SSS','Indirect','Volume']
    return arnoldHeader        

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
    
    
# Getting and Setting Attributes


    

	
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


    
