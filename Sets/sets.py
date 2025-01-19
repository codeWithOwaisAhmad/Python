# Python Sets Tutorial

# Easy Level Example: Creating and Using Sets

# Step 1: Create an empty set
my_set = set()
print("Initial empty set:", my_set)

# Step 2: Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("Set after adding elements:", my_set)

# Step 3: Add duplicate elements (they will be ignored)
my_set.add(2)
print("Set after adding a duplicate element:", my_set)

# Step 4: Check if an element exists in the set
print("Is 2 in the set?", 2 in my_set)
print("Is 4 in the set?", 4 in my_set)

# Step 5: Remove an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)


# Medium Level Example: Set Operations

# Step 1: Create two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set A:", set_a)
print("Set B:", set_b)

# Step 2: Perform union operation
union_set = set_a.union(set_b)
print("Union of A and B:", union_set)

# Step 3: Perform intersection operation
intersection_set = set_a.intersection(set_b)
print("Intersection of A and B:", intersection_set)

# Step 4: Perform difference operations
difference_set_a_b = set_a.difference(set_b)
difference_set_b_a = set_b.difference(set_a)
print("Difference (A - B):", difference_set_a_b)
print("Difference (B - A):", difference_set_b_a)


# Hard Level Example: Set Comprehensions and Advanced Operations

# Step 1: Create a set using set comprehension
squared_set = {x**2 for x in range(1, 6)}
print("Set of squares from 1 to 5:", squared_set)

# Step 2: Create two new sets
set_c = {1, 2, 3, 4, 5}
set_d = {2, 4, 6, 8}
print("Set C:", set_c)
print("Set D:", set_d)

# Step 3: Perform symmetric difference operation
symmetric_difference_set = set_c.symmetric_difference(set_d)
print("Symmetric Difference of C and D:", symmetric_difference_set)

# Step 4: Check if one set is a subset of another
is_subset = set_c.issubset(squared_set)
print("Is Set C a subset of the squared set?", is_subset)

# Step 5: Check if one set is a superset of another
is_superset = set_d.issuperset({2, 4})
print("Is Set D a superset of {2, 4}?", is_superset)