# aliasing a functions
def disp():
    print('hello')
x=disp # storing address of function into x variable
x() # invoking the function
print('------')

def study():
    print('studing python')
x=study 
y=x
z=y
z()
print('-------')
