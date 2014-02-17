# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_valuewidgetbase.ui'
#
# Created: Mon Feb 17 17:46:44 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ValueWidgetBase(object):
    def setupUi(self, ValueWidgetBase):
        ValueWidgetBase.setObjectName(_fromUtf8("ValueWidgetBase"))
        ValueWidgetBase.resize(321, 213)
        self.verticalLayout = QtGui.QVBoxLayout(ValueWidgetBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbxActive = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxActive.setObjectName(_fromUtf8("cbxActive"))
        self.horizontalLayout.addWidget(self.cbxActive)
        self.line_2 = QtGui.QFrame(ValueWidgetBase)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.cbxActiveBands = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxActiveBands.setStatusTip(_fromUtf8(""))
        self.cbxActiveBands.setObjectName(_fromUtf8("cbxActiveBands"))
        self.horizontalLayout.addWidget(self.cbxActiveBands)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbxGraph = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxGraph.setObjectName(_fromUtf8("cbxGraph"))
        self.horizontalLayout_3.addWidget(self.cbxGraph)
        self.line = QtGui.QFrame(ValueWidgetBase)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.cbxDigits = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxDigits.setObjectName(_fromUtf8("cbxDigits"))
        self.horizontalLayout_3.addWidget(self.cbxDigits)
        self.spinBox = QtGui.QSpinBox(ValueWidgetBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMaximum(99)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_3.addWidget(self.spinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.graphControls = QtGui.QWidget(ValueWidgetBase)
        self.graphControls.setObjectName(_fromUtf8("graphControls"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.graphControls)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbxStats = QtGui.QCheckBox(self.graphControls)
        self.cbxStats.setObjectName(_fromUtf8("cbxStats"))
        self.horizontalLayout_2.addWidget(self.cbxStats)
        self.label = QtGui.QLabel(self.graphControls)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leYMin = QtGui.QLineEdit(self.graphControls)
        self.leYMin.setObjectName(_fromUtf8("leYMin"))
        self.horizontalLayout_2.addWidget(self.leYMin)
        self.label_2 = QtGui.QLabel(self.graphControls)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leYMax = QtGui.QLineEdit(self.graphControls)
        self.leYMax.setObjectName(_fromUtf8("leYMax"))
        self.horizontalLayout_2.addWidget(self.leYMax)
        self.plotSelector = QtGui.QComboBox(self.graphControls)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSelector.sizePolicy().hasHeightForWidth())
        self.plotSelector.setSizePolicy(sizePolicy)
        self.plotSelector.setObjectName(_fromUtf8("plotSelector"))
        self.horizontalLayout_2.addWidget(self.plotSelector)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.graphControls)
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
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(ValueWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(ValueWidgetBase)

    def retranslateUi(self, ValueWidgetBase):
        ValueWidgetBase.setWindowTitle(_translate("ValueWidgetBase", "Form", None))
        self.cbxActive.setToolTip(_translate("ValueWidgetBase", "(Shift+A) to toggle", None))
        self.cbxActive.setStatusTip(_translate("ValueWidgetBase", "Check to activate value tool", None))
        self.cbxActive.setText(_translate("ValueWidgetBase", "Active", None))
        self.cbxActiveBands.setToolTip(_translate("ValueWidgetBase", "If checked, only display values of bands which are used by rendererer (defined in raster style)", None))
        self.cbxActiveBands.setText(_translate("ValueWidgetBase", "Use active bands only", None))
        self.cbxGraph.setToolTip(_translate("ValueWidgetBase", "Show graph instead of table", None))
        self.cbxGraph.setText(_translate("ValueWidgetBase", "Show graph", None))
        self.cbxDigits.setToolTip(_translate("ValueWidgetBase", "Specify how many digits to show in table", None))
        self.cbxDigits.setText(_translate("ValueWidgetBase", "Decimals", None))
        self.cbxStats.setToolTip(_translate("ValueWidgetBase", "Compute min/max when layers are loaded", None))
        self.cbxStats.setText(_translate("ValueWidgetBase", "Stats", None))
        self.label.setText(_translate("ValueWidgetBase", "Y min", None))
        self.label_2.setText(_translate("ValueWidgetBase", "Y max", None))
        self.plotSelector.setToolTip(_translate("ValueWidgetBase", "Select plotting toolkit", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Value", None))

