#to check if number is positive,negative or zero
# Read a number from the user
num = float(input("Enter a number: "))

# Check the sign of the number
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")