# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_resources import *
from default_layers_dialog import LayersDialog
from qgis.core import *
from qgis.gui import *
from default_attribute_dialog import AttributeDialog
from default_statis_dialog import StatisDialog
from default_trace_dialog import TraceDialog
from default_settings_dialog import SettingsDialog
from ui_main_window import *


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)        
        self.sizeLabel = QLabel("Coordinate")
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.sizeLabel)
        mirrorGroup = QActionGroup(self)
        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)        
        self.actionZoomPan.setCheckable(True)
        self.actionTrace.setCheckable(True)
        self.actionImport.setCheckable(True)
        mirrorGroup.addAction(self.actionZoomIn)
        mirrorGroup.addAction(self.actionZoomOut)        
        mirrorGroup.addAction(self.actionZoomPan)
        mirrorGroup.addAction(self.actionTrace)
        mirrorGroup.addAction(self.actionImport)
        self.connect(self.actionZoomIn, SIGNAL("activated()"), self.mapCanvas.zoomIn)
        self.connect(self.actionZoomOut, SIGNAL("activated()"), self.mapCanvas.zoomOut)
        self.connect(self.actionFullExten, SIGNAL("activated()"), self.mapCanvas.zoomFull)
        self.connect(self.actionZoomPan, SIGNAL("activated()"), self.mapCanvas.pan)
        self.connect(self.actionTrace,SIGNAL("activated()"),self.mapCanvas.indentifyFeature)
        self.connect(self.actionAttribute, SIGNAL("activated()"), self.showAttribute)
        self.connect(self.actionStatis, SIGNAL("activated()"), self.showStatis)
        self.connect(self.actionImport,SIGNAL("activated()"),self.showImport)
        self.connect(self.actionSetting,SIGNAL("activated()"),self.showSettings)
        self.connect(self.actionLayers,SIGNAL("activated()"),self.showLayers)
        self.connect(self.mapCanvas, SIGNAL("xyCoordinates(QgsPoint)"), self.showCoordinates)        
        self.connect(self.mapCanvas.mapIndentify, SIGNAL("indentifyTrace"), self.showTrace)
        self.connect(self.runSqlButton,SIGNAL("clicked()"),self.queryFeatures)
        QTimer.singleShot(0, self.mapCanvas.loadInitialLayers)

    def showAttribute(self):
        if self.mapCanvas.isDrawing(): return
        dialog = AttributeDialog(self.mapCanvas)
        self.actionAttribute.setEnabled(False)
        self.connect(dialog.thread, SIGNAL("finished()"), self.showOkayMessage)
        self.connect(dialog.thread, SIGNAL("terminated()"), self.showErrorMessage)
        dialog.loadingData()
        dialog.show()

    def showStatis(self):
        if self.mapCanvas.isDrawing(): return
        dialog = StatisDialog(self.mapCanvas)
        dialog.show()

    def showOkayMessage(self):
        self.actionAttribute.setEnabled(True)
        self.status.showMessage("Loaded attributes", 5000)

    def showErrorMessage(self):
        self.actionAttribute.setEnabled(True)
        self.status.showMessage("Oops, error occurs", 5000)

    def showCoordinates(self, point):
        self.sizeLabel.setText("Coordinate: %.5f,%.5f" % (point.x(), point.y()))

    def showTrace(self, point):
        if self.mapCanvas.isDrawing(): return
        dialog = TraceDialog(self.mapCanvas)
        dialog.loadAttribute(point)

    def showImport(self):
        dir =  "."
        formats = ["*.%s" % unicode("shp")]
        fileName = unicode(QFileDialog.getOpenFileName(self, "Image Changer - Choose Image", dir,"Image files (%s)" % " ".join(formats)))
        if fileName:
            QMessageBox.information(self,"The name",fileName);

    def showSettings(self):
        if self.mapCanvas.isDrawing(): return
        dialog = SettingsDialog(self)
        dialog.exec_()

    def showLayers(self):
        if self.mapCanvas.isDrawing(): return
        dialog = LayersDialog(self.mapCanvas)
        dialog.show()

    def queryFeatures(self):
        where = self.sqlConsole.text()
        if not where: return
        layer = self.mapCanvas.currentLayer()
        sql = "select gid from %s where %s" % (layer.name(), where)
        print sql
        layer.setSubsetString(where)
        layer.triggerRepaint()



