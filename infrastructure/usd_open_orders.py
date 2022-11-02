import infrastructure.my_login as my_login

import applications.open_orders as open_orders

import database.entities as entities

def usd_orders():
    c = my_login.my_login()
    total_orders = open_orders.open_orders(c,'info')
    print("len(total_orders) = ",len(total_orders),flush=True)
    positions = [total_orders[coin]['info'] for coin in range(len(total_orders))]
    print("positions = ",positions,flush=True)
    return positions