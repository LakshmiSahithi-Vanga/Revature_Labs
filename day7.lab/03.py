""" Analyzing Sales Data with Dictionaries
You are given a dictionary where keys are product names and values are lists of
sales amounts for each month. Calculate the total sales for each product and return a new
dictionary with the product names as keys and their total sales as values.
Input:

sales_data = {
"Product A": [100, 200, 150],
"Product B": [50, 75, 100],
"Product C": [300, 250, 400]
}
output:

{
"Product A": 450,
"Product B": 225,
"Product C": 950
}
"""

def calculate_total_sales(sales_data):
    return {product: sum(sales) for product, sales in sales_data.items()}
sales_data = {
"Product A": [100, 200, 150],
"Product B": [50, 75, 100],
"Product C": [300, 250, 400]
}
total_sales = calculate_total_sales(sales_data)
print(total_sales)