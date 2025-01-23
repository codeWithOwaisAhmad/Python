# Recursion Tutorial in Python

# Easy Example: Factorial of a Number
def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: The number to calculate the factorial for.
    :return: The factorial of the number.
    """
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Step-by-step explanation:
# factorial(5)
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# 120

# Expected output:
print("Factorial of 5:", factorial(5))  # Output: 120

# Medium Example: Fibonacci Series
def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using recursion.
    :param n: The position in the Fibonacci series.
    :return: The n-th Fibonacci number.
    """
    # Base cases: if n is 0, return 0; if n is 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Step-by-step explanation:
# fibonacci(5)
# fibonacci(4) + fibonacci(3)
# (fibonacci(3) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
# ((fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0))) + ((fibonacci(1) + fibonacci(0)) + 1)
# (((1 + 0) + 1) + (1 + 0)) + ((1 + 0) + 1)
# ((1 + 1) + (1 + 0)) + (1 + 1)
# (2 + 1) + 2
# 3 + 2
# 5

# Expected output:
print("5th Fibonacci number:", fibonacci(5))  # Output: 5

# Hard Example: Solving the Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem using recursion.
    :param n: The number of disks.
    :param source: The source peg.
    :param target: The target peg.
    :param auxiliary: The auxiliary peg.
    :return: None
    """
    # Base case: if there's only one disk, move it from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        # Move the top n-1 disks from source to auxiliary
        tower_of_hanoi(n - 1, source, auxiliary, target)
        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")
        # Move the n-1 disks from auxiliary to target
        tower_of_hanoi(n - 1, auxiliary, target, source)

# Step-by-step explanation for 3 disks:
# Move 2 disks from A to B using C as auxiliary
# Move disk 3 from A to C
# Move 2 disks from B to C using A as auxiliary

# Expected output:
print("Tower of Hanoi solution for 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')
# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C