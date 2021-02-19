# Script to collect user data,
# store user data,
# and print back to the user
#
# Include information on:
# Name
# Age
# Address (collect different parts separately)
# Favourite Films

first_name = input("Please input your first name: ")
last_name = input("Please input your last name: ")

age = input("Please input your age: ")
house_num = input("What is your house number? ")
road = input("What road do you live on? ")
city = input("What city do you live in? ")
postcode = input("What is your postcode? ")

film1 = input("What is your favourite film? ")
film2 = input("What is your second favourite film? ")

print(f"\nYour name is {first_name} {last_name}. You are {age} years old.\n"
      f"You live at {house_num} {road}, {postcode.upper()}, in {city}.\n"
      f"Your favourite films are {film1} and {film2}")


