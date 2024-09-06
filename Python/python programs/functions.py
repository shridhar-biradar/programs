a='this is python class'
print(a) 
print(a.title())# This Is Python Class
# title() will convert each words first character to upper case

print(a.capitalize()) # This is python class
# capitalize() convert first character of entire string into upper case

print(a.startswith('this'))# True
print(a.startswith('This'))# False
# startswith() will check the if the string starts
# with the specified substring or not

print(a.endswith('ss')) #True
print(a.endswith('S')) #False
# endswith() will check the if the string endswith
# the specified substring or not

print(a.upper()) #THIS IS PYTHON CLASS
# upper() will convert entire string into upper case

print(a.lower()) # this is python class
# lower() will convert entire sting into lower case 

print('Hello'.isalpha())# True
print('Hello123'.isalpha())#False
# isalpha() will check given string has only characters
# no numbers and no special characters allowed

print('123'.isdigit()) # True
print('hello123'.isdigit()) # False
# isdigit() will check the given string has only numbers
# no character and no special character allowed

print('hello123'.isalnum()) #True
print('Hello@123'.isalnum()) #False
print('Hello'.isalnum()) #True
print('123'.isalnum()) # True
# isalnum() will check given character has only number
# and character , special charcter not allowed
# isalnum() will check

a='Hello World'
print(a.count('z')) # 0
print(a.count('o')) # 2
print(a.count('o',6)) # 1
print(a.count('o',8)) # 0
# 6 index is starting point count() will count from
# starting point
print(a.count('o',3,7)) # 1
print(a.count('o',3,8)) # 2
print(a.count('l',1,8)) # 2
# 7 index is ending point count() will count upto ending point

