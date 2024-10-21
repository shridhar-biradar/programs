class Bank:
    def __init__(self,balance):
        self.balance=balance

    def deposite(self,amount):
        print('Depositing Rs {}'.format(amount))
        self.balance=self.balance + amount
        print('Amount deposited successfully')

    def withdraw(self,amount):
        print('Withdrawing Rs {}'.format(amount))
        self.balance=self.balance - amount
        print('Amount withdrawn successfully')

    def checkbalance(self):
        print('Available Balance : Rs.{}'.format(self.balance))

obj=Bank(5000)

while True:
    print('1:deposite amount')
    print('2:withdra amount')
    print('3:check balance')
    print('4:Exit')
    print('enter your choice:')
    choice=int(input())

    if choice == 1:
        print('Enter amount to be deposited')
        amount=int(input())
        obj.deposite(amount)
    elif choice == 2:
        print('enter amount to be withdrawn')
        amount=int(input())
        obj.withdraw(amount)
    elif choice == 3:
        obj.checkbalance()
    elif choice == 4:
        print('thank you')
        exit()
        
    else:
        print('Invalid choice')
    print('******************')
