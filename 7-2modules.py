from Calc import add #imported all the methods from the module
print(add(4,5))#directly called
print()

import Calc #imported only module 
print(Calc.add(4,5)) #called by calc.
print()

#special name 
#print(__name__)#it prints __main__ which is stating point of the program

import Calc
print("Demo says "+__name__)#as we imported and trying to run main so it will print the name of the module and also print statement in calc replacing name of the module in place of __main__... here Demo says __main__ will be ouTput
print()

'''
def main():
    print("hello")
    print("welcome user")
    
if __name__ =="__main__":
    main()
'''