# Variable 'x' stores the integer value
x = 5
print(x)
# Variable 'y' stores the float
y = 5.55
print(y)
# Variable 'name' stores the string
name = "Sagar"  
print(name)
# Variable 'list' stores the list
list = [1, 2, 3]
print(list)
# Variable 'tuple' stores the tuple
tuple = (1, 2, 3, 4, 5)
print(tuple)
# Variable 'set' stores the set
set = {1, 2, 3, 4, 5}
print(set)
# Variable 'dict' stores the dict
dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
print(dict)
# Variable 'boolean' stores the boolean
boolean = True
print(boolean)



# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True
# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))


#swapping two values
a, b = 5, 10
a, b = b, a
print(a, b)


#assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#using + join variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
myvar = "Sagar"
my_var = "Sagar"
_my_var = "Sagar"
myVar = "Sagar"
MYVAR = "Sagar"
myvar2 = "Sagar"


#typecasting
# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string
# Display results
print(n)  
print(f)  
print(s2)