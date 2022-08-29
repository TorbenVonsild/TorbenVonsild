import yfinance as yf
import pandas as pd
import os.path
import json
import matplotlib.pyplot as plt
import numpy as np

# Find dataperiode
from datetime import date 
today = date.today()
print("Today's date:", today)

startdato = "2015-01-01"
slutdato = today


# Hent OMXC25
DATA_PATH = "Data/omxc25.json"
omxc25 = yf.download("^OMXC25", start=startdato, end=slutdato)
# Save file to json in case we need it later.  
omxc25.to_json(DATA_PATH)

# Vælg aktie
aktienavn = "DANSKE.CO"
DATA_PATH = "Data/" + aktienavn + ".json"

# Hent aktie
aktiekurs = yf.download(aktienavn, start=startdato, end=slutdato)
# Save file to json in case we need it later.
aktiekurs.to_json(DATA_PATH)

print (aktienavn)
print (aktiekurs)
print (omxc25)
