# Python Regular Expressions Explained for Beginners (Detailed Version)

# What are Regular Expressions (RegEx)?
# Regular expressions are sequences of characters that define search patterns.
# They are used for pattern matching, searching, and text manipulation.
# In Python, the 're' module provides support for working with regular expressions.

# Why Use Regular Expressions?
# Regular expressions are useful for tasks such as:
# - Validating input (e.g., email addresses, phone numbers)
# - Searching and extracting information from text
# - Replacing or splitting text based on patterns

# Importing the 're' Module
import re

# Example 1: Basic Pattern Matching
print("\nExample 1: Basic Pattern Matching")
text = "Hello, welcome to the world of Python!"
pattern = r"Python"

# Using re.search() to find the pattern in the text
match = re.search(pattern, text)
if match:
    print("Pattern found at position:", match.start())  # Output: Position of 'Python'
else:
    print("Pattern not found")

# Example 2: Using Special Characters
print("\nExample 2: Using Special Characters")
text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"

# Using re.findall() to extract phone numbers
phone_numbers = re.findall(pattern, text)
print("Phone numbers found:", phone_numbers)  # Output: ['123-456-7890']

# Example 3: Matching Multiple Patterns
print("\nExample 3: Matching Multiple Patterns")
text = "cat, bat, rat, mat"
pattern = r"[cm]at"

matches = re.findall(pattern, text)
print("Words matching the pattern:", matches)  # Output: ['cat', 'mat']

# Example 4: Replacing Text Using re.sub()
print("\nExample 4: Replacing Text")
text = "I love coding in Python. Python is awesome!"
pattern = r"Python"

# Replace 'Python' with 'Programming'
new_text = re.sub(pattern, "Programming", text)
print("Modified text:", new_text)  # Output: 'I love coding in Programming. Programming is awesome!'

# Example 5: Splitting Strings Using re.split()
print("\nExample 5: Splitting Strings")
text = "apple, banana; orange: grape"
pattern = r"[;, :]"

# Split text using multiple delimiters
fruits = re.split(pattern, text)
print("Fruits:", fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Commonly Used Special Characters in Regular Expressions:
# 1. \d - Matches any digit (0-9)
# 2. \w - Matches any alphanumeric character (a-z, A-Z, 0-9, _)
# 3. \s - Matches any whitespace character
# 4. .  - Matches any character except a newline
# 5. ^  - Matches the start of a string
# 6. $  - Matches the end of a string
# 7. *  - Matches zero or more occurrences of the preceding pattern
# 8. +  - Matches one or more occurrences of the preceding pattern
# 9. ?  - Matches zero or one occurrence of the preceding pattern
# 10. {} - Specifies the number of repetitions
# 11. [] - Matches any one of the characters inside the brackets
# 12. |  - Alternation (logical OR)
# 13. () - Groups patterns for capturing

# Advantages of Regular Expressions:
# 1. Efficient for searching and manipulating large amounts of text.
# 2. Powerful for pattern matching and validation.
# 3. Flexible with concise syntax.

# Disadvantages of Regular Expressions:
# 1. Syntax can be complex and hard to read.
# 2. Difficult to debug if patterns are too complicated.
# 3. Can be inefficient if not used properly.

# Tips for Using Regular Expressions:
# 1. Test your patterns on sample data to ensure accuracy.
# 2. Use online tools like regex101 to visualize and test expressions.
# 3. Comment your regex patterns for better readability.

# Regular expressions are a powerful tool for string processing, but it is important to use them wisely and optimize your patterns to avoid performance issues.
