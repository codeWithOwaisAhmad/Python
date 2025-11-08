
# Conditionals allow your program to make decisions based on conditions.
# The main conditional statements in Python are: if, elif, and else.

# Example 1: Basic if statement
number = 10
if number > 5:  # Checks if the number is greater than 5
    print('Number is greater than 5')

# Example 2: if-else statement
age = 17
if age >= 18:
    print('You are an adult.')
else:
    print('You are a minor.')

# Example 3: if-elif-else statement
score = 85
if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
else:
    print('Grade: F')

# Example 4: Using multiple conditions with 'and'
x = 7
if x > 5 and x < 10:
    print('x is between 5 and 10')

# Example 5: Using 'or' in conditionals
y = 3
if y < 2 or y > 8:
    print('y is either less than 2 or greater than 8')
else:
    print('y is between 2 and 8')

# Example 6: Checking if a value is in a list
fruits = ['apple', 'banana', 'cherry']
if 'banana' in fruits:
    print('Banana is in the list!')

# Example 7: Nested if statements
number = 15
if number > 10:
    print('Number is greater than 10')
    if number % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

# Example 8: Ternary operator (short if-else)
num = 20
result = 'Even' if num % 2 == 0 else 'Odd'
print(f'Number is {result}')

# This script demonstrates the basics of conditionals in Python.
# Try changing the values of variables to see different outputs!















