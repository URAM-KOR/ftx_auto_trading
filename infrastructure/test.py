import json
import requests

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

cg.ping()

coin_list = cg.get_coins_markets('usd')
print(coin_list)