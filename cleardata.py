# Fjern data med fejl og kombiner
import pandas as pd
import os
import json
import matplotlib.pyplot as plt
import numpy as np

#Vælg aktie
aktieindex="omxc25"
aktienavn="DANSKE.CO"

#Hent fra bibliotek
DATA_PATH = "Data/" + aktienavn + ".json"
aktiekurs = pd.read_json(DATA_PATH)
DATA_PATH = "Data/" + aktieindex + ".json"
indexkurs = pd.read_json(DATA_PATH)

#Fjern linjer med fejl samt Adj Close
aktiekurs.index.name='Date'
indexkurs.index.name='Date'
aktiekurs=aktiekurs.dropna(how='all')
indexkurs=indexkurs.dropna(how='all')
del indexkurs["Adj Close"]
del aktiekurs["Adj Close"]

#Læg data sammen med udgangspunkt i dato(Date)
indexkurs = indexkurs.rename(columns = {"Open":"Open_i", "High":"High_i", "Low":"Low_i", "Close":"Close_i", "Volume":"Volume_i"})
aktiekurs = pd.merge_asof(indexkurs, aktiekurs, on="Date")
aktiekurs = aktiekurs.set_index('Date')

# Ensure we know the actual closing price
data = aktiekurs[["Open", "Open_i", "Close"]]
data = data.rename(columns = {'Open':'Actual_Open',"Open_i":"Actual_Open_i", "Close":"Actual_Close"})

# Shift stock prices forward one day, so we're predicting tomorrow's stock prices from today's prices.
aktiekurs = aktiekurs.shift(1)

# Create our collected data
yesterday = ["Close", "Volume", "Open", "High", "Low", "Open_i", "High_i", "Low_i", "Close_i", "Volume_i"]

aktiekurs = data.join(aktiekurs[yesterday]).iloc[1:]

# Save file to json in case we need it later.
aktiekurs.to_json("data/data.json")