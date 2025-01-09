# Variables in Python

# 1. Introduction to Variables
# Variables are used to store data that can be used later in the program.
# In Python, you don't need to declare the type of variable explicitly.

# Example of variable assignment
x = 10  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_active = True  # Boolean

# 2. Naming Rules
# Variable names must start with a letter or an underscore
# and can only contain alphanumeric characters and underscores.

# Valid variable names
age = 25
_address = "123 Main St"

# Invalid variable names
# 2nd_place = "Second"  # SyntaxError: invalid syntax
# first-place = 1  # SyntaxError: invalid syntax

# 3. Reassigning Variables
# Variables can be reassigned to different values or types.

# Initial assignment
count = 100
print(count)  # Output: 100

# Reassignment
count = 50
print(count)  # Output: 50

# Different type
count = "fifty"
print(count)  # Output: fifty

# 4. Multiple Assignments
# You can assign multiple variables at once.

a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

# 5. Constants
# In Python, constants are usually defined using uppercase letters.
# Note that Python does not enforce constant values, this is just a convention.

PI = 3.14159
GRAVITY = 9.8

# 6. Data Types
# Common data types in Python include integers, floats, strings, and booleans.

# Integer
num = 10

# Float
height = 5.8

# String
city = "New York"

# Boolean
is_open = False

# 7. Type Conversion
# You can convert between different data types using functions like int(), float(), str(), and bool().

# Convert float to integer
num = 3.75
num = int(num)
print(num)  # Output: 3

# Convert integer to string
age = 25
age_str = str(age)
print(age_str)  # Output: "25"

# Convert string to float
price = "9.99"
price = float(price)
print(price)  # Output: 9.99

# 8. Checking Variable Types
# You can use the type() function to check the type of a variable.

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_active))  # Output: <class 'bool'>

# 9. Deleting Variables
# You can delete variables using the del statement.

del x
# print(x)  # This will raise an error because x is deleted.

