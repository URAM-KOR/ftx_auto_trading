import infrastructure.my_login as my_login

import applications.position as position

import database.entities as entities

def usd_position():
    c = my_login.my_login()
    total_position = position.coin_positions(c,'info')
    positions = [total_position[coin]['info'] for coin in range(len(total_position)) if total_position[coin]['info']['cost']!='0.0']
    return positions