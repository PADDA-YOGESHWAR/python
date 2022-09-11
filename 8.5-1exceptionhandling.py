#exception handling
'''
complie time error --> syntax error
logical error--> wrong output comes
runtime error --> wrong input error
'''
#runtime error can be handled and logical error means bugs which are removed by testing in softwear team
a=5
b=2
c=0
try:
    print("Open a file")
    print(a/b)
    print("Still open")
    k=int(input("Enter an input value : "))
    print(k)
except ValueError as e:
    print("please enter valid input",e)
except Exception as e:
    print("something went wrong",e)
    #print("closed the file")
finally:
    try:
        print(a/c)
    #print("closed the file")
    except ZeroDivisionError as e:
        print("Cannot be divided by zero",e)
    print("closed the file successfully")
print("by byeee")