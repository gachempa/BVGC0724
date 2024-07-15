# from here: https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/

import requests
import json

def get_stock_data():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        return None

stock_prices = {}
price = get_stock_data()
symbol = "IBM"
# symbol = 
if price:
    stock_prices[symbol] = price

print(f"{symbol}: {price}")