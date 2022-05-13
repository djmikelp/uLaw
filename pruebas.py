from random import sample
from turtle import color
import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

def sgn(numero):
    if(numero > 0):
        return 1
    if(numero < 0):
        return -1
    else:
        return 0
def expansion(y,u):
    F=y
    i=0
    for x in y:
        F[i]=sgn(x)*(1/u)*(((1+u)**(abs(x)))-1)
        i=i+1
    return F


wav = wave.open("audioulaw.wav","r")
raw = wav.readframes(-1)
wav2 =wave.open("audio2.wav","w")
wav2.setnchannels(wav.getnchannels())
wav2.setsampwidth(wav.getsampwidth())
wav2.setframerate(wav.getframerate())
#print(np.size(raw))
print("*** tal cual ***")
for i in range(5):
    print(raw[i])

raw = np.frombuffer(raw, dtype=np.int16)
raw3 = raw*1.0/(max(abs(raw))) 
raw3 = expansion(raw3,255)
#print("signo ",raw3)
print("*** normalizado ***")
for i in range(5):
    print(sgn(raw3[i]))
wav2.writeframes(np.frombuffer(raw3, dtype=np.int16))
sampleRate = wav.getframerate()

if wav.getnchannels() ==2:
    print("Estereo 2 canales")
    sys.exit(0)
Time = np.linspace(0,len(raw)/sampleRate, num = len(raw))
plt.title("Wveform of Wave File")
plt.plot(Time,raw, color="blue")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
#plt.show()
print(type(raw[1]))