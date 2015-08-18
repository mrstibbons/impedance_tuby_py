# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_dialog.ui'
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

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName(_fromUtf8("ExportDialog"))
        ExportDialog.resize(259, 188)
        self.verticalLayout = QtGui.QVBoxLayout(ExportDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupValue = QtGui.QGroupBox(ExportDialog)
        self.groupValue.setObjectName(_fromUtf8("groupValue"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupValue)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioReal = QtGui.QRadioButton(self.groupValue)
        self.radioReal.setObjectName(_fromUtf8("radioReal"))
        self.verticalLayout_2.addWidget(self.radioReal)
        self.radioImag = QtGui.QRadioButton(self.groupValue)
        self.radioImag.setObjectName(_fromUtf8("radioImag"))
        self.verticalLayout_2.addWidget(self.radioImag)
        self.radioMagnitude = QtGui.QRadioButton(self.groupValue)
        self.radioMagnitude.setChecked(True)
        self.radioMagnitude.setObjectName(_fromUtf8("radioMagnitude"))
        self.verticalLayout_2.addWidget(self.radioMagnitude)
        self.radioAngle = QtGui.QRadioButton(self.groupValue)
        self.radioAngle.setObjectName(_fromUtf8("radioAngle"))
        self.verticalLayout_2.addWidget(self.radioAngle)
        self.verticalLayout.addWidget(self.groupValue)
        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(_translate("ExportDialog", "Export Dialog", None))
        self.groupValue.setTitle(_translate("ExportDialog", "Wert auswählen", None))
        self.radioReal.setText(_translate("ExportDialog", "Real", None))
        self.radioImag.setText(_translate("ExportDialog", "Imaginär", None))
        self.radioMagnitude.setText(_translate("ExportDialog", "Betrag", None))
        self.radioAngle.setText(_translate("ExportDialog", "Winkel", None))

