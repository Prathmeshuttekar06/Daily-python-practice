#simple function
def greet():    print("Hello, welcome to Python programming!")
greet()
print("---------------------------")
#function with parameters
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming!")
greet_user("Alice")
greet_user("Bob")
print("---------------------------")
#function with return value
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum of 5 and 3 is:", result)
print("---------------------------")
#function with default parameter value
def greet_user(name="Guest"):
    print(f"Hello, {name}! Welcome to Python programming!")    
greet_user()  # Uses default value "Guest"
greet_user("Charlie")  # Uses provided value "Charlie"
print("---------------------------")
#even odd function
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
number = 10
if is_even(number):
    print(f"{number} is even.") 