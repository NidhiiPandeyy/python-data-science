# if condition

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
    print("This is also always printed.")

# if...else condition

num = 7
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

# if...elif...else condition

num = 0

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")