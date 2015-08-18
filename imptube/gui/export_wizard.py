import numpy as np
from PyQt4 import QtCore, QtGui

from imptube.gui.base_classes.export_wizard import Ui_ExportWizard

class ExportWizard(QtGui.QWizard, Ui_ExportWizard):

    def __init__(self, mainWindow):
        QtGui.QWizard.__init__(self)
        self.setupUi()
        self.setModal(True)

        self.mainWindow = mainWindow

    def fillListWidgets(self):
        for i in range(self.mainWindow.listProjectMeasurements.count):
            self.listSelectMesurements.addItem(self.mainWindow.listProjectMeasurements.item(i))

        for i in range(self.mainWindow.listMeasurementParameter.count):
            self.listSelectFunction.addItem(self.mainWindow.listMeasurementParameter.item(i))

    def finishWizard(self):
        currentProject = self.mainWindow.currentProject()
        seperator = str(self.editSeperator.text())

        # Get seleted measurement indices
        indices = []
        for index in range(self.listSelectMesurements.count):
            if self.listSelectMeasurements.item(index).isSelected():
                indices.append(index)

        # Get the Headers
        headers = ['freq']
        for index in indices:
            headers.append(currentProject.measurements[index].name)

        # make the header string
        headerString = seperator.join(headers)

        # get the method to call
        methodIndex = self.listSelectFunction.currentRow()
        methodName = ''



        # get the frequencies


        # Get the Data
        data = []
        for index in indices:
            raw = getattr(currentProject.measurements[index], methodName)

        # Make an Array of it

        # Write it out