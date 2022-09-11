'''
THERE ARE 4 TYPES OF POLYMORPHISMS IN PYTHON
1.Duck Typing
2.operator overloading
3.method overloading
4.method overriding
'''
#Duck Typing
from operator import truediv


class VScode:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Executed")
class myeditor:
    def execute(self):
        print("My own IDE")
class laptop:
    def code(self,ide):#here the argument ide doesn't depend on which ide it is it must have a method execute... here polymorphism is done by changing the ide type...
        ide.execute()

ide=VScode()   
ide1=myeditor()     
lap1=laptop()
lap1.code(ide)
lap1.code(ide1)
print()

#operator overloading
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
s1=student(34,56)
s2=student(56,89)
s3=s1+s2
print(s3.m1)
if s1.m1>s2.m1:
    print("s1 wins")
else:
    print("s2 wins")
    
print(s1)
print()

#method overloading -->same meythod name but the arguments are different.. number of arguments are different.. in python it is not possible because we cannot create 2 methods with same name
class std:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None,d=None):
        s=0
        if a!=None and b!=None and c!=None and d!=None:
            s=a+b+c+d
        elif a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
a=std(19,20)
print(a.sum(2,4))
#method overriding--> by inheritance
class A:
    def show(self):
        print("In A show")
class B(A):
    def show(self):
        print("In B show")
a1=B()
a1.show()
