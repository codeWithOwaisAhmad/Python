"""
Operator Precedence in Python
---------------------------
When an expression contains more than one operator, the order of evaluation 
depends on operator precedence. (Similar to PEMDAS / BODMAS in math).

Topics Covered:
1. Basic Math Precedence
2. Parentheses to Override Precedence
3. Short-Circuit Evaluation (Logical Precedence)
4. Interview Gotchas
"""

def basic_precedence() -> None:
    """Precedence evaluation with math operations."""
    print("--- 1. Mathematical Precedence ---")
    
    # PEMDAS: Parentheses, Exponentiation, Multiplication/Division, Addition/Subtraction
    # Example 1: Multiplication before Addition
    result = 10 + 5 * 2
    print(f"10 + 5 * 2 = {result} (Multiplication happens first)")
    
    # Example 2: Exponentiation has higher precedence
    result2 = 5 + 2 ** 3
    print(f"5 + 2 ** 3 = {result2} (Exponentiation happens first)")
    
    # Right-to-Left evaluation for Exponentiation
    result3 = 2 ** 3 ** 2
    print(f"2 ** 3 ** 2 = {result3} (Evaluated right-to-left: 2 ** 9)")

def overriding_precedence() -> None:
    """Using parentheses to force an order."""
    print("\n--- 2. Parentheses (Overriding Precedence) ---")
    
    # Parentheses always win!
    result = (10 + 5) * 2
    print(f"(10 + 5) * 2 = {result} (Addition happens first due to parentheses)")

def logical_short_circuit() -> None:
    """Logical 'and' has higher precedence than 'or'."""
    print("\n--- 3. Logical Precedence & Short-Circuit ---")
    
    res = False or True and False
    print(f"False or True and False = {res} (Because 'and' is evaluated before 'or')")
    
    # Short-Circuiting:
    # Python stops evaluating logical expressions as soon as it knows the answer
    def slow_function():
        print("    [slow_function was executed!]")
        return True
    
    print("\nTesting 'False and slow_function()':")
    # slow_function() will NEVER run because False AND anything is False
    result1 = False and slow_function()
    
    print("\nTesting 'True or slow_function()':")
    # slow_function() will NEVER run because True OR anything is True
    result2 = True or slow_function()

def interview_prep_gotchas() -> None:
    """Common gotchas regarding precedence."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    # Gotcha 1: Chained Comparisons
    x = 5
    result = 1 < x < 10
    print(f"1 < x < 10: {result} (Python evaluates this as: 1 < x and x < 10)")
    
    # Gotcha 2: Bitwise vs Logical
    # Bitwise operators (&, |) have HIGHER precedence than comparison operators (>, <)
    # This often causes bugs.
    try:
        if 5 > 2 & 1 > 0:
            print("Bitwise precedence bug!")
    except Exception as e:
        pass
    
    print("5 > 2 & 1 > 0 is evaluated as 5 > (2 & 1) > 0. Use parentheses for clarity!")

if __name__ == "__main__":
    print("🌟 Operator Precedence 🌟")
    basic_precedence()
    overriding_precedence()
    logical_short_circuit()
    interview_prep_gotchas()
