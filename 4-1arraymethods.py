from xml.etree.ElementPath import find
from numpy import *
arr = array([1,2,3,4,5])
#addition of the arrays
arr = arr + 5 #adding 5 to all the elements of the array
print(arr)
arr2=array([5,4,3,2,1])
print(arr+arr2)#adding 2 arrays
print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(sort(arr))
print(concatenate([arr,arr2]))
print()

#copying an array
arr3=arr
print(arr)
print(arr3)
print(id(arr))
print(id(arr3))
print()

#anotherway -->shallow copy ----> when we change the values for arr the arr4 values also changes
arr4=arr.view()
print(arr)
arr[3]=10
print(arr4)
print(id(arr))
print(id(arr4))

#deepcopy
arr5=arr.copy()
arr[3]=10
print(arr)
print(arr5)
print(id(arr))
print(id(arr5))