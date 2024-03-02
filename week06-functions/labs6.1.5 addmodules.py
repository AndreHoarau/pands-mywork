# this program will iterate on the previous program and will look to add the modules component and will quit when an empty module is entered.
# Author Andre Hoarau

def readmodules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    while moduleName != "":
         module = {}
         module["name"]= moduleName
 # I am not doing error handling
         module["grade"]=int(input("\t\tEnter grade:"))
         modules.append(module)
 # now read the next module name
         moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules
print(readmodules())
    
# I really struggled with this i need to look into and understand dictionaries more 



