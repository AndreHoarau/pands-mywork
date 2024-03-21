# Elaborating on the previous programme except adding a label to plot and set the titles and labels on the acis.
# author Andre Hoarau
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
plt.title("Age and Salary Scatter plot vs y=x^2")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.plot(xaxis, yaxis, label= "y = x^2", color= "pink")
plt.scatter(agesarray, salaryarray)
plt.show()
