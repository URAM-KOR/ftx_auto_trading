import ccxt

def login(YOUR_API_KEY,API_SECRET):

    client = ccxt.ftx({
        'apiKey': YOUR_API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
        'options':{
            'defaultType':'future',
        },
          })

    return client