import os
import pyaudio
import threading
import wave
import time
import sys
import numpy as np


class AudioController(object):

    available_windows = ['barthann', 'bartlett', 'blackman', 'blackmanharris', 'bohman', 'boxcar',
                         'triag', 'flattop', 'hamming', 'hann', 'parzen']

    def __init__(self,
                 chunk_size=1024,
                 input_channels=2,
                 sample_format=pyaudio.paInt32,
                 sampling_rate=96000,
                 signal_dir=None):

        self.chunk_size = chunk_size
        self.input_channels = input_channels
        self.sample_format = sample_format
        self.sampling_rate = sampling_rate
        self.input_device = None
        self.output_device = None
        self.signal = None

        if signal_dir is None:
            self.signal_dir = os.path.dirname(__file__) + '/signals/'
        else:
            self.signal_dir = signal_dir

        self.signals = []
        self.load_signals()

        self.devices = []
        self.load_devices()

    def load_signals(self):
        # TODO: Raise an Exception somewhere if there are no Signals to be found on Startup!
        # TODO: This will need to crash miserably if there are no Signals to be found
        self.signals = []

        for _file in os.listdir(self.signal_dir):
            if _file.endswith('.wav'):
                self.signals.append(self.signal_dir + _file)

    def load_devices(self):
        self.devices = []
        pa = pyaudio.PyAudio()

        try:
            for dev_index in range(pa.get_device_count()):
                dev_info = pa.get_device_info_by_index(dev_index)
                self.devices.append(AudioDevice(dev_index, dev_info))
        except:
            raise
        finally:
            pa.terminate()

        return self

    def device_count(self):
        return len(self.devices)

    def set_input_device(self, device_index):
        if device_index not in range(self.device_count()):
            raise ValueError("Invalid Input Device %i. Must be between 0 and %i" % (device_index, self.device_count() - 1))

        if self.devices[device_index].is_not_input_device():
            raise ValueError("The Device %i has no input capabilities!" % device_index)

        self.input_device = device_index

        return self

    def set_output_device(self, device_index):
        if device_index not in range(self.device_count()):
            raise ValueError("Invalid Output Device %i. Must be between 0 and %i" % (device_index, self.device_count() - 1))

        if self.devices[device_index].is_not_output_device():
            raise ValueError("The Device %i has no output capabilities!" % device_index)

        self.output_device = device_index

        return self

    # We wrap the "record_sample_unsafe" method to catch exceptions concerning sound and to do the necessary cleanup.
    # If we don't terminate pyaudio and free the resources the whole thing stops working.
    def record_sample(self, samples_to_record, signal):
        pa = pyaudio.PyAudio()
        try:
            return self.record_sample_unsafe(samples_to_record, signal, pa)
        except:
            raise
        finally:
            pa.terminate()

    def record_sample_unsafe(self, samples_to_record, signal, pa):
        print "Starting Recording"

        if self.input_device is None and self.output_device is None:
            raise ValueError("You have to specify Input and Output devices!")

        if self.input_device is None:
            raise ValueError("You have to specify an Input device!")

        if self.output_device is None:
            raise ValueError("You have to specify an Output device!")

        if self.signal is None:
            self.signal = self.signals[0]

        player = LoopingWavePlayer(signal, pa, self.output_device, self.chunk_size, loop=True)
        frames = ""

        # Lets say we have 2000 samples to record and a chunk size of 512. Since we only can record "full" samples we
        # will use integers. If we divide 2000 by 512 we get 3, the decimals are being "clipped" because we use integers.
        # 512 * 3 is 1536 so we are a few hundred samples short. That's why we will record one chunk more, hence the +1
        # in the following expression. Like this we will get the correct amount of samples in any case. A bit more does
        # not hurt, we will throw the "too much" away later
        chunks_to_record = int(samples_to_record / self.chunk_size) + 1

        player.start()
        # We will will put a pause after the starting of the player because the speaker is making some ugly noise just
        # when the sound starts. Because we want a lot of energy inside of the system the volume levels are very high
        # and this noise causes clipping. We wait a second after we started the recording to avoid record that clipping
        # moment
        time.sleep(1)

        stream = pa.open(
            format=self.sample_format,
            channels=self.input_channels,
            rate=self.sampling_rate,
            frames_per_buffer=self.chunk_size,
            input=True,
            input_device_index=self.input_device
        )

        for i in range(chunks_to_record):
            frames += stream.read(self.chunk_size)

        stream.stop_stream()
        stream.close()
        player.stop()

        # I don't know why, i think it has to do with the player, but we have to wait some time here, otherwise the
        # program will segfault
        time.sleep(0.1)

        frames = np.fromstring(frames, dtype=np.int16)
        frames = frames.reshape((len(frames)/2, 2))

        # Because we always record one more sample than we calculated to be sure to get enough samples we here select
        # only the amount of samples we really need.
        return frames[:samples_to_record, 0], frames[:samples_to_record, 1]


class AudioDevice(object):
    SAMPLING_RATES = [8000, 11025, 16000, 22050, 32000, 37800, 44056, 44100, 47250, 48000, 96000]

    def __init__(self, pa_index, properties_dict):
        self.properties_dict = properties_dict
        self.pa_index = pa_index

    def max_input_channels(self):
        return self.properties_dict['maxInputChannels']

    def max_output_channels(self):
        return self.properties_dict['maxOutputChannels']

    def name(self):
        return self.properties_dict['name']

    def default_sample_rate(self):
        return self.properties_dict['defaultSampleRate']

    def is_input_device(self):
        if self.max_input_channels() > 0:
            return True
        else:
            return False

    def is_not_input_device(self):
        return not self.is_input_device()

    def is_output_device(self):
        if self.max_output_channels() > 0:
            return True
        else:
            return False

    def is_not_output_device(self):
        return not self.is_output_device()

    def get_all_sampling_rates(self):
        return self.SAMPLING_RATES


# Thanks to THeK3nger for this Class, found it on his Github-Page. Here is the original:
#   https://gist.github.com/THeK3nger/3624478
class LoopingWavePlayer(threading.Thread):
    def __init__(self, file_path, pa_instance, output_device, chunk_size, loop=True):
        super(LoopingWavePlayer, self).__init__()

        self.file_path = file_path
        self.pa_instance = pa_instance
        self.output_device = output_device
        self.chunk_size = 8192
        self.loop = loop

    def run(self):
        wf = wave.open(self.file_path)

        stream = self.pa_instance.open(
            format=self.pa_instance.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            frames_per_buffer=self.chunk_size,
            output=True,
            output_device_index=self.output_device,
            input=False
        )

        data = wf.readframes(self.chunk_size)
        while self.loop:
            stream.write(data)
            data = wf.readframes(self.chunk_size)
            if data == '':
                wf.rewind()
                data = wf.readframes(self.chunk_size)

        stream.close()

    def play(self):
        self.start()

    def stop(self):
        self.loop = False
