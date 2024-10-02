def isHappy(num):
    while num>9:
        sum=0
        while num!=0:
            digit=num%10
            sum=sum+digit**2
            num=num//10
        num=sum
    return num==1 or num==7
num=int(input('enter the number: '))
if isHappy(num):
    print(num ,' is happy number') 
else:
    print(num, 'is not happay number')
