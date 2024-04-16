# Calculate and print the means of the grades of the DF
# Author: Andre Hoarau
import pandas as pd
Datalist = [
 ['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df= pd.DataFrame(Datalist, columns=['name','subject', 'grade'])
mean = df['grade'].mean()
print(mean)