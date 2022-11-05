import infrastructure.my_login as my_login

import database.entities as entities

import heapq
import timeit

# def fetch_markets():
#     c = my_login.my_login()
#     markets = c.fetch_markets()
#
#     perp_list = entities.perp_list
#     perp_dict={perp:format(c.fetch_ticker(perp)['percentage'],'1000.2f') for perp in perp_list if c.fetch_ticker(perp)['percentage']>0}
#     print(heapq.nlargest(10,perp_dict))
#
#     return perp_dict
#

def fetch_perp_markets():
    c = my_login.my_login()
    fetch_market = c.fetch_markets()

    # changeBod, change1h, change24h, volumeUsd24h
    perp_dict={}
    perp_markets={}
    for i in range(len(fetch_market)):
        if 'PERP' in fetch_market[i]['id']:
            info_markets = fetch_market[i]['info']
            perp_markets[info_markets['name']] = {'name': info_markets['name'],
                                                  'changeBod': format(100*float(info_markets['changeBod']),'.2f'),
                                                  'change1h': format(100*float(info_markets['change1h']),'.2f'),
                                                  'change24h': format(100*float(info_markets['change24h']),'.2f'),
                                                  "volumeUsd24h": format(100*float(info_markets['volumeUsd24h']),',')
                                                  }
    for item in sorted(perp_markets, key=lambda k: perp_markets[k]['volumeUsd24h'], reverse=True):
        perp_dict[item]=perp_markets[item]
    return perp_dict.values()