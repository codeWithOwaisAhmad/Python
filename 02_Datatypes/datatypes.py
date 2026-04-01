"""
Data Types in Python
------------------
Python has an extensive set of built-in data types.
Everything in Python is an object, meaning data types are actually classes.

Topics Covered:
1. Primitive Data Types (int, float, str, bool, complex)
2. Sequence Types (list, tuple, range)
3. Set and Mapping Types (set, dict)
4. Finding Data Types and Memory IDs
5. Interview Questions & Gotchas
"""

def primitive_datatypes() -> None:
    """Demonstrates basic primitive built-in data types."""
    print("--- 1. Primitive Data Types ---")
    
    i: int = 42
    f: float = 3.14159
    c: complex = 1 + 2j
    s: str = "Python is Beautiful"
    b: bool = False
    
    print(f"Integer: {i} | Type: {type(i)}")
    print(f"Float: {f} | Type: {type(f)}")
    print(f"Complex: {c} | Type: {type(c)}")
    print(f"String: {s} | Type: {type(s)}")
    print(f"Boolean: {b} | Type: {type(b)}")

def sequence_and_mapping_types() -> None:
    """Demonstrates collections, sequences, and mappings."""
    print("\n--- 2. Sequence & Mapping Types ---")
    
    my_list: list = [1, 2, 3, "apple"]        # Mutable sequence
    my_tuple: tuple = (1, 2, 3, "apple")      # Immutable sequence
    my_range: range = range(10)               # Sequence of numbers
    my_dict: dict = {"key": "value"}          # Key-Value Mapping
    my_set: set = {1, 2, 3, 3, 3}             # Unique unordered items
    
    print(f"List: {my_list} | Mutable? Yes")
    print(f"Tuple: {my_tuple} | Mutable? No (Immutable)")
    print(f"Range: {my_range}")
    print(f"Dictionary: {my_dict}")
    print(f"Set: {my_set} (Notice the duplicates were removed!)")

def interview_prep_gotchas() -> None:
    """Common gotchas and interview questions regarding Data Types."""
    print("\n--- 3. Interview Prep & Gotchas ---")
    
    # Question 1: How does Python handle large integers?
    # Answer: Python 3 handles arbitrarily large integers automatically!
    big_num = 10**100
    print(f"Big Number: 10^100 | Type: {type(big_num)}")
    
    # Question 2: Why floating point math seems 'broken'?
    # It's an IEEE 754 limitation, not a Python bug.
    math_result = 0.1 + 0.2
    print(f"Is 0.1 + 0.2 equal to 0.3? {math_result == 0.3} (Result is {math_result})")
    print("Use the 'decimal' module for precise mathematical calculations.")
    
    # Question 3: Type checking using isinstance() vs type() ==
    # isinstance() is preferred because it accounts for subclassing.
    class Animal: pass
    class Dog(Animal): pass
    x = Dog()
    
    print(f"type(x) == Animal? {type(x) == Animal}") # False
    print(f"isinstance(x, Animal)? {isinstance(x, Animal)}") # True (Best Practice!)

if __name__ == "__main__":
    print("🌟 Built-in Data Types 🌟")
    primitive_datatypes()
    sequence_and_mapping_types()
    interview_prep_gotchas()
