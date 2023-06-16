from Framework import Framework


class FourDaysForecast(Framework):
    def __init__(self, coordinates):
        super().__init__()
        self._url = f"http://api.openweathermap.org/data/2.5/forecast?lat={coordinates[0]}&lon={coordinates[1]}&appid=715c3bcddc3796ecec3432f8e4554454"

    @property
    def url(self):
        return self._url

    def return_data(self):
        return self.request()