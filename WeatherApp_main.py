import requests
user_request = input("Choose a location.\n")
url = f"http://api.openweathermap.org/geo/1.0/direct?q={user_request}&limit=5&appid=715c3bcddc3796ecec3432f8e4554454"
response = requests.get(url)
data = response.json()
result_prob = 0
name = data[result_prob].get('name')
coordinates = [data[result_prob].get('lat'), data[result_prob].get('lon')]
print(name)
print(coordinates)
url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid=715c3bcddc3796ecec3432f8e4554454"
response1 = requests.get(url2)
data1 = response1.json()
print(data1)