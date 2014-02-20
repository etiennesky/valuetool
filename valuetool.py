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
from qgis.gui import QgsMapTool

from valuewidget import ValueWidget

#from selectPointTool import *
# initialize Qt resources from file resouces.py
import resources_rc

class ValueTool:
  def __init__(self, iface):
    # save reference to the QGIS interface
    self.iface = iface
    self.canvas=self.iface.mapCanvas()

  def initGui(self):
    # create action that will start plugin configuration
    #self.action = QAction(QIcon(":/plugins/valuetool/icon.png"), "Value Tool", self.iface.getMainWindow())
    #self.action.setWhatsThis("Value Tool")
    #QObject.connect(self.action, SIGNAL("activated()"), self.run)
    ## add toolbar button and menu item
    #self.iface.addToolBarIcon(self.action)
    #self.iface.addPluginMenu("Analyses", self.action)
    ## add the tool to select feature
    #self.tool = selectPointTool(self.iface.getMapCanvas(),self.action)

    # add action to toolbar
    self.action=QAction(QIcon(":/plugins/valuetool/icon.svg"), "Value Tool", self.iface.mainWindow())
    self.iface.addToolBarIcon(self.action)
    self.tool=ValueMapTool(self.canvas, self.action)
    self.saveTool=None
    QObject.connect(self.action, SIGNAL("triggered()"), self.activateTool)
    QObject.connect(self.tool, SIGNAL("deactivate"), self.deactivateTool)

    # create the widget to display information
    self.valuewidget = ValueWidget(self.iface)
    self.valuewidget.cbxActive.setEnabled(False)
    QObject.connect(self.tool, SIGNAL("moved"), self.valuewidget.toolMoved)
    QObject.connect(self.tool, SIGNAL("pressed"), self.valuewidget.toolPressed)

    # create the dockwidget with the correct parent and add the valuewidget
    self.valuedockwidget=QDockWidget("Value Tool" , self.iface.mainWindow() )
    self.valuedockwidget.setObjectName("Value Tool")
    self.valuedockwidget.setWidget(self.valuewidget)
    #QObject.connect(self.valuedockwidget, SIGNAL('visibilityChanged ( bool )'), self.showHideDockWidget)
    
    # add the dockwidget to iface
    self.iface.addDockWidget(Qt.LeftDockWidgetArea,self.valuedockwidget)
    #self.valuewidget.show()



###Qt.AllDockWidgetAreas
  def unload(self):
    self.valuedockwidget.close()
    self.valuewidget.disconnect()
    self.canvas.unsetMapTool(self.tool)
    if self.saveTool:
      self.canvas.setMapTool(self.saveTool)
    # remove the dockwidget from iface
    self.iface.removeDockWidget(self.valuedockwidget)
    # remove the plugin menu item and icon
    #self.iface.removePluginMenu("Analyses",self.action)
    self.iface.removeToolBarIcon(self.action)

  def activateTool(self):
    self.saveTool=self.canvas.mapTool()
    self.canvas.setMapTool(self.tool)
    if not self.valuedockwidget.isVisible():
      self.valuedockwidget.show()
    self.valuewidget.cbxActive.setEnabled(True)
    self.valuewidget.cbxActive.setChecked(True)

  def deactivateTool(self):
    self.valuewidget.cbxActive.setEnabled(False)
    self.valuewidget.cbxActive.setChecked(False)


class ValueMapTool(QgsMapTool):

    def __init__(self, canvas, button):
        QgsMapTool.__init__(self,canvas)
        self.canvas = canvas
        self.cursor = QCursor(Qt.CrossCursor)
        self.button = button

    def activate(self):
        QgsMapTool.activate(self)
        self.canvas.setCursor(self.cursor)
        self.button.setCheckable(True)
        self.button.setChecked(True)
        
    def deactivate(self):
        if not self:
            return
        self.emit( SIGNAL("deactivate") )
        self.button.setCheckable(False)
        QgsMapTool.deactivate(self)

    def isZoomTool(self):
        return False

    def setCursor(self,cursor):
        self.cursor = QCursor(cursor)

    def canvasMoveEvent(self,event):
        self.emit( SIGNAL("moved"), QPoint(event.pos().x(), event.pos().y()) )

    def canvasPressEvent(self,event):
        self.emit( SIGNAL("pressed"), QPoint(event.pos().x(), event.pos().y()) )
