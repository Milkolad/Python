from queue import Queue
from collections import deque
from threading import Thread
import time
import random

class Customer(object):
 
    def __init__(self, number):
        """Constructor"""
        self.number = number
    
    def come(self):
        return "Покупатель %s пришел" % self.number 
    
    def leave(self):
        return "Покупатель ушел" 

    def order(self,q):
        if(not(q.empty())): print("Покупатель",self.number,"встает в очередь"); 
        q.put(self.number)
        return self.number
    
    def wait(self,q):
        q.put(self.number)
        return "Покупатель %s ожидает выдачи заказа" % self.number


class Cashier(object):

    def __init__(self, q, name="Вася"):
        self.name = name
        self.q=q

    def service(self):
        print("Кассир",self.name," начинает обслуживать покупателя")

    def servcomplete(self,qd):
        amount = random.randint(4, 7)
        time.sleep(amount)
        self.cu=self.q.get()
        self.cust=Customer(self.cu)
        print("Кассир", self.name, "завершил обслуживание покупателя ", self.cu)
        print((self.cust).wait(qd))


    def shout(self):
        return '%s кричит: "Свободная касса!"' % self.name

    def turn(self, q):
        self.q=q
        return q




class Delivery(object):

    def __init__(self, q):
        self.q=q

    def collect(self):
        return "Сбор заказа"  

    def dev(self):
        amount = random.randint(5, 10)
        time.sleep(amount)
        cu=self.q.get()
        cust=Customer(cu)
        print("Выдача заказа,покупателю", cu)
        print(cust.leave())
        
        
def quecass(qc,qd,cash,deliver):
    while(not(cass.empty())):
        if(qc.empty()):print(cash.shout())
        if(not(qc.empty())): cash.service(); cash.servcomplete(qd) 
   
def quedev(qd,deliver):
    while((not(cass.empty()))|(not(deliv.empty()))):
        #print(not(cass.empty()))
        #print(not(deliv.empty()))
        if (not(qd.empty())): print(deliver.collect()); deliver.dev()

def people(qc,lenght):
    for i in range(1,lenght+1):
        cust=Customer(i)
        print(cust.come())
        cust.order(qc)
        amount = random.randint(2, 7)
        time.sleep(amount)



cass=Queue()
deliv=Queue()
b=Cashier(cass)
c=Delivery(deliv)
lenght=4 #длина очереди


thr1=Thread(target=quecass, args=(cass,deliv,b,c))
thr2=Thread(target=quedev, args=(deliv,c))
thr3=Thread(target=people, args=(cass,lenght))
thr3.start()
time.sleep(0.2)
thr1.start()
thr2.start()
thr1.join()
thr2.join() 
thr3.join()