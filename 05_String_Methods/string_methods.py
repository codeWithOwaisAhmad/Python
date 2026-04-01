"""
String Methods in Python
----------------------
Because strings are objects, they come with a rich set of built-in methods.
Note: Since strings are immutable, ALL string methods return a *new* string 
and do not alter the original string.

Topics Covered:
1. Modification (Upper, Lower, Title, Replace)
2. Whitespace Management (Strip, Lstrip, Rstrip)
3. Validation (Isalpha, Isnumeric, Islower)
4. Searching & Splitting (Find, Split, Join)
"""

def text_modification() -> None:
    """Methods that modify the case or content."""
    print("--- 1. Case & Content Modification ---")
    
    text: str = "  hello WORLD!  "
    print(f"Original: '{text}'")
    
    # Upper, Lower, Title
    print(f"upper(): '{text.upper()}'")
    print(f"lower(): '{text.lower()}'")
    print(f"title(): '{text.title()}'")
    
    # Replace
    course = "I like Java"
    print(f"\nreplace(): {course.replace('Java', 'Python')}")

def whitespace_management() -> None:
    """Methods used to clean up messy inputs (crucial for web forms/inputs)."""
    print("\n--- 2. Whitespace Management ---")
    
    dirty_string: str = "   Python   "
    print(f"Original String: '{dirty_string}'")
    
    print(f"lstrip() (Left strip): '{dirty_string.lstrip()}'")
    print(f"rstrip() (Right strip): '{dirty_string.rstrip()}'")
    print(f"strip() (Both sides): '{dirty_string.strip()}'") # MOST COMMON

def splitting_and_joining() -> None:
    """Converting between Lists and Strings."""
    print("\n--- 3. Split & Join (Interview Favorites) ---")
    
    csv_data = "apple,banana,cherry"
    print(f"Original CSV: {csv_data}")
    
    # Splitting turns a string into a List based on a delimiter
    fruit_list = csv_data.split(",")
    print(f"split(','): {fruit_list}")
    
    # Joining turns an iterable (like List) back into a single string
    hashtag_separator = " # "
    joined_text = hashtag_separator.join(fruit_list)
    print(f"join(): {joined_text}")

def validations_and_searching() -> None:
    """Boolean checks and substring searching."""
    print("\n--- 4. Validation & Searching ---")
    
    password = "123password"
    print(f"Is '{password}' alphanumeric? {password.isalnum()}")
    print(f"Is '{password}' only numbers? {password.isnumeric()}")
    
    sentence = "The quick brown fox jumps"
    # Searching
    print(f"\nFind 'fox' index: {sentence.find('fox')} (Returns -1 if not found)")
    print(f"Starts with 'The': {sentence.startswith('The')}")
    print(f"Ends with 'dog': {sentence.endswith('dog')}")

def interview_prep_gotchas() -> None:
    """Gotchas commonly asked in interviews."""
    print("\n--- 5. Interview Prep & Gotchas ---")
    
    # Difference between find() and index()
    text = "Hello"
    print("index() vs find(): They do the same thing, EXCEPT when the substring is missing.")
    print("find('z'):", text.find('z')) # Returns -1 safely
    try:
        text.index('z') # Raises a ValueError
    except ValueError:
        print("index('z') raises a ValueError! Use find() for safer checks.")

if __name__ == "__main__":
    print("🌟 Python String Methods 🌟")
    text_modification()
    whitespace_management()
    splitting_and_joining()
    validations_and_searching()
    interview_prep_gotchas()
