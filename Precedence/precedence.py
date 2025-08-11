"""
# Python Tutorial: Understanding Operator Precedence

This tutorial is designed to teach you the basics of operator precedence in Python.
Operator precedence determines the order in which operations are performed when
there are multiple operators in an expression.

## What is Operator Precedence?
In Python (and most programming languages), some operations have higher priority than others.
For example:
    - Multiplication (*) has higher precedence than addition (+).
    - Parentheses () have the highest precedence.

Understanding precedence helps you write correct expressions and avoid unexpected results.

## General Rules of Precedence
1. Parentheses `()`
2. Exponentiation `**`
3. Unary operators `+`, `-`
4. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
5. Addition `+`, Subtraction `-`
6. Comparison operators (`<`, `>`, `<=`, `>=`, `==`, `!=`)
7. Logical NOT `not`
8. Logical AND `and`
9. Logical OR `or`

In this tutorial, we will explore these rules using examples.
"""

# Example 1: Easy Level
# Demonstrating Basic Arithmetic Precedence
# Expression: 10 + 5 * 2

print("Example 1: Easy Level\n")
expression_easy = 10 + 5 * 2
print("Expression: 10 + 5 * 2")
print("Step 1: Multiplication (*) is evaluated first: 5 * 2 = 10")
print("Step 2: Addition (+) is evaluated next: 10 + 10 = 20")
print("Result:", expression_easy)
print("\nExplanation: Multiplication has higher precedence than addition, so it is evaluated first.")

# Example 2: Medium Level
# Using Parentheses to Change Precedence
# Expression: (10 + 5) * 2

print("\nExample 2: Medium Level\n")
expression_medium = (10 + 5) * 2
print("Expression: (10 + 5) * 2")
print("Step 1: Parentheses are evaluated first: 10 + 5 = 15")
print("Step 2: Multiplication (*) is evaluated next: 15 * 2 = 30")
print("Result:", expression_medium)
print("\nExplanation: Parentheses have the highest precedence, so the addition is evaluated before multiplication.")

# Example 3: Hard Level
# Combining Multiple Operators with Logical Operations
# Expression: 10 + 5 * 2 > 20 or not 5 == 5

print("\nExample 3: Hard Level\n")
expression_hard = 10 + 5 * 2 > 20 or not 5 == 5
print("Expression: 10 + 5 * 2 > 20 or not 5 == 5")
print("Step 1: Multiplication (*) is evaluated first: 5 * 2 = 10")
print("Step 2: Addition (+) is evaluated next: 10 + 10 = 20")
print("Step 3: Comparison (>): 20 > 20 is False")
print("Step 4: Equality (==) is evaluated: 5 == 5 is True")
print("Step 5: Logical NOT is applied: not True is False")
print("Step 6: Logical OR is evaluated: False or False is False")
print("Result:", expression_hard)
print("\nExplanation: The precedence order of arithmetic, comparison, and logical operators determines the final result.")

# Additional Notes for Beginners
"""
## Key Takeaways
1. **Parentheses ()**: Always use parentheses to explicitly specify the order of operations.
2. **Operator Precedence Table**: Memorizing or referencing the precedence table can help avoid errors.
3. **Logical Operators**: Logical operators like `not`, `and`, and `or` follow their own precedence rules.
4. **Debugging Expressions**: If you're unsure about the precedence, break the expression into smaller steps.

## Try It Yourself
Here are a few expressions to practice:
1. 8 + 3 * 2
2. (8 + 3) * 2
3. 10 > 5 and 3 < 2
4. not (10 > 5 or 3 < 2)

Practice breaking them down step by step and predicting the result before running the code.
"""

