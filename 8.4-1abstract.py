#python doesn't support abstract classes directly
from abc import ABC, abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("It's running")
class whiteboard:
    def write(self):
        print("its writing")
class programmer:
    def work(self,com):
        print("solving bugs")
        com.process()
#com=computer()--> gives error
com1=laptop()
com2=whiteboard()
prog1=programmer()
prog1.work(com1)
#prog1.work(com2)-->gives error
com1.process()