from Framework import Framework


class CurrentWeather(Framework):
    def __init__(self, coordinates):
        super().__init__()
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid=715c3bcddc3796ecec3432f8e4554454"
        self.data = Framework.request(self)

    def current_weather(self):
        return self.data.get('weather')[0]
