import os
import re
from datetime import datetime
import requests
import urllib.request
from lxml import html
import wget
import xmltodict
import json
import pandas as pd
import producer as prod

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")#-%H-%M") #Construction de la date du jour : YYYY-MM-DD
testdate='2020-02-09'
url='http://192.168.76.159/data/trafic/'
files=os.listdir('../hist_data_trafic') #On met sous liste tous les fichiers presents dans hist_data_trafic
dirtrafic = requests.get(url)
webpage = html.fromstring(dirtrafic.content)
listserv=webpage.xpath('//a/@href') #On recupere la liste de tous les href de la page internet (xml)
regexdujour=re.compile(testdate,re.IGNORECASE) #regex pour recuperer les href du jour
nbfichierstelecharges=0
for i in range(len(listserv)):
    if re.search(regexdujour,listserv[i]) and not listserv[i] in files: #Si il y a des fichiers du jour qui ne sont pas dans notre repertoire :
        wget.download(url+listserv[i],out='../hist_data_trafic/') #On les dwnl
        with open('../hist_data_trafic/'+listserv[i]) as fd:
            doc = xmltodict.parse(fd.read())
        newdic=[dict(od) for od in doc['Etats_Troncons_Web_InfoTrafic']['troncon_web_infotrafic'] ]
        data1=list(filter(lambda dic: dic['id'] == '1108', newdic)) #bvd stalingrad
        data2=list(filter(lambda dic: dic['id'] == '54', newdic)) #avenue 11 novembre
        data3=list(filter(lambda dic: dic['id'] == '2228', newdic)) #avenue Roger Salengro

        listofdicts=[]
        nomderue=[]

        listofdatas=[data1,data2,data3]
        for data in listofdatas:
            if 'point_de_mesure' in data[0]:
                listofdicts.append(dict(data[0]['point_de_mesure']))
                nomderue.append(data[0]['libelle']) 
        testdatas=pd.DataFrame(listofdicts,index=None).T
        testdatas.columns = nomderue
        csv_path = '../data_trafic/' + listserv[i][:-3] + 'csv'
        file_path = []
        file_path.append(csv_path)
        testdatas.to_csv(csv_path)
        prod.main(file_path)
        nbfichierstelecharges+=1
print(nbfichierstelecharges,' fichiers telecharges')
