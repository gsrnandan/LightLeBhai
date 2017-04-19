'''
Light Manager - LightLeBhai
Version 1.0: 10-03-2017
Select and edit lights and their attributes from the window
'''

import maya.cmds as cmds
from functools import partial
import operator
from PySide import QtCore
from PySide import QtGui
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
        self.header = header
        self.attrValues = self.populateDictionary()

    def populateDictionary(self):
        attrValues =  {}
        for attr in self.header:
            attr = attr.replace(" ","")
            if attr.lower() == "intensity":
                attrValues[attr.lower()] = self.getIntensity()
            elif attr.lower() == "color":
                attrValues[attr.lower()] = list()
                attrValues[attr.lower()].append(self.getColor())
            elif attr.lower() == "enable":
                attrValues[attr.lower()] = self.getEnableState()                
            elif attr.lower() == "isolate":
                attrValues[attr.lower()] = self.getEnableState()                   
            elif attr.lower() == "decayrate":
                attrValues[attr.lower()] = self.getDecayRate()
            elif attr.lower() == "decaytype":
                attrValues[attr.lower()] = self.getDecayType()    
            elif attr.lower() == "shadows":
                attrValues[attr.lower()] = self.getShadowsState()                   
            elif attr.lower() == "shadowrays":
                attrValues[attr.lower()] = self.getShadowRays()                   
            elif attr.lower() == "exposure":
                attrValues[attr.lower()] = self.getExposure()                   
            elif attr.lower() == "samples":
                attrValues[attr.lower()] = self.getAiSamples()                   
            elif attr.lower() == "diffuse":
                attrValues[attr.lower()] = self.getDiffuseSamples() 
            elif attr.lower() == "specular":
                attrValues[attr.lower()] = self.getSpecularSamples()                   
            elif attr.lower() == "sss":
                attrValues[attr.lower()] = self.getSSSSamples()
            elif attr.lower() == "indirect":
                attrValues[attr.lower()] = self.getIndirectSamples()
            elif attr.lower() == "volume":
                attrValues[attr.lower()] = self.getVolumeSamples()
            elif attr.lower() == "lights":
                attrValues[attr.lower()] = self.lightName                
        return attrValues                                                      

    def __getattr__(self,attr):
        attr = attr.replace(" ","")
        try:
            return self.attrValues[attr.lower()]
        except:
            print "Maya Attribute not found"                                 
                
#Light Intensity     
    def setIntensity(self,val):
        if cmds.attributeQuery( 'intensity', node=self.lightName, ex = True ):
            cmds.setAttr(self.lightName+".intensity",val)
        else:
            pass
    def getIntensity(self):
        if cmds.attributeQuery( 'intensity', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".intensity")
        else:
            return "NA"
            
        
        
#Color Value of the Light'''    
    def setColor(self,light,colorPicker,NPI):
        colorVal = cmds.colorSliderGrp(colorPicker,q= True, rgb = True)
        cmds.setAttr(light+".colorR",colorVal[0])
        cmds.setAttr(light+".colorG",colorVal[1])
        cmds.setAttr(light+".colorB",colorVal[2])    
    def getColor(self):
        lightColor = []
        lightColor.append(cmds.getAttr(self.lightName+".colorR"))
        lightColor.append(cmds.getAttr(self.lightName+".colorG"))
        lightColor.append(cmds.getAttr(self.lightName+".colorB"))
        return lightColor
        
#Enable and Disable Lights'''    
    def enableLight(self):
        cmds.setAttr(self.lightName+".visibility",1)
        return 1        
    def disableLight(self):
        cmds.setAttr(self.lightName+".visibility",0)
        return 0
    def getEnableState(self):
        val = cmds.getAttr(self.lightName+".visibility")
        if val:
            return True
        else:
            return False

#Isolate and integrate Lights'''        
    def isolateLight(self):
        cmds.setAttr(self.lightName+".visibility",1)
        return 1        
    def integrateLight(self):
        cmds.setAttr(self.lightName+".visibility",0)
        return 0
    
#Decay Rate for Lights'''    
    def setDecayRate(self,val):
        cmds.setAttr(self.lightName+".decayRate",val)        
    def getDecayRate(self):
        if cmds.attributeQuery( 'decayRate', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".decayRate")
        else:
            return "NA"
        
