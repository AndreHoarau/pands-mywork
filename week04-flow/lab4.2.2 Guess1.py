# a program that prompts the use to enter a number and if the numebr is not correct prompts them to enter it again until they guess the number
# author Andre Hoarau

guess = int(input("type in a random integer: "))
while guess != 10:
    print("good try but that's wrong please try again")
    guess = int(input("type in a random integer again: "))
print("You got it correct!")