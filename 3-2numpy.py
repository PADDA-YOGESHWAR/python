#multi dimentional array is not possible by importing array package... so we use numpy
from numpy import *
arr = array([1,2,3,4,5])#1D array using numpy
arr2=array([1,2,3,4,5,6,7],int) #we can also specify the type of elements likr this
print(arr2)
print(arr)

##different ways to handle arrays
#1.array()
a = array([1,2,3,4,5])
print(a,a.dtype)#default the array elements are integers
b=array([1,2,3,4,5.0])
print(b.dtype)#here all the element are converted to float
c=array([1,2,3,4,5],float)
print(c)#all the elements here are converted to float

#2.linspace()
d=linspace(0,16,10)
print(d)

#3.arange()
e=arange(1,15,3)
print(e)

#4.logspace()
f=logspace(1,40,5)
print(f)
print("%.2f"%f[4])

#5.zeros()
g=zeros(5)
print(g)

#6.ones()
h=ones(5)
print(h)
i=ones(5,int)
print(i)
