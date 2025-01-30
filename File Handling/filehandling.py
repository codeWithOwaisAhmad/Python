# Detailed Explanation of File Handling in Python

# 1. Introduction to File Handling
# File handling allows you to read and write files, which is essential for working with data.

# 2. Opening a File
file = open('example.txt', 'r')  # Open file for reading

# 3. Reading from a File
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# 4. Writing to a File
file = open('example.txt', 'w')
file.write('Hello, World!\n')
file.close()

# 5. Closing a File
file = open('example.txt', 'r')
file.close()

# 6. Using `with` Statement
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 7. File Modes
# 'r': Read
# 'w': Write (truncate)
# 'x': Create (fails if exists)
# 'a': Append
# 'b': Binary
# 't': Text
# '+': Read and write

# 8. Handling Exceptions
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found.')
finally:
    file.close()

# 9. Reading and Writing Binary Files
# Writing binary data
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02')

# Reading binary data
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)

# 10. File Object Methods
# file.read(size): Reads up to `size` bytes
# file.readline(): Reads a single line
# file.readlines(): Reads all lines into a list
# file.write(string): Writes a string to the file
# file.writelines(list): Writes a list of strings to the file
# file.seek(offset): Moves the file pointer to `offset`
# file.tell(): Returns the current file pointer position