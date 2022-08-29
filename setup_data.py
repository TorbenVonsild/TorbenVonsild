# Setup data 
# 
import pandas as pd
import os.path
import json
import numpy as np
import datetime as dt

# Hent data fra fil:
aktiekurs = pd.read_json("Data/data.json")

# Omgør Data til forholdstal :1.10 = 10 % stigning
udvikling_idag = aktiekurs["Actual_Close"] / aktiekurs["Actual_Open"]-1
udvikling_inat = aktiekurs["Actual_Open"] / aktiekurs["Close"]-1
udvikling_igår = aktiekurs["Close"] / aktiekurs["Open"]-1
udvikling_5dage = aktiekurs["Open"] / aktiekurs["Open"].rolling(5).mean()-1
volume = aktiekurs["Volume"] / aktiekurs["Volume"].rolling(30).mean()-1
high = aktiekurs["High"] / aktiekurs["Close"]-1
low = aktiekurs["Low"] / aktiekurs["Close"]-1
udvikling_inat_i = aktiekurs["Actual_Open_i"] / aktiekurs["Close_i"]-1
udvikling_igår_i = aktiekurs["Close_i"] / aktiekurs["Open_i"]-1
udvikling_5dage_i = aktiekurs["Open_i"] / aktiekurs["Open_i"].rolling(5).mean()-1
volume_i = aktiekurs["Volume_i"] / aktiekurs["Volume_i"].rolling(30).mean()-1

navne=["udvikling_idag","udvikling_inat","udvikling_igår", "udvikling_5dage", "volume", "high", "low", "udvikling_inat_i", "udvikling_5dage_i", "volume_i"]
#aktieudvikling=[udvikling_idag,udvikling_inat,udvikling_igår, udvikling_5dage, volume, high, low, udvikling_inat_i, udvikling_5dage_i, volume_i]

# Navngiv og samle dataset
aktieudvikling = pd.DataFrame(udvikling_idag , columns=["udvikling_idag"])
aktieudvikling['udvikling_inat'] = udvikling_inat #0.092
aktieudvikling['udvikling_inat_i'] = udvikling_inat_i #0.081
aktieudvikling['volume'] = volume #0.046
aktieudvikling['udvikling_5dage'] = udvikling_5dage #0.036
aktieudvikling['volume_i'] = volume_i #0.033
aktieudvikling['low'] = low #-0.032
aktieudvikling['high'] = high #-0.022

#aktieudvikling['udvikling_igår'] = udvikling_igår #0.016
#aktieudvikling['udvikling_igår_i'] = udvikling_igår_i #-0.003
#aktieudvikling['udvikling_5dage_i'] = udvikling_5dage_i #0.007


#Fjern linier med manglende data samt linijer hvor der ikke er en dag før. Lidt kompleks, men jeg kunne ikke finde bedre
aktieudvikling = aktieudvikling.dropna()
df = aktieudvikling.reset_index()
df1 = df["index"].shift(1)
df1 = pd.DataFrame(df1 , columns=["index"])
df1["index"] = df1["index"] + pd.Timedelta(days=1)
df["index2"] = df1["index"]
df.drop(df[df['index'] != df['index2']].index, inplace = True)
del df["index"]
del df["index2"]
aktieudvikling = df

print (aktieudvikling)
#Gem aktieudvikling
aktieudvikling.to_json("data/aktieudvikling.json")
