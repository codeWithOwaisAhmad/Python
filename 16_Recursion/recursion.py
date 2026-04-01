"""
Recursion in Python
-----------------
Recursion is when a function calls itself to solve smaller instances of the same problem.
It is an essential concept for algorithms (like trees, graphs, and sorting).

Topics Covered:
1. Base Cases and Recursive Cases
2. Factorial and Fibonacci Sequences
3. The Recursion Limit
4. Recursion vs Iteration (Interview Question)
"""

def basic_recursion() -> int:
    """A minimal recursive function with base limit."""
    print("--- 1. Basic Recursion Structure ---")
    
    # Needs a base case to stop infinite loops
    def countdown(n: int) -> None:
        print(n)
        if n <= 1: # Base Case
            print("🚀 Liftoff!")
        else:      # Recursive Case
            countdown(n - 1)
            
    print("Starting countdown from 3:")
    countdown(3)
    return 3

def factorial(n: int) -> int:
    """Computes factorial: 5! = 5 * 4 * 3 * 2 * 1."""
    if n == 0 or n == 1:
        return 1
    
    # 5 * factorial(4) --> 5 * 4 * factorial(3) ...
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """Computes the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def recursion_limit() -> None:
    """Python has a default recursion limit to prevent Stack Overflow."""
    print("\n--- 3. System Recursion Limit ---")
    
    import sys
    limit = sys.getrecursionlimit()
    print(f"Default Python Recursion Limit: {limit} frames")
    
    print("\nWarning: If a function recurses >1000 times without hitting the base case,")
    print("it will raise a 'RecursionError'. You can manually raise the limit, but it's dangerous.")
    # sys.setrecursionlimit(2000) # How to change it

def interview_prep_gotchas() -> None:
    """Questions comparing recursion vs iteration."""
    print("\n--- 4. Interview Prep & Gotchas (Recursion vs Iteration) ---")
    
    print("Question 1: Recursion is elegant, why not use it everywhere?")
    print("  Answer: Because of Time & Space Complexity overhead.")
    print("  1) Memory: Each recursive call adds a frame to the Call Stack (O(N) space). Iteration uses O(1) space.")
    print("  2) Speed: Repeatedly evaluating the same function calls (like in Fibonacci) creates exponential O(2^N) time.")
    
    print("\nQuestion 2: How do you fix the Fibonacci time complexity issue?")
    print("  Answer: Memoization (Caching previously calculated results).")
    print("  In Python, you can simply use the `@functools.lru_cache` decorator!")

if __name__ == "__main__":
    print("🌟 Python Recursion 🌟")
    basic_recursion()
    
    print("\n--- 2. Classic Recursion Examples ---")
    fact_num = 5
    print(f"Factorial of {fact_num}: {factorial(fact_num)} (5 * 4 * 3 * 2 * 1) ")
    
    fib_index = 6
    print(f"Fibonacci number at index {fib_index}: {fibonacci(fib_index)} (0, 1, 1, 2, 3, 5, *8*) ")
    
    recursion_limit()
    interview_prep_gotchas()
