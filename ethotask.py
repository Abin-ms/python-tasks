
def maths(a , b ):
    print("1.addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Exit")
    value = int(input("Enter your choice"))
    
    
    match value:
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
        case 5:
            mod(a,b)
        case 6:
            power(a,b)
        case 7:
            return "exiting.... \n Exited"
        case _:
            print("Invalid choice")

def add(a,b):
    c = a + b
    print(c)

def sub(a,b):
    c = a - b
    print(c)

def mul(a,b):
    c = a * b
    print(c)

def div(a,b):
    c = a / b
    print(c)

def mod(a,b):
    c = a % b
    print(c)

def power(a,b):
    c = a**b
    print(c)


a = int(input("Enter the first value"))
b = int(input("Enter the second value"))
maths(a,b)


   


