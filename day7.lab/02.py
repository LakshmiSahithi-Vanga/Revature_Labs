"""Logging Errors While Processing a List
    You are processing a list of numbers and performing division by each number.
However, some numbers might be zero, which would raise a ZeroDivisionError . Use
Python's logging module to log errors when division by zero occurs and skip those
numbers.
Input:

numbers = [10, 5, 0, 3, 0]
Output:

Logs: "Error: Division by zero encountered for number 0" (logged twice).
Returns: [1.0, 0.5, 0.3333]
"""

import logging
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
def safe_division(numbers, divisor):
    results = []
    for num in numbers:
        try:
            result = divisor / num
            results.append(round(result, 4))
        except ZeroDivisionError:
            logging.error(f"Error: Division by zero encountered for number{num}")
    return results
numbers = [1, 2, 0, 3, 0]
divisor = 1
output = safe_division(numbers, divisor)
print(output)