import numpy
from PyQt4 import QtCore, QtGui

from imptube.gui.base_classes.export_dialog import Ui_ExportDialog


class ExportDialog(QtGui.QDialog, Ui_ExportDialog):
    def __init__(self, mainWindow):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.setModal(True)

        self.mainWindow = mainWindow
        self.saveButton = self.buttonBox.button(QtGui.QDialogButtonBox.Save)

        self.setupConnections()

    def setupConnections(self):
        self.saveButton.clicked.connect(self.finishWizard)

    def finishWizard(self):
        print "caught signal"
        path = QtGui.QFileDialog.getSaveFileName(self, 'Messung exportieren', '', 'CSV Datei (*.csv)')
        path = str(path)

        data = self.mainWindow.plottedParameterData()

        if self.radioReal.isChecked():
            data = data.real
        elif self.radioImag.isChecked():
            data = data.imag
        elif self.radioMagnitude.isChecked():
            data = numpy.abs(data)
        elif self.radioAngle.isChecked():
            data = numpy.angle(data)

        freqs = self.mainWindow.plottedFrequencies()

        print 'len(freqs) = ', len(freqs)
        print 'len(data) = ', len(data)
        out_data = numpy.column_stack((freqs, data))
        header = 'freq;' + self.mainWindow.selectedParameterAxisCaption()

        numpy.savetxt(path, out_data, fmt='%4f', delimiter=';', header=header, comments='')
