"""
Python List Tutorial
====================

This tutorial covers the basics of Python lists with examples ranging from easy to hard.

1. Introduction to Lists
2. Basic Operations on Lists
3. Intermediate Operations on Lists
4. Advanced Operations on Lists

"""

# Easy Example: Creating and Accessing Lists
def easy_example():
    # Create a list of fruits
    fruits = ["apple", "banana", "cherry"]

    # Accessing elements in the list
    first_fruit = fruits[0]
    second_fruit = fruits[1]
    third_fruit = fruits[2]

    # Output the elements
    print(f"The first fruit is: {first_fruit}")
    print(f"The second fruit is: {second_fruit}")
    print(f"The third fruit is: {third_fruit}")

# Medium Example: Modifying Lists
def medium_example():
    # Create a list of fruits
    fruits = ["apple", "banana", "cherry"]

    # Modify elements in the list
    fruits[1] = "blueberry"

    # Add elements to the list
    fruits.append("date")
    fruits.insert(1, "apricot")

    # Remove elements from the list
    del fruits[0]
    fruits.remove("cherry")

    # Output the modified list
    print(f"Modified list of fruits: {fruits}")

# Hard Example: List Comprehensions and Nested Lists
def hard_example():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # List comprehension to create a new list with squared values
    squared_numbers = [x**2 for x in numbers]

    # Create a nested list (a list of lists)
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Accessing elements in a nested list
    first_row = nested_list[0]
    first_element_in_first_row = nested_list[0][0]

    # Output the results
    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squared_numbers}")
    print(f"Nested list: {nested_list}")
    print(f"First row of nested list: {first_row}")
    print(f"First element in the first row of nested list: {first_element_in_first_row}")