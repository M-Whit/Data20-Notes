num_start = int(input("Where does your list start? "))
num_end = int(input("Where does the list end? "))

def fizzbuzz(num_start, num_end):
    for n in range(num_start, num_end+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz!")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
    #return(n)

print(fizzbuzz(num_start, num_end))