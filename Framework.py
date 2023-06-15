import requests


class Framework:

    def __init__(self):
        self.url = None

    def request(self):
        response = requests.get(self.url)
        data = response.json()
        return data

    def return_data(self):
        pass
