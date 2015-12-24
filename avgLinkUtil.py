import sys
import os
import json



filename1 = "mr20load40/Host1/link_log.json"
filename2 = "mr20load40/Host2/link_log.json"
filename3 = "mr20load40/Host3/link_log.json"
filename4 = "mr20load40/Host4/link_log.json"


linkHost1 = []
timeHost1 = []

linkHost2 = []
timeHost2 = []

linkHost3 = []
timeHost3 = []

linkHost4 = []
timeHost4 = []

avgLink = []
aveTime = []

output = []
arrayLinkUtil = []
ArrayTime = []
numbOfPkt_Array = []
myResult = []
myP = [2]



def mytest(type) :
    
    
    with open(filename1) as data_file :
        data = json.load(data_file)
        for line  in data:
            linkHost1.append(line["RX"])
            timeHost1.append(line["Time"])
        data_file.close()

    with open(filename2) as data_file2 :
        data = json.load(data_file2)
        for line  in data:
            linkHost2.append(line["RX"])
            timeHost2.append(line["Time"])
        data_file2.close()

    with open(filename3) as data_file3 :
        data = json.load(data_file3)
        for line  in data:
            linkHost3.append(line["RX"])
            timeHost3.append(line["Time"])
        data_file3.close()

    with open(filename2) as data_file4 :
        data = json.load(data_file4)
        for line  in data:
            linkHost4.append(line["RX"])
            timeHost4.append(line["Time"])
        data_file4.close()


    length = []
    
    length.append( len(linkHost1))
    length.append( len(linkHost2))
    length.append( len(linkHost3))
    length.append( len(linkHost4))

    length.sort()
    
    max_counter = length[0]
    
    totalUtil = 0; 
    i = 0
    while (i < max_counter-1):
        
        numbPkt1 = linkHost1[i+1] - linkHost1[i]
        numbPkt2 = linkHost2[i+1] - linkHost2[i]
        numbPkt3 = linkHost3[i+1] - linkHost3[i]
        numbPkt4 = linkHost4[i+1] - linkHost4[i]
        total =  numbPkt1 + numbPkt2 +numbPkt3 +numbPkt4
        avg_NumbPacket = total / 4;
        inBite = avg_NumbPacket * 1500 * 8
  
        interval1 = timeHost1[i+1] - timeHost1[i]
        interval2 = timeHost2[i+1] - timeHost2[i]
        interval3 = timeHost3[i+1] - timeHost3[i]
        interval4 = timeHost4[i+1] - timeHost4[i]
        total = interval1 +interval2 + interval3 + interval4
        avg_interval = total / 4
        
        avgBite = inBite / avg_interval


        time1 = timeHost1[i+1] 
        time2 = timeHost2[i+1] 
        time3 = timeHost3[i+1] 
        time4 = timeHost4[i+1] 

        total = time1 + time2 + time3 + time4
        avgCT = total / 4

        myP = [avgCT, avgBite]
        myResult.append(myP)
       
        i += 1
       
    myResult.sort()
    #print(myResult)
    
    #replace with outputFile
    with open('outputLB.json', 'w') as outFile:

        myType = "ECMP"
        output.append({"name": myType,"data": myResult})
        #output.append({"name":"ECMP","data": myResult})
        json.dump(output, outFile)

    outFile.close()

#end mytets



mytest("ECMP");
