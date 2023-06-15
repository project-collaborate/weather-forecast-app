from Geo import Geo
from Current import CurrentWeather

req = Geo()
req2 = CurrentWeather(req.coord)
print(req.coord)
print(req2.current_weather())
