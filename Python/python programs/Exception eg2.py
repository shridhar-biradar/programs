# exception handling using raise()
class InvalidPasswordException(Exception):
    pass

print('Start')
password=int(input('enter password: '))
if password == 123:
    print('Login successful')
else:
    try:
        obj=InvalidPasswordException() # Exception object
        raise obj #raise InvalidPasswordException
    except InvalidPasswordException:
        print('kindly enter valid password')
print('End')

print('*****************')

# exception handling by using method
class InvalidPasswordException(Exception):
    pass

def login(password):
    if password==123:
        print('Login successful')
    else:
        try:
            raise InvalidPasswordException()
        except Exception:
            print('Invalid password')

print('Start')
password = int(input('Enter password: '))
login(password)
print('End')

print('****************')

# without function 
class InsufficientBalanceException(Exception):
    pass
balance=5000
amount= int(input('enter amount to be withdrawn: '))
if amount<= balance:
    print('Amount is withdrawn successful')
else:
    try:
        raise InsufficientBalanceException
    except:
        print('insufficient balance')


print('*****************')

# with function
class InsufficientBalance(Exception):
    pass
def withdraw(amount):
    balance=5000
    if amount<=balance:
        print('Available balance before withdrawn: ',balance)
        print('Withdrawing Rs. ',amount)
        balance=balance-amount
        print('amount withdrawn successfully')
        print('Available balance after withdrawn: ',balance)
    else:
        try:
            raise InsufficientBalance()
        except InsufficientBalance:
            print('No sufficient balance')
print('Welcome to Canara Bank Atm')
amount=int(input('enter anount to be withdrawn: '))
withdraw(amount)
print('Thank you for visiting')
