# Python Sets Explained for Beginners (Detailed Version)

# What are Sets in Python?
# A set is an unordered collection of unique elements.
# Sets do not allow duplicate values and are mutable, meaning elements can be added or removed.
# Sets are defined using curly braces {} or the set() constructor.

# Why Use Sets?
# - To store unique values and eliminate duplicates.
# - For efficient membership testing (checking if an element exists).
# - To perform mathematical set operations like union, intersection, difference, and symmetric difference.

# Creating a Set
print("\nCreating Sets")
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])  # Using set() constructor
print("Set 1:", set1)  # Output: {1, 2, 3, 4, 5}
print("Set 2:", set2)  # Output: {3, 4, 5, 6, 7}

# Adding and Removing Elements
print("\nAdding and Removing Elements")
set1.add(6)  # Adding a single element
print("After adding 6 to Set 1:", set1)  # Output: {1, 2, 3, 4, 5, 6}
set1.update([7, 8, 9])  # Adding multiple elements
print("After adding 7, 8, 9 to Set 1:", set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
set1.remove(3)  # Removing an element
print("After removing 3 from Set 1:", set1)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}
set1.discard(10)  # No error if element not present
print("After discarding 10 from Set 1:", set1)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

# Mathematical Set Operations
print("\nMathematical Set Operations")

# Union: Combines elements from both sets (removes duplicates)
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9, 3}

# Intersection: Elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)  # Output: {4, 5, 6, 7}

# Difference: Elements present in Set 1 but not in Set 2
difference_set = set1.difference(set2)
print("Difference of Set 1 - Set 2:", difference_set)  # Output: {1, 2, 8, 9}

# Symmetric Difference: Elements present in either of the sets, but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of Set 1 and Set 2:", symmetric_difference_set)  # Output: {1, 2, 8, 9, 3}

# Set Membership Testing
print("\nSet Membership Testing")
print("Is 4 in Set 1?:", 4 in set1)  # Output: True
print("Is 10 in Set 1?:", 10 in set1)  # Output: False

# Set Comprehension
print("\nSet Comprehension")
square_set = {x**2 for x in range(5)}
print("Square Set:", square_set)  # Output: {0, 1, 4, 9, 16}

# Advantages of Sets:
# 1. Fast membership testing (O(1) on average).
# 2. Automatically removes duplicate values.
# 3. Useful for mathematical operations.

# Disadvantages of Sets:
# 1. Unordered, so elements cannot be accessed by index.
# 2. Cannot store duplicate items.
# 3. Elements must be hashable (e.g., no lists or dictionaries within sets).

# Tips for Using Sets:
# 1. Use sets when you need unique values and efficient lookups.
# 2. Utilize set operations for mathematical computations.
# 3. Be cautious with mutable elements, as they are not allowed in sets.
