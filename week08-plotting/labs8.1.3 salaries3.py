# A prgoram that makes a list called salaries that has 10 random numbers (20000-80000)
# Author Andre Hoarau
'''import numpy as np
salaries= np.random.randint(20000,80001, size=10)
print(salaries)
# After feedback
import numpy as np 
minsalary= 20000
maxsalary = 80000
numberentries= 10
salaryarray= np.random.randint(minsalary,maxsalary,numberentries)
print(salaryarray)'''
# Elaborating on this we are going to make this program generate the same set of random numbers 

# After feedback
#Elaborate more in this instance to hadd 5000 to the salaries
import numpy as np 
minsalary= 20000
maxsalary = 80000
numberentries= 10
np.random.seed(1)
salaryarray= np.random.randint(minsalary,maxsalary,numberentries)
print(salaryarray)
salaryarrayextra= salaryarray + 5000
print(salaryarrayextra)
