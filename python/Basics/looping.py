# x = 10
#
# while x > 0:
#     print (x)
#     x = x - 1
# print ('we are done with the loop')

x = 10
while x > 0:
    print (x)
    x = x - 1
    if x < 5:
        print ('x now has a value Less than 5')
        break
print ('we are done with the loop')

# Second Example This time using a ==

var = 10
while var > 0:
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
        break

print ("Good bye!")


# Breaks in a name
for letter in 'edinburgh':
   if letter == 'u':
      break
   print ('Current Letter :', letter)
   
