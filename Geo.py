from Framework import Framework


class Geo(Framework):
    def __init__(self):
        super().__init__()
        self.result_prob = 0
        self.user_request = input("Choose a location.\n")
        self._url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.user_request}&limit=5&appid={self.api_key}"
        self.coord = self.coordinates(self.request())

    @property
    def url(self):
        return self._url

    def coordinates(self, data):
        return [data[self.result_prob].get('lat'), data[self.result_prob].get('lon')]
