import numpy as np
import matplotlib.pyplot as plt

n = 1021 # Количество точек
A = 5 # Амплитуда
fi = 60 # Начальная фаза 
f = 10 # Частота

t = np.linspace(0, 1, n)
x = A*np.sin((2*np.pi*t*f)+fi)
y = A*np.cos((2*np.pi*t*f)+fi)

plt.plot(t, x)
plt.title("A*sin(w*f*t)")
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.figure()
plt.plot(t, x, t, y)
plt.title("A*sin(w*f*t), A*cos(w*f*t)")
plt.xlabel("Время")
plt.ylabel("Амплитуда")