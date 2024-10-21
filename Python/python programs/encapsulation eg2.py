'''
# Encapsulation example 1
class Employee:
    __name=None
    __salary=None

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name
        

    def setSalary(self,salary):
        self.__salary=salary
        
    def getSalary(self):
        return self.__salary

e=Employee()
name=input('enter ur name: ')
sal=int(input('enter ur salary: '))
e.setName(name)
e.setSalary(sal)
print(e.getName())
print(e.getSalary())

print('******************')
# encapsulation example 2
class Student:
    __age=0

    def setAge(self,age):
        if age>0:
            self.__age=age
            print('age is initialized')
        else:
            print('invalid age')

    def getAge(self):
        return self.__age

std=Student()
age=int(input('enter a age: '))
std.setAge(age)
print(std.getAge())
'''

print('***************')

class Gmail:
    __password=0

    def setPassword(self,password):
        if len(password)>=8:
            self.__password=password
        else:
            print('enter strong password')

    def getPassword(self):
        return self.__password
g=Gmail()
password=input('enter ur password: ')
g.setPassword(password)
print(g.getPassword())
    
