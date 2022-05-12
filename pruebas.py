from random import sample
from turtle import color
import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

wav = wave.open("audioulaw.wav","r")
raw = wav.readframes(-1)
wav2 =wave.open("audio2.wav","w")
wav2.setnchannels(wav.getnchannels())
wav2.setsampwidth(wav.getsampwidth())
wav2.setframerate(wav.getframerate())

print(raw[2])
raw = np.frombuffer(raw, dtype=np.int16)
print(raw[2])
wav2.writeframes(np.frombuffer(raw, dtype=np.int16))
sampleRate = wav.getframerate()

if wav.getnchannels() ==2:
    print("Estereo 2 canales")
    sys.exit(0)
Time = np.linspace(0,len(raw)/sampleRate, num = len(raw))
plt.title("Wveform of Wave File")
plt.plot(Time,raw, color="blue")
plt.ylabel("Amplitude")
#plt.show()