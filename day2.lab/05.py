#hollow rectangle pattern

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * cols)
    else:
        print("*" + " " * (cols - 2) + "*")
