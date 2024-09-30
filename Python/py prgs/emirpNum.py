def isPrime(num):
    for i in range(2,num//2+1):
        if num% i==0:
            return False
        return True

def getReverse(num):
    rev=0
    while num!=0:
        digit=num%10
        rev=rev*10 + digit
        num=num//10
    return rev

def emirp(num):
    return isPrime(num) and isPrime(getReverse(num))

num=int(input('enter number: '))
if emirp(num):
    print(num,'is emirp number ')
else:
    print(num ,'is not emirp number')