class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()#creating an object for inner class
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
        def show(self):#this is invoked in line number 8
            print(self.brand,self.cpu,self.ram)

m1=student('Lucky',2)
m2=student('yogesh',1)
print(m1.name,m1.rollno)
m1.show()
print(m1.lap.brand)#accessing the variable by reference
lap1=m1.lap
lap2=m2.lap
print(id(lap1))
print(id(lap2))