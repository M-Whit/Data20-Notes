import json

# new_dict = {"name": "apple", "flavour": "tasty"}
#
# print(type(new_dict))
# print(new_dict)
#
# new_json_str = json.dumps(new_dict)
#
# print(type(new_json_str))
# print(new_json_str)

# # creates json file
# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(new_dict, jsonfile)
#
# # opens/loads json files
# with open("new_json_file.json") as jsonfile:
#     fruit = json.load(jsonfile)
#     # REMEMBER HOW TO ACCESS STUFF IN DICTIONARIES!
#     print(fruit['name'])

# new json file with just exchange rates
# countries as keys
# rates as values

with open("exchange_rates.json") as exchange_rates:
    exchange = json.load(exchange_rates)
    print(exchange['rates'])

with open("country_rates.json", "w") as country_rates:
    json.dump(exchange['rates'], country_rates)
