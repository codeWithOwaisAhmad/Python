# Python Exception Handling Explained for Beginners

# Exception handling in Python allows us to handle runtime errors gracefully.
# The 'try' block lets us test a block of code for errors.
# The 'except' block handles the error if it occurs.

# Example 1: Basic try-except block
try:
    x = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 2: Handling multiple exceptions
try:
    num = int("abc")  # This will cause a ValueError
except ValueError:
    print("Error: Cannot convert string to integer.")
except TypeError:
    print("Error: Type mismatch occurred.")

# Example 3: Using a generic exception
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index out of range error
except Exception as e:
    print("An error occurred:", e)

# Example 4: Using finally block (executes no matter what)
try:
    f = open("sample.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution completed.")

# Example 5: Raising custom exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Access granted."

try:
    print(check_age(15))  # Will raise an exception
except ValueError as e:
    print("Custom Exception:", e)

# Exception handling is crucial for writing robust and error-free programs.
# Try modifying the code to explore different exceptions!
f
