# Find korrelation mellem datasæt
# 
import pandas as pd
import numpy as np
import os.path
import json
import math

aktieudvikling = pd.read_json("Data/aktieudvikling.json")

udvikling_inat = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["udvikling_inat"]))
udvikling_igår = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["udvikling_igår"]))
udvikling_5dage = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["udvikling_5dage"]))
volume = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["volume"]))
high = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["high"]))
low = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["low"]))
udvikling_inat_i = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["udvikling_inat_i"]))
udvikling_igår_i = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["udvikling_igår_i"]))
udvikling_5dage_i = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["udvikling_5dage_i"]))
volume_i = (aktieudvikling["udvikling_idag"].corr(aktieudvikling["volume_i"]))

print (aktieudvikling)
print ("Correlation ",udvikling_inat, udvikling_igår, udvikling_5dage, volume, high, low, udvikling_inat_i, udvikling_igår_i, udvikling_5dage_i, volume_i)

# Korrelation
# udvikling_idag  udvikling_inat  udvikling_igår  udvikling_5dage    volume      high       low     udvikling_inat_i   udvikling_igår_i   udvikling_5dage_i    volume_i
#                 0.092164279951  0.01648326453   0.03680804750292   0.0466319  -0.022     -0.032   0.08137764056590  -0.00339303474297   0.007412510578249293 0.033469193014490556