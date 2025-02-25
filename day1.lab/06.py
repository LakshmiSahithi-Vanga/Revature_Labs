#remove duplicates from the list and return it

lst1=[10,30,30,20,40,40,50]
unique =[]
for item in lst1:
  if item not in unique:
       unique.append(item)
print(unique)