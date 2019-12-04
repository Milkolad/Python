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

    lenght=(len(x)*len(y))//4
    arr=np.zeros((lenght,3), dtype=float)
    count=0

    for i in range(0,len(x),2):
        for j in range(0,len(y),2):
            arr[count][0]=x[i]
            arr[count][1]=y[j]
            arr[count][2]=x[i+1]*y[j+1]
            count+=1
    print(arr,"\n")
    
    for i in range(lenght):
        arr[i,1]=min(arr[i,0],arr[i,1])
    
    arr=arr[arr[:,2].argsort()]
    arr=arr[:,1:3]
    print(arr)

    res=[]
    myiter=iter(range(lenght))
    for i in myiter:
        if((np.count_nonzero(arr==arr[i][1]))==1): res.append(arr[i][0]); res.append(arr[i][1])
        else: 
                maximum=arr[i][0]
                for j in range(np.count_nonzero(arr==arr[i][1])-1):
                    print(i)
                    print(arr[i][0])
                    maximum=max(arr[i][0],maximum)
                    i=next(myiter,None)
                res.append(maximum)
                res.append(arr[i-1][1])
    
    return res

def main()
    A=[]
    B=[]
    print("Введите A")
    #string=input()
    string="0.7/2+1/3+0.6/4"
    scan(string, A)
    printf(A)
    print("Введите B")
    #string=input()
    string="0.8/3+1/4+0.5/6"
    scan(string, B)
    printf(B)
    A=list(map(float,A))
    B=list(map(float,B))
    C=mult(A,B)
    C=list(map(str,C))
    printf(C)