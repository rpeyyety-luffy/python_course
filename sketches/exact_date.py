#program to check i f the date is exact by inputing date year and month and checking if all are same
# Read inputs from the user
day = int(float(input("Enter day: ")))
month = int(float(input("Enter month: ")))
year = int(float(input("Enter year: ")))

# --- STEP 1: Determine if the year is a Leap Year ---
is_century_year = (year % 100 == 0)
is_divisible_by_400 = (year % 400 == 0)
is_divisible_by_4 = (year % 4 == 0)

is_leap_year = is_divisible_by_400 or (is_divisible_by_4 and not is_century_year)

# --- STEP 2: Determine maximum allowed days for the month ---
is_valid_month = (month >= 1 and month <= 12)
is_valid_year = (year >= 1)

if is_valid_month:
    if month == 2:
        if is_leap_year:
            max_days = 29
        else:
            max_days = 28
    elif month in (4, 6, 9, 11):
        max_days = 30
    else:
        max_days = 31
else:
    max_days = 0

is_valid_day = (day >= 1 and day <= max_days)
is_valid_date = is_valid_year and is_valid_month and is_valid_day

# --- STEP 3: Check if Day, Month, and Year are Exact ---
is_exact_match = (day == month) and (month == year)

# --- STEP 4: Output Results ---
if not is_valid_date:
    print(f"INVALID DATE: {day}/{month}/{year} is not a valid calendar date.")
else:
    print(f"VALID DATE: {day}/{month}/{year}")

    if is_exact_match:
        print(f"EXACT DATE MATCH: Day, Month, and Year are all identical ({day})!")
    else:
        print("NOT AN EXACT MATCH: Day, Month, and Year are not all equal.")