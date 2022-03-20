def p10():
    string = input("Enter a string: ")
    d = {}
    for i in string:
        d[i] = string.count(i)
    print(d)