"""
Tuples in Python
--------------
Tuples are ordered collections similar to lists, but they are IMMUTABLE.
Once created, you cannot change, add, or remove elements from a tuple.

Topics Covered:
1. Tuple Creation (Parentheses vs Commas)
2. Tuple Packing & Unpacking
3. Why use Tuples over Lists? (Interview Insight)
4. Tuple Methods (Count, Index)
"""

def tuple_creation() -> None:
    """Creating and basic indexing of Tuples."""
    print("--- 1. Tuple Creation & Access ---")
    
    # Parentheses are standard, but the COMMA is what actually makes the tuple!
    my_tuple = (1, 2, 3, "Apple")
    print(f"Tuple: {my_tuple} | Type: {type(my_tuple).__name__}")
    
    # Indexing exactly like lists
    print(f"Access my_tuple[1]: {my_tuple[1]}")
    
    print("\n--- Single Item Tuple Gotcha ---")
    not_a_tuple = ("Hello") # This is just a string in parentheses!
    print(f"('Hello') is of type: {type(not_a_tuple).__name__}")
    
    # Critical: You need a trailing comma for a single-item tuple
    real_single_tuple = ("Hello",)
    print(f"('Hello',) is of type: {type(real_single_tuple).__name__} (Notice the comma)")

def packing_and_unpacking() -> None:
    """Assigning and extracting multiple values easily."""
    print("\n--- 2. Packing & Unpacking ---")
    
    # Packing: Putting multiple values into one variable
    person = "Alice", 30, "Engineer" # Commas automatically make a tuple
    print(f"Packed Person: {person}")
    
    # Unpacking: Extracting values into separate variables
    name, age, profession = person
    print(f"Unpacked -> Name: {name}, Age: {age}, Profession: {profession}")
    
    # Extended Unpacking (Using Asterisk *)
    # Useful when there are more values than variables
    grades = (95, 80, 85, 90, 100)
    first_grade, *middle_grades, last_grade = grades
    print(f"\nExtended Unpacking -> First: {first_grade}, Middle: {middle_grades}, Last: {last_grade}")

def interview_prep_gotchas() -> None:
    """Common questions on the differences between Lists and Tuples."""
    print("\n--- 3. Interview Prep & Gotchas (Tuples vs Lists) ---")
    
    print("Question 1: Why use Tuples over Lists?")
    print("  1) Memory Efficiency: Tuples use less memory than lists.")
    print("  2) Data Integrity: Mutability rules guarantee values won't change.")
    print("  3) Dictionary Keys: Only immutable types (like Tuples) can be Hashmap (Dict) keys!")
    
    print("\nQuestion 2: Are Tuples *completely* immutable?")
    print("  Answer: No! If a tuple contains a mutable object (like a list),")
    print("  that internal object can still be modified.")
    
    tricky_tuple = (1, 2, [3, 4])
    print(f"\nOriginal tricky tuple: {tricky_tuple}")
    
    # tricky_tuple[0] = 5 # Error! Tuple is immutable
    # However, the list INSIDE the tuple is mutable...
    try:
        tricky_tuple[2].append(5)
        print(f"Modified tricky tuple! {tricky_tuple} (The underlying list was changed)")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("🌟 Tuples 🌟")
    tuple_creation()
    packing_and_unpacking()
    interview_prep_gotchas()
