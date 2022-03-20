import p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
i = 0
while i == 0:
    ch = int(input("ENTER CHOICE(1-10): "))
    if ch == 1:
        p1.p1()
    elif ch == 2:
        p2.p2()
    elif ch == 3:
        p3.p3()
    elif ch == 4:
        p4.p4()
    elif ch == 5:
        p5.p5()
    elif ch == 6:
        p6.p6()
    elif ch == 7:
        p7.p7()
    elif ch == 8:
        p8.p8()
    elif ch == 9:
        p9.p9()
    elif ch == 10:
        p10.p10()
    c = input("Want to continue?(y/n) ")
    if c.lower() == "y":
        i = 0
    else:
        i = 1
