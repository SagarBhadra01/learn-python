class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."   
# Example usage
person1 = Person("Alice", 30) 
person2 = Person("Bob", 25)
print(person1.greet()) 
print(person2.greet()) 


'''
{Person} = Class
{person1, person2} = Objects
{def __init__(self, name, age): ...} = attributors / Constructor
{__init__} is a special method called a constructor that initializes new objects.
{self.name, self.age} = Attributes
{self is a reference to the current instance of the class.}
{def greet(self): ...} = Method
'''


#multiple parameters in class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
# Example usage
car1 = Car("Toyota", "Camry", 2020)
print(car1.display_info())


#default parameter in class
class Dog:
    def __init__(self, name, breed="Mixed"):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} says Woof!"
# Example usage
dog1 = Dog("Buddy")
print(dog1.bark())

#modifying attributes
dog1.breed = "Golden Retriever"
print(dog1.breed)   
print(dog1.bark())

#modifying attributes using methods
class BankAccount:  
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}."
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New balance is {self.balance}."
# Example usage
account = BankAccount("John Doe", 1000)
print(account.deposit(500))
print(account.withdraw(200))

#deleting attributes
del account.balance
#print(account.balance)  # This will raise an AttributeError

#__str_ method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"
# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(book1)
#The __str__() method is a special method that controls what is returned when the object is printed