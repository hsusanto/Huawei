import sys
import os
import json
import socket
import time
from time import sleep
from threading import Thread

output = []
arrayLinkUtil = []
ArrayTime = []
numbOfPkt_Array = []
myResult = []
myP = [2]


directory = "data/"
pktSize = 1500  #bytes


def mytest(inputFile,outputFile,expType) :
        
    #replace with inputFile
    with open(inputFile) as data_file :
        data = json.load(data_file)
        #print(data)
        for line  in data:
            arrayLinkUtil.append(line["RX"])
            ArrayTime.append(line["Time"])

    data_file.close()

    totalUtil = 0; 
    i = 0
    while (i < len(arrayLinkUtil)-1):
        
        numbOfPkt = arrayLinkUtil[i+1] - arrayLinkUtil[i] 
        inBite = numbOfPkt * 1500 * 8;

        timeInterval = ArrayTime[i+1] - ArrayTime[i]

        linkUtil = inBite / timeInterval
        avgLinkUtil = linkUtil
        
        #totalUtil = totalUtil + linkUtil
        myP = [ArrayTime[i+1], avgLinkUtil]
        myResult.append(myP)

        i += 1

        
    outputFile = directory + outputFile 
    with open(outputFile, 'w') as outFile:

        myType = "ECMP"
        output.append({"name": myType,"data": myResult})
        #output.append({"name":"ECMP","data": myResult})
        json.dump(output, outFile)

    outFile.close()

#end mytets

#mytest("mr20load40/Host1/link_log.json","host1.json","ECMP");
#mytest("mr20load40/Host2/link_log.json","host2.json","ECMP");
#mytest("mr20load40/Host3/link_log.json","host3.json","ECMP");
mytest("mr20load40/Host4/link_log.json","host4.json","ECMP");
