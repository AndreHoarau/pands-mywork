#Quiz from the lab
#Author Andre Hoarau
'''1.
a. Look at the program below, if the file test-a.txt does not exist. What will
happen when the program runs?
# when it is finished with it
with open("test-a.txt") as f:
 data = f.read()
 print (data)
# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()
'''
# Answer A: As the file name does not exist this should throw an error.
'''b. Look at the program below, if the file test-b.txt does not exist, what will be
outputted to the console when this program is run?
c. What will the contents of the file test-b.txt be when this program is run?'''
'''# the with statement will automatically close the file
# when it is finished with it
with open("test-b.txt", "w") as f:
 data = f.write("test b\n") # returns the number of
chars written
 print (data)
with open("test-b.txt", "w") as f2: # open file again
 data = f2.write("another line\n")
 print (data)
'''
#Answer B: As this file is opened in write mode it will create the file the console will output "another line" as this is in write mode the last write will overwrite the previous one.
    #7
    #13
    #This is because the write function returns the number of characters
    #writing to the file this includes the new line character, I have not
    #tested this on a windows machine(it may be one more).

#Answer c: when the file is run the contents will be just another line
'''d. Look at the modified program below, what will the contents of the file be
after this program is run.'''
'''# The with statement will automatically close the file
# when it is finished with it
with open("test-d.txt", "w") as f:
 data = f.write("test d\n") # returns the number of
chars written
 print (data)
with open("test-d.txt", "a") as f2: # open file again
 data = f2.write("another line\n")
 print (data)'''

#Answer D: the contents of the console will be  test d (new line) another line as we are using an append here instead of a write 
