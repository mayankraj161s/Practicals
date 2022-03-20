# Write a Python program to implement the random function random, randint, Randrange using random module.
from random import *
def p7():
    while True:
        print("Random Number Generator")
        print("1) Randrange")
        print("2) Randint")
        print("3) Random")
        print("4) Exit") 
        ch = int(input("Enter choice(1-4): "))
        if ch == 1:
            l = int(input("Enter lower limit: "))
            h = int(input("Enter upper limit: "))
            random_num = randrange(l,h)
            print(random_num)
        elif ch == 2:
            l = int(input("Enter lower limit: "))
            h = int(input("Enter upper limit: "))
            random_num = randint(l,h)
            print(random_num)
        elif ch == 3:
            print(random())
        else:
            break