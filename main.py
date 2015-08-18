import sys
import os
import ConfigParser as cp
from PyQt4.QtGui import QApplication

from imptube.gui import MainWindow
from imptube.audio import AudioController
from imptube.project import Project
from imptube.tube import Tube

AUDIO_CONFIG = os.path.dirname(__file__) + "/config/audio.cfg"


class ImpedanceTube(object):
    def __init__(self):

        self.qt_app = QApplication(sys.argv)

        self.audio_controller = None
        self.create_audio_controller()
        self.current_project = None
        self.current_tube = None

        self.setup_gui()

    def setup_gui(self):
        self.main_window = MainWindow(self)

    #TODO: Move this method to the AudioController class
    def create_audio_controller(self):
        parser = cp.SafeConfigParser()
        parser.read(AUDIO_CONFIG)

        sampling_rate = parser.getint('AudioConfig', 'sampling_rate')
        chunk_size = parser.getint('AudioConfig', 'chunk_size')
        input_device = parser.getint('AudioConfig', 'input_device')
        output_device = parser.getint('AudioConfig', 'output_device')
        form = parser.get('AudioConfig', 'format')

        try:
            signal_dir = parser.get('AudioConfig', 'signal_dir')
        except cp.NoOptionError:
            signal_dir = None

        if form == 'float32':
            form = 1
        elif form == 'int8':
            form = 16
        elif form == 'int16':
            form = 8
        elif form == 'int24':
            form = 4
        elif form == 'int32':
            form = 2
        else:
            raise ValueError('Unknown format in audio.cfg')

        self.audio_controller = AudioController(chunk_size=chunk_size,
                                                sampling_rate=sampling_rate,
                                                sample_format=form,
                                                signal_dir=signal_dir)

        self.audio_controller.set_input_device(input_device)
        self.audio_controller.set_output_device(output_device)

    def start_app(self):
        self.main_window.show()
        self.qt_app.exec_()

    def set_current_project(self, project):
        self.current_project = project

    def set_current_tube(self, tube):
        self.current_tube = tube

    def add_calibration(self, calibration):
        self.current_tube.add_calibration_function(calibration)

    def add_measurement(self, measurement):
        self.current_project.add_measurement(measurement)

    def remove_measurement(self, index):
        self.current_project.remove_measurement(index)

    def save_project(self, path):
        self.current_project.save_to_file(path)

    def load_project(self, path):
        self.current_project = Project.load_from_file(path)

    def save_tube(self, path):
        self.current_tube.save_to_file(path)

    def load_tube(self, path):
        self.current_tube = Tube.load_from_file(path)

imp_tube = ImpedanceTube()

imp_tube.start_app()