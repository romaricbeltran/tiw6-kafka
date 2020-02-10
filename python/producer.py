#!/usr/bin/python

from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
import os
from datetime import date

today = date.today()
d1 = today.strftime("%Y-%m-%d")
data_file = "../data_atmo/" + d1 + "atmo.csv"
path_data_file = os.path.abspath(data_file)
list_data_path = []
list_data_path.append(data_file)

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
        producer.send_messages("grp-9-atmo", line)

def main(args):
    kafka = KafkaClient('192.168.76.137:9092')
    producer = SimpleProducer(kafka, async =True)

    for path in args[0:]:
        files = getInput(path)
        for filename in files:
            print("File: ", filename)
            f = open(filename, "r")
            sendCSVFile(producer, f)
            seenFiles = True
        
    kafka.close()

    return

# main(sys.argv)
main(list_data_path)