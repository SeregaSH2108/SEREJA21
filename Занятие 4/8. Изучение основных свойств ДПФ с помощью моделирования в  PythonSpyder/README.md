# Задание на работу

1. Для заданных значений частоты сигнала и частоты дискретизации получите дискретное колебание, отсчеты посмотрите в Variable Explorer. Далее увеличьте частоту сигнала в несколько раз, при этом так же увеличится и частота дискретизации, но отношение частоты сигнала и частоты дискретизации - нормированная частота останется той же величиной.
Сравните дискретные отсчеты первого и второго сигналов.

2. Вычислите шаг частот между точками ДПФ ∆f =fs/N. Определите, в
какой точке ДПФ находится заданный сигнал.

1. Измените частоту сигнала в целое чисто раз, определите номер точки
ДПФ для данного сигнала.

2. Измените количество точек ДПФ до 512. Вычислите шаг частот между
точками ДПФ ∆f = fs/N. Определите, в какой точке ДПФ находится заданный сигнал.
3. Задайте сигнал в виде суммы двух колебаний. Вычислите ДПФ сигнала.

4. Вычислите ОДПФ сигнала, заданного в частотной области в виде X=np.array([0,0,1]).

Задавайте ненулевое значение в различных разрядах. Также задайте значение в комплексной форме X=np.array([0,0,1j,0,0,0,0,0]), поменяйте знак мнимой единицы, задайте спектр ДПФ в виде X=np.array([0,0,2-1j,0,0,0,0,0]) поменяйте знак мнимой единицы. Можно увеличить количество точек до 16 при одном ненулевом значении.

# Дополнительное задание

Вычислить ДПФ реального WI-FI сигнала, вывести график.