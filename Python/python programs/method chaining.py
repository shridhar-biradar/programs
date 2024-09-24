# method chaining by using super()
class Vehicle:
    def start(self):
        print('vehicle is started')
class Car(Vehicle):
    def start(self):
        print('car is started')
        super().start()
c=Car()
c.start()
print()

# super() can be called where ever we want inside the child function
class Person:
    def walk(self):
        print('person is walking')
class Tom(Person):
    def walk(self):
        super().walk()
        print('tom is walking')
        super().walk()
t=Tom()
t.walk()
print()

# hirarchial inheritance
class emp:
    def work(self):
        print('employee is working')
class dev(emp):
    def work(self):
        super().work() #emp.work(self)
        print('developing an app')
        emp.work(self) # we can use this in place of super()

class tester(emp):
    def work(self):
        super().work() #emp.work(self)
        print('testing the code') 
d=dev()
d.work()
print('----------')
t=tester()
t.work()
print()

# method overriding & method chaining in multiple inheritance
class Employee:
    def display(self):
        print('in employee')
class Student:
    def display(self):
        print('in student')
class John(Employee,Student):
    def display(self):
        super().display()
        # Student.display(self)
        print('in john')
j=John()
j.display()
