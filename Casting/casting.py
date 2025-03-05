# Python Casting Explained for Beginners

# Casting means converting one data type into another.
# Python provides built-in functions for casting: int(), float(), str(), and more.

# Example 1: Converting a string to an integer
num_str = "10"  # This is a string
to_int = int(num_str)  # Converts string to integer
print("String to Integer:", to_int, "| Type:", type(to_int))

# Example 2: Converting a string to a float
num_str2 = "10.5"
to_float = float(num_str2)  # Converts string to float
print("String to Float:", to_float, "| Type:", type(to_float))

# Example 3: Converting an integer to a string
num = 25
to_str = str(num)  # Converts integer to string
print("Integer to String:", to_str, "| Type:", type(to_str))

# Example 4: Converting a float to an integer (note: this removes decimal part)
num_float = 9.99
to_int_from_float = int(num_float)  # Converts float to integer
print("Float to Integer:", to_int_from_float, "| Type:", type(to_int_from_float))

# Example 5: Converting an integer to a float
num2 = 7
to_float_from_int = float(num2)  # Converts integer to float
print("Integer to Float:", to_float_from_int, "| Type:", type(to_float_from_int))

# Example 6: Converting a list of numbers (as strings) into integers using map()
num_list = ["1", "2", "3", "4"]
to_int_list = list(map(int, num_list))  # Converts each string to an integer
print("List of Strings to List of Integers:", to_int_list, "| Type:", type(to_int_list))

# Example 7: Converting a boolean to an integer
true_val = True
false_val = False
print("Boolean True to Integer:", int(true_val))  # 1
print("Boolean False to Integer:", int(false_val))  # 0

# Example 8: Converting an integer to a boolean
zero = 0
non_zero = 5
print("Integer 0 to Boolean:", bool(zero))  # False
print("Non-zero Integer to Boolean:", bool(non_zero))  # True

# Example 9: Converting a list to a string
char_list = ['H', 'e', 'l', 'l', 'o']
to_string = ''.join(char_list)  # Joins list elements into a single string
print("List to String:", to_string)

# Python casting is useful when handling different data types in programs.
# Try modifying the values and observe how they change!
