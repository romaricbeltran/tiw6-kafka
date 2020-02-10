# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import KafkaProducer
import socket
from utils.network import NetworkWriter

class AlertBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        self.emit([jsonData], anchors=[tuple])

class ExitBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092']) #,
                         # value_serializer=lambda x: dumps(x).encode('utf-8'))
                         

    def process(self, tuple):
        # Send to the monitor
        self.nwriter.write(tuple.values[0])
        
        # Send through kafka
        self.producer.send('out_test', value=tuple.values[0])


