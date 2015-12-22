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
myResult = []
myP = [2]


filetypes = ["ECMP", "Algo"]
hadoopTraff = ["20", "40"] 
traffPattern = ["20","40","60"] 
inputFN = "linkUtil"
extenFN = ".json"
directory = "data/"

def mytest(inputFile,outputFile,expType) :

    #print(inputFile)
    print(outputFile)
        
    #replace with inputFile
    with open('test.json') as data_file :
        data = json.load(data_file)
        #print(data)
        for line  in data:
            arrayLinkUtil.append(line["Size"])
            ArrayTime.append(line["EndTime"])

    data_file.close()


    i = 0
    while (i < len(arrayLinkUtil)):
        j = 0
        avgLinkUtil = 0
        while (j <= i):
            avgLinkUtil = avgLinkUtil + arrayLinkUtil[j]
            j +=1

        avgLinkUtil = avgLinkUtil / (i+1)

        myP = [ArrayTime[i],avgLinkUtil]
        #print(myP)
        myResult.append(myP)

        i += 1

    
    outputFile = directory + outputFile 
    #print(outputFile)
    #replace with outputFile
    with open('outputLB.json', 'w') as outFile:

        myType = "ECMP"
        output.append({"name": myType,"data": myResult})
        #output.append({"name":"ECMP","data": myResult})
        json.dump(output, outFile)

    outFile.close()

#end mytets

#hadoopTraff = ["20", "40"]
#traffPattern = ["20","40","60"]
#flowECMP20low.json

def collectFiles():
        
    #print(int(traffPattern[0])+2)

    ft = 0
    while (ft < len(filetypes)): 
    
        ht = 0
        while (ht < len(hadoopTraff)):

            tp = 0
            while (tp < len(traffPattern)):
                
                if (hadoopTraff[ht] == "40" and traffPattern[tp] == "60"): 
                     break

                mytest(filetypes[ft] + hadoopTraff[ht] + traffPattern[tp] + extenFN,
                       inputFN + filetypes[ft] + hadoopTraff[ht] + traffPattern[tp],
                       filetypes[ft])
                tp += 1

            ht +=1

        ft +=1


#mytest("myfile","outputF");






#end  collectFiles

#collectFiles()
mytest("myinput","myinput","ECMP");
