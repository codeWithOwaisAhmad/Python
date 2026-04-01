"""
Lists in Python
-------------
Lists are mutable, ordered sequences in Python. They are versatile and widely used.

Topics Covered:
1. List Creation and Accessing Elements
2. List Mutability (Change, Add, Remove)
3. List Comprehensions (Advanced & Pythonic)
4. Interview Prep (Copy vs Deepcopy, List Methods)
"""

def basic_lists() -> None:
    """Lists are defined with square brackets [] and can hold mixed types."""
    print("--- 1. List Creation & Access ---")
    
    mixed_list = [10, "Hello", 3.14, True]
    print(f"List: {mixed_list}")
    
    # Accessing via Index
    print(f"First item (Index 0): {mixed_list[0]}")
    print(f"Last item (Index -1): {mixed_list[-1]}")
    
    # Slicing
    nums = [0, 1, 2, 3, 4, 5]
    print(f"\nNumbers: {nums}")
    print(f"nums[1:4]: {nums[1:4]} (Elements at index 1, 2, 3)")
    print(f"Reverse (nums[::-1]): {nums[::-1]}")

def modifying_lists() -> None:
    """Methods used to mutate a list in place."""
    print("\n--- 2. List Modification ---")
    
    cities = ["New York", "London", "Tokyo"]
    print(f"Original: {cities}")
    
    # Changing values
    cities[1] = "Paris" 
    print(f"cities[1] = 'Paris': {cities}")
    
    # Adding items
    cities.append("Berlin") # Adds to end
    print(f"append('Berlin'): {cities}")
    
    cities.insert(0, "Sydney") # Inserts at index
    print(f"insert(0, 'Sydney'): {cities}")
    
    more_cities = ["Cairo", "Mumbai"]
    cities.extend(more_cities) # Adds another list
    print(f"extend(another_list): {cities}")
    
    # Removing items
    popped = cities.pop() # Removes last item and returns it
    print(f"\npop(): removed '{popped}', list is now: {cities}")
    
    cities.remove("Paris") # Removes first occurrence of value
    print(f"remove('Paris'): {cities}")

def list_comprehensions() -> None:
    """A highly Pythonic way to build lists based on existing lists/iterables."""
    print("\n--- 3. List Comprehensions (Very Common Interview Question) ---")
    
    # Syntax: [expression for item in iterable if condition]
    
    # Example 1: Squares of numbers 1 to 5
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")
    
    # Example 2: Filtering even numbers
    evens = [x for x in range(1, 11) if x % 2 == 0]
    print(f"Even numbers 1-10: {evens}")

def interview_prep_gotchas() -> None:
    """Important concepts commonly tested in Python interviews."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    import copy
    
    print("Gotcha 1: Pass by Reference vs Value (Shallow Copy)")
    list_a = [1, 2, 3]
    # BAD: This doesn't copy the list, it just creates a second name for it!
    list_b = list_a
    list_b[0] = 99
    
    # Because list_b and list_a point to the SAME list in memory, modifying one modifies both.
    print(f"Modified list_b... but look at list_a: {list_a} (It changed!)")
    
    print("\nCorrect Ways to Copy:")
    # Using slice
    list_c = list_a[:]
    # Using list() constructor
    list_d = list(list_a)
    # Using .copy() method
    list_e = list_a.copy()
    
    print("Gotcha 2: Understanding Deep Copy")
    # Shallow copies (.copy(), [:], list()) fail on nested lists/objects!
    nested_list = [[1, 2], [3, 4]]
    shallow = nested_list.copy()
    
    shallow[0][0] = 'HACKED'
    print(f"Nested List original after modifying shallow copy: {nested_list}")
    print("-> Nested items share memory in shallow copies!")
    
    # To fix this, use deepcopy
    nested2 = [[1, 2], [3, 4]]
    deep = copy.deepcopy(nested2)
    deep[0][0] = 'SAFE'
    print(f"\nDeepcopy protects nested structures. Original: {nested2}, Copied: {deep}")

if __name__ == "__main__":
    print("🌟 Lists 🌟")
    basic_lists()
    modifying_lists()
    list_comprehensions()
    interview_prep_gotchas()
