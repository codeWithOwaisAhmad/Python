# Python For Loop Explained for Beginners

# A 'for' loop in Python is used to iterate over a sequence (like a list, tuple, string, or range).
# It is useful when you want to repeat a block of code multiple times.

# Syntax:
# for variable in sequence:
#     # Code to execute in each iteration

# Example 1: Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Example 2: Looping through a string
message = "Hello"
for char in message:
    print("Character:", char)

# Example 3: Using the range() function
for num in range(5):  # Loops from 0 to 4
    print("Number:", num)

# Example 4: Specifying a range with start and end values
for num in range(1, 6):  # Loops from 1 to 5
    print("Counting:", num)

# Example 5: Using a step value in range()
for num in range(0, 10, 2):  # Loops from 0 to 8 with a step of 2
    print("Step:", num)

# Example 6: Looping through a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Example 7: Nested for loops (loop within a loop)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each inner loop

# Example 8: Using 'break' to exit a loop early
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print("Number:", num)

# Example 9: Using 'continue' to skip an iteration
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3")
        continue
    print("Number:", num)

# Example 10: Using 'else' with a for loop
for num in range(3):
    print("Iteration:", num)
else:
    print("Loop completed!")

# For loops are powerful for iterating through data and performing repeated actions.
# Experiment with different sequences and operations to master the 'for' loop!
