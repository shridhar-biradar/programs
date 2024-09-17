# pen Class is created
class pen:
    def write(self):
        print('self address->',self)
        print('writing')
p=pen()
print('p address->',p)
p.write()
print()

# car class is created
class Car:
    # def driving() -> driving() takes 0 positional arguments but 1 was given
    # if we do not pass any parameter it gives above error 
    def driving(self):
        print('driving a car')
c=Car() # object creation
c.driving() # internal working -> Car.write(c)
print()

# employee class created
class Employee:
    def work(self): 
        print(self)
        print('employee is working')
e1=Employee()
print('e1:',e1)
e1.work()
e2=Employee()
print('e2',e2)
e2.work()
