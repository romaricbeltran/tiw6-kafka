import pandas as pd
import re
import numpy as np
import requests
import urllib.request
import time
from datetime import date
import json

today = date.today()
d1 = today.strftime("%Y%m%d")
datatmo='http://api.atmo-aura.fr/communes/69381/vigilances?date=now&&api_token=ac33ef51d0007489b798fc09244ccb73'
nomfichier=d1+'dataatmo.json'
datas=urllib.request.urlretrieve(datatmo, '../hist_data_atmo/'+ nomfichier) #On enregistre le json complet du jour dans le dossier hist_data_atmo
datajson=pd.DataFrame(pd.read_json('../hist_data_atmo/'+ nomfichier, typ='series')).T #On en fait un dataframe
datajson["date"]=d1
datajson=datajson.drop(['licence','commune','code_insee','id_com'], axis=1)
if datajson["vigilances"][0]==None:
    datajson["vigilances"][0]="pas_de_vigilance"
datajson.to_csv('../data_atmo/'+d1+'atmo.csv', index=None) #On sauvegarde le dataframe avec les vars d'interet dans le dossier data_atmo