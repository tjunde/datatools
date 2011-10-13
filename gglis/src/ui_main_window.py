# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Jul 21 15:46:35 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
from default_canvas_widget import CanvasWidget
from qgis.core import *
from qgis.gui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/default/images/application.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.mapCanvas = CanvasWidget(self.centralwidget)
        self.mapCanvas.setBaseSize(QtCore.QSize(0, 0))
        self.mapCanvas.setObjectName("mapCanvas")
        self.mainLayout.addWidget(self.mapCanvas)
        self.consoleLayout = QtGui.QHBoxLayout()
        self.consoleLayout.setObjectName("consoleLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.consoleLayout.addWidget(self.label)
        self.quickComboBox = QtGui.QComboBox(MainWindow)
        self.quickComboBox.setObjectName("quickComboBox")		
        self.consoleLayout.addWidget(self.quickComboBox)
        self.sqlConsole = QtGui.QLineEdit(self.centralwidget)
        self.sqlConsole.setObjectName("sqlConsole")
        self.consoleLayout.addWidget(self.sqlConsole)
        self.runSqlButton = QtGui.QPushButton(self.centralwidget)
        self.runSqlButton.setObjectName("runSqlButton")
        self.consoleLayout.addWidget(self.runSqlButton)
        self.mainLayout.addLayout(self.consoleLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.quickView = QtGui.QMenu(self.menubar)
        self.quickView.setObjectName("quickView")
        self.menuStatistics = QtGui.QMenu(self.menubar)
        self.menuStatistics.setObjectName("menuStatistics")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/default/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon2)
        self.actionClose.setObjectName("actionClose")
        self.actionZoomIn = QtGui.QAction(MainWindow)
        self.actionZoomIn.setCheckable(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/default/images/in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon3)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/default/images/out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon4)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionFullExten = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/default/images/extent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullExten.setIcon(icon5)
        self.actionFullExten.setObjectName("actionFullExten")
        self.actionZoomPan = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/default/images/pan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomPan.setIcon(icon6)
        self.actionZoomPan.setObjectName("actionZoomPan")
        self.actionAttribute = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/default/images/attribute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAttribute.setIcon(icon7)
        self.actionAttribute.setObjectName("actionAttribute")
        self.actionIdenty = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/default/images/identy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIdenty.setIcon(icon13)
        self.actionIdenty.setObjectName("actionIdenty")

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/default/images/statis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatisType = QtGui.QAction(MainWindow)
        self.actionStatisType.setIcon(icon8)
        self.actionStatisType.setObjectName("actionStatisType")


        self.menuBasinStatis = QtGui.QMenu(self.menuStatistics)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/default/images/trans.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBasinStatis.setIcon(icon9)
        self.menuBasinStatis.setObjectName("menuBasinStatis")

        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/default/images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/default/images/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(icon10)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setIcon(icon11)
        self.actionHelp.setObjectName("actionHelp")

        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/default/images/layers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLayers = QtGui.QAction(MainWindow)
        self.actionLayers.setIcon(icon12)
        self.actionLayers.setObjectName("actionLayers")
        self.toolBar.addAction(self.actionLayers)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoomPan)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionFullExten)
        self.toolBar.addAction(self.actionIdenty)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAttribute)        
        self.toolBar.addSeparator()        
        self.toolBar.addAction(self.actionClose)        
        self.menuFile.addAction(self.actionClose)
        self.menuStatistics.addAction(self.actionStatisType)
        self.menuStatistics.addAction(self.menuBasinStatis.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.quickView.menuAction())        
        self.menubar.addAction(self.menuStatistics.menuAction())        
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Glacial Lake Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Query:", None, QtGui.QApplication.UnicodeUTF8))
        self.runSqlButton.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.quickView.setTitle(QtGui.QApplication.translate("MainWindow", "Quick View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStatistics.setTitle(QtGui.QApplication.translate("MainWindow", "&Statistics", None, QtGui.QApplication.UnicodeUTF8))        
        self.menuBasinStatis.setTitle(QtGui.QApplication.translate("MainWindow", "By Basin", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))        
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullExten.setText(QtGui.QApplication.translate("MainWindow", "Full Extent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomPan.setText(QtGui.QApplication.translate("MainWindow", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAttribute.setText(QtGui.QApplication.translate("MainWindow", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIdenty.setText(QtGui.QApplication.translate("MainWindow", "Identy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLayers.setText(QtGui.QApplication.translate("MainWindow", "Layers", None, QtGui.QApplication.UnicodeUTF8))                
        self.actionStatisType.setText(QtGui.QApplication.translate("MainWindow", "By Type", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
import default_resources