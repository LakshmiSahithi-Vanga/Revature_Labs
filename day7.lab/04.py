"""Sorting Tuples Based on Math Operations
You are given a list of tuples, where each tuple contains two integers. Sort the
list based on the sum of the two integers in descending order. If two tuples have the same
sum, sort them by the first integer in ascending order.

data = [(3, 5), (1, 8), (4, 4), (2, 6)]

[(1, 8), (2, 6), (3, 5), (4, 4)]
"""

def sort_tuples(data):
    return sorted(data, key=lambda x: (-sum(x), x[0]))
data = [(3, 5), (1, 8), (4, 4), (2, 6)]
sorted_data = sort_tuples(data)
print(sorted_data)