#occurences of vowels in a sentence

str= input("string:").lower()
c =0
for i in str:
  if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
    c+=1
print(c)