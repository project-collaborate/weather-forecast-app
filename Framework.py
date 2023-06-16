import requests


class Framework:

    def __init__(self):
        self._url = None

    @property
    def url(self):
        return self._url

    def request(self):
        return requests.get(self.url).json()

    def return_data(self):
        pass
