from time import sleep#scheduler will give us time to handle
from threading import *#importing thread package
class hello(Thread):#inheriting thread class
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)
t1=hello()
t2=hii()
t1.start()#start method is used to invoke the run method that inherited the properties of thread class
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("bye")