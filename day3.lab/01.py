# Write a Python program that generates a random DNA sequence of length 20 using the 
# characters A , T , C , and G . Use a list comprehension to create the sequence.

# Example Output:
# ['A', 'T', 'G', 'C', 'A', 'G', 'T', 'C', 'A', 'T', 'G', 'C', 'A', 'T', 'G','C', 'A', 'T', 'G', 'C']

import random

print([random.choice('ATCG') for i in range(20)])
