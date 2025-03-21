# Python Strings Explained for Beginners (Detailed Version)

# What are Strings in Python?
# A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning their content cannot be changed after creation.

# Creating Strings
print("\nCreating Strings")
str1 = 'Hello, World!'
str2 = "Python is awesome"
str3 = '''This is a multi-line
string in Python.'''
print("String 1:", str1)  # Output: Hello, World!
print("String 2:", str2)  # Output: Python is awesome
print("String 3:", str3)  # Output: This is a multi-line

# Accessing Characters in Strings
print("\nAccessing Characters")
print("First character of str1:", str1[0])  # Output: H
print("Last character of str1:", str1[-1])  # Output: !

# String Length
print("\nString Length")
print("Length of str1:", len(str1))  # Output: 13

# String Concatenation
print("\nString Concatenation")
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Concatenated String:", full_greeting)  # Output: Hello, Alice!

# String Repetition
print("\nString Repetition")
repeat_str = "Python! " * 3
print("Repeated String:", repeat_str)  # Output: Python! Python! Python! 

# String Slicing
print("\nString Slicing")
sub_str = str1[7:12]
print("Sliced String (7:12):", sub_str)  # Output: World

# String Methods
print("\nString Methods")
print("Uppercase:", str1.upper())  # Output: HELLO, WORLD!
print("Lowercase:", str1.lower())  # Output: hello, world!
print("Title Case:", str2.title())  # Output: Python Is Awesome
print("Replaced String:", str1.replace("World", "Python"))  # Output: Hello, Python!
print("Stripped String:", "   Hello   ".strip())  # Output: Hello

# String Formatting
print("\nString Formatting")
age = 25
formatted_str = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_str)  # Output: My name is Alice and I am 25 years old.

# Checking Substrings
print("\nChecking Substrings")
print("Python in str2:", "Python" in str2)  # Output: True
print("Java in str2:", "Java" in str2)  # Output: False

# Splitting and Joining Strings
print("\nSplitting and Joining Strings")
words = str2.split(" ")
print("Split String:", words)  # Output: ['Python', 'is', 'awesome']
joined_str = "-".join(words)
print("Joined String:", joined_str)  # Output: Python-is-awesome

# Advantages of Strings:
# 1. Easy manipulation and formatting.
# 2. Supports various methods for transformation and analysis.
# 3. Efficient for storing textual data.

# Disadvantages of Strings:
# 1. Immutable, so modifications create new strings.
# 2. Memory-intensive if heavily modified.

# Tips for Using Strings:
# 1. Use f-strings for clean and efficient formatting (Python 3.6+).
# 2. Prefer using built-in methods for transformations.
# 3. Be mindful of immutability when performing repetitive operations.
