# ley u
import wave
import json
import os
import numpy as np
import json
from matplotlib import pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
def Read_WAV(wav_path):
    """
         Esta es una función para leer archivos wav, los datos de audio son de un solo canal. Volver json
         : param wav_path: dirección del archivo WAV
    """
    wav_file = wave.open(wav_path,'r')
    numchannel = wav_file.getnchannels()          # Número de canales
    samplewidth = wav_file.getsampwidth()      # Dígitos de cuantización
    framerate = wav_file.getframerate()        # Frecuencia de muestreo
    numframes = wav_file.getnframes()           # Número de puntos de muestreo
#    print("channel", numchannel)
#    print("sample_width", samplewidth)
#    print("framerate", framerate)
#    print("numframes", numframes)
    Wav_Data = wav_file.readframes(numframes)
    Wav_Data = np.frombuffer(Wav_Data,dtype=np.int16)
    Wav_Data = Wav_Data*1.0/(max(abs(Wav_Data)))        # Normalizar los datos
    # Generar datos de audio, ndarray no puede ser json, debe convertirse a la lista, generar JSON
    dict = {"channel":numchannel,
            "samplewidth":samplewidth,
            "framerate":framerate,
            "numframes":numframes,
            "WaveData":list(Wav_Data)}
    return json.dumps(dict)

def DrawSpectrum(wav_data,framerate):
    """
         Esta es la función espectral del audio.
         : param wav_data: datos de audio
         : param framerate: frecuencia de muestreo
    """
    Time = np.linspace(0,len(wav_data)/framerate*1.0,num=len(wav_data))
    plt.figure(1)
    plt.plot(Time,wav_data)
    plt.grid(True)
    plt.ylabel('Datos wav')
    plt.xlabel('Tiempo')
    plt.show()
#    plt.figure(2)
#    Pxx, freqs, bins, im = plt.specgram(wav_data,NFFT=1024,Fs = 16000,noverlap=900)
#    plt.show()
#    print(Pxx)
#    print(freqs)
#    print(bins)
#    print(im)

 #def Expansor(wav_data,u):
    
# Main
archivoAudio='audioulaw.wav';
sound = AudioSegment.from_wav(archivoAudio)
#play(sound)
wavJson=Read_WAV(archivoAudio)
with open('datos.json','w') as archivo:
    json.dump(wavJson, archivo)
#print(wavJson)
wav = json.loads(wavJson)
wav_data = np.array(wav['WaveData'])
framerate = int(wav['framerate'])
DrawSpectrum(wav_data,framerate)
