# A prgoram that makes a list called salaries that has 10 random numbers (20000-80000)
# Author Andre Hoarau
import numpy as np
salaries= np.random.randint(20000,80001, size=10)
print(salaries)