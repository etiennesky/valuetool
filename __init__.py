"""
/***************************************************************************
         Value Tool       - A QGIS plugin to get values at the mouse pointer
                             -------------------
    begin                : 2008-08-26
    copyright            : (C) 2008-2010 by G. Picard
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
# load valuetool class from file valuetool.py


def name(): 
  return 'Value Tool'

def description():
  return 'Display in a table or plot the values from the visible raster layers at the current mouse position' 

def version(): 
  return 'Version 0.4.5'

def qgisMinimumVersion():
  return '1.0'

def category():
    return 'Raster'


def authorName():
  return 'Ghislain Picard'


def classFactory(iface): 
  from valuetool import ValueTool
  return ValueTool(iface)



# Display the values of the raster layers at the current mouse position. Values are printed in a table or plotted on a graph. The plugin is dockable like overview or coordinate capture, go to View/Panels to activate it.
