# -*- coding: utf-8 -*-
import logging
import json
import time
from random import randint
from streamparse.spout import Spout
from kafka import KafkaConsumer

class PreProcMeteoFranceSpout(Spout):
    outputs = ['json']

    def initialize(self, stormconf, context):
        self.consumer = KafkaConsumer('in_test', group_id='my-group', bootstrap_servers=['localhost:9092'], consumer_timeout_ms=10)

    def next_tuple(self):
        try:
            message = self.consumer.next_v1()
            self.emit([message.value])
        except:
            pass

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
