#swapping of two numbers

def swapping(x,y):
    x = x+y
    y = x-y
    x=x-y
    return x,y

a=10
b=15

print(swapping(a,b))