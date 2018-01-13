import key
import requests
import json
import pandas as pd

r30min = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BTC&interval=30min&apikey={APIkey}&datatype=json')
rexchange = requests.get(f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={APIkey}')
snapshot30min = json.loads(r30min.text)
BTCtoUSD = json.loads(rexchange.text)

dfBTCtoUSD = pd.io.json.json_normalize(BTCtoUSD)
dfBTC30min = pd.io.json.json_normalize(snapshot30min)