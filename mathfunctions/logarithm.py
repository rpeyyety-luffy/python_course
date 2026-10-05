#program to find logarithm
import math

# Get positive number input from user
num = float(input("Enter a positive number: "))

if num <= 0:
    print("Logarithm is only defined for positive numbers.")
else:
    # 1. Natural Logarithm (base e)
    natural_log = math.log(num)

    # 2. Base-10 Logarithm
    log10 = math.log10(num)

    # 3. Base-2 Logarithm
    log2 = math.log2(num)

    # Display results
    print(f"Natural Logarithm (ln({num})): {natural_log}")
    print(f"Base-10 Logarithm (log10({num})): {log10}")
    print(f"Base-2 Logarithm (log2({num})): {log2}")

    # Optional: Custom base logarithm
    base = float(input("\nEnter any custom base: "))
    if base <= 0 or base == 1:
        print("Base must be positive and not equal to 1.")
    else:
        custom_log = math.log(num, base)
        print(f"Logarithm of {num} with base {base}: {custom_log}")