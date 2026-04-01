"""
Operators in Python
-------------------
Operators are special symbols that perform computations on variables and values.

Topics Covered:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical & Identity & Membership Operators
5. Bitwise Operators (Advanced)
"""

def arithmetic_operators() -> None:
    """Basic math operators."""
    print("--- 1. Arithmetic Operators ---")
    
    a, b = 10, 3
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division (Float): {a} / {b} = {a / b}")
    
    # Very commonly asked in interviews!
    print(f"Floor Division (Int): {a} // {b} = {a // b} (Removes decimal)")
    print(f"Modulus (Remainder): {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b} (10 to the power of 3)")

def assignment_operators() -> None:
    """Assigning values to variables with shorthand operators."""
    print("\n--- 2. Assignment Operators ---")
    
    x = 5
    print(f"Initial x = {x}")
    x += 3
    print(f"x += 3: {x} (Same as x = x + 3)")
    x *= 2
    print(f"x *= 2: {x}")

def comparison_logical_identity() -> None:
    """Comparing values, boolean logic, and identity checking."""
    print("\n--- 3. Comparison, Logical, Identity ---")
    
    x, y = 5, 10
    
    # Comparison
    print(f"Is x == y? {x == y}")
    print(f"Is x != y? {x != y}")
    print(f"Is x < y? {x < y}")
    
    # Logical (and, or, not)
    condition1 = x > 0 # True
    condition2 = y > 20 # False
    print(f"\nCondition 1 AND Condition 2: {condition1 and condition2}")
    print(f"Condition 1 OR Condition 2: {condition1 or condition2}")
    print(f"NOT Condition 1: {not condition1}")
    
    # Identity (is, is not) -> Checks memory location, not just value!
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"\na is b? {a is b} (Same values, different memory!)")
    print(f"a is c? {a is c} (Same memory)")
    print(f"a == b? {a == b} (Same values)")
    
    # Membership (in, not in)
    fruits = ["apple", "banana"]
    print(f"\nIs 'apple' in fruits? {'apple' in fruits}")

def bitwise_operators_advanced() -> None:
    """Bitwise operators work on binary bits."""
    print("\n--- 4. Bitwise Operators (Advanced/Interview Prep) ---")
    
    a = 10 # 1010 in binary (8 + 2)
    b = 4  # 0100 in binary
    
    print(f"a = {a} (1010 in binary), b = {b} (0100 in binary)")
    print(f"Bitwise AND (a & b): {a & b} (0000)")
    print(f"Bitwise OR (a | b): {a | b} (1110 -> 14)")
    print(f"Left Shift (a << 1): {a << 1} (Shifts bits left, multiplies by 2)")

if __name__ == "__main__":
    print("🌟 Python Operators 🌟")
    arithmetic_operators()
    assignment_operators()
    comparison_logical_identity()
    bitwise_operators_advanced()
