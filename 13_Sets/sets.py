"""
Sets in Python
-------------
Sets are unordered collections of UNIQUE elements. 
They are highly optimized for fast membership testing (in / not in)
and removing duplicates from sequences.

Topics Covered:
1. Creating Sets (Curly braces vs set() constructor)
2. Adding and Removing Elements
3. Mathematical Set Operations (Union, Intersection, Difference)
4. Interview Prep (Hashability and Time Complexity)
"""

def basic_sets() -> None:
    """Creating and modifying sets."""
    print("--- 1. Set Creation and Modification ---")
    
    fruits = {"apple", "banana", "cherry"}
    print(f"Set: {fruits}")
    
    # Adding
    fruits.add("orange")
    print(f"fruits.add('orange'): {fruits}")
    
    # Trying to add duplicate - gets ignored!
    fruits.add("apple")
    print(f"Added 'apple' again, Set is still: {fruits} (Duplicates ignored!)")
    
    # Removing (remove vs discard)
    fruits.remove("banana") # Raises KeyError if not found
    print(f"remove('banana'): {fruits}")
    
    fruits.discard("watermelon") # Safe, does nothing if not found
    print("discard('watermelon') did nothing gracefully.")

def mathematical_operations() -> None:
    """Set Theory operations (Union, Intersection, etc.)."""
    print("\n--- 2. Set Operations ---")
    
    set_a = {"ironman", "batman", "superman"}
    set_b = {"batman", "wonderwoman", "spiderman"}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # Union (Everything in both sets)
    print(f"\nUnion (A | B): {set_a | set_b}")
    print(f"Alternative (A.union(B)): {set_a.union(set_b)}")
    
    # Intersection (Only what is in BOTH sets)
    print(f"Intersection (A & B): {set_a & set_b}")
    
    # Difference (What is in A but NOT in B)
    print(f"Difference (A - B): {set_a - set_b}")
    
    # Symmetric Difference (In A or B, but NOT both)
    print(f"Symmetric Diff (A ^ B): {set_a ^ set_b}")

def interview_prep_gotchas() -> None:
    """Key interview concepts regarding Sets."""
    print("\n--- 3. Interview Prep & Gotchas ---")
    
    # Empty Set Creation Gotcha
    empty_curly = {}
    print("Gotcha 1: Creating an empty set")
    print(f"  What is type({{}})? Answer: {type(empty_curly).__name__} (It's a Dictionary!)")
    
    empty_set = set() # This is the ONLY way to create an empty set
    print(f"  Type of set(): {type(empty_set).__name__}")
    
    # Set Operations Time Complexity
    print("\nQuestion 2: Time Complexity")
    print("  Checking if an item is in a list: O(N) Time (Linear Search)")
    print("  Checking if an item is in a set: O(1) Time (Hash Table Lookup) - VERY FAST")
    
    # Removing Duplicates from a List
    print("\nClassic Interview Question: 'Remove duplicates from this list efficiently'")
    dirty_list = [1, 2, 2, 3, 3, 3, 4]
    clean_list = list(set(dirty_list))
    print(f"  List: {dirty_list}")
    print(f"  Clean: list(set(dirty_list)) -> {clean_list}")
    
    # Hashability Requirement
    # print( { [1, 2] } ) # Error! Sets cannot contain mutable objects (like lists or dictionaries)!

if __name__ == "__main__":
    print("🌟 Python Sets 🌟")
    basic_sets()
    mathematical_operations()
    interview_prep_gotchas()
