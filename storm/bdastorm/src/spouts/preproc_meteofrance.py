# -*- coding: utf-8 -*-
import logging
import json
import time
from random import randint
from streamparse.spout import Spout
from pykafka import KafkaClient
from pykafka.common import OffsetType

class PreProcMeteoFranceSpout(Spout):
    outputs = ['json']

    def initialize(self, stormconf, context):
        self.client = KafkaClient('192.168.76.137:9092')
        self.topic = self.client.topics['grp-9-meteo_1']
        self.consumer = self.topic.get_simple_consumer(
            auto_offset_reset=OffsetType.EARLIEST,
            consumer_timeout_ms=1000,
            reset_offset_on_start=False)

    def next_tuple(self):
        #message = self.consumer.consume(block=False)
        for message in self.consumer:
            if message is not None:
                self.emit([message.value])

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
