import pandas as pd
import re
import numpy as np
import requests
import urllib.request
import time
from datetime import date
import json
import os
os.environ["http_proxy"] = "http://proxy.univ-lyon1.fr:3128"

today = date.today()
d1 = today.strftime("%Y-%m-%d")
datatmo='http://api.atmo-aura.fr/communes/69381/vigilances?date=now&&api_token=ac33ef51d0007489b798fc09244ccb73'
nomfichier=d1+'dataatmo.json'
datas=urllib.request.urlretrieve(datatmo, '../hist_data_atmo/'+ nomfichier) #On enregistre le json complet du jour dans le dossier hist_data_atmo
datajson=pd.DataFrame(pd.read_json('../hist_data_atmo/'+ nomfichier, typ='series')).T #On en fait un dataframe
datajson.to_csv('../data_atmo/'+d1+'atmo.csv', index=None)

kafka = KafkaClient('192.168.76.137:9092')
producer = SimpleProducer(kafka, async=True)

f = open('../data_atmo/'+d1+'atmo.csv', "r")
for line in f:
    producer.send_messages("grp-9-atmo-aura", line.encode("utf-8"))

#datajson["date"]=d1
#datajson=datajson.drop(['licence','commune','code_insee','id_com'], axis=1)
#if datajson["vigilances"][0]==None:
#    datajson["vigilances"][0]="pas_de_vigilance"
#datajson=datajson
#datajson.to_csv('../data_atmo/'+d1+'atmo.csv', index=None) #On sauvegarde le dataframe avec les vars d'interet dans le dossier data_atmo. Il est desormais possible re retirer les variables lignes par ligne