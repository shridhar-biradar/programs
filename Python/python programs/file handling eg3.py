# writing data into file
'''
f=open('pen.txt','w')
f.write('Hello how are you')
f.close()
'''
# reading data from file
'''
f=open('pen.txt','r')
print(f.read())
f.close()
'''

# appending data into file
f=open('pen.txt','a')
f.write(' : i am fine')
f.close()

f=open('pen.txt','r')
print(f.read())
f.close()
