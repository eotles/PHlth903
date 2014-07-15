'''
Created on Jul 15, 2014

@author: eotles
'''

import sys
import os
from __builtin__ import id

idDict = dict()

def main():
    if(len(sys.argv)!=2):
        print("incorrect usage - KinIbCoefFormatter needs one parameter\n"+
              "e.g. python KinIbCoefFormatter /dir/pedFile")

    pedFilePath = sys.argv[1]
    outputFilePath = os.getcwd()
    pedFile = open(pedFilePath, "r")
    outPedFile = open(outputFilePath + "/outPed", "w+")
    outListFile = open(outputFilePath + "/outList", "w+")
    idDict.update({"0":"0"})
    len(idDict)
    
    next(pedFile)
    #make new formatted files
    for line in pedFile:
        lineData = line.strip().split(",")
        convertLD(lineData)
        outPedFile.write(",".join(lineData[0:4])+"\n")
        outListFile.write(",".join(lineData[0:2])+"\n")
    
    #close files
    pedFile.close()
    outPedFile.close()
    outListFile.close()
    
def convert2intID(stringID):
    if(len(stringID)>1):
        intID = str(int(stringID[5:]))
        if not(idDict.has_key(intID)):
            idDict.update({intID : str(len(idDict))})
        return idDict.get(intID)
    else:
        return stringID

def convertLD(lineData):
    for i in xrange(1,4):
        lineData[i] = convert2intID(lineData[i])

if __name__ == '__main__':
    main()