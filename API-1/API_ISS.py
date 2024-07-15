import json
import turtle
import urllib.request
import time
import webbrowser
# import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# print(result)

file = open("iss.txt","w")
file.write(
    "There are currently " + str(result["number"]) +
    " astronauts on the ISS: \n\n"
)

people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

