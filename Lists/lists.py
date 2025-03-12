# Python Lists Explained for Beginners

# Lists are one of the most versatile data types in Python.
# They are used to store multiple items in a single variable.
# Lists are created using square brackets [] and can hold different data types.

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# Example 2: Accessing list items using index
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Example 3: Changing list items
fruits[1] = "orange"
print("Updated Fruits List:", fruits)

# Example 4: Looping through a list
for fruit in fruits:
    print("Fruit:", fruit)

# Example 5: Checking if an item exists
if "apple" in fruits:
    print("Apple is in the list!")

# Example 6: Adding items to a list
fruits.append("mango")  # Adds at the end
print("List after append:", fruits)

fruits.insert(1, "kiwi")  # Adds at specific position
print("List after insert:", fruits)

# Example 7: Removing items from a list
fruits.remove("banana")  # Removes the first occurrence
print("List after removal:", fruits)

popped_fruit = fruits.pop()  # Removes the last item
print("Popped Fruit:", popped_fruit)
print("List after pop:", fruits)

# Example 8: Sorting a list
numbers = [5, 3, 8, 1, 2]
numbers.sort()
print("Sorted Numbers:", numbers)

# Example 9: Reversing a list
numbers.reverse()
print("Reversed Numbers:", numbers)

# Example 10: List Comprehension
squares = [x * x for x in range(6)]
print("Squares:", squares)

# Example 11: Copying a list
copy_fruits = fruits.copy()
print("Copied List:", copy_fruits)

# Example 12: Joining two lists
combined = fruits + numbers
print("Combined List:", combined)

# Example 13: Clearing a list
fruits.clear()
print("Cleared Fruits List:", fruits)

# Lists are powerful and flexible, making them an essential part of Python programming.
# Practice creating and manipulating lists to become comfortable with them!
