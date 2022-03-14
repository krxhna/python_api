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
@app.route('/ping', methods=['GET'])
def ping_pong():
    msft = yf.Ticker("AAPL")
    return jsonify(msft.info)


if __name__ == '__main__':
    app.run()