# Python Dictionaries Explained for Beginners

# A dictionary in Python is a collection of key-value pairs.
# It is unordered, mutable, and does not allow duplicate keys.

# Example 1: Creating a dictionarya
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", person)
print("Type:", type(person))

# Example 2: Accessing values using keys
print("Name:", person["name"])  # Access value by key
print("Age:", person.get("age"))  # Using get() method

# Example 3: Adding a new key-value pair
person["job"] = "Engineer"
print("Updated Dictionary:", person)

# Example 4: Modifying an existing value
person["age"] = 26  # Update value of a key
print("Modified Dictionary:", person)

# Example 5: Removing a key-value pair
del person["city"]  # Using del keyword
print("Dictionary after deletion:", person)

# Example 6: Looping through a dictionary
print("Dictionary Keys:")
for key in person:
    print(key)  # Prints only keys

print("Dictionary Values:")
for value in person.values():
    print(value)  # Prints only values

print("Dictionary Items:")
for key, value in person.items():
    print(key, ":", value)  # Prints key-value pairs

# Example 7: Checking if a key exists
if "name" in person:
    print("Key 'name' exists in dictionary")

# Example 8: Dictionary length
print("Number of key-value pairs:", len(person))

# Example 9: Copying a dictionary
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

# Example 10: Clearing all elements from dictionary
person.clear()
print("Cleared Dictionary:", person)

# Dictionaries are powerful data structures used in Python for efficient data management.
# Try modifying the dictionary and experiment with different methods!






