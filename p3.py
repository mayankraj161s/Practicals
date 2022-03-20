# Write a Python Program to Input a list/tuple of elements, search for a given element in the list/tuple and frequency and position of search element.
def p3():
    l1 = []
    n = int(input("Enter no. of elements: "))
    for i in range(n):
        e = int(input("Enter element no.{} : ".format(i + 1)))
        l1.append(e)
    print(l1)
    search = eval(input("Enter the element to be searched: "))
    count = l1.count(search)
    for i in l1:
        if search == i:
            print("Element is present at position",l1.index(search))
            print("Frequency:",count)
            break
    if count == 0:
        print("Element not present")