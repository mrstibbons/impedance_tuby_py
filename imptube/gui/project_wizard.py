import os
from PyQt4 import QtCore, QtGui

from imptube import Project, MeasurementParameters, EnvironmentParameters, MaterialParameters
from imptube.gui.base_classes import Ui_newProjectWizard


class ProjectWizard(QtGui.QWizard, Ui_newProjectWizard):

    # This signal will be emitted when the Wizard is finished to send the newly created Project to the rest of the
    # Application.
    projectCreated = QtCore.pyqtSignal(Project)

    def __init__(self, mainWindow, audioController):
        QtGui.QWizard.__init__(self)

        self.mainWindow = mainWindow
        self.audioController = audioController

        self.setupUi(self)
        self.setModal(True)

        self.deDate.setMinimumDate(QtCore.QDate.currentDate())

        self.nextButton = self.button(QtGui.QWizard.NextButton)

        self.setupFields()
        self.setupConnections()
        self.fillFFTWindowComboBox()
        self.fillSignalSelectComboBox()

    #--------------------------------- Setup ---------------------------------
    def setupFields(self):
        self.wpProjectData.registerField(
            'name*', self.editName)
        self.wpProjectData.registerField(
            'date', self.deDate)
        self.wpProjectData.registerField(
            'comment', self.teComment)

        self.wpMaterialParameters.registerField(
            'material*', self.editMaterial)
        self.wpMaterialParameters.registerField(
            'materialDepth*', self.dsbMaterialThickness, 'value', self.dsbMaterialThickness.valueChanged)
        self.wpMaterialParameters.registerField(
            'degreeOfCleaning*', self.dsbDegreeOfCleaning, 'value', self.dsbDegreeOfCleaning.valueChanged)
        self.wpMaterialParameters.registerField(
            'amountScrub*', self.dsbAmountOfScrub,'value', self.dsbAmountOfScrub.valueChanged)
        self.wpMaterialParameters.registerField(
            'thousandSeedWeight*', self.dsbThousandSeedWeight,'value', self.dsbThousandSeedWeight.valueChanged)

        self.wpEnvironmentParameters.registerField(
            'temperature', self.dsbTemperature, 'value', self.dsbTemperature.valueChanged)
        self.wpEnvironmentParameters.registerField(
            'moisture', self.dsbMoisture, 'value', self.dsbMoisture.valueChanged)
        self.wpEnvironmentParameters.registerField(
            'pressure', self.dsbPressure, 'value', self.dsbPressure.valueChanged)

        self.wpMeasurementParameters.registerField(
            'meanAmount', self.sbMeanAmount)
        self.wpMeasurementParameters.registerField(
            'fftResolution', self.dsbFFTResolution, 'value', self.dsbFFTResolution.valueChanged)
        self.wpMeasurementParameters.registerField(
            'overlap', self.sbOverlap)
        self.wpMeasurementParameters.registerField(
            'fftWindow', self.cbFFTWindow)

    def setupConnections(self):
        self.accepted.connect(self.finishWizard)

        self.sbMeanAmount.valueChanged.connect(self.setRecordingLengthText)
        self.dsbFFTResolution.valueChanged.connect(self.setRecordingLengthText)
        self.sbOverlap.valueChanged.connect(self.setRecordingLengthText)

        self.nextButton.clicked.connect(self.nextButtonClicked)

    def fillFFTWindowComboBox(self):
        for i in range(len(self.audioController.available_windows)):
            self.cbFFTWindow.setItemData(i, self.audioController.available_windows[i])

    def fillSignalSelectComboBox(self):
        for sig in self.audioController.signals:
            self.cbSignalSelect.addItem(os.path.basename(sig), sig)
    #--------------------------------- Slots ---------------------------------
    def finishWizard(self):
        self.createProject()
        self.restart()

    def setRecordingLengthText(self):
        meanAmount = self.field('meanAmount').toPyObject()
        fftResolution = self.field('fftResolution').toPyObject()
        overlap = self.field('overlap').toPyObject() / 100.0  # Value is in %, we need it between 1 and 0
        samplingRate = self.audioController.sampling_rate

        samplesPerFFT = samplingRate / fftResolution
        samplesToRecord = samplesPerFFT + ((1 - overlap) * (meanAmount - 1) * samplesPerFFT)
        recordingLength = samplesToRecord / samplingRate

        self.lblMeasurementTimeDisplay.setText(str(recordingLength) + ' s')

    def nextButtonClicked(self):
        if self.currentPage() == self.wpSelectTube:
            if self.mainWindow.currentTube() is None:
                self.rbCurrentTube.setEnabled(False)
                self.rbNewTube.setChecked(True)
            self.nextButton.setEnabled(True)

        if self.currentPage() == self.wpMeasurementParameters:
            self.setRecordingLengthText()

            if self.rbNewTube.isChecked():
                self.mainWindow.tubeWizard.show()
            elif self.rbTubeFromFile.isChecked():
                self.mainWindow.loadTube()

            self.nextButton.setEnabled(True)

    #------------------------------- Utility ---------------------------------
    def createProject(self):
        name = self.field('name').toPyObject()
        date = self.field('date').toPyObject().toPyDateTime()
        comment = self.field('comment').toPyObject()

        material = self.field('material').toPyObject()
        materialDepth = self.field('materialDepth').toPyObject() / 1000
        degreeOfCleaning = self.field('degreeOfCleaning').toPyObject()
        amountOfScrub = self.field('amountScrub').toPyObject()
        thousandSeedWeight = self.field('thousandSeedWeight').toPyObject()

        temperature = self.field('temperature').toPyObject()
        relMoisture = self.field('moisture').toPyObject()
        airPressure = self.field('pressure').toPyObject()

        meanAmount = self.field('meanAmount').toPyObject()
        fftResolution = self.field('fftResolution').toPyObject()
        overlap = self.field('overlap').toPyObject() / 100.0
        fftWindow = str(self.cbFFTWindow.itemData(self.cbFFTWindow.currentIndex()).toPyObject())
        signal = str(self.cbSignalSelect.itemData(self.cbSignalSelect.currentIndex()).toPyObject())

        materialParameters =\
            MaterialParameters(material, materialDepth, degreeOfCleaning, amountOfScrub,thousandSeedWeight)
        environmentParameters =\
            EnvironmentParameters(temperature, relMoisture, airPressure)
        measurementParameters =\
            MeasurementParameters(self.audioController.sampling_rate, fftResolution, meanAmount, overlap, fftWindow, signal)

        project = Project(name, date, comment, self.mainWindow.currentTube(), materialParameters, environmentParameters,
                          measurementParameters)

        self.projectCreated.emit(project)