import time
import adi
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np


# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2437000000

sdr.rx_buffer_size = 100000

# Collect data
N = 256
fs = 40e6
k = np.arange(0, N)
k2 = np.arange(-N/2, N/2)
df=fs/N
kf = k*df


for r in range(30):
    rx = sdr.rx()
    print(len(rx))

    plt.figure(1)

    plt.clf()
    X = fft(rx, N) / N
    plt.plot(rx.real)
    plt.plot(rx.imag)

    plt.figure(2)

    plt.stem(k, abs(X))
    plt.xlabel('k')
    plt.ylabel('$x[k]$')
    plt.draw()
    plt.title("6 канал WI-FI")

    plt.figure(3)

    plt.stem(kf, abs(X))  # выводим модуль ДПФ в частота
    plt.xlabel('Гц')
    plt.ylabel('$x[k]$')
    X2 = fftshift(X)  # сдвиг ДПФ на центр

    plt.figure(4)

    kf2 = k2 * df
    plt.stem(kf2,abs(X2))
    plt.xlabel('Гц')
    plt.ylabel('$x[k]$')
    plt.pause(0.05)
    time.sleep(0.1)
