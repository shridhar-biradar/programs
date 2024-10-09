# eg for decorater function
def outer(func):
    def inner():
        print('start')
        func()
        print('end')
    return inner
@outer
def display():
    print('hello world') 

display()
'''
internal process once a function is decorated
x=outer(display)
x()
'''
