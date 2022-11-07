import infrastructure.my_login as my_login

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
                                                  "volumeUsd24h": f"{float(info_markets['volumeUsd24h']):.0f}"
                                                  }
    for item in sorted(perp_markets, key=lambda k: float(perp_markets[k]['volumeUsd24h']), reverse=True):
        perp_dict[item]=perp_markets[item]
    perp_dict=list(perp_dict.values())[:10]
    return perp_dict