#Use Ray Trace Shadows for Lights'''
    def setRayTraceShadow(self):
        cmds.setAttr(self.lightName+".useRayTraceShadows",1)
    def unsetRayTraceShadows(self):
        cmds.setAttr(self.lightName+".useRayTraceShadows",0)
    def getShadowsState(self):
        if cmds.attributeQuery( 'useRayTraceShadows', node=self.lightName, ex = True ):
            val = cmds.getAttr(self.lightName+".useRayTraceShadows")
            if val:
                return True
            else:
                return False
        else:
            return "NA"
        
#Setting the number of Shadow Rays'''
    def setShadowRays(self,val):
        cmds.setAttr(self.lightName+".shadowRays",val)
    def getShadowRays(self):
        if cmds.attributeQuery( 'shadowRays', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".shadowRays")
        else:
            return "NA"
        
        
#Setting the Exposure of the lights'''
    def setExposure(self,val):
        cmds.setAttr(self.lightName+".exposure",val)
    def getExposure(self):
        if cmds.attributeQuery( 'exposure', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".exposure")
        elif cmds.attributeQuery( 'aiExposure', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiExposure")
        else:
            return "NA"

#Decay Type for Lights'''    
    def setDecayType(self,val):
        cmds.setAttr(self.lightName+".aiDecayType",val)        
    def getDecayType(self):
        if cmds.attributeQuery( 'aiDecayType', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiDecayType")
        else:
            return "NA"        
        
#Setting the aiSamples'''
    def setAiSamples(self,val):
        cmds.setAttr(self.lightName+".aiSamples",val)
    def getAiSamples(self):
        if cmds.attributeQuery( "aiSamples", node = self.lightName , ex = True ):
            return cmds.getAttr(self.lightName+".aiSamples")
        else:
            return "NA"
        
#Getting and Setting the Diffuse,Specular,SSS,Indirect and Volume Samples'''

    def setDiffuseSamples(self,val):
        cmds.setAttr(self.lightName+".aiDiffuse",val)
    def setSpecularSamples(self,val):
        cmds.setAttr(self.lightName+".aiSpecular",val)
    def setSSSSamples(self,val):
        cmds.setAttr(self.lightName+".aiSss",val)
    def setIndirectSamples(self,val):
        cmds.setAttr(self.lightName+".aiIndirect",val)
    def setVolumeSamples(self,val):
        cmds.setAttr(self.lightName+".aiVolume",val)
        
    def getDiffuseSamples(self):
        if cmds.attributeQuery( 'aiDiffuse', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiDiffuse")
        else:
            return "NA"
    def getSpecularSamples(self):
        if cmds.attributeQuery( 'aiSpecular', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiSpecular")
        else:
            return "NA"
    def getSSSSamples(self):
        if cmds.attributeQuery( 'aiSss', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiSss")
        else:
            return "NA"
    def getIndirectSamples(self):
        if cmds.attributeQuery( 'aiIndirect', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiIndirect")
        else:
            return "NA"
    def getVolumeSamples(self):
        if cmds.attributeQuery( 'aiVolume', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiVolume")
        else:
            return "NA"
            
                     
#Create a class for Arnold Lights
class arnoldLightNodes():
    
    def __init__(self,lightType,header,lightName):
        self.lightType = lightType
        self.lightName = lightName
        self.header = header
        self.attrValues = self.populateDictionary()
    
    def populateDictionary(self):
        attrValues =  {}
        for attr in self.header:
            attr = attr.replace(" ","")
            if attr.lower() == "intensity":
                attrValues[attr.lower()] = self.getIntensity()
            elif attr.lower() == "color":
                attrValues[attr.lower()] = list()
                attrValues[attr.lower()].append(self.getColor())
            elif attr.lower() == "enable":
                attrValues[attr.lower()] = self.getEnableState()                
            elif attr.lower() == "isolate":
                attrValues[attr.lower()] = self.getEnableState()                   
            elif attr.lower() == "decaytype":
                attrValues[attr.lower()] = self.getDecayType()   
            elif attr.lower() == "castshadows":
                attrValues[attr.lower()] = self.getCastShadowsState()                   
            elif attr.lower() == "affectvolumetrics":
                attrValues[attr.lower()] = self.getAffectVolumetricsState()
            elif attr.lower() == "castvolumetricshadows":
                attrValues[attr.lower()] = self.getCastVolumetricShadowsState()                                  
            elif attr.lower() == "exposure":
                attrValues[attr.lower()] = self.getExposure()                   
            elif attr.lower() == "samples":
                attrValues[attr.lower()] = self.getAiSamples()                   
            elif attr.lower() == "diffuse":
                attrValues[attr.lower()] = self.getDiffuseSamples() 
            elif attr.lower() == "specular":
                attrValues[attr.lower()] = self.getSpecularSamples()                   
            elif attr.lower() == "sss":
                attrValues[attr.lower()] = self.getSSSSamples()
            elif attr.lower() == "indirect":
                attrValues[attr.lower()] = self.getIndirectSamples()
            elif attr.lower() == "volume":
                attrValues[attr.lower()] = self.getVolumeSamples()
            elif attr.lower() == "lights":
                attrValues[attr.lower()] = self.lightName              
        return attrValues        
    
    def __getattr__(self,attr):
        attr = attr.replace(" ","")
        try:
            return self.attrValues[attr.lower()]
        except:
            print "Arnold Attribute not found"
                   

#Light Intensity     
    def setIntensity(self,val):
        if cmds.attributeQuery( 'intensity', node=self.lightName, ex = True ):
            cmds.setAttr(self.lightName+".intensity",val)
        else:
            pass
    def getIntensity(self):
        if cmds.attributeQuery( 'intensity', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".intensity")
        else:
            return "NA"
            
        
        
#Color Value of the Light'''    
    def setColor(self,light,colorPicker,NPI):
        colorVal = cmds.colorSliderGrp(colorPicker,q= True, rgb = True)
        cmds.setAttr(light+".colorR",colorVal[0])
        cmds.setAttr(light+".colorG",colorVal[1])
        cmds.setAttr(light+".colorB",colorVal[2])    
    def getColor(self):
        lightColor = []
        lightColor.append(cmds.getAttr(self.lightName+".colorR"))
        lightColor.append(cmds.getAttr(self.lightName+".colorG"))
        lightColor.append(cmds.getAttr(self.lightName+".colorB"))
        return lightColor
        
#Enable and Disable Lights'''    
    def enableLight(self):
        cmds.setAttr(self.lightName+".visibility",1)
        return 1        
    def disableLight(self):
        cmds.setAttr(self.lightName+".visibility",0)
        return 0
    def getEnableState(self):
        val = cmds.getAttr(self.lightName+".visibility")
        if val:
            return True
        else:
            return False

#Isolate and integrate Lights'''        
    def isolateLight(self):
        cmds.setAttr(self.lightName+".visibility",1)
        return 1        
    def integrateLight(self):
        cmds.setAttr(self.lightName+".visibility",0)
        return 0
    
#Decay Type for aiLights'''    
    def setDecayType(self,val):
        cmds.setAttr(self.lightName+".aiDecayType",val)        
    def getDecayType(self):
        if cmds.attributeQuery( 'aiDecayType', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiDecayType")
        else:
            return "NA"
                    
        
#Use Cast Shadows for Lights'''
    def setCastShadows(self):
        cmds.setAttr(self.lightName+".aiCastShadows",1)
    def unsetCastShadows(self):
        cmds.setAttr(self.lightName+".aiCastShadows",0)
    def getCastShadowsState(self):
        if cmds.attributeQuery( 'aiCastShadows', node=self.lightName, ex = True ):
            val = cmds.getAttr(self.lightName+".aiCastShadows")
            if val:
                return True
            else:
                return False
        else:
            return "NA"        

#Affect Volumetrics for aiLights'''
    def setAffectVolumetrics(self):
        cmds.setAttr(self.lightName+".aiAffectVolumetrics",1)
    def unsetAffectVolumetrics(self):
        cmds.setAttr(self.lightName+".aiAffectVolumetrics",0)
    def getAffectVolumetricsState(self):
        if cmds.attributeQuery( 'aiAffectVolumetrics', node=self.lightName, ex = True ):
            val = cmds.getAttr(self.lightName+".aiAffectVolumetrics")
            if val:
                return True
            else:
                return False
        else:
            return "NA"                 

#Affect Cast Volumetric Shadows'''
    def setVolumetricCastShadows(self):
        cmds.setAttr(self.lightName+".aiCastVolumetricShadows",1)
    def unsetVolumetricCastShadows(self):
        cmds.setAttr(self.lightName+".aiCastVolumetricShadows",0)
    def getCastVolumetricShadowsState(self):
        if cmds.attributeQuery( 'aiCastVolumetricShadows', node=self.lightName, ex = True ):
            val = cmds.getAttr(self.lightName+".aiCastVolumetricShadows")
            if val:
                return True
            else:
                return False
        else:
            return "NA"         
        
#Setting the Exposure of the lights'''
    def setExposure(self,val):
        cmds.setAttr(self.lightName+".aiExposure",val)
    def getExposure(self):
        if cmds.attributeQuery( 'aiExposure', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiExposure")
        else:
            return "NA"
        
#Setting the aiSamples'''
    def setAiSamples(self,val):
        cmds.setAttr(self.lightName+".aiSamples",val)
    def getAiSamples(self):
        if cmds.attributeQuery( "aiSamples", node = self.lightName , ex = True ):
            return cmds.getAttr(self.lightName+".aiSamples")
        else:
            return "NA"
        
#Getting and Setting the Diffuse,Specular,SSS,Indirect and Volume Samples'''

    def setDiffuseSamples(self,val):
        cmds.setAttr(self.lightName+".aiDiffuse",val)
    def setSpecularSamples(self,val):
        cmds.setAttr(self.lightName+".aiSpecular",val)
    def setSSSSamples(self,val):
        cmds.setAttr(self.lightName+".aiSss",val)
    def setIndirectSamples(self,val):
        cmds.setAttr(self.lightName+".aiIndirect",val)
    def setVolumeSamples(self,val):
        cmds.setAttr(self.lightName+".aiVolume",val)
        
    def getDiffuseSamples(self):
        if cmds.attributeQuery( 'aiDiffuse', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiDiffuse")
        else:
            return "NA"
    def getSpecularSamples(self):
        if cmds.attributeQuery( 'aiSpecular', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiSpecular")
        else:
            return "NA"
    def getSSSSamples(self):
        if cmds.attributeQuery( 'aiSss', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiSss")
        else:
            return "NA"
    def getIndirectSamples(self):
        if cmds.attributeQuery( 'aiIndirect', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiIndirect")
        else:
            return "NA"
    def getVolumeSamples(self):
        if cmds.attributeQuery( 'aiVolume', node=self.lightName, ex = True ):
            return cmds.getAttr(self.lightName+".aiVolume")
        else:
            return "NA"
            

#Create a model class for the TableView
class myModel(QAbstractTableModel):
    
    def __init__(self,parent,lightType,header,lights,*args):
        QAbstractTableModel.__init__(self,parent,*args)
        self.lightType = lightType
        self.param = header
        self.lights = lights
    
    def rowCount(self,parent):
        if ( self.lightType == "Maya"):
            return len(self.lights)
        elif (self.lightType == "Arnold"):
            return len(self.lights)
        else:
            return 0
        
    def columnCount(self,parent):
        return len(self.param)
        
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
    
        attr = self.param[index.column()]
        custom = getCustomWidgetAttrs()
        bool = False
        for val in custom:
            if val == attr:
                bool = True
                
        if bool:
            return None
        else:
            return self.lights[index.row()].__getattr__(attr)        
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.param[col]
        return None
        
    
#Create different Widgets for each attribute
'''ComboBoxes for Isolate and Enable'''
class comboDelegate(QtGui.QItemDelegate):
    
    def __init__(self,parent,comboList,view):
        QtGui.QItemDelegate.__init__(self, parent)
        self.comboList = comboList
        self.tableView = view
        
    def createEditor(self,parent,option,index):
        editor = QtGui.QComboBox(parent)
        editor.addItems(self.comboList)  
        return editor
        
    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        if value:
            editor.setCurrentIndex(int(value))
        
    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentIndex(), QtCore.Qt.EditRole)
        
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        
    def paint(self, painter, option, index):
        text = self.comboList[index.row()]
        option.text = text
        QtGui.QApplication.style().drawControl(QtGui.QStyle.CE_ItemViewItem, option, painter)    
                

#Create Main Window for Maya
class MainControlWindow(QDialog):
     
     def __init__(self, parent=None):
         
         super(MainControlWindow, self).__init__(parent)
         self.setWindowFlags(Qt.Tool)
         self.setWindowTitle("LightLeBhai")
         self.ui =  customUI.Ui_Form()
         self.ui.setupUi(self)
         #Create the light Instances
         self.mayaLights = self.createMayaLightInstances()
         self.arnoldLights = self.createArnoldLightInstances()
         # set the maya table
         mayaHeader = getMayaHeader()
         tableModelMaya = myModel(self, "Maya", mayaHeader,self.mayaLights)
         self.ui.tableView.setModel(tableModelMaya)
         font = QFont("Calibri", 12)
         self.ui.tableView.setFont(font)
         
         #combo for decayRate 
         decayRateCombo = comboDelegate(self,getDecayRateCombo(),self.ui.tableView)
         self.ui.tableView.setItemDelegateForColumn(getColumnNumber(mayaHeader,'decayrate'), decayRateCombo)
         for row in range(0,tableModelMaya.rowCount(self)):
             self.ui.tableView.openPersistentEditor(tableModelMaya.index(row,getColumnNumber(mayaHeader,'decayrate'))) 
             
         #Combo for decayType
         decayTypeCombo = comboDelegate(self,getDecayTypeCombo(),self.ui.tableView)
         self.ui.tableView.setItemDelegateForColumn(getColumnNumber(mayaHeader,'decaytype'), decayTypeCombo)
         for row in range(0,tableModelMaya.rowCount(self)):
             self.ui.tableView.openPersistentEditor(tableModelMaya.index(row,getColumnNumber(mayaHeader,'decaytype')))                 

         # set Arnold table
         arnoldHeader = getArnoldHeader()
         tableModelArnold = myModel(self, "Arnold", arnoldHeader,self.arnoldLights)
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

     #Create the lightNodes
     def createMayaLightInstances(self):
         mayaLights = []
         Lights = cmds.ls(lights = True)
         for i in range(len(Lights)):
             mayaLights.append(mayaLightNodes("Maya",getMayaHeader(),Lights[i]))
         return mayaLights
         
     def createArnoldLightInstances(self):
         #Checking if the arnold plugin is installed
         arnoldLights = []
         if 'mtoa' in cmds.moduleInfo(listModules = True):
             #Checking if the plugin is loaded
             if cmds.pluginInfo('mtoa',query = True , settings = True)[0]:
                 Lights = cmds.ls(exactType = ("aiAreaLight","aiPhotometricLight","aiSkyDomeLight"))
                 for i in range(len(Lights)):
                     arnoldLights.append(arnoldLightNodes("Arnold",getArnoldHeader(),Lights[i]))
                 return arnoldLights
             else:
                 print "Arnold not loaded"
                    
         return none
    
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
    mayaHeader = ['Lights','Enable','Isolate','Color','Intensity', 'Decay Rate','Decay Type','Shadows','Shadow Rays','Exposure','Samples','Diffuse','Specular','SSS','Indirect','Volume']
    #mayaHeader = ['Lights','Intensity', 'Decay Rate']
    return mayaHeader
    
def getArnoldHeader():
    arnoldHeader = ['Lights','Enable','Isolate','Color','Intensity', 'Decay Type','Cast Shadows','Affect Volumetrics','Cast Volumetric Shadows', 'Exposure','Samples','Diffuse','Specular','SSS','Indirect','Volume']
    #arnoldHeader = ['Lights','Intensity', 'Decay Type','Cast Volumetric Shadows','Volume']
    return arnoldHeader        

def getColumnNumber(header,attr):
    for head in header:
        var = head.replace(" ","")
        var = var.lower()
        if var == attr:
            coloumn = header.index(head)
    return coloumn   

#define list of custom widget cells
def getCustomWidgetAttrs():
    list = ['Decay Rate','Decay Type']
    return list

 
#Define the list for the ComboBox
#Decay Rate
def getDecayRateCombo():
    list = ['No decay','Linear','Quadratic','Cubic']
    return list

#Decay Type
def getDecayTypeCombo():
    list = ['Quadratic','Constant']
    return list    
     
#Creating a Maya Window to Append our Gui
def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer),QWidget)

#Create a Window
def lightListPanel():
	win = MainControlWindow(parent = getMayaWindow())
	win.setWindowTitle("LightLeBhai")	
	win.show()
   
lightListPanel()    



# Create a template attributes for each light


    
