# a program that takes in numbers until the user enters 0 once 0 is entered the program then prints each of the entered values and provides the average
# Author Andre Hoarau
enternumbers= []
enternumber = int(input('type in a number 0 will quit:'))
while enternumber !=0:
    enternumbers.append(enternumber)
    enternumber = int(input('type in a number 0 will quit:'))

for value in enternumbers:
    print(value)

average = sum(enternumbers)/ len(enternumbers)
print ( " the average is", average)