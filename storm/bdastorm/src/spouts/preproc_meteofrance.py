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
        self.consumer = SimpleConsumer(self.kafka, None, "grp-9-meteo")

    def next_tuple(self):
        for msgCons in self.consumer:
            if msgCons is not None:
                self.emit([msgCons.message.value])
        #message = self.consumer.consume(block=False)
        #if message is not None:
        #    self.emit([message.value])

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
