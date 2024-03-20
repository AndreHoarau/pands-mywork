# A prgoram that makes a list called salaries that has 10 random numbers (20000-80000)
# Author Andre Hoarau
'''import numpy as np
salaries= np.random.randint(20000,80001, size=10)
print(salaries)
'''
# After feedback
import numpy as np 
import matplotlib.pyplot as plt
minsalary= 20000
maxsalary = 80000
numberentries= 10
np.random.seed(1)
salaryarray= np.random.randint(minsalary,maxsalary,numberentries)
print(salaryarray)

#This program will now take the above program and use it to make a histogram of salaries.

plt.hist(salaryarray)
plt.show()