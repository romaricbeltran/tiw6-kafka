# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from utils.network import NetworkWriter
import pandas as pd
from datetime import date

class PreProcMeteoBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        file = pd.DataFrame(jsonData) 
        fileinteret = file[["numer_sta","date","pmer","ff","t","u","vv"]]
        self.emit([fileinteret], anchors=[tuple])

class SaveFileMeteoBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        
    def process(self, tuple):
        # Send to the monitor
        #self.nwriter.write(tuple.values[0])
        UTC = "00"
        today = date.today()
        d1 = today.strftime("%Y%m%d")
        tuple.values[0].to_csv('archive_meteo/select'+d1+UTC+'lyon.csv', index=False)

        


