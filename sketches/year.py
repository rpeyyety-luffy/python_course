#program to check if the years is a leap year, a century year and if both a century year and a leap year
# Read the year from the user
year = int(input("Enter a year: "))

# Check for both first, then individual conditions
if year % 400 == 0:
    print(f"{year} is BOTH a Century Year and a Leap Year.")
elif year % 100 == 0:
    print(f"{year} is a Century Year, but NOT a Leap Year.")
elif year % 4 == 0:
    print(f"{year} is a Leap Year, but NOT a Century Year.")
else:
    print(f"{year} is NEITHER a Century Year nor a Leap Year.")