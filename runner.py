'''
Created on Aug 5, 2014

@author: eotles
'''

#import argparse
import sys
import subprocess
from casel import autoCall as casel
from monsterFormatter import autoCall as monsterFormatter

def main():
    args = sys.argv[1:]
    caseFilepath = args[0]
    contFilepath = args[1]
    contRatio = args[2]
    kicFilepath = args[3]
    mapFilepath = args[4]
    
    selectedControlsList = casel(caseFilepath, contFilepath, contRatio, kicFilepath)
    monFiles = monsterFormatter(caseFilepath, contFilepath, kicFilepath, mapFilepath, selectedControlsList)
    
    #print(monFiles)
    print("run like this>>>> /project/EngelmanGroup/GAW19/MONSTER/scr/./MONSTER "+
          "-p %s -g %s -s %s -k %s" %("pheno.txt", "geno.txt", "SNP.txt", "kin.txt"))
    
    #subprocess.call(["/project/EngelmanGroup/GAW19/MONSTER/scr/./MONSTER"])
    

if __name__ == '__main__':
    main()