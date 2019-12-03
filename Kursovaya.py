
lst=[]
print("Введите A")
s=input()
print(s)
symb=""


for ch in s:
    #print(ch)
    if((ch!=',')&(ch!="/")&(ch!=" ")): symb+=ch
    elif(symb!=""): lst.append(symb); symb="" 


for a in lst:
    print(a)
    