# program to invoke private function
class Car:
    def __start(self): # private method
        print('car is started')

    def invokeStart(self): # public method
        self.__start()
print('program started')
c=Car()
c.invokeStart()
print('program ended')

print('**************')

class Swiggy:
    def eatFood(self):
        self.__orderFood()
        print('Eating burger')

    def __orderFood(self):
        print('Ordered Burger')

obj=Swiggy()
obj.eatFood()


