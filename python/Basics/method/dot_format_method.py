
# Suplementing into a string
print ("this is a {} string".format("banana"))

#inserts the strings in the order they are presented
print ("the {} {} {}".format('fox','brown','quick'))

#inserts the strings in specified order they are presented
print ("the {2} {1} {0}".format('fox','brown','quick'))


# Passing in variable identifiers into a string
print ('the {q} {b} {f}'.format(f='fox',q='quick',b='brown'))
