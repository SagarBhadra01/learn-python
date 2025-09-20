# create list
thislist = ["apple", "banana", "cherry"]
print("created list =",thislist)

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("created list with duplicates =",thislist)

#list length
thislist = ["apple", "banana", "cherry"]
print("list length =",len(thislist))

#List items can be of any data type:
#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print("created list with diff datatypes=",list1)

#access list items
thislist = ["apple", "banana", "cherry"]
print("access list item =",thislist[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print("access list item using negative indexing =",thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("access list range wise =",thislist[2:5])
#returns the items from the beginning to, but NOT including, 4:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#returns the items from(-4) to, but NOT including(-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change list value
thislist = ["apple","banana","cherry"]
thislist[2] = "mango"
print("change value of list =",thislist)

#insert value in list
thislist = ["a","b","c"]
thislist.insert(2, "d")
print("insert value in list =",thislist)

#append value in list
thislist = ["a","b", "c"]
thislist.append("d")
print("append value in list =",thislist)

#extend list by merge another list(not only list we also can add tuple,sets,dictionaries)
list1 = ["a","b"]
list2 = ["c","d"]
list1.extend(list2)
print("extended list =",list1)
tuple = ("e", "f")
list1.extend(tuple)
print("extended list =",list1)

#remove from list
list = ["a", "b", "c","d"]
list.remove(list[3])
list.remove("b")
print("remove from list =",list)

#pop from list
list = ["a","b","c","d"]
list.pop()  #always pop last one
list.pop(0)  #specific index wise pop
print("remove from list =",list)

#delete list
list = ["a","b","c","d"]
del list[0]
print("delete from list =",list)
del list
print("delete list =",list)

#clear list
list = ["a","b","c","d"]
list.clear()
print("clear list =", list)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print("list:",x)
# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print("list:",thislist[i])

#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Alphanumerically sorted list",thislist)
#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print("numerically sorted list",thislist)
#Sort Descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print("descending order sorted list",thislist)

#Copy list using copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print("Copy list", mylist)
#Copy list using list()
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print("Copy list", mylist)
#copy list using slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print("Copy list",mylist)

#Join Two List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#append 1 list into another list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)