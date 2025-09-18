# creating a Function
def my_function():
  print("Hello World")

# calling a Function
my_function()

# Function with parameters
def my_function_with_params(fname, lname):
  print(fname + " " + lname)
my_function_with_params("Sagar", "Bhadra")

# Function with default parameter values
def my_function_with_default_params(country = "Norway"):
  print("I am from " + country)
my_function_with_default_params("Sweden")
my_function_with_default_params() 
my_function_with_default_params("India")

#non keyword arguments
def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("a", "b", "c")

#keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Sagar", lname = "Bhadra")

#return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))

#Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

#function within function
def f1():
    s = 'hey,'
    def f2():
        print(s)  
    f2()
f1()

#anonymous function 
def cube(x): return x*x*x   # without lambda
print(cube(3))
cube_l = lambda x : x*x*x  # with lambda
print(cube_l(4))

#recursion function
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
print(factorial(4))