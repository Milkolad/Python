from queue import Queue
import time

class Customer(object):
 
    def __init__(self, number):
        """Constructor"""
        self.number = number
    
    def come(self):
        return "Покупатель %s пришел" % self.number 
    
    def leave(self):
        return "Покупатель %s ушел" % self.number

    def order(self,q):
        q.put(self.number)
        if(not(q.empty())): print("Покупатель",self.number,"встает в очередь"); 
        return self.number
    
    def wait(self,q):
        q.put(self.number)
        return "Покупатель %s ожидает выдачи заказа" % self.number


class Cashier(object):

    def __init__(self, q, name="Вася"):
        self.name = name
        self.q=q

    def service(self):
        return  "Кассир %s начинает обслуживать покупателя %s" % (self.name, self.q.get()) 

    def servcomplete(self):
        return "Кассир %s завершил обслуживание" % self.name

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
        return "Выдача заказа %s покупателю"% self.q.get()


cass=Queue()
deliv=Queue()

b=Cashier(cass)
c=Delivery(deliv)

for i in range(1,3):
    a=Customer(i)
    print(a.come())
    if(cass.empty()):print(b.shout())
    a.order(cass)
    if(not(cass.empty())):print(b.service()); print(b.servcomplete())
    
    
    #print(a.wait(deliv))
   # if(not(deliv.empty):print(c.collect())
    #print(c.dev())
    #print(a.leave())
    




