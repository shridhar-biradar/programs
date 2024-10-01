# with __str__()
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return '{} has scored {} marks'.format(self.name,self.marks)
        
s=Student('tom',88)
print(s)
# print(s.__str__()) # it is same as   print(s) '''


# without __str__()

#
'''
class Pen:
    def __init__(self,brand,cost):
        self.brand=brand
        self.cost=cost
    def __str__(self):
        return 'cost of {} is {}'.format(self.brand , self.cost)
p1=Pen('parker',40)
p2=Pen('butterfly',20)
print(p1)
print(p2)
print()
'''
#
'''
class Car:
    def __init__(self,brand,cost):
        self.brand = brand
        self.cost = cost

    def __str__(self):
        return '{} car cost is {}'.format(self.brand,self.cost)

c1=Car('suzuki',50000)
c2=Car('hundai',100000)
c3=Car('swift',8273767)
l = [c1,c2,c3]
for i in l: 
    print(i)
print('-------------')  '''

# program to accept user input and store it in list 
class Student:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'student name is {}'.format(self.name)
    
student_list=[ ] # creating empty list
size=int(input('enter number of  object to be added: '))

# for loop to add student objects
for i in range(size):
    name=input('enter name: ') # accepting name
    obj= Student(name) # creating student object
    student_list.append(obj) # adding student object inside list

# for loop to display student objects
for i in student_list:
    print(i)

