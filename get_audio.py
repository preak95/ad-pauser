import json
import pyaudio
import struct
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


CHUNK = 5 #2048 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

def get_audio():
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=CHUNK
    )
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * CHUNK, 2)
    line, = ax.plot((x, [1,2,3,4,5]))

    ax.set_ylim(0,255)
    ax.set_xlim(0, CHUNK)
    
    while True:
        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK ) + 'B', data), dtype='b')[::2] + 127
        print(data_int)

get_audio()