#passing a list to a function and return the list

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[1,2,3,4,5,6]
even,odd=count(lst)
print(even,odd)
print("Even = {} and odd = {}".format(even,odd))
print()

#fibonacci sequence up to n terms without recursion using function and for loop
def fib(n):
    if(n<0):
        print("Enter +ve input: ")
    else:
        a=0
        b=1
        if(n==1):
            print(a)
        else:
            print(a)
            print(b)
            for i in range (2,n):
                c=a+b
                a,b=b,c
                print(c)
fib(5)
print()

#nth term in fibnacci sequence
def fibn(n):
    a=0
    b=1
    if(n<0):
        print("Enter valid input")
    else:
        if(n==0):
            print(a)
        else:
            for i in range(0,n-2):
                c=a+b
                a,b=b,c
            print(c)
fibn(5)
print()

#Factorial of a number without recursion
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
fact(5)

#there is a recurssion limit when a function call itself
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
print()

#factorial of a number using recursion
def factr(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factr(n-1)
print(factr(5))
print()


#fibanocci sequence number of nth term using recursion
def fibr(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibr(n-2)+fibr(n-1)
print(fibr(5))
print()

#fibanocci sequence upto n terms using recursion
def fibr(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibr(n-2)+fibr(n-1)
for i in range(1,6):
    print(fibr(i))
print()

#gcd of 2 numbers using recursion
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(12,38))
print()

#towers of henoi using recusrcion
def TOH(n , A, B, C):
    if n==1:
        print ("Move disk 1 from source",A,"to destination",B)
        return
    TOH(n-1, A, C, B)
    print ("Move disk",n,"from source",A,"to destination",B)
    TOH(n-1, C, B, A)
TOH(5,'A','B','C')
print()