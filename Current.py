from Framework import Framework


class CurrentWeather(Framework):
    def __init__(self, coordinates):
        super().__init__()
        self._url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={self.api_key}"
    
    @property
    def url(self):
        return self._url
    
    def return_data(self):
        # return self.request().get('weather')[0]
        return self.request()
