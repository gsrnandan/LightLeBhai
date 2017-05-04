from PySide import QtGui  
from PySide import QtCore
from PySide import QtUiTools
import pysideuic
import maya.OpenMayaUI as mui
import shiboken
import xml.etree.ElementTree as xml
from cStringIO import StringIO

def loadUiType(uiFile):
	    """
	    Pyside lacks the "loadUiType" command, so we have to convert the ui file to py code in-memory first
	    and then execute it in a special frame to retrieve the form_class.
	    """
	    parsed = xml.parse(uiFile)
	    widget_class = parsed.find('widget').get('class')
	    form_class = parsed.find('class').text
	
	    with open(uiFile, 'r') as f:
	    	o = StringIO()
	    	frame = {}
			
	    	pysideuic.compileUi(f, o, indent=0)
	    	pyc = compile(o.getvalue(), '<string>', 'exec')
	    	exec pyc in frame
			
	    	#Fetch the base_class and form class based on their type in the xml from designer
	    	form_class = frame['Ui_%s'%form_class]
	    	base_class = eval('QtGui.%s'%widget_class)
	    return form_class, base_class

class WndTutorial05(base, form):
    
    def __init__(self, parent=None):
        super(base, self).__init__(parent)
        self.setupUi(self)


class MainControlWindow(QtGui.QDialog):
     
     def __init__(self, parent=None):
         
         super(MainControlWindow, self).__init__(parent)
         tableView = QtGui.QTableView()

base, form = loadUiType("/homes/govindaluris/Documents/light/tableView.ui")

if __name__ == '__main__':
     
          
    pointer = mui.MQtUtil.mainWindow()    
    win = WndTutorial05()
    win.setWindowTitle("LightLeBhai")
    win.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    win.show()
    

    