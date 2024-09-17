# sum of two number

def add(num1,num2):
    sum=num1+num2
    #print('sum of ',num1,'&',num2,'is',sum)
    print('sum of {} & {} is: {}'.format(num1,num2,sum))
    #print('sum of {1} & {0} is: {}'.format(num1,num2,sum))
   
for i in range(3):
    num1=int(input('enter 1 number:'))
    num2=int(input('enter 2 number:'))
    add(num1,num2)
    print('--------')

# function to check given number is even or odd
'''
def checkEvenOdd(num):
    if num%2==0:
        print(num,'is even number')
    else:
        print(num,'is odd number')

for i in range(2):
    num=int(input('enter the number: '))
    checkEvenOdd(num)
    print('------------')
'''

# find sum & avg of list elements
'''
a=[10,20,30]
sum=0
for i in a:
    sum+=i
print('sum is: ',sum)
avg=sum//len(a)
print('avg is',avg)
# for concatination we can use format()
print('total sum is {}'.format(sum))
print('avarage is {}'.format(avg))
'''
