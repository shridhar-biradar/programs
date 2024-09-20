# init() is used for initialization
class Cars:
    def __init__(self):
        print('it is car')
c=Cars()
c1=Cars()
print()

class Bike:
    def __init__(self,company):
        print(company)
b=Bike(' honda')
print()

class Car:
    def __init__(self,cost):
        self.cost=cost
c1=Car(100)
print('cost:',c1.cost)
c2=Car(200)
print('cost:',c2.cost)
print()

class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
p1=Person(20,'tom')# Person.__init__(p1,20,'tom')
p2=Person(21,'john') # Person.__init__(p2,21,'john')
print('{} is {} years old'.format(p1.name,p1.age))
print('{} is {} years old'.format(p2.name,p2.age))
print()

class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
e1=Emp(1,'rahul',77873)
print('id is:',e1.id)
print('name is:',e1.name)
print('salary is: ',e1.salary)
print()
e2=Emp(2,'abhi',99873)
print('id is: ',e2.id)
print('name is: ',e2.name)
print('salary is: ',e2.salary)


