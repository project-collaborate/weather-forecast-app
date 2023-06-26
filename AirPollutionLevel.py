from Framework import Framework


class AirPollutionLevel(Framework):
    def __init__(self, coordinates):
        super().__init__()
        self._url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={coordinates[0]}&lon={coordinates[1]}&appid={self.api_key}"
    
    @property
    def url(self):
        return self._url
    
    def return_data(self):
        if self.request().get('list')[0].get("main").get('aqi') == 1:
            return [self.request().get('list')[0].get("main").get('aqi'), "Clear"]
        elif self.request().get('list')[0].get("main").get('aqi') == 2:
            return [self.request().get('list')[0].get("main").get('aqi'), "Good"]
        elif self.request().get('list')[0].get("main").get('aqi') == 3:
            return [self.request().get('list')[0].get("main").get('aqi'), "Moderate"]
        else:
            return [self.request().get('list')[0].get("main").get('aqi'), "Dangerous"]
