a=10
print(a,type(a))

b=float(a)
print(b,type(b))

c=str(a)
print(c,type(c))

# list can be converted into str,set,tuple
a=[12,2.3,'hello']
b=set(a)
print(b,type(b))

c=tuple(a)
print(c,type(c))

d=str(a)
print(d,type(d))

a='hello'
print(a)
print(list(a))
print(set(a))
print(tuple(a))

a={1:10,2:20}
print(tuple(a)) #(1,2)
# its returns only keys

a=[[1,10],[2,20]]
print(dict(a)) # {1:10,2:20}

a=[[1,10],{2,20},(3,30)]
print(a)
print(type(a)) # <class list>
print(dict(a)) # {1:10,2:20,3:30}
print()

print('input functions')

print('enter 1st no:')
x=int(input())# 10
print('enter 2nd no:')
y=int(input()) # 20
print(x+y) # 30

# or

x=int(input('enter 1st no:')) # 20
y=int(input('enter 2nd no:')) #40
print(x+y) #60
