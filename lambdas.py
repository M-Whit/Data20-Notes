# # Normal function
# def add(num1, num2):
#     return num1 + num2
#
#
# print(add(2, 3))
#
# # Lambda function
# # Define parameters to the left of :, and then what the function does to the right
# addition = lambda num1, num2: num1 + num2
#
# print(addition(2, 3))

# Lambda functions are useful typically in conjunction with transformative function, such as map
# map - map a function over an iterable

# map(function, iterable)

# def square_func(num):
#     return num ** 2
#
#
# # We want to apply the above function using the list below
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
# # You have to print a 'list', otherwise it will return a 'map object'
# # map KNOWS that you will be passing the iterable into the function, so you don't need to add brackets to the function
# squared_numbers = map(square_func, numbers_list)
# print(squared_numbers)
# print(list(squared_numbers))
#
# # Where would a lambda go inside the map() function?
# # --- It will replace the function parameter
# squared_numbers_lambda = map(lambda x: x ** 2, numbers_list)
# print(squared_numbers_lambda)
# print(list(squared_numbers_lambda))

# salary = [230, 350, 540, 430]
#
# # Apply a 10% bonus to the salary
# # The lambda function is a bit tricky, treat it like a for loop when you consider what 'x' is
# # E.g. 'x' will be, as the function processes, everything in the iterable
# # So we want to multiply it (and by extension, everything in the list) by 1.10, for the 10% increase
# bonus = map(lambda x: round(x * 1.10, 2), salary)
# print(list(bonus))

