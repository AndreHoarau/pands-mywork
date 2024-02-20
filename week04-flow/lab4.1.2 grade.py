# a program that reads in a students percentatge mark and prints out the grade
# program should check the percentatge is valid
#under 40% is fail 
# between 40 and 59% is merit 2
# between 60 and 69% is merit 1 
# over 70% is distinction
# Author Andre Hoarau
grade = float(input("enter the student's grade:"))
if grade < 0 or grade > 100:
    print("please enter a valid grade floar")
elif (grade < 40):
    print("this grade is a fail")
elif (grade >=40 and grade <= 59):
    print("this grade is a merit 2")
elif (grade >= 60 and grade <= 69):
    print("this grade is a merit 1")
elif (grade >= 70):
    print("this grade is a distinction")