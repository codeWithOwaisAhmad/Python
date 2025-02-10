"""
Regular expressions (often abbreviated as regex or regexp) are sequences of characters that define search patterns. 
These patterns are used to match strings or parts of strings. Regular expressions are incredibly powerful for text 
processing tasks, such as searching, matching, and replacing text.
"""

# Importing the re module
import re

# Basic Functions in the re Module

# 1. re.match(): This function tries to match a pattern at the beginning of a string.
pattern = r'hello'
string = 'hello world'

match = re.match(pattern, string)

if match:
    print("Match found!")
else:
    print("No match.")

# 2. re.search(): This function searches the entire string for a match.
pattern = r'world'
string = 'hello world'

search = re.search(pattern, string)

if search:
    print("Match found!")
else:
    print("No match.")

# 3. re.findall(): This function returns a list of all non-overlapping matches in the string.
pattern = r'\d+'
string = 'There are 123 apples and 456 oranges.'

matches = re.findall(pattern, string)
print(matches)  # Output: ['123', '456']

# 4. re.finditer(): This function returns an iterator yielding match objects for all non-overlapping matches.
pattern = r'\d+'
string = 'There are 123 apples and 456 oranges.'

matches = re.finditer(pattern, string)

for match in matches:
    print(match.group())  # Output: 123 then 456

# 5. re.sub(): This function replaces occurrences of the pattern with a replacement string.
pattern = r'apples'
replacement = 'bananas'
string = 'I like apples.'

new_string = re.sub(pattern, replacement, string)
print(new_string)  # Output: I like bananas.

"""
Metacharacters:
Regular expressions use special characters (metacharacters) to define patterns:
- . : Matches any character except a newline.
- ^ : Matches the beginning of the string.
- $ : Matches the end of the string.
- * : Matches 0 or more repetitions of the preceding pattern.
- + : Matches 1 or more repetitions of the preceding pattern.
- ? : Matches 0 or 1 repetition of the preceding pattern.
- {m,n} : Matches between m and n repetitions of the preceding pattern.
- [] : Matches any single character within the brackets.
- | : Acts as an OR operator.
- () : Groups patterns.
"""

# Example Using Metacharacters
pattern = r'\b\w{5}\b'
string = 'Hello world, this is a regex example.'

matches = re.findall(pattern, string)
print(matches)  # Output: ['Hello', 'world']

"""
Escaping Metacharacters:
If you want to match a metacharacter literally, you need to escape it with a backslash (\).
"""

pattern = r'\$100'
string = 'The price is $100.'

search = re.search(pattern, string)

if search:
    print("Match found!")
else:
    print("No match.")