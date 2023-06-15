import requests


class Framework:

    def __init__(self):
        self.url = "null"
        self.user_request = "null"

    def request(self):
        response = requests.get(self.url)
        data = response.json()
        return data
