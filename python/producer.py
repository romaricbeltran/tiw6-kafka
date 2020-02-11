#!/usr/bin/python

from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
import os
from datetime import date

def getInput(inputPath):
    files = []
    if os.path.isfile(inputPath) and inputPath.endswith(".csv"):
        files.append(inputPath)
    elif os.path.isdir(inputPath):
        for inputFile in os.listdir(inputPath):
            if fnmatch.fnmatch(inputFile, '*.csv'):
                files.append(inputPath+inputFile)
    return files

def sendCSVFile(producer, f):
    for line in f:
        producer.send_messages("grp-9-trafic_1", line.encode('utf-8'))

def main(args):
    kafka = KafkaClient('192.168.76.137:9092')
    producer = SimpleProducer(kafka, async =True)

    for path in args:
        files = getInput(path)
        for filename in files:
            print("File: ", filename)
            f = open(filename, "r")
            sendCSVFile(producer, f)
            seenFiles = True
        
    kafka.close()

    return

# main(sys.argv)
# main(list_data_path)