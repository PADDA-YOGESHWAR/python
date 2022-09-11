'''there are 3 types of methods
1.Instance methods
2.class methods
3.static methods
'''
#instance method --> instance methods are also of 2types 1.accessor methods--to fetch the value 2.mutator methods--> to modify the value
class student:
    college ="MVGR"
    @classmethod#class variable
    def get_collegename(cls):#class methods.. to access class varibles
        return cls.college
    @staticmethod#static methods
    def info():
        print("This is a student class")
    
    def __init__(self,m1,m2,m3):#here m1,m2,m3 are instance variables
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):#accessors as they onlu fetch the value
        return self.m1
    def set_m1(self,value):#mutators as they change the value
        self.m1=value
s1=student(34,23,44)
s2=student(25,35,45)
print(s1.m1)#fetching the value by object variable
s1.set_m1(20)
print(s1.get_m1())#fetchig the value by method

print(s1.avg())
print(student.get_collegename())
student.info()