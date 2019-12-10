print("Введите число (от 0 до 255)")
a=int(input())
print("Введите количество прогонов") #сколько раз полностью преобразовать вектор
count=int(input())
if((a<0)|(a>255)): print("Неправильное число")
else:
    ar=[['111','110','101','100','011','010','001','000'], ['0','0','0','0','0','0','0','0']]
    for i in reversed(range(8)):
        ar[1][i]=str(a%2)
        a=a//2

    b=[]  
    c=[] 

    b.append(['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0'])

    for k in range(count):
        for i in range(len(b[0])):
            if(i==0):string="0"+b[k][i]+b[k][i+1]; 
            elif(i==(len(b[0])-1)): string=b[k][i-1]+b[k][i]+"0"; 
            else:string=b[k][i-1]+b[k][i]+b[k][i+1]
            for j in range(8):
                if(string==ar[0][j]): c.append(ar[1][j]);
        b.append(list(c))
        c.clear()
    
    for i in range(count+1):
        print(*b[i])