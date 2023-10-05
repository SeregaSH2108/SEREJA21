from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt


f1 = 10 # Первый сигнал
f2 = 20 # Второй сигнал
fs=320 # частота дискретизации, избыточная 
t=np.arange( 0, 2,  1/fs) # длительность сигнала 2 с
x=np.cos(2*np.pi*f1*t)+np.cos(2*np.pi*f2*t) # формирование временного сигнала
plt.figure(1)
plt.plot(t,x)
 
plt.stem(t,x) # для отображения временных отсчетов сигнала, выбрать длительность 0.2 сек
plt.xlabel('$t=nT_s$')
plt.ylabel('$x[n]$') 

N=256 # количество точек ДПФ
X = fft(x,N)/N # вычисление ДПФ и нормирование на N
plt.figure(2)
k = np.arange(0, N)
plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
plt.xlabel('k')
plt.ylabel('$x[k]$') 

#df=fs/N
#kf = k*df
#plt.figure(3)
#plt.stem(kf,abs(X)) # выводим модуль ДПФ в частотах 
#plt.xlabel('Гц')
#plt.ylabel('$x[k]$') 


#kf2=k2*df
#X2 = fftshift(X) # сдвиг ДПФ на центр 
#plt.figure(4)
#plt.stem(kf2,abs(X2))
#plt.xlabel('Гц')
#plt.ylabel('$x[k]$') 


#plt.figure(5)
#x_ifft = N*ifft(X,N)
#t = np.arange(0, len(x_ifft))/fs
#plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # временные отсчеты колебания
#plt.xlabel('c')
#plt.ylabel('$x[n]$')

X =np.array([0,0,2-1j,0,0,0,0,0])
plt.figure(5)
x_ifft = N*ifft(X,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
