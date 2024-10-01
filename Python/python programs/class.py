class Car:
    def __init__(self,cost):
        self.cost=cost
    def display(self):
        print('cost is', self.cost)
c=Car(1000)
print('cost:' ,c.cost)
c.display()
print()

'''
class Student:
     def __init__(self,age,name):
        self.age=age
        self.name=name
    
     def display(self):
        print(self.age,self.name)
s1=Student(21,'john')
s2=Student(32,'alex')

s1.display()
s2.display()
'''


class Emp:
    def  __init__(self,id,name,age,sal):
        self.id=id
        self.name=name
        self.age=age
        self.sal=sal

    def disp(self):
        print('id is{} \n name is {} \n age is {} \n sal is {}'.format(self.id,self.name,self.age,self.sal))

e1=Emp(1,'alex',22,200)
e2=Emp(2,'monika',20,20000)
e3=Emp(3,'john',21,300)

e1.disp()
e2.disp()
e3.disp()




