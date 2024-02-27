# this program puts 10 random numbers into a queue
# it then outputs all the numbers into a list
# it then takes the first numnber in the queue states this is the number and shows the new list minus that number until we have one number left
# Author Andre Hoarau
#import random 
#numberlist = [random.randint(1,100) for _ in range(10) ]
# import the random module to generate a random integer better to set a range otherwise could get some very large numbers
# source of above is chat gpt
import random
listofnumbers =[]
listmax = 10
upto= 100
for n in range(0,listmax):
    listofnumbers.append(random.randint(0,upto))
print (f'The queue is: {listofnumbers}')
while len(listofnumbers) !=0:
    currentnumber = listofnumbers.pop(0)
    print (f'current number is {currentnumber} and the queue is {listofnumbers}')
print('The queue is now empty')