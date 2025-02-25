#return count of words in a sentence

str= input("string:").lower()
c=0
for i in str:
  if i==" ":
    c+=1
print(c+1)