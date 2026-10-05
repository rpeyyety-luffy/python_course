#program to find factorial of number by importing math
import math

# Input: Get integer from user
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    # Calculate factorial using math.factorial()
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")