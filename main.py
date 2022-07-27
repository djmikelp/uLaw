from audio_wav import AudioWav
from u_law import compress, decompress
# to play sound on Windows install pyaudio or simple audio

input_wav = "Media/audio.wav"
output_wav = "Media/audio_compressed.wav"
output_wav_2 = "Media/audio_decompressed.wav"
wav = AudioWav(input_wav)

if __name__ == '__main__':
    wav.print_d()
    wav.play()
    wav.graph(f"{input_wav}", "Red")
    wav_compressed = compress(wav, 255, output_wav)
    wav_compressed.play()
    wav_compressed.print_d()
    wav_compressed.graph(f"{output_wav}", "Green")
    wav_decompressed = decompress(wav_compressed, 255, output_wav_2)
    wav_decompressed.print_d()
    wav_decompressed.play()
    wav_decompressed.graph(f"{output_wav_2}", "Blue")

