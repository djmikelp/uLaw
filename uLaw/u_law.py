import numpy as np
from audio_wav import AudioWav
import wave
import math


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def floor_8(array):
    temp_array = np.empty(len(array), dtype=np.int8)
    i = 0
    for x in array:
        temp_array[i] = int(x)
        i += 1
    return temp_array


def ceil_16(array):
    temp_array = np.empty(len(array), dtype=np.int16)
    i = 0
    for x in array:
        x_ceil = math.ceil(x)
        temp_array[i] = int(x_ceil)
        i += 1
    return temp_array


def compress_formula(data_array, u):
    temp_array = np.empty(len(data_array), dtype=float)
    i = 0
    b = np.log(1 + u)
    for x in data_array:
        temp_array[i] = sgn(x) * (np.log(1 + (u * abs(x))) / b)
        i += 1
    return temp_array


def decompress_formula(data_array, u):
    temp_array = np.empty(len(data_array), dtype=float)
    i = 0
    a = 1 / u
    b = 1 + u
    for x in data_array:
        temp_array[i] = sgn(x) * a * ((b ** (abs(x))) - 1)
        i += 1
    return temp_array


def make_wav(output_location, num_channel, sample_width, frame_rate, wav_array):
    wav = wave.open(output_location, "w")
    wav.setnchannels(num_channel)
    wav.setsampwidth(sample_width)
    wav.setframerate(frame_rate)
    wav.writeframes(wav_array)
    wav.close()


def compress(audio_wav, u, output_location):
    wav_array = audio_wav.normalize_array_16()
    wav_array = compress_formula(wav_array, u)
    wav_array = wav_array * 128
    wav_array = floor_8(wav_array)
    make_wav(output_location, 1, 1, 44100.0, wav_array)
    wav_compressed = AudioWav(output_location)
    return wav_compressed


def decompress(audio_wav, u, output_location):
    wav_array = audio_wav.normalize_array_8()
    wav_array = decompress_formula(wav_array, u)
    wav_array = wav_array * 32768
    wav_array = ceil_16(wav_array)
    make_wav(output_location, 1, 2, 44100.0, wav_array)
    wav_decompressed = AudioWav(output_location)
    return wav_decompressed
