#This is a basic list

print('We have set the value of our list my_list=[1,2,3]')
my_list=[1,2,3]

# A list can be built up of integers and strings
my_list=['cat','dog',3,24]

# How many items are in my list
print(len(my_list))

# finding items in a list
my_list = ['one','two','three']

# what is in postion 1 ?

print(my_list[1])

# what comes between postion 2 and end of my list

print(my_list[2:])

another_list=['four','five']

#concatonate the list and print result
print(my_list + another_list)


#concatonate the list and store result in a var called 'new list'
print ('new_list = my_list + another_list')

new_list = my_list + another_list


new_list[0] = 'ONE ALL CAPS'

print (new_list)



# add to the end of a List

new_list.append('six')
print (new_list)


new_list.append('seven')
print (new_list)


# remove to the end of a List

new_list.pop()
print (new_list)


popped_item = new_list.pop()
print (f'i have removed the item {popped_item} from the list')

one = new_list.pop(0)
print (one)


# sort in place - does not return
new_list=['t','j','c','s','r']
num_list=[30,4,6,2,7,3,9]

new_list.sort()
num_list.sort()

print (new_list)
print (num_list)

# reverse in place - does not return
new_list.reverse()
num_list.reverse()

print (new_list)
print (num_list)
