# Write a Python Program to find the largest / smallest number in a list/tuple and displaying the position of that number
def p1():
    l1 = []
    n = int(input("Enter no. of elements: "))
    for i in range(n):
        e = int(input("Enter element no.{} : ".format(i + 1)))
        l1.append(e)
    print(l1)
    l2 = l1.copy()
    for j in range(n-1):
        for k in range(n-j-1):
            if l2[k] > l2[k+1]:
                l2[k], l2[k+1] = l2[k+1], l2[k]
    print("Maximum : ",l2[-1])
    print("Position : ",l1.index(l2[-1]))
    print("Minimum : ",l2[0])
    print("Position : ",l1.index(l2[0]))