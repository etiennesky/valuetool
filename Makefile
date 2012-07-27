#/***************************************************************************
# Valuetool
# 
# A QGIS plugin to get values at the mouse pointer
#
#        begin                : 2008-08-26
#        copyright            : (C) 2008-2010 by G. Picard
#        email                :
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

PLUGINNAME = valuetool

# for building dist zip
TEMPDIR = /tmp

PY_FILES = __init__.py valuetool.py valuewidget.py

EXTRAS = docs/*

UI_FILES = ui_valuewidgetbase.py

RESOURCE_FILES = resources.py

default: compile

#compile: $(UI_FILES) $(RESOURCE_FILES)
compile: $(UI_FILES)

%.py : %.rc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/.qgis/python/plugins
deploy: compile
	mkdir -p $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	#cp -vf $(RESOURCE_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	#cp -vrf $(EXTRAS) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	#mkdir -p $(HOME)/.qgis/python/plugins/$(PLUGINNAME)/docs


dist: cleandist
	mkdir -p $(TEMPDIR)/$(PLUGINNAME)
	cp -r ./*.* $(TEMPDIR)/$(PLUGINNAME)
	cd $(TEMPDIR); zip -9rv $(PLUGINNAME).zip $(PLUGINNAME)
	@echo "You can find the plugin for the qgis repo here: $(TEMPDIR)/$(PLUGINNAME).zip"

cleandist:
	rm -rf $(TEMPDIR)/$(PLUGINNAME)
	rm -rf $(PLUGINNAME).zip
