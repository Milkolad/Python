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
        return "Покупатель %s ушел" % self.number

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


def que(number,qc,qd,cash,deliver):
    cust=Customer(number)
    print(cust.come())
    if(qc.empty()):print(cash.shout())
    cust.order(qc)
    if(not(qc.empty())): print(cash.service(number)); print(cash.servcomplete()); print(cust.wait(qd))
    if(not(qd.empty())): print(deliver.collect()); print(deliver.dev()); print(cust.leave())


cass=Queue()
deliv=Queue()
b=Cashier(cass)
c=Delivery(deliv)
thr1=Thread(target=que, args=(1,cass,deliv,b,c))
thr2=Thread(target=que, args=(2,cass,deliv,b,c))


thr1.start()
time.sleep(2)
thr2.start()
thr1.join()
thr2.join()
#for i in range(1,3):
    #thr1=Thread(target=que, args=(i,cass,deliv,b,c))
  #  thr[i-1].start()
  #  thr[i-1].join()