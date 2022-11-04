import infrastructure.my_login as my_login

import database.entities as entities

def fetch_ohlcv():
    c = my_login.my_login()
    markets = c.fetch_markets()

    perp_list = entities.perp_list
    perp_dict={perp:format(c.fetch_ticker(perp)['percentage'],'1000.2f') for perp in perp_list if c.fetch_ticker(perp)['percentage']>0}

    rank_dict=sorted(perp_dict.items(), key = lambda item: item[1], reverse = True)

    return rank_dict[:10]