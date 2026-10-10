#program 8 cards input from user
# 1. Take N from the user
N = int(input("Enter the total number of cards (N): "))

# 2. Calculate the expected sum of cards from 1 to N
exp_sum = N * (N + 1) // 2

# 3. Read the remaining (N - 1) cards from the user
print(f"Enter the {N - 1} remaining cards (separated by spaces):")
reamaining_card = list(map(int, input().split()))

# 4. Actual sum of the given cards
act_sum = sum(reamaining_card)

# 5. Calculate the lost card
lost = exp_sum - act_sum

# 6. Display the result
print("\nExpected Sum:", exp_sum)
print("Actual Sum:", act_sum)
print("Lost Card:", lost)