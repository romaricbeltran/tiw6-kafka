# -*- coding: utf-8 -*-
import logging
import json
import time
from random import randint
from streamparse.spout import Spout
from kafka import KafkaClient, SimpleConsumer

class PreProcMeteoFranceSpout(Spout):
    outputs = ['json']

    def initialize(self, stormconf, context):
        self.kafka = KafkaClient('192.168.76.137:9092')
        self.consumer = SimpleConsumer(self.kafka, None, "grp-9-meteo-in")

    def next_tuple(self):
        try:
            message = self.consumer.consume(block=False)
            if message is not None:
                self.emit([message.value])
        except:
            pass

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
