import pandas as pd
import re
import numpy as np
import requests
import urllib.request
import time
from datetime import date
import json
import wget

today = date.today()
d1 = today.strftime("%Y-%m-%d")
datatmo='http://api.atmo-aura.fr/communes/69382/vigilances?api_token=ac33ef51d0007489b798fc09244ccb73'
#'http://api.atmo-aura.fr/communes/69381/vigilances?date=now&&api_token=ac33ef51d0007489b798fc09244ccb73'
nomfichier='alldataatmo.json'
wget.download(datatmo, out='../hist_data_atmo/'+ nomfichier) #On enregistre le json complet du jour dans le dossier hist_data_atmo
file=pd.read_json('../hist_data_atmo/'+ nomfichier, typ='series')
atts=[]
for i in file['vigilances']['data'][0]:
    if i != 'commentaire':
        atts.append(i)
vigi={}
for att in atts:
    vigi[att]=[file['vigilances']['data'][i][att] for i in range(len(file['vigilances']['data']))]
df=pd.DataFrame(vigi)
date = [df['nom_procedure'][i][-4:]+df['nom_procedure'][i][-7:-5]+df['nom_procedure'][i][-10:-8] for i in range(len(df['zone']))]
vigi['dates']=date
data=pd.DataFrame(vigi)
data.to_csv('../data_atmo/archive_atmo.csv',index=False)