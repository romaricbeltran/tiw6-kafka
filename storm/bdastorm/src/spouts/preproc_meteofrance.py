# -*- coding: utf-8 -*-
import logging
import json
import time
from random import randint
from streamparse.spout import Spout
from kafka import KafkaClient, SimpleConsumer
from kafka.common import OffsetType

class PreProcMeteoFranceSpout(Spout):
    outputs = ['json']

    def initialize(self, stormconf, context):
        self.kafka = KafkaClient('192.168.76.137:9092')
        #self.consumer = SimpleConsumer(self.kafka, None, "grp-9-meteo")
        self.topic = self.kafka.topics['grp-9-meteo']
        self.consumer = self.topic.get_simple_consumer(
            consumer_group=None,
            auto_offset_reset=OffsetType.EARLIEST,
            consumer_timeout_ms=1000,
            reset_offset_on_start=False
        )

    def next_tuple(self):
        for message in self.consumer:
            if message is not None:
                self.emit([message.value])
        #message = self.consumer.consume(block=False)
        #if message is not None:
        #    self.emit([message.value])

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
