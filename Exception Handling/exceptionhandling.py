# exception_handling_examples.py

"""
Exception Handling in Python: From Basic to Advanced

Exception handling in Python is a mechanism that allows you to handle errors gracefully,
ensuring that your program can continue running or terminate cleanly when an error occurs.
This is crucial for building robust and reliable applications.
"""

# Basic Concepts

"""
1. Exception: An error that disrupts the normal flow of the program.
2. Try Block: The code that might throw an exception is placed inside a `try` block.
3. Except Block: The code that handles the exception is placed inside an `except` block.
4. Finally Block: This block contains code that will run no matter what, whether an exception was raised or not.
"""

# Basic Example

def basic_example():
    try:
        # Code that may raise an exception
        result = 10 / 0
    except ZeroDivisionError:
        # Code to handle the exception
        print("Cannot divide by zero!")
    finally:
        # Code that will always execute
        print("Execution completed.")

# Call the basic example function
basic_example()

"""
Explanation:
1. Try Block: The `try` block contains the code that may raise an exception. In this case, dividing by zero will raise a `ZeroDivisionError`.
2. Except Block: The `except` block handles the exception. If a `ZeroDivisionError` is raised, the message "Cannot divide by zero!" is printed.
3. Finally Block: The `finally` block contains code that will run regardless of whether an exception was raised or not. Here, it prints "Execution completed."
"""

# Advanced Concepts

"""
1. Multiple Except Blocks: You can have multiple `except` blocks to handle different exceptions.
2. Exception Hierarchy: Handle exceptions in a specific-to-general order.
3. Custom Exceptions: Define your own exceptions for specific use cases.
4. Raising Exceptions: Manually raise exceptions using the `raise` keyword.
"""

# Multiple Except Blocks Example

def multiple_except_blocks_example():
    try:
        # Code that may raise different exceptions
        value = int(input("Enter a number: "))
        result = 10 / value
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Execution completed.")

# Call the multiple except blocks example function
# Uncomment the line below to test the function
# multiple_except_blocks_example()

# Custom Exceptions Example

class CustomError(Exception):
    """Custom Exception"""
    pass

def custom_exceptions_example():
    try:
        raise CustomError("This is a custom error.")
    except CustomError as e:
        print(e)
    finally:
        print("Execution completed.")

# Call the custom exceptions example function
custom_exceptions_example()

# Raising Exceptions Example

def check_positive(number):
    if number < 0:
        raise ValueError("Negative value entered!")
    return number

def raising_exceptions_example():
    try:
        value = check_positive(-10)
    except ValueError as e:
        print(e)
    finally:
        print("Execution completed.")

# Call the raising exceptions example function
raising_exceptions_example()

"""
Conclusion:
Exception handling is a powerful feature in Python that helps you manage errors gracefully. By using `try`, `except`, and `finally` blocks,
you can ensure that your program can handle different types of errors and continue running or terminate gracefully.
Custom exceptions and raising exceptions manually provide additional flexibility to handle specific scenarios.
"""