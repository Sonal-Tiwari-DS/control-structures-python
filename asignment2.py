# Assignment 2: Control Structures in Python
# This program contains two tasks:
# 1. Check if a number is even or odd
# 2. Calculate the sum of integers from 1 to 50

# _________________________________________
# Task 1: Check if a Number is Even or Odd
# _________________________________________

print("TASK 1: Check if a Number is Even or Odd")
print("This program checks whether a number entered by the user is even or odd.\n")

# Take an integer input from the user
num = int(input("Enter an integer: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.\n")
else:
    print(f"{num} is an odd number.\n")

# _________________________________________
# Task 2: Sum of Integers from 1 to 50 Using a Loop
# _________________________________________

print("TASK 2: Sum of Integers from 1 to 50")
print("This program calculates the sum of all integers from 1 to 50 using a for loop.\n")

# Initialize a variable to store the sum
total_sum = 0

# Use a for loop to iterate from 1 to 50 (inclusive)
for i in range(1, 51):
    total_sum += i  # Add each number to total_sum

# Display the final sum
print(f"The sum of integers from 1 to 50 is: {total_sum}")
