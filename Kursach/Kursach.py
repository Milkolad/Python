import numpy as np

def scan(s,v):
    symb=""
    for ch in s:
        if((ch!='+')&(ch!="/")&(ch!=s[-1])): symb+=ch
        elif((symb=="")&(ch==s[-1])): v.append(ch)
        elif(symb!=""): v.append(symb); symb="" 

def printf(v):
    count=0
    for i in range(len(v)//2):
        if(v[i]!=v[-1]): print(v[count]+"/"+v[count+1], end=''); count+=2
        if(i!=(len(v)//2)-1): print("+", end='')
    print()

def mult(x,y):
    arr=np.zeros((9,3), dtype=float)
    count=0

    for i in range(0,len(x),2):
        for j in range(0,len(y),2):
            arr[count][0]=x[i]
            arr[count][1]=y[j]
            arr[count][2]=x[i+1]*y[j+1]
            count+=1
    print(arr)
    
   
   




A=[]
B=[]
print("Введите A")
#string=input()
string="0.7/2+1/3+0.6/4"
scan(string, A)
#print(A)
printf(A)
print("Введите B")
#string=input()
string="0.8/3+1/4+0.5/6"
scan(string, B)
printf(B)
A=list(map(float,A))
B=list(map(float,B))
mult(A,B)