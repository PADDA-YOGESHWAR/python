#functions are used to make complex tasks into parts as make the work simple
#funtions are of 2 types.. 1) which performs a task and 2) which returns a value
def fun():
    print("Hello")#just printing 
fun()
print()
for i in range(3):
    fun()
print()


def add(x,y):
    return x+y#returning only one value here 
print(add(5,4))
print()

def add_sub(x,y):
    return x+y,x-y #returns to values in a tuple format
print(add_sub(4,5))
print()

result1,result2=add_sub(3,2)
print(result1)
print(result2)
print(print())

#passing the arguments to the funtion
def update(x):
    print(id(x))#same address
    x=8#local
    print(id(x))#when value changes address is also changed
    print(x)
    print()
a=10#global
print(id(a))
update(a)#pass by reference --> it uses the memory where x is stored
update(10)#pass by value --> it takes different memory
print(a)

#types of arguments
def sum(x,y):
    print(x+y)
sum(4,5)
print()

#1)position
def person(name,age=20):
    print(name)
    print(age-5)
    print()
person("Lucky",21)

#2)sequence
person(age=21,name="Lucky")

#3)default
person('lucky')

#4)variable length
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
    print()
sum(5,6,7,3,2)


#keyworded variable length argument
def person(name,*data):
    print(name)
    print(data)
    print()    
person("Lucky",28,"HYD","12345678")
#here in the above example you observe that data is displayed but it won't say what data it is


def persons(name,**data):#we use doble star and mention what data it is while passing the arguments to solve the problem
    print(name)
    print(data)#redturns like a dictionary datatype
    for i,j in data.items():
        print(i,j)#it prints key, value pairs
    print()
    
persons("Lucky",age=28,city="HYD",mob="12345678")

#scope of the variable

a=10#global variable
b=20
c=30
e=50
print(id(c))
def some():
    global e#here we are mentioning that to use global value inside the function also
    e=25#we tried to change the value of c -> global one
    print("fun e=",e)
    a=15#local variable
    print("The value of c in the function with local scope = ",c)
    d=globals()['c']#d=globals() is for all the variables
    print(id(d))#we observe that we can use global variable access to d
    print("The value of d = ",c)
    #now if we try to change the value of d it will create a new variable and new memory will be allocated
    globals()['c']=15#so we use this code to change the value of global varible
    print("The value of c in the function after changing = ",c)
    print("No local variable but b = ",b)
    print("inside the function",a)
print("the value of c before changing in the function = ",c)    
some()
print("e =",e)   
print("outside the function",a)
print("The value of c after the function is being exectuted = ",c)