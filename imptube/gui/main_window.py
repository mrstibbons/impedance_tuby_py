from PyQt4 import QtCore, QtGui, Qwt5
import numpy as np

from imptube import Measurement
from imptube.gui import ProjectWizard
from imptube.gui import TubeWizard
from imptube.gui import CorrectionWizard
from imptube.gui import MeasurementWizard
from imptube.gui import GraphSettings, GraphConfig
from imptube.gui.base_classes import Ui_MainWindow
from imptube.gui.export_dialog import ExportDialog

# TODO: Ask to save unsaved changes before quitting
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    projectLoaded = QtCore.pyqtSignal()
    projectCreated = QtCore.pyqtSignal()
    projectChanged = QtCore.pyqtSignal()
    projectSaved = QtCore.pyqtSignal()

    tubeLoaded = QtCore.pyqtSignal()
    tubeCreated = QtCore.pyqtSignal()
    tubeChanged = QtCore.pyqtSignal()
    tubeSaved = QtCore.pyqtSignal()

    def __init__(self, application):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.application = application
        self.graphConfig = GraphConfig()

        self.setupPlot()

        self.tubeWizard = TubeWizard()
        self.projectWizard = ProjectWizard(self, self.audioController())

        self.tubeHasUnsavedChanges = False
        self.projectHasUnsavedChanges = False
        self.useFrequencyRangeLimits = False

        self.setupMeasurementParameterSelect()

        self.setupConnections()

    #--------------------------------- Setup ---------------------------------
    def setupMeasurementParameterSelect(self):
        for method_name, parameter_name in Measurement.parameters:
            item = QtGui.QListWidgetItem()
            item.setText(parameter_name)
            item.setData(QtCore.Qt.UserRole, method_name)
            self.listMeasurementParameter.addItem(item)

    def setupPlot(self):
        self.qwtPlot.setAxisTitle(Qwt5.QwtPlot.xBottom, 'Frequenz (Hz)')

    def setupConnections(self):
        # Tube-Actions
        self.actionNewTube.triggered.connect(self.tubeWizard.show)
        self.actionLoadTube.triggered.connect(self.loadTube)
        self.actionSaveTube.triggered.connect(self.saveTube)

        # Project-Actions
        self.actionNewProject.triggered.connect(self.projectWizard.show)
        self.actionLoadProject.triggered.connect(self.loadProject)
        self.actionSaveProject.triggered.connect(self.saveProject)
        self.actionMeasureCorrFunc.triggered.connect(self.startCorrectionWizard)

        # Measurement-Actions
        self.actionNewMeasurement.triggered.connect(self.startMeasurementWizard)
        self.actionExportMeasurement.triggered.connect(self.exportSelection)
        self.actionRemoveMeasurement.triggered.connect(self.removeMeasurement)

        # Graph-actions
        self.actionGraphSettings.triggered.connect(self.showGraphSettingsDialog)

        # Wizard-Control
        self.projectWizard.projectCreated.connect(self.setCurrentProject)
        self.tubeWizard.tubeCreated.connect(self.setCurrentTube)

        # List-Control
        self.listProjectMeasurements.currentRowChanged.connect(self.listsSelectionChangedHandler)
        self.listMeasurementParameter.currentRowChanged.connect(self.listsSelectionChangedHandler)

        # Frequency Selection Controls
        self.dsbLowerDisplayedFrequency.valueChanged.connect(self.updateFrequencySelectLimits)
        self.dsbUpperDisplayedFrequency.valueChanged.connect(self.updateFrequencySelectLimits)
        self.btnApplyFrequencyRange.clicked.connect(self.applyFrequencySelectionHandler)
        self.btnRefreshSelection.clicked.connect(self.plotSelection)

        # Project-Signals and Handlers
        self.projectCreated.connect(self.projectCreatedHandler)
        self.projectLoaded.connect(self.projectLoadedHandler)
        self.projectChanged.connect(self.projectChangedHandler)
        self.projectSaved.connect(self.projectSavedHandler)

        # Tube-Signals and Handlers
        self.tubeCreated.connect(self.tubeCreatedHandler)
        self.tubeLoaded.connect(self.tubeLoadedHandler)
        self.tubeChanged.connect(self.tubeChangedHandler)
        self.tubeSaved.connect(self.tubeSavedHandler)

    #--------------------------------- Slots ---------------------------------
    def startCorrectionWizard(self):
        if self.currentTube() is None or self.currentProject() is None:
            QtGui.QMessageBox.warning(
                self,
                'No Tube or no Project Set!',
                'You need to load or create a Tube and load or create a Project before measuring a Correction Function!'
            )
            return


        correctionWizard = CorrectionWizard(self.audioController(), self.currentProject())

        if correctionWizard.exec_() == QtGui.QDialog.Accepted:
            self.projectChanged.emit()

    def startMeasurementWizard(self):
        if self.application.current_project is None:
            # This should not be reached
            QtGui.QMessageBox.warning(
                self,
                'No Project!',
                'You need to load or create a project before you can measure!'
            )
            return

        if not self.currentProject().has_correction_function():
            QtGui.QMessageBox.warning(
                self,
                'No Correction Function!',
                'You need to measure a correction function before you can measure!'
            )
            return

        measurementWizard = MeasurementWizard(self.audioController(), self.currentProject())

        if measurementWizard.exec_() == QtGui.QDialog.Accepted:
            self.projectChanged.emit()
            self.reloadMeasurementsListFromProject()

    def setCurrentTube(self, tube):
        self.application.set_current_tube(tube)
        self.tubeChanged.emit()

    def loadTube(self):
        if self.tubeHasUnsavedChanges:
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Aenderungen speichern?')
            msgBox.setInformativeText('Das derzeitige Rohr entaehlt ungespeicherte Aenderungen. Wollen sie diese speichern?')
            msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save)
            ret = msgBox.exec_()

            if ret == QtGui.QMessageBox.Save:
                self.saveTube()

        path = QtGui.QFileDialog.getOpenFileName(self, 'Messrohr Laden', '', 'Tube Datei (*.tube)')
        path = str(path)

        if path == '':
            return

        self.application.load_tube(path)
        self.tubeLoaded.emit()

    def saveTube(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Messrohr Speichern','', 'Tube Datei (*.tube)')
        path = str(path)

        if path == '':
            return

        self.application.save_tube(path)
        self.tubeSaved.emit()

    def setCurrentProject(self, project):
        self.application.set_current_project(project)
        self.projectCreated.emit()

    def loadProject(self):
        if self.projectHasUnsavedChanges:
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Aenderungen speichern?')
            msgBox.setInformativeText('Das derzeitige Projekt entaehlt ungespeicherte Aenderungen. Wollen sie diese speichern?')
            msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save)
            ret = msgBox.exec_()

            if ret == QtGui.QMessageBox.Save:
                self.saveProject()

        path = QtGui.QFileDialog.getOpenFileName(self, 'Projekt Laden', '', 'Projekt Datei (*.project)')
        path = str(path)

        if path == '':
            return

        self.application.load_project(path)
        self.setCurrentTube(self.currentProject().tube)
        self.projectLoaded.emit()
        self.tubeLoaded.emit()

    def saveProject(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Projekt Speichern', '', 'Project Datei (*.project)')
        path = str(path)

        if path == '':
            return

        self.application.save_project(path)
        self.projectSaved.emit()

    def plotSelection(self):
        if not self.measurementIsSelected() or not self.parameterIsSelected():
            return

        # Clear already plotted Curves
        self.qwtPlot.detachItems()

        data = self.selectedParameterData()
        frequencies = self.currentProject().fft_frequencies()

        if self.useFrequencyRangeLimits:
            # We cast to float64 - equality on python-floats is a very risky thing
            lowerDisplayedFrequency = np.float64(self.dsbLowerDisplayedFrequency.value())
            upperDisplayedFrequency = np.float64(self.dsbUpperDisplayedFrequency.value())
            fftRes = self.currentProject().fft_resolution

            start_index = np.where(np.isclose(frequencies, lowerDisplayedFrequency))[0][0]
            stop_index = np.where(np.isclose(frequencies, upperDisplayedFrequency))[0][0] + 1

            data = data[start_index:stop_index]
            frequencies = frequencies[start_index:stop_index]

        # Set Y Axis Title
        self.qwtPlot.setAxisTitle(Qwt5.QwtPlot.yLeft, self.selectedParameterName())

        if self.graphConfig.showReal:
            curve = Qwt5.QwtPlotCurve('Realteil')
            curve.setData(frequencies, data.real)
            curve.setPen(QtGui.QPen(QtCore.Qt.red))
            curve.setRenderHint(Qwt5.QwtPlotItem.RenderAntialiased)
            curve.attach(self.qwtPlot)

        if self.graphConfig.showImag:
            curve = Qwt5.QwtPlotCurve('Imaginaerteil')
            curve.setData(frequencies, data.imag)
            curve.setPen(QtGui.QPen(QtCore.Qt.yellow))
            curve.setRenderHint(Qwt5.QwtPlotItem.RenderAntialiased)
            curve.attach(self.qwtPlot)

        if self.graphConfig.showAbs:
            curve = Qwt5.QwtPlotCurve('Betrag')
            curve.setData(frequencies, np.abs(data))
            curve.setPen(QtGui.QPen(QtCore.Qt.blue))
            curve.setRenderHint(Qwt5.QwtPlotItem.RenderAntialiased)
            curve.attach(self.qwtPlot)

        if self.graphConfig.showPhase:
            curve = Qwt5.QwtPlotCurve('Phase')

            if self.graphConfig.unwrapPhase:
                curve.setData(frequencies, np.unwrap(np.angle(data), self.graphConfig.unwrapDiscont))
            else:
                curve.setData(frequencies, np.angle(data))
            curve.setPen(QtGui.QPen(QtCore.Qt.green))
            curve.setRenderHint(Qwt5.QwtPlotItem.RenderAntialiased)
            curve.attach(self.qwtPlot)

        # Build Legend
        legend = Qwt5.QwtLegend()
        legend.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Sunken)
        self.qwtPlot.insertLegend(legend, Qwt5.QwtPlot.RightLegend)

        # Set Axis Scaling
        if self.graphConfig.xAxisLinear:
            self.qwtPlot.setAxisScaleEngine(Qwt5.QwtPlot.xBottom, Qwt5.QwtLinearScaleEngine())
        else:
            self.qwtPlot.setAxisScaleEngine(Qwt5.QwtPlot.xBottom, Qwt5.QwtLog10ScaleEngine())

        if self.graphConfig.yAxisLinear:
            self.qwtPlot.setAxisScaleEngine(Qwt5.QwtPlot.yLeft, Qwt5.QwtLinearScaleEngine())
        else:
            self.qwtPlot.setAxisScaleEngine(Qwt5.QwtPlot.yLeft, Qwt5.QwtLog10ScaleEngine())

        # See this: http://stackoverflow.com/questions/14685010/qwt-plot-auto-scale-not-working
        self.qwtPlot.axisScaleEngine(Qwt5.QwtPlot.xBottom).setAttribute(Qwt5.QwtScaleEngine.Floating, True)
        self.qwtPlot.axisScaleEngine(Qwt5.QwtPlot.yLeft).setAttribute(Qwt5.QwtScaleEngine.Floating, True)

        self.qwtPlot.replot()

    def exportSelection(self):
        exportDialog = ExportDialog(self)
        exportDialog.exec_()

    def removeMeasurement(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText('Sind sie sicher?')
        msgBox.setInformativeText('Sind sie sicher, dass sie die Messung entfernen wollen?')
        msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        msgBox.setDefaultButton(QtGui.QMessageBox.No)
        ret = msgBox.exec_()

        if ret == QtGui.QMessageBox.No:
            return

        index = self.listProjectMeasurements.currentRow()

        item = self.listProjectMeasurements.takeItem(index)
        del item

        self.application.remove_measurement(index)
        self.projectChanged.emit()

    def projectLoadedHandler(self):
        self.projectHasUnsavedChanges = False
        self.reloadMeasurementsListFromProject()
        self.actionNewMeasurement.setEnabled(True)
        self.actionMeasureCorrFunc.setEnabled(True)

        self.activateFrequencyRangeSelection()

    def projectCreatedHandler(self):
        self.projectHasUnsavedChanges = True
        self.reloadMeasurementsListFromProject()
        self.actionSaveProject.setEnabled(True)
        self.actionNewMeasurement.setEnabled(True)
        self.actionMeasureCorrFunc.setEnabled(True)

        self.activateFrequencyRangeSelection()

    def projectChangedHandler(self):
        self.projectHasUnsavedChanges = True
        self.reloadMeasurementsListFromProject()
        self.actionSaveProject.setEnabled(True)

    def projectSavedHandler(self):
        self.projectHasUnsavedChanges = False
        self.actionSaveProject.setEnabled(False)

    def tubeLoadedHandler(self):
        self.tubeHasUnsavedChanges = False

    def tubeCreatedHandler(self):
        self.tubeHasUnsavedChanges = True
        self.actionSaveTube.setEnabled(True)

    def tubeChangedHandler(self):
        self.tubeHasUnsavedChanges = True
        self.actionSaveTube.setEnabled(True)

    def tubeSavedHandler(self):
        self.tubeHasUnsavedChanges = False
        self.actionSaveTube.setEnabled(False)

    def listsSelectionChangedHandler(self):
        if self.measurementIsSelected() and self.parameterIsSelected():
            self.plotSelection()
        elif self.measurementIsSelected():
            self.actionRemoveMeasurement.setEnabled(True)
        else:
            self.actionRemoveMeasurement.setEnabled(False)

    def showGraphSettingsDialog(self):
        graphSettingsDialog = GraphSettings(self.graphConfig)
        graphSettingsDialog.exec_()
        self.plotSelection()

    def activateFrequencyRangeSelection(self):
        self.dsbLowerDisplayedFrequency.setEnabled(True)
        self.dsbUpperDisplayedFrequency.setEnabled(True)
        self.btnApplyFrequencyRange.setEnabled(True)


        self.dsbLowerDisplayedFrequency.setMinimum(self.currentProject().fft_resolution)
        self.dsbLowerDisplayedFrequency.setMaximum(self.currentProject().upper_frequency_limit() - self.currentProject().fft_resolution)
        self.dsbLowerDisplayedFrequency.setSingleStep(self.currentProject().fft_resolution)
        self.dsbLowerDisplayedFrequency.setValue(self.currentProject().fft_resolution)

        self.dsbUpperDisplayedFrequency.setMinimum(2 * self.currentProject().fft_resolution)
        self.dsbUpperDisplayedFrequency.setMaximum(self.currentProject().upper_frequency_limit())
        self.dsbUpperDisplayedFrequency.setSingleStep(self.currentProject().fft_resolution)
        self.dsbUpperDisplayedFrequency.setValue(self.currentProject().upper_frequency_limit())

    def updateFrequencySelectLimits(self):
        self.dsbUpperDisplayedFrequency.setMinimum(self.dsbLowerDisplayedFrequency.value() + self.currentProject().fft_resolution)
        self.dsbLowerDisplayedFrequency.setMaximum(self.dsbUpperDisplayedFrequency.value() - self.currentProject().fft_resolution)

    def applyFrequencySelectionHandler(self):
        if self.useFrequencyRangeLimits:
            self.btnApplyFrequencyRange.setText('Auswahl anwenden')
            self.useFrequencyRangeLimits = False
            self.btnRefreshSelection.setEnabled(False)
        else:
            self.btnApplyFrequencyRange.setText('Auswahl aufheben')
            self.useFrequencyRangeLimits = True
            self.btnRefreshSelection.setEnabled(True)

        self.plotSelection()

    #----------------------------------- Delegations ---------------------------------
    def currentTube(self):
        return self.application.current_tube

    def currentProject(self):
        return self.application.current_project

    def audioController(self):
        return self.application.audio_controller

    #------------------------------------- Utility -----------------------------------
    def reloadMeasurementsListFromProject(self):
        self.listProjectMeasurements.clear()

        for measure in self.currentProject().measurements:
            item = QtGui.QListWidgetItem()
            item.setText(measure.name)
            item.setData(QtCore.Qt.UserRole, measure)
            self.listProjectMeasurements.addItem(item)

    def selectedMeasurement(self):
        return self.listProjectMeasurements.currentItem().data(QtCore.Qt.UserRole).toPyObject()

    def selectedParameterMethod(self):
        return str(self.listMeasurementParameter.currentItem().data(QtCore.Qt.UserRole).toPyObject())

    def selectedParameterData(self):
        return getattr(self.selectedMeasurement(), self.selectedParameterMethod())()

    def selectedParameterName(self):
        return str(self.listMeasurementParameter.currentItem().text())

    def frequencies(self):
        return self.currentProject().fft_frequencies()

    def measurementIsSelected(self):
        if self.listProjectMeasurements.currentRow() != -1:
            return True
        else:
            return False

    def parameterIsSelected(self):
        if self.listMeasurementParameter.currentRow() != -1:
            return True
        else:
            return False