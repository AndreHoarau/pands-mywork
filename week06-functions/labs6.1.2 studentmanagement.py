# A function that prints out a menu of command to perform, add view and quit. The output returns what the user chose
# Author Andre Hoarau
def displaymen():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) quit")
    choice= input("Type one letter a,v,q:")

    return choice 
#this is the above function now we test it 
choice=displaymen()
print(f" you chose {choice}")