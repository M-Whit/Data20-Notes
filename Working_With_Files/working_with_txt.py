def open_and_print_file(file):
    try:
        # Typically, when we use open on its own, we need to close() as well
        opened_file = open(file, "r")
        # Using .read() will get rid of the '\n' for future reference!
        file_line_list = opened_file.readlines()

        print(file_line_list)

        # Iterate through list and print items individually
        # Get rid of \n

        for x in file_line_list:
            # Cannot use .rstrip() on file_line_list because it is a list! Have to strip each item (x) individually
            x = x.rstrip("\n")
            print(x)

        # We close the file so that we can then move the file around later on
        opened_file.close()

    except FileNotFoundError as msg:
        print("There is an error!")
        print(msg)

    finally:
        print("\nExecution Complete")


def writing_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + "\n")

    except FileNotFoundError:
        print("File Not Found!")


writing_to_file("chips.txt", "chips")
open_and_print_file("chips.txt")

# "r" - Default mode. Opens the file for reading.
# "w" - Opens the file for writing. If file does not exists, creates a new file. Truncates existing files.
# "x" - Creates a new file. If file already exists, operation fails.
# "a" - Open file in append mode. If file does not exist, creates a new file.
# "t" - Default mode. Opens in text mode.
# "b" - Opens in binary mode.
# "+" - Opens a file for reading and writing (updating).
