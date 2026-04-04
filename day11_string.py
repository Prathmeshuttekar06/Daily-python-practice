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