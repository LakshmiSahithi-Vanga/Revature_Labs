# You are given a list of tuples containing user data in the format (name, age, city) .
# Create a dictionary comprehension that maps each user's name to their age, but only
# include users who are older than 18.

# Input:
# users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,"Chicago")]

# Output:
#{'Alice': 25, 'Charlie': 30}

users_data = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,"Chicago")]

users = {name : age  for name,age,city in users_data if age > 18}
# if we want city too 
#users = {name : (age,city) for name,age,city in users_data if age > 18}
# because dictionary takes only key value pairs

print(users)