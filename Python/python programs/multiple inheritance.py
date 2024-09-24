# multiple inheritance
class A:
    x=10
class B:
    y=20
class C(A,B):
    z=30
obj=C()
print(obj.x,obj.y, obj.z)
print()

class A:
    x=10
class B:
    x=20
class C(A,B):
    pass
obj=C()
print(obj.x) # 10
print()

# hybrid inheriatnce
class Vehicle:
    brand='suzuki'
class Car(Vehicle):
    color='white'
class Bike(Vehicle):
    cost=50000
class Person(Car,Bike):
    name='john'
p=Person()
print(p.brand,p.color,p.cost,p.name)
print()

# method overriding
class Father:
    def bike(self):
        print('fathers bike')
class Son(Father):
    def bike(self):
        print('son bike')
s=Son()
s.bike()
print()

#method overriding in hirarchial inheritance
class Employees:
    def work(self):
        print('employee is working')
class Developer(Employees):
    def work(self):
        print('Developing app')
class Tester(Employees):
    def work(self):
        print('Testing App')
d=Developer()
d.work()
t=Tester()
t.work()
print()

#
class Vehicle:
    def start(self):
        print('vehicle started')
class Car(Vehicle):
    def start(self,brand):
        
        print(brand,'car started')
c=Car()
c.start('suzuki') # Car.start(c,'suzuki')
