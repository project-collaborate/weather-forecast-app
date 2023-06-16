from Geo import Geo
from Current import CurrentWeather
from AirPollutionLevel import AirPollutionLevel

req = Geo()
req2 = CurrentWeather(req.coord)
req3 = AirPollutionLevel(req.coord)
print(req.coord)
print(req2.return_data())
print(req3.return_data())
