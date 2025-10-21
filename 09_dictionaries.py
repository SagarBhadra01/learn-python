#create a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"  
}
print("Original dictionary:", my_dict)  

#length of dictionary
print("Length of dictionary:", len(my_dict))

#accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict.get("age"))
print("City:", my_dict["city"])

#dict() constructor
another_dict = dict(country="USA", profession="Engineer")
print("Another dictionary:", another_dict)

#getting all keys
print("Keys:", my_dict.keys())
#getting all values
print("Values:", my_dict.values())
#getting all items
print("Items:", my_dict.items())

#adding a new key-value pair
my_dict["profession"] = "Engineer"
print("Updated dictionary:", my_dict)

#updating an existing key-value pair
my_dict["age"] = 31 
print("Updated age:", my_dict)
#using update() method
my_dict.update({"city": "Los Angeles"})
print("Updated city:", my_dict)

#removing a key-value pair
removed_value = my_dict.pop("city")
print("Removed city:", removed_value)
print("Dictionary after removal:", my_dict)

#checking if a key exists
print("Is 'name' in dictionary?", "name" in my_dict)
print("Is 'city' in dictionary?", "city" in my_dict)

#iterating through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

#clearing the dictionary
my_dict.clear()
print("Cleared dictionary:", my_dict)

#deleting the dictionary
del another_dict    
#print(another_dict)  # This will raise an error since another_dict is deleted
print("Deleted another_dict.")  


#looping through a dictionary
sample_dict = {"a": 1, "b": 2, "c": 3}
for key in sample_dict:
    print(f"Key: {key}, Value: {sample_dict[key]}")
#using dictionary comprehension
squared_dict = {k: v**2 for k, v in sample_dict.items()}    
print("Squared dictionary:", squared_dict)

#copying a dictionary
copied_dict = sample_dict.copy()
print("Copied dictionary:", copied_dict)

#nested dictionaries
nested_dict = {
    "person1": {"name": "Bob", "age": 25},
    "person2": {"name": "Carol", "age": 28}
}
print("Nested dictionary:", nested_dict)
print("Person1's name:", nested_dict["person1"]["name"])   
print("Person2's age:", nested_dict["person2"]["age"])

#merging dictionaries
dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}
dict1.update(dict2)
print("Merged dictionary:", dict1)
