"""
/***************************************************************************
         Value Tool       - A QGIS plugin to get values at the mouse pointer
                             -------------------
    begin                : 2008-08-26
    copyright            : (C) 2008 by G. Picard
    email                : 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

hasqwt=True
try:
    from PyQt4.Qwt5 import QwtPlot,QwtPlotCurve,QwtScaleDiv,QwtSymbol
except:
    hasqwt=False

from valuewidgetbase import Ui_Form

class ValueWidget(QWidget,Ui_Form):

    def __init__(self, iface, canvas):
        QWidget.__init__(self)

        
        Ui_Form.__init__(self)
        self.setupUi(self)

        self.iface=iface
        self.canvas=canvas

        QObject.connect(self.checkBox_2,SIGNAL("stateChanged(int)"),self.changeActive)
        self.changeActive(Qt.Checked)
        QObject.connect(self.checkBox,SIGNAL("stateChanged(int)"),self.changePage)
        QObject.connect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseDisplay )

        if (hasqwt):
            self.curve = QwtPlotCurve()
            self.curve.setSymbol(
                QwtSymbol(QwtSymbol.Ellipse,
                          QBrush(Qt.white),
                          QPen(Qt.red, 2),
                          QSize(9, 9)))
            self.curve.attach(self.qwtPlot)

    def disconnect(self):
        self.changeActive(False)
        QObject.disconnect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseDisplay )


    def pauseDisplay(self,e):
      if ( e.modifiers() == Qt.ShiftModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_A:

        self.checkBox_2.toggle()
        return True
      return False


    def keyPressEvent( self, e ):
      if ( e.modifiers() == Qt.ControlModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_C:
        items = QString()
        for rec in range( self.tableWidget.rowCount() ):
          items.append( '"' + self.tableWidget.item( rec, 0 ).text() + '",' + self.tableWidget.item( rec, 1 ).text() + "\n" )
        if not items.isEmpty():
          clipboard = QApplication.clipboard()
          clipboard.setText( items )
      elif (self.pauseDisplay(e)):
        pass
      else:
        QWidget.keyPressEvent( self, e )


    def changePage(self,state):
        if (state==Qt.Checked):
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def changeActive(self,state):
        if (state==Qt.Checked):
            if int(QGis.QGIS_VERSION[2]) > 2: # for QGIS >= 1.3
                QObject.connect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.printValue)
            else:
                QObject.connect(self.canvas, SIGNAL("xyCoordinates(QgsPoint &)"), self.printValue)
        else:
            if int(QGis.QGIS_VERSION[2]) > 2: # for QGIS >= 1.3
                QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.printValue)
            else:
                QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(QgsPoint &)"), self.printValue)


    def printValue(self,position):
        mapPos = position

        needextremum= self.checkBox.isChecked() # if plot is checked

        layers=self.iface

        # count the number of requires rows and remember the raster layers
        nrow=0
        rasterlayers=[]
        layersWOStatistics=[]

        for i in range(self.canvas.layerCount()):
            layer = self.canvas.layer(i)
            if (layer!=None and layer.isValid() and layer.type()==QgsMapLayer.RasterLayer):
              if layer.providerKey()=="wms":
                continue

              if layer.providerKey()=="grassraster":
                nrow+=1
                rasterlayers.append(layer)
              else: # normal raster layer
                nrow+=layer.bandCount()
                rasterlayers.append(layer)
                
              # check statistics for each band
              if needextremum:
                for i in range( 1,layer.bandCount()+1 ):
                  if not layer.hasStatistics(i):
                    layersWOStatistics.append((layer,i))

        if layersWOStatistics:
          self.calculateStatistics(layersWOStatistics)
                  
        # create the row if necessary
        self.tableWidget.setRowCount(nrow)

        irow=0
        self.values=[]
        self.ymin=1e38
        self.ymax=-1e38

        for layer in rasterlayers:
            isok,ident = layer.identify(mapPos)
            if not isok:
                continue

            layername=unicode(layer.name())
            
            if layer.providerKey()=="grassraster":
              if not ident.has_key(QString("value")):
                continue
              cstr = ident[QString("value")]
              if cstr.isNull():
                continue
              value = cstr.toDouble()
              if not value[1]:
                continue
              self.values.append((layername,cstr))
              if needextremum:
                self.ymin = min(self.ymin,value[0])
                self.ymax = max(self.ymax,value[0])

            else:
              for iband in range(1,layer.bandCount()+1): # loop over the bands
                bandvalue=ident[layer.bandName(iband)]
                layernamewithband=layername
                if len(ident)>1:
                    layernamewithband+=' '+layer.bandName(iband)

                self.values.append((layernamewithband,bandvalue))

                if needextremum:
                  cstr=layer.bandStatistics(iband)
                  self.ymin=min(self.ymin,cstr.minimumValue)
                  self.ymax=max(self.ymax,cstr.maximumValue)


        if self.checkBox.isChecked():
          self.plot()
        else:
          self.printInTable()


    def calculateStatistics(self,layersWOStatistics):

      lays= [l[0].name() for l in layersWOStatistics]
      lays = list(set( lays ))
      lays = QStringList() << lays
      res = QMessageBox.warning( self, self.tr( 'Warning' ),
                                 self.tr( 'There are no statistics in the following rasters:\n%1\n\nCalculate?' ).arg(lays.join('\n')),
                                 QMessageBox.Yes | QMessageBox.No )
      if res != QMessageBox.Yes:
        self.checkBox_2.setCheckState(Qt.Unchecked)
        return

      # calculate statistics
      save_state=self.checkBox_2.isChecked()
      self.changeActive(Qt.Unchecked) # deactivate

      for layerband in layersWOStatistics:
        layer,iband=layerband
        stat = layer.bandStatistics(iband)

      if save_state:
        self.changeActive(Qt.Checked) # activate if necessary


    def printInTable(self):

        irow=0
        for row in self.values:
          layername,value=row
          if (self.tableWidget.item(irow,0)==None):
              # create the item
              self.tableWidget.setItem(irow,0,QTableWidgetItem())
              self.tableWidget.setItem(irow,1,QTableWidgetItem())


          self.tableWidget.item(irow,0).setText(layername)
          self.tableWidget.item(irow,1).setText(value)
          irow+=1


    def plot(self):

        if (hasqwt):
            numvalues=[]
            self.qwtPlot.setAxisMaxMinor(QwtPlot.xBottom,0)
            #self.qwtPlot.setAxisMaxMajor(QwtPlot.xBottom,0)
            self.qwtPlot.setAxisScale(QwtPlot.xBottom,1,len(self.values))
            self.qwtPlot.setAxisScale(QwtPlot.yLeft,self.ymin,self.ymax)
            
            for row in self.values:
                layername,value=row
                try:
                    numvalues.append(float(value))
                except:
                    numvalues.append(0)
            self.curve.setData(range(1,len(numvalues)+1), numvalues)
            self.qwtPlot.replot()

        #try:
                #    attr = float(ident[j])
                #except:
                #    attr = 0
                #    print "Null cell value catched as zero!"  # For none values, profile height = 0. It's not elegant...

                    #nr = rastLayer.getRasterBandNumber(self.rastItems[field[1]][field[2]][0])

                    #print ident
            #for j in ident:
                #print j
                #if j.right(1) == str(nr):
       #attr = int(ident[j])
       #attr = float(ident[j])  ##### I MUST IMPLEMENT RASTER TYPE HANDLING!!!!
       #outFeat.addAttribute(i, QVariant(attr))
