import math
import wave
import struct

freq      = 440.0
data_size = 40000
fname     = "fourier.wav"
srate     = 44100.0 # sampling rate as a float
amp       = 128.0 # multiplier for amplitude

sine_list_x = []
for X in range(data_size):
    x = freq*(X/srate)
    # sine_list_x.append(math.sin(2*math.pi*freq*(X/srate)))
    sine_list_x.append((x - math.pi) * math.sin((x - math.pi)))

wav_file = wave.open(fname, "w")

nchannels = 1
sampwidth = 2
samplingrate = int(srate)
nframes   = data_size
comptype  = "NONE"
compname  = "not compressed"

wav_file.setparams((nchannels, sampwidth, samplingrate, nframes,
    comptype, compname))

for s in sine_list_x:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    # print int(s*amp/2)
wav_file.close()
