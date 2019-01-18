# Dictonaries use {} and : to seperate signfy the keys and there associated
# values

my_dict = {'key':'value','key1':'value1','key3':'value3'}

print (my_dict)
print (my_dict['key1'])


prices_lookup = {'Apples':5.99,'Carrots':2.43,'Macbook':1000000}

print (prices_lookup['Macbook'])


d = {'k1':123,'k2':[1,2,3],'k3':{'inside key':432}}


# Calling items

print (d.keys())
print (d.values())
print (d.items())

print (d['k2'])
print (d['k3'])
print (d['k3']['inside key'])
print (d['k2'][2])

d = {'key1':['a','c','b']}

my_list= d['key1']
print (my_list)

letter = my_list[2]

print (letter)

# Uppercase the letter
print (letter.upper())


#or

print (d['key1'][2].upper())



# adding to dict


b = {'key1':100,'key2':200}

b['key3'] = 300

print (b)



# overwriting a value to dict


f = {'key1':100,'key2':200}

f['key1'] = 300

print (f)
