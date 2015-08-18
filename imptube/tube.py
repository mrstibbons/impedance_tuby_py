import pickle


class Tube(object):
    def __init__(self, name, comment, form, length, diameter, mic1_pos, mic2_pos):
        self.name = name
        self.comment = comment
        self.form = form

        self.length = length
        self.diameter = diameter
        self.mic1_pos = mic1_pos
        self.mic2_pos = mic2_pos

        # Rectangular and round tubes have different k values
        if self.form == "rect":
            self.k = 0.5
        else:
            self.k = 0.586

        self.mic_distance = self.mic1_pos - self.mic2_pos

    def upper_frequency_limit(self, speed_of_sound=343.3):
        return int((self.k * speed_of_sound) / self.diameter)

    @staticmethod
    def load_from_file(path):
        tube = None
        with open(path, 'rb') as infile:
            tube = pickle.load(infile)

        return tube

    def save_to_file(self, path):
        with open(path, 'wb') as outfile:
            pickle.dump(self, outfile, pickle.HIGHEST_PROTOCOL)