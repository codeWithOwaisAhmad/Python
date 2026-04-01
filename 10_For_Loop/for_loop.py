"""
For Loops in Python
-----------------
A `for` loop in Python iterates over a sequence (list, tuple, dictionary, set, or string).
Unlike C-style loops governed by counter increments, Python's for loop is actually a 'foreach' loop.

Topics Covered:
1. Iterating Sequences
2. The range() Function
3. Enumerate and Zip (Pythonic Techniques)
4. List Comprehensions (Advanced & Essential)
"""

def iterating_sequences() -> None:
    """Iterating over Lists, Strings, and Dictionaries."""
    print("--- 1. Iterating over Sequences ---")
    
    fruits = ["Apple", "Banana", "Cherry"]
    print("List Iteration:")
    for fruit in fruits:
        print(f" - {fruit}")
        
    print("\nString Iteration:")
    for char in "Python":
        print(char, end=" ")
    print() # Newline
    
    print("\nDictionary Iteration:")
    person = {"name": "Alice", "role": "Dev"}
    for key, value in person.items():
        print(f"Key: {key} -> Value: {value}")

def using_range() -> None:
    """Using the range() function to generate numbers."""
    print("\n--- 2. The range() Function ---")
    
    # range(stop) - 0 to stop-1
    print("range(3):", list(range(3)))
    
    # range(start, stop)
    print("range(5, 8):", list(range(5, 8)))
    
    # range(start, stop, step) -> Excellent for skipping numbers or reversing
    print("range(10, 0, -2) (Reverse):", list(range(10, 0, -2)))

def pythonic_loops() -> None:
    """Using enumerate() and zip() over traditional counters."""
    print("\n--- 3. Pythonic Iteration (Enumerate & Zip) ---")
    
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    
    # BAD PRACTICE (C-style):
    # for i in range(len(names)):
    #     print(i, names[i])
        
    # GOOD (Pythonic) - Enumerate gets both index and value!
    print("Enumerate:")
    for index, name in enumerate(names, start=1):
        print(f"Rank {index}: {name}")
        
    # VERY GOOD (Pythonic) - Zip iterates multiple lists simultaneously
    print("\nZip:")
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

def list_comprehensions() -> None:
    """Creating lists from loops cleanly and efficiently."""
    print("\n--- 4. List Comprehensions (Interview Must-Know) ---")
    
    # Goal: Create a list of squares for even numbers 1 to 5.
    
    # Standard Loop Way:
    squares = []
    for x in range(1, 6):
        if x % 2 == 0:
            squares.append(x**2)
    print(f"Standard Loop Result: {squares}")
    
    # Comprehension Way: [expression for item in iterable if condition]
    comp_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
    print(f"List Comprehension Result: {comp_squares} (Notice it's just 1 line!)")

if __name__ == "__main__":
    print("🌟 For Loops 🌟")
    iterating_sequences()
    using_range()
    pythonic_loops()
    list_comprehensions()
