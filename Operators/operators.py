# Python Operators Tutorial with Outputs

# ---------------------------
# 1. Arithmetic Operators
# ---------------------------

print("Arithmetic Operators")
a, b = 15, 4

# Easy Example
print("Addition:", a + b)  # Output: 19
print("Subtraction:", a - b)  # Output: 11
print("Multiplication:", a * b)  # Output: 60

# Medium Example
base = 5
exponent = 3
dividend = 20
divisor = 6
print("Exponentiation (5^3):", base ** exponent)  # Output: 125
print("Remainder (20 % 6):", dividend % divisor)  # Output: 2

# Hard Example
num1 = 43
num2 = 6
floor_result = num1 // num2
combined_result = (num1 + num2) * 2 - (num1 % num2)
print("Floor Division:", floor_result)  # Output: 7
print("Combined Result:", combined_result)  # Output: 94

print("\n")  # Blank line for separation


# ---------------------------
# 2. Comparison Operators
# ---------------------------

print("Comparison Operators")
x, y, z = 30, 20, 10

# Easy Example
print("Is x equal to y?", x == y)  # Output: False
print("Is x greater than y?", x > y)  # Output: True

# Medium Example
print("Is x greater than y and y greater than z?", x > y > z)  # Output: True
print("Is x not equal to z?", x != z)  # Output: True

# Hard Example
a, b, c = 15, 10, 20
result = a > b and b < c and a + b < c
print("Complex Comparison:", result)  # Output: True

print("\n")  # Blank line for separation


# ---------------------------
# 3. Logical Operators
# ---------------------------

print("Logical Operators")
x, y = 10, 20

# Easy Example
print("Logical AND:", x < 15 and y > 15)  # Output: True

# Medium Example
x, y = 5, 25
print("Logical OR:", x > 10 or y > 10)  # Output: True

# Hard Example
a, b = 5, 15
print("Logical NOT:", not (a > b))  # Output: True

print("\n")  # Blank line for separation


# ---------------------------
# 4. Assignment Operators
# ---------------------------

print("Assignment Operators")

# Easy Example
x = 10
x += 5  # Add 5 to x
print("New value of x:", x)  # Output: 15

# Medium Example
y = 7
y *= 3  # Multiply y by 3
print("New value of y:", y)  # Output: 21

# Hard Example
z = 20
z /= 4  # Divide by 4
z += 10  # Add 10
z *= 2   # Multiply by 2
print("Final value of z:", z)  # Output: 40.0
