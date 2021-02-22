def my_add_func(num1: int, num2: int):
    return num1 + num2

# With num1: int and num2: int, there are no default values, so arguments must be passed below
# print(my_add_func())

# Still works concatenating strings
print(my_add_func("hello", "hi"))

# Adding two integers still works as normal
print(my_add_func(10, 5))

# Defining multiple arguments using *multiargs
def multi_add_func(*multiargs):
    print(multiargs)
    print(type(multiargs))
    for arg in multiargs:
        print(arg)

multi_add_func(3, "asdf", ["hello", 3])
