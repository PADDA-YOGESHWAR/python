from array import *  #imports the array package
a = array('i',[1,2,3,4,5])
print(a)
print(a.buffer_info()) #returns the address of the array and the size of array
print(type(a))
for i in range(len(a)):
    print(a[i],',',end=" ")
print()
    


newarr= array(a.typecode,(i for i in a))#coping an array
for e in newarr:#printing array using for loop
    print(e)
print()

i=0
while(i<len(newarr)):#printing array using while loop
    print(newarr[i])
    i=i+1
print()

#user input array
arr = array('i',[])#declaring an empty array
n=int(input("Enter the length of the array : "))#reading the size of an array
for i in range(n):
    x=int(input("Enter the value : "))#asking for input using for loop
    arr.append(x)#appending the input to the array
print(arr)

#Searching an element in the array
e = int(input("Enter the element you want to search in the array : "))
k=0
for i in arr:
    if e==arr[i]:
        k=k+1
        print(i)
        break
    else:
        pass
if(k==0):
    print("Element is not found")

#searching the element using functions in the array
print(arr.index(int(input("Enter the element to search by function : "))))


    