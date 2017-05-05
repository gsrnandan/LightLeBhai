import maya.cmds as cmds
from functools import partial
import operator
from PySide import QtCore
from PySide import QtGui
import maya.OpenMayaUI as mui
import shiboken
import sys, pprint
import maya.OpenMaya as OpenMaya
from pysideuic import compileUi
pyfile = open("/homes/govindaluris/Documents/light/tableView.py", 'w')
compileUi("/homes/govindaluris/Documents/light/tableView.ui", pyfile, False, 4,False)
pyfile.close()
import tableView as customUI


table = [[1,2,3],[4,5,6],[7,8,9]]

def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer),QtGui.QWidget)
    

def getTable():
    return table

def getHeader():
    header = ["Pallete0", "Colors", "Brushes"]
    return header 
    
class MainControlWindow(QtGui.QMainWindow):

      
     def __init__(self, parent=None):
         
         super(MainControlWindow, self).__init__(parent)
         self.setWindowFlags(QtCore.Qt.Tool)         
         self.ui =  customUI.Ui_uiMainWindow()
         self.ui.setupUi(self)
         self.table = [[1,2,3],[4,5,6],[7,8,9]]
         self.model = PaletteTableModel(self.table,getHeader())
         self.ui.uiTable.setModel(self.model)
         font = QtGui.QFont("Calibri", 12)
         self.ui.uiTable.setFont(font)
         
         
     def closeEvent(self, event):
         deleteCallBacks()     
         
         
class PaletteTableModel(QtCore.QAbstractTableModel):
    
    def __init__(self, table = [[]], headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__table = table
        self.__headers = headers



    def rowCount(self, parent):
        return len(self.__table)
    
    
    def columnCount(self, parent):
        return len(self.__table[0])


    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


    def data(self, index, role):
        
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.__table[row][column]
        
        
        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return  self.__table[row][column]
        
              
        if role == QtCore.Qt.DisplayRole:
            
            row = index.row()
            column = index.column()
            value = self.__table[row][column]
            return value


    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            
            row = index.row()
            column = index.column()            
            self.__table[row][column] = value
            self.dataChanged.emit(row, column)
            cmds.setAttr('pointLightShape1'+".intensity",value)
            return True





    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                
                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "not implemented"
            else:
                return "Wassup"
                
                
def deleteCallBacks():
    for callback in callBacks:
        OpenMaya.MMessage.removeCallback( callback )

callBacks = []                      

def updateTable(*args,**Kwargs):
    val = cmds.getAttr(' pointLightShape1'+ ".intensity")
    win.model.layoutAboutToBeChanged.emit()
    win.table[0][0] = val
    win.table[2][2] = val
    win.model.layoutChanged.emit()


if __name__ == '__main__':
        
    pointer = mui.MQtUtil.mainWindow()
    win = MainControlWindow(parent = shiboken.wrapInstance(long(pointer),QtGui.QWidget))
    win.setWindowTitle("LightLeBhai")
    win.show()
    print win.table
    
    selectionList = OpenMaya.MSelectionList()
    selectionList.add( ' pointLightShape1'  )
    node = OpenMaya.MObject()
    selectionList.getDependNode( 0, node )
    callBacks.append(OpenMaya.MNodeMessage.addAttributeChangedCallback( node, updateTable))
    
    

    
    