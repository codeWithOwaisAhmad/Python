"""
Variables in Python - A Comprehensive Guide
-----------------------------------------
This module covers the basics and advanced concepts of variables in Python.
Python is dynamically typed, meaning you don't need to declare variable types explicitly.

Topics Covered:
1. Variable Creation and Assignment
2. Naming Conventions (PEP 8)
3. Multiple Assignment
4. Global and Local Scope
5. Type Hinting (Modern Python)
6. Interview Questions & Gotchas
"""

from typing import List, Dict, Any

def basics_of_variables() -> None:
    """Demonstrates basic variable assignment and naming conventions."""
    print("--- 1. Variable Assignment ---")
    
    # Simple assignment
    age: int = 25  # Type hinting (optional but recommended!)
    name: str = "Alice"
    is_developer: bool = True
    salary: float = 85000.50
    
    print(f"Name: {name}, Age: {age}, Developer: {is_developer}, Salary: {salary}")

def multiple_assignment() -> None:
    """Demonstrates how to assign multiple variables elegantly."""
    print("\n--- 2. Multiple Assignment ---")
    
    # Assigning multiple values to multiple variables
    x, y, z = 10, 20, 30
    print(f"x: {x}, y: {y}, z: {z}")
    
    # Assigning the same value to multiple variables
    a = b = c = 100
    print(f"a: {a}, b: {b}, c: {c}")

    # Swapping variables without a temporary variable! (Common Interview Question)
    x, y = y, x
    print(f"After swap -> x: {x}, y: {y}")

# Global variable
global_counter: int = 0

def scope_demonstration() -> None:
    """Demonstrates variable scope (Local vs Global)."""
    print("\n--- 3. Variable Scope ---")
    
    # Local variable
    local_counter: int = 5
    
    # To modify a global variable inside a function, use the 'global' keyword
    global global_counter
    global_counter += 1
    
    print(f"Local counter: {local_counter}")
    print(f"Global counter modified inside function: {global_counter}")

def interview_prep_gotchas() -> None:
    """Common gotchas and interview questions regarding variables."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    # Gotcha 1: Mutable default arguments. NEVER DO THIS in production.
    # def bad_func(item, my_list=[]): ...
    
    # Gotcha 2: Python caches small integers (-5 to 256) (Is vs ==)
    a = 256
    b = 256
    print(f"a is b (up to 256)? {a is b}")  # True
    
    c = 257
    d = 257
    print(f"c is d (above 256)? {c is d}")  # Mostly False (depends on REPL execution vs Script execution)
    
    # Gotcha 3: Deleting a variable
    temp_var = "I will be deleted"
    del temp_var
    try:
        print(temp_var)
    except NameError as e:
        print(f"Expected Error: {e}")

if __name__ == "__main__":
    print("🌟 Variables 🌟")
    basics_of_variables()
    multiple_assignment()
    scope_demonstration()
    interview_prep_gotchas()
