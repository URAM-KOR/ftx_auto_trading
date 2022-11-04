from flask import Flask,blueprints
#Blueprint
from routes import main_route,market_view_route

app = Flask(__name__)

app.register_blueprint(main_route.index)
app.register_blueprint(market_view_route.market)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)