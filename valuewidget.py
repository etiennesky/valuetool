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

import logging
# change the level back to logging.WARNING(the default) before releasing
logging.basicConfig(level=logging.DEBUG)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

hasqwt=True
try:
    from PyQt4.Qwt5 import QwtPlot,QwtPlotCurve,QwtScaleDiv,QwtSymbol
except:
    hasqwt=False

hasmpl=True
try:
    import matplotlib.pyplot as plt 
    import matplotlib.ticker as ticker
except:
    hasmpl=False

from valuewidgetbase import Ui_Form

class ValueWidget(QWidget,Ui_Form):

    def __init__(self, iface):
        self.hasqwt=hasqwt
        self.hasmpl=hasmpl
        QWidget.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.iface=iface
        self.canvas=self.iface.mapCanvas()
        self.logger = logging.getLogger('.'.join((__name__, 
                                        self.__class__.__name__)))
        QObject.connect(self.checkBox_2,SIGNAL("stateChanged(int)"),self.changeActive)
        #self.changeActive(Qt.Checked)
        #set inactive by default - should save last state in user config
        self.checkBox_2.setCheckState(Qt.Unchecked)
        QObject.connect(self.checkBox,SIGNAL("stateChanged(int)"),self.changePage)
        QObject.connect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseDisplay )
        QObject.connect(self.plotSelector, SIGNAL( "currentIndexChanged ( int )" ), self.changePlot )


        if (self.hasqwt):
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
            if (self.plotSelector.currentText()=='matplotlib'):
                self.stackedWidget.setCurrentIndex(2)
            else:
                self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def changePlot(self):
        self.changePage(self.checkBox_2.checkState())

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

        if self.canvas.layerCount() == 0:
            return

        needextremum = self.checkBox.isChecked() # if plot is checked

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

        mapCanvasSrs = self.iface.mapCanvas().mapRenderer().destinationSrs()

        for layer in rasterlayers:
            layerSrs = layer.srs()
            pos = position
            if not mapCanvasSrs == layerSrs and self.iface.mapCanvas().hasCrsTransformEnabled():
              srsTransform = QgsCoordinateTransform(mapCanvasSrs, layerSrs)
              try:
                pos = srsTransform.transform(position)
              except QgsCsException, err:
                # ignore transformation errors
                continue
            isok,ident = layer.identify(pos)
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
                # if this is not a double, it is probably a (GRASS string like
                # 'out of extent' or 'null (no data)'. Let's just show that:
                self.values.append((layername, cstr))
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

        numvalues=[]
        if ( (self.plotSelector.currentText()!='None') and (self.hasqwt or self.hasmpl) ):
            for row in self.values:
                layername,value=row
                try:
                    numvalues.append(float(value))
                except:
                    numvalues.append(0)

        if ( self.hasqwt and (self.plotSelector.currentText()=='Qwt') ):
            self.qwtPlot.setAxisMaxMinor(QwtPlot.xBottom,0)
            #self.qwtPlot.setAxisMaxMajor(QwtPlot.xBottom,0)
            self.qwtPlot.setAxisScale(QwtPlot.xBottom,1,len(self.values))
            self.qwtPlot.setAxisScale(QwtPlot.yLeft,self.ymin,self.ymax)
            
            self.curve.setData(range(1,len(numvalues)+1), numvalues)
            self.qwtPlot.replot()

        elif ( self.hasmpl and (self.plotSelector.currentText()=='matplotlib') ):
            # axis major?
            self.mplPlt.plot(range(1,len(numvalues)+1), numvalues, marker='o', color='k', mfc='b', mec='b')
            self.mplPlt.yaxis.set_minor_locator(ticker.AutoMinorLocator())                                
            self.mplPlt.set_xlim( (1-0.25,len(self.values)+0.25 ) )
            self.mplPlt.set_ylim( (self.ymin, self.ymax) ) 
            self.mplFig.canvas.draw()

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
