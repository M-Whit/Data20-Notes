import csv
#--------------------------MY WORK------------------------------------
# def open_and_print_csv_file(file):
#     try:
#         with open(file) as file:
#             readCSV = csv.reader(file, delimiter=',')
#             for row in readCSV:
#                 print(row)
#     except FileNotFoundError:
#         print("File Not Found!")
#
# def first_name_last_name_email(file):
#     try:
#         with open(file) as file:
#             readCSV = csv.reader(file, delimiter=',')
#             first_names = []
#             last_names = []
#             emails = []
#             for row in readCSV:
#                 first_name = row[1]
#                 last_name = row[2]
#                 email = row[4]
#
#                 first_names.append(first_name)
#                 last_names.append(last_name)
#                 emails.append(email)
#             print(first_names)
#             print(last_names)
#             print(emails)
#
#     except FileNotFoundError:
#         print("File Not Found!")
#
#
# open_and_print_csv_file("user_details.csv")
# first_name_last_name_email("user_details.csv") # Find out how to add this to a new CSV file!

#------------PAULA'S SOLUTION---------------------------------
# Reads and transforms the data at once

def transform_user_details(csv_file_name):
    # need a list to append each list to from transformation
    new_user_data = []
    with open(csv_file_name) as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')

        # Use iter() and next() to skip the first row filled with the column headers!
        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[4])
            new_user_data.append(transformation)
    # Returns a list of lists
    return new_user_data


# print(transform_user_details("user_details.csv"))

# Inserts transformed data into a new csv file (as previously defined)
def create_new_details(old_user_data_file="user_details.csv", new_file_name="new_user_details.csv"):
    # Transform using the previous function
    new_user_data = transform_user_details(old_user_data_file)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        # Make sure you use writerows to get multiple rows!
        csv_writer.writerows(new_user_data)


create_new_details()



#---------------PRACTICE--------------------------------

# with open('user_details.csv') as user_details:
#     readCSV = csv.reader(user_details, delimiter=',')
#     # Use these to pull specific data out of the file and store it as a list variable
#     titles = []
#     surnames = []
#
#     # Print each row of the file
#     # for row in readCSV:
#     #     print(row)
#
#     # Creating the list variables
#     for row in readCSV:
#         title = row[0]
#         surname = row[2]
#
#         # Append the lists created in the for loop to the temporary tables from before
#         titles.append(title)
#         surnames.append(surname)
#
#     print(titles)
#     print(surnames)
#
#     # Whose Surname has what Title?
#     whatname = input("Whose title do you want to know? [Enter Surname] ")
#     surnamedex = surnames.index(whatname)
#     title_go_by = titles[surnamedex]
#     print('The surname of', whatname, 'is:', title_go_by)
