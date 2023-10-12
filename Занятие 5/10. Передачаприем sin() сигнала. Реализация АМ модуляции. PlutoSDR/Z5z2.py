import time
import adi
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np



sdr = adi.Pluto("ip:192.168.2.1")
#несущая частота приема и передачи
sdr.rx_lo = 414000000
sdr.tx_lo = 414000000

print(sdr.sample_rate)
sample_rate = 1e6

fc = 60000

t =  np.arange(0,fc)#количество сэмплов
t = t / sdr.sample_rate
print(t)
i=  np.sin(2*np.pi*fc *t)
q=  np.cos(2*np.pi* fc *t)
samples = i + 1j*q

print(samples)
plt.figure(1)
plt.plot(samples.imag)
plt.plot(samples.real)
plt.figure(2)
plt.plot(samples)

#закодированное имя при помощи таблицы ASCII 

array_1=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
0, 1, 0, 1, 0, 0, 1, 1,
0, 1, 0, 0, 0, 1, 0, 1,
0, 1, 0, 1, 0, 0, 1, 0,
0, 1, 0, 0, 0, 1, 1, 1,
0, 1, 0, 0, 0, 1, 0, 1,
0, 1, 0, 1, 1, 0, 0, 1]

for r in range(0,59,1):
    if array_1[r]==1:
        for m in range(r*1000,r*100+99,1):
            samples[m] = samples[m]*2**12
   
sdr.tx_cyclic_buffer = True
sdr.tx(samples)






plt.figure(1)
plt.plot(samples)
plt.ylim(-1000, 1000)
for r in range(40):
    rx = sdr.rx()
    print(len(rx))
    plt.figure(2)
    plt.clf()
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.ylim(-1000, 1000)
    plt.pause(0.05)
    time.sleep(0.1)

plt.show()

