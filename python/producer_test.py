#!/usr/bin/python

from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
import os

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
        producer.send_messages("grp-9-atmo-in", line)

def main(args):
    kafka = KafkaClient('192.168.76.137:9092')
    producer = SimpleProducer(kafka, async =True)

    for path in args[1:]:
        files = getInput(path)
        for filename in files:
            print("File: ", filename)
            f = open(filename, "r")
            sendCSVFile(producer, f)
            seenFiles = True
        
    kafka.close()

    return

main(sys.argv)