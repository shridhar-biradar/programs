# example for generator
def gen(): 
    i=1
    yield i

    i+=1
    yield i

    i+=1
    yield i

obj=gen() # calling generator function, & it return address
i=iter(obj) # traversing obj
print(next(i)) # 1
print(next(i)) # 2
print(next(i)) # 3
print('--------')

# python program to find first 3 even number
def even():
    i=2
    yield i

    i+=2
    yield i

    i+=2
    yield i

    i+=2
    yield i

obj=even()
i=iter(obj) 
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print('-------------------')

# find square root of 1st 5 number
def square():
    for i in range(1,6):
        yield i*i

obj=square()
i=iter(obj)
for x in range(1,6):
    print(next(i))

    
