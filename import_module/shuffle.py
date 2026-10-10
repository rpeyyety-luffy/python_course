import random

# Sample data
my_list = [10, 20, 30, 40, 50]
my_tuple = ("red", "green", "blue", "yellow")
my_string = "python"
#note that shuffle only works for list not tuple and string...so you have to convert them first and then they will work
# 1. Using random.shuffle() on a List
# Note: random.shuffle() modifies the list directly in-place and returns None

random.shuffle(my_list)
print(f"Shuffled List: {my_list}")

# 2. Using random.shuffle() on a Tuple
# Convert to list first, shuffle in-place, then convert back to tuple
list_from_tuple = list(my_tuple)
random.shuffle(list_from_tuple)
shuffled_tuple = tuple(list_from_tuple)
print(f"Shuffled Tuple: {shuffled_tuple}")

# 3. Using random.shuffle() on a String
# Convert string to list of characters, shuffle in-place, then join back to string
list_from_string = list(my_string)
random.shuffle(list_from_string)
shuffled_string = "".join(list_from_string)
print(f"Shuffled String: {shuffled_string}")