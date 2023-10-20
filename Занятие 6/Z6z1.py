import time
import adi
import matplotlib.pyplot as plt
import numpy as np

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = 1e6
sdr.rx_buffer_size = 1000

#config tx
sdr.tx_lo = int(2300e6)

#config rx
sdr.rx_lo = int(2300e6)

fc = 60000
t =  np.arange(0,fc)
t = t / sdr.sample_rate
i=  np.sin(2*np.pi*fc *t)
q=  np.cos(2*np.pi* fc *t)
samples = i + 1j*q


Podacha=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
0, 1, 1, 0, 0, 0, 1, 1,
0, 1, 1, 0, 0, 0, 0, 1,
0, 1, 1, 0, 0, 0, 1, 1,
0, 1, 1, 0, 0, 1, 0, 0,
1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1]

for r in range(0,59,1):
    if Podacha[r]==1:
        for m in range(r*500,r*500+499,1):
            samples[m] = samples[m]*2**12


#pereda4a signal
sdr.tx_cyclic_buffer = False

plt.plot(samples)

array3 = []

for l in range(1000):
    if l == 200 or  l == 400:
        sdr.tx(samples)
    rx = sdr.rx()
    array3 = np.concatenate((array3, abs(rx)))
    plt.figure(2)


plt.plot(array3)
plt.ylim(-5000, 5000)
decoder = []
y = 0
summ = 0
i = 0
# for p in range(0, len(array3),1000):
#     # if abs(array3[p]) > 1000:
#     #     print("index = ", p)
#     #     for i in range(12*100):
#     #         summ += array3[p+i].real
#     #     print(summ)
#     #     print(12*100*1000)
#     if abs(array3[p]) >= 600:
#         summ += 1
#         print('start', summ)
#         if summ == 12:
#             y = p/100
#             print(y*100)
#             for i in range(int(y*100), len(array3), 1000):
#                 if array3[i] > 600:
#                     decoder.append(1)
#                 else:
#                     decoder.append(0)
#     if abs(array3[p]) <600:
#         print('end', summ)
#         summ = 0
#         print("false")
                    # print("серега берюзовый")

summ1 = 0
while(i < len(array3)):
    if abs(array3[i]) > 1000:
        for j in range(12 * 500):
            summ += abs(array3[i + j])
        if(summ >= 12*500*800):
            for l in range (i + 12 * 500, i + 12 * 500 + 48 * 500, 500):
                for p in range(l, l + 500, 1):
                    summ1 += abs(array3[i + j + p])
                if (summ >= 500*700):
                    decoder.append(1)
                else:
                    decoder.append(0)
                summ1 = 0
            print("summ = ", summ)
            print("expected summ = ", 12*500*800)
            print("Sync in ", i)
            i += 12*500
            print("switch to ", i)
        summ = 0
    i = i + 1

print(decoder)
plt.show()

