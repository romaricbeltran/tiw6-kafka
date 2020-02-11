# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from utils.network import NetworkWriter

class PreProcTrafficBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json", "alert"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        self.emit([jsonData, jsonData], anchors=[tuple])

class SaveFileTrafficBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        
    def process(self, tuple):
        # Send to the monitor
        self.nwriter.write(tuple.values[1])
        
        


