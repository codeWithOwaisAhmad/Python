"""
Conditionals (If-Else) in Python
------------------------------
Decision-making in Python relies on the `if`, `elif`, and `else` statements.

Topics Covered:
1. Basic If-Elif-Else structures
2. Nested Conditionals
3. The Ternary Operator (One-line If-Else)
4. Advanced Patterns (Match-Case) -> Python 3.10+
"""

def basic_conditionals() -> None:
    """Standard if/elif/else blocks."""
    print("--- 1. Basic If-Else ---")
    
    age: int = 20
    print(f"Age: {age}")
    
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")

def nested_conditionals() -> None:
    """Conditionals inside conditionals."""
    print("\n--- 2. Nested Conditionals ---")
    
    score = 85
    is_present = True
    
    if is_present:
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        else:
            print("Grade: C or Below")
    else:
        print("Grade: F (Absent)")

def ternary_operator() -> None:
    """A pythonic way to write simple if-else on a single line."""
    print("\n--- 3. Ternary Operator (Interview Favorite) ---")
    
    # Standard way
    is_raining = True
    if is_raining:
        action = "Take an umbrella"
    else:
        action = "Wear sunglasses"
        
    # Ternary way (Pythonic!)
    # Syntax: value_if_true if condition else value_if_false
    pythonic_action = "Take an umbrella" if is_raining else "Wear sunglasses"
    
    print(f"Standard Action: {action}")
    print(f"Ternary Action: {pythonic_action}")

def match_case_modern_python() -> None:
    """Introduced in Python 3.10, Structural Pattern Matching (Switch-Case)."""
    print("\n--- 4. Pattern Matching (Python 3.10+ Only) ---")
    
    # Simulating a server status code response
    status: int = 404
    
    print(f"Evaluating status code {status} using match-case:")
    match status:
        case 200 | 201:
            print("Success!")
        case 400:
            print("Bad Request.")
        case 404:
            print("Not Found.")
        case 500:
            print("Internal Server Error.")
        case _: # The underscore is the default case (similar to 'else')
            print("Unknown status.")

def interview_prep_gotchas() -> None:
    """Common gotchas regarding conditionals."""
    print("\n--- 5. Interview Prep & Gotchas ---")
    
    # Gotcha: Evaluating Lists/Strings directly
    # Empty sequences ([], "", (), {}) evaluate to False
    my_list: list = []
    
    # BAD PRACTICE:
    if len(my_list) == 0:
        pass
        
    # GOOD / PYTHONIC PRACTICE:
    print("Pythonic Truthiness Check:")
    if not my_list:
        print("The list is empty (evaluated as falsy)!")

if __name__ == "__main__":
    print("🌟 Conditionals 🌟")
    basic_conditionals()
    nested_conditionals()
    ternary_operator()
    
    import sys
    # Only run match-case if Python version is >= 3.10
    if sys.version_info >= (3, 10):
        match_case_modern_python()
    else:
        print("\n--- 4. Pattern Matching Skipped (Requires Python 3.10+) ---")
        
    interview_prep_gotchas()
