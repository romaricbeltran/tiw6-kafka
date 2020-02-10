import os
import re
from datetime import datetime
import requests
import urllib.request
from lxml import html
import wget
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")#-%H-%M") #Construction de la date du jour : YYYY-MM-DD
print("date du jour: ", dt_string,"\n verification et telechargement des donnees jourlalières manquantes :")
datelist=dt_string.split('-')
url='http://192.168.76.159/data/trafic/'
files=os.listdir('../hist_data_trafic') #On met sous liste tous les fichiers presents dans hist_data_trafic
dirtrafic = requests.get(url)
webpage = html.fromstring(dirtrafic.content)
listserv=webpage.xpath('//a/@href') #On récupere la liste de tous les href de la page internet (xml)
regexdujour=re.compile(dt_string,re.IGNORECASE) #regex pour recuperer les href du jour
nbfichierstelecharges=0
for i in range(len(listserv)):
    if re.search(regexdujour,listserv[i]) and not listserv[i] in files: #Si il y a des fichiers du jour qui ne sont pas dans notre repertoire :
        wget.download(url+listserv[i],out='../hist_data_trafic/') #On les dwnl
        nbfichierstelecharges+=1
print(nbfichierstelecharges,' fichiers telecharges')
