import numpy as np

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
c=[[0,0,0],[0,0,0],[0,0,0]]

ma=np.matrix(a)
mb=np.matrix(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print()
    

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print()
print()


if len(b) != len(a[0]): print("Нельзя")

else:
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(b)):
                c[i][j]+=a[i][k]*b[k][j]
            print(c[i][j], end=' ')
   
        print()
    
print("\n Проверка: \n", ma*mb) 