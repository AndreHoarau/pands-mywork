# Add a sheet called summary.
# Author Andre Hoarau
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
path = "./week10-PANDAS"
excelfilename = path + 'grades.xlsx'
with pd.ExcelWriter(excelfilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")