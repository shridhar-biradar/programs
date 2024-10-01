def biggestNum(num):
    max=0
    while num>0:
        digit=num%10
        if digit>max:
            max=digit
        num=num//10
    return max

num=int(input('enter number to find out biggest digit: '))
big_digit=biggestNum(num)
print('biggest digit is: ',big_digit)