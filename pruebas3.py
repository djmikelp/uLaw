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
def expansor(x,u):
    y=np.empty(len(x),dtype=float)
    i=0
    for data in x:
        temp=sgn(data)*(1/u)*(((1+u)**(abs(data)))-1)
        y[i]=(temp)
        i=i+1
    return y
def graficar(datos,framerate,titulo,color):
    Time = np.linspace(0,len(datos)/framerate,num=len(datos))
    plt.title(titulo)
    plt.plot(datos,color=color)
    plt.grid(True)
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo")
    plt.show()
def redondear(x):
    y=np.empty(len(x),dtype=int)
    i=0
    for data in x:
        y[i]=round(data)
        i=i+1
    return y

archivoWav="audioulaw.wav"
archivoWav2="archivoWav2.wav"
wav=wave.open(archivoWav,"r")
numchannel=wav.getnchannels()
samplewidth=wav.getsampwidth()
framerate=wav.getframerate()
numframes=wav.getnframes()
raw=wav.readframes(numframes)
print("numchannel=",numchannel," samplewidth=",samplewidth
      ,"framerate=",framerate,"numframes=",numframes)

if wav.getnchannels() ==2:
    print("Estereo 2 canales")
    sys.exit(0)

wav8Bits=np.frombuffer(raw,dtype=np.int8)
wavNormalizado=wav8Bits*1.0/(max(abs(wav8Bits)))
wavExpandido=expansor(wavNormalizado,255)
wavExpandidoM=wavExpandido*(max(abs(wav8Bits)))
wavExpandidoR=redondear(wavExpandidoM)
#wav2=np.ndarray.tobytes(wavExpandidoR)
wav2=np.frombuffer(wavExpandidoR,dtype=np.int16)
print(wav2)

wav16Bits=np.frombuffer(raw,dtype=np.int16)
wavNormalizado16=wav16Bits*1.0/(max(abs(wav16Bits)))
wavExpandido16=expansor(wavNormalizado16,255)
wavExpandidoM16=wavExpandido*(max(abs(wav16Bits)))
wavExpandidoR16=redondear(wavExpandidoM16)

print("raw",type(raw),len(wav8Bits))
for i in range(3):
    print(raw[i],type(raw[i]))
print("wav8Bits",type(wav8Bits))
print(wav8Bits)
print("wavNormalizado",type(wavNormalizado))
print(wavNormalizado)
print("wavExpandido",type(wavExpandido))
print(wavExpandido)
print("wavExpandidoMultiplicado",type(wavExpandidoM16))
print(wavExpandidoM16)
print("wavExpandidoRedondeado",type(wavExpandidoR))
print(wavExpandidoR)
print("*** (max(abs(wav16Bits)))***",(max(abs(wav8Bits))))

print("wav16Bits",type(wav16Bits),len(wav16Bits))
print(wav16Bits)
print("wavNormalizado16",type(wavNormalizado16))
print(wavNormalizado16)
print("wavExpandido16",type(wavExpandido16))
print(wavExpandido16)
print("wavExpandidoMultiplicado16",type(wavExpandidoM16))
print(wavExpandidoM16)
print("wavExpandidoRedondeado16",type(wavExpandidoR16))
print(wavExpandidoR16)
print("*** (max(abs(wav16Bits)))***",(max(abs(wav16Bits))))
graficar(wav8Bits,framerate,"wav16Bits","red")
#graficar(wavExpandido,framerate,"Wav Expandido","blue")

wav2 =wave.open(archivoWav2,"w")
wav2.setnchannels(numchannel)
wav2.setsampwidth(samplewidth)
wav2.setframerate(framerate)
#wav2.writeframes(wav2)
