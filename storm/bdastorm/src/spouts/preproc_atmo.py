# -*- coding: utf-8 -*-
import logging
import json
import time
from random import randint
from streamparse.spout import Spout
from kafka import KafkaClient, SimpleConsumer
from utils.network import NetworkWriter

class PreProcAtmoSpout(Spout):
    outputs = ['json']

    def initialize(self, stormconf, context):
        self.nwriter = NetworkWriter()
        # self.consumer = KafkaConsumer('grp-9-atmo-in', group_id=None, bootstrap_servers=['192.168.76.137:9092'], consumer_timeout_ms=10)
        self.kafka = KafkaClient('192.168.76.137:9092')
        self.consumer = SimpleConsumer(self.kafka, None, "grp-9-atmo-in")

    def next_tuple(self):
        try:
            message = self.consumer.consume(block=False)
            if message is not None:
                self.emit([message.value])
            #for msgCons in self.consumer:
            #    self.emit([msgCons.message.value])
            #message = self.consumer.get_message(block=False)
            #self.nwriter.write(message)
            #self.emit([message.value])
        except:
            pass

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
