#for loops
#print numbers from 1 to 5 using a for loop
for i in range(1, 6):
    print(i)
print("-------------------------")
#print even numbers from 1 to 10 using a for loop
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("-------------------------")
#while loops
#print numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1
print("-------------------------")
#print sum of first 10 natural numbers using a while loop
n = 10
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of first 10 natural numbers:", sum)