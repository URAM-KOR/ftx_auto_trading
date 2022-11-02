def open_orders(c, str):
    str_orders = c.fetch_open_orders()
    return str_orders