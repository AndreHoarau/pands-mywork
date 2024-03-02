# combining all the components 
# Author: Andre Hoarau
def displaymen():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) quit")
    choice= input("Type one letter a,v,q:")

    return choice 
def doadd(students):
    currentstudent = {}
    currentstudent ["name"] = input("enter name: ")
    currentstudent ["module"] = readmodules()

    students.append(currentstudent)

def readmodules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    while moduleName != "":
         module = {}
         module["name"]= moduleName

         module["grade"]=int(input("\t\tEnter grade:"))
         modules.append(module)
 # now read the next module name
         moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules
# the main program

def doview(students):
    print (students)
    
students= []
choice = displaymen()
while choice != "q":
    if choice == "a":
        doadd(students)
    elif choice == "v":
        doview(students)
    elif choice != "q":
        print("\n\n please select either a,v, or q")
    choice = displaymen()