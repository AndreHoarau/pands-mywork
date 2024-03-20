# Write a program that plots the function of y=x^2
# Author Andre Hoarau
import numpy as np
import matplotlib.pyplot as plt

xaxis= np.array(range(1,101))
yaxis= xaxis * xaxis
plt.plot(xaxis, yaxis, label= "y = x^2")
plt.legend()
plt.show()