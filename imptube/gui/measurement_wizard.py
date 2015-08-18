
from PyQt4 import QtCore, QtGui

from imptube.gui.base_classes import Ui_MeasurementWizard


class MeasurementWizard(QtGui.QWizard, Ui_MeasurementWizard):
    def __init__(self, audioController, project):
        QtGui.QWizard.__init__(self)

        self.setupUi(self)
        self.setModal(True)

        self.audioController = audioController
        self.project = project

        self.measurement = None

        self.measuringFinished = False

        self.nextButton = self.button(QtGui.QWizard.NextButton)
        self.finishButton = self.button(QtGui.QWizard.FinishButton)

        self.setupFields()
        self.setupConnections()

    #--------------------------------- Setup ---------------------------------
    def setupFields(self):
        self.wpGeneralInformation.registerField('name*', self.editName)
        self.wpGeneralInformation.registerField('comment', self.teComment)

    def setupConnections(self):
        self.nextButton.clicked.connect(self.nextButtonClicked)

        self.btnStartMeasuring.clicked.connect(self.measure)

        self.accepted.connect(self.finishWizard)
        self.rejected.connect(self.resetWizard)

    #------------------------------- Slots -------------------------------
    def nextButtonClicked(self):
        self.nextButton.setEnabled(False)

        if self.currentPage() == self.wpMeasuring:
            self.finishButton.setEnabled(False)

            if self.measuringFinished:
                self.finishButton.setEnabled(True)
                
    def measure(self):
        self.pbMeasurementProgress.setMaximum(0)
        self.btnStartMeasuring.setEnabled(False)
        self.btnStartMeasuring.setText('Messe...')
        self.lblInfoText.setText('Messe...')

        self.measurement = self.audioController.record_sample(self.project.samples_to_record, self.project.signal)

        self.pbMeasurementProgress.setMaximum(10)
        self.pbMeasurementProgress.setValue(10)
        self.pbMeasurementProgress.setFormat("Fertig!")
        self.btnStartMeasuring.setText('Fertig!')
        self.lblInfoText.setText("Fertig!")

        self.measuringFinished = True

        self.finishButton.setEnabled(True)

    def finishWizard(self):
        name = str(self.field('name').toPyObject())
        comment = str(self.field('name').toPyObject())

        self.project.add_measurement(name, comment, self.measurement[0], self.measurement[1])
        self.resetWizard()
        self.restart()

    #------------------------------- Utility -------------------------------
    def resetWizard(self):
        self.measurement = None

        self.measuringFinished = False

        self.pbMeasurementProgress.setMaximum(10)
        self.pbMeasurementProgress.setValue(0)
        self.pbMeasurementProgress.setFormat('')
        self.btnStartMeasuring.setEnabled(True)
        self.btnStartMeasuring.setText('Messung starten')
        self.lblInfoText.setText('')