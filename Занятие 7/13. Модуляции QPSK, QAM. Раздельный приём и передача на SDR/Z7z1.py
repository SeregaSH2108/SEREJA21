import adi
import matplotlib.pyplot as plt
import numpy as np

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = 1e6
sdr.rx_buffer_size = 4000

sdr.rx_lo = int(1500e6)
sdr.tx_lo = int(1500e6)
sdr.tx_hardwaregain_chan0 = -40

fc = 4000
t =  np.arange(0,fc)
t = t / sdr.sample_rate
i=  np.sin(2*np.pi*fc *t)*2**10
q=  np.cos(2*np.pi* fc *t)*2**10
samples = i + 1j * q


plt.figure(1)
plt.plot(samples.real)
plt.plot(samples.imag)

sdr.tx_cyclic_buffer = True
sdr.tx(samples)

array = []
while(1):
    rx = sdr.rx()
    plt.scatter(rx.real, rx.imag)    
    array = np.concatenate((array, rx))
    plt.clf()
    plt.plot(rx)
    plt.draw()
    plt.pause(1)

