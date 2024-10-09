# decorator function: It has the logic to decorate another function
def outer(func):
    def inner():
        print('hi what is your name ')
        func()
        print('nice name !!')
    return inner

# Function to be decorated
@outer
def tom():
    print('my name is Tom')

# function to be decorated
@outer
def jerry():
    print('my name is jerry') 

tom()
'''
internal implimentation
x=outer(tom)
x()
'''
print('------')
jerry()
'''
internal implimentation or working
x=outer(jerry)
x()
'''

print('------------------------------ ')
print()

def amazon(func):
    def sale():
        print('Hii', func())
        print('There is a big sale in amazon , do shopping')
        print('Thank you')
    return sale

def john():
    return 'john'
# explicitly we are calling decorator
z = amazon(john)
z()

print('-----')

@amazon
def jack():
    return 'jack'

jack()
