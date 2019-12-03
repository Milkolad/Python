
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
    arr=[[],[3]]

    for i in range(len(x)*len(y)):
        arr[i].append(0)
    
    arr[0][0]=0
    arr[1][0]=1
    print(arr[0][0])
    print(arr[1][0])

"""
    for i in range(3):
        print("i",i)
        for j in range(0,len(x),2):
            print("j",j)
            #arr[i+j][0]=x[j]
            for k in range(0,len(y),2):
                print("k",k)
               # arr[i+j][1]=y[k]
                #arr[i+j][2]=x[j+1]*y[k+1]"""
    
   




A=[]
B=[]
print("Введите A")
string=input()
scan(string, A)
#print(A)
printf(A)
print("Введите B")
string=input()
scan(string, B)
printf(B)

mult(A,B)