import numpy as np
import scipy.spatial

#Перемножить матрицы 5x3 и 3x2
A = np.dot(np.ones((5,3)), np.ones((3,2)))
print(A,"\n")

#Дан массив, поменять знак у элементов, значения которых между 3 и 8
A = np.arange(11)
print(A)
A[(3 < A) & (A < 8)] *= -1
print(A,"\n")

#Создать 5x5 матрицу со значениями в строках от 0 до 4
A = np.zeros((5,5))
A += np.arange(5)
print(A,"\n")

#Есть генератор, сделать с его помощью массив
def generate():
    for x in range(10):
        yield x
A = np.fromiter(generate(),dtype=float,count=-1)
print(A,"\n")

#Создать вектор размера 10 со значениями от 0 до 1, не включая ни то, ни другое
A = np.linspace(0,1,12)[1:-1]
print(A,"\n")

#Отсортировать вектор
A = np.random.random(10)
A.sort()
print(A,"\n")

#Проверить, одинаковы ли 2 numpy массива
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal,"\n")

#Сделать массив неизменяемым
A = np.zeros(10)
A.flags.writeable = False
#A[0] = 1

#Дан массив 10x2 (точки в декартовой системе координат), преобразовать в полярную
A = np.random.random((10,2))
X,Y = A[:,0], A[:,1]
R = np.hypot(X, Y)
T = np.arctan2(Y,X)
print(R)
print(T,"\n")

#Заменить максимальный элемент на ноль
A = np.random.random(10)
A[A.argmax()] = 0
print(A,"\n")

#Создать структурированный массив с координатами x, y на сетке в квадрате [0,1]x[0,1]
A = np.zeros((10,10), [('x',float),('y',float)])
A['x'], A['y'] = np.meshgrid(np.linspace(0,1,10),
                             np.linspace(0,1,10))
print(A,"\n")

#Из двух массивов сделать матрицу Коши C (Cij = 1/(xi - yj))
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C),"\n")

#Найти минимальное и максимальное значение, принимаемое каждым числовым типом numpy
for dtype in [np.int8, np.int32, np.int64]:
   print(np.iinfo(dtype).min)
   print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
   print(np.finfo(dtype).min)
   print(np.finfo(dtype).max)
   print(np.finfo(dtype).eps)

#Напечатать все значения в массиве
#np.set_printoptions(threshold=np.nan)
A = np.zeros((25,25))
print(A,"\n")

#Найти ближайшее к заданному значению число в заданном массиве
A = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(A-v)).argmin()
print(A[index],"\n")

#Создать структурированный массив, представляющий координату (x,y) и цвет (r,g,b)
A = np.zeros(10, [ ('position', [ ('x', float, 1),
                                   ('y', float, 1)]),
                    ('color',    [ ('r', float, 1),
                                   ('g', float, 1),
                                   ('b', float, 1)])])
print(A,"\n")

#Дан массив (100,2) координат, найти расстояние от каждой точки до каждой
A = np.random.random((10,2))
D = scipy.spatial.distance.cdist(A,A)
print(D,"\n")

#Преобразовать массив из float в int
A = np.arange(10, dtype=np.int32)
A = A.astype(np.float32, copy=False)

'''Дан файл:
1,2,3,4,5
6,,,7,8
,,9,10,11
Как прочитать его?
->A = np.genfromtxt("file.dat", delimiter=",")'''

#Каков эквивалент функции enumerate для numpy массивов?
A = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(A):
    print(index, value)
for index in np.ndindex(A.shape):
    print(index, A[index],"\n")

#Сформировать 2D массив с распределением Гаусса
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.hypot(X, Y)
sigma, mu = 1.0, 0.0
G = np.exp(-((D - mu) ** 2 / (2.0 * sigma ** 2)))
print(G,"\n")

#Случайно расположить p элементов в 2D массив
n = 10
p = 3
A = np.zeros((n,n))
np.put(A, np.random.choice(range(n*n), p, replace=False), 1)

#Отнять среднее из каждой строки в матрице
X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)

#Отсортировать матрицу по n-ому столбцу
A = np.random.randint(0,10,(3,3))
n = 1  # Нумерация с нуля
print(A)
print(A[A[:,n].argsort()],"\n")

#Определить, есть ли в 2D массиве нулевые столбцы
A = np.random.randint(0,3,(3,10))
print((~A.any(axis=0)).any(),"\n")

#Дан массив, добавить 1 к каждому элементу с индексом, заданным в другом массиве (осторожно с повторами)
A = np.ones(10)
I = np.random.randint(0,len(A),20)
A += np.bincount(I, minlength=len(A))
print(A,"\n")

#Дан массив (w,h,3) (картинка) dtype=ubyte, посчитать количество различных цветов
w,h = 16,16
I = np.random.randint(0, 2, (h,w,3)).astype(np.ubyte)
F = I[...,0] * 256 * 256 + I[...,1] * 256 + I[...,2]
n = len(np.unique(F))
print(np.unique(I),"\n")

#Дан четырехмерный массив, посчитать сумму по последним двум осям
#A = np.random.randint(0,10, (3,4,3,4))
#sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
#print(sum,"\n")

#Найти диагональные элементы произведения матриц
A=np.random.random((3,3))
B=np.random.random((3,3))
print(A,"\n")
print(B,"\n")
print(np.diag(np.dot(A, B)))