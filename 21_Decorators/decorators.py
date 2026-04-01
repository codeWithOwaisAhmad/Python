"""
Decorators in Python
------------------
A decorator is a design pattern in Python that allows you to modify or 
enhance the behavior of a function or class without permanently modifying it.

Functions are First-Class Objects:
1. They can be assigned to variables
2. They can be passed into other functions
3. They can be returned from other functions

Decorators rely on these 3 principles!
"""

import time
import functools

# ---------------------------------------------------------
# 1. Understanding the syntax (Without @ sugar)
# ---------------------------------------------------------
def basic_decorator(func):
    """A wrapper function that adds behavior around the target 'func'."""
    def wrapper():
        print("    [Decorator] Something happens BEFORE the function is called.")
        func() # Call the original function
        print("    [Decorator] Something happens AFTER the function is called.")
    return wrapper

def say_hello():
    print("    Hello!")

# This is what decorators actually do under the hood!
# say_hello = basic_decorator(say_hello)

# ---------------------------------------------------------
# 2. Modern Decorators (Using @ syntax)
# ---------------------------------------------------------
def timer_decorator(func):
    """Measures the execution time of any function."""
    
    @functools.wraps(func) # Preserves the original function's name and docstring!
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # Execute the actual function
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        print(f"    [Timer] '{func.__name__}' ran in {end_time - start_time:.4f} secs")
        return result
        
    return wrapper

@timer_decorator
def calculate_squares(n: int) -> list:
    """Takes some time to calculate squares."""
    return [i**2 for i in range(n)]

# ---------------------------------------------------------
# Execution & Interview Gotchas
# ---------------------------------------------------------
def demonstrate_decorators() -> None:
    print("--- 1. Basic Decorator Execution ---")
    
    # Applying the decorator manually
    wrapped_hello = basic_decorator(say_hello)
    wrapped_hello()
    
    print("\n--- 2. Practical Decorator (@ syntax) ---")
    calculate_squares(100000)

def interview_prep_gotchas() -> None:
    print("\n--- 3. Interview Prep & Gotchas ---")
    
    print("Question 1: What does @functools.wraps() do?")
    print("Answer: When you wrap a function, its metadata (name, docstring) gets overwritten ")
    print("by the wrapper function. Using @wraps(func) ensures the original identity is preserved.")
    
    print(f"\nDid our timer preserve identity? calculate_squares.__name__: '{calculate_squares.__name__}'")
    
    print("\nQuestion 2: Can you stack decorators?")
    print("Answer: Yes! They execute from the bottom up (closest to the function first).")
    print("\n@authenticate")
    print("@timer_decorator")
    print("def view_profile(): ...")
    print(" -> Execution: authenticate(timer_decorator(view_profile))")

if __name__ == "__main__":
    print("🌟 Python Decorators 🌟")
    demonstrate_decorators()
    interview_prep_gotchas()
