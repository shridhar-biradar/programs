print('membership function') 
a=[10,20]
print(10 in a)
print(100 not in a)
print(10 not in a)
print(10 in [10,20,40])
print(100 in(10,30))
print(10 in {10,20})
print(10 not in {10,20})
print(100 not in (10,30))
print()

print('identity operator')
a=[10,20,30]
b=[10,20,30]
c=a
print(a is b)#list will compair address of 2 variable 
print(a is c)
print(id(a))
print(id(b))
a=(10,20)
b=(10,20)
print(a is b)#tuple will compaire the values 

print()

print('functions')
a=[10,20,30]
a.append(40)
# append() is used to insert value at last position

print(a)
a.append(100)
print(a)
a.pop()
#pop() is used to remove object from last position

print(a)
a.remove(10)
#remove() is used to remove the particular object

print(a)
a.clear()
#clear() is used to remove complete object from the list
print(a)
print()

a=[10,20,30]
print(a)
# insert() is used to insert value at particular index value
a.insert(1,50)
print(a)
a.insert(3,100)
a.insert(2,10)
print(a)
#index() is used to find the index value of an object
print(a.index(100))
print(a.index(10,1))
print(a.index(10,1,4))
print(a.index(20,2,5))
#count() is used to count the no of occurences of an element
print(a.count(10))
print(a.count(100))
