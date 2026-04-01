"""
Exception Handling in Python
--------------------------
Errors are inevitable. Exception handling allows Python to catch runtime errors gracefully 
preventing the program from crashing abruptly.

Topics Covered:
1. Compile-time vs Runtime Errors
2. Try, Except, Else, and Finally blocks
3. Catching Specific Exceptions vs Broad Exceptions
4. Raising custom exceptions
"""

def syntax_vs_exceptions() -> None:
    """Understanding the difference between error types."""
    print("--- 1. Compile-Time vs Runtime Errors ---")
    
    print("SyntaxError (Compile-Time): Detected before the code runs.")
    print("Example: An unclosed parenthesis or a missing colon.")
    
    print("\nException (Runtime): Occurs during execution, often due to invalid data.")
    print("Example: Dividing by zero or trying to read a missing file.")

def basic_try_except() -> None:
    """The fundamental error handling block."""
    print("\n--- 2. Try & Except Blocks ---")
    
    try:
        print("Attempting a risky calculation...")
        result = 10 / 0
        print(f"Result: {result} (This will never print)")
        
    except ZeroDivisionError as e:
        print(f"CRASH AVOIDED! Caught Error: '{e}'")
        
    except Exception as general_error:
        print(f"Caught a general error: '{general_error}'")

def full_error_handling_flow() -> None:
    """Combining Try, Except, Else, and Finally."""
    print("\n--- 3. Try, Except, Else, Finally ---")
    
    print("Test 1: Normal Execution (No Error)")
    try:
        val = int("10")
    except ValueError:
        print("  -> (Except) Failed to convert to int.")
    else:
        # The 'else' block runs ONLY if the 'try' block succeeds.
        print(f"  -> (Else) Conversion Successful: {val}")
    finally:
        # The 'finally' block ALWAYS runs, error or not. Critical for cleanup!
        print("  -> (Finally) Cleaned up resources closed file handles.")

def raising_exceptions() -> None:
    """You can intentionally raise errors using the 'raise' keyword."""
    print("\n--- 4. Raising Exceptions & Interview Gotchas ---")
    
    age = -5
    print(f"Validating Age: {age}")
    
    try:
        if age < 0:
            raise ValueError("Age cannot be negative!")
        print("Age is valid.")
    except ValueError as val_err:
        print(f"Triggered Exception: {val_err}")

def interview_prep_gotchas() -> None:
    print("\nGotcha 1: The 'Bare Except' Anti-Pattern")
    print("  BAD PRACTICE:")
    print("  try:")
    print("      # code")
    print("  except:")
    print("      pass")
    print("  Why? Because it catches EVERYTHING, including SystemExit and KeyboardInterrupt (Ctrl+C).")
    print("  You should always catch 'Exception' or specific errors (ZeroDivision, KeyError...).")
    
    print("\nGotcha 2: Returning inside a 'Finally' block")
    print("  If you return a value inside the 'finally' block, it overrides the return values")
    print("  from the 'try' or 'except' blocks. Avoid doing this!")

if __name__ == "__main__":
    print("🌟 Exception Handling 🌟")
    syntax_vs_exceptions()
    basic_try_except()
    full_error_handling_flow()
    raising_exceptions()
    interview_prep_gotchas()
