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

