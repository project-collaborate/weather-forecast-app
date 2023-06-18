import requests
import json


class Framework:

    def __init__(self):
        self._url = None
        self.__api_key = self.__get_api_key()

    @property
    def url(self):
        return self._url
    
    def __get_api_key(self):
        """Gets the API key from the config file."""
        with open("config.json") as config_file:
            config = json.load(config_file)
        return config.get("api_key", "")
    
    @property
    def api_key(self):
        return self.__api_key

    def request(self):
        """Gets(request) the Data from the API."""
        return requests.get(self.url).json()

    def return_data(self):
        pass
