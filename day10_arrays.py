arr1 = [1, 2, 3, 4, 5]
print("Original array:", arr1)
print("----------------------------")
# Accessing elements
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("----------------------------")
# Modifying elements
arr1[2] = 10
print("Modified array:", arr1)
print("----------------------------")
# Adding elements
arr1.append(6)
print("Array after appending 6:", arr1)
print("----------------------------")
# Removing elements
arr1.remove(2)
print("Array after removing 2:", arr1)
print("----------------------------")
# Slicing arrays
print("Sliced array (first 3 elements):", arr1[:3])
print("----------------------------")