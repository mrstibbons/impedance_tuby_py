# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_settings.ui'
#
# Created: Wed Aug  5 09:24:10 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_GraphSettings(object):
    def setupUi(self, GraphSettings):
        GraphSettings.setObjectName(_fromUtf8("GraphSettings"))
        GraphSettings.setWindowModality(QtCore.Qt.ApplicationModal)
        GraphSettings.resize(502, 326)
        self.verticalLayout_5 = QtGui.QVBoxLayout(GraphSettings)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.grpbXAxis = QtGui.QGroupBox(GraphSettings)
        self.grpbXAxis.setFlat(False)
        self.grpbXAxis.setObjectName(_fromUtf8("grpbXAxis"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.grpbXAxis)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbXLinear = QtGui.QRadioButton(self.grpbXAxis)
        self.rbXLinear.setChecked(True)
        self.rbXLinear.setObjectName(_fromUtf8("rbXLinear"))
        self.grpXAxisScale = QtGui.QButtonGroup(GraphSettings)
        self.grpXAxisScale.setObjectName(_fromUtf8("grpXAxisScale"))
        self.grpXAxisScale.addButton(self.rbXLinear)
        self.horizontalLayout.addWidget(self.rbXLinear)
        self.rbXLogarithmic = QtGui.QRadioButton(self.grpbXAxis)
        self.rbXLogarithmic.setObjectName(_fromUtf8("rbXLogarithmic"))
        self.grpXAxisScale.addButton(self.rbXLogarithmic)
        self.horizontalLayout.addWidget(self.rbXLogarithmic)
        self.horizontalLayout_3.addWidget(self.grpbXAxis)
        self.grpbYAxis = QtGui.QGroupBox(GraphSettings)
        self.grpbYAxis.setObjectName(_fromUtf8("grpbYAxis"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.grpbYAxis)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.rbYLinear = QtGui.QRadioButton(self.grpbYAxis)
        self.rbYLinear.setChecked(True)
        self.rbYLinear.setObjectName(_fromUtf8("rbYLinear"))
        self.horizontalLayout_2.addWidget(self.rbYLinear)
        self.rbYLogarithmic = QtGui.QRadioButton(self.grpbYAxis)
        self.rbYLogarithmic.setObjectName(_fromUtf8("rbYLogarithmic"))
        self.horizontalLayout_2.addWidget(self.rbYLogarithmic)
        self.horizontalLayout_3.addWidget(self.grpbYAxis)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.grpbAbs = QtGui.QGroupBox(GraphSettings)
        self.grpbAbs.setObjectName(_fromUtf8("grpbAbs"))
        self.verticalLayout = QtGui.QVBoxLayout(self.grpbAbs)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbDisplayAbs = QtGui.QCheckBox(self.grpbAbs)
        self.cbDisplayAbs.setObjectName(_fromUtf8("cbDisplayAbs"))
        self.verticalLayout.addWidget(self.cbDisplayAbs)
        self.horizontalLayout_5.addWidget(self.grpbAbs)
        self.grpPhase = QtGui.QGroupBox(GraphSettings)
        self.grpPhase.setObjectName(_fromUtf8("grpPhase"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.grpPhase)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cbDisplayPhase = QtGui.QCheckBox(self.grpPhase)
        self.cbDisplayPhase.setObjectName(_fromUtf8("cbDisplayPhase"))
        self.verticalLayout_2.addWidget(self.cbDisplayPhase)
        self.cbUnwrapPhase = QtGui.QCheckBox(self.grpPhase)
        self.cbUnwrapPhase.setObjectName(_fromUtf8("cbUnwrapPhase"))
        self.verticalLayout_2.addWidget(self.cbUnwrapPhase)
        self.leUnwrapDiscont = QtGui.QLineEdit(self.grpPhase)
        self.leUnwrapDiscont.setEnabled(False)
        self.leUnwrapDiscont.setFrame(True)
        self.leUnwrapDiscont.setCursorPosition(0)
        self.leUnwrapDiscont.setObjectName(_fromUtf8("leUnwrapDiscont"))
        self.verticalLayout_2.addWidget(self.leUnwrapDiscont)
        self.horizontalLayout_5.addWidget(self.grpPhase)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.grpbReal = QtGui.QGroupBox(GraphSettings)
        self.grpbReal.setObjectName(_fromUtf8("grpbReal"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.grpbReal)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cbDisplayReal = QtGui.QCheckBox(self.grpbReal)
        self.cbDisplayReal.setObjectName(_fromUtf8("cbDisplayReal"))
        self.verticalLayout_3.addWidget(self.cbDisplayReal)
        self.horizontalLayout_4.addWidget(self.grpbReal)
        self.grpbImag = QtGui.QGroupBox(GraphSettings)
        self.grpbImag.setObjectName(_fromUtf8("grpbImag"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.grpbImag)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cbDisplayImag = QtGui.QCheckBox(self.grpbImag)
        self.cbDisplayImag.setObjectName(_fromUtf8("cbDisplayImag"))
        self.verticalLayout_4.addWidget(self.cbDisplayImag)
        self.horizontalLayout_4.addWidget(self.grpbImag)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtGui.QDialogButtonBox(GraphSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(GraphSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GraphSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GraphSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(GraphSettings)

    def retranslateUi(self, GraphSettings):
        GraphSettings.setWindowTitle(_translate("GraphSettings", "Graphen-Einstellungen", None))
        self.grpbXAxis.setTitle(_translate("GraphSettings", "X-Achse", None))
        self.rbXLinear.setText(_translate("GraphSettings", "Linear", None))
        self.rbXLogarithmic.setText(_translate("GraphSettings", "Logarithmisch", None))
        self.grpbYAxis.setTitle(_translate("GraphSettings", "Y-Achse", None))
        self.rbYLinear.setText(_translate("GraphSettings", "Linear", None))
        self.rbYLogarithmic.setText(_translate("GraphSettings", "Logarithmisch", None))
        self.grpbAbs.setTitle(_translate("GraphSettings", "Betrag", None))
        self.cbDisplayAbs.setText(_translate("GraphSettings", "Anzeigen", None))
        self.grpPhase.setTitle(_translate("GraphSettings", "Phase", None))
        self.cbDisplayPhase.setText(_translate("GraphSettings", "Anzeigen", None))
        self.cbUnwrapPhase.setText(_translate("GraphSettings", "Unwrap bei:", None))
        self.leUnwrapDiscont.setText(_translate("GraphSettings", "3,141592653589793", None))
        self.grpbReal.setTitle(_translate("GraphSettings", "Realteil", None))
        self.cbDisplayReal.setText(_translate("GraphSettings", "Anzeigen", None))
        self.grpbImag.setTitle(_translate("GraphSettings", "Imaginärteil", None))
        self.cbDisplayImag.setText(_translate("GraphSettings", "Anzeigen", None))

