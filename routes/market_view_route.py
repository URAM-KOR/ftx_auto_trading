from flask import Blueprint, render_template

from infrastructure import market_view_render, usd_fetch_ohlcv

market = Blueprint('market', __name__, url_prefix='/')

@market.route('/market')
def market_route():
    perp_dict = usd_fetch_ohlcv.fetch_ohlcv()
    return render_template(market_view_render.market_view(), perp_dict = perp_dict)