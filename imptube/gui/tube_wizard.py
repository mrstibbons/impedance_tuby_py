from PyQt4 import QtCore, QtGui

from imptube.tube import Tube
from imptube.gui.base_classes.tube_wizard import Ui_TubeWizard


class TubeWizard(QtGui.QWizard, Ui_TubeWizard):

    tubeCreated = QtCore.pyqtSignal(Tube)

    def __init__(self):
        QtGui.QWizard.__init__(self)

        self.tube = None
        self.setupUi(self)
        self.setModal(True)

        self.setupFields()
        self.fillFormComboBox()
        self.setupConnections()

    #--------------------------------- Setup ---------------------------------
    def setupFields(self):
        self.wpGeneralInformation.registerField('name*', self.editName)
        self.wpGeneralInformation.registerField('comment', self.teComment)

        self.wpTubeDimensions.registerField('form', self.cbForm)
        self.wpTubeDimensions.registerField('diameter*', self.dsbDiameter,
                                            'value', self.dsbDiameter.valueChanged)
        self.wpTubeDimensions.registerField('length*', self.dsbLength,
                                            'value', self.dsbLength.valueChanged)
        self.wpTubeDimensions.registerField('posMic1*', self.dsbPosMic1,
                                            'value', self.dsbLength.valueChanged)
        self.wpTubeDimensions.registerField('posMic2*', self.dsbPosMic2,
                                            'value', self.dsbLength.valueChanged)


    def fillFormComboBox(self):
        self.cbForm.setItemData(0, 'rect')
        self.cbForm.setItemData(1, 'round')

    def setupConnections(self):
        self.accepted.connect(self.finishWizard)

    #--------------------------------- Slots ---------------------------------
    def finishWizard(self):
        self.createTube()
        self.restart()

    #--------------------------------- Utility ---------------------------------
    def createTube(self):
        name = self.field('name').toPyObject()
        comment = self.field('comment').toPyObject()

        form = self.cbForm.itemData(self.cbForm.currentIndex()).toPyObject()

        # The measures will be entered in mm, so we convert to m by dividing by 1000
        diameter = self.field('diameter').toPyObject() / 1000
        length = self.field('length').toPyObject() / 1000
        posMic1 = self.field('posMic1').toPyObject() / 1000
        posMic2 = self.field('posMic2').toPyObject() / 1000

        tube = Tube(name, comment, form, length, diameter, posMic1, posMic2)

        self.tubeCreated.emit(tube)

        return tube