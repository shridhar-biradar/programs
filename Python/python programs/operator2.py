
print('functions or operations on set')
a={10,20,30}
print(a)
print(type(a))
print(len(a))
#add() is used to add object in set 
a.add('python')
print(a)

#remove() is used to remove particular
#object from set
a.remove(20)
print(a)

#set() is used to remove all object from set
a.clear() 
print(a)

a={10,20,30}
b={20,30,40}

#union() is used to find the union of 2 set
#(combine both the set without duplication)
print(a.union(b))

#intersection() is used to find the intersection of 2 set
#(prints only common elements between 2 sets)
print(a.intersection(b))

a={10,20,30}
b={20,30,40}

#difference() is used to find the difference of 2 sets(- =>minus)
print(a.difference(b))#10
print(b.difference(a))#40

a={'apple',11.4}
b={11.4,'mango'}
print(a.difference(b))#apple
print(b.difference(a))#mango

a={10,20,30}
b={20,30,40}
c={50,60,70}

#isdisjoint() is used to check if 2 sets are disjoint or not
#return True if there is no common element else return False
print(a.isdisjoint(b))#False
print(a.isdisjoint(c))#True
print()

print('function or operation on dictionary')
a={1:10,2:20,3:30}
print(a) # {1: 10, 2: 20, 3: 30}
print(type(a)) # <class 'dict'>
print(len(a)) # 3

# keys() returns all the keys from the dictionary
print(a.keys())# dict_keys([1, 2, 3])

# values() returns all the values from the dictionary
print(a.values()) # dict_keys([10, 20, 30])

# get() returns the value based on the key
# get() returns None if the key is not present
print(a.get(1)) #10
print(a.get(10)) # None

print(a) # {1: 10, 2: 20, 3: 30}

# pop() remove specific object based on given key
a.pop(2) 
print(a) # {1: 10, 3: 30}

# clear() remove all elemnets from dictionary
a.clear()
print(a) # {}

# setdefault() is used to add specific element 
a.setdefault(4,40)
print(a)
a.setdefault(5)
print(a)
