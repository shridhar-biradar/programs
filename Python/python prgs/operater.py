a=10
b=2
print('arithmetic operators')
print('a=',a , 'b=' , b)
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a//b=',a//b)
print('')

print('relational operator')
a=10
b=20
print('a=',a , 'b=' , b)
print('a<=b ',a<=b)
print('a>=b ',a>=b)
print('a<b ',a<b)
print('a>b ',a>b)
# we can apply relational oprator for str type also
print()
a='python'
b='python'
print('a=',a , 'b=' , b)
print('a>b is',a>b)
print('a<b is' ,a<b)
print('a>=b is',a>=b)
print('a<=b is' ,a<=b)
print('')

print('equality operators')
a=10
b=20
print('a=',a , 'b=' , b)
print('a==b is', a==b)
print('a!=b is ',a!=b)
print()

print('conditional operator')
a=int(input('enter first num:'))
b=int(input('enter 2nd num:'))
min=a if a<b else b
print('minimum value is:' ,min)
print()

print('to find maximum of 3 numbers')
a=int(input('enter 1st num :'))
b=int(input('enter 2nd num:'))
c=int(input('enter 3rd num:'))
max=a if a>b and a>c else b if b>c else c
print('maximum value:', max)