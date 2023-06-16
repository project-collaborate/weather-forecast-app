from Framework import Framework


class Geo(Framework):
    def __init__(self):
        super().__init__()
        self._result_prob = 0
        self._user_request = input("Choose a location.\n")
        self._url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.user_request}&limit=5&appid=715c3bcddc3796ecec3432f8e4554454"
        self.coord = self.coordinates(self.request())

    @property
    def result_prob(self):
        return self._result_prob
    
    @property
    def user_request(self):
        return self._user_request
    
    @property
    def url(self):
        return self._url
    
    def coordinates(self, data):
        return [data[self.result_prob].get('lat'), data[self.result_prob].get('lon')]
