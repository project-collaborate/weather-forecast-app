from Geo import Geo
from Current import CurrentWeather
from AirPollutionLevel import AirPollutionLevel
from FourDaysForecast import FourDaysForecast

req = Geo()
req2 = CurrentWeather(req.coord)
req3 = AirPollutionLevel(req.coord)
req4 = FourDaysForecast(req.coord)
print(req.coord)
print(req2.return_data())
print(req3.return_data())
print(req4.return_data())
