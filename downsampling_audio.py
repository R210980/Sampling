
from scipy.io import wavfile

fs, x = wavfile.read('/home/rguktrkvalley/mixkit-sci-fi-ship-alert-768.wav')


def sampling(x, a):
    if a > 1:
        y=x[::a]
        wavfile.write('ds1.wav',fs,y)


a=int(input("Enter sampling factor:"))
sampling(x, a)
