# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from datetime import date
from utils.network import NetworkWriter

class PreProcAtmoBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        #data = df.D
        #datajson["date"]=d1
        #datajson=datajson.drop(['licence','commune','code_insee','id_com'], axis=1)
        #if datajson["vigilances"][0]==None:
        #    datajson["vigilances"][0]="pas_de_vigilance"
        #datajson=datajson
        self.emit([jsonData], anchors=[tuple])

class SaveFileAtmoBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        
    def process(self, tuple):
        # Send to the monitor
        self.nwriter.write(tuple.values[0])
        today = date.today()
        d1 = today.strftime("%Y%m%d")

        filename = 'archive_atmo/'+d1+'atmo.csv'

        exec("import subprocess\nsubprocess.run(['hdfs', 'dfs', '-mkdir', 'archive_atmo'])\nsubprocess.run(['echo', '\""+ str(tuple.values[0]) +"\"', '|', 'hdfs', 'dfs', '-appendToFile', '-', '"+ filename +"'])")  



