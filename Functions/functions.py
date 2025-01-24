# Functions in Python
# --------------------

# Introduction to Functions
# A function is a block of reusable code that performs a specific task. Functions help in organizing code, making it more readable, and enabling code reuse.

# Easy Example: Basic Function
# ----------------------------
# This example demonstrates how to define and call a basic function that prints a greeting message.

def greet():
    """
    This function prints a greeting message.
    """
    print("Hello, welcome to the world of functions in Python!")

# Calling the function
greet()

# Explanation:
# 1. We define a function named 'greet' using the 'def' keyword.
# 2. Inside the function, we use the 'print' statement to display a greeting message.
# 3. We call the function 'greet()' to execute the code inside the function.

# Output:
# Hello, welcome to the world of functions in Python!


# Medium Example: Function with Parameters
# ----------------------------------------
# This example demonstrates how to define a function that takes parameters and returns a value.

def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b

# Calling the function with arguments
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

# Explanation:
# 1. We define a function named 'add_numbers' that takes two parameters 'a' and 'b'.
# 2. Inside the function, we return the sum of 'a' and 'b'.
# 3. We call the function with arguments 5 and 3 and store the result in the variable 'result'.
# 4. We print the result using an f-string.

# Output:
# The sum of 5 and 3 is: 8


# Hard Example: Recursive Function
# --------------------------------
# This example demonstrates how to define a recursive function that calculates the factorial of a number.

def factorial(n):
    """
    This function calculates the factorial of a given number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function with an argument
result = factorial(5)
print(f"The factorial of 5 is: {result}")

# Explanation:
# 1. We define a function named 'factorial' that takes one parameter 'n'.
# 2. Inside the function, we check if 'n' is equal to 0. If it is, we return 1 (base case).
# 3. If 'n' is not 0, we return 'n' multiplied by the result of calling 'factorial' with 'n-1' (recursive case).
# 4. We call the function with the argument 5 and store the result in the variable 'result'.
# 5. We print the result using an f-string.

# Output:
# The factorial of 5 is: 120