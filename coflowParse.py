import sys
import os
import json


FALSE = -1
output = []

coflowArray = []
coflow = [3]
myResult = []
myP = [2]

directory = "data/"


def mytest(inputFile,outputFile,expType) :

    with open(inputFile) as data_file :

        data = json.load(data_file)
        for line  in data:
                 
            coflowID = line["ID"]
            endTime = line["EndTime"]
            startTime = line["StartTime"]

            coflow = [coflowID, endTime, startTime]
            coflowArray.append(coflow)
    
    data_file.close()

    coflowArray.sort()
    
    CurrCoflow = coflowArray[0][0]
    currStart  = coflowArray[0][1]
    currEnd    = coflowArray[0][2]
    cfCounter  = 1 
    total      = 0
    i = 0

    while (i < len(coflowArray)):

        coflowID = coflowArray[i][0]
        endT   = coflowArray[i][1]
        startT     = coflowArray[i][2]

        if (CurrCoflow == coflowID) :

            if (currStart > startT ) :
                currStart = startT
            
            if (currEnd < endT ):
                currEnd = endT
        
        else :
            CCT = currEnd - currStart  # info from previous coflow in array
            total = total + CCT
            avgCCT = total / cfCounter
            myP = [currEnd , avgCCT]
            myResult.append(myP)

            #processing next coflow
            cfCounter += 1
            currStart = startT
            currEnd = endT

        i += 1
        myResult.sort()

    #print(myResult)
    outputFile = directory + outputFile 
   
    with open(outputFile, 'w') as outFile:

        myType = "ECMP"
        output.append({"name": myType,"data": myResult})
        #output.append({"name":"ECMP","data": myResult})
        json.dump(output, outFile)

    outFile.close()

#end mytets


mytest("inflowmr20load4.json","outputCF.json","ECMP");
