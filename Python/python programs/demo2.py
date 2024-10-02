import demo1

print(demo1.age)
print(demo1.name)

demo1.study()

print('it is demo2 file')
print('********')

import demo1 as d1
print(d1.brand)
d1.drive()
obj=d1.Suzuki()
obj.start()
