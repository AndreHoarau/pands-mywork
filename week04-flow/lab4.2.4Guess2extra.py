# this program is a continuation of guess 2 where we generate a random number between 0-100 and checks it againf the correct numbet
# author Andre Hoarau
import random
guess = random.randint(0, 100)
while guess != 10:
    if guess > 10:
        print(" the number you have entered it too high!")
    else:
        print("the number you have entered is too low!")
    guess = random.randint(0, 100)
print("You got it correct!")
