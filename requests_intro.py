import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
print(post_codes_req)

# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.content) # bytes array
print(post_codes_req.json()) # dictionary

# put everything into a class
# extract information from JSON file
# grab postcode, country, longitude, latitude, region
# output... somehow
