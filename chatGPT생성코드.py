# Advantages and Disadvantages of Lists, Tuples, Sets, and Dict in Python

# Lists:
# Advantages:
# - Mutable (can be modified)
# - Supports indexing and slicing
# - Can store duplicate elements
# Disadvantages:
# - Slower for lookups compared to sets and dictionaries
# - Inefficient for large-scale operations due to dynamic resizing

my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Lists are mutable
print("List:", my_list)

# Tuples:
# Advantages:
# - Immutable (cannot be modified)
# - Faster than lists for iteration
# - Can be used as dictionary keys
# Disadvantages:
# - Cannot add or remove elements after creation
# - Limited functionality compared to lists

my_tuple = (1, 2, 3, 4, 5)
# my_tuple.append(6)  # This will raise an error
print("Tuple:", my_tuple)

# Sets:
# Advantages:
# - Unordered collection of unique elements
# - Very fast membership tests (O(1))
# - Supports set operations (union, intersection, etc.)
# Disadvantages:
# - Cannot access elements by index
# - Does not allow duplicate values

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print("Set:", my_set)

# Dictionaries:
# Advantages:
# - Key-Value pairs for efficient data retrieval
# - Keys are unique and immutable
# - Supports dictionary-specific methods (keys, values, items)
# Disadvantages:
# - No guaranteed order (before Python 3.7, dictionaries were unordered)
# - Overhead in terms of memory usage

my_dict = {'one': 1, 'two': 2, 'three': 3}
my_dict['four'] = 4
print("Dictionary:", my_dict)

# Summary:
# - Lists are versatile but slower for lookups.
# - Tuples are immutable and faster for iteration.
# - Sets are useful for unique, unordered data with fast membership tests.
# - Dictionaries are great for key-value pairs and efficient data retrieval.
