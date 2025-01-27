# for_loop_tutorial.py

# Introduction
"""
This tutorial covers the basics of the 'for' loop in Python. A 'for' loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string). With a 'for' loop, you can execute a set of statements for each item in the sequence.

We'll go through three examples of increasing difficulty: easy, medium, and hard.
"""

# Easy Example
"""
Example 1: Iterating over a list of numbers and printing each number.

In this example, we'll use a 'for' loop to iterate over a list of numbers and print each number in the list.
"""

# Code for Easy Example
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Explanation:
"""
1. We define a list of numbers: [1, 2, 3, 4, 5]
2. We use a 'for' loop to iterate over each element in the list.
3. The 'number' variable takes the value of each element in the list one by one.
4. We print the current value of 'number' in each iteration.
"""

# Medium Example
"""
Example 2: Iterating over a string and printing each character along with its index.

In this example, we'll use a 'for' loop with the 'enumerate' function to iterate over a string and print each character along with its index.
"""

# Code for Medium Example
text = "Python"
for index, char in enumerate(text):
    print(f"Index {index}: Character {char}")

# Explanation:
"""
1. We define a string: "Python"
2. We use the 'enumerate' function to get both the index and the character for each iteration.
3. The 'index' variable takes the value of the current index, and 'char' takes the value of the current character.
4. We print the index and the character in each iteration using an f-string.
"""

# Hard Example
"""
Example 3: Iterating over a dictionary and printing each key-value pair.

In this example, we'll use a 'for' loop to iterate over a dictionary and print each key-value pair.
"""

# Code for Hard Example
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

for student, score in student_scores.items():
    print(f"{student}: {score}")

# Explanation:
"""
1. We define a dictionary with student names as keys and their scores as values.
2. We use the 'items()' method to get both the key and the value for each iteration.
3. The 'student' variable takes the value of the current key, and 'score' takes the value of the current value.
4. We print the student name and their score in each iteration using an f-string.
"""
# The Following Loop is a Multiplication Table of 10 
for i in range(11):
    print(f"10 x {i} = {10 * i}")
#Iterating in the List Using For Loop
# 1)Method
sample_list = [31,23,45,24,12,68,97]
for i in range(len(sample_list))
   print(i)
# 2)Method
sample_list = [31,23,45,24,12,68,97]
for i in sample_list:
   print(sample_list[i])
# Conclusion
"""
In this tutorial, we covered the basics of the 'for' loop in Python with three examples of increasing difficulty. We learned how to iterate over a list, a string, and a dictionary using a 'for' loop. Understanding loops is fundamental for programming, and the 'for' loop is a versatile tool for iterating over sequences in Python.
"""
