import numpy as np
from numpy.lib import stride_tricks

#Дан вектор [1, 2, 3, 4, 5], построить новый вектор с тремя нулями между каждым значением
Z=([1, 2, 3, 4, 5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0,'\n')

#Поменять 2 строки в матрице
A = np.arange(25).reshape(5,5)
A[[0,1]] = A[[1,0]]
print(A,'\n')

#Рассмотрим набор из 10 троек, описывающих 10 треугольников (с общими вершинами), найти множество уникальных отрезков, составляющих все треугольники
faces = np.random.randint(0,100,(10,3))
F = np.roll(faces.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = np.sort(F,axis=1)
G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )
G = np.unique(G)
print(G,'\n')

#Дан массив C; создать массив A, что np.bincount(A) == C
C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print(A,'\n')

#Посчитать среднее, используя плавающее окно
def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
print(moving_average(np.arange(20), 3),'\n')

#Дан вектор Z, построить матрицу, первая строка которой (Z[0],Z[1],Z[2]), каждая последующая сдвинута на 1 (последняя (Z[-3],Z[-2],Z[-1]))
def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.itemsize, a.itemsize)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
Z = rolling(np.arange(10), 3)
print(Z,'\n')

#Инвертировать булево значение, или поменять знак у числового массива без создания нового
Z = np.random.randint(0,2,100)
np.logical_not(Z, out=Z)

Z = np.random.uniform(-1.0,1.0,100)
np.negative(Z, out=Z)

#Посчитать ранг матрицы
Z = np.random.uniform(0,1,(10,10))
rank = np.linalg.matrix_rank(Z)

#Найти наиболее частое значение в массиве
Z = np.random.randint(0,10,50)
print(np.bincount(Z).argmax(),'\n')

#Извлечь все смежные 3x3 блоки из 10x10 матрицы
Z = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (Z.shape[0] - n)
j = 1 + (Z.shape[1] - n)
C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
print(C,'\n')

#Рассмотрим множество матриц (n,n) и множество из p векторов (n,1). Посчитать сумму p произведений матриц (результат имеет размерность (n,1))
p, n = 10, 20
M = np.ones((p,n,n))
V = np.ones((p,n,1))
S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
print(S,'\n')

#Дан массив 16x16, посчитать сумму по блокам 4x4
Z = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                       np.arange(0, Z.shape[1], k), axis=1)

#Найти n наибольших значений в массиве
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

print (Z[np.argpartition(-Z,n)[:n]],'\n')

#Построить прямое произведение массивов (все комбинации с каждым элементом)
def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = map(len, arrays)

    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]

    return ix

print(cartesian(([1, 2, 3], [4, 5], [6, 7])),'\n')

#Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B, независимо от порядка элементов в B
A = np.random.randint(0,5,(8,3))
B = np.random.randint(0,5,(2,2))

C = (A[..., np.newaxis, np.newaxis] == B)
rows = (C.sum(axis=(1,2,3)) >= B.shape[1]).nonzero()[0]
print(rows,'\n')

#Дана 10x3 матрица, найти строки из неравных значений (например [2,2,3])
Z = np.random.randint(0,5,(10,3))
E = np.logical_and.reduce(Z[:,1:] == Z[:,:-1], axis=1)
U = Z[~E]
print(Z)
print(U,'\n')

#Преобразовать вектор чисел в матрицу бинарных представлений
I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
print(np.unpackbits(I[:, np.newaxis], axis=1),'\n')

#Дан двумерный массив. Найти все различные строки
Z = np.random.randint(0, 2, (6,3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print(uZ,'\n')

#Даны векторы A и B, написать einsum эквиваленты функций inner, outer, sum и mul
A=np.random.random(10)
B=np.random.random(10)
np.einsum('i->', A)       # np.sum(A)
np.einsum('i,i->i', A, B) # A * B
np.einsum('i,i', A, B)    # np.inner(A, B)
np.einsum('i,j', A, B)    # np.outer(A, B)