# Python Tuples Explained for Beginners (Detailed Version)

# What are Tuples in Python?
# A tuple is an ordered, immutable collection of elements.
# Tuples are defined using parentheses () and can contain elements of different data types.
# Once a tuple is created, its elements cannot be changed, added, or removed.

# Creating Tuples
print("\nCreating Tuples")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (1, 'Hello', 3.14)
tuple4 = ()  # Empty tuple
tuple5 = (42,)  # Single element tuple (with a trailing comma)
print("Tuple 1:", tuple1)  # Output: (1, 2, 3, 4, 5)
print("Tuple 2:", tuple2)  # Output: ('apple', 'banana', 'cherry')
print("Tuple 3:", tuple3)  # Output: (1, 'Hello', 3.14)
print("Empty Tuple:", tuple4)  # Output: ()
print("Single Element Tuple:", tuple5)  # Output: (42,)

# Accessing Tuple Elements
print("\nAccessing Tuple Elements")
print("First element of tuple1:", tuple1[0])  # Output: 1
print("Last element of tuple2:", tuple2[-1])  # Output: cherry

# Slicing Tuples
print("\nSlicing Tuples")
sliced_tuple = tuple1[1:4]
print("Sliced Tuple (1:4):", sliced_tuple)  # Output: (2, 3, 4)

# Tuple Length
print("\nTuple Length")
print("Length of tuple1:", len(tuple1))  # Output: 5

# Concatenating Tuples
print("\nConcatenating Tuples")
tuple6 = tuple1 + tuple2
print("Concatenated Tuple:", tuple6)  # Output: (1, 2, 3, 4, 5, 'apple', 'banana', 'cherry')

# Repeating Tuples
print("\nRepeating Tuples")
tuple7 = ('Hi!',) * 3
print("Repeated Tuple:", tuple7)  # Output: ('Hi!', 'Hi!', 'Hi!')

# Checking Membership
print("\nChecking Membership")
print("'banana' in tuple2:", 'banana' in tuple2)  # Output: True
print("'grape' in tuple2:", 'grape' in tuple2)  # Output: False

# Tuple Methods
print("\nTuple Methods")
tuple8 = (1, 2, 3, 2, 4, 2)
print("Count of 2 in tuple8:", tuple8.count(2))  # Output: 3
print("Index of 3 in tuple8:", tuple8.index(3))  # Output: 2

# Unpacking Tuples
print("\nUnpacking Tuples")
a, b, c = tuple3
print("a:", a)  # Output: 1
print("b:", b)  # Output: Hello
print("c:", c)  # Output: 3.14

# Advantages of Tuples:
# 1. Fast and efficient due to immutability.
# 2. Can be used as dictionary keys and elements of sets.
# 3. Useful for fixed data structures (e.g., coordinates).

# Disadvantages of Tuples:
# 1. Cannot be modified after creation.
# 2. Lack of flexibility compared to lists.

# Tips for Using Tuples:
# 1. Use tuples for fixed data that shouldn't change.
# 2. Use lists if you need to modify the data frequently.
