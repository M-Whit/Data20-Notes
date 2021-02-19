# Create simple for loop for FizzBuzz
# If a number is a multiple of 3, print "Fizz"
# If a number is a multiple of 5, print "Buzz"
# If a number is a multiple of 3 AND 5, print "FizzBuzz"

fizz_list = range(1, 16)
# for n in fizz_list:
#     print(n)
for n in fizz_list:
    if n % 3 == 0 and n % 5 == 0:
        print(n, "FizzBuzz!")
    elif n % 3 == 0:
        print(n, "Fizz")
    elif n % 5 == 0:
        print(n, "Buzz")
    else:
        pass
