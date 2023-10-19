# Importing necessary modules.

import requests

# Preparing for API request.

url = "https://api.wmata.com/Rail.svc/json/jStations"
querystring = {"LineCode": "RD"}
headers = {"api_key": "3ceb0f2d46344b8cbff8cc5eb40ea1bd"}

# Making request for JSON.

response = requests.get(url, headers=headers)

# Since the response consists of an array named "Stations", defining our work list as such.
stationlist = response.json()["Stations"]

# Ask the user what city they are in.
user_city = input("What city are you in?")

print(f"The following stations are in {user_city}:")

# Begin counting stations in the city.
count = 0

for station in stationlist:
    if station["Address"]["City"] == user_city:
        print(station["Name"])
        count += 1

print(f"There are {count} WMATA Metro stations in this city. ")
