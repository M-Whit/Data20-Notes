# Determine if a word is an Isogram
# Meaning that no letter is repeated in the word
# Examples include lumberjacks, background, downstream and six-year-old
# Hyphens are allowed

# First, user inputs a word
iso_test = input("What word do you want to check? ")

# Strip the input of "-"
# Could strip more punctuation in V2
iso_test = iso_test.replace("-", "")

# Put each character from iso_test into a list
iso_list = list(iso_test)
# Sort iso_list alphabetically
iso_list = sorted(iso_list)
# Remove duplicate characters from iso_list
iso_list_compare = set(iso_list)
# Sort iso_list_compare alphabetically
iso_list_compare = sorted(iso_list_compare)

# Print list comparison (optional)
print(iso_list)
print(iso_list_compare)

# Checking if the lists are identical
if iso_list != iso_list_compare:
    # If they are not identical
    print(f"{iso_test} is not an Isogram")
else:
    # If they are identical
    print(f"{iso_test} is an Isogram")
