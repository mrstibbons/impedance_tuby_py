# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_wizard.ui'
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

class Ui_ExportWizard(object):
    def setupUi(self, ExportWizard):
        ExportWizard.setObjectName(_fromUtf8("ExportWizard"))
        ExportWizard.resize(481, 318)
        self.wpSelectMeasurement = QtGui.QWizardPage()
        self.wpSelectMeasurement.setObjectName(_fromUtf8("wpSelectMeasurement"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wpSelectMeasurement)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listSelectMesurements = QtGui.QListWidget(self.wpSelectMeasurement)
        self.listSelectMesurements.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listSelectMesurements.setObjectName(_fromUtf8("listSelectMesurements"))
        self.verticalLayout.addWidget(self.listSelectMesurements)
        ExportWizard.addPage(self.wpSelectMeasurement)
        self.wpSelectParameter = QtGui.QWizardPage()
        self.wpSelectParameter.setObjectName(_fromUtf8("wpSelectParameter"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.wpSelectParameter)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listSelectFunction = QtGui.QListWidget(self.wpSelectParameter)
        self.listSelectFunction.setObjectName(_fromUtf8("listSelectFunction"))
        self.verticalLayout_3.addWidget(self.listSelectFunction)
        ExportWizard.addPage(self.wpSelectParameter)
        self.wpSelectValues = QtGui.QWizardPage()
        self.wpSelectValues.setObjectName(_fromUtf8("wpSelectValues"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wpSelectValues)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rbAbs = QtGui.QRadioButton(self.wpSelectValues)
        self.rbAbs.setChecked(True)
        self.rbAbs.setObjectName(_fromUtf8("rbAbs"))
        self.buttonGroup = QtGui.QButtonGroup(ExportWizard)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rbAbs)
        self.verticalLayout_2.addWidget(self.rbAbs)
        self.rbAngle = QtGui.QRadioButton(self.wpSelectValues)
        self.rbAngle.setObjectName(_fromUtf8("rbAngle"))
        self.buttonGroup.addButton(self.rbAngle)
        self.verticalLayout_2.addWidget(self.rbAngle)
        self.rbAbsAngle = QtGui.QRadioButton(self.wpSelectValues)
        self.rbAbsAngle.setEnabled(False)
        self.rbAbsAngle.setObjectName(_fromUtf8("rbAbsAngle"))
        self.buttonGroup.addButton(self.rbAbsAngle)
        self.verticalLayout_2.addWidget(self.rbAbsAngle)
        self.rbReal = QtGui.QRadioButton(self.wpSelectValues)
        self.rbReal.setObjectName(_fromUtf8("rbReal"))
        self.buttonGroup.addButton(self.rbReal)
        self.verticalLayout_2.addWidget(self.rbReal)
        self.rbImag = QtGui.QRadioButton(self.wpSelectValues)
        self.rbImag.setObjectName(_fromUtf8("rbImag"))
        self.buttonGroup.addButton(self.rbImag)
        self.verticalLayout_2.addWidget(self.rbImag)
        self.rbRealImag = QtGui.QRadioButton(self.wpSelectValues)
        self.rbRealImag.setEnabled(False)
        self.rbRealImag.setObjectName(_fromUtf8("rbRealImag"))
        self.buttonGroup.addButton(self.rbRealImag)
        self.verticalLayout_2.addWidget(self.rbRealImag)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.editSeperator = QtGui.QLineEdit(self.wpSelectValues)
        self.editSeperator.setObjectName(_fromUtf8("editSeperator"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editSeperator)
        self.lblSeperator = QtGui.QLabel(self.wpSelectValues)
        self.lblSeperator.setObjectName(_fromUtf8("lblSeperator"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblSeperator)
        self.verticalLayout_2.addLayout(self.formLayout)
        ExportWizard.addPage(self.wpSelectValues)

        self.retranslateUi(ExportWizard)
        QtCore.QMetaObject.connectSlotsByName(ExportWizard)

    def retranslateUi(self, ExportWizard):
        ExportWizard.setWindowTitle(_translate("ExportWizard", "Export-Assistent", None))
        self.wpSelectMeasurement.setTitle(_translate("ExportWizard", "Messungen auswählen:", None))
        self.wpSelectParameter.setTitle(_translate("ExportWizard", "Funktion auswählen:", None))
        self.wpSelectValues.setTitle(_translate("ExportWizard", "Exportierte Werte auswählen", None))
        self.rbAbs.setText(_translate("ExportWizard", "Betrag", None))
        self.rbAngle.setText(_translate("ExportWizard", "Winkel", None))
        self.rbAbsAngle.setText(_translate("ExportWizard", "Betrag/Winkel", None))
        self.rbReal.setText(_translate("ExportWizard", "Realteil", None))
        self.rbImag.setText(_translate("ExportWizard", "Imaginärteil", None))
        self.rbRealImag.setText(_translate("ExportWizard", "Real/Imaginärteil", None))
        self.editSeperator.setText(_translate("ExportWizard", ";", None))
        self.lblSeperator.setText(_translate("ExportWizard", "Seperator", None))

