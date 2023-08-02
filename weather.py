import requests
API_KEY = "9b45401a22246d410c2c3a1510f9fea4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

"""
API has changed requiring us to feth the langitude and the longitude of the city and passing it through.
This requires us to use a second API to assist which allows us to retrieve the longitude and latitude of the
city inputted by the user.

"""
lat,lon = '',''
geoloc_URL = "http://api.openweathermap.org/geo/1.0/direct"
city = input("Enter a main city:")

# Customize the geoloc API link to satisfy format requirements
getCoord = f"{geoloc_URL}?q={city}&limit=1&appid={API_KEY}"

# get the results and display it in JSON format
result = requests.get(getCoord)
info = result.json()

# Iterate over the values retrieved by JSON to extract the Latitude and Longitude
for x in range(0,1):
    element = info[x]
    for key in element:
        if key == 'lat':
            lat = element[key]
        if key == 'lon':
            lon = element[key]

# Formatting the URL to call the weather API using the Lat and Lon retrieved from the first API call. 
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

data = response.json()

# Get the weather information from the JSON list
weather = data['weather'][0]['description']
print(weather)

# Get the temp information from the JSON list. Returns in Kelvin have to convert to degrees. celsius. 
temp = round(data['main']['temp'] - 273.15, 1)
print(temp)


