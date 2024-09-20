# program to find factorial of given number
num=int(input('enter the number: '))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

# prime factore of a given number
n=int(input('enter the number: '))
for i in range(1,n+1):
    if n%i==0:
        print(i)