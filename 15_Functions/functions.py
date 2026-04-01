"""
Functions in Python
-----------------
Functions are reusable blocks of code that perform specific tasks.
They help keep code DRY (Don't Repeat Yourself), modular, and testable.

Topics Covered:
1. Defining and Calling functions
2. Parameters and Return Values
3. Default Args, *args, and **kwargs
4. Variable Scope (Local vs Global)
5. Interview Prep (First-Class Objects)
"""

# Type hints are a modern Python feature to explicitly state expected variable types
def basic_function(name: str) -> None:
    """1. Basic Function: Prints a greeting."""
    print(f"Hello, {name}!")

def default_parameters(name: str = "Guest", retries: int = 3) -> str:
    """2. Default Parameters: If an argument is missing, the default is used."""
    return f"Welcome {name}! You have {retries} retries left."

def flexible_args(*args, **kwargs) -> None:
    """
    3. *args and **kwargs (Interview Favorite)
    - *args: Captures positional arguments into a Tuple.
    - **kwargs: Captures keyword arguments into a Dictionary.
    """
    print("\n--- Flexible Arguments (*args and **kwargs) ---")
    print(f"args Tuple (Positional): {args}")
    for item in args:
        print(f" - Arg: {item}")
        
    print(f"\nkwargs Dictionary (Keyword): {kwargs}")
    for key, value in kwargs.items():
        print(f" - Kwarg '{key}': {value}")

def multiple_return_values() -> tuple:
    """4. In Python, you can easily return multiple values as a tuple."""
    return 200, "OK", {"data": [1, 2, 3]}

def interview_prep_gotchas() -> None:
    """Commonly tested concepts revolving around functions."""
    print("\n--- 5. Interview Prep & Gotchas ---")
    
    print("Gotcha 1: Functions are First-Class Objects in Python.")
    print("This means you can assign a function to a variable or pass it to another function!")
    
    # Assigning Function to Variable
    greet_alias = basic_function 
    greet_alias("Alice (via Alias variable)")
    
    print("\nGotcha 2: The Mutable Default Argument Trap. NEVER DO THIS:")
    print("  def bad_function(item, my_list=[]):")
    print("      my_list.append(item)")
    print("      return my_list")
    
    print("Why? Because the default list is created ONLY ONCE when function is defined.")
    print("If you call it multiple times, it shares the SAME list and values pile up!")
    
    print("\nCorrect Pattern for mutable defaults:")
    print("  def good_function(item, my_list=None):")
    print("      if my_list is None:")
    print("          my_list = []")
    print("      my_list.append(item)")
    print("      return my_list")

if __name__ == "__main__":
    print("🌟 Python Functions 🌟")
    print("\n--- 1. Basic Functions ---")
    basic_function("Developer")
    
    print("\n--- 2. Default Parameters ---")
    print(default_parameters())
    print(default_parameters("Admin", 5))
    
    flexible_args("apple", 10, True, user="Jane", admin=False)
    
    print("\n--- 4. Multiple Return Values ---")
    status_code, status_msg, response = multiple_return_values()
    print(f"Status: {status_code} ({status_msg}) | Payload: {response}")
    
    interview_prep_gotchas()
