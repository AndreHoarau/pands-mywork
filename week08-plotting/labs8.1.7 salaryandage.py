# A program that makes a list ages that has the same number random values as salaries range 21-65 making a scatter plot of this data.
# Author Andre Hoarau
# Salaries from earlier program 
import numpy as np 
import matplotlib.pyplot as plt
minsalary= 20000
maxsalary = 80000
numberentries= 10
np.random.seed(1)
salaryarray= np.random.randint(minsalary,maxsalary,numberentries)
print(salaryarray)
minage= 21
maxage= 65
numberages=10
agesarray= np.random.randint(minage,maxage, numberages)

plt.scatter(agesarray, salaryarray)
plt.show()