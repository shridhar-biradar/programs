print('start')
try:
    print(10/0)
except ZeroDivisionError as z:
    print(z)
print('end')

print('*************')
 
a=[10,20,30]
try:
    print(a[99])
except IndexError as i:
    print(i)

print('****************')

# finally block-> it will execute always  
print('start')
try :
    print(10/0)
except ZeroDivisionError as i:
    print(i)
finally:
    print('Inside a finally block')
print('end')

print('****************')

#raise -> used to throw an object of exception
for i in range(1,6):
    print(i)
else:
    raise StopIteration()
