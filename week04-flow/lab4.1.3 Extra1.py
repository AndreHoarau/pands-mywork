# This program will incorporate labs 4.1.1 and 4.1.2 to consider the rounding of percentages eg 69.5 to 70% and therefore giving a distinction and not a merit 1
# Author Andre Hoarau
grade = float(input("enter the student's grade:"))
if grade < 0 or grade > 100:
    print("please enter a valid grade floar")
elif (grade <= 39 and grade % 10 < 5):
    print("this grade is a fail")    
elif (grade >= 39 and grade % 10 > 5 and grade <= 59):
    print("this grade is a merit 2")
elif (grade >= 59  and grade % 10 > 5 and grade <= 69 ):
    print("this grade is a merit 1")
elif (grade >= 69 and  grade %10 >5):
    print("this grade is a distinction")

print ("sanity")