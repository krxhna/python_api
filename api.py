from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping/<ticker>', methods=['GET'])
def ping_pong(ticker):
    msft = yf.Ticker(ticker)
    return jsonify(msft.info)


if __name__ == '__main__':
    app.run()