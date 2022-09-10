#lambda is used in place of single expression fucntions
l=lambda a:a*a
print(l(5))
print()

m=lambda a,b:a+b
print(m(3,5))

#filter
nums=[1,2,3,4,5,6,7,8]
'''
def is_even(nums):
    return nums%2==0
'''
evens =list(filter(lambda n:n%2==0,nums))
print(evens)
print()

#map
'''
def update(nums):
    return nums+2
'''
doubles = list(map(lambda n:n+2,evens))
print(doubles)
print()

#reduce
from functools import reduce
'''
def add_all(a,b):
    return a+b
'''
sum =reduce(lambda a,b : a+b,doubles)
print(sum)
print()

#decorators
def div(a,b):
    print(a/b)
div(2,4)#here the function returns 0.5
print()
#but when we want a spicial feature like always highest number must be in numerator we use the following function
def smart_work(fun):
    def inner(c,d):
        if(c<d):
            c,d=d,c
        return fun(c,d)
    return inner
div2=smart_work(div)
div2(2,4)
print()

#modules in python 
#--> complex project in real world are made into simple
#debuging --> removing bugs... codeing --> adding bugs
#we need to read and understand the code while debuging it 
#so make a complex project the work is broken into modules which won't effect other modules... we can also reuse the modules
