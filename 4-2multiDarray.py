from numpy import *
arr = array([
    [1,2,3],
    [4,5,6]
])
print(arr)
print(arr.dtype)#returns the type of data elements present in the array
print(arr.ndim)#returns the dimentions weather it is 1D or 2D etc...
print(arr.shape)#returns the shape like mxn in matrix
print(arr.size)#returns the number of elements
arr2=arr.flatten() #2D array is converted into 1D array
print(arr2)
print()
arr3 = array([
    [1,2,3,4,5,6],
    [7,8,9,0,1,2]
])
arr4 = arr3.reshape(3,4) #shapes the array in the shape we need but here m*n == arr3.size
print(arr4)
print()

arr5=arr3.reshape(2,2,3)#it returns a 3D array in which contains 2 2D arrays
print(arr5)
print()

#matrices
arr6=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
m=matrix(arr6)#converting array to matrix. the main reason to convert an array to matrix is to perform more number of operations
print(m)
m2=matrix('1 2 3;4 5 6;7 8 9')
print(diagonal(m2))
print(m.min())
print(m.max())
print()

print(m+m2)
print(m*m2)
