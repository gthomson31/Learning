import random

inputs = ['back to the future']

for input in inputs:
    # Removes the spacing from the word
    anagram = input.replace(' ', '')
    print (anagram)
    # Converts the name into individual letters in a list
    anagram=list(anagram)
    print (anagram)
    #Shuffles the letters in the list
    random.shuffle(anagram)
    print (anagram)
    # Removes the quotations to make a single item in a list
    anagram = ''.join(anagram)
    print (anagram)
    #Prints the two input values
    print('{},{}'.format(input, anagram))
