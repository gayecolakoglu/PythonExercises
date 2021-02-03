def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y

def factorial(x):
    carpim = 1
    for i in range(x):
        carpim *= i + 1
    return carpim

def squareRoot(x):
    return x**0.5


def base(x, y):
    sonuc = 1
    for i in range(y):
        sonuc = sonuc * x
    return sonuc


while True:
    print("to addition => 1")
    print("to subtraction => 2")
    print("to division => 3 ")
    print("to multiplication => 4")
    print("to factorial => 5")
    print("to take base => 6")
    print("to get square root => 7")
    print("to exit => 0")
    operation = int(input("Please enter the operation you want to do: "))
    print("")

    if operation==5 or operation==7:
        if operation==5:
            number=int(input("Enter the number you want to get the factorial of: "))
            print("Answer:", factorial(number))
        else:
            number = float(input("Enter the number for which you want the square root: "))
            print("Answer:", squareRoot(number))

    elif operation==6:
            number=int(input("Enter the number you want to get the base: "))
            power=int(input("Enter the power of the number: "))
            print("Answer:", base(number, power))
    elif operation==4 or operation==1:
            number1=int(input("Enter the first number: "))
            number2=int(input("Enter the second number: "))
            if operation==4:
                print("Answer:", multiplication(number1, number2))
            else:
                print("Answer:", add(number2, number1))
    elif operation==3:
            dividend=int(input("Enter your dividend: "))
            divisor=int(input("Enter your divisor: "))
            print("Answer:", division(dividend, divisor))
    elif operation==2:
            small=int(input("Enter the number you want to subtract: "))
            big=int(input("Enter the number you want to subtract from: "))
            while big<small:
                print("The first entered value must be smaller than the second entered value, please re-enter!")
                small = int(input("Enter the number you want to subtract: "))
                big = int(input("Enter the number you want to subtract from: "))
            print("Answer:", subtraction(big, small))


    elif operation == 0:
        print("Exiting the program ...")
        break

    else:
        print("You entered an invalid process name.")
        print("")

