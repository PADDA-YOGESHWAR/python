#Inheritance --> single level inheritance--> multi level inheritance --> multiple inheritance
class A:
    def fun1(self):
        print("I am 1st function")
    def fun2(self):
        print("I am 2nd function")
class B(A):#class B is inheriting the properties of A #B is subclass and A is superclass
    def fun3(self):
        print("I am 3rd function")
    def fun4(self):
        print("I am 4th function")
class C(B,A):
    def fun5(self):
        print("I am 5th function")
        
a1=A()
a1.fun1()
a1.fun2()
b1=B()
b1.fun3()
b1.fun4()
print()
b1.fun1()
b1.fun2()
print()
c1=C()
c1.fun1()
print()
print()

#contructor in inheritance and it's behaviour
class a:
    def __init__(self):
        print("in init in a")
    def fun1(self):
        print("I am 1a function")
    def fun2(self):
        print("I am 2a function")
class b(a):
    def __init__(self):#if this method is not defined then init a is performed
        super().__init__()#also uses all the method... calls the inti method from a
        print("in init in b")
    def fun1(self):
        print("I am 1b function")
    def fun2(self):
        print("I am 2b function")
class c(b,a):
    def __init__(self):
        super().__init__()
        super().fun2()
        print("in init in c")
        
a1=a()
print()
b1=b()
print()
c1=c()
c1.fun1()#method resolution order