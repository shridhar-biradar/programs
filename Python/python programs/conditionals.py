# simple if
print('simple if conditions')
n=10
if n<20:
    print(n,'is lesser than 20')
if True:
    print('good morning')
# if condition is true then only it executes statements
if False:
    print('it is false condition')
print()

# if else
print('if else conditions')
num=-10
if num>0:
    print(num, 'is a positive number')
else:
    print(num,'is negetive number')
print()

#elif is used whenever more condition are applicable
a=60
b=20
if a<b:
    print(a,'is lesser than', b)
elif a>b:
    print(a,'is greater than', b)
else:
    print(a,'is equals to', b)
