#creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
print("name:", my_dict["name"])
print("---------------------------")
#lopping through a dictionary
print("keys in the dictionary:")
for key in my_dict:
    print(key)  
print("---------------------------")
print("values in the dictionary:")  
for value in my_dict.values():
    print(value)    
print("---------------------------")
print("key-value pairs in the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)
print("---------------------------")
#adding new key-value pair to the dictionary
my_dict["country"] = "USA"
print("updated dictionary:", my_dict)
print("---------------------------")
#removing a key-value pair from the dictionary
del my_dict["age"]
print("updated dictionary after deletion:", my_dict)
print("---------------------------")
#dictionary methods
print("keys in the dictionary:", my_dict.keys())
print("values in the dictionary:", my_dict.values())    
print("items in the dictionary:", my_dict.items())
print("---------------------------")