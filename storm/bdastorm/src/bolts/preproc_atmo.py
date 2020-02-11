# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from utils.network import NetworkWriter

class PreProcBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json", "alert"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        self.emit([jsonData, jsonData], anchors=[tuple])

class ExitBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        self.kafka = KafkaClient('192.168.76.137:9092')
        self.producer = SimpleProducer(self.kafka, async =True)

        #self.producer = KafkaProducer(bootstrap_servers=['192.168.76.137:9092']) #,
                         # value_serializer=lambda x: dumps(x).encode('utf-8'))
                         

    def process(self, tuple):
        # Send to the monitor
        self.nwriter.write(tuple.values[1])
        
        # Send through kafka
        self.producer.send_messages('grp-9-atmo-out', tuple.values[0].encode('utf-8'))


