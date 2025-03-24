# Python While Loop Explained for Beginners (Detailed Version)

# What is a While Loop?
# A while loop repeatedly executes a block of code as long as a given condition is true.
# It is used when the number of iterations is not known beforehand.

# Syntax of a While Loop:
# while condition:
#     statement(s)

# Example 1: Basic While Loop
print("\nBasic While Loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1  # Increment the counter
# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5

# Example 2: Sum of First 10 Natural Numbers
print("\nSum of First 10 Natural Numbers:")
sum = 0
num = 1
while num <= 10:
    sum += num
    num += 1
print("Sum:", sum)  # Output: 55

# Example 3: Using Break to Exit the Loop
print("\nUsing Break to Exit the Loop:")
count = 0
while True:
    print("Infinite Loop Count:", count)
    count += 1
    if count == 3:
        print("Breaking the loop!")
        break
# Output:
# Infinite Loop Count: 0
# Infinite Loop Count: 1
# Infinite Loop Count: 2
# Breaking the loop!

# Example 4: Using Continue to Skip Iteration
print("\nUsing Continue to Skip Iteration:")
number = 0
while number < 5:
    number += 1
    if number == 3:
        print("Skipping number 3!")
        continue
    print("Number:", number)
# Output:
# Number: 1
# Number: 2
# Skipping number 3!
# Number: 4
# Number: 5

# Example 5: Nested While Loop
print("\nNested While Loop:")
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2

# Important Tips:
# 1. Make sure to update the counter to avoid infinite loops.
# 2. Use break and continue wisely for better control.
# 3. Nested while loops can make code complex and harder to debug.
