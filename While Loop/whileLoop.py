# Python Tutorial on While Loop

# Easy Example: Simple Countdown

# Initialize the counter
counter = 5

# While loop to print countdown from 5 to 1
while counter > 0:
    print("Counter:", counter)
    counter -= 1

print("Liftoff!")

# Output:
# Counter: 5
# Counter: 4
# Counter: 3
# Counter: 2
# Counter: 1
# Liftoff!

# Medium Example: Summing Numbers

# Initialize the sum and counter
total_sum = 0
number = 1

# While loop to calculate the sum of numbers from 1 to 10
while number <= 10:
    total_sum += number
    number += 1

print("The sum of numbers from 1 to 10 is:", total_sum)

# Output:
# The sum of numbers from 1 to 10 is: 55

# Hard Example: Finding the First N Prime Numbers

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Initialize variables
num_primes = 0
number = 2
N = 10  # Find the first 10 prime numbers
prime_numbers = []

# While loop to find the first N prime numbers
while num_primes < N:
    if is_prime(number):
        prime_numbers.append(number)
        num_primes += 1
    number += 1

print("The first", N, "prime numbers are:", prime_numbers)

# Output:
# The first 10 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]