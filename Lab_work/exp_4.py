# FOR LOOP
# Program to find the sum of all numbers stored in a list

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
    sum = sum+val

print("The sum is", sum)

#WHILE LOOP
# Program to add natural numbers up to sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    
print("The sum is", sum)