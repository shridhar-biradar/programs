def reverse(num):
    res=0
    while num>0:
        digit=num%10 # 3 ,2,1 
        res=res*10 + digit # 3, 32,321
        num=num//10 #12 ,1
    return res
num=int(input('enter the num: ')) # 123
print('reversed number is: ',reverse(num))
