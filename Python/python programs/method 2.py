def outer():
    print('inside outer function')
    def inner():
        print('inside inner function')
    inner() # calling inner function
outer() # calling outer function
print('-------')

def outer():
    print('inside outer')
    def inner():
        print('inside inner')
    return inner # returning the address of inner
z=outer() # storing the address of inner in z
z() # invoking inner() as z & inner are pointing to same address

print('-------')

def person():
    print('in person')
    def student():
        print('in student')
    return student # returning the address of student
z=person() # invoking person() & storing the address of student in z
z() # student()

print('-------')

def person():
    print('in person')
    def student():
        print('in student')
    return student() # returning the address of student
z=person() # storing the address of student in z

print('-------------')

# passing function name as an argument
def display():
    print('hello')

def tom(x):
    x() # display()
    print(x) # print address of diplay()
    print('my name is tom')

tom(display) #  invoking tom() & passing address of display to tom function

print('-----------')

def car():
    print('car started')
def bike(z):
    z() # car()
    print('bike started')
    z() # car()
bike(car)
    
