class Student:
    id=12
    age=22
    name='tom'
s1=Student() # object creation
print('id is ',s1.id)
print('age is ',s1.age)
print('name is ',s1.name)
print()

class Car:
    brand="audi"
    cost=20000

c1=Car() # object creation 
c2=Car() # object creation

# objectName.variableName
print(Car.brand,Car.cost)
print(c1.brand,c1.cost)
print(c2.brand,c2.cost)
print()

#if we update the class values it will affecet all the object of 
# that class untill it has connection with class
Car.brand='sujuki' 
print(Car.brand,Car.cost)
print(c1.brand,c1.cost)
print(c2.brand,c2.cost)
print()

c1.brand='honda'
print(Car.brand,Car.cost)
print(c1.brand,c1.cost)
print(c2.brand,c2.cost)
print()

Car.brand='mercedes'
print(Car.brand,Car.cost)
print(c1.brand,c1.cost)
print(c2.brand,c2.cost)
print()

