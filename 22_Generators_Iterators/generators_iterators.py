"""
Generators & Iterators in Python
------------------------------
Iterables (like Lists) allow you to loop over them. 
Iterators are stateful objects that remember where they are during iteration.
Generators are simple ways to create iterators using the 'yield' keyword.

Why Generators?
Generators do not store all values in memory. They generate them 'On-The-Fly',
making them INCREDIBLY memory-efficient for large datasets.
"""

import sys

def iterators_vs_iterables() -> None:
    """Understanding the underlying mechanics of loops."""
    print("--- 1. Iterables vs Iterators ---")
    
    fruits = ["Apple", "Banana", "Cherry"] # An Iterable (Not an iterator, but CAN create one)
    
    # A for-loop actually does this under the hood:
    iterator_obj = iter(fruits) # 1. Get the iterator
    
    print("Extracting via next():")
    print(f" 1) {next(iterator_obj)}")
    print(f" 2) {next(iterator_obj)}")
    print(f" 3) {next(iterator_obj)}")
    
    # print(next(iterator_obj)) # CRASH: StopIteration Exception! (The iterator is exhausted)
    print(" (After 3 items, the iterator is exhausted. It cannot be 'rewound').")

def my_generator(max_val: int):
    """
    The 'yield' keyword turns a regular function into a Generator function.
    Instead of 'return'ing a final value and dying, 'yield' PAUSES the function,
    returns a value, and waits to be called again!
    """
    print("\n    [Generator Init]")
    num = 1
    while num <= max_val:
        print(f"    [Generator Yielding {num}]")
        yield num  # Pauses here!
        print(f"    [Generator Resuming...]")
        num += 1

def testing_generators() -> None:
    print("\n--- 2. Building Generators ---")
    
    gen = my_generator(3) # Does NOT execute code! Returns a generator object.
    print(f"Generator Type: {type(gen)}")
    
    print("\nExecuting:")
    for value in gen:
        print(f"Got Value: {value}")
        print("-------------")

def Memory_efficiency_test() -> None:
    """Why generators are critical in big data engineering."""
    print("\n--- 3. Memory Efficiency: Lists vs Generators ---")
    
    # List Comprehension generates 1,000,000 numbers in Memory immediately!
    list_comp = [x**2 for x in range(1000000)]
    
    # Generator Expression uses () brackets. Starts calculating ONLY when next() is called.
    gen_comp = (x**2 for x in range(1000000))
    
    print(f"Size of List in Memory: {sys.getsizeof(list_comp)} bytes")
    print(f"Size of Generator in Memory: {sys.getsizeof(gen_comp)} bytes !!")
    print("-> Generators are lazy and take almost zero memory!")

def interview_prep_gotchas() -> None:
    print("\n--- 4. Interview Prep & Gotchas ---")
    
    print("Question 1: What is the difference between 'yield' and 'return'?")
    print("Answer: 'return' terminates the local state, destroys variables, and exits.")
    print("'yield' pauses execution, saves all variables and state locally, and resumes on next().")
    
    print("\nQuestion 2: How do you read a 100 GB log file in Python?")
    print("Answer: DO NOT use readlines() or read()! They load everything into RAM.")
    print("You should iterate line-by-line using a for-loop on the file object, which ")
    print("acts as a generator internally, yielding one line at a time.")

if __name__ == "__main__":
    print("🌟 Generators & Iterators 🌟")
    iterators_vs_iterables()
    testing_generators()
    Memory_efficiency_test()
    interview_prep_gotchas()
