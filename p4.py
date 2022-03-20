# Write a Python Program to Input a list of numbers and test if a number is equal to the sum of the cubes of its digits. Find the smallest and largest such number from the given list of numbers.
def p4():
    l1 = []
    n = int(input("Enter no. of elements: "))
    for i in range(n):
        e = int(input("Enter element no.{} : ".format(i + 1)))
        l1.append(e)
    print(l1)
    l2 = []
    count = 0
    for i in l1:
        # Checking armstrong number
        num = i
        sum = 0
        while num >= 0:
            a = num%10
            num = int(num/10)
            sum += a**3
            if num == 0:
                break
        var = sum
        if (var == i):
            l2.append(var)
            count += 1
    print(l2)
    print("There are",count,"such numbers.")
    l2.sort()   # Sorting list of armstrong numbers
    # Smallest
    print("Smallest :",l2[0])
    # Largest
    print("Largest :",l2[-1])