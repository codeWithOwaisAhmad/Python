"""
Dictionaries in Python
--------------------
Dictionaries are mutable, unordered (ordered since Python 3.7+),
collections of Key-Value pairs. They are essentially Hash Maps.

Topics Covered:
1. Dictionary Creation and accessing items
2. Adding, Updating, and Removing (pop)
3. Iterating Dictionaries
4. Interview Prep (Dictionary Comprehensions, get() vs [] )
"""

def basic_dictionaries() -> None:
    """Creating and accessing key-value pairs."""
    print("--- 1. Dictionary Creation & Access ---")
    
    # Using curly braces
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(f"Car Dict: {car}")
    
    # Standard Access via key
    print(f"Accessing via key: car['model'] = {car['model']}")
    
    # Access via .get() (Best Practice!)
    print(f"Accessing via get(): car.get('year') = {car.get('year')}")
    
    # Missing Keys:
    # print(car['color']) # Crash! KeyError
    print(f"Missing key via get(): car.get('color') = {car.get('color')} (Safe, returns None)")
    print(f"With Default via get(): car.get('color', 'Red') = {car.get('color', 'Red')}")

def dict_methods() -> None:
    """Updating and removing components of a Dictionary."""
    print("\n--- 2. Modifying Dictionaries ---")
    
    student = {"name": "Alice", "age": 25}
    print(f"Original: {student}")
    
    # Adding & Updating
    student["grade"] = "A" # Adding a new key
    student["age"] = 26    # Updating existing key
    print(f"After Add/Update: {student}")
    
    # Using .update() with another dictionary
    student.update({"school": "MIT", "grade": "A+"})
    print(f"After .update(): {student}")
    
    # Removing specific items
    removed_grade = student.pop("grade")
    print(f"Removed grade ('{removed_grade}') via pop(): {student}")
    
    # Python 3.9+ Merge Operator (|)
    dict_a = {"x": 1, "y": 2}
    dict_b = {"y": 99, "z": 3}
    print(f"\nMerge dict_a {dict_a} | dict_b {dict_b} (Python 3.9+): {dict_a | dict_b}")

def iterating_dictionaries() -> None:
    """Iterating through keys, values, and key-value pairs."""
    print("\n--- 3. Iterating Dictionaries ---")
    
    capitals = {"USA": "Washington", "France": "Paris"}
    
    print("Keys (default):")
    for key in capitals:
        print(f"- {key}")
        
    print("\nValues (.values()):")
    for value in capitals.values():
        print(f"- {value}")
        
    print("\nItems (.items()): (Interview Favorite - Tuple Unpacking in Loop)")
    for country, capital in capitals.items():
        print(f"- The capital of {country} is {capital}")

def interview_prep_gotchas() -> None:
    """Advanced topics frequently tested."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    # What can be a key?
    print("Gotcha 1: Dictionary Keys Requirement")
    print("Keys MUST be immutable types (Strings, Ints, Tuples).")
    print("Lists and Dicts cannot be keys because they are mutable/unhashable.")
    
    # Dictionary Comprehensions
    print("\nGotcha 2: Dictionary Comprehensions")
    # Syntax: {key_expr: value_expr for item in iterable if condition}
    prices = {"apple": 0.50, "orange": 0.60, "steak": 5.00}
    
    # E.g. Apply 10% tax to all items over $1.00
    taxed_prices = {k: round(v * 1.10, 2) for k, v in prices.items() if v >= 1.00}
    print(f"Prices over $1.00 with Tax: {taxed_prices}")

if __name__ == "__main__":
    print("🌟 Dictionaries 🌟")
    basic_dictionaries()
    dict_methods()
    iterating_dictionaries()
    interview_prep_gotchas()
