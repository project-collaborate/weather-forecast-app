from Framework import Framework


class Geo(Framework):
    def __init__(self, city_name):
        super().__init__()
        self._result_prob = 0
        self._user_request = city_name
        self._url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.user_request}&limit=5&appid={self.api_key}"
        self._coord = self.coordinates(self.request())

    @property
    def result_prob(self):
        return self._result_prob
    
    @property
    def user_request(self):
        return self._user_request
    
    @property
    def url(self):
        return self._url
    
    @property
    def coord(self):
        return self._coord
    
    def coordinates(self, data):
        """Gets the Latitude and Longitude of a given city."""
        return [data[self.result_prob].get('lat'), data[self.result_prob].get('lon')]
