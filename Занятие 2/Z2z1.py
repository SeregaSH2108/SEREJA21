import time
import numpy as np
import matplotlib.pyplot as plt
import random

#Сортировка Puthon list
array_0 = []
array_1 = []
array_22  = []
for r in range(10, 5000000, 500000):
    for m in range(r):
        array_22.append(random.random())
    start = time.time()
    array_22.sort()
    end1 = time.time()- start
    array_1.append(end1)
    array_0.append(r)
    print(end1)
    print(r)

#Сортировка Numpy
array_2 = [] #Количество элементов
array_3  = []
array_21 = []
for i in range(10, 5000000, 500000):
    array_21 = np.random.sample(i)
    start = time.time()
    np.sort(array_21)
    end = time.time()- start
    array_2.append(i)
    array_3.append(end)

plt.plot(array_0, array_1, array_2, array_3)
plt.xlabel("Количество элементов")
plt.ylabel("Время сортировки") 

