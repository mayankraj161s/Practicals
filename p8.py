# Write a Python program to implement the statistics functions (mean, median, mode) using statistics module.
from statistics import *
def p8():
    while True:
        print("Statistics: Mean, Mode, Median")
        print("1) Mean")
        print("2) Median")
        print("3) Mode")
        print("4) Exit") 
        ch = int(input("Enter choice(1-4): "))
        if ch == 1:
            lst = []
            n = int(input("Enter no. of integers whose mean is to be calculated: "))
            for i in range(n):
                e = float(input("Enter number no.{} : ".format(i + 1)))
                lst.append(e)
            print("Mean",mean(lst))
        elif ch == 2:
            lst = []
            n = int(input("Enter no. of integers whose median is to be calculated: "))
            for i in range(n):
                e = float(input("Enter number no.{} : ".format(i + 1)))
                lst.append(e)
            print("Median",median(lst))
        elif ch == 3:
            lst = []
            n = int(input("Enter no. of objects whose mode is to be calculated: "))
            for i in range(n):
                e = float(input("Enter number no.{} : ".format(i + 1)))
                lst.append(e)
            print("Mode",mode(lst))
        else:
            break