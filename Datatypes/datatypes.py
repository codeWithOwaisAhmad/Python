# Python Data Types Explained with Examples

# 1. Numeric Data Types
# - int: Whole numbers
# - float: Decimal numbers
# - complex: Complex numbers

# Integer Example
num_int = 10
print(f'Integer: {num_int}, Type: {type(num_int)}')

# Float Example
num_float = 10.5
print(f'Float: {num_float}, Type: {type(num_float)}')

# Complex Example
num_complex = 2 + 3j
print(f'Complex: {num_complex}, Type: {type(num_complex)}')

# 2. String Data Type
# - Strings are sequences of characters
text = "Hello, Python!"
print(f'String: {text}, Type: {type(text)}')

# 3. Boolean Data Type
# - Used to represent True or False values
is_python_fun = True
print(f'Boolean: {is_python_fun}, Type: {type(is_python_fun)}')

# 4. Sequence Data Types
# - list: Ordered, mutable collection
# - tuple: Ordered, immutable collection
# - range: Represents an immutable sequence of numbers

# List Example
my_list = [1, 2, 3, "Python"]
print(f'List: {my_list}, Type: {type(my_list)}')

# Tuple Example
my_tuple = (1, 2, 3, "Python")
print(f'Tuple: {my_tuple}, Type: {type(my_tuple)}')

# Range Example
my_range = range(5)  # Generates numbers from 0 to 4
print(f'Range: {list(my_range)}, Type: {type(my_range)}')

# 5. Set Data Type
# - Unordered collection of unique elements
my_set = {1, 2, 3, 3, 4}
print(f'Set: {my_set}, Type: {type(my_set)}')

# 6. Dictionary Data Type
# - Stores key-value pairs
my_dict = {"name": "Alice", "age": 25}
print(f'Dictionary: {my_dict}, Type: {type(my_dict)}')

# 7. NoneType
# - Represents the absence of a value
my_none = None
print(f'NoneType: {my_none}, Type: {type(my_none)}')
