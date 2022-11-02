def coin_balance(c, str):
    str_balance = c.fetch_balance()
    return str_balance[str]