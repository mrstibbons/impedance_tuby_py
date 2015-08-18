import numpy as np
from scipy import fftpack, signal

import matplotlib.pyplot as pp

# Nomenclature in this File:
#   aps = Auto Power Spectrum
#   cps = Cross Power Spectrum


class MeasurementBase(object):

    parameters = [('aps_mic1', 'Auto Power Spectrum Mic 1'), ('aps_mic2', 'Auto Power Spectrum Mic 2'),
                  ('cps_mic12', 'Cross Power Spectrum Mic 1-2'), ('cps_mic21', 'Cross Power Spectrum Mic 2-1'),
                  ('transfer_function', 'Transfer Function')]

    def __init__(self, project, mic1_data, mic2_data):
        self.project = project
        _mic1_fft = self.calc_fft(mic1_data)
        _mic2_fft = self.calc_fft(mic2_data)
        self._aps_mic1  = np.average(_mic1_fft * np.conj(_mic1_fft), axis=0)
        self._aps_mic2  = np.average(_mic2_fft * np.conj(_mic2_fft), axis=0)
        self._cps_mic12 = np.average(_mic2_fft * np.conj(_mic1_fft), axis=0)
        self._cps_mic21 = np.average(_mic1_fft * np.conj(_mic2_fft), axis=0)
        self._transfer_function = None

    def calc_fft(self, data):
        fft_array = np.empty([self.project.number_of_ffts, self.project.sampling_rate / self.project.fft_resolution], dtype=np.complex)

        lower_border = 0
        upper_border = self.project.samples_per_fft
        step_width = int(self.project.samples_per_fft * (1 - self.project.overlap))
        fft_window = signal.get_window(self.project.fft_window, self.project.samples_per_fft)

        for i in range(0, self.project.number_of_ffts):
            fft = fftpack.fft(data[lower_border:upper_border] * fft_window)
            fft_array[i] = fft
            lower_border += step_width
            upper_border += step_width

        return fft_array

    def aps_mic1(self):
        return self._aps_mic1

    def aps_mic2(self):
        return self._aps_mic2

    def cps_mic12(self):
        return self._cps_mic12

    def cps_mic21(self):
        return self._cps_mic21

    def transfer_function(self):
        if self._transfer_function is None:
            self._transfer_function = np.sqrt((self.cps_mic12() / self.aps_mic1()) * (self.aps_mic2() / self.cps_mic21()))

        return self._transfer_function


class Measurement(MeasurementBase):

    parameters = MeasurementBase.parameters
    parameters +=\
        [
            ('correction_function', 'Correction Function'),
            ('corrected_transfer_function', 'Corrected Transfer Function'), ('factor_of_reflection', 'Factor of Reflection'),
            ('degree_of_reflection', 'Degree of Reflection'), ('degree_of_absorption', 'Degree of Absorption'),
            ('specific_admittance', 'Specific Admittance'), ('specific_impedance', 'Specific Impedance')
        ]

    def __init__(self, project, name, comment, mic1_data, mic2_data, correction_function):
        super(Measurement, self).__init__(project, mic1_data, mic2_data)
        self._correction_function = correction_function

        self.name = name
        self.comment = comment

        self._corrected_transfer_function = None
        self._factor_of_reflection = None
        self._degree_of_reflection = None
        self._degree_of_absorption = None
        self._specific_admittance = None
        self._specific_impedance = None

    def correction_function(self):
        return self._correction_function

    def corrected_transfer_function(self):
        if self._corrected_transfer_function is None:
            self._corrected_transfer_function = self.transfer_function() / self.correction_function()

        return self._corrected_transfer_function

    # Reflexionsfaktor r
    def factor_of_reflection(self):
        if self._factor_of_reflection is None:

            # Calculation based on brunnader diploma thesis
            dividend = self.corrected_transfer_function() - np.exp(-1j * self.project.k * self.project.mic_distance)
            divisor = np.exp(1j * self.project.k * self.project.mic_distance) - self.corrected_transfer_function()

            self._factor_of_reflection = (dividend / divisor) * np.exp(1j * 2 * self.project.k * self.project.mic1_pos)

        return self._factor_of_reflection

    # Reflextionsgrad R = |r|^2
    def degree_of_reflection(self):
        if self._degree_of_reflection is None:
            self._degree_of_reflection = np.square(np.abs(self.factor_of_reflection()))

        return self._degree_of_reflection

    # Absorptionsgrad alpha = 1 - R
    def degree_of_absorption(self):
        if self._degree_of_absorption is None:
            self._degree_of_absorption = 1 - self.degree_of_reflection()

        return self._degree_of_absorption

    # Spezifische Admittanz rho * c / Z = (1 - r) / (1 + r)
    def specific_admittance(self):
        if self._specific_admittance is None:
            self._specific_admittance = (1 - self.factor_of_reflection()) / (1 + self.factor_of_reflection())

        return self._specific_admittance

    # Spezifische Impedanz Z / rho * c = (1 + r) / (1 - r)
    def specific_impedance(self):
        if self._specific_impedance is None:
            self._specific_impedance = (1 + self.factor_of_reflection()) / (1 - self.factor_of_reflection())

        return self._specific_impedance