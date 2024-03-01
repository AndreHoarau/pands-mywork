# Create a program that keeps displaying the menu until the user picks q. if user picks a then do function call do add if user chooses v do a function call doview
# Author Andre Hoarau
def displaymen():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) quit")
    choice= input("Type one letter a,v,q:")

    return choice 
#this is the above function now we test it 
def doview():
    print("in viewing")
 
def doadd():
    print("in adding")
choice= displaymen()
while choice != "q":
    if choice == "a":
        doadd()
    elif choice == "v":
        doview()
    elif choice != "q":
        print("\n\n please select either a,v, or q")
    choice = displaymen()