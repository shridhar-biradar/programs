# single level inheritance
class parent:
    name='tom'

class child(parent):
    age=22

c=child()
print(c.age,c.name)
print()

# multi level inheritance
class person:
    name='john'

class emp(person):
    id=101

class developer(emp):
    subject='python'

d=developer()
print(d.name,d.id,d.subject)
print()

# hirarchial inheritance
class parent:
    name='tom'

class child1(parent):
    age=22
class child2(parent):
    age=33
c=child2()

