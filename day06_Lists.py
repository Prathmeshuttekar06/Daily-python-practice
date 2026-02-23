#practice on lists
#creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)
print("first element:", my_list[0])
print("last element:", my_list[-1])
print("length of the list:", len(my_list))
print("-------------------------")
#adding elements to a list
my_list.append(6)
print("after appending 6:", my_list)
#removing elements from a list
my_list.remove(3)
print("after removing 3:", my_list)
print("-------------------------")
#slicing a list
print("first three elements:", my_list[:3])
print("last two elements:", my_list[-2:])
print("-------------------------")

