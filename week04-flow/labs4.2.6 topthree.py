# write out a program that prints out 10 random numbers between 0-100 it then prints out the top three numbers 
# author Andre Hoarau
howmany = 10
topmany = 3
lowrange= 0
highrange= 100
numbers=[]
import random
for i in range(0,howmany):
    numbers.append(random.randint(lowrange,highrange))
print(f'{howmany} random numbers\t {numbers}')

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print(f"the top {topmany} is are {topOnes[0: topmany]}")