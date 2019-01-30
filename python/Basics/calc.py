global x
x = 1
def main():
    global x
    print ("\n\n\n1.) Addition\n2.) Subtraction\n3.) Multiplication\n4.) Division\n5.) Free Hand\n6.) Exit")
    choice = int(input("Pick an option (1-6):  "))
    if choice == 1:
        Addition()
    elif choice == 2:
        Subtraction()
    elif choice == 3:
        Multiplication()
    elif choice == 4:
        Division()
    elif choice == 5:
        Free()
    elif choice == 6:
        x = 0
    else:
        print ('Invalid Choice!')

def Addition():
    x = int(input("First number:  "))
    y = int(input("Second number: "))
    print ('Your result is:  ' + str(x+y))

def Subtraction():
    x = int(input("First number:  "))
    y = int(input("Second number: "))
    print ('Your result is:  ' + str(x-y))

def Multiplication():
    x = int(input("First number:  "))
    y = int(input("Second number: "))
    print ('Your result is:  ' + str(x*y))

def Division():
    x = int(input("First number:  "))
    y = int(input("Second number: "))
    print ('Your result is:  ' + str(x/y))

def Free():
    x = input("First number:  ")
    print (eval(x))

while x == 1:
    main()
