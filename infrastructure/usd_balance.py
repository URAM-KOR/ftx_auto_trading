import infrastructure.my_login as my_login

import applications.balance as balance

import database.entities as entities

def usd_balance():
    c = my_login.my_login()
    return balance.coin_balance(c,'total')