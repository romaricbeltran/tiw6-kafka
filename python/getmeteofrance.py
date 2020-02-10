import wget
from datetime import date
import pandas as pd
import requests
import urllib.request
today = date.today()
# YYmmdd
UTC = "00"
d1 = today.strftime("%Y%m%d")
print("d1 =", d1)
url = 'https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/synop.'+d1+UTC+'.csv'
#      https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/synop.2020020406.csv
urllib.request.urlretrieve(url,"../hist_data_meteo_france/"+'synop.'+d1+UTC+'.csv')
file = pd.read_csv('../hist_data_meteo_france/synop.'+d1+UTC+'.csv',sep=';')
ligneutile = file[file['numer_sta']==7481].to_csv(index=False)
with open("../data_meteo_france/" + d1 + UTC + "lyon.csv","w") as f: 
    f.write(ligneutile)
