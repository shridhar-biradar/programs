# constructor chaining
class Vehicle:
    def __init__(self):
        print('in vehicle')
class Bike(Vehicle):
        pass
b=Bike() # in vehicle
print()

class Vehicle:
    def __init__(self):
        print('in vehicle')
class Car(Vehicle):
    def __init__(self):
        super().__init__() # invoking parent class constructor 
        print('in car')
c=Car()
print()

#
class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks=marks

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
std=Student('tom',77)
print('{} is scored {} marks'.format(std.name,std.marks)) # tom is scored 77 marks

emp=Employee('john',4.5)
print('{} is earning {} LPA'.format(emp.name,emp.salary)) # john is earning 4.5 LPA
print()

#
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,brand,cost):
        super().__init__(brand)
        self.cost=cost
class Bike(Vehicle):
    def __init__(self,brand,color):
        super().__init__(brand)
        self.color=color
c=Car('suzuki',500000)
print(c.brand,c.cost)
b=Bike('honda','blue')
print(b.brand,b.color)
