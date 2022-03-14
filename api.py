from flask import Flask
import pandas as pd
import numpy as np
import yfinance as yf
import json 


app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask nic! hfsajhfjd'

@app.route('/a/<ticker>')
def getinfo(ticker):
    data = yf.Ticker(ticker)
    return json.dumps(data.info)




    

app.run(host='0.0.0.0', port=81)