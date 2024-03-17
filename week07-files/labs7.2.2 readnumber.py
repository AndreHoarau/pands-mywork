# This program will read in a number from a file that already exists (count.txt) by calling a function and outputting a number
FILENAME = "pands-mywork\week07-files\labs7.2.1 count.txt"
#this is the constant variable above to the file name 
def read_number():
    with open (FILENAME) as f:
        number = int(f.read())
        return number 
#this is the function that opens the file and then converts the txt to an int and reads it and then returns the number 
num= read_number()
print (num)  
#this then prints that number 
