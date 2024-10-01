class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print('name is  ',self.name)

class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks=marks

    def display(self):
        super().display()
        print('marks is: ',self.marks)

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
    def display(self):
        super().display()
        print('salary is: ', self.salary)


std=Student('rohan',87)
std.display()
emp=Employee('sachin',4)
emp.display()