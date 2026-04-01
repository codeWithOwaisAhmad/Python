"""
Type Casting in Python
--------------------
Type casting is the process of converting a variable from one data type to another.

In Python, there are two types of casting:
1. Implicit Casting (done automatically by the Python interpreter)
2. Explicit Casting (done by the developer using constructor functions)

Constructor Functions: int(), float(), str(), list(), tuple(), set()
"""

def implicit_casting() -> None:
    """Python automatically promotes smaller data types to larger ones."""
    print("--- 1. Implicit Type Casting ---")
    
    int_val = 10
    float_val = 5.5
    
    # Python automatically converts int to float to prevent data loss
    result = int_val + float_val
    print(f"{int_val} ({type(int_val).__name__}) + {float_val} ({type(float_val).__name__})")
    print(f"Result: {result} | Final Type: {type(result).__name__}")

def explicit_casting() -> None:
    """Manually converting types using constructor functions."""
    print("\n--- 2. Explicit Type Casting ---")
    
    # String to Int
    str_num = "100"
    num = int(str_num)
    print(f"String '{str_num}' to Int: {num} (Type: {type(num).__name__})")
    
    # Float to Int (WARNING: Drops the decimal part, does NOT round)
    pi = 3.14159
    rounded_pi = int(pi) 
    print(f"Float {pi} to Int: {rounded_pi} (Truncated, not rounded!)")
    
    # Int to String
    age = 25
    age_str = str(age)
    print(f"Int {age} to String: '{age_str}'")

def structural_casting() -> None:
    """Casting between iterables (Lists, Tuples, Sets)."""
    print("\n--- 3. Structural Type Casting ---")
    
    my_list = [1, 2, 2, 3, 4, 4]
    print(f"Original List: {my_list}")
    
    # List to Set (Excellent way to remove duplicates)
    my_set = set(my_list)
    print(f"Cast to Set (Duplicates removed): {my_set}")
    
    # Set to Tuple
    my_tuple = tuple(my_set)
    print(f"Cast Set to Tuple: {my_tuple}")

def interview_prep_gotchas() -> None:
    """Common gotchas and interview questions regarding Type Casting."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    # Gotcha 1: Casting invalid strings
    try:
        invalid_int = int("10.5") # This will fail. You must cast to float first.
    except ValueError as e:
        print(f"ValueError caught: Cannot cast float-string '10.5' directly to int. Error: {e}")
        
    # Gotcha 2: Truthy and Falsy values
    print("\nFalsy Values in Python:")
    print(f"bool(0): {bool(0)}")
    print(f"bool(''): {bool('')} (Empty string)")
    print(f"bool([]): {bool([])} (Empty list)")
    print(f"bool(None): {bool(None)}")
    
    print("\nTruthy Values in Python:")
    print(f"bool(1): {bool(1)}")
    print(f"bool(' '): {bool(' ')} (Space is not empty)")
    print(f"bool([0]): {bool([0])} (List with elements)")

if __name__ == "__main__":
    print("🌟 Type Casting 🌟")
    implicit_casting()
    explicit_casting()
    structural_casting()
    interview_prep_gotchas()
