import adi
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import fftpack

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = 1e6
sdr.rx_buffer_size = 4000

sdr.rx_lo = int(1500e6)
sdr.tx_lo = int(1500e6)
sdr.tx_hardwaregain_chan0 = -40

# fc = 4000
# t =  np.arange(0,fc)
# t = t / sdr.sample_rate
# i=  np.sin(2*np.pi*fc *t)*2**10
# q=  np.cos(2*np.pi* fc *t)*2**10
# samples = i + 1j * q

#Генерируем QPSK-модулированный сигнал, 16 сэмплов на символ
num_symbols = 1000
x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_degrees = x_int*360/4.0 + 45 # 45, 135, 225, 315 град.
x_radians = x_degrees* np.pi/180.0 # sin() и cos() в рад.
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) #генерируем комплексные числа
samples = np.repeat(x_symbols, 16) # 16 сэмплов на символ
samples *= 2**14 #Повысим значения для наших сэмплов


plt.figure(3)
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.scatter(samples.imag, samples.real)

plt.figure(4)
plt.plot(samples)

sdr.tx_cyclic_buffer = True
sdr.tx(samples)

rx = sdr.rx()
plt.figure(1)
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.scatter(rx.imag, rx.real)


plt.figure(2)
plt.plot(rx)

plt.figure(5)
sp = fftpack.fft(rx)
plt.stem(sp)
plt.show()