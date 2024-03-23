#Modify the previous programme to make it a bar chart
# Author Andre Hoarau
import numpy as np
import matplotlib.pyplot as plt
listofcounties= ["Dublin", "Kildare", "Galway", "Mayo", "Sligo"]
sizes =[15,30,45,10,60]

plt.bar(listofcounties,sizes)
plt.show()