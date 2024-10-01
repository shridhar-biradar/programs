def isPallindrome(num):
    rev=0
    temp=num
    while num>0:
        digit=num%10
        rev=rev*10 + digit
        num=num//10
    return rev==temp

num=int(input('enter number: '))
if isPallindrome(num)==True:
    print(num,' is a pallindrome number')
else:
    print(num,' is not a palindrome number')


