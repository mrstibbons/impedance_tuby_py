import os
import time
from PyQt4 import QtCore, QtGui

from imptube import MeasurementBase
from imptube.gui.base_classes import Ui_correctionWizard


class CorrectionWizard(QtGui.QWizard, Ui_correctionWizard):
    #------------------------------- Signals -------------------------------
    def __init__(self, audioController, project):
        QtGui.QWizard.__init__(self)

        self.setupUi(self)
        self.setModal(True)

        self.audioController = audioController
        self.project = project

        self.firstMeasurement = None
        self.secondMeasurement = None

        self.firstRecordingFinished = False
        self.secondRecordingFinished = False

        self.nextButton = self.button(QtGui.QWizard.NextButton)
        self.backButton = self.button(QtGui.QWizard.BackButton)

        self.setupConnections()

    #--------------------------------- Setup ---------------------------------
    def setupConnections(self):
        self.nextButton.clicked.connect(self.nextButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)

        self.btnStartDefaultPosRecording.clicked.connect(self.recordInStandardPosition)
        self.btnStartSwitchedPosRecording.clicked.connect(self.recordInSwitchedPosition)

        self.accepted.connect(self.finishWizard)
        self.rejected.connect(self.resetWizard)

    #--------------------------------- Slots ---------------------------------
    def nextButtonClicked(self):
        self.nextButton.setEnabled(False)

        if self.currentPage() == self.wpDefaultMicPositionsPage:
            if self.firstRecordingFinished:
                self.nextButton.setEnabled(True)
                self.backButton.setEnabled(False)

        if self.currentPage() == self.wpSwitchedMicPositionsPage and self.secondRecordingFinished:
            self.nextButton.setEnabled(True)

    def backButtonClicked(self):
        self.backButton.setEnabled(True)

        if self.currentPage() == self.wpDefaultMicPositionsPage and self.firstRecordingFinished:
            self.backButton.setEnabled(False)

    def recordInStandardPosition(self):
        self.btnStartDefaultPosRecording.setEnabled(False)
        self.btnStartDefaultPosRecording.setText('Messe...')
        self.pbDefaultMicPositionMeasuring.setMaximum(0)
        self.pbDefaultMicPositionMeasuring.setMinimum(0)

        self.firstMeasurement = self.audioController.record_sample(self.project.samples_to_record, self.project.signal)

        self.pbDefaultMicPositionMeasuring.setMaximum(10)
        self.pbDefaultMicPositionMeasuring.setValue(10)
        self.pbDefaultMicPositionMeasuring.setFormat('Fertig!')
        self.btnStartDefaultPosRecording.setText('Fertig!')

        time.sleep(5)

        self.nextButton.setEnabled(True)
        self.backButton.setEnabled(False)
        self.firstRecordingFinished = True

    def recordInSwitchedPosition(self):
        self.btnStartSwitchedPosRecording.setEnabled(False)
        self.btnStartSwitchedPosRecording.setText('Messe...')
        self.pbSwitchedMicPositionMeasuring.setMaximum(0)
        self.pbDefaultMicPositionMeasuring.setMinimum(0)

        self.secondMeasurement = self.audioController.record_sample(self.project.samples_to_record, self.project.signal)

        self.pbSwitchedMicPositionMeasuring.setMaximum(10)
        self.pbSwitchedMicPositionMeasuring.setValue(10)
        self.pbSwitchedMicPositionMeasuring.setFormat('Fertig!')
        self.btnStartSwitchedPosRecording.setText('Fertig!')

        self.nextButton.setEnabled(True)
        self.secondRecordingFinished = True

    def finishWizard(self):
        self.project.set_correction_measurements(
            self.firstMeasurement[0], self.firstMeasurement[1], self.secondMeasurement[0], self.secondMeasurement[1])
        self.resetWizard()
        self.restart()

    #--------------------------------- Utility ---------------------------------
    def resetWizard(self):
        self.firstRecordingFinished = False
        self.secondRecordingFinished = False

        self.btnStartDefaultPosRecording.setEnabled(True)
        self.btnStartDefaultPosRecording.setText('Aufnahme starten')
        self.pbDefaultMicPositionMeasuring.setFormat('')
        self.pbDefaultMicPositionMeasuring.setMaximum(10)
        self.pbDefaultMicPositionMeasuring.setValue(0)

        self.btnStartSwitchedPosRecording.setEnabled(True)
        self.btnStartSwitchedPosRecording.setText('Aufnahme starten')
        self.pbSwitchedMicPositionMeasuring.setFormat('')
        self.pbSwitchedMicPositionMeasuring.setMaximum(10)
        self.pbSwitchedMicPositionMeasuring.setValue(0)