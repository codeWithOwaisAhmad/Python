# Python File Handling Explained for Beginners

# File handling in Python allows us to create, read, write, and delete files.
# The built-in 'open()' function is used for this purpose.

# Example 1: Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python makes file handling easy!\n")
print("File written successfully.")

# Example 2: Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Example 3: Appending to a file
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
print("Content appended successfully.")

# Example 4: Reading file line by line
with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())  # strip() removes extra newline characters

# Example 5: Checking if a file exists before reading
import os
if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print("File exists, reading content:")
        print(file.read())
else:
    print("File does not exist.")

# Example 6: Deleting a file
os.remove("example.txt")
print("File deleted successfully.")

# File handling is crucial for storing and managing data in applications.
# Try modifying the code and working with different file operations!


