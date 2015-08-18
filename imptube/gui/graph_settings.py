from PyQt4 import QtGui
import numpy as np

from imptube.gui.base_classes import Ui_GraphSettings

class GraphConfig(object):
    def __init__(self):
        self.xAxisLinear = True
        self.yAxisLinear = True
        self.showAbs = True
        self.showPhase = True
        self.showReal = False
        self.showImag = False
        self.unwrapPhase = False
        self.unwrapDiscont = np.pi

class GraphSettings(QtGui.QDialog, Ui_GraphSettings):
    def __init__(self, graphConfig):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.graphConfig = graphConfig

        self.leUnwrapDiscont.setValidator(QtGui.QDoubleValidator())

        self.cbDisplayAbs.setChecked(self.graphConfig.showAbs)
        self.cbDisplayPhase.setChecked(self.graphConfig.showPhase)
        self.cbDisplayReal.setChecked(self.graphConfig.showReal)
        self.cbDisplayImag.setChecked(self.graphConfig.showImag)

        self.cbUnwrapPhase.setChecked(self.graphConfig.unwrapPhase)
        self.leUnwrapDiscont.setEnabled(self.graphConfig.unwrapPhase)
        self.leUnwrapDiscont.setText(str(self.graphConfig.unwrapDiscont))

        self.rbXLinear.setChecked(self.graphConfig.xAxisLinear)
        self.rbXLogarithmic.setChecked(not self.graphConfig.xAxisLinear)

        self.rbYLinear.setChecked(self.graphConfig.yAxisLinear)
        self.rbYLogarithmic.setChecked(not self.graphConfig.yAxisLinear)

        self.setupConnections()

    def setupConnections(self):
        self.accepted.connect(self.updateGraphConfig)
        self.cbUnwrapPhase.stateChanged.connect(self.togglePhaseDiscontEdit)

    def updateGraphConfig(self):
        self.graphConfig.showAbs = self.cbDisplayAbs.isChecked()
        self.graphConfig.showPhase = self.cbDisplayPhase.isChecked()
        self.graphConfig.showReal = self.cbDisplayReal.isChecked()
        self.graphConfig.showImag = self.cbDisplayImag.isChecked()

        self.graphConfig.yAxisLinear = self.rbYLinear.isChecked()
        self.graphConfig.xAxisLinear = self.rbXLinear.isChecked()

        self.graphConfig.unwrapDiscont = float(self.leUnwrapDiscont.text())
        self.graphConfig.unwrapPhase = self.cbUnwrapPhase.isChecked()

    def togglePhaseDiscontEdit(self):
        self.leUnwrapDiscont.setEnabled(not self.leUnwrapDiscont.isEnabled())