import numpy as np
import matplotlib.pyplot as plt

n = 21

t = np.linspace(0, 1, n, endpoint=True)

x = np.sin(np.pi*t) + np.sin(2*np.pi*t) + np.sin(3*np.pi*t) + np.sin(5*np.pi*t)

fig = plt.figure(figsize=(15, 5), dpi=100)
plt.grid()
plt.xlabel("Амплитуда")
plt.ylabel("Время")
plt.title("Aналоговый")
plt.plot(t, x)
fig = plt.figure(figsize=(15, 5), dpi=100)
plt.grid()
plt.xlabel("Амплитуда")
plt.ylabel("Интервал дискретизации")
plt.title("Дискретный")
plt.stem(t, x)
fig = plt.figure(figsize=(15, 5), dpi=100)
plt.grid()
plt.xlabel("Уровпень")
plt.ylabel("Время")
plt.title("Квантованный")
plt.step(t, x)
fig = plt.figure(figsize=(15, 5), dpi=100)
plt.title("3 графика")
plt.plot(t, x)
plt.stem(t, x)
plt.step(t, x)