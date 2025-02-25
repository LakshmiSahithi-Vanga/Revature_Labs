#closest to zero

def closest_to_zero(nums):
    return min(nums, key=lambda x: (abs(x), -x))

# Example usage
numbers = [-10, 5, -3, 7, 2, -2, 1]
print(closest_to_zero(numbers))  # Output: 1
