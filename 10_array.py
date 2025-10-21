#create an array
my_array = [10, 20, 30, 40, 50]
print("Original array:", my_array)

#accessing array elements
print("First element:", my_array[0])
print("Third element:", my_array[2])
print("Last element:", my_array[-1])

#length of array
print("Length of array:", len(my_array))

#modifying array elements
my_array[1] = 25    
print("Modified array:", my_array)

#adding elements to array
my_array.append(60)
print("Array after appending 60:", my_array)
my_array.insert(2, 22)
print("Array after inserting 22 at index 2:", my_array)

#removing elements from array
my_array.remove(30) 
print("Array after removing 30:", my_array)
popped_element = my_array.pop()
print("Popped element:", popped_element)
print("Array after popping last element:", my_array)

#slicing array
sub_array = my_array[1:4]
print("Sliced array (index 1 to 3):", sub_array)

#looping through array
print("Looping through array:")
for element in my_array:
    print(element)

#checking if an element exists
print("Is 25 in array?", 25 in my_array)
print("Is 100 in array?", 100 in my_array)

#clearing the array
my_array.clear()
print("Cleared array:", my_array)

#deleting the array
del my_array    
#print(my_array)  # This will raise an error since my_array is deleted
print("Deleted my_array.")
