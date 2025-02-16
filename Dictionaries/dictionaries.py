"""
Tutorial: Basics of Python Dictionaries

Dictionaries in Python are a collection of key-value pairs. Each key is unique, and the values can be of any data type. 
Dictionaries are also mutable, meaning you can change their content without changing their identity.
"""

# Easy Example: Creating and Accessing a Dictionary

# Step-by-step Explanation:
# 1. We create a dictionary with three key-value pairs.
# 2. We access the value associated with the key 'name'.
# 3. We add a new key-value pair to the dictionary.
# 4. We update the value of an existing key.

# Creating a dictionary
person = {
    "name": "Owais",
    "age": 25,
    "city": "New York"
}

# Accessing a value by key
print("Name:", person["name"])  # Output: Name: Owais

# Adding a new key-value pair
person["email"] = "owais@example.com"
print("Updated Dictionary:", person)
# Output: Updated Dictionary: {'name': 'Owais', 'age': 25, 'city': 'New York', 'email': 'owais@example.com'}

# Updating an existing value
person["age"] = 26
print("Updated Age:", person["age"])  # Output: Updated Age: 26


# Medium Example: Iterating Over a Dictionary

# Step-by-step Explanation:
# 1. We create a dictionary representing a book.
# 2. We iterate over the dictionary to print each key-value pair.
# 3. We use the items() method to get key-value pairs as tuples.

# Creating a dictionary
book = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2021
}

# Iterating over the dictionary
for key, value in book.items():
    print(f"{key}: {value}")
# Output:
# title: Python Programming
# author: John Doe
# year: 2021


# Hard Example: Nested Dictionaries and Complex Operations

# Step-by-step Explanation:
# 1. We create a nested dictionary representing a library with multiple books.
# 2. We iterate over the nested dictionary to print details of each book.
# 3. We demonstrate adding a new book to the library.

# Creating a nested dictionary
library = {
    "book1": {
        "title": "Python Basics",
        "author": "Jane Smith",
        "year": 2020
    },
    "book2": {
        "title": "Advanced Python",
        "author": "James Brown",
        "year": 2019
    }
}

# Iterating over the nested dictionary
for book_id, book_info in library.items():
    print(f"Book ID: {book_id}")
    for key, value in book_info.items():
        print(f"  {key}: {value}")
# Output:
# Book ID: book1
#   title: Python Basics
#   author: Jane Smith
#   year: 2020
# Book ID: book2
#   title: Advanced Python
#   author: James Brown
#   year: 2019

# Adding a new book to the library
library["book3"] = {
    "title": "Python Data Science",
    "author": "Emily Davis",
    "year": 2022
}
print("\nUpdated Library:")
for book_id, book_info in library.items():
    print(f"Book ID: {book_id}")
    for key, value in book_info.items():
        print(f"  {key}: {value}")
# Output:
# Updated Library:
# Book ID: book1
#   title: Python Basics
#   author: Jane Smith
#   year: 2020
# Book ID: book2
#   title: Advanced Python
#   author: James Brown
#   year: 2019
# Book ID: book3
#   title: Python Data Science
#   author: Emily Davis
#   year: 2022
