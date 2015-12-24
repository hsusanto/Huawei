import sys
import os
import json
import operator

output = []
averageFCT = []
arrayFCT = []
CT_flowArr = []
myResult = []
myP = [2]

myFCT = [2]
FCTArr = []

extenFN = ".json"
directory = "data/"

def mytest(inputFile,outputFile,expType) :

    with open(inputFile) as data_file :

        data = json.load(data_file)
        for line  in data:

            FCT = line["EndTime"] - line["StartTime"]
            myFCT = [line["EndTime"], FCT]
            FCTArr.append(myFCT)

        FCTArr.sort()

    data_file.close()

    i = 0
    totalFCT = 0
    while (i < len(FCTArr)):
        
        totalFCT = totalFCT +  FCTArr[i][1]
        avgFCT = totalFCT / (i+1)

        endtime = FCTArr[i][0]

        myP = [endtime, avgFCT]
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



mytest("inflowmr20load4.json" , "flowmr20load40-2.json","ECMP")

