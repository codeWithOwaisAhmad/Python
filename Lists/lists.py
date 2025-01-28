# Python List Tutorial
# ====================
# This tutorial covers the basics of Python lists with examples ranging from easy to hard.

# 1. Introduction to Lists
# Lists are ordered collections of items, which can be of different data types.
# Lists are created using square brackets, and items are separated by commas.

# Example: Creating and Accessing Lists
def introduction_to_lists():
    # Create a list of fruits
    fruits = ["apple", "banana", "cherry"]

    # Accessing elements in the list using indices (0-based indexing)
    first_fruit = fruits[0]
    second_fruit = fruits[1]
    third_fruit = fruits[2]

    # Output the elements
    print(f"The first fruit is: {first_fruit}")
    print(f"The second fruit is: {second_fruit}")
    print(f"The third fruit is: {third_fruit}")

# 2. Basic Operations on Lists
def basic_operations():
    # Create a list of fruits
    fruits = ["apple", "banana", "cherry"]

    # Add elements to the list
    fruits.append("date")  # Adds an element to the end of the list
    fruits.insert(1, "apricot")  # Inserts an element at a specific position

    # Remove elements from the list
    fruits.remove("banana")  # Removes the first occurrence of the specified element
    popped_fruit = fruits.pop(2)  # Removes and returns the element at the specified index

    # Output the modified list and the removed element
    print(f"Modified list of fruits: {fruits}")
    print(f"Removed fruit: {popped_fruit}")

# 3. Intermediate Operations on Lists
def intermediate_operations():
    # Create a list of fruits
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]

    # Slicing lists
    first_three_fruits = fruits[:3]  # Get the first three elements
    last_two_fruits = fruits[-2:]  # Get the last two elements

    # List comprehension
    fruit_lengths = [len(fruit) for fruit in fruits]  # Create a new list with the lengths of each fruit

    # Output the results
    print(f"First three fruits: {first_three_fruits}")
    print(f"Last two fruits: {last_two_fruits}")
    print(f"Lengths of each fruit: {fruit_lengths}")

# 4. Advanced Operations on Lists
def advanced_operations():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # List comprehension with condition
    squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]  # Square only the even numbers

    # Create a nested list (a list of lists)
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Accessing elements in a nested list
    first_row = nested_list[0]  # First sublist
    first_element_in_first_row = nested_list[0][0]  # First element in the first sublist

    # Output the results
    print(f"Original numbers: {numbers}")
    print(f"Squared even numbers: {squared_even_numbers}")
    print(f"Nested list: {nested_list}")
    print(f"First row of nested list: {first_row}")
    print(f"First element in the first row of nested list: {first_element_in_first_row}")


# Example usage of the functions
print("Introduction to Lists")
introduction_to_lists()
print("\nBasic Operations on Lists")
basic_operations()
print("\nIntermediate Operations on Lists")
intermediate_operations()
print("\nAdvanced Operations on Lists")
advanced_operations()
