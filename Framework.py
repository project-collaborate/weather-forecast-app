import requests


class Framework:

    def __init__(self):
        self.url = None

    def request(self):
        data = requests.get(self.url).json()
        return data

    def return_data(self):
        pass
