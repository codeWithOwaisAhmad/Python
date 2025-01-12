### Python Casting Tutorial
# This script provides examples and explanations for casting in Python.

# Easy Example: Casting an Integer to a String
print("\n--- Easy Example ---")
num = 10  # Integer
print("Before casting:", type(num))  # Check type before casting

# Casting integer to string
num_str = str(num)
print("After casting:", type(num_str))  # Check type after casting

# Output the result
print("The number as a string is:", num_str)

# Medium Example: Converting a List of Strings to Integers
print("\n--- Medium Example ---")
str_numbers = ["1", "2", "3", "4"]  # List of strings
print("Before casting:", [type(x) for x in str_numbers])  # Check types

# Casting each string to an integer
int_numbers = [int(x) for x in str_numbers]
print("After casting:", [type(x) for x in int_numbers])  # Check types

# Output the converted list
print("The list of integers is:", int_numbers)

# Hard Example: Handling Mixed Data Types for Casting
print("\n--- Hard Example ---")
data = ["42", 3.14, "7.5", 15, "hello"]  # Mixed list of strings, floats, integers, and a non-numeric string
int_list = []  # To store integers after casting

for item in data:
    try:
        # Attempt to cast item to integer
        int_value = int(float(item))  # Convert to float first if it's a string with decimals, then to integer
        int_list.append(int_value)
    except ValueError:
        # Handle non-numeric strings gracefully
        print(f"Cannot cast '{item}' to an integer.")

# Output the valid integers
print("The list of valid integers is:", int_list)
