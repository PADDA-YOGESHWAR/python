import math
print(8/4)#we gwt 2.0 here keep in mind that .0 comes as / returns float value
print(5/2)#here we get 2.5
print(5//2)#// is a integer division operator returns 2
#print(8+9-) this will give error as this is incomplete operation
print('Lucky')#strings must be in single or double quotes
#print('navins's laptop') --syntax error and the alternatives follows
print("Lucky's laptop")
#print('navin's "laptop"') -- error and alternative follows
print("navin\'s laptop")
print("c:\docs\nikhil")#\n is to print in nextline
print(r"c:\docs\nikhil")#raw string doesn't read \n as nextline
#in python IDLE terminal _ is used to take privious output as input
 #y=3
 #9+10
 #_+y  --here it prints 22 because 19+3 is 22 and _ is used to take previous output
print("yogesh" + "lucky") #string concatination operator is + returns yogeshlucky
name = "lucky"
print(name[1]+" "+name[-1]+" "+name[2:4]+" "+name[1:]+" "+name[:5]+" "+name[0:5:2]+" "+name[::-1])
#name[0:3]='my' -- strings are immutable so we can't change and gets TypeError

#Lists
nums=[1,2,3,4,5]
print(nums)
#nums[54] --returns IndexError : out of range
nums.append(5)
print(nums)
nums.insert(3,0)#lists arem mutable
print(nums)
nums.remove(0)
print(nums)
nums.pop(1) #1 indexed element is poped out
print(nums)
nums.pop()#last element is rmeoved
print(nums)
del nums[2:]
print(nums)
nums.extend([6,7,8,9])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print(nums.sort())

#Tuples
tup=(1,2,3,4,5)
#tup[1]=33 tuples are immutables --TypeError
print(tup.count(2))#counts the number of occurence of 2 in the tuple
print(tup.index(3))#returns the index of 3 in the tuple

#sets
s={1,2,3,4,5}
print(s)#unodered collection
#sets won't support indexing == TypeError
#sets must not support duplicate values

#Dictionary
data = {1:'ok',2:'no'}
#print(data[4]) --KeyError as 4 key is not there in the dictionary
print(data[1])
print(data.get(3))#returns none as no element is there at index 3
print(data.get(1,'Not found'))
print(data.get(3,"Not found"))
keys = [1,2,3]
values = ['no','ok','done']
data=dict(zip(keys,values))
print(data)
data[4]="yes"
print(data)
prog = {'js':'atom','cs':'vs','python':['pycharm','subline'],'java':{'jse':'netbeans','jee':'elipse'}}
print(prog['python'][1])
print(prog['java']['jee'])

#to know abt python completely
#help()-->topics-->Lists-->quit
#help("lists")
print(help("LISTS"))

#variables
num = 5
print(id(num))
num2=num #both of them will have same address
print(id(num2))
print(id(5))
num=10 #value changes so address also changes of num
print(id(num))
print(id(num2))#num2 is refering to num so remains same
print(type(num))#returns the datatype of element stored in num

#data types
#none, 
#numberic -->int,float,complex(complex(a,b)--a+bj),bool--true or false
#Lists[]
#tuples()
#set{}
#String""
#dictionary{keys: values } --  d.keys(),d.values()

#Arithemetic operations *,-,+,/
#assaignment operators =,+=,-=,*=,/=,  a,b=5,6
#relational operators <,>,==,<=,>=,!=
#logical operators and,or,not

#conversion of number system in python
print(bin(25))#retruns binary number of an integer
print(oct(25))
print(hex(25))

#SWAPPING LOGICS
a=5
b=3

temp=a 
a=b
b=temp

a=a+b
b=a-b
a=a-b

a=a^b
b=a^b
a=a^b

a,b=b,a 

print(~12)#returns -13
#bitwise operators... here the digits are converted to binary and performs logic and gives output as digit again
#~,&,|,^,<<,>>
print(math.sqrt(25))
print(math.floor(2.9))
print(math.ceil(2.2))
print(math.pow(3,2))
print(math.pi)
print(math.e)
import math as m
print(m.sqrt(9))


''' to run python in command promt 
python filename.py
'''
''' default input in python is string '''