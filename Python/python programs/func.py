# function without parameter & without return statement
def display():
    print('hello')
display() # function calling
print()

#function with parameter & without return statement
def add(x,y):
    print('sum of',x,'&',y, ' is',x+y)
add(10,20)
add(20,15.5)
print()

# function without parameter & with return statement
def display():
    return 10
x=display() # x=10
print(x)  # 10
# or
print(display()) # 10

# function with parameter & with return statement
def mul(a,b):
    return a*b

print(mul(100,2))
