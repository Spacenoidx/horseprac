import requests

url = "https://api-basketball.p.rapidapi.com/statistics"

querystring = {"season":"2019-2020","league":"12","team":"133"}

headers = {
	"X-RapidAPI-Key": "6650263043msh8f35ace535922fdp192060jsn908ce0c54d18",
	"X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

response