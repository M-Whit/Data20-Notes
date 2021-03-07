from .config_manager import *
from .models.single_postcodes_model import SinglePCModel
import requests


class SinglePC:

    def __init__(self, single_post_code):
        self.url = base_url() + f"postcodes/{single_post_code}"
        # self.requests gets ALL information stored within self.url
        self.request = requests.get(self.url)
        # We can then get the headers of the request (not the data!) as well as the json response
        self.header_details = self.request.headers
        self.response_json = self.request.json()

    # Pass in json response into SinglePCModel and return everything
    def response_data(self):
        return SinglePCModel(self.response_json)


