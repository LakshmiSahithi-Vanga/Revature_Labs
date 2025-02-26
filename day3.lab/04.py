# Question 4: Generator Comprehension - FibonacciSequence
# Create a generator comprehension that generates the first 10 numbers of the Fibonaccisequence.

#Expected Output (when converted to a list):
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
