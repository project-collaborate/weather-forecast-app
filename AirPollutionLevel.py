from Framework import Framework


class AirPollutionLevel(Framework):
    def __init__(self, coordinates):
        super().__init__()
        self.url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={coordinates[0]}&lon={coordinates[1]}&appid=715c3bcddc3796ecec3432f8e4554454"
    

    def return_data(self):
        return self.request().get('list')[0].get("main")