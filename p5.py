# Write a Python Program to Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have marks above 75.
def p5():
    d1 = {}
    students = int(input("Enter no. of students: "))
    for i in range(students):
        name = input("Enter Name: ")
        roll_no = int(input("Enter roll no: "))
        marks = int(input("Enter marks: "))
        d1[roll_no] = [name, marks]
    # Display names of students who got marks more than 75
    for i in d1:
        if d1[i][1] > 75:
            print(d1[i][0])