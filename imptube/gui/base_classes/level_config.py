# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'level_config.ui'
#
# Created: Wed Aug  5 09:24:09 2015
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

class Ui_levelDialog(object):
    def setupUi(self, levelDialog):
        levelDialog.setObjectName(_fromUtf8("levelDialog"))
        levelDialog.resize(206, 204)
        self.abortOkButtons = QtGui.QDialogButtonBox(levelDialog)
        self.abortOkButtons.setGeometry(QtCore.QRect(10, 170, 181, 32))
        self.abortOkButtons.setOrientation(QtCore.Qt.Horizontal)
        self.abortOkButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.abortOkButtons.setObjectName(_fromUtf8("abortOkButtons"))
        self.widget = QtGui.QWidget(levelDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 191, 153))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.levelDialogLayout = QtGui.QHBoxLayout(self.widget)
        self.levelDialogLayout.setMargin(0)
        self.levelDialogLayout.setObjectName(_fromUtf8("levelDialogLayout"))
        self.levelKnobLayout = QtGui.QVBoxLayout()
        self.levelKnobLayout.setObjectName(_fromUtf8("levelKnobLayout"))
        self.levelKnob = QwtKnob(self.widget)
        self.levelKnob.setTotalAngle(270.0)
        self.levelKnob.setObjectName(_fromUtf8("levelKnob"))
        self.levelKnobLayout.addWidget(self.levelKnob)
        self.levelTextDisplay = QtGui.QLineEdit(self.widget)
        self.levelTextDisplay.setEnabled(False)
        self.levelTextDisplay.setObjectName(_fromUtf8("levelTextDisplay"))
        self.levelKnobLayout.addWidget(self.levelTextDisplay)
        self.levelDialogLayout.addLayout(self.levelKnobLayout)
        self.levelDisplay = QwtThermo(self.widget)
        self.levelDisplay.setObjectName(_fromUtf8("levelDisplay"))
        self.levelDialogLayout.addWidget(self.levelDisplay)

        self.retranslateUi(levelDialog)
        QtCore.QObject.connect(self.abortOkButtons, QtCore.SIGNAL(_fromUtf8("accepted()")), levelDialog.accept)
        QtCore.QObject.connect(self.abortOkButtons, QtCore.SIGNAL(_fromUtf8("rejected()")), levelDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(levelDialog)

    def retranslateUi(self, levelDialog):
        levelDialog.setWindowTitle(_translate("levelDialog", "Pegel Einstellen", None))

from qwt_thermo import QwtThermo
from qwt_knob import QwtKnob
