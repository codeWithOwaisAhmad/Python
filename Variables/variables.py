# Python Variables Explained for Beginners (Detailed Version)

# What are Variables in Python?
# Variables are used to store data that can be used and manipulated later in the program.
# In Python, variables do not need explicit declaration. They are created when you assign a value to them.

# Variable Naming Rules:
# 1. Must start with a letter (a-z, A-Z) or underscore (_)
# 2. Cannot start with a number
# 3. Can contain letters, numbers, and underscores
# 4. Variable names are case-sensitive (age and Age are different)

# Creating Variables
print("\nCreating Variables")
x = 5
name = "John"
salary = 2500.50
is_student = True
print("x:", x)  # Output: 5
print("name:", name)  # Output: John
print("salary:", salary)  # Output: 2500.5
print("is_student:", is_student)  # Output: True

# Multiple Assignment
print("\nMultiple Assignment")
a, b, c = 10, 20, 30
print("a:", a)  # Output: 10
print("b:", b)  # Output: 20
print("c:", c)  # Output: 30

# Assigning the Same Value to Multiple Variables
print("\nSame Value to Multiple Variables")
p = q = r = 100
print("p:", p)  # Output: 100
print("q:", q)  # Output: 100
print("r:", r)  # Output: 100

# Changing Variable Values
print("\nChanging Variable Values")
age = 18
print("Original age:", age)  # Output: 18
age = 21
print("Updated age:", age)  # Output: 21

# Variable Types
print("\nVariable Types")
print("Type of x:", type(x))  # Output: <class 'int'>
print("Type of name:", type(name))  # Output: <class 'str'>
print("Type of salary:", type(salary))  # Output: <class 'float'>
print("Type of is_student:", type(is_student))  # Output: <class 'bool'>

# Deleting Variables
print("\nDeleting Variables")
del x
try:
    print(x)  # This will raise an error since x is deleted
except NameError:
    print("Variable 'x' is not defined.")

# Advantages of Using Variables:
# 1. Makes code readable and maintainable.
# 2. Reduces redundancy by storing reusable values.
# 3. Enables dynamic changes in data without altering the entire code.

# Tips for Using Variables:
# 1. Use meaningful names that reflect the purpose of the variable.
# 2. Avoid using reserved keywords as variable names.
# 3. Follow a consistent naming convention (e.g., snake_case or camelCase).
