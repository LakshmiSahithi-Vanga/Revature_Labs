# Set Comprehension - Unique Characters in a String
# Write a Python program that uses a set comprehension to extract all unique alphabetic
# characters from a given string, ignoring case.

# Input:
# text = "Hello World!"

#output:
# {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
from collections import OrderedDict
text = "Hello World!"
# it prints in random order 
# print({char.lower() for char in text if char.isalpha()})

#if we do not use char.isalpha() then it include the spaces
# print({char.lower() for char in text})

# we want to print in the specified order

a = OrderedDict.fromkeys([char.lower() for char in text if char.isalpha()])
print(f"{{{','.join(a.keys())}}}") 