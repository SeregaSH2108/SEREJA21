import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

Ts1 = 2e-3 # Интервал дискретизации
fs1 = 1/Ts1
f0 = (0.4*np.pi*fs1)/(2*np.pi)#определение значения аналоговой частоты
t = np.arange(-5, 11)*Ts1
   

    

for f in range(25, 226, 50):
    s = np.cos(f*t*(2*np.pi))
    sp = fftpack.fft(s) 
    plt.figure()
    freqs=np.arange(0,fs1,fs1/len(s))
    plt.stem(freqs, np.abs(sp))
    plt.xlabel('Частота в герцах')
    plt.ylabel('Модуль спектра')
    plt.title('Спектр отсчетов')
    plt.grid()