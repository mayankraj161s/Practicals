def p9():
    f_dict = {}
    while True:
        print("1) Add Friends Details")
        print("2) Display the list of all your friends")
        print("3) Add another friend")
        print("4) Delete a particular friend of the record")
        print("5) Modify the phone no. of the existing friend")
        print("6) Search for a friend")
        print("7) Display the record in sorted order according to the names of friends")
        print("8) Exit")
        choice = int(input("Enter your choice(1-8):"))
        if choice == 1:
            n = int(input("Enter the no. of entries: "))
            for i in range(n):
                name = input("Enter name: ")
                phone = int(input("Enter phone no. "))
                f_dict[name] = phone
        elif choice == 2:
            print("*"*20,"Friend\'s details","*"*20)
            print("NAME"," "*20,"PHONE NO.")
            print("-"*58)
            for i in range(len(f_dict)):
                print(list(f_dict.keys())[i].ljust(25," "),list(f_dict.values())[i])
            print("-"*58)
        elif choice == 3:
            name = input("Enter name: ")
            phone = int(input("Enter phone no. "))
            f_dict[name] = phone
            print("The modified dictionary: ",f_dict)
        elif choice == 4:
            name = input("Enter name: ")
            del f_dict[name]
        elif choice == 5:
            name = input("Enter name of friend whose phone no. is to be modified: ")
            phone = int(input("Enter phone no. "))
            f_dict[name] = phone
        elif choice == 6:
            name = input("Enter name of friend to search: ")
            s = f_dict.get(name)
            if s == "None":
                print("Friend not found.")
            else:
                print("Friend found.")
        elif choice == 7:
            a = dict(sorted(f_dict.items()))
            print("*"*20,"Friend\'s details","*"*20)
            print("NAME"," "*20,"PHONE NO.")
            print("-"*58)
            for i in range(len(a)):
                print(list(a.keys())[i].ljust(25," "),list(a.values())[i])
            print("-"*58)
        elif choice == 8:
            break
        else:
            print("Incorrect input")
            break