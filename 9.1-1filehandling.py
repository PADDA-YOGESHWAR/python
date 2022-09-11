from asyncore import write
f=open(r"C:\Users\USER\OneDrive\Desktop\programming\python\4\demo.txt",'r')
print(f)#returns the type of the information like encoding and mode of operation
print(f.read())#prints the complete data
print(f.readline(),end="")#prints only 1st line
print(f.readline())#pointer moves to next line and prints the 2nd line
print(f.readline(3))#prints the line number 3 as we mentioned the line number here
f2=open(r"C:\Users\USER\OneDrive\Desktop\programming\python\4\write.txt",'w')#here if we won't have any file existing at that path it will create a blank file
f2.write("something")#writing that text into that file but evert time it rewrites the data by clearing the before data it means the data is overridden
f3=open(r"C:\Users\USER\OneDrive\Desktop\programming\python\4\write.txt",'a')#to overcome the previous problem we have opened the file in append mode
f3.write(" successful")#this text will be added to that text before

#coping complete data from 1 file to another file
f4=open(r"C:\Users\USER\OneDrive\Desktop\programming\python\4\copy.txt",'w')#creating another blank file and opening it in write mode
for data in f :#for loop to run complete data
    f4.write(data)#copies complete data 
f5=open(r"C:\Users\USER\OneDrive\Desktop\programming\python\4\dog.jpg",'rb')
f6=open(r"C:\Users\USER\OneDrive\Desktop\programming\python\4\mydog.jpg",'wb')
for i in f5:
    f6.write(i)