#advance level function
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def calculator(x,y,operation):
    return operation(x,y)
print("Calculator result (add):", calculator(10,5,add))
print("Calculator result (sub):", calculator(10,5,sub))
print("Calculator result (mul):", calculator(10,5,mul))
print("Calculator result (div):", calculator(10,5,div))
print("----------------------------")
#lambda function
square = lambda x: x**2
print("Square of 5:", square(5))
cube = lambda x: x**3
print("Cube of 5:", cube(5))
add_lambda = lambda x,y: x+y
print("Sum of 10 and 5 using lambda:", add_lambda(10,5))
print("----------------------------")
#higher order function
def apply_operation(x,y,operation):
    return operation(x,y)   
print("Applying add operation:", apply_operation(10,5,add))
print("Applying sub operation:", apply_operation(10,5,sub))
print("Applying mul operation:", apply_operation(10,5,mul))
print("Applying div operation:", apply_operation(10,5,div))
print("----------------------------")
#map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)
cubed_numbers = list(map(lambda x: x**3, numbers))
print("Cubed numbers:", cubed_numbers)
print("----------------------------")
#filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)
print("----------------------------")
