# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tube_wizard.ui'
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

class Ui_TubeWizard(object):
    def setupUi(self, TubeWizard):
        TubeWizard.setObjectName(_fromUtf8("TubeWizard"))
        TubeWizard.resize(453, 316)
        TubeWizard.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.wpGeneralInformation = QtGui.QWizardPage()
        self.wpGeneralInformation.setObjectName(_fromUtf8("wpGeneralInformation"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wpGeneralInformation)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.wdGeneralInformation = QtGui.QWidget(self.wpGeneralInformation)
        self.wdGeneralInformation.setObjectName(_fromUtf8("wdGeneralInformation"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wdGeneralInformation)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
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
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.wdGeneralInformation)
        TubeWizard.addPage(self.wpGeneralInformation)
        self.wpTubeDimensions = QtGui.QWizardPage()
        self.wpTubeDimensions.setObjectName(_fromUtf8("wpTubeDimensions"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.wpTubeDimensions)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.wdTubeDimensions = QtGui.QWidget(self.wpTubeDimensions)
        self.wdTubeDimensions.setObjectName(_fromUtf8("wdTubeDimensions"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.wdTubeDimensions)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblForm = QtGui.QLabel(self.wdTubeDimensions)
        self.lblForm.setObjectName(_fromUtf8("lblForm"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblForm)
        self.cbForm = QtGui.QComboBox(self.wdTubeDimensions)
        self.cbForm.setObjectName(_fromUtf8("cbForm"))
        self.cbForm.addItem(_fromUtf8(""))
        self.cbForm.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbForm)
        self.lblDiameter = QtGui.QLabel(self.wdTubeDimensions)
        self.lblDiameter.setObjectName(_fromUtf8("lblDiameter"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblDiameter)
        self.dsbDiameter = QtGui.QDoubleSpinBox(self.wdTubeDimensions)
        self.dsbDiameter.setMaximum(500.0)
        self.dsbDiameter.setObjectName(_fromUtf8("dsbDiameter"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.dsbDiameter)
        self.lblLength = QtGui.QLabel(self.wdTubeDimensions)
        self.lblLength.setObjectName(_fromUtf8("lblLength"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblLength)
        self.dsbLength = QtGui.QDoubleSpinBox(self.wdTubeDimensions)
        self.dsbLength.setMaximum(2000.0)
        self.dsbLength.setObjectName(_fromUtf8("dsbLength"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.dsbLength)
        self.lblPosMic1 = QtGui.QLabel(self.wdTubeDimensions)
        self.lblPosMic1.setObjectName(_fromUtf8("lblPosMic1"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblPosMic1)
        self.dsbPosMic1 = QtGui.QDoubleSpinBox(self.wdTubeDimensions)
        self.dsbPosMic1.setMaximum(2000.0)
        self.dsbPosMic1.setObjectName(_fromUtf8("dsbPosMic1"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.dsbPosMic1)
        self.lblPosMic2 = QtGui.QLabel(self.wdTubeDimensions)
        self.lblPosMic2.setObjectName(_fromUtf8("lblPosMic2"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblPosMic2)
        self.dsbPosMic2 = QtGui.QDoubleSpinBox(self.wdTubeDimensions)
        self.dsbPosMic2.setMaximum(2000.0)
        self.dsbPosMic2.setObjectName(_fromUtf8("dsbPosMic2"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.dsbPosMic2)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_4.addWidget(self.wdTubeDimensions)
        TubeWizard.addPage(self.wpTubeDimensions)

        self.retranslateUi(TubeWizard)
        QtCore.QMetaObject.connectSlotsByName(TubeWizard)

    def retranslateUi(self, TubeWizard):
        TubeWizard.setWindowTitle(_translate("TubeWizard", "Messrohr-Assistent", None))
        self.wpGeneralInformation.setTitle(_translate("TubeWizard", "Allgemeine Information", None))
        self.lblName.setText(_translate("TubeWizard", "Name", None))
        self.lblComment.setText(_translate("TubeWizard", "Kommentar", None))
        self.wpTubeDimensions.setTitle(_translate("TubeWizard", "Abmessungen", None))
        self.lblForm.setText(_translate("TubeWizard", "Form", None))
        self.cbForm.setItemText(0, _translate("TubeWizard", "Quadratisch", None))
        self.cbForm.setItemText(1, _translate("TubeWizard", "Rund", None))
        self.lblDiameter.setText(_translate("TubeWizard", "Durchmesser", None))
        self.dsbDiameter.setSuffix(_translate("TubeWizard", " mm", None))
        self.lblLength.setText(_translate("TubeWizard", "Länge", None))
        self.dsbLength.setSuffix(_translate("TubeWizard", " mm", None))
        self.lblPosMic1.setText(_translate("TubeWizard", "Position Mic 1", None))
        self.dsbPosMic1.setSuffix(_translate("TubeWizard", " mm", None))
        self.lblPosMic2.setText(_translate("TubeWizard", "Position Mic 2", None))
        self.dsbPosMic2.setSuffix(_translate("TubeWizard", " mm", None))

