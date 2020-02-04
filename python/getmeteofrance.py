import wget
from datetime import date
import pandas as pd
today = date.today()
# YYmmdd
UTC = "00"
d1 = today.strftime("%Y%m%d")
print("d1 =", d1)
url = 'https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/synop.'+d1+UTC+'.csv'
#      https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/synop.2020020406.csv
print(d1)
wget.download(url)
file = pd.read_csv('synop.'+d1+UTC+'.csv',sep=';')
ligneutile = file[file['numer_sta']==7481].to_csv(index=False)
with open("archive/" + d1 + UTC + "lyon.txt","a") as f:
    f.write(ligneutile)