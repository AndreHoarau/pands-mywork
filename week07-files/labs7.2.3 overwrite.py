#This program will take in a number and overwrite a file with that number.
#Author Andre Hoarau
FILENAME = "pands-mywork\week07-files\labs7.2.1 count.txt"
def overwrite():
    with open (FILENAME, "r+") as f:
        number = int(f.read())
        newnumber = number + 1
        f.write(str(newnumber))
        return newnumber
num = overwrite()
print (num)
'''def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
 f.write(str(number))
# test it
writeNumber(3)
'''
#Andrew's solution in comment above I feel my way also works it is just slightly different