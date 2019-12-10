print("Введите число (от 0 до 511)")
a=int(input())
if((a<0)|(a>511)): print("Неправильное число")
else:
    ar=[['111','110','101','100','011','010','001','000'], ['0','0','0','0','0','0','0','0']]
    for i in reversed(range(8)):
        #print(a%2)
        ar[1][i]=str(a%2)
        a=a//2
        print(ar[1][i])
        
    b=['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0']
    c=[]
    print(b)
    i=0
    
    while(i!=len(b)-2):
        string=b[i]+b[i+1]+b[i+2]
        #print('str'+string)
        for j in range(8):
            #print(ar[0][j])
            if(string==ar[0][j]): del b[i]; c.append(ar[1][j])
            
        #print(b)
        print(c)
        #i+=1
    
    #print(b)