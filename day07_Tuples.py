#creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print("first element:", my_tuple[0])
print("---------------------------")
#lopping through a tuple
print("elements in the tuple:")
for element in my_tuple:
    print(element)
print("---------------------------")
#length of a tuple
print("length of the tuple:", len(my_tuple))
print("---------------------------")
#count and index of an element in a tuple
print("count of 2 in the tuple:", my_tuple.count(2))
print("index of 3 in the tuple:", my_tuple.index(3))
print("---------------------------")
#slicing a tuple
print("first three elements:", my_tuple[:3])
print("last two elements:", my_tuple[-2:])
print("---------------------------")    