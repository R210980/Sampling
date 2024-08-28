from scipy.io import wavfile
import numpy as np

fs, x = wavfile.read('/home/rguktrkvalley/mixkit-sci-fi-ship-alert-768.wav')

def upsampling(x1, a):
    if a > 1:
    
        y = np.zeros((len(x1) * a, x1.shape[1])) 
        y[::a] = x1
        wavfile.write('upsampled.wav', fs, y)

a = int(input("Enter upsampling factor: "))
upsampling(x, a)
