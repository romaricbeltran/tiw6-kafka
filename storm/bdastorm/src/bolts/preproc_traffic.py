# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from utils.network import NetworkWriter
import subprocess

class PreProcTrafficBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        self.emit([jsonData], anchors=[tuple])

class SaveFileTrafficBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        
    def process(self, tuple):
        filename = 'archive_trafic/trafic.csv'

        subprocess.run(['hdfs', 'dfs', '-mkdir', 'archive_trafic'])
        subprocess.Popen('echo "' + tuple.values[0] + '" | hdfs dfs -appendToFile - ' + filename, shell=True)  

        
        


