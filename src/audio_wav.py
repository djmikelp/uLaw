import wave
from pydub import AudioSegment  # to play sound on windows install pyaudio o simple audio
from pydub import playback as p
import numpy as np
import matplotlib.pyplot as plt


class AudioWav:
    def __init__(self, file_location):
        self.file_location = file_location
        wav = wave.open(self.file_location, "r")
        self.num_channel = wav.getnchannels()
        self.sample_width = wav.getsampwidth()
        self.frame_rate = wav.getframerate()
        self.num_frames = wav.getnframes()
        self.frames = wav.readframes(self.num_frames)
        wav.close()

    def print_d(self):
        print(
            f"""
File        : '{self.file_location}'
Channels    : {self.num_channel}
Sample with : {self.sample_width}
Frames      : {self.num_frames}
Frame rate  : {self.frame_rate}
"""
        )

    def play(self):
        audio = AudioSegment.from_wav(self.file_location)
        p.play(audio)

    def graph(self, title, color):
        data = self.normalize_array_16()
        time = np.linspace(-1, len(data) / self.frame_rate, num=len(data))
        plt.title(title)
        plt.plot(time, data, color=color)
        plt.grid(True)
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.show()

    def normalize_array_16(self):
        array_16 = np.frombuffer(self.frames, dtype=np.int16)
        array_16_normalized = array_16 * 1.0 / 32768
        return array_16_normalized

    def normalize_array_8(self):
        array_8 = np.frombuffer(self.frames, dtype=np.int8)
        array_8_normalized = array_8 * 1.0 / 128
        return array_8_normalized
