#create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#allow duplicate values also
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#one item tuple(remember coma)
thistuple = ("apple",)
print(type(thistuple))
#without coma, NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#diff data type
tuple = ("abc", 34, True, 40, "male")
print(tuple)

#access tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#if statement
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# add items
mytuple = ("apple", "banana", "cherry")
y = list(mytuple)
y.append("orange")
mytuple = y
print(mytuple)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#remove tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = y
print(thistuple)

#delete tuple
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

#unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#using asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  
print(green)
print(yellow)   
print(red)
# Add a list of values the "tropic" variable:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *tropic, red) = fruits  
print(green)
print(tropic)   
print(red)

#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#tuple methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5))
print(thistuple.index(8))