import scipy.io.wavfile as wv
import soundfile as sf 
import speech_recognition as  sr
import numpy as np
import time
import matplotlib.pyplot as plt

data, samplerate = sf.read('trial.wav') 

import matplotlib.animation as animation
from matplotlib import style 

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
x=[]
y=[]
i=8000
x=[k for k in range(i-50,i)]
y=[data[k] for k in range(i-50,i)]
def animate(k):
    global i
    i+=1
    x.append(i)
    y.append(data[i])
    x.pop(0)
    y.pop(0)
    ax1.clear()
    ax1.plot(x,y)
    # print(y)
    
ani=animation.FuncAnimation(fig,animate,interval=1000/44100)
plt.show()
