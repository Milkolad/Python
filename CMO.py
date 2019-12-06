from queue import Queue
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

    def service(self,number):
        return  "Кассир %s начинает обслуживать покупателя %s" % (self.name, number) 
        

    def servcomplete(self):
        amount = random.randint(5, 10)
        time.sleep(amount)
        return "Кассир %s завершил обслуживание покупателя %s" % (self.name, self.q.get())

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
        return "Выдача заказа %s покупателю"% self.q.get()


def quecass(cust,qc,qd,cash,deliver):
    print(cust.come())
    if(qc.empty()):print(cash.shout())
    cust.order(qc)
    if(not(qc.empty())): print(cash.service(cust.number)); print(cash.servcomplete()); print(cust.wait(qd)); 
   
def quedev(qd,deliver,cust):
    if (not(qd.empty())): print(deliver.collect()); print(deliver.dev()); print(cust.leave())


cass=Queue()
deliv=Queue()
b=Cashier(cass)
c=Delivery(deliv)
length=30


for i in range(1,length+1):
    cu=Customer(i) 
    thr1=Thread(target=quecass, args=(cu,cass,deliv,b,c))
    thr2=Thread(target=quedev, args=(deliv,c,cu))
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    time.sleep(2)
   
#костыль
if(not(deliv.empty())):
    cus=Customer(length)
    thr2=Thread(target=quedev, args=(deliv,c,cus))
    thr2.start()
    thr2.join()