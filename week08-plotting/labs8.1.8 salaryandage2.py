# Elaborate on the salary and age programme to include a plot that shows the line y = x^2
# Author Andre Hoarau
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
xaxis= np.array(range(1,101))
yaxis= xaxis * xaxis
plt.plot(xaxis, yaxis, label= "y = x^2", color= "pink")
plt.scatter(agesarray, salaryarray)
plt.show()

