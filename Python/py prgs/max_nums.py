a=int(input('enter 1at number:'))
b=int(input('enter 2nd number: '))
c=int(input('enter 3rd number: '))
max_nums=a if a>b and a>c else b if b>c else c
print('maximum number is: ', max_nums)