#1 задание
import numpy as np

#2 задание
print(np.__version__,"\n")
np.show_config()

#3 задание
V=np.zeros(10)
print(V,"\n")

#4 задание
V1=np.ones(10)
print(V1,"\n")

#5 задание
V2=np.full(10, 2.5)
print(V2,"\n")

#6 задание
#python -c "import numpy; numpy.info(numpy.add)"

#7 задание
V3=np.zeros(10)
V3[4]=1
print(V3,"\n")

#8 задание
V4=np.arange(10,50)
print(V4,"\n")

#9 задание
V4=V4[::-1]
print(V4,"\n")

#10 задание
A=np.arange(9).reshape(3,3)
print(A,"\n")

#11 задание
F=np.nonzero([1,2,0,0,4,0])
print(F,"\n")

#12 задание
A1=np.random.random((3,3,3))
print(A1,"\n")

#13 задание
A2=np.random.random((10,10))
print(A2,"\n")
print(A2.min(), A2.max(),"\n")

#14 задание
V5=np.random.random(30)
print(V5.mean(),"\n")

#15 задание
A3=np.ones((10,10))
A3[1:-1, 1:-1]=0
print(A3,"\n")

#16 задание
print(0*np.nan)
print(np.nan==np.nan)
print(np.inf>np.nan)
print(np.nan-np.nan,"\n")

#17 задание
A4=np.diag(np.arange(1,5),k=-1)
print(A4,"\n")

#18 задание
A5=np.zeros((8,8),dtype=int)
A5[1::2,::2]=1
A5[::2,1::2]=1
print(A5,"\n")

#19 задание
print(np.unravel_index(100,(6,7,8)),"\n")

#20 задание
A6=np.tile(np.array([[0,1],[1,0]]), (4,4))
print(A6)