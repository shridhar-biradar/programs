print('identity operator')
a=10
b=20
print('a=10 & b=20  a is b',a is b)
print(id(a))
print(id(b))

a='shridhar'
b='shri'
print(id(a))
print(id(b))
print('a=shridhar b=shri  a is not b',a is not b)

list1=['one','two','three']
list2=['one','two','three']
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1==list2)
# we can use identity operator for address comparison 1) is operator 2) is not operator