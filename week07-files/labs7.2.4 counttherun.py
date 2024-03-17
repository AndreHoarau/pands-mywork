# This program will use the 2 suggested solutions from the previous questions to count how many times the program has been run. 
#Author Andre Hoarau
FILENAME = "pands-mywork\week07-files\labs7.2.1 count.txt"
def readNumber():
 with open(FILENAME) as f:
    number = int(f.read())
    return number
# test it
num = readNumber()
def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number)) 

num = readNumber()
num += 1
print(f" we have run this program {num} times")
writeNumber(num)
#here we read the number and then add 1 to it before writing out the number of times we have run it and writing that numebr to it 
