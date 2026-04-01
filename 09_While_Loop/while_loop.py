"""
While Loops in Python
-------------------
A `while` loop executes a block of code repeatedly as long as a condition is True.
Useful for reading streams, waiting for user input, or running infinite servers.

Topics Covered:
1. Basic While Loop
2. Break, Continue, and Pass Statements
3. The While-Else Clause (Python Specific Feature)
4. Infinite Loops & Avoidance
"""

def basic_while_loop() -> None:
    """Demonstrates a simple counter loop."""
    print("--- 1. Basic While Loop ---")
    
    count: int = 1
    while count <= 3:
        print(f"Count is: {count}")
        # CRITICAL: Always update the condition variable to avoid infinite loops!
        count += 1
    
    print("Loop finished!")

def loop_control_statements() -> None:
    """Using break and continue to control loop flow."""
    print("\n--- 2. Break and Continue ---")
    
    print("Scenario: Print odd numbers up to 10, but stop if number is exactly 7.")
    num: int = 0
    while num < 10:
        num += 1
        
        # 'continue' skips the rest of the current iteration and jumps to the top
        if num % 2 == 0:
            continue
            
        # 'break' terminates the loop entirely
        if num == 7:
            print(f"Found {num}! Breaking out of loop.")
            break
            
        print(f"Processing number: {num}")

def while_else_clause() -> None:
    """The mysterious while-else clause (Common Interview Question)."""
    print("\n--- 3. The While-Else Clause ---")
    
    # Rule: The 'else' block runs ONLY if the loop finishes NATURALLY.
    # If the loop hits a 'break' statement, the 'else' block is SKIPPED.
    
    print("Test 1: Loop finishes naturally")
    i = 0
    while i < 3:
        i += 1
    else:
        print("    -> Loop naturally completed! Else block executed.")
        
    print("Test 2: Loop hits a break statement")
    j = 0
    while j < 5:
        if j == 2:
            break
        j += 1
    else:
        print("    -> This will NOT print because loop broke.")
    print("    -> Loop broke early. Else block skipped.")

def interview_prep_gotchas() -> None:
    """Common gotchas regarding while loops."""
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    # Pass statement
    print("The 'pass' statement does nothing. It's a placeholder for future code.")
    # Example (won't run to avoid infinite loop):
    # while True:
    #     pass
    
    print("Simulation of a 'do-while' loop (Python doesn't have one natively):")
    # Using while True with a break condition at the end
    attempts = 0
    while True:
        attempts += 1
        print("Executing code block blindly at least once...")
        if attempts >= 1: # Condition checked at the end
            break

if __name__ == "__main__":
    print("🌟 While Loops 🌟")
    basic_while_loop()
    loop_control_statements()
    while_else_clause()
    interview_prep_gotchas()
