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
def compresor(x,u):
    y=np.empty(len(x),dtype=float)
    i=0
    ln1plusU=np.log(1+u)
    for data in x:
        temp=sgn(data)*(np.log(1+(u*abs(data)))/ln1plusU)
        y[i]=(temp)
        i=i+1
    return y
def graficar(datos,framerate,titulo,color):
    Time = np.linspace(0,len(datos)/framerate,num=len(datos))
    plt.title(titulo)
    plt.plot(Time,datos,color=color)
    plt.grid(True)
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo")
    plt.show()
def entero(x):
    y=np.empty(len(x),dtype=np.int8)
    i=0
    for data in x:
        y[i]=int(data)
        i=i+1
    return y

archivoWav="alain.wav"
archivoWav2="alainComprimido.wav"
wav=wave.open(archivoWav,"r")
wav2=wave.open(archivoWav2,"w")
numchannel=wav.getnchannels()
samplewidth=wav.getsampwidth()
framerate=wav.getframerate()
numframes=wav.getnframes()
raw=wav.readframes(numframes)
print("numchannel=",numchannel," samplewidth=",samplewidth
      ,"framerate=",framerate,"numframes=",numframes)

raw16Bits=np.frombuffer(raw,dtype=np.int16)
#raw8Bits=np.frombuffer(raw,dtype=np.int8)
raw16BitsNormalizado=raw16Bits*1.0/32768
raw16BisComprimido=compresor(raw16BitsNormalizado,255)
raw8Bits=raw16BisComprimido*128
raw8Bits=entero(raw8Bits)
print("*** raw16Bits ***")
for i in range(5):
    print(raw16Bits[i],type(raw16Bits[i]))
print("maximo ",max(abs(raw16Bits)))
print("*** raw8Bits ***")
for i in range(5):
    print(raw8Bits[i],type(raw8Bits[i]))
print("maximo ",max(abs(raw8Bits)))
graficar(raw8Bits,framerate,"Grafico 8 bits comrpimido","red")
wav2.setnchannels(1)
wav2.setsampwidth(1)
wav2.setframerate(44100.0)
wav2.writeframes(raw8Bits)
wav2.close()
