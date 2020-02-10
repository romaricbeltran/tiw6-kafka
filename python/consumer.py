#!/usr/bin/python

from kafka import SimpleConsumer, SimpleClient
from kafka import KafkaConsumer
from kafka import KafkaClient
import argparse
import logging
import os

group_name = None
topic_name = "grp-9-atmo"
path = os.path.abspath('../kafka_example/message')

print "Consumer pour le groupe: [%s] et le topic: [%s]" % (group_name, topic_name)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Consume messages from Kafka",
        epilog="Example Usage: "
               "python consumer.py -c, "
               "python consumer.py -f [file-path]")

    parser.add_argument("-c", "--screen_output",
                        dest="screen_output",
                        action="store_true",
                        help="Ecrire dans la console")

    parser.add_argument("-f", "--file",
                        dest="file",
                        action="store_true",
                        help="Ecrire dans un fichier")

    return parser.parse_args()


def write_messages(dest):
    args = parse_arguments()
    kafka = KafkaClient('192.168.76.137:9092')
    consumer = SimpleConsumer(kafka, group_name, topic_name)
    for msgCons in consumer:
        # Ecrire dans la console
        if dest is args.screen_output:
            print(msgCons.message.value)

        # Ecrire dans un fichier
        if dest is args.file:
            write_to_file(msgCons.message.value)

def write_to_file(msg):
    if not msg:
        return
    with open(path, "a+") as fp:
        fp.write("\n" + msg)


def main():
    args = parse_arguments()
    if args.screen_output:
        write_messages(args.screen_output)

    if args.file:
        write_messages(args.file)

    kafka.close()

main()