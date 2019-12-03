#a=int(input())
#b=int(input())
#c=int(input())

#print(a,b,c)

#class FuzzyTriangular(object):

lst=[]
print("Введите A")
s=input()
print(s)
symb=""


for ch in s:
    #print(ch)
    if((ch!=',')&(ch!="/")&(ch!=" ")): symb+=ch
    elif(symb!=""): lst.append(symb); symb="" 


print(lst[0],lst[1], lst[2], lst[3], lst[4], lst[5])

"""for a in lst:
    print(a)"""
    