import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import fftpack
 
Ts1=1e-3 # Интервал дискретизации
fs1 = 1/Ts1
f = (0.4*np.pi*fs1)/(2*np.pi)#определение значения аналоговой частоты
t = np.arange(-5, 11)*Ts1
s =  np.cos(f*t*(2*np.pi))
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t, s)
plt.subplot(3,1,2)
plt.stem(t,s)
print("Аналоговая частота", f)

plt.figure(2)


sp = fftpack.fft(s)
freqs=np.arange(0,fs1,fs1/len(s))
plt.stem(freqs, np.abs(sp))
plt.xlabel('Частота в герцах [Hz]')
plt.ylabel('Модуль спектра')