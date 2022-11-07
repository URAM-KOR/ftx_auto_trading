from flask import Blueprint, render_template

from infrastructure import market_view_render,order_view_render,\
    usd_fetch_markets, order_options

market = Blueprint('market', __name__, url_prefix='/')

@market.route('/market')
def market_route():
    perp_dict = usd_fetch_markets.fetch_perp_markets()
    return render_template(market_view_render.market_view(),
                           perp_dict = perp_dict,
                           symbols = order_options.symbols,
                           positions = order_options.positions,
                           qty = order_options.qty,
                           )


# @market.route('/order/')
# def order_options():
#     symbols = order_options.symbol
#     return render_template(order_view_render.order_view(), symbols = symbols)