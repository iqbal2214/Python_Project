a = 5            # integer
b = 3.14         # float
c = 2 + 3j       # complex number
print(c)
name = "John"    # string
message = 'Hello, World!'   # string

is_sunny = True   # boolean
is_raining = False  # boolean

my_list = [1, 2, 3, 'apple', 'banana']   # list of integers and strings
my_tuple = (4, 5, 'dog')    # tuple of integers and a string

#     Mutability: Lists are mutable, which means their elements can be added, removed, or changed after they are created. Tuples, on the other hand, are immutable, which means their elements cannot be changed after they are created.
#    Syntax: Lists are defined using square brackets [ ] while tuples are defined using parentheses ( ).
#    Usage: Lists are commonly used for storing collections of data that need to be modified, while tuples are commonly used for storing collections of data that do not need to be modified.

my_set = {1, 2, 3, 4, 4, 4}   # set of unique integers

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}  # dictionary of key-value pairs


my_var = None   # variable with no value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 30)   # object of class Person

#changes to check git

