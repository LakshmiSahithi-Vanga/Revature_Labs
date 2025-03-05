""" Question 1: Filtering Data Using Lists and Regex
You are working on a data cleaning task where you need to filter out invalid email
addresses from a list of strings. Write a Python program that:
Accepts a list of strings.
Uses the re module to validate email addresses (e.g., example@example.com ).
Returns a new list containing only valid email addresses.

input:

emails = ["user@example.com", "invalid-email", "admin@domain.org", "test@com"]

output:

["user@example.com", "admin@domain.org"] """

import re
def filter_valid_emails(emails):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return [email for email in emails if re.match(pattern, email)]
emails = ["user@example.com", "invalid-email", "admin@domain.org", "test@com"]
print(filter_valid_emails(emails)) 