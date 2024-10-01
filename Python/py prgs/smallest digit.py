def smallNum(num):
    min=9
    while num>0:
        digit=num%10
        if digit<min:
            min=digit
        num=num//10
    return min

num=int(input('enter number to find smallest digit: '))
small_digit=smallNum(num)
print('smallest digit is: ', small_digit)