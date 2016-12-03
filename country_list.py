import json

countries = []

with open("woeid.json",mode="r") as file:
	woeid = json.load(file)

for i in range(0,len(woeid)):
	countries.append(woeid[i]['country_name'])

