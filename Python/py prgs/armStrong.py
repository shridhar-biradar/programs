# it is for only 3 digit number
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