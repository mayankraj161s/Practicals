# Write a Python Program to Input a list of numbers and swap elements at the even location with the elements at the odd location.
def p2():
    l1 = []
    n = int(input("Enter no. of elements: "))
    for i in range(n):
        e = int(input("Enter element no.{} : ".format(i + 1)))
        l1.append(e)
    print(l1)
    for j in range(n):
        if j%2 != 0:
            l1[j], l1[j-1] = l1[j-1], l1[j]
    print(l1)