# reads in a string and strips any leading or trailing spaces also convert the string to lower case/ also out put the length of the input and the output string
# Autho Andre Hoarau
input= input('Please input a string: ')
normalsstring = input.lower().strip()
lengthofinput= len(input)
lenfthofnormal = len(normalsstring)
print('The string normalised is: {}'.format(normalsstring))
print('We reduced the input string from {} to {} characters' .format(lengthofinput, lenfthofnormal))
