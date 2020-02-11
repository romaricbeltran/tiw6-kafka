# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt
from kafka import SimpleProducer, KafkaClient
import socket
from utils.network import NetworkWriter
import pandas as pd
from datetime import date
import subprocess

class PreProcMeteoBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]
        #file = pd.DataFrame(jsonData) 
        #fileinteret = file[["numer_sta","date","pmer","ff","t","u","vv"]]
        self.emit([jsonData], anchors=[tuple])

class SaveFileMeteoBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()
        #self.fs = pyhdfs.HdfsClient(hosts='192.168.76.137:50070', user_name='p1612598')
        
    def process(self, tuple):
        # Send to the monitor
        #self.nwriter.write(tuple.values[0])
        UTC = "00"
        today = date.today()
        d1 = today.strftime("%Y%m%d")
        #tuple.values[0].to_csv('archive_meteo/select'+d1+UTC+'lyon.csv', index=False)

        #if 'archive_meteo' not in self.fs.listdir('/'):
        #    self.fs.mkdirs('/archive_meteo')

        filename = 'archive_meteo/select'+d1+UTC+'lyon.csv'

        #if not self.fs.exists(filename):
        #    self.fs.create(filename, tuple.values[0])
        #else:
        #    self.fs.append(filename, tuple.values[0])

        subprocess.run(['hdfs', 'dfs', '-mkdir', 'archive_meteo'])
        subprocess.Popen('echo "' + tuple.values[0] + '" | hdfs dfs -appendToFile - ' + filename, shell=True)  
