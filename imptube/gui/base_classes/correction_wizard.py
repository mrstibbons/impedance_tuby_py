# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'correction_wizard.ui'
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

class Ui_correctionWizard(object):
    def setupUi(self, correctionWizard):
        correctionWizard.setObjectName(_fromUtf8("correctionWizard"))
        correctionWizard.resize(451, 338)
        self.wpDefaultMicPositionsPage = QtGui.QWizardPage()
        self.wpDefaultMicPositionsPage.setObjectName(_fromUtf8("wpDefaultMicPositionsPage"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.wpDefaultMicPositionsPage)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.wdDefaultMicPositions = QtGui.QWidget(self.wpDefaultMicPositionsPage)
        self.wdDefaultMicPositions.setObjectName(_fromUtf8("wdDefaultMicPositions"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.wdDefaultMicPositions)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tbMicDefaultPositionInstructions = QtGui.QTextBrowser(self.wdDefaultMicPositions)
        self.tbMicDefaultPositionInstructions.setObjectName(_fromUtf8("tbMicDefaultPositionInstructions"))
        self.verticalLayout_4.addWidget(self.tbMicDefaultPositionInstructions)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnStartDefaultPosRecording = QtGui.QPushButton(self.wdDefaultMicPositions)
        self.btnStartDefaultPosRecording.setObjectName(_fromUtf8("btnStartDefaultPosRecording"))
        self.horizontalLayout.addWidget(self.btnStartDefaultPosRecording)
        self.pbDefaultMicPositionMeasuring = QtGui.QProgressBar(self.wdDefaultMicPositions)
        self.pbDefaultMicPositionMeasuring.setMaximum(10)
        self.pbDefaultMicPositionMeasuring.setProperty("value", 0)
        self.pbDefaultMicPositionMeasuring.setFormat(_fromUtf8(""))
        self.pbDefaultMicPositionMeasuring.setObjectName(_fromUtf8("pbDefaultMicPositionMeasuring"))
        self.horizontalLayout.addWidget(self.pbDefaultMicPositionMeasuring)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.wdDefaultMicPositions)
        correctionWizard.addPage(self.wpDefaultMicPositionsPage)
        self.wpSwitchedMicPositionsPage = QtGui.QWizardPage()
        self.wpSwitchedMicPositionsPage.setObjectName(_fromUtf8("wpSwitchedMicPositionsPage"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.wpSwitchedMicPositionsPage)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.wdSwitchedMicPositions = QtGui.QWidget(self.wpSwitchedMicPositionsPage)
        self.wdSwitchedMicPositions.setObjectName(_fromUtf8("wdSwitchedMicPositions"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.wdSwitchedMicPositions)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tbSwitchedMicPositionInstructions = QtGui.QTextBrowser(self.wdSwitchedMicPositions)
        self.tbSwitchedMicPositionInstructions.setObjectName(_fromUtf8("tbSwitchedMicPositionInstructions"))
        self.verticalLayout_6.addWidget(self.tbSwitchedMicPositionInstructions)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnStartSwitchedPosRecording = QtGui.QPushButton(self.wdSwitchedMicPositions)
        self.btnStartSwitchedPosRecording.setObjectName(_fromUtf8("btnStartSwitchedPosRecording"))
        self.horizontalLayout_2.addWidget(self.btnStartSwitchedPosRecording)
        self.pbSwitchedMicPositionMeasuring = QtGui.QProgressBar(self.wdSwitchedMicPositions)
        self.pbSwitchedMicPositionMeasuring.setMaximum(10)
        self.pbSwitchedMicPositionMeasuring.setProperty("value", 0)
        self.pbSwitchedMicPositionMeasuring.setFormat(_fromUtf8(""))
        self.pbSwitchedMicPositionMeasuring.setObjectName(_fromUtf8("pbSwitchedMicPositionMeasuring"))
        self.horizontalLayout_2.addWidget(self.pbSwitchedMicPositionMeasuring)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addWidget(self.wdSwitchedMicPositions)
        correctionWizard.addPage(self.wpSwitchedMicPositionsPage)
        self.wpDonePage = QtGui.QWizardPage()
        self.wpDonePage.setObjectName(_fromUtf8("wpDonePage"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.wpDonePage)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.wdDone = QtGui.QWidget(self.wpDonePage)
        self.wdDone.setObjectName(_fromUtf8("wdDone"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.wdDone)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tbDoneInstructions = QtGui.QTextBrowser(self.wdDone)
        self.tbDoneInstructions.setObjectName(_fromUtf8("tbDoneInstructions"))
        self.verticalLayout_8.addWidget(self.tbDoneInstructions)
        self.verticalLayout_9.addWidget(self.wdDone)
        correctionWizard.addPage(self.wpDonePage)

        self.retranslateUi(correctionWizard)
        QtCore.QMetaObject.connectSlotsByName(correctionWizard)

    def retranslateUi(self, correctionWizard):
        correctionWizard.setWindowTitle(_translate("correctionWizard", "Korrekturfunktionsassistent", None))
        self.wpDefaultMicPositionsPage.setTitle(_translate("correctionWizard", "Messung in Standard-Position", None))
        self.tbMicDefaultPositionInstructions.setHtml(_translate("correctionWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Um die Aufnahme in Standard-Position zu beginnen klicken sie bitte auf &quot;Aufnahme starten&quot;. Sobald die Aufnahme beendet ist klicken sie bitte auf &quot;Weiter&quot;.</p></body></html>", None))
        self.btnStartDefaultPosRecording.setText(_translate("correctionWizard", "Aufnahme starten", None))
        self.wpSwitchedMicPositionsPage.setTitle(_translate("correctionWizard", "Messung in vertauschter Position", None))
        self.tbSwitchedMicPositionInstructions.setHtml(_translate("correctionWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bitte vertauschen Sie die Mikrofone. Sobald die Mikrofone vertauscht sind, klicken sie bitte auf &quot;Aufnahem starten&quot;, um die Aufnahme in vertauschter Position zu beginnen.</p></body></html>", None))
        self.btnStartSwitchedPosRecording.setText(_translate("correctionWizard", "Aufnahme starten", None))
        self.wpDonePage.setTitle(_translate("correctionWizard", "Fertig!", None))
        self.tbDoneInstructions.setHtml(_translate("correctionWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Die Messungen für die Korrekturfunktion sind fertig. Bitte bringen sie die Mikrofone wieder in die Standard-Position zurück.</p></body></html>", None))

