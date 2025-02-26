#Nested List Comprehension - Matrix Transposition
#Given a matrix represented as a list of lists, use a nested list comprehension to transpose the matrix.
#Input:
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Expected Output:
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# Original matrix (2x3)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpose using nested list comprehension
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Print transposed matrix
print("Transposed Matrix:")
for row in transpose:
    print(row)
