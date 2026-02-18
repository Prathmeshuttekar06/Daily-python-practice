#Day 04 - Conditional Statements 
#simple if-else statement
age=18

if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("-------------------------")
#if-elif-else statement
marks=85
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:    print("Grade: F")
print("-------------------------")
#Nested if statement
num=10
if num>0:
    print("The number is positive.")
    if num%2==0:
        print("The number is even.")
    else:
        print("The number is odd.")
print("-------------------------")

#Example 1 : Check Positive, Negative or Zero
number = -5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
print("-------------------------")
#Example 2 : find the largest of three numbers
num1 = 10
num2 = 20
num3 = 15
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
print("-------------------------")
#Example 3 : Check leap year
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

