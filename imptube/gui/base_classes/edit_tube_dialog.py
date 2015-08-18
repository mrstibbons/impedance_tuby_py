# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_tube_dialog.ui'
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

class Ui_editTubeDialog(object):
    def setupUi(self, editTubeDialog):
        editTubeDialog.setObjectName(_fromUtf8("editTubeDialog"))
        editTubeDialog.resize(434, 296)
        self.verticalLayout = QtGui.QVBoxLayout(editTubeDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(editTubeDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setObjectName(_fromUtf8("tabGeneral"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabGeneral)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblName = QtGui.QLabel(self.tabGeneral)
        self.lblName.setObjectName(_fromUtf8("lblName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblName)
        self.editName = QtGui.QLineEdit(self.tabGeneral)
        self.editName.setObjectName(_fromUtf8("editName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editName)
        self.lblComment = QtGui.QLabel(self.tabGeneral)
        self.lblComment.setObjectName(_fromUtf8("lblComment"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblComment)
        self.teComment = QtGui.QTextEdit(self.tabGeneral)
        self.teComment.setObjectName(_fromUtf8("teComment"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.teComment)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tabGeneral, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblForm = QtGui.QLabel(self.tab_2)
        self.lblForm.setObjectName(_fromUtf8("lblForm"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblForm)
        self.cbForm = QtGui.QComboBox(self.tab_2)
        self.cbForm.setObjectName(_fromUtf8("cbForm"))
        self.cbForm.addItem(_fromUtf8(""))
        self.cbForm.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbForm)
        self.lblDiameter = QtGui.QLabel(self.tab_2)
        self.lblDiameter.setObjectName(_fromUtf8("lblDiameter"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblDiameter)
        self.dsbDiameter = QtGui.QDoubleSpinBox(self.tab_2)
        self.dsbDiameter.setObjectName(_fromUtf8("dsbDiameter"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.dsbDiameter)
        self.lblLength = QtGui.QLabel(self.tab_2)
        self.lblLength.setObjectName(_fromUtf8("lblLength"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblLength)
        self.dsbLength = QtGui.QDoubleSpinBox(self.tab_2)
        self.dsbLength.setObjectName(_fromUtf8("dsbLength"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.dsbLength)
        self.lblPosMic1Wide = QtGui.QLabel(self.tab_2)
        self.lblPosMic1Wide.setObjectName(_fromUtf8("lblPosMic1Wide"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblPosMic1Wide)
        self.dsbPosMic1Narrow = QtGui.QDoubleSpinBox(self.tab_2)
        self.dsbPosMic1Narrow.setObjectName(_fromUtf8("dsbPosMic1Narrow"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.dsbPosMic1Narrow)
        self.lblPosMic1Narrow = QtGui.QLabel(self.tab_2)
        self.lblPosMic1Narrow.setObjectName(_fromUtf8("lblPosMic1Narrow"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblPosMic1Narrow)
        self.dsbPosMic1Wide = QtGui.QDoubleSpinBox(self.tab_2)
        self.dsbPosMic1Wide.setObjectName(_fromUtf8("dsbPosMic1Wide"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.dsbPosMic1Wide)
        self.lblPosMic2 = QtGui.QLabel(self.tab_2)
        self.lblPosMic2.setObjectName(_fromUtf8("lblPosMic2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.lblPosMic2)
        self.dsbPosMic2 = QtGui.QDoubleSpinBox(self.tab_2)
        self.dsbPosMic2.setObjectName(_fromUtf8("dsbPosMic2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.dsbPosMic2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(editTubeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(editTubeDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), editTubeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), editTubeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(editTubeDialog)

    def retranslateUi(self, editTubeDialog):
        editTubeDialog.setWindowTitle(_translate("editTubeDialog", "Dialog", None))
        self.lblName.setText(_translate("editTubeDialog", "Name", None))
        self.lblComment.setText(_translate("editTubeDialog", "Kommentar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("editTubeDialog", "Allgemein", None))
        self.lblForm.setText(_translate("editTubeDialog", "Form", None))
        self.cbForm.setItemText(0, _translate("editTubeDialog", "Rund", None))
        self.cbForm.setItemText(1, _translate("editTubeDialog", "Quadratisch", None))
        self.lblDiameter.setText(_translate("editTubeDialog", "Durchmesser", None))
        self.lblLength.setText(_translate("editTubeDialog", "Länge", None))
        self.lblPosMic1Wide.setText(_translate("editTubeDialog", "Position Mic1 (weit)", None))
        self.lblPosMic1Narrow.setText(_translate("editTubeDialog", "Position Mic1 (eng)", None))
        self.lblPosMic2.setText(_translate("editTubeDialog", "Position Mic2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("editTubeDialog", "Abmessungen", None))

