'''
class Country:
    def __init__(self,name,popul):
        self.name=name
        self.popul=popul

    def __str__(self):
        return 'population of {} is {} crs'.format(self.name,self.popul)

c_list=[]
size=int(input('enter the size of list'))

for i in range(size):
    name=input('enter name of country: ')
    popu=int(input('enter population of country: '))
    c=Country(name,popu)
    c_list.append(c)
print('---')

for i in c_list:
    if i.popul>50:
        print(i)
'''

#
class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def __str__(self):
        return 'id {}  name  {}  salary  {}'.format(self.id,self.name,self.salary)

emp_list=[]

size=int(input('enter size of list: '))

for i in range(size):
    id=int(input('enter id of emp: '))
    name=input('enter employee name: ')
    salary=int(input('enter salary of emp: '))
    e=Emp(id,name,salary)
    emp_list.append(e)

print('salary is > 3.5')
for i in emp_list:
    if  i.salary>3:
        print(i)


