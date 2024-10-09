a=[10,40,20,30]
i=iter(a)
print(i) # <list_iterator object at 0x000001E56BFA4148>
print(next(i)) # 10
print(next(i)) # 40
print(next(i)) # 20
print(next(i)) # 30
# print(next(i)) # error: stopIteration
print('-----------------')

data=('john','M',20,3.5)
i=iter(data)
print(next(i)) # 'john'
print(next(i)) # 'M'
print(next(i)) # 20
print(next(i)) # 3.5
print('-------------')

bike={'honda','royal','RX'}
i=iter(bike)
print(next(i)) # royal
print(next(i)) # honda
print(next(i)) # RX
print('------------')

bike={'honda','royal','RX'}
i=iter(bike)
for x in range(len(bike)):
    print(next(i))
print('-------------')

a='Hai'
itr=iter(a)
for i in range(len(a)):
    print(next(itr))
print('--------------')

# 'int' object is not iterable
'''
a=76767
itr1=iter(a)
for i in range(len(a)):
    print(next(itr1))
'''

