import requests


class Request:
    def __init__(self):
        self.json_file = ""
        self.postcode_info = ''
        self.values = []
        self.pull_items = []

    # Pulling information from url and returning the results of the pull
    def load_results(self):
        pull_from_url = requests.get(self.json_file)
        self.postcode_info = pull_from_url.json().get('result')
        return self.postcode_info

    # Appending to a temporary list the values of the keys we want (country, longitude etc.)
    def obtain_results(self, list):
        temp = self.values
        for x in list:
            temp.append(self.load_results()[x])
        self.values = temp
        return self.values

    # Running the main function, where we determine what we want to find using the above methods
    def main(self, url):
        self.json_file = url
        self.pull_items = ['postcode', 'country', 'longitude', 'latitude', 'region']
        print(self.load_results())
        print(self.obtain_results(self.pull_items))


instance = Request()
instance.main("https://api.postcodes.io/postcodes/se120nb")
