print('Access specifiers')
class Car:
    brand='BMW' # public variable 
    __cost='1cr' # private variable

    print(brand)
    print(__cost)
c=Car()
print(c.brand)
# print(c.__cost) -> error because cost is private variable
# cannot access directly outside class
# by using get() we can access it

print('******************')

print('Encapsulation')
class Student:
    __age=23
    __name='Shri'

    def getAge(self):
        return self.__age # 23
    def getName(self):
        return self.__name # Shri
s=Student()
age=s.getAge()
name=s.getName()
print('Age is: ',age)
print(name)

print('*******************')

# setters and getters
class Bike:
    __cost = 100

    def setCost(self,cost):
        self.__cost = cost

    def getCost(self):
        return self.__cost

b = Bike()
print(b.getCost())
b.setCost(500)
print(b.getCost())

print('******************')

class Person:
    __height=5.1 

    def setHeight(self,height):
        self.__height=height

    def getHeight(self):
        return self.__height
p=Person()
p.setHeight(6.2)
print('Height is: ',p.getHeight()) # initialy 5.1 after update it is 6.2 

