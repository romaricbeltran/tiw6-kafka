# -*- coding: utf-8 -*-
from streamparse import Bolt
import socket
from utils.network import NetworkWriter


class NothingBold(Bolt):
    outputs = ["json"]

    def process(self, tuple):
        jsonData = tuple.values[0]  # premier composant du tuple
        self.emit([jsonData], anchors=[tuple])


class ExitBolt(Bolt):
    outputs = ["json"]

    def initialize(self, storm_conf, context):
        self.nwriter = NetworkWriter()

    def process(self, tuple):
        self.nwriter.write(tuple.values[0])
        # self.ack(tuple)

