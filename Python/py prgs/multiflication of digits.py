def mul(num):
    mul_no=1
    while num>0:
        digit=num%10
        mul_no=mul_no*digit
        num=num//10
    return mul_no
num=int(input('enter the number : '))
print(mul(num))