# A Programme that takes a list of counties 5 and make  a pie chart of the counties.
# Author Andre Hoarau
import numpy as np
import matplotlib.pyplot as plt
listofcounties= ["Dublin", "Kildare", "Galway", "Mayo", "Sligo"]
sizes =[15,30,45,10,60]

plt.pie(sizes, labels= listofcounties)
plt.show()