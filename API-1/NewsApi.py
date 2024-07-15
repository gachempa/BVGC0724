# from: https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/

import requests
import json

def fetch_and_print_articles(api_url):
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles',[])

        for index, article in enumerate(articles[:3], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")

API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
api_endpoint = url

fetch_and_print_articles(api_endpoint)

def jprint(obj): #this is not used .... hmmm
    print(json.dumps(obj, sort_keys=True, indent=4))


# print(response.status_code)