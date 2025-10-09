#create sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#allow duplicate values not allowed
thisset = {"apple", "banana", "cherry", "apple"}    
print(thisset)

#length of set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#different data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}  
set3 = {True, False, False}
set4 = {"abc", 34, True}
print(set1)
print(set2)
print(set3)
print(set4)

#access set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#check if item exists
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


# add items
thisset = {"apple", "banana", "cherry"} 
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)
# add any iterable (list, tuple, dictionary etc.)
thisset.update({"kiwi", "orange"})
print(thisset)


#remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #raises an error if item not found
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #does not raise an error if item not found    
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #removes a random item
print(x)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.clear() #empties the set
print(thisset)
thisset = {"apple", "banana", "cherry"} 

#delete set
del thisset #deletes the set completely

#join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)   # We can use the | operator instead of the union(), set3 = set1 | set2
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
print(set2)

#intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#The intersection() method will return a new set, that only contains the items that are present
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection(y)
print(x)


#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"} 
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#The symmetric_difference() method will return a new set, that contains only the elements that are
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print(x)
print(y)

#difference_update() method will remove the items that are present in both sets from the first set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
#The difference() method will return a new set, that contains the difference between two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z)


#subset and superset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = {"a", "b", "c"}
print(x.issubset(y))
print(y.issuperset(x))
print(x.issubset(z))
print(z.issuperset(x))
print(y.issubset(x))
print(x.issuperset(y))
print(x == z)
print(x is z)
print(x is not z)
print(x is not y)
print(x != y)

#frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
#x.add("orange") #this will raise an error
#x.remove("banana") #this will raise an error
print("banana" in x)
#copy(),difference(),intersection(),isdisjoint(),issubset(),issuperset(),symmetric_difference(),union()   only support

#discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #does not raise an error if item not found
print(thisset)