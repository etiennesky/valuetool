# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_valuewidgetbase.ui'
#
# Created: Fri Jul 27 14:10:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ValueWidgetBase(object):
    def setupUi(self, ValueWidgetBase):
        ValueWidgetBase.setObjectName(_fromUtf8("ValueWidgetBase"))
        ValueWidgetBase.resize(360, 156)
        ValueWidgetBase.setWindowTitle(QtGui.QApplication.translate("ValueWidgetBase", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ValueWidgetBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbxActive = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxActive.setToolTip(QtGui.QApplication.translate("ValueWidgetBase", "(Shift+A) to toggle", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxActive.setText(QtGui.QApplication.translate("ValueWidgetBase", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxActive.setObjectName(_fromUtf8("cbxActive"))
        self.horizontalLayout.addWidget(self.cbxActive)
        self.line = QtGui.QFrame(ValueWidgetBase)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.cbxGraph = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxGraph.setText(QtGui.QApplication.translate("ValueWidgetBase", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxGraph.setObjectName(_fromUtf8("cbxGraph"))
        self.horizontalLayout.addWidget(self.cbxGraph)
        self.cbxStats = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxStats.setToolTip(QtGui.QApplication.translate("ValueWidgetBase", "Compute min/max when layers are loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxStats.setText(QtGui.QApplication.translate("ValueWidgetBase", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxStats.setObjectName(_fromUtf8("cbxStats"))
        self.horizontalLayout.addWidget(self.cbxStats)
        self.plotSelector = QtGui.QComboBox(ValueWidgetBase)
        self.plotSelector.setToolTip(QtGui.QApplication.translate("ValueWidgetBase", "Select plotting toolkit", None, QtGui.QApplication.UnicodeUTF8))
        self.plotSelector.setObjectName(_fromUtf8("plotSelector"))
        self.horizontalLayout.addWidget(self.plotSelector)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget = QtGui.QStackedWidget(ValueWidgetBase)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.page)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("ValueWidgetBase", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("ValueWidgetBase", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(ValueWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(ValueWidgetBase)

    def retranslateUi(self, ValueWidgetBase):
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)

