import asyncio
import aiohttp
import requests
import os 
import time

from dotenv import load_dotenv

load_dotenv()


## Getting API Key
api_key = os.getenv('ALPHAVANTAGE_API_KEY')

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'


symbols = ['AAPL','GOOG','TSLA','MSFT','AAPL']
results = []



## Working

# def get_tasks(session):
#     tasks=[]

#     for symbol in symbols:
#         tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    
#     return tasks


def run_tasks():
    for symbol in symbols:
        print(f"Hitting for {symbol}")
        response = requests.get(url.format(symbol,api_key))
        results.append(response.json)


print("Time Started...")
start = time.time()
run_tasks()
end = time.time()


total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))