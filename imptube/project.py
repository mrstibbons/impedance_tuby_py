import pickle
import copy
import numpy as np

from imptube.measurement import Measurement, MeasurementBase


class MaterialParameters:
    def __init__(self, material, material_depth, degree_of_cleaning, amount_of_scrub, thousand_seed_weight):
        self.material = material
        self.material_depth = material_depth
        self.degree_of_cleaning = degree_of_cleaning
        self.amount_of_scrub = amount_of_scrub
        self.thousand_seed_weight = thousand_seed_weight


class EnvironmentParameters:
    def __init__(self, temperature, rel_moisture, air_pressure):
        self.temperature = temperature
        self.rel_moisture = rel_moisture
        self.air_pressure = air_pressure


class MeasurementParameters:
    def __init__(self, sampling_rate, fft_resolution, number_of_ffts, overlap, fft_window, signal):
        self.sampling_rate = sampling_rate
        self.fft_resolution = fft_resolution
        self.number_of_ffts = number_of_ffts
        self.overlap = overlap
        self.fft_window = fft_window
        self.signal = signal
        self.samples_per_fft = int(self.sampling_rate / self.fft_resolution)
        self.samples_to_record =\
            self.samples_per_fft + (self.samples_per_fft * (1 - self.overlap) * (self.number_of_ffts - 1))


class Project(object):
    # This class has so many attributes that I moved them to separate classes. You still are able to access these
    # attributes as if they are normal class attributes due to the fact that I changed the behaviour of __getattr__ that
    # will delegate the request to the appropriate attribute
    material_parameter_delegations =\
        ["material", "material_depth", "degree_of_cleaning", "amount_of_scrub","thousand_seed_weight"]
    environment_parameter_delegations =\
        ["temperature", "rel_moisture", "air_pressure"]
    measurement_parameter_delegations =\
        ["sampling_rate", "fft_resolution", "number_of_ffts", "overlap", "fft_window", "signal", "samples_per_fft",
         "samples_to_record"]
    tube_delegations = \
        ["mic1_pos", "mic_distance", "upper_frequency_limit", "k"]

    def __init__(self, name, date, comment, tube, material_parameters, environment_parameters, measurement_parameters):
        self.name = name
        self.date = date
        self.comment = comment
        self.tube = tube

        self.material_parameters = material_parameters
        self.environment_parameters = environment_parameters
        self.measurement_parameters = measurement_parameters

        self.measurements = []

        self.first_correction_measurement = None
        self.second_correction_measurement = None
        self._correction_function = None
        # With this we count how many measurements were done with the same correction measurement. In the config you
        # can set how many measurements can be done before the software warns you that you should make a new correciton
        # measurement
        self.measurements_since_last_correction = 0

    def __getattr__(self, attribute):
        if attribute in self.material_parameter_delegations:
            return getattr(self.material_parameters, attribute)

        if attribute in self.environment_parameter_delegations:
            return getattr(self.environment_parameters, attribute)

        if attribute in self.measurement_parameter_delegations:
            return getattr(self.measurement_parameters, attribute)

        if attribute in self.tube_delegations:
            return getattr(self.tube, attribute)

        raise AttributeError("Attribute Not Found: " + attribute)

    def fft_frequencies(self):
        return np.arange(self.fft_resolution, self.upper_frequency_limit() + self.fft_resolution, self.fft_resolution)

    def remove_measurement(self, index):
        del self.measurements[index]

    def set_correction_measurements(self, data11, data12, data21, data22):
        self.first_correction_measurement = MeasurementBase(self, data11, data12)
        self.second_correction_measurement = MeasurementBase(self, data21, data22)

        self._correction_function = None

        self.measurements_since_last_correction = 0

    def correction_function(self):
        if self.first_correction_measurement is None:
            raise AttributeError("First correction measurement missing!")
        if self.second_correction_measurement is None:
            raise AttributeError("Second correction measurement missing!")

        if self._correction_function is None:
            #corr_sqrt = np.sqrt(np.abs(self.first_correction_measurement.transfer_function()) * np.abs(self.second_correction_measurement.transfer_function()))
            #corr_exp = np.exp(1j * (np.angle(self.first_correction_measurement.transfer_function()) + np.angle(self.second_correction_measurement.transfer_function())) / 2)
            #self._correction_function = corr_sqrt * corr_exp
            self._correction_function = np.sqrt(self.second_correction_measurement.transfer_function() * self.first_correction_measurement.transfer_function())

        return self._correction_function

    def has_correction_function(self):
        if self.first_correction_measurement is None or self.second_correction_measurement is None:
            return False
        else:
            return True

    def add_measurement(self, name, comment, mic1_data, mic2_data):
        self.measurements.append(Measurement(self, name, comment, mic1_data, mic2_data, self.correction_function()))

        self.measurements_since_last_correction += 1

    @staticmethod
    def load_from_file(path):
        project = None
        with open(path, 'rb') as infile:
            project = pickle.load(infile)

        return project

    def save_to_file(self, path):
        with open(path, 'wb') as outfile:
            pickle.dump(self, outfile, pickle.HIGHEST_PROTOCOL)