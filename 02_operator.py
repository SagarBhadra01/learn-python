#arithmatic operators
a = 15
b = 4
# Addition
print("Addition:", a + b)  
# Subtraction
print("Subtraction:", a - b) 
# Multiplication
print("Multiplication:", a * b)  
# Division
print("Division:", a / b) 
# Floor Division
print("Floor Division:", a // b)  
# Modulus
print("Modulus:", a % b) 
# Exponentiation
print("Exponentiation:", a ** b)


#relational operators
a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


#logical operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#bitwise operators
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


#assignment operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)


#identity operators
a = 10
b = 20
c = a
print(a is not b)
print(a is c)


#ternary operator
a, b = 10, 20
min = a if a < b else b
print(min)