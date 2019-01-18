
#OLDER METHOD - PYTHON 2
# printing out var number into a string
result = 100/23
print ('the result was {}'.format(result))


# printing out var number into a string using the letter 'r' to
# identify the result in the string

result = 100/23
print ('the result was {r}'.format(r=result))

# Formating for decimal point/length
#
# {value:width.precision f}
# {r:4.4f}
# This formula means we want the print the result rounded to 4 decimal places after the .
# the 'f' states to start after the break.
# The width specifys the white space in the string number

result = 100/23
print ('the result was {r:4.2f}'.format(r=result))

# Outcome
#The result was  4.35

#NEW PYTHON 3 METHOD

name='jose'
age='15'
print('hello his name is {}'.format(name))

#New method - fstrings
print (f'hello his name is {name}')

# formating in with age var
print (f'{name} is {age} years old')
