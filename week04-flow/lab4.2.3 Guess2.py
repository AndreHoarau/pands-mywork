# this program is a continuation of guess 1 where if the guess is too low or too high we will tell the user accordungly
# author Andre Hoarau
guess = int(input("type in a random integer: "))
while guess != 10:
    if guess > 10:
        print(" the number you have entered it too high!")
    else:
        print("the number you have entered is too low!")
    guess = int(input("type in a random integer again: "))
print("You got it correct!")