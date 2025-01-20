# Basics of Programming with Python - Conditionals

"""
Conditionals in Python allow you to execute different blocks of code based on certain conditions.
The primary conditional statements in Python are:
- if
- elif (else if)
- else

Let's go through three examples of conditionals with increasing complexity.
"""

# Easy Example: Checking if a number is positive, negative, or zero
def check_number(num):
    """
    This function checks if the input number is positive, negative, or zero.
    """
    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is zero.")

# Example usage of check_number function
print("Easy Example:")
check_number(10)
check_number(-5)
check_number(0)
print("\n")

"""
Explanation:
1. The function `check_number` takes a single argument `num`.
2. It checks if the number is greater than zero using `if num > 0`.
3. If the condition is true, it prints that the number is positive.
4. If the condition is false, it checks if the number is less than zero using `elif num < 0`.
5. If this condition is true, it prints that the number is negative.
6. If neither of the above conditions are true, it executes the `else` block and prints that the number is zero.
"""

# Medium Example: Grading system based on marks
def grade_student(marks):
    """
    This function assigns a grade based on the input marks.
    """
    if marks >= 90:
        print(f"Marks: {marks} - Grade: A")
    elif marks >= 80:
        print(f"Marks: {marks} - Grade: B")
    elif marks >= 70:
        print(f"Marks: {marks} - Grade: C")
    elif marks >= 60:
        print(f"Marks: {marks} - Grade: D")
    else:
        print(f"Marks: {marks} - Grade: F")

# Example usage of grade_student function
print("Medium Example:")
grade_student(95)
grade_student(85)
grade_student(75)
grade_student(65)
grade_student(55)
print("\n")

"""
Explanation:
1. The function `grade_student` takes a single argument `marks`.
2. It checks if the marks are greater than or equal to 90 using `if marks >= 90`.
3. If the condition is true, it prints that the grade is A.
4. If the condition is false, it checks if the marks are greater than or equal to 80 using `elif marks >= 80`.
5. If this condition is true, it prints that the grade is B.
6. This process continues with additional `elif` statements for grades C, D, and F.
7. If none of the conditions are met, it executes the `else` block and prints that the grade is F.
"""

# Hard Example: Checking if a year is a leap year
def is_leap_year(year):
    """
    This function checks if the input year is a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")

# Example usage of is_leap_year function
print("Hard Example:")
is_leap_year(2020)
is_leap_year(1900)
is_leap_year(2000)
is_leap_year(2021)
print("\n")

"""
Explanation:
1. The function `is_leap_year` takes a single argument `year`.
2. It checks if the year is divisible by 4 and not divisible by 100 using `if (year % 4 == 0 and year % 100 != 0)`.
3. Alternatively, it checks if the year is divisible by 400 using `or (year % 400 == 0)`.
4. If either condition is true, it prints that the year is a leap year.
5. If neither condition is true, it executes the `else` block and prints that the year is not a leap year.
"""

# End of Python file tutorial on conditionals