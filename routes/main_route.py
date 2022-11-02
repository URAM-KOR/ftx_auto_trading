from flask import Blueprint, render_template

from infrastructure import index_render, usd_positions, usd_balance,usd_open_orders

index = Blueprint('index', __name__, url_prefix='/')

@index.route('/')
def index_route():
    balance = usd_balance.usd_balance()
    positions = usd_positions.usd_position()
    open_orders = usd_open_orders.usd_orders()
    return render_template(index_render.index_view(), balance=[balance], positions=positions, open_orders=open_orders)