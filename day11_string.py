str1 = "Hello, World!"
# Accessing characters
print("First character:", str1[0])
print("Last character:", str1[-1])
print("----------------------------")
# Modifying characters (strings are immutable, so we create a new string)
str2 = str1[:7] + "Universe!"
print("Modified string:", str2)
print("----------------------------")
# String concatenation
str3 = str1 + " How are you?"
print("Concatenated string:", str3)
print("----------------------------")
# String slicing
print("Sliced string (first 5 characters):", str1[:5])
print("Sliced string (characters 7-12):", str1[7:12])
print("----------------------------")
# String methods
print("Uppercase string:", str1.upper())
print("Lowercase string:", str1.lower())
print("String with replaced characters:", str1.replace("World", "Universe"))
print("----------------------------")
# String formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print("Formatted string:", formatted_str)
print("----------------------------")
# String splitting
str4 = "apple,banana,cherry"
fruits = str4.split(",")
print("Split string into list:", fruits)
print("----------------------------")
# String joining
joined_str = " - ".join(fruits)
print("Joined string:", joined_str)
print("----------------------------")
# String length
print("Length of str1:", len(str1))
print("Length of str4:", len(str4))
print("----------------------------")