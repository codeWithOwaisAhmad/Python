def easy_example():
    # Easy Example: Creating and Accessing Tuples

    # Step 1: Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)

    # Step 2: Accessing elements in a tuple
    first_element = my_tuple[0]
    second_element = my_tuple[1]

    # Step 3: Printing the elements
    print("First Element:", first_element)
    print("Second Element:", second_element)

    # Step 4: Tuple with mixed data types
    mixed_tuple = (1, "Hello", 3.14)
    print("Mixed Tuple:", mixed_tuple)

def medium_example():
    # Medium Example: Tuple Operations and Methods

    # Step 1: Creating a tuple
    my_tuple = (10, 20, 30, 40, 50)

    # Step 2: Slicing a tuple
    slice_tuple = my_tuple[1:4]  # Slicing from index 1 to 3 (4 is excluded)

    # Step 3: Finding the length of a tuple
    tuple_length = len(my_tuple)

    # Step 4: Concatenating tuples
    another_tuple = (60, 70)
    concatenated_tuple = my_tuple + another_tuple

    # Step 5: Checking for element existence
    is_present = 30 in my_tuple

    # Step 6: Counting occurrences and finding index
    count_of_30 = my_tuple.count(30)
    index_of_40 = my_tuple.index(40)

    # Step 7: Printing the results
    print("Original Tuple:", my_tuple)
    print("Sliced Tuple:", slice_tuple)
    print("Length of Tuple:", tuple_length)
    print("Concatenated Tuple:", concatenated_tuple)
    print("Is 30 present in tuple?", is_present)
    print("Count of 30:", count_of_30)
    print("Index of 40:", index_of_40)

def hard_example():
    # Hard Example: Nested Tuples and Tuple Unpacking

    # Step 1: Creating nested tuples
    nested_tuple = ((1, 2), (3, 4), (5, 6))

    # Step 2: Accessing elements in nested tuples
    first_inner_tuple = nested_tuple[0]
    first_element_of_second_tuple = nested_tuple[1][0]

    # Step 3: Tuple unpacking
    a, b, c = nested_tuple

    # Step 4: Unpacking inner tuples
    (x1, y1), (x2, y2), (x3, y3) = nested_tuple

    # Step 5: Printing the results
    print("Nested Tuple:", nested_tuple)
    print("First Inner Tuple:", first_inner_tuple)
    print("First Element of Second Tuple:", first_element_of_second_tuple)
    print("Unpacked Tuples:", a, b, c)
    print("Unpacked Inner Tuples:", (x1, y1), (x2, y2), (x3, y3))

# Run examples
easy_example()
medium_example()
hard_example()