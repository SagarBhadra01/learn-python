#inheritance example in Python
class Animal:           #parent class
    def speak(self):
        return "Animal speaks"

class Dog(Animal):      #child class
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"      

#printing the output
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())
print(dog.speak())
print(cat.speak())

#super() function example
class Parent:
    def show(self):
        return "Parent class method"

class Child(Parent):
    def show(self):
        return "Child class method"
    def parent_show(self):
        return super().show()
#printing the output
child = Child() 
print(child.show())
print(child.parent_show())