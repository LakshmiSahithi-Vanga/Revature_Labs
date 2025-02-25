#diamond pyramid pattern

rows = int(input("Enter the number of rows: "))

# Upper pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

