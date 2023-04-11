import math



def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def divide(x, y):
    if y==0:
        return "cannot divide zero!!!"
    return x/y

def multiply(x, y):
    return x*y

def square(x):
    return x*x

def sqrt(x):
    return math.sqrt(x)

def cube(x):
    return x*x*x

def pow(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)


print("!!!!!!!!Welcome to Calculator Application!!!!!!!!")

while(True):
    print("Select the operation you want to perform: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Power")
    print("8. Square Root")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Exit")
    choice = int(input("Enter your operation number: "))

    if choice==12:
        print("Exiting the Application")
        break

    elif choice==11 or choice==10 or choice==9 or choice==8 or choice==6 or choice==5:
        num_one = int(input("Enter number: "))

        if choice==11:
            print("The tan of the ", num_one," is ",tangent(num_one))

        elif choice==10:
            print("The cosine of the ",num_one," is ",cosine(num_one))

        elif choice==9:
            print("The sine of the ",num_one," is ",sine(num_one))

        elif choice==8:
            print("The square root of the ",num_one," is ",sqrt(num_one))

        elif choice==6:
            print("The cube of ",num_one," is ",cube(num_one))


        elif choice==5:
            print("The square of ",num_one," is ",square(num_one))





    else:
        number1 = int(input("Enter number: "))
        number2 = int(input("Enter next number: "))

        if choice==1:
            print("Addition of ",number1," and ",number2," is ",add(number1, number2))


        elif choice==2:
            print("Subtraction of ",number1," and ",number2," is ",subtract(number1, number2))

        elif choice==3:
            print("multiplication of ",number1," and ",number2," is ",multiply(number1, number2))


        elif choice==4:
            print("division of ",number1," and ",number2," is ",divide(number1, number2))


        elif choice==7:
            print("Power of ",number1," and ",number2," is ",pow(number1, number2))











