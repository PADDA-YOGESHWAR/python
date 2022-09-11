class demo:#declared class name
    def __init__(self,accept,num):
        self.accept='accept'
        self.num = num
        print("in intit")
    def hey(self):#declared class methods / functions
        print("Hey.. hw r u",self.accept,self.num)
    def compare(self,others):
        if self.num == others.num :
            return True
        else:
            return False
        
        
hi=demo("ok",33) #creating an object to the class --> objects are stored in heap memory
hi2 = demo('done',44)
print(id(hi))# objects are stored in heap memory and constructor is responsible to allocate that memory
print(id(hi2)) #the size of the object depends upon the number of variables we have in the class
hi.hey()#calling by object reference
hi2.hey()
if hi.compare(hi2):
    print("They are same")
else:
    print("They are different")
print(hi.accept)
print(hi2.accept)
#changing the values in the class by using object reference
hi.accept='sare'
hi.num=24
print(hi.accept)
print(hi.num)


#namespace is an area where you create and store object/variabl... -> there are 2 types of namespaces  1.classnamespace--stores all class varibles 2.object/instancenamespace--> where we will create an instance variables
#there are two types of variables --> 1. instance variable and 2.class(Static) variable
class car:
    wheels=4#if we define he variables outside the __inti__ it becomes a class variable -->belongs to classnamespace
    
    
    def __init__(self):#defining a variable inside __init__ it becomes an instance variable--> beongs to instancenamespace
        self.milage = 10
        self.company ='BMW' #these are instance variables because as the value in object changes this values also changes
        
c1=car()
c2=car()
print(c1.milage,c1.company,c1.wheels)
car.wheels=5
print(c2.milage,c2.company,c2.wheels)
c1.milage= 0
print(c1.milage)