def avg(num):
    sum=0
    count=0
    while num>0:
        digit=num%10
        sum=sum+digit
        count=count+1
        num=num//10
    return sum/count
num=int(input('enter the number: '))
print(avg(num))

