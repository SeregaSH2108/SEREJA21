from scipy.fftpack import fft, ifft,  fftshift, ifftshift
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz
import numpy as np
import matplotlib.pyplot as plt

 
Ns = 2048 # количество дискретных отсчетов сигнала
Tmax = 10 # временной интервал формирования сигнала
dt=Tmax/(Ns-1)  # интервал дискретизации
fs = 1/dt #частота дисктеризации 
t=np.arange(0, 10,1/fs) 

Ac = 2   #амплитуда несущего колебания
fc = 2  #частота несущего колебания
wc = 2*np.pi*fc #  Фаза
xc = np.cos(wc*t) # Несущее колебание f=4

plt.figure(1)
plt.plot(t,xc)
plt.title('Несущее колебание')
plt.xlabel('t')
plt.ylabel('$s_{нес}(t)$') 

N=2048 # количество точек ДПФ
X = fft(xc,N)/N # вычисление ДПФ и нормирование на N
plt.figure(2)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(X[0:100 ] )) 
plt.title('Спектр несущего колебания')
plt.xlabel('f')
plt.ylabel('$s_{нес}(f)$') 


# Низкочастотное колебание

Am = 1.5 #амплитуда НЧ колебания
fm = 0.2  # Частота НЧ несущего колебания
wm = 2*np.pi*fm # модулирующий НЧ сигнал f=0.5
xm = np.cos(wm*t)

plt.figure(3)
plt.plot(t,xm)
plt.title('НЧ сигнал')
plt.xlabel('t')
plt.ylabel('$s_{НЧ}(t)$') 

N=2048 # количество точек ДПФ
X = fft(xm,N)/N # вычисление ДПФ и нормирование на N
plt.figure(4)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(X[0:100 ] )) 
plt.title('Спектр НЧ сигнала')
plt.xlabel('f')
plt.ylabel('$s_{НЧ}(f)$')

mu = Am/Ac #коэффициент модуляции
 
sam = Ac*(1+mu*xm)*xc # АМ сигнал 

plt.figure(5)
plt.plot(t,sam)
plt.title('Колебание АМ ')
plt.xlabel('t')
plt.ylabel('$s_{AM}(t)$') 


N=2048 # количество точек ДПФ
X = fft(sam,N)/N # вычисление ДПФ и нормирование на N
plt.figure(6)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(X[0:100 ] )) 
plt.title('Спектр АМ сигнала')
plt.xlabel('f')
plt.ylabel('$s_{AM}(f)$') 




