"""
Strings in Python
-----------------
Strings in Python are immutable sequences of Unicode characters.

Topics Covered:
1. String Creation (Single, Double, Triple quotes)
2. Slicing & Indexing
3. String Formatting (f-strings vs .format)
4. Immutability
5. Interview Questions & Gotchas
"""

def string_basics() -> None:
    """Demonstrates creating and accessing strings."""
    print("--- 1. String Basics & Indexing ---")
    
    # Multiline strings using triple quotes
    multiline = '''This is a
multiline string
in Python.'''
    
    text: str = "Hello Python"
    
    # Indexing (0-based)
    print(f"Text: '{text}'")
    print(f"First character: {text[0]}")
    print(f"Last character: {text[-1]} (-1 accesses from the end)")

def string_slicing() -> None:
    """Demonstrates slicing [start:stop:step]."""
    print("\n--- 2. String Slicing ---")
    
    text: str = "Programming"
    print(f"Full text: {text}")
    print(f"text[0:4]: {text[0:4]} (Extracts indices 0,1,2,3)")
    print(f"text[3:]: {text[3:]} (From index 3 to the end)")
    print(f"text[:4]: {text[:4]} (From start to index 3)")
    
    # The trick to reverse a string in Python!
    print(f"text[::-1]: {text[::-1]} (Reverses the string perfectly)")

def string_formatting() -> None:
    """Demonstrates modern f-strings vs historical methods."""
    print("\n--- 3. String Formatting ---")
    
    name, age = "Developer", 30
    
    # Modern Way (Python 3.6+) - F-Strings! Fast and readable.
    print(f"f-string: My name is {name} and I am {age} years old.")
    
    # Older Way (Python 3.0)
    print("format(): My name is {} and I am {} years old.".format(name, age))

def interview_prep_gotchas() -> None:
    """Common gotchas and interview questions regarding Strings."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    # Gotcha 1: Strings are Immutable
    text = "Car"
    try:
        text[0] = "B" # Trying to change 'C' to 'B' to make 'Bar'
    except TypeError as e:
        print(f"Why Strings are Immutable: {e}")
    # Workaround: You must create a new string
    new_text = "B" + text[1:]
    print(f"Workaround for immutability: {new_text}")
    
    # Gotcha 2: String Interning
    # Python optimizes small strings by reusing their memory ID.
    str1 = "hello"
    str2 = "hello"
    print(f"Is 'hello' identically stored in memory? {str1 is str2}")
    
    str3 = "hello world!"
    str4 = "hello world!"
    print(f"Are complex strings always internally same? {str3 is str4} (Compiler depending)")

if __name__ == "__main__":
    print("🌟 Python Strings 🌟")
    string_basics()
    string_slicing()
    string_formatting()
    interview_prep_gotchas()
