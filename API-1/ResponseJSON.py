# https://www.geeksforgeeks.org/response-json-python-requests/

import requests
import json

response = requests.get('https://api.github.com')

API_Data = response.json()

# for key in API_Data:
#     print(key,":", API_Data[key])

print(json.dumps(API_Data,indent=4,sort_keys=True))
