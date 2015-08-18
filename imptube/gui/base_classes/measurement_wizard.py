# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measurement_wizard.ui'
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

class Ui_MeasurementWizard(object):
    def setupUi(self, MeasurementWizard):
        MeasurementWizard.setObjectName(_fromUtf8("MeasurementWizard"))
        MeasurementWizard.resize(451, 340)
        self.wpGeneralInformation = QtGui.QWizardPage()
        self.wpGeneralInformation.setObjectName(_fromUtf8("wpGeneralInformation"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.wpGeneralInformation)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.wdGeneralInformation = QtGui.QWidget(self.wpGeneralInformation)
        self.wdGeneralInformation.setObjectName(_fromUtf8("wdGeneralInformation"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.wdGeneralInformation)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblName = QtGui.QLabel(self.wdGeneralInformation)
        self.lblName.setObjectName(_fromUtf8("lblName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblName)
        self.editName = QtGui.QLineEdit(self.wdGeneralInformation)
        self.editName.setObjectName(_fromUtf8("editName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editName)
        self.lblComment = QtGui.QLabel(self.wdGeneralInformation)
        self.lblComment.setObjectName(_fromUtf8("lblComment"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblComment)
        self.teComment = QtGui.QTextEdit(self.wdGeneralInformation)
        self.teComment.setObjectName(_fromUtf8("teComment"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.teComment)
        self.verticalLayout_7.addLayout(self.formLayout)
        self.verticalLayout_8.addWidget(self.wdGeneralInformation)
        MeasurementWizard.addPage(self.wpGeneralInformation)
        self.wpMeasuring = QtGui.QWizardPage()
        self.wpMeasuring.setObjectName(_fromUtf8("wpMeasuring"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.wpMeasuring)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.wdMeasuring = QtGui.QWidget(self.wpMeasuring)
        self.wdMeasuring.setObjectName(_fromUtf8("wdMeasuring"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.wdMeasuring)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnStartMeasuring = QtGui.QPushButton(self.wdMeasuring)
        self.btnStartMeasuring.setObjectName(_fromUtf8("btnStartMeasuring"))
        self.horizontalLayout.addWidget(self.btnStartMeasuring)
        self.pbMeasurementProgress = QtGui.QProgressBar(self.wdMeasuring)
        self.pbMeasurementProgress.setProperty("value", 0)
        self.pbMeasurementProgress.setFormat(_fromUtf8(""))
        self.pbMeasurementProgress.setObjectName(_fromUtf8("pbMeasurementProgress"))
        self.horizontalLayout.addWidget(self.pbMeasurementProgress)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.lblInfoText = QtGui.QLabel(self.wdMeasuring)
        self.lblInfoText.setText(_fromUtf8(""))
        self.lblInfoText.setObjectName(_fromUtf8("lblInfoText"))
        self.verticalLayout_12.addWidget(self.lblInfoText)
        self.verticalLayout_13.addWidget(self.wdMeasuring)
        MeasurementWizard.addPage(self.wpMeasuring)

        self.retranslateUi(MeasurementWizard)
        QtCore.QMetaObject.connectSlotsByName(MeasurementWizard)

    def retranslateUi(self, MeasurementWizard):
        MeasurementWizard.setWindowTitle(_translate("MeasurementWizard", "Messungsassistent", None))
        self.wpGeneralInformation.setTitle(_translate("MeasurementWizard", "Allgemeine Information", None))
        self.lblName.setText(_translate("MeasurementWizard", "Name", None))
        self.lblComment.setText(_translate("MeasurementWizard", "Kommentar", None))
        self.wpMeasuring.setTitle(_translate("MeasurementWizard", "Messung", None))
        self.btnStartMeasuring.setText(_translate("MeasurementWizard", "Messung starten", None))

