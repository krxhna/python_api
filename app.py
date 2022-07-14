from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf


# configuration


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/info/<ticker>', methods=['GET'])
def info(ticker):
    msft = yf.Ticker(ticker)
    return jsonify(msft.info)


@app.route('/finance/<ticker>', methods=['GET'])
def get_finance(ticker):
    object = yf.Ticker(ticker)
    #gwttng the finance thing
    finance = object.financials
    #transposing
    finance_t = finance.transpose()
    #repalce nuil
    finance_t = finance_t.fillna(0).rename(columns=str.lower)
    #remove space
    finance_t.columns = finance_t.columns.str.replace(' ','_')


    #picking up the first row 
    res = finance_t.iloc[0].to_dict()
    return jsonify(res)

    



@app.route('/hello', methods=['GET'])
def hello():
    return jsonify("hola")

























if __name__ == '__main__':
    app.run(debug=True)