import time
import adi
import matplotlib.pyplot as plt
import math as mh
import numpy as np

# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2437000000

# Collect data
for r in range(300):
    rx = sdr.rx()
    plt.clf()
    plt.plot(abs(rx),'r')
    plt.figure()
    plt.plot(mh.sqrt(rx.real[r]**2)+mh.sqrt(rx.imag[r]**2))
    plt.title("6 канал WI-FI")
    if rx.real[r] <= 800:
        plt.pause(10)
        print("10")
    plt.pause(0.05)
    time.sleep(0.1)

plt.show()