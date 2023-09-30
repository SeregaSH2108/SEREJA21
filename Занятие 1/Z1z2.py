import numpy as np

array_2 = []

array_0 = np.random.randint(-1000, 1000, 1024)

array_1 = np.sort(array_0)

print(array_1)

array_2 = array_1[array_1 >= 0]

print(array_2)
