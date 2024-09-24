def sum(n):
    sum_no=0
    while n>0:
        digit=n%10
        sum_no+=digit
        n=n//10
    return sum_no
num=int(input('enter the number: '))
print(sum(num))