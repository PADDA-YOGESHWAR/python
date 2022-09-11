class demo:#declared class name
    def hey(self):#declared class methods / functions
        print("Hey.. hw r u")
hi=demo() #creating an object to the class
hi2 = demo()
print(type(hi))
demo.hey(hi)#calling the methods of class by class reference
demo.hey(hi2)
hi.hey()#calling by object reference
hi2.hey()
