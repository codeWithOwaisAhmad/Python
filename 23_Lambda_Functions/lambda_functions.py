"""
Lambda Functions in Python
------------------------
A lambda function is a small, anonymous function defined without a name.
It can take any number of arguments, but can only have ONE expression.

Syntax: lambda arguments : expression

Topics Covered:
1. Basic Syntax
2. Using Lambda with map(), filter(), and sorted()
3. Why and when to avoid Lambdas (PEP 8 Gotcha)
"""

def basic_lambda() -> None:
    """Comparing standard functions vs Lambdas."""
    print("--- 1. Basic Syntax ---")
    
    # Standard function
    def add(x, y):
        return x + y
        
    # Lambda Equivalent (Anonymous function)
    add_lambda = lambda x, y: x + y
    
    print(f"Standard Function add(2,3): {add(2, 3)}")
    print(f"Lambda Equivalent(2,3): {add_lambda(2, 3)}")

def higher_order_functions() -> None:
    """Lambdas shine when passed as arguments to other functions."""
    print("\n--- 2. Map, Filter, Sorted ---")
    
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original list: {numbers}")
    
    # 1. filter() - Extracts elements that return 'True' from the function
    # Extract even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"\nfilter() (Evens): {evens}")
    
    # 2. map() - Applies a function to ALL elements
    # Square all numbers
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"map() (Squares): {squares}")
    
    # 3. sorted() - Custom sorting logic
    words = ["banana", "apple", "cherry", "blueberry"]
    # Sort by the LENGTH of the string, not alphabetically
    sorted_words = sorted(words, key=lambda word: len(word))
    print(f"sorted() by length: {sorted_words}")

def interview_prep_gotchas() -> None:
    print("\n--- 3. Interview Prep & Gotchas (PEP 8) ---")
    
    print("Question: Are Lambdas always the best choice?")
    print("Answer: No. In fact, PEP 8 explicitly warns AGAINST assigning ")
    print("lambdas directly to variables (e.g. `f = lambda x: x*2`). ")
    print("If you need a name, define a proper function with `def f(x): return x*2`. ")
    """
    Why?
    - `def` is better for tracebacks and debugging (assigns a __name__).
    - `def` is more readable.

    Lambdas are strictly designed to be passing Anonymous single-use arguments 
    (like the sorting key in our previous example).
    
    However, list comprehensions are often preferred over map/filter:
    - Lists Comp: [x**2 for x in nums] (Readability winner!)
    - Map: list(map(lambda x: x**2, nums))
    """
    
    # Sorting a List of Dictionaries
    print("\nClassic Custom Sort Problem:")
    users = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 95},
        {"name": "Charlie", "score": 70}
    ]
    # We want to sort the list of dictionaries by 'score', highest to lowest
    sorted_users = sorted(users, key=lambda u: u["score"], reverse=True)
    
    for u in sorted_users:
        print(f" - {u['name']} (Score: {u['score']})")

if __name__ == "__main__":
    print("🌟 Lambda Functions (Anonymous Functions) 🌟")
    basic_lambda()
    higher_order_functions()
    interview_prep_gotchas()
