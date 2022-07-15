from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf


# configuration

from pymongo import MongoClient
import pymongo


    # Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://krish:greenlines123@cluster1.7qmda.mongodb.net/test"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/info/<ticker>', methods=['GET'])
def info(ticker):
    ticker = ticker.upper()
    db = client.test
    collection = db.tickers
    #checking if it exsits in the database
    if collection.count_documents({'symbol': ticker}, limit = 1) == 0:
        res = yf.Ticker(ticker)
        return jsonify(res.info) 
    else:
        data= collection.find_one({'symbol': ticker})
        data['_id'] = str(data['_id'])
        data['gmtOffSetMilliseconds'] = str(data['gmtOffSetMilliseconds'])
        return jsonify(data)



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


@app.route('/balancesheet/<ticker>', methods=['GET'])
def get_balancesheet(ticker):
    object = yf.Ticker(ticker)
    #gwttng the finance thing
    finance = object.balance_sheet
    #transposing
    finance_t = finance.transpose()
    #repalce nuil
    finance_t = finance_t.fillna(0).rename(columns=str.lower)
    #remove space
    finance_t.columns = finance_t.columns.str.replace(' ','_')


    #picking up the first row 
    res = finance_t.iloc[0].to_dict()
    return jsonify(
                {
            'symbol': ticker,
            '2021': finance_t.iloc[0].to_dict(),
            '2020': finance_t.iloc[1].to_dict(),
            '2019': finance_t.iloc[2].to_dict(),
            '2018': finance_t.iloc[3].to_dict()
        }
    )
    



@app.route('/hello', methods=['GET'])
def hello():
    return jsonify("hola")

























if __name__ == '__main__':
    app.run(debug=True)