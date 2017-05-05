# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/homes/govindaluris/Documents/light/tableView.ui'
#
# Created: Fri May  5 11:42:19 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_uiMainWindow(object):
    def setupUi(self, uiMainWindow):
        uiMainWindow.setObjectName("uiMainWindow")
        uiMainWindow.resize(697, 520)
        self.uiCentralWidget = QtGui.QWidget(uiMainWindow)
        self.uiCentralWidget.setObjectName("uiCentralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.uiCentralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTable = QtGui.QTableView(self.uiCentralWidget)
        self.uiTable.setObjectName("uiTable")
        self.verticalLayout.addWidget(self.uiTable)
        uiMainWindow.setCentralWidget(self.uiCentralWidget)

        self.retranslateUi(uiMainWindow)
        QtCore.QMetaObject.connectSlotsByName(uiMainWindow)

    def retranslateUi(self, uiMainWindow):
        uiMainWindow.setWindowTitle(QtGui.QApplication.translate("uiMainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

