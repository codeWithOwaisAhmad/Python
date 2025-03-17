# Python Recursion Explained for Beginners (Detailed Version)

# What is Recursion?
# Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem.
# This process continues until it reaches a base case, which stops the recursion.
# Recursion is particularly useful for solving problems that can be broken down into smaller, similar subproblems.

# Structure of a Recursive Function:
# 1. Base Case: The condition under which the function stops calling itself.
# 2. Recursive Case: The part of the function where it calls itself with a smaller problem.

# Why Use Recursion?
# Recursion is useful when a problem can be divided into similar subproblems, such as:
# - Mathematical computations (factorials, Fibonacci numbers)
# - Tree and graph traversal
# - Divide-and-conquer algorithms (like merge sort)

# Example 1: Factorial of a Number (Using Recursion)
print("Factorial Calculation using Recursion:")

def factorial(n):
    # Base case: Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        print(f"Reached base case: factorial({n}) = 1")
        return 1
    # Recursive case: n * factorial of (n-1)
    print(f"Calculating factorial({n}) = {n} * factorial({n - 1})")
    result = n * factorial(n - 1)
    print(f"Result of factorial({n}) = {result}")
    return result

num = 5
print("Factorial of", num, "is", factorial(num))  # Output: Factorial of 5 is 120

# Example 2: Fibonacci Series (Using Recursion)
print("\nFibonacci Series using Recursion:")

def fibonacci(n):
    # Base cases: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n == 0:
        print("Fibonacci(0) = 0")
        return 0
    elif n == 1:
        print("Fibonacci(1) = 1")
        return 1
    # Recursive case: Sum of the two preceding numbers
    print(f"Calculating Fibonacci({n}) = Fibonacci({n - 1}) + Fibonacci({n - 2})")
    result = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"Result of Fibonacci({n}) = {result}")
    return result

terms = 7
print("Fibonacci Series:", [fibonacci(i) for i in range(terms)])  # Output: [0, 1, 1, 2, 3, 5, 8]

# Advantages of Recursion:
# 1. Simplifies complex problems by breaking them down into smaller subproblems.
# 2. Code becomes more readable and elegant for problems like tree traversal.
# 3. Reduces the need for complex loops and nested iterations.

# Disadvantages of Recursion:
# 1. Can lead to high memory usage due to the call stack (stack overflow).
# 2. Performance may be slower compared to iterative solutions for large inputs.
# 3. Can be challenging to understand and debug if not written correctly.

# Tips for Writing Recursive Functions:
# 1. Always define a base case to stop recursion.
# 2. Ensure that the problem size is reduced in each recursive call.
# 3. Test your function with simple cases to verify correctness.

# Recursion is powerful and elegant, but it must be used carefully. Always analyze whether recursion is the most efficient solution for your problem!
