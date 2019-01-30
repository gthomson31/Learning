myfile = open('test.txt')
myfile.read()
# resets the cursur position
myfile.seek(0)

# Read in the contents of the the txt file and store as var
# my_new_file then set the method as .read

# when calling contents you will see the output of the file

with open('test.txt') as my_new_file:
    contents = my_new_file.read()

# Write only access to a file
with open('test.txt', mode='w') as myfile:
    contents = myfile.read()

# Read/write access to a file
with open('test.txt', mode='rw') as myfile:
    contents = myfile.read()

# Append  to a file 
with open('test.txt', mode='rw') as myfile:
    contents = myfile.read()
