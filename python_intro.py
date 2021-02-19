# # Variables and Data Types
# # Python automatically generates the data type for us!
# str_var = 'Hello'
# int_var = 5
# float_var = 2.3
#
# print(type(str_var))
# print(type(int_var))
# print(type(float_var))

# # Integer addition
# a = 5
# b = 2
# print(a + b)
#
# # String Concatenation
# c = '5'
# d = '2'
# print(c + d)
#
# # You cannot add (+) a string and an integer together!
# # Convert the string to add, or convert the integer to concatenate
#
# # Boolean Comparison
# print(a > b)

# # If you want single quotes in a sentence, use double quotes
# # Vice versa if you want double quotes
# single = 'this is "single" quotes'
# double = "this is 'double' quotes"
# print(single)
# print(double)
# # Can also use escape characters
# esc = 'this is \'escaped\''
# print(esc)
# # String Slicing and Functions
# # INDEXES START FROM ZERO
# hello = 'Hello World'
# hello_long = 'Hello World           '
#
# print(hello[6:])
# print(hello[:6]) # Includes the space after Hello!
# print(hello_long)
# print(hello_long.strip())
# print(hello.count('l')) # Counts the instances of a string in a passed argument
# print(hello.upper())
# print(hello.lower())

# F Strings
# hello = 'Hello'
# name = 'Jenny'
# age = 11
#
# print(f"{hello} {name}, you are {age} years old!")
# # Boolean Methods
# hi = 'Hello Everyone!'
# name = 'Jenny'
# age = '11'
#
# print(hi.isalpha()) # This is false because there is a ! in the string
# print(name.isalpha()) # True, isalpha checks if string is only alphabetical characters
# print(age.isalpha())
# # Many different is...() methods, trial them out whenever you need them!
# x = None # NULL
# y = False
#
# print(bool(x))
# print(bool(y))
#
# print(x == False) # x is None, not False! None and False are not equivalent
# print(y == False)
#
# print(x == None) # Comparing x to None will return True
# print(x is None)
#
# print(bool(x) == False) # But this will be True! bool(x) IS False and thus is equivalent to False, and returns True

# Lists and Tuples
# shopping_list = ["Cheese", "Avocados", "Apples"]
# shopping_list.append("Sugar") # Appends an item to the end of the list
# shopping_list[0] = "Milk" # Replaces the first item in the list
# shopping_list.remove("Avocados") # Removes the specified item from the list (can also use the index)
# print(shopping_list) # Prints the items in the list
# print(type(shopping_list)) # Prints the data type
# print(shopping_list[0]) # Prints the first item in the list
# print(shopping_list[-1]) # Prints the last item in the list
# print(len(shopping_list)) # Prints the number of items in the list

# # Slicing Lists
# shopping_list = ["Cheese", "Avocados", "Apples", "Milk", "Tea", "Coffee"]
# print(shopping_list[:2]) # Gets the first two items from the list
# print(shopping_list[::2]) # Step size for getting different items in the list

# # Tuples
# # Similar to lists, except Tuples are immutable and their contents cannot be changed
# shopping_tup = ("Cheese", "Avocados", "Apples", "Milk", "Tea", "Coffee")
#
# print(shopping_tup)
# print(type(shopping_tup))
# print(shopping_tup[0])

# # Dictionaries
# # Use Key-Value pairs
# new_dict = {"my_key": "values", "num": 3,
#             "key_list": ["val1", "val2", "val3"]}
#
# print(new_dict)
# print(new_dict['num']) # Returns the value using the key name
# print(new_dict['key_list'])
# print(new_dict['key_list'][0]) # Don't include spaces when searching a list in a dictionary!
#
# print(new_dict.keys()) # Prints list of dictionary keys
# print(new_dict.values()) # Prints list of dictionary values
#
# new_dict["my_key"] = "Something Else" # Changes the value of the key in the square brackets
# print(new_dict)

num = 11
# This clause is followed if the statement is True
if num == 10:
    print("The number is 10")
# This is followed if the original if statement is False
else:
    print("The number is not 10")

if num == 10:
    print("The number is 10")
elif num > 10:
    print("The number is greater than 10")
else:
    print("The number is not 10")
