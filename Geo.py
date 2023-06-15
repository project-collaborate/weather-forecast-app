from Framework import Framework


class Geo(Framework):
    def __init__(self):
        super().__init__()
        self.result_prob = 0
        self.user_request = input("Insert the city name")
        self.url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.user_request}&limit=5&appid=715c3bcddc3796ecec3432f8e4554454"
        self.data = Framework.request(self)
        self.coord = self.coordinates(self.data)

    def coordinates(self, data):
        return [data[self.result_prob].get('lat'), data[self.result_prob].get('lon')]
