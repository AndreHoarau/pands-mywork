# program that takes in the input of an amount in of a float with or without negative bank will take it as an amount in cent the absolute amount in cent 
# author Andre Hoarau
amount= input('input the amount: ')
modifyamount= abs(float(amount))
cents= int(modifyamount * 100)
print('the amount in cent is: {}'.format(cents))