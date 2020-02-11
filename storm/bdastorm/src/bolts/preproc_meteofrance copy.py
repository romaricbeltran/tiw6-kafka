# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from utils.network import NetworkWriter
import pandas as pd
from datetime import date

class PreProcBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        today = date.today()
        # YYmmdd
        UTC = "00"
        d1 = today.strftime("%Y%m%d")
        file = pd.read_csv('../archive_meteo/'+d1+UTC+'lyon.txt')
        fileinteret = file[["numer_sta","date","pmer","ff","t","u","vv"]].to_csv(index=False)
        self.emit([fileinteret], anchors=[tuple])

class ExitBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        self.kafka = KafkaClient('192.168.76.137:9092')
        self.producer = SimpleProducer(self.kafka, async =True)
                         
    def process(self, tuple):
        # Send to the monitor
        self.nwriter.write(tuple.values[0])
        
          # Send through kafka
        self.producer.send_messages('grp-9-meteo-out', tuple.values[0].encode('utf-8'))



