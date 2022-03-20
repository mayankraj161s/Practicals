# Write a Python Program to implement python maths function/method (pi, e, sqrt, ceil, floor, pow, fabs, sin, cos, tan) using math module.
import math
def p6():
    while True:
        print("Math functions")
        print("1) Pi value")
        print("2) e constant")
        print("3) Square root")
        print("4) Ceil()")
        print("5) Floor()")
        print("6) Pow()")
        print("7) Fabs()")
        print("8) Sin")
        print("9) Cos")
        print("10) Tan")
        print("11) Exit")
        ch = int(input("Enter your choice from 1-11 : "))
        if ch == 1:
            print(math.pi)
        elif ch == 2:
            print(math.e)
        elif ch == 3:
            num = float(input("Enter number: "))
            print("Square root:",math.sqrt(num))
        elif ch == 4:
            num = float(input("Enter number: "))
            print(math.ceil(num))
        elif ch == 5:
            num = float(input("Enter number: "))
            print(math.floor(num))
        elif ch == 6:
            num = float(input("Enter number: "))
            pow = float(input("Enter power: "))
            print(math.pow(num, pow))
        elif ch == 7:
            num = float(input("Enter number: "))
            print(math.fabs(num))
        elif ch == 8:
            angle = float(input("Enter angle(in degrees): "))
            a_rad = angle*math.pi/180
            print(math.sin(a_rad))
        elif ch == 9:
            angle = float(input("Enter angle(in degrees): "))
            a_rad = angle*math.pi/180
            print(math.cos(a_rad))
        elif ch == 10:
            angle = float(input("Enter angle(in degrees): "))
            a_rad = angle*math.pi/180
            print(math.tan(a_rad))
        elif ch == 11:
            print("Exiting........")
            break