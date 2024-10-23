# method overloadding

def display(name='Tom',marks=50,subject='Python'):
    print('{} has scored {} marks in {}'.format(name,marks,subject))

display()
display('John')
display('Alex',60)
display('Jack',87,'Java')
display(subject='java')

print('*****************')

# method overridding

class Vehicle:
    def start(self):
        print('Vehicle is started')

class Car(Vehicle):
    def start(self):
        print('Car is started')

c=Car()
c.start()
