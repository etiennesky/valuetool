# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valuewidgetbase.ui'
#
# Created: Sun Aug 31 17:23:43 2008
#      by: PyQt4 UI code generator 4.3.3
#

# Adapted by Ghislain


from PyQt4 import QtCore, QtGui
hasqwt=True
try:
    from PyQt4.Qwt5 import QwtPlot
except:
    hasqwt=False

hasmpl=True
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
except:
    hasmpl=False


class Ui_Form(object):
    def setupUi(self, Form):

        self.vboxlayout = QtGui.QVBoxLayout(Form)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.hboxlayout.addWidget(self.checkBox_2)

        self.checkBox = QtGui.QCheckBox(Form)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.hboxlayout.addWidget(self.checkBox)

        self.plotSelector = QtGui.QComboBox(Form)
        if self.hasqwt:
            self.plotSelector.addItem( 'Qwt' )
        if self.hasmpl:
            self.plotSelector.addItem( 'matplotlib' )
        self.plotSelector.setCurrentIndex( 0 );
        if (not self.hasqwt or not self.hasmpl):
            self.plotSelector.setVisible(False)

        self.hboxlayout.addWidget(self.plotSelector)
                
        spacerItem = QtGui.QSpacerItem(40,15,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.stackedWidget = QtGui.QStackedWidget(Form)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")

        # Page 1
        self.tableWidget = QtGui.QTableWidget(self.stackedWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.stackedWidget.addWidget(self.tableWidget)

        #Page 2
        if self.hasqwt:
            self.qwtPlot = QwtPlot(self.stackedWidget)
            self.qwtPlot.setAutoFillBackground(False)
            self.qwtPlot.setObjectName("qwtPlot")
        else:
            self.qwtPlot = QtGui.QLabel("Need Qwt!")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwtPlot.sizePolicy().hasHeightForWidth())
        self.qwtPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")
        self.qwtPlot.updateGeometry()
        self.stackedWidget.addWidget(self.qwtPlot)

        #Page 3 - matplotlib
        if self.hasmpl:
            # mpl stuff
            # should make figure light gray
            self.mplFig = plt.Figure(facecolor='w', edgecolor='w')
            self.mplFig.subplots_adjust(left=0.1, right=0.975, bottom=0.13, top=0.95)
            self.mplPlt = self.mplFig.add_subplot(111)   
            self.mplPlt.tick_params(axis='both', which='major', labelsize=12)
            self.mplPlt.tick_params(axis='both', which='minor', labelsize=10)                           
             # We want the axes cleared every time plot() is called
            self.mplPlt.hold(False)
            # qt stuff
            self.pltCanvas = FigureCanvasQTAgg(self.mplFig)
            self.pltCanvas.setParent(self.stackedWidget)
            self.pltCanvas.setAutoFillBackground(False)
            self.pltCanvas.setObjectName("mplPlot")
            self.mplPlot = self.pltCanvas
        else:
            self.mplPlot = QtGui.QLabel("Need matplotlib!")         

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplPlot.sizePolicy().hasHeightForWidth())
        self.mplPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")
        self.mplPlot.updateGeometry()
        self.stackedWidget.addWidget(self.mplPlot)

        self.vboxlayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "Active (Shift+A)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("Form", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("Form", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1,headerItem1)

