# file handaling
fobj=open('car.txt','w')
data='Hello'
fobj.write(data)
print('data is stored')
fobj.close()
# if the file is already present then all data in that file is lost and new data will be stored.
# if no file is present it will create new file and store the data
print('------------')
print()

# file writing eg2
f=open('student.txt','w')
#f.write('studying python ')
f.write('studying python programing')
f.close()
print('******************')

# file reading eg1
f=open('car.txt','r')
data=f.read()
print(data)
f.close()

# file reading eg2
f=open('student.txt','r')
print(f.read())
print(f.read(5))
f.close()

# importantfunctions
f=open('car.txt','w')
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
