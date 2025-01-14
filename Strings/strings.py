# tutorial_strings.py

# This tutorial covers the basics of programming with strings in Python.

# Introduction to Strings in Python
# Strings in Python are sequences of characters enclosed in either single quotes (' ') or double quotes (" ").
# They are used to represent text data. Strings are immutable, meaning once created, they cannot be changed.

# Basic String Operations

# 1. Creating Strings
string1 = "Hello, World!"
string2 = 'Python Programming'

# 2. Accessing Characters
# We can access individual characters in a string using indexing.
first_char = string1[0]   # 'H'
last_char = string1[-1]   # '!'

# 3. String Length
# The length of a string can be obtained using the len() function.
length = len(string1)    # 13

# 4. String Concatenation
# We can concatenate (join) strings using the '+' operator.
full_string = string1 + " " + string2

# 5. String Repetition
# We can repeat a string multiple times using the '*' operator.
repeated_string = string1 * 3

# 6. Slicing Strings
# Slicing allows us to get a substring by specifying a start and end index.
sliced_string = string1[0:5]    # 'Hello'

# Easy Example: String Concatenation and Length
def easy_example():
    string1 = "Hello"
    string2 = "World"
    
    # Concatenate strings using the '+' operator
    concatenated = string1 + ", " + string2 + "!"
    print(f"Concatenated String: {concatenated}")
    
    # Get the length of the concatenated string using the len() function
    length = len(concatenated)
    print(f"Length of Concatenated String: {length}")

# Output:
# Concatenated String: Hello, World!
# Length of Concatenated String: 13

# Medium Example: String Slicing and Case Conversion
def medium_example():
    string = "Python Programming is Fun"
    
    # Slice the string to get a part of it using string[start:end] syntax
    sliced_part = string[7:18]
    print(f"Sliced Part: {sliced_part}")
    
    # Convert the entire string to uppercase using the upper() method
    upper_case = string.upper()
    print(f"Uppercase: {upper_case}")
    
    # Convert the entire string to lowercase using the lower() method
    lower_case = string.lower()
    print(f"Lowercase: {lower_case}")

# Output:
# Sliced Part: Programming
# Uppercase: PYTHON PROGRAMMING IS FUN
# Lowercase: python programming is fun

# Hard Example: Palindrome Check
def hard_example():
    def is_palindrome(s):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]

    test_string1 = "A man, a plan, a canal, Panama"
    test_string2 = "Hello, World!"
    
    print(f"Is '{test_string1}' a palindrome? {is_palindrome(test_string1)}")
    print(f"Is '{test_string2}' a palindrome? {is_palindrome(test_string2)}")

# Output:
# Is 'A man, a plan, a canal, Panama' a palindrome? True
# Is 'Hello, World!' a palindrome? False

# Run the examples
if __name__ == "__main__":
    print("Easy Example:")
    easy_example()
    print("\nMedium Example:")
    medium_example()
    print("\nHard Example:")
    hard_example()