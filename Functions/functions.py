# Python Functions Explained for Beginners

# Functions in Python are reusable blocks of code that perform a specific task.
# They help in organizing code and avoiding repetition.

# Syntax:
# def function_name(parameters):
#     # Code block
#     return value (optional)

# Example 1: A simple function without parameters
def greet():
    print("Hello, welcome to Python functions!")

greet()  # Calling the function

# Example 2: A function with parameters
def add_numbers(a, b):
    result = a + b
    return result

print("Sum:", add_numbers(5, 3))

# Example 3: Function with default parameters
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice")  # Uses default age
introduce("Bob", 25)  # Overrides default age

# Example 4: Returning multiple values from a function
def calculate(x, y):
    sum_result = x + y
    diff_result = x - y
    return sum_result, diff_result

add, subtract = calculate(10, 5)
print("Addition:", add)
print("Subtraction:", subtract)

# Example 5: Using *args for variable-length arguments
def multiply(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print("Product:", multiply(2, 3, 4))

# Example 6: Using **kwargs for keyword arguments
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="John", age=30, city="New York")

# Example 7: Lambda functions (anonymous functions)
square = lambda x: x * x
print("Square of 5:", square(5))

# Example 8: Nested functions
def outer_function(text):
    def inner_function():
        print("Inner Function:", text)
    inner_function()

outer_function("Hello from the outer function!")

# Functions are essential for writing modular and reusable code.
# Practice creating different functions to understand how they work!
