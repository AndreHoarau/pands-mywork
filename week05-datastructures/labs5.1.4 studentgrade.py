# a program that stores a student name and a list of her course and grades in a dictionary. the programe should then print out her data.
#number of course she has could change 
# Author Andre Hoarau
student = {"Name":"Mary",
           "modules":[
               {
                   "Coursename":"Programming",
                     "grade":45,
               },
               {
                   "Coursename":"History",
                   "grade":99
               }
           ]
}

print(f"Student: {student['Name']}")
for module in student ['modules']:
    print (f"\t {module['Coursename'], module['grade']}")