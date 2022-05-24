from random import sample
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

print("*** raw ***", type(raw))
# for i in range(1000):
#     raw5[i]=raw[i]

raw = np.frombuffer(raw, dtype=np.int16)
print("*** rawBufer ***", type(raw))
for i in range(5)
    print(raw[i])
print("tipo raw",type(raw))
raw3 = raw*1.0/(max(abs(raw))) 
print("*** rawNormalizado ***", type(raw3))
for i in range(5):
    print(raw3[i])
raw4 = expansion(raw3,255)
#print("tipo raw4 ",type(raw4))
#print("raw3 ",raw3)
print("*** raw4 ***", type(raw4))
for i in range(5):
    print(raw4[i])
wav2.writeframes(raw4)
sampleRate = wav.getframerate()

if wav.getnchannels() ==2:
    print("Estereo 2 canales")
    sys.exit(0)
Time = np.linspace(0,len(raw4)/sampleRate, num = len(raw4))
plt.title("Wveform of Wave File")
plt.plot(Time,raw4, color="red")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.show()
#print(type(raw[1]))
