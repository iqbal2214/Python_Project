# Lists are mutable
my_list = [1, 2, 3]
my_list.append(4)   # Add an element to the list
my_list[0] = 0     # Change the first element of the list
print(my_list)   # Output: [0, 2, 3, 4]

# Tuples are immutable
my_tuple = (1, 2, 3)
my_tuple.append(4)   # This will give an AttributeError
my_tuple[0] = 0     # This will give a TypeError



# List syntax
my_list = [1, 2, 3]

# Tuple syntax
my_tuple = (1, 2, 3)



# Lists are commonly used for storing collections of data that need to be modified
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 0
print(my_list)   # Output: [0, 2, 3, 4]

# Tuples are commonly used for storing collections of data that do not need to be modified
my_tuple = (1, 2, 3)
print(my_tuple)   # Output: (1, 2, 3)
#changes to check git

