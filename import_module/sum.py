# program to add random number in a list and print the sum of the list
import random

# Get the number of random elements to generate
count = int(input("How many random numbers do you want to generate? "))

# Get the range for random numbers
min_val = int(input("Enter minimum possible value: "))
max_val = int(input("Enter maximum possible value: "))

numbers = []

# Generate random numbers and add them to the list
for _ in range(count):
    rand_num = random.randint(min_val, max_val)
    numbers.append(rand_num)

# Calculate sum of the list
total_sum = sum(numbers)

# Display results
print(f"\nGenerated List: {numbers}")
print(f"Sum of the list: {total_sum}")