# -*- coding: utf-8 -*-
from streamparse import Bolt
import socket
import logging


class NetworkWriter:
    """Utility class to send data to the monitor"""

    def __init__(self, host=None, port=None):
        self.host = host if host is not None else "localhost"
        self.port = port if port is not None else 12345
        self.socket = None

    def _openSocketIfNeeded(self):
        if self.socket is None:
            try:
                address = (self.host, self.port)
                self.socket = socket.create_connection(address)
            except:
                logging.error("Connection to monitor failed")

    def write(self, data):
        self._openSocketIfNeeded()
        if self.socket is not None:
            try:
                self.socket.sendall(bytes(str(data) + "\n","utf-8"))
            except:
                logging.error("Error while sending data to monitor")
                try:
                    self.socket.close()
                except:
                    logging.error("Could not close monitor socket after previous error")
                finally:
                    self.socket = None

    def close(self):
        if self.socket is not None:
            try:
                self.socket.close()
            except:
                logging.error("Could not close monitor socket")
            finally:
                self.socket = None


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

