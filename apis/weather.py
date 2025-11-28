import requests

# We need coordinates to get weather data
latitude = 21.9974  
longitude = 79.0011   

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()
type(data)
data.keys()
data.values()
type(data["current"])
data["timezone"]

print(data)