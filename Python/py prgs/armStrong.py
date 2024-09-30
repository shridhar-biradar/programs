# it is for only 3 digit number
'''
def isArmStrong(num):
    sum=0
    temp=num
    while num!=0:
        digit=num%10
        sum=sum+digit**3
        num=num//10
    return temp==sum
no=int(input('enter 3 digit number: '))
if isArmStrong(no):
    print(no,' is a armStrong number')
else:
   print(no,' is a not armStrong number')
'''
# or for 3 digit number 

def isArmStrong(num):
    sum=0
    for i in range(3):
        sum=sum+int(num[i])**3
    sum=str(sum)
    return sum==num
num=input('enter number: ')
if isArmStrong(num):
    print(num ,' is armstrong number')
else:
    print(num, 'is not armStrong number')



# To find armStrong number of all type input
'''
def isArmStrong(num):
    sum=0
    l=len(str(num))
    for i in range(l):
        sum=sum + int(num[i])**l
    sum=str(sum)
    return sum==num
no=input('enter the number: ')
if isArmStrong(no):
    print(no, ' is armStrong Number')
else:
    print(no, 'is not armStrong number ')
'